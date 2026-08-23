#!/usr/bin/env python3
"""
PostToolUse hook: controleert Python code-blokken in markdown bestanden (en
markdown-cellen van notebooks) op syntaxfouten en opmaakproblemen (ruff).
Wordt automatisch uitgevoerd na Write en Edit tool-aanroepen.

Let op: dit controleert alleen ```python-fences in *prose* (markdown-tekst of
notebook-markdowncellen), niet de uitvoerbare code-cellen van een notebook.
Die laatste worden al gedekt door myst-nb's uitvoering tijdens de build, en
kunnen los gelint worden met ruffs eigen .ipynb-ondersteuning.
"""
import ast
import json
import os
import re
import subprocess
import sys
import tempfile


def markdown_from_notebook(filepath: str) -> str:
    """Voegt de bronnen van alle markdown-cellen van een notebook samen tot
    één tekst, zodat ```python-fences erin op dezelfde manier gecontroleerd
    kunnen worden als in een los .md-bestand."""
    with open(filepath, encoding="utf-8") as f:
        notebook = json.load(f)

    parts = []
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        source = cell.get("source", "")
        if isinstance(source, list):
            source = "".join(source)
        parts.append(source)

    return "\n\n".join(parts)


SKIP_MARKER = "<!-- codecontrole:skip -->"


def _has_skip_marker(content: str, block_start: int) -> bool:
    """Kijkt of de regel direct vóór een code-blok de skip-marker bevat.
    Hiermee kan je een blok dat *opzettelijk* ongeldige/niet-conventionele
    Python bevat (bijvoorbeeld een meerkeuzevraag over een indentatiefout)
    uitsluiten van de syntax- en opmaakcontrole."""
    preceding = content[:block_start].rstrip("\n")
    last_line = preceding.rsplit("\n", 1)[-1]
    return last_line.strip() == SKIP_MARKER


def extract_python_blocks(content: str) -> list[tuple[int, str]]:
    """Geeft lijst van (bloknummer, code) tuples terug. Blokken direct na
    `<!-- codecontrole:skip -->` worden overgeslagen."""
    blocks = []
    pattern = re.compile(r'```python\n(.*?)```', re.DOTALL)
    for i, match in enumerate(pattern.finditer(content), 1):
        if _has_skip_marker(content, match.start()):
            continue
        blocks.append((i, match.group(1)))
    return blocks


def is_partial_block(code: str) -> bool:
    """
    Partiële code-blokken zijn opzettelijk onvolledig. Herkent:
    - Code die start met inspringing (methodbody buiten klasse)
    - Code die begint met except/elif/else/finally (fragment van control flow)
    - Code die alleen een decorator toont zonder functiedefinitie
    - Een enkele regel die begint als een samengestelde instructie (if/for/
      while/etc.) zonder afsluitende dubbele punt en zonder body erna --
      een losstaand "kijk zo gebruik je deze clause"-hint, geen echte code
    """
    non_empty_lines = [l for l in code.splitlines() if l.strip() and not l.strip().startswith("#")]
    if not non_empty_lines:
        return False

    first = non_empty_lines[0]

    if first[0] in (" ", "\t"):
        return True

    if re.match(r"^(except|elif|else|finally)\b", first.strip()):
        return True

    if len(non_empty_lines) == 1:
        stripped = first.strip().rstrip("#").rstrip()
        if re.match(r"^(if|elif|else|for|while|try|with)\b", stripped) and not stripped.endswith(":"):
            return True

    if all(l.strip().startswith("@") for l in non_empty_lines):
        return True

    return False


def check_syntax(block_num: int, code: str) -> str | None:
    """Controleert syntaxfouten via ast.parse. Geeft foutmelding of None terug."""
    try:
        ast.parse(code)
        return None
    except SyntaxError as e:
        if "expected an indented block" in str(e.msg):
            lines = [l for l in code.splitlines() if l.strip()]
            if e.lineno and e.lineno >= len(lines):
                return None
        lines = code.splitlines()
        offending = lines[e.lineno - 1].strip() if e.lineno and e.lineno <= len(lines) else ""
        return f"Blok {block_num}, syntaxfout regel {e.lineno}: {e.msg}\n      → {offending}"


def run_ruff(args: list[str]) -> subprocess.CompletedProcess | None:
    """
    Voert ruff uit via uv run. Geeft None terug als ruff niet beschikbaar is.
    """
    try:
        return subprocess.run(
            ["uv", "run", "ruff"] + args,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return None


def check_ruff(block_num: int, code: str) -> list[str]:
    """
    Controleert opmaak via ruff format --check.
    Linting wordt overgeslagen: te veel false positives in losse code-blokken
    (F821 undefined names, etc. zijn onvermijdelijk buiten context).
    """
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False, encoding="utf-8") as f:
        f.write(code)
        tmpfile = f.name

    try:
        # exit 0 = al opgemaakt, exit 1 = wijkt af, exit 2 = fout/niet gevonden
        result = run_ruff(["format", "--check", "--quiet", tmpfile])
        if result is not None and result.returncode == 1:
            return [f"Blok {block_num}: opmaak wijkt af van ruff-standaard (run `ruff format`)"]
        return []
    finally:
        os.unlink(tmpfile)


def check_file(filepath: str) -> bool:
    """Controleert een bestand en print de resultaten. Geeft True terug als er problemen zijn."""
    is_notebook = filepath.endswith(".ipynb")
    if not (filepath.endswith(".md") or is_notebook):
        return False

    if not os.path.isfile(filepath):
        return False

    if is_notebook:
        try:
            content = markdown_from_notebook(filepath)
        except (json.JSONDecodeError, OSError):
            return False
    else:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()

    blocks = extract_python_blocks(content)
    if not blocks:
        return False

    syntax_errors = []
    ruff_issues = []
    checked = 0

    for block_num, code in blocks:
        if is_partial_block(code):
            continue

        checked += 1
        err = check_syntax(block_num, code)
        if err:
            syntax_errors.append(err)
        else:
            ruff_issues.extend(check_ruff(block_num, code))

    filename = os.path.basename(filepath)
    all_issues = syntax_errors + ruff_issues

    if all_issues:
        print(f"CODECONTROLE {filename}: {len(all_issues)} probleem/problemen gevonden:")
        for issue in all_issues:
            print(f"  - {issue}")
        print("  Corrigeer deze problemen voordat je verder gaat.")
        return True
    else:
        print(f"CODECONTROLE {filename}: {checked} blok(ken) gecontroleerd — syntax en opmaak ok.")
        return False


def main() -> None:
    # Pre-commit modus: bestandspaden als CLI-argumenten
    if sys.argv[1:]:
        has_errors = False
        for filepath in sys.argv[1:]:
            if check_file(filepath):
                has_errors = True
        sys.exit(1 if has_errors else 0)

    # Claude Code PostToolUse modus: bestandspad via JSON stdin
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        return

    tool_input = data.get("tool_input", {})
    filepath = tool_input.get("file_path", "")
    if filepath:
        check_file(filepath)


if __name__ == "__main__":
    main()

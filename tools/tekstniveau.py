#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11,<3.12"
# dependencies = [
#   "click==8.5.1",
#   "nbformat==5.11.1",
#   "numpy==1.26.4",
#   "pandas==3.0.6",
#   "pyyaml==6.0.3",
#   "spacy==3.7.5",
#   "lint-ii==0.1.3",
#   "nl-core-news-lg @ https://github.com/explosion/spacy-models/releases/download/nl_core_news_lg-3.7.0/nl_core_news_lg-3.7.0-py3-none-any.whl",
# ]
# [tool.uv]
# python-preference = "managed"
# ///
"""tekstniveau: position Dutch course texts against 2F, 3F and 4F reading levels.

Run with uv, which installs the dependencies on first use:

    uv run tekstniveau.py check FILE_OR_FOLDER...
    uv run tekstniveau.py brief --profile introduces [--file TEXT]
    uv run tekstniveau.py compare BEFORE AFTER

The term list defaults to the nearest conventies/begrippen.md above the working folder or this
file.
"""
from __future__ import annotations

import contextlib
import functools
import html
import json
import re
import statistics
import subprocess
import sys
import types
from collections import Counter
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable, Sequence

import click
import nbformat
import numpy as np
import pandas as pd
import yaml
from lint_ii import ReadabilityAnalysis
from lint_ii.core.lint_scorer import LintScorer
from lint_ii.core.preprocessor import preprocess_text
from lint_ii.core.sentence_analysis import SentenceAnalysis
from lint_ii.linguistic_data.wordlists import FREQ_DATA
from spacy.tokens import Token


# ============================================================================
# connectives: Dutch connectives: words that make the relation between sentences and clauses explicit.
# ============================================================================

SINGLE = {
    # cause and result
    "omdat", "doordat", "want", "daardoor", "daarom", "dus", "zodat", "waardoor", "aangezien",
    # contrast
    "maar", "echter", "toch", "hoewel", "terwijl", "ofschoon", "daarentegen", "anderzijds",
    # condition and time
    "als", "wanneer", "indien", "zodra", "nadat", "voordat", "totdat", "sinds", "daarna",
    "vervolgens", "eerst", "tenslotte", "uiteindelijk", "intussen",
    # addition, example and summary
    "bovendien", "daarnaast", "verder", "bijvoorbeeld", "kortom", "namelijk", "oftewel",
}
MULTI = {("ten", "slotte"), ("met", "andere", "woorden"), ("dat", "wil", "zeggen"), ("met", "name"), ("in", "plaats", "van")}


def count(tokens: Sequence[Token]) -> int:
    words = [t.lower_ for t in tokens]
    n = 0
    taken: set[int] = set()
    for phrase in MULTI:
        k = len(phrase)
        for i in range(len(words) - k + 1):
            if tuple(words[i:i + k]) == phrase and not taken & set(range(i, i + k)):
                taken |= set(range(i, i + k))
                n += 1
    for i, t in enumerate(tokens):
        if i in taken or words[i] not in SINGLE:
            continue
        if words[i] == "als" and not _opens_clause(tokens, i):
            continue
        n += 1
    return n


def _opens_clause(tokens: Sequence[Token], i: int) -> bool:
    """Whether "als" opens a clause ("als de lijst leeg is"), rather than comparing or naming
    a role ("groter als", "als vervanging"). spaCy tags all of these the same way, so look
    for a verb before the next comma or full stop."""
    for t in tokens[i + 1:]:
        if t.is_punct:
            return False
        if t.pos_ in {"VERB", "AUX"}:
            return True
    return False


def per_100_words(sentences: Iterable[Sequence[Token]]) -> float:
    total = words = 0
    for tokens in sentences:
        total += count(tokens)
        words += sum(t.is_alpha for t in tokens)
    return 100 * total / words if words else 0.0

connectives = types.SimpleNamespace(MULTI=MULTI, SINGLE=SINGLE, count=count, per_100_words=per_100_words)


# ============================================================================
# terms: Load the term list: protected terms and rejected variants.
# ============================================================================

WE_WRITE = "wij schrijven"
ALSO_FOUND = "ook aangetroffen"
ENGLISH_SECTION = "Engelse termen die we niet vertalen"
NOTES = "toelichting"
NEW_IN = r"Nieuw in (PGM\d+ week \d+)"


class TermListError(ValueError):
    """The term list can't be read, usually because its format changed."""


@dataclass(frozen=True)
class TermSource:
    """Where a term list came from, so a result can be traced to one version of it."""

    path: Path
    commit: str | None  # last commit that touched the file; None if untracked or outside git
    modified: bool  # uncommitted changes, or not committed at all

    def as_dict(self) -> dict:
        return {"path": str(self.path), "commit": self.commit, "modified": self.modified}


@dataclass
class TermList:
    protected: set[str] = field(default_factory=set)
    rejected: set[str] = field(default_factory=set)
    sources: list[TermSource] = field(default_factory=list)
    replacements: dict[str, str] = field(default_factory=dict)  # rejected variant -> listed term
    introduced: dict[str, str] = field(default_factory=dict)  # term -> where it's new, such as "PGM2 week 5"

    def merge(self, other: TermList) -> TermList:
        protected = self.protected | other.protected
        rejected = (self.rejected | other.rejected) - protected
        replacements = {**self.replacements, **other.replacements}
        return TermList(
            protected=protected,
            rejected=rejected,
            sources=self.sources + other.sources,
            replacements={v: r for v, r in replacements.items() if v in rejected},
            introduced={**self.introduced, **other.introduced},
        )

    @property
    def modified(self) -> bool:
        return any(s.modified for s in self.sources)


def _normalise(term: str) -> str:
    return re.sub(r"\s+", " ", term.strip().lower())


def _table_rows(text: str):
    """Yield each Markdown table as (lower-case header, rows of cells)."""
    header: list[str] | None = None
    rows: list[list[str]] = []
    for line in text.splitlines() + [""]:
        if not line.lstrip().startswith("|"):
            if header:
                yield header, rows
            header, rows = None, []
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if set("".join(cells)) <= set("-: "):
            continue  # separator row
        if header is None:
            header = [c.lower() for c in cells]
        elif len(cells) == len(header):
            rows.append(cells)


def parse_begrippen(path: Path) -> TermList:
    """Read the course's begrippen.md.

    - Protected: the bold terms in the "Wij schrijven" column, and the code-formatted
      terms in the section on English terms that aren't translated.
    - Rejected: the comma-separated variants in "Ook aangetroffen", without the counts
      and notes in brackets.
    - Introduced: terms whose "Toelichting" says "Nieuw in PGM2 week 5" or similar.
    """
    text = Path(path).read_text(encoding="utf-8")
    protected: set[str] = set()
    rejected: set[str] = set()
    replacements: dict[str, str] = {}
    introduced: dict[str, str] = {}
    found_table = False
    for header, rows in _table_rows(text):
        if WE_WRITE not in header:
            continue
        found_table = True
        we_write = header.index(WE_WRITE)
        also_found = header.index(ALSO_FOUND) if ALSO_FOUND in header else None
        notes = header.index(NOTES) if NOTES in header else None
        for cells in rows:
            row_terms = [_normalise(t) for t in re.findall(r"\*\*(.+?)\*\*", cells[we_write])]
            protected |= set(row_terms)
            new = re.search(NEW_IN, cells[notes]) if notes is not None else None
            if new:
                introduced.update({term: new.group(1) for term in row_terms})
            if also_found is None:
                continue
            cell = re.sub(r"\([^)]*\)", "", cells[also_found])
            for variant in cell.split(","):
                variant = _normalise(variant.replace("`", ""))
                if variant and variant != "-":
                    rejected.add(variant)
                    if row_terms:
                        replacements.setdefault(variant, row_terms[0])

    if not found_table:
        raise TermListError(f"{path}: no table with a '{WE_WRITE}' column; has the format changed?")
    section = re.search(rf"^##\s+{ENGLISH_SECTION}\s*$(.*?)(?=^##\s|\Z)", text, re.M | re.S)
    if section:
        protected |= {_normalise(t) for t in re.findall(r"`([^`]+)`", section.group(1))}

    protected.discard("")
    rejected -= protected
    replacements = {v: r for v, r in replacements.items() if v in rejected}
    return TermList(protected, rejected, [source_of(path)], replacements, introduced)


def load_extra(path: Path) -> TermList:
    """Read an extra term list in YAML:

    ```yaml
    protected: [state machine, docstring]
    rejected: [returnen]
    ```
    """
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict) or set(data) - {"protected", "rejected"}:
        raise TermListError(f"{path}: expected only the keys 'protected' and 'rejected'")
    lists = {}
    for key in ("protected", "rejected"):
        values = data.get(key) or []
        if not isinstance(values, list) or not all(isinstance(v, str) for v in values):
            raise TermListError(f"{path}: '{key}' must be a list of strings")
        lists[key] = {_normalise(v) for v in values} - {""}
    return TermList(lists["protected"], lists["rejected"] - lists["protected"], [source_of(path)])


def load_terms(begrippen: Path, extra: Path | None = None) -> TermList:
    terms = parse_begrippen(begrippen)
    return terms.merge(load_extra(extra)) if extra else terms


def source_of(path: Path) -> TermSource:
    path = Path(path).resolve()

    def git(*args: str) -> str | None:
        try:
            result = subprocess.run(
                ["git", "-C", str(path.parent), *args], capture_output=True, text=True, check=True
            )
        except (OSError, subprocess.CalledProcessError):
            return None
        return result.stdout.strip()

    commit = git("log", "-1", "--format=%H", "--", path.name) or None
    status = git("status", "--porcelain", "--", path.name)
    modified = commit is None or bool(status)
    return TermSource(path, commit, modified)


# ============================================================================
# matching: Find protected terms and rejected variants in spaCy tokens.
# ============================================================================

SEPARABLE = ("aan", "af", "uit", "mee", "terug", "op", "in", "over", "door", "om", "toe", "voor")
VOWELS = "aeiou"
VERB_POS = {"VERB", "AUX"}
ORDINARY_FREQUENCY = 3.0  # log10 per billion words in SUBTLEX-NL: about 1 per million
# A past participle such as "geprint" or "afgedrukt": a verb form, like the infinitives.
PARTICIPLE = re.compile(rf"^(?:{'|'.join(SEPARABLE)})?ge[^\W\d_]{{2,}}[td]$")


def inflections(term: str) -> set[str]:
    """Generate common Dutch forms of a single-word term."""
    forms = {term}
    if " " in term:
        return forms
    if term.endswith("en") and len(term) > 4:  # verb: aanroepen, afdrukken, teruggeven
        stem = term[:-2]
        if len(stem) > 2 and stem[-1] == stem[-2] and stem[-1] not in VOWELS:
            stem = stem[:-1]  # afdrukk -> afdruk
        if stem[-1] == "v":
            stem = stem[:-1] + "f"
        elif stem[-1] == "z":
            stem = stem[:-1] + "s"
        prefix = separable_prefix(term)
        base = stem[len(prefix):]
        full_base = term[len(prefix):-2]
        forms |= {stem, stem + "t", stem + "d", stem + "de", stem + "te", stem + "ten", stem + "den"}
        forms |= {prefix + "ge" + base + "t", prefix + "ge" + base + "d", prefix + "ge" + full_base + "en"}
        forms |= {prefix + "ge" + base + "te", prefix + "ge" + base + "de"}
        return forms
    forms |= {term + "s", term + "en", term + "'s", term + "je", term + "jes"}
    if len(term) > 2 and term[-1] == "y" and term[-2] not in VOWELS:
        forms.add(term[:-1] + "ies")  # English plural: dictionary -> dictionaries
    if term.endswith("e"):
        forms |= {term + "n", term + "s"}
    if len(term) > 2 and term[-1] not in VOWELS and term[-2] in VOWELS and term[-3] not in VOWELS:
        forms |= {term + term[-1] + "en"}  # lus -> lussen
    return forms


def separable_prefix(term: str) -> str:
    return next((p for p in SEPARABLE if term.startswith(p) and len(term) > len(p) + 3), "")


def is_verb_term(term: str) -> bool:
    """An infinitive such as "aanroepen" or a participle such as "geprint"."""
    return (term.endswith("en") and len(term) > 4) or bool(PARTICIPLE.match(term))


@dataclass(frozen=True)
class Hit:
    term: str  # the listed term, in its base form
    positions: tuple[int, ...]  # positions in the token sequence; not adjacent for "roep ... aan"


@dataclass(frozen=True)
class VariantHit(Hit):
    ordinary_word: bool  # also an ordinary Dutch word, so it may be used in its normal sense

    @property
    def severity(self) -> str:
        return "warning" if self.ordinary_word else "error"


class _Forms:
    """Lookup from inflected forms to the terms they belong to."""

    def __init__(self, terms: set[str]) -> None:
        self.single: dict[str, str] = {}
        for term in sorted(t for t in terms if " " not in t):
            for form in inflections(term):
                self.single.setdefault(form, term)
        self.multi: dict[tuple[str, ...], str] = {}
        for term in sorted(t for t in terms if " " in t):
            *head, last = term.split()
            for form in inflections(last):
                self.multi.setdefault((*head, form), term)

    def word(self, token: Token) -> str | None:
        for candidate in (token.lower_, token.lemma_.lower()):
            term = self.single.get(candidate)
            # a nominal term such as "staat" must not match the verb "staat"
            if term and (is_verb_term(term) or token.pos_ not in VERB_POS):
                return term
        return None

    def phrases(self, tokens: Sequence[Token]) -> list[Hit]:
        texts = [t.lower_ for t in tokens]
        hits = []
        for phrase, term in self.multi.items():
            n = len(phrase)
            for i in range(len(texts) - n + 1):
                if tuple(texts[i:i + n]) == phrase:
                    hits.append(Hit(term, tuple(range(i, i + n))))
        return hits

    def separated(self, tokens: Sequence[Token]) -> list[Hit]:
        """Separable verbs split over a sentence: "roep de functie aan"."""
        index = {t.i: n for n, t in enumerate(tokens)}
        hits = []
        for n, particle in enumerate(tokens):
            if particle.dep_ != "compound:prt" or particle.head.i not in index:
                continue
            verb = particle.head
            for candidate in (particle.lower_ + verb.lemma_.lower(), particle.lower_ + verb.lower_):
                term = self.single.get(candidate)
                if term and is_verb_term(term) and separable_prefix(term) == particle.lower_:
                    hits.append(Hit(term, tuple(sorted((n, index[verb.i])))))
                    break
        return hits


class TermMatcher:
    """Finds protected terms, including inflections, compounds and separated verbs."""

    def __init__(self, terms: TermList) -> None:
        self.terms = terms
        self._protected = _Forms(terms.protected)
        self._rejected = _Forms(terms.rejected)
        bases = {t for t in terms.protected if " " not in t and len(t) >= 5}
        # each base term with its inflected forms, longest form first: "subdirectories"
        self._base_forms = sorted(
            ((form, term) for term in bases for form in inflections(term) if len(form) >= 5),
            key=lambda ft: (-len(ft[0]), ft[0]),
        )

    def _compound(self, token: Token) -> str | None:
        text = token.lower_
        parts = text.split("-")
        if len(parts) > 1:
            for part in parts:
                if part in self._protected.single:
                    return self._protected.single[part]
        # compounds such as "stringvariabele": the remainder must be a real word,
        # so "object" doesn't match "objectief" and "waarde" doesn't match "waarderen"
        for form, term in self._base_forms:
            if len(text) <= len(form) + 2:
                continue
            if text.endswith(form) and text[:-len(form)] in FREQ_DATA:
                return term
            if form == term and text.startswith(term) and text[len(term):] in FREQ_DATA and token.pos_ in {"NOUN", "PROPN"}:
                return term
        return None

    def protected(self, tokens: Sequence[Token]) -> list[Hit]:
        """Return each protected term found, longest match first where they overlap."""
        hits = self._protected.phrases(tokens) + self._protected.separated(tokens)
        taken = {p for h in hits for p in h.positions}
        for n, token in enumerate(tokens):
            if n in taken:
                continue
            term = self._protected.word(token) or self._compound(token)
            if term:
                hits.append(Hit(term, (n,)))
        return sorted(hits, key=lambda h: h.positions)

    def protected_positions(self, tokens: Sequence[Token]) -> set[int]:
        return {p for h in self.protected(tokens) for p in h.positions}

    def rejected(self, tokens: Sequence[Token]) -> list[VariantHit]:
        """Return rejected variants, ignoring any that are part of a protected term."""
        taken = self.protected_positions(tokens)
        candidates = self._rejected.phrases(tokens) + self._rejected.separated(tokens)
        candidates += [
            Hit(term, (n,)) for n, t in enumerate(tokens) if (term := self._rejected.word(t))
        ]
        hits, seen = [], set()
        for hit in sorted(candidates, key=lambda h: (h.positions, -len(h.positions))):
            if taken & set(hit.positions) or seen & set(hit.positions):
                continue
            seen |= set(hit.positions)
            hits.append(VariantHit(hit.term, hit.positions, self.is_ordinary(hit.term)))
        return hits

    @staticmethod
    def is_ordinary(variant: str) -> bool:
        """Whether every word of a variant is common in SUBTLEX-NL.

        SUBTLEX-NL comes from subtitles and holds English words too, so being listed isn't
        enough: "base case" is listed, but "base" is too rare to count as ordinary Dutch.
        """
        return all(FREQ_DATA.get(w, 0.0) >= ORDINARY_FREQUENCY for w in variant.split())


# ============================================================================
# reader: Turn a MyST Markdown file or a Jupyter notebook into prose for LiNT-II.
# ============================================================================

PLACEHOLDER = "Pyx"  # stands in for inline code and math, so sentences stay intact

PROSE_DIRECTIVES = {
    "admonition", "note", "tip", "warning", "important", "hint", "attention", "caution",
    "danger", "error", "seealso", "dropdown", "tab-set", "tab-item", "card", "grid",
    "grid-item", "grid-item-card", "margin", "sidebar", "topic", "epigraph",
}
REMOVE_TAGS = {"remove-cell", "remove_cell"}
SUFFIXES = {".md", ".ipynb"}

_FENCE = re.compile(r"^(`{3,}|~{3,}|:{3,})\s*(?:\{([\w-]+)\})?")
_LIST_ITEM = re.compile(r"^\s*([-*+]|\d+[.)])\s+\S")


@dataclass
class _Fence:
    char: str
    length: int
    prose: bool

    def closed_by(self, line: str) -> bool:
        return len(line) >= self.length and set(line) == {self.char}


def _is_markup_line(line: str) -> bool:
    return (
        line.startswith("|")  # table row
        or line.startswith("+++")  # MyST block break
        or bool(re.match(r"^\(.+\)=$", line))  # label target
        or bool(re.match(r"^:[\w-]+:", line)) and not line.startswith(":::")  # directive option
    )


def _clean_inline(line: str) -> str:
    line = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", line)  # images
    line = re.sub(r"\[\^[^\]]+\]:?\s*", "", line)  # footnote references and labels
    line = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line)  # links keep their text
    line = re.sub(r"\{[\w:-]+\}`([^`]*)`", r"\1", line)  # roles keep their text
    line = re.sub(r"`[^`]+`", PLACEHOLDER, line)
    line = re.sub(r"\$[^$\n]+\$", PLACEHOLDER, line)
    line = re.sub(r"</?[a-zA-Z][^>]*>", "", line)
    line = html.unescape(line).replace("\u2003", " ").replace("\u00a0", " ")  # &emsp;, &nbsp;
    # list items often have no full stop, which would merge them into one sentence
    if _LIST_ITEM.match(line) and not re.search(r"[.!?:;]\s*$", line):
        line = line.rstrip() + "."
    return line


def clean_markdown(text: str) -> str:
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    kept: list[str] = []
    fences: list[_Fence] = []
    in_math = False
    for line in text.splitlines():
        stripped = line.strip()
        if fences and fences[-1].closed_by(stripped):
            fences.pop()
            continue
        if fences and not fences[-1].prose:
            continue  # inside code or a non-prose directive: only its closing fence matters
        if in_math:
            in_math = not stripped.endswith("$$")
            continue
        if stripped.startswith("$$"):
            in_math = not (len(stripped) > 2 and stripped.endswith("$$"))
            continue
        opening = _FENCE.match(stripped)
        if opening:
            marker, name = opening.groups()
            # an unnamed colon fence wraps prose; an unnamed backtick fence is code
            prose = name in PROSE_DIRECTIVES if name else marker[0] == ":"
            fences.append(_Fence(marker[0], len(marker), prose))
            continue
        if _is_markup_line(stripped):
            continue
        kept.append(_clean_inline(line))
    return "\n".join(kept)


def file_settings(path: Path) -> dict:
    """Settings a file sets for this tool, under the key `tekstniveau`.

    In MyST front matter:

        ---
        tekstniveau:
          profile: practises
        ---

    In a notebook, the same key in the notebook metadata.
    """
    path = Path(path)
    if path.suffix == ".ipynb":
        settings = nbformat.read(path, as_version=4).metadata.get("tekstniveau")
    else:
        match = re.match(r"\A---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
        front = yaml.safe_load(match.group(1)) if match else None
        settings = front.get("tekstniveau") if isinstance(front, dict) else None
    return dict(settings) if isinstance(settings, dict) else {}


def read_course_file(path: Path) -> str:
    """Return the prose of a course file, ready for LiNT-II."""
    path = Path(path)
    if path.suffix == ".ipynb":
        nb = nbformat.read(path, as_version=4)
        cells = [
            clean_markdown(c.source) for c in nb.cells
            if c.cell_type == "markdown" and not set(c.metadata.get("tags", [])) & REMOVE_TAGS
        ]
        return "\n\n".join(cells)
    if path.suffix == ".md":
        return clean_markdown(path.read_text(encoding="utf-8"))
    raise ValueError(f"{path}: expected one of {sorted(SUFFIXES)}")


# ============================================================================
# scoring: Score a text with LiNT-II, ignoring fragments under 4 words.
# ============================================================================

MIN_SENTENCE_WORDS = 4


@dataclass(frozen=True)
class TextScore:
    score: float  # LiNT-II score, undiscounted
    lint_level: int  # LiNT level 1-4, not an F-level
    word_freq: float | None  # mean log frequency of content words
    max_sdl: float | None  # mean of each sentence's longest dependency length
    content_per_clause: float | None
    prop_concrete: float | None
    sentences: int  # sentences scored
    fragment_share: float  # share of sentences left out as fragments
    sentence_len: float  # words per sentence; feedback only, not a LiNT-II input
    word_len: float  # letters per word; feedback only
    connectives_per_100: float  # feedback only; see connectives.py

    def as_dict(self) -> dict:
        return asdict(self)


def word_count(sentence: SentenceAnalysis) -> int:
    return sum(t.is_alpha for t in sentence.doc)


def scored_sentences(analysis: ReadabilityAnalysis) -> list[SentenceAnalysis]:
    return [s for s in analysis.sentences if word_count(s) >= MIN_SENTENCE_WORDS]


def features(
    sentences: Sequence[SentenceAnalysis],
    terms: Sequence[set[int]] | None = None,
    floor: float | None = None,
) -> dict[str, float | None]:
    """The four LiNT-II inputs.

    With `terms`, the positions of listed terms per sentence, the term rules apply: a term's
    frequency is raised to `floor`, and terms are left out of the concrete-noun share.
    Dependency length and content words per clause don't change, because terms don't
    change sentence structure.
    """
    freqs, concrete, total = [], 0, 0
    for n, sentence in enumerate(sentences):
        hits = terms[n] if terms else set()
        for i, w in enumerate(sentence.word_features):
            if w.token.text == PLACEHOLDER:
                continue
            freq = w.word_frequency
            if freq is not None:
                freqs.append(max(freq, floor) if i in hits and floor is not None else freq)
            if i in hits:
                continue
            concrete += w.is_concrete
            total += w.is_concrete + w.is_abstract + w.is_undefined
    sdl = [s.max_sdl for s in sentences if s.max_sdl is not None]
    density = [s.content_words_per_clause for s in sentences if s.content_words_per_clause is not None]
    return {
        "word_freq": statistics.mean(freqs) if freqs else None,
        "max_sdl": statistics.mean(sdl) if sdl else None,
        "content_per_clause": statistics.mean(density) if density else None,
        "prop_concrete": concrete / total if total else None,
    }


def lint(values: dict[str, float | None]) -> LintScorer:
    return LintScorer(
        freq_log=values["word_freq"],
        max_sdl=values["max_sdl"],
        content_words_per_clause=values["content_per_clause"],
        proportion_concrete=values["prop_concrete"],
    )


def score_analysis(analysis: ReadabilityAnalysis) -> TextScore | None:
    """Score an existing analysis; None if no sentence has enough words."""
    sentences = scored_sentences(analysis)
    if not sentences:
        return None
    values = features(sentences)
    result = lint(values)
    if result.score is None:
        return None
    words = [t for s in sentences for t in s.doc if t.is_alpha]
    return TextScore(
        score=result.score,
        lint_level=result.level,
        sentences=len(sentences),
        fragment_share=1 - len(sentences) / len(analysis.sentences),
        sentence_len=len(words) / len(sentences),
        word_len=statistics.mean(len(t.text) for t in words) if words else 0.0,
        connectives_per_100=connectives.per_100_words(list(s.doc) for s in sentences),
        **values,
    )


# ============================================================================
# feedback: Feedback for writers: what to change, worded around what the writer can change.
# ============================================================================

@dataclass(frozen=True)
class Feature:
    name: str
    coefficient: str  # key in LiNT-II's coefficients
    easier_when_higher: bool
    label: str
    advice: str


FEATURES = [
    Feature("max_sdl", "mean_max_sdl", False, "dependency length",
            "Keep related words close: put the verb near its subject and object, move long "
            "insertions to their own sentence, and split sentences that carry two ideas."),
    Feature("content_per_clause", "mean_content_words", False, "content words per clause",
            "Give each clause one idea: spread information over more clauses, and unpack long "
            "noun phrases into a clause with a verb."),
    Feature("word_freq", "mean_log_word_freq", True, "word frequency",
            "Use everyday words for everything that isn't a listed term."),
    Feature("prop_concrete", "proportion_concrete", True, "concrete-noun share",
            "Use concrete examples: name things a student can picture or type, such as a "
            "list of names or a file on disk, around the abstract ideas."),
]
CONNECTIVE_EXAMPLES = "omdat, daardoor, zodat, maar, terwijl, als, daarna, bijvoorbeeld"


def coefficients() -> dict[str, float]:
    from lint_ii.linguistic_data.nlp_model import COEFFICIENTS

    return COEFFICIENTS


def points(feature: Feature, value: float, target: float) -> float:
    """Score points gained by moving a feature from `value` to `target`."""
    # score = 100 - (const + sum(coef * feature)), so a change in a feature moves the score by -coef
    return abs(coefficients()[feature.coefficient] * (value - target))


def gap(feature: Feature, value: float, target_range: tuple[float, float]) -> float:
    """How far a value is beyond its target range, on the harder side; 0 if not beyond."""
    lo, hi = target_range
    return max(lo - value, 0.0) if feature.easier_when_higher else max(value - hi, 0.0)


def messages(result: dict, replacements: dict[str, str]) -> list[str]:
    """Plain feedback for a check result, most important first."""
    lint, limit, terms = result["lint"], result["limit"], result["terms"]
    score, over, cost = lint["score"], limit["over_by"], lint["term_cost"]
    out = []
    if limit["status"] == "over":
        out.append(
            f"Score {score}, limit {limit['score']} ({limit['reference']}): over by {over}. "
            f"Listed terms account for {cost} points and stay, so reduce the rest by about {over} points."
        )
    elif limit["status"] == "borderline":
        if over > 0:
            out.append(
                f"Score {score} is just over the limit {limit['score']} ({limit['reference']}), within its "
                f"uncertainty ({limit['interval'][0]}-{limit['interval'][1]}). Small changes are enough: about {over} points."
            )
        else:
            out.append(
                f"Score {score} is just under the limit {limit['score']} ({limit['reference']}), within its "
                "uncertainty. Don't make the text harder."
            )
    else:
        out.append(f"Score {score} is under the limit {limit['score']} ({limit['reference']}); no rewrite is needed for difficulty.")

    needs_easing = limit["status"] != "under"
    for g in result["gaps"]:
        if g["caused_by_terms"]:
            out.append(f"The {g['label']} is outside its target only because of listed terms; that's expected, and the terms stay.")
        elif needs_easing and g["points"] >= 0.3:
            lo, hi = g["target_range"]
            out.append(
                f"{g['label'].capitalize()}: {g['value']}, against a target of {lo}-{hi}. {g['advice']} "
                f"Worth up to about {g['points']} points."
            )
    if needs_easing and not any(g["points"] >= 0.3 and not g["caused_by_terms"] for g in result["gaps"]):
        out.append("No single feature stands out: make small improvements across sentences, starting with the hardest ones below.")

    c = result["connectives"]
    if c["per_100_words"] < c["target_range"][0]:
        out.append(
            f"Few connectives: {c['per_100_words']} per 100 words, against a target of "
            f"{c['target_range'][0]}-{c['target_range'][1]}. Link sentences with words like {CONNECTIVE_EXAMPLES}. "
            "Don't reach a lower score by chopping sentences into fragments."
        )
    for p in terms["dense_paragraphs"]:
        out.append(
            f"Paragraph {p['paragraph']} has {p['terms']} terms in {p['words']} words. Introduce terms one at a "
            f"time, with an example in between. Paragraph start: \"{p['start']}\""
        )
    if terms["unexplained_at_first_use"]:
        out.append("Check that these terms are explained briefly at first use; no explanation was recognised: "
                   + ", ".join(terms["unexplained_at_first_use"]) + ". Marking the explanation in bold also counts.")
    errors = [v for v in terms["rejected_variants"] if v["severity"] == "error"]
    warnings = [v for v in terms["rejected_variants"] if v["severity"] == "warning"]
    if errors:
        out.append("Use the listed term instead of a rejected variant: "
                   + ", ".join(_replacement(v["variant"], replacements) for v in errors) + ".")
    if warnings:
        out.append("Check whether these words mean the listed concept; if so, use the listed term: "
                   + ", ".join(_replacement(v["variant"], replacements) for v in warnings) + ".")
    if terms["unlisted_rare_words"]:
        words = ", ".join(w["word"] for w in terms["unlisted_rare_words"][:10])
        out.append(f"Rare words not on the term list: {words}. Use a common word, or add the word to the term list if it's a course term.")
    rounds = result.get("round")
    if rounds and rounds["stop"]:
        out.append(f"This is round {rounds['round']} of at most {rounds['max']}: stop rewriting, and have a person review the text.")
    return out


def _replacement(variant: str, replacements: dict[str, str]) -> str:
    term = replacements.get(variant)
    return f"{variant} → {term}" if term else variant


# ============================================================================
# profiles: Target profiles: which limit applies to a text, and where its default comes from.
# ============================================================================

# The single-file build puts profiles.yml here, so it needs no data file next to it.
EMBEDDED_PROFILES: str | None = """\
# Target profiles: editable configuration.
#
# A limit is a percentile of a reference level's scores, or its mean plus `sd` standard
# deviations, so it moves when the reference set changes. `source` is `exams` (the default,
# central exams) or `anchors` (texts that anchor the 2F and 3F levels).

profiles:
  introduces:  # concept-introducing text
    # The top of the 2F band: the anchor texts separate 2F from 3F cleanly, their 2F mean plus
    # 1 SD (about 45) is below the 3F range, and it's about the median of 2F exam texts.
    level: 2F
    source: anchors
    sd: 1
    # Orientation for the writer in the brief. F-levels describe readers: a text at the top of
    # the 2F range is easy for a 3F reader and still manageable for a 2F reader.
    guide: >-
      Aim for text a 3F reader handles easily and a 2F reader can still manage: the top of the
      2F range, not 3F.
  practises:  # practice texts: allowed up to the edge of the 2F range
    level: 2F
    source: anchors
    sd: 2
    guide: >-
      Aim for text a 3F reader handles comfortably: at most the upper edge of the 2F range.
  reference:  # enrichment and reference texts: up to the top of the 3F band
    level: 3F
    source: anchors
    sd: 1
    guide: >-
      Aim for text a 3F reader can handle: at most the top of the 3F range.

# Default profile per folder. A file can override it with `tekstniveau: {profile: ...}`
# in its front matter or notebook metadata.
folders:
  lectures: introduces
  problems: practises
  practicals: practises
  support: reference
  extra: reference

# Below this, warn about fragmented or choppy prose. It's a warning, not a limit.
lower_bound:
  level: 2F
  percentile: 10

# A score inside this interval around a limit counts as borderline. The interval comes from
# a bootstrap over exam booklets, because texts in one booklet aren't independent, or over
# anchor texts.
confidence: 0.95

# Scores of shorter texts are unreliable.
min_words: 150

# Feedback settings. These are starting values, not validated.
feedback:
  # Target ranges per feature: these percentiles of the exam texts at the profile's level
  # that score at or below its limit, whatever the limit's source.
  target_percentiles: [25, 75]
  hardest_sentences: 5
  # Warn about a paragraph of at least min_words words with more terms per 100 words.
  paragraph_term_load: 15
  paragraph_min_words: 25
  # Rewrite rounds before a person should take over.
  max_rounds: 3
"""
SOURCES = {"exams", "anchors"}


class ProfileError(ValueError):
    pass


@dataclass(frozen=True)
class Threshold:
    """A score taken from a reference set: a percentile, or the mean plus `sd` standard deviations.

    `source` is "exams" (the central exams) or "anchors" (texts that anchor the 2F and 3F levels).
    """
    level: str
    percentile: float | None = None
    sd: float | None = None
    source: str = "exams"

    def __post_init__(self):
        if (self.percentile is None) == (self.sd is None):
            raise ValueError(f"{self.level}: give either a percentile or sd, not both or neither")
        if self.source not in SOURCES:
            raise ValueError(f"unknown source {self.source!r}; expected one of {sorted(SOURCES)}")

    @property
    def label(self) -> str:
        """The threshold as shown in output, without its source."""
        stat = f"P{self.percentile:g}" if self.percentile is not None else f"mean{self.sd:+g} SD"
        return f"{self.level} {stat}"

    def of(self, values) -> float:
        """This threshold's statistic for a set of reference scores."""
        values = np.asarray(values, dtype=float)
        if self.percentile is not None:
            return float(np.percentile(values, self.percentile))
        return float(values.mean() + self.sd * values.std(ddof=1))

    @classmethod
    def parse(cls, data: dict) -> Threshold:
        unknown = set(data) - {"level", "percentile", "sd", "source"}
        if unknown:
            raise ValueError(f"unknown threshold settings {sorted(unknown)}")
        return cls(
            level=str(data["level"]),
            percentile=float(data["percentile"]) if "percentile" in data else None,
            sd=float(data["sd"]) if "sd" in data else None,
            source=str(data.get("source", "exams")),
        )


@dataclass(frozen=True)
class Feedback:
    target_percentiles: tuple[float, float] = (25, 75)
    hardest_sentences: int = 5
    paragraph_term_load: float = 15
    paragraph_min_words: int = 25
    max_rounds: int = 3


@dataclass(frozen=True)
class Profiles:
    limits: dict[str, Threshold]
    folders: dict[str, str]
    lower_bound: Threshold
    confidence: float
    min_words: int
    feedback: Feedback = Feedback()
    guides: dict[str, str] = field(default_factory=dict)  # writer orientation per profile

    @classmethod
    def parse(cls, text: str, path: str) -> Profiles:
        """Profiles from YAML text; `path` names it in errors."""
        data = yaml.safe_load(text)
        try:
            limits = {name: Threshold.parse({k: v for k, v in p.items() if k != "guide"})
                      for name, p in data["profiles"].items()}
            guides = {name: " ".join(str(p["guide"]).split()) for name, p in data["profiles"].items() if p.get("guide")}
            lower = data["lower_bound"]
            profiles = cls(
                limits=limits,
                folders=dict(data.get("folders") or {}),
                lower_bound=Threshold.parse(lower),
                confidence=float(data.get("confidence", 0.95)),
                min_words=int(data.get("min_words", 0)),
                feedback=_feedback(data.get("feedback") or {}),
                guides=guides,
            )
        except (KeyError, TypeError, ValueError) as e:
            raise ProfileError(f"{path}: {e!r}") from e
        unknown = set(profiles.folders.values()) - set(limits)
        if unknown:
            raise ProfileError(f"{path}: folders refer to unknown profiles {sorted(unknown)}")
        return profiles

    def limit(self, name: str) -> Threshold:
        if name not in self.limits:
            raise ProfileError(f"unknown profile {name!r}; expected one of {sorted(self.limits)}")
        return self.limits[name]

    def for_path(self, path: Path) -> str | None:
        """The default profile from the nearest folder with one."""
        for part in reversed(Path(path).parts[:-1]):
            if part in self.folders:
                return self.folders[part]
        return None


def builtin_profiles() -> Profiles:
    """The tool's own profiles."""
    return Profiles.parse(EMBEDDED_PROFILES, "built-in profiles")


def _feedback(data: dict) -> Feedback:
    unknown = set(data) - set(Feedback.__dataclass_fields__)
    if unknown:
        raise ValueError(f"unknown feedback settings {sorted(unknown)}")
    if "target_percentiles" in data:
        lo, hi = data["target_percentiles"]
        data = {**data, "target_percentiles": (float(lo), float(hi))}
    return Feedback(**data)


# ============================================================================
# reference: Reference score distributions: numbers and metadata only, never text.
# ============================================================================

LEVELS = ("2F", "3F", "4F")
# The single-file build puts the exam scores here, as CSV text, so it needs no data files next
# to it: level, score and the features feedback uses.
EMBEDDED_REFERENCE: dict[str, str] | None = {"exams": """\
level,score,word_freq,max_sdl,content_per_clause,prop_concrete,sentence_len,connectives_per_100
2F,32.143635,4.833027,7.051724,3.722024,0.588889,15.275862,2.595937
2F,35.659681,4.803720,7.161290,4.403226,0.520000,14.838710,3.695652
2F,37.144914,4.612257,6.666667,3.925397,0.508197,12.866667,2.245250
2F,37.328846,4.530086,5.514706,2.830729,0.294118,11.000000,4.411765
2F,37.413059,4.623386,6.187500,3.535714,0.368421,12.500000,3.000000
2F,37.615073,4.569269,7.122449,4.460993,0.657143,14.408163,2.691218
2F,38.370690,4.523227,6.333333,3.389815,0.408696,13.017544,3.638814
2F,40.155401,4.581270,7.804878,4.307692,0.529915,13.195122,2.772643
2F,40.218561,4.576733,8.433333,3.306944,0.435374,14.916667,3.687151
2F,41.089744,4.407585,6.183333,4.198830,0.477419,11.950000,2.649930
2F,41.110061,4.482630,7.500000,4.375000,0.556818,13.650000,3.113553
2F,41.420682,4.566969,8.181818,4.849928,0.590909,15.969697,3.605313
2F,42.394572,4.292066,5.958333,3.469203,0.381818,11.229167,3.339518
2F,42.613117,4.510421,8.345455,4.199686,0.490566,14.945455,3.163017
2F,42.615950,4.542687,7.203125,4.366120,0.365591,14.906250,2.096436
2F,42.692876,4.503816,8.233333,4.252874,0.489796,14.933333,2.343750
2F,43.227864,4.363630,7.450000,4.618644,0.586957,13.900000,3.117506
2F,43.305454,4.319765,6.884058,4.514925,0.555556,12.260870,3.191489
2F,43.721914,4.507598,8.203704,4.178105,0.406250,14.777778,3.007519
2F,44.198292,4.230139,6.071429,4.105392,0.448864,12.228571,2.219626
2F,44.849840,4.487830,8.875000,5.115705,0.574766,16.392857,2.396514
2F,44.918835,4.378295,7.322034,3.991379,0.352041,14.101695,2.764423
2F,45.181502,4.352184,8.431818,4.829457,0.610465,15.818182,3.304598
2F,45.369446,4.283680,6.101449,4.242537,0.342246,12.594203,2.186421
2F,45.651733,4.284159,8.333333,4.826543,0.644330,15.037037,1.970443
2F,45.865570,4.255481,7.222222,4.040936,0.423729,13.126984,3.385732
2F,45.964336,4.488164,8.750000,4.414848,0.380117,16.053571,2.447164
2F,46.037859,4.554598,8.604651,4.613492,0.320261,16.906977,2.751032
2F,46.197446,4.464789,9.347826,4.229630,0.422222,17.108696,2.922490
2F,46.303292,4.131024,6.666667,4.605000,0.564706,13.611111,1.496599
2F,46.960348,4.246036,6.958333,3.784524,0.297619,13.902778,2.797203
2F,46.990901,4.183635,8.377358,4.448718,0.613757,15.056604,2.506266
2F,47.163888,4.198576,7.071429,4.722222,0.497326,14.089286,2.408112
2F,47.732890,4.299444,9.207547,4.206731,0.487500,15.754717,2.994012
2F,48.248873,4.137888,6.645161,4.277778,0.380952,13.387097,2.891566
2F,48.862001,4.355504,7.562500,4.583333,0.248408,16.375000,2.162850
2F,49.091746,4.368063,8.608696,5.781061,0.517766,17.021739,2.937420
2F,50.087326,4.108047,8.750000,5.128472,0.647959,15.653846,2.825553
2F,50.134641,4.108831,7.481481,5.137821,0.516484,13.166667,2.531646
2F,50.170346,4.197098,7.510204,4.659091,0.345070,14.102041,1.736614
2F,52.702156,4.202351,8.675000,5.423423,0.421053,16.000000,1.875000
2F,54.325237,4.243301,9.114286,5.280952,0.296875,14.685714,4.085603
2F,54.439263,4.161494,8.135135,4.763889,0.196429,16.972973,3.025478
3F,35.173746,4.900415,8.533333,4.153846,0.545455,15.533333,2.575107
3F,37.722927,4.657376,6.548673,3.731481,0.380074,12.920354,2.123288
3F,38.348046,4.546756,6.673469,3.448582,0.428571,14.244898,3.008596
3F,40.527867,4.390400,6.733333,3.128205,0.416667,13.733333,3.398058
3F,40.716559,4.613492,8.416667,5.102778,0.648760,15.033333,2.549889
3F,42.952111,4.168617,5.152174,3.598291,0.419355,9.934783,2.188184
3F,43.351670,4.368663,8.000000,3.829928,0.504032,14.958763,2.136458
3F,44.968807,4.568984,9.605263,4.078968,0.388350,17.131579,2.764977
3F,45.229298,4.506172,9.452381,3.506098,0.333333,16.047619,3.857567
3F,45.709664,4.181733,7.916667,4.126488,0.597884,14.600000,2.625571
3F,45.847959,4.165445,6.061224,4.013605,0.400000,12.653061,2.741935
3F,46.411755,4.380317,7.952381,4.387500,0.383562,16.571429,3.448276
3F,46.572948,4.423133,7.404762,4.254274,0.250000,14.761905,3.548387
3F,46.707490,4.351961,8.259259,3.948889,0.357143,15.728395,1.883830
3F,47.019990,4.340335,7.791667,4.645833,0.413636,15.347222,2.171946
3F,47.099021,4.305293,7.296875,4.675000,0.400990,14.281250,2.297593
3F,48.152518,4.337166,7.200000,4.420930,0.250000,14.488889,2.760736
3F,48.370034,4.163780,8.261538,4.551913,0.553506,16.446154,2.432180
3F,49.690177,4.040420,6.047619,4.368421,0.350000,11.904762,2.000000
3F,49.797384,4.391905,8.325581,4.835366,0.268116,16.697674,2.785515
3F,50.265696,4.433641,8.781250,5.041667,0.272727,18.281250,2.393162
3F,51.083890,4.061454,7.880952,4.502137,0.447761,16.095238,2.514793
3F,51.271721,4.261812,9.453125,4.851190,0.434211,16.953125,2.211982
3F,51.443487,4.057971,7.234375,4.059836,0.292683,13.765625,3.291714
3F,51.451393,4.087567,5.773585,4.653061,0.205882,12.301887,2.607362
3F,51.939121,4.251970,8.612903,5.181034,0.370079,16.580645,1.945525
3F,52.351534,4.164334,7.744681,4.937500,0.312139,15.446809,2.203857
3F,53.009564,4.184644,11.066667,4.583333,0.530612,16.333333,2.040816
3F,54.705489,4.466823,12.461538,5.621795,0.425532,19.923077,4.633205
3F,55.080115,4.179913,8.200000,6.089744,0.354167,16.600000,3.162651
3F,55.310720,4.471671,11.921053,6.571930,0.478723,19.605263,2.953020
3F,56.308120,4.086909,9.604167,5.145390,0.370588,17.229167,2.176542
3F,56.846833,4.228520,8.628571,6.019048,0.223022,17.857143,1.600000
3F,58.015515,4.081120,7.820513,5.532895,0.150000,14.769231,2.604167
3F,66.391011,4.092857,11.187500,6.788889,0.155172,20.437500,3.058104
4F,37.245872,4.574605,5.750000,3.794643,0.428571,11.156250,2.521008
4F,38.704103,4.518298,6.400000,3.651010,0.441558,13.228571,3.671706
4F,41.052831,4.417821,6.200000,3.594340,0.373984,12.472727,2.332362
4F,41.685576,4.498313,8.823529,3.815476,0.549296,17.352941,3.389831
4F,42.362056,4.583938,7.142857,4.964286,0.425926,15.928571,2.690583
4F,44.541523,4.537673,8.029412,4.291667,0.322581,14.147059,3.534304
4F,45.114575,4.242221,7.727273,3.630851,0.471264,15.018182,2.058111
4F,45.648048,4.313741,7.702703,3.691429,0.367347,14.918919,3.985507
4F,45.687713,4.213097,7.774194,3.772222,0.494253,16.161290,3.792415
4F,46.060489,4.449175,9.000000,3.181373,0.245283,15.526316,3.728814
4F,46.415799,4.283307,8.285714,4.772222,0.583851,18.595238,1.024328
4F,46.602200,4.482366,6.941176,4.000000,0.096154,14.794118,3.578529
4F,46.699983,4.307647,7.125000,4.465409,0.372549,13.803571,2.069858
4F,47.968059,4.274670,8.403509,4.620440,0.483721,16.894737,2.388370
4F,48.052869,4.287518,7.111111,3.362179,0.132353,14.111111,1.574803
4F,48.707894,4.271293,7.541667,4.767021,0.376623,14.333333,2.906977
4F,48.863688,4.300603,7.866667,3.877778,0.226415,17.533333,0.380228
4F,49.665873,4.474442,10.721311,3.728202,0.254237,20.081967,3.591837
4F,49.840676,4.309091,8.352941,4.338235,0.278846,15.470588,2.471483
4F,50.453689,4.093327,7.363636,3.651042,0.264368,15.696970,5.019305
4F,51.333484,4.164622,9.879310,4.679697,0.551887,17.034483,2.732794
4F,51.986908,4.262953,9.362637,3.822700,0.215017,18.373626,2.631579
4F,52.240917,3.996516,7.276596,4.151852,0.328358,14.680851,4.202899
4F,53.027936,4.136446,9.298851,4.691057,0.418960,16.942529,1.696065
4F,53.459880,3.951924,8.843750,4.118280,0.454545,15.593750,2.605210
4F,54.217396,4.203050,10.312500,4.591111,0.359375,17.312500,2.166065
4F,55.050442,4.131135,12.326531,3.840217,0.470588,19.673469,2.178423
4F,55.622776,4.322201,10.500000,5.346591,0.281437,18.522727,1.349693
4F,55.932738,4.140626,9.333333,4.993421,0.284024,18.487179,1.525659
4F,57.906422,4.133530,9.636364,5.382576,0.260870,17.181818,2.910053
4F,59.559469,4.038619,10.611111,5.337438,0.352304,19.444444,1.942857
4F,62.061450,4.031671,9.722222,6.117647,0.236842,17.777778,2.187500
4F,62.127422,4.109002,12.019231,5.101307,0.220657,19.538462,1.673228
4F,66.798498,3.784196,12.181818,5.651515,0.384615,18.727273,0.970874
"""}
# ...and the finished limits, one per profile threshold and each anchor-based one: the
# threshold's settings with its score and interval. The build holds no anchor scores and no
# exam booklets, so it can't compute other intervals itself.
EMBEDDED_LIMITS: list[dict] | None = [
    {'threshold': {'level': '2F', 'source': 'anchors', 'sd': 1.0}, 'confidence': 0.95, 'score': 44.961681620883596, 'low': 40.742636238307725, 'high': 47.77893061420588},
    {'threshold': {'level': '2F', 'source': 'anchors', 'sd': 2.0}, 'confidence': 0.95, 'score': 50.11724442358537, 'low': 44.32636673561568, 'high': 53.343850267385186},
    {'threshold': {'level': '3F', 'source': 'anchors', 'sd': 1.0}, 'confidence': 0.95, 'score': 57.978536074574286, 'low': 55.028768106851885, 'high': 60.50166722672508},
]


@dataclass
class Reference:
    """Stored reference scores, one row per text, from the exams and, if built, the anchor texts.

    Methods default to the exam texts. Limits name their own source.
    """

    texts: pd.DataFrame
    # Finished limits for thresholds whose texts aren't stored: threshold -> (score, low, high)
    # at `confidence`.
    fixed: dict = field(default_factory=dict)

    def __post_init__(self):
        if "source" not in self.texts:
            self.texts = self.texts.assign(source="exams")

    def _rows(self, level: str, source: str) -> pd.DataFrame:
        return self.texts[(self.texts.level == level) & (self.texts.source == source)]

    def scores(self, level: str, column: str = "score", source: str = "exams") -> np.ndarray:
        values = self._rows(level, source)[column].dropna().to_numpy()
        if not len(values):
            raise KeyError(f"no {source} reference texts for level {level!r}")
        return np.sort(values)

    def mean(self, level: str, column: str, source: str = "exams") -> float:
        return float(self.scores(level, column, source).mean())

    def _fixed(self, threshold, confidence: float | None = None):
        for (t, c), values in self.fixed.items():
            if t == threshold and (confidence is None or c == confidence):
                return values
        return None

    def limit(self, threshold) -> float:
        """The score for a profile threshold: a percentile, or mean plus SDs, of its source."""
        fixed = self._fixed(threshold)
        if fixed is not None:
            return fixed[0]
        return threshold.of(self.scores(threshold.level, source=threshold.source))

    def describe(self, threshold) -> str:
        """The threshold in words, for a writer. Output names only exam texts as a source."""
        if threshold.source == "exams" and threshold.percentile is not None:
            return (f"the {threshold.label} of exam texts, easier than "
                    f"{100 - threshold.percentile:g}% of {threshold.level} exam texts")
        return ""

    def position(self, level: str, score: float, source: str = "exams") -> float:
        """Share of the level's reference texts that score lower; ties count half."""
        scores = self.scores(level, source=source)
        below = np.searchsorted(scores, score, side="left")
        ties = np.searchsorted(scores, score, side="right") - below
        return float((below + ties / 2) / len(scores))

    def target_range(
        self, level: str, limit: float, column: str, percentiles: tuple[float, float] = (25, 75),
    ) -> tuple[float, float]:
        """The middle range of a feature among the level's texts that score at or below `limit`."""
        texts = self.texts[(self.texts.level == level) & (self.texts.source == "exams") & (self.texts.score <= limit)]
        values = texts[column].dropna().to_numpy()
        if len(values) < 5:
            raise ValueError(f"only {len(values)} {level} texts at or below {limit:.1f}; too few for a target")
        lo, hi = np.percentile(values, percentiles)
        return float(lo), float(hi)

    def limit_interval(
        self, threshold, confidence: float = 0.95, n_boot: int = 2000, seed: int = 20261107,
    ) -> tuple[float, float]:
        """Bootstrap interval for a threshold, resampling whole booklets.

        Texts in one exam booklet share a test and an editor, so they aren't independent. Each
        anchor text is its own group. Groups are taken in order of their scores, not their
        labels, so the single-file build, which stores no booklet names, gives the same result.
        """
        fixed = self._fixed(threshold, confidence)
        if fixed is not None:
            return fixed[1], fixed[2]
        raise KeyError(f"no finished interval for {threshold.label} in this build")


def builtin_reference() -> Reference:
    """The tool's own reference: stored scores and, in the single-file build, finished limits."""
    from io import StringIO

    texts = pd.concat(
        [pd.read_csv(StringIO(csv)).assign(source=source) for source, csv in EMBEDDED_REFERENCE.items()],
        ignore_index=True,
    )
    fixed = {
        (Threshold.parse(d["threshold"]), d["confidence"]): (d["score"], d["low"], d["high"])
        for d in EMBEDDED_LIMITS or []
    }
    return Reference(texts, fixed=fixed)


# ============================================================================
# check: Check a course text: its position against exam texts, its profile limit and its term cost,
# ============================================================================

ADVISORY = "Position relative to exam texts; limits not validated for programming texts."
RARE_FREQUENCY = 3.0  # log10 per billion words: under about 1 per million
DEFINITION_AFTER = {"zijn", "heten", "noemen", "betekenen"}  # "een subklasse is ...", "X betekent ..."
DEFINITION_BEFORE = {"noemen", "heten"}  # "dat noemen we een subklasse", "dat heet een subklasse"
MIN_RANKED_WORDS = 8  # LiNT-II is unstable on very short sentences, so they aren't ranked


def _paragraph_spans(text: str) -> list[tuple[int, int]] | None:
    """Character spans of each paragraph in the text LiNT-II analyses, or None if they
    can't be located."""
    full = preprocess_text(text)
    spans, pos = [], 0
    for block in re.split(r"\n\s*\n", text):
        piece = preprocess_text(block).strip()
        if not piece:
            continue
        start = full.find(piece, pos)
        if start < 0:
            return None
        spans.append((start, start + len(piece)))
        pos = start + len(piece)
    return spans


def _emphasised(text: str) -> str:
    """All bold and italic spans in the Markdown, lower-cased and joined."""
    return " | ".join(m.group(2).lower() for m in re.finditer(r"(\*\*|\*|__|_)(?=\S)(.+?)(?<=\S)\1", text))


def _is_explained(tokens, hit: Hit, emphasised: str) -> bool:
    words = [tokens[p].lower_ for p in hit.positions]
    if " ".join(words) in emphasised or any(w in emphasised for w in words if len(w) > 3):
        return True
    first, last = hit.positions[0], hit.positions[-1]
    after = tokens[last + 1:last + 4]
    if after and after[0].text in {":", "("}:
        return True
    if any(t.lemma_.lower() in DEFINITION_AFTER or t.lower_ in {"heet", "is", "zijn"} for t in after[:2]):
        return True
    before = tokens[max(first - 4, 0):first]
    return any(t.lemma_.lower() in DEFINITION_BEFORE or t.lower_ == "heet" for t in before)


def _has_code(word: str) -> bool:
    """Whether a word holds inline code, such as "Pyx-statement" for "`if`-statement"."""
    return PLACEHOLDER in word.split("-")


def _sentence_score(sentence, fallback: dict, terms: set[int] | None = None, floor: float | None = None) -> float | None:
    """A sentence's LiNT-II score. A feature a sentence lacks, such as the concrete-noun share
    of a sentence without nouns, takes the text's value."""
    values = features([sentence], [terms] if terms is not None else None, floor)
    return lint({k: v if v is not None else fallback[k] for k, v in values.items()}).score


@dataclass
class Checker:
    matcher: TermMatcher
    reference: Reference
    profiles: Profiles

    @property
    def term_floor(self) -> float:
        """The neutral frequency for terms: the mean content-word frequency of 2F exam texts."""
        return self.reference.mean("2F", "word_freq")

    def check_text(self, text: str, profile: str, round_number: int | None = None) -> dict:
        limit = self.profiles.limit(profile)
        settings = self.profiles.feedback
        analysis = ReadabilityAnalysis.from_text(text)
        result = score_analysis(analysis)
        warnings = [ADVISORY]
        if self.matcher.terms.modified:
            warnings.append("The term list has uncommitted changes.")
        if result is None:
            return {"profile": profile, "lint": None, "warnings": warnings + ["No sentence of 4 words or more to score."]}

        sentences = scored_sentences(analysis)
        words = sum(word_count(s) for s in sentences)
        if words < self.profiles.min_words:
            warnings.append(f"Only {words} words; scores under {self.profiles.min_words} words are unreliable.")

        # terms, per sentence
        tokens_per_sentence = [[w.token for w in s.word_features] for s in sentences]
        hits_per_sentence = [self.matcher.protected(tokens) for tokens in tokens_per_sentence]
        positions = [{p for h in hits for p in h.positions} for hits in hits_per_sentence]
        term_counts = Counter(h.term for hits in hits_per_sentence for h in hits)
        variants, rare = Counter(), Counter()
        for tokens, taken, s in zip(tokens_per_sentence, positions, sentences):
            variant_positions = set()
            for hit in self.matcher.rejected(tokens):
                variants[(hit.term, hit.severity)] += 1
                variant_positions |= set(hit.positions)
            for i, w in enumerate(s.word_features):
                if i in taken or i in variant_positions or _has_code(w.token.text) or w.word_frequency is None:
                    continue
                if w.word_frequency < RARE_FREQUENCY:
                    rare[w.text] += 1  # as written: spaCy lemmas fail on many words ("kolommen" -> "kolomm")
        term_hits = sum(len(p) for p in positions)

        # scores
        score = result.score
        neutral = features(sentences, positions, self.term_floor)
        recalculated = lint(neutral).score
        limit_score = self.reference.limit(limit)
        lo, hi = self.reference.limit_interval(limit, self.profiles.confidence)
        status = "over" if score > hi else "under" if score < lo else "borderline"
        lower = self.profiles.lower_bound
        lower_score = self.reference.limit(lower)
        if score < lower_score:
            warnings.append(
                f"Score is below {lower.label} ({lower_score:.1f}): check for fragmented or choppy prose. "
                "This doesn't mean the text must get harder."
            )

        def target(column: str) -> tuple[float, float]:
            return self.reference.target_range(limit.level, limit_score, column, settings.target_percentiles)

        # gaps to target, judged on what the writer can change
        gaps = []
        for f in FEATURES:
            raw, own = getattr(result, f.name), neutral[f.name]
            if raw is None or own is None:
                continue
            rng = target(f.name)
            raw_gap, own_gap = gap(f, raw, rng), gap(f, own, rng)
            if not raw_gap and not own_gap:
                continue
            edge = rng[0] if f.easier_when_higher else rng[1]
            gaps.append({
                "feature": f.name, "label": f.label, "value": round(raw, 2), "without_terms": round(own, 2),
                "target_range": [round(rng[0], 2), round(rng[1], 2)],
                "points": round(points(f, own, edge), 1) if own_gap else 0.0,
                "caused_by_terms": bool(raw_gap) and not own_gap,
                "advice": f.advice,
            })
        gaps.sort(key=lambda g: -g["points"])

        # hardest sentences
        text_features = result.as_dict()
        sdl_hi, density_hi = target("max_sdl")[1], target("content_per_clause")[1]
        ranked, seen_sentences = [], set()
        for s, tokens, taken in zip(sentences, tokens_per_sentence, positions):
            if word_count(s) < MIN_RANKED_WORDS or s.doc.text.strip() in seen_sentences:
                continue
            seen_sentences.add(s.doc.text.strip())
            s_score = _sentence_score(s, text_features)
            own_score = _sentence_score(s, neutral, taken, self.term_floor)
            if s_score is None or own_score is None:
                continue
            reasons = []
            if s.max_sdl is not None and s.max_sdl > sdl_hi + 2:
                reasons.append(f"related words up to {s.max_sdl} words apart")
            if s.content_words_per_clause is not None and s.content_words_per_clause > density_hi + 1:
                reasons.append(f"{s.content_words_per_clause:.1f} content words per clause")
            if word_count(s) > 25:
                reasons.append(f"{word_count(s)} words long")
            rare_here = sorted({w.token.text for i, w in enumerate(s.word_features)
                                if i not in taken and w.word_frequency is not None and w.word_frequency < RARE_FREQUENCY
                                and not _has_code(w.token.text)})
            if rare_here:
                reasons.append("rare words: " + ", ".join(rare_here))
            keep = sorted({h.term for h in self.matcher.protected(tokens)})
            ranked.append({
                "sentence": s.doc.text.strip(), "score": round(s_score, 1), "without_terms": round(own_score, 1),
                "reasons": reasons, "keep_terms": keep,
            })
        # rank by what the writer can change, so a sentence that is hard only through its terms ranks low
        ranked.sort(key=lambda r: -r["without_terms"])

        # term load per paragraph
        dense = []
        spans = _paragraph_spans(text)
        if spans:
            per_paragraph = [[0, 0, None] for _ in spans]
            for s, taken in zip(sentences, positions):
                for n, (start, end) in enumerate(spans):
                    if start <= s.doc.start_char < end:
                        per_paragraph[n][0] += word_count(s)
                        per_paragraph[n][1] += len(taken)
                        per_paragraph[n][2] = per_paragraph[n][2] or s.doc.text.strip()
                        break
            for n, (w, t, first) in enumerate(per_paragraph, 1):
                if w >= settings.paragraph_min_words and 100 * t / w > settings.paragraph_term_load:
                    start = first if len(first) <= 60 else first[:57] + "..."
                    dense.append({"paragraph": n, "words": w, "terms": t, "per_100_words": round(100 * t / w, 1), "start": start})

        # rare terms without an explanation at first use, for concept-introducing text. If the
        # list marks where terms are new, only those are checked: the others were taught earlier.
        unexplained = []
        introduced = self.matcher.terms.introduced
        if profile == "introduces":
            emphasised = _emphasised(text)
            headings = " | ".join(re.findall(r"(?m)^#+\s+(.*)$", text)).lower()
            seen = set()
            for tokens, hits in zip(tokens_per_sentence, hits_per_sentence):
                for hit in hits:
                    if hit.term in seen:
                        continue
                    seen.add(hit.term)
                    in_heading = any(tokens[p].lower_ in headings for p in hit.positions)
                    if introduced and hit.term not in introduced:
                        continue
                    if not self.matcher.is_ordinary(hit.term) and not in_heading and not _is_explained(tokens, hit, emphasised):
                        unexplained.append(hit.term)

        connective_rate = connectives.per_100_words(tokens_per_sentence)
        c_lo, c_hi = target("connectives_per_100")
        out = {
            "profile": profile,
            "words": words,
            "lint": {
                "score": round(score, 1),
                "term_cost": round(score - recalculated, 1) + 0.0 if recalculated is not None else None,
                "level": result.lint_level,
                "fragment_share": round(result.fragment_share, 2),
            },
            "harder_than": {f"{lv}_exam_texts": round(self.reference.position(lv, score), 2) for lv in LEVELS},
            "limit": {
                "reference": limit.label,
                "score": round(limit_score, 1),
                "interval": [round(lo, 1), round(hi, 1)],
                "over_by": round(score - limit_score, 1) + 0.0,  # no "-0.0"
                "status": status,
            },
            "lower_bound": {"reference": lower.label, "score": round(lower_score, 1), "below": score < lower_score},
            "features": {k: round(text_features[k], 3) for k in
                         ("word_freq", "max_sdl", "content_per_clause", "prop_concrete", "sentence_len", "word_len")
                         if text_features[k] is not None},
            "gaps": gaps,
            "hardest_sentences": ranked[:settings.hardest_sentences],
            "terms": {
                "hits": term_hits,
                "per_100_words": round(100 * term_hits / words, 1) if words else 0.0,
                "counts": dict(sorted(term_counts.items())),
                "dense_paragraphs": dense,
                "unexplained_at_first_use": unexplained,
                "rejected_variants": [
                    {"variant": v, "severity": sev, "count": n} for (v, sev), n in sorted(variants.items())
                ],
                "unlisted_rare_words": [
                    {"word": w, "count": n} for w, n in rare.most_common(15)
                ],
                "lists": [s.as_dict() for s in self.matcher.terms.sources],
                "list_has_uncommitted_changes": self.matcher.terms.modified,
            },
            "connectives": {"per_100_words": round(connective_rate, 1), "target_range": [round(c_lo, 1), round(c_hi, 1)]},
            "warnings": warnings,
        }
        if spans is None:
            warnings.append("Paragraphs couldn't be located, so term load per paragraph is missing.")
        if round_number is not None:
            out["round"] = {"round": round_number, "max": settings.max_rounds, "stop": round_number >= settings.max_rounds}
        out["feedback"] = messages(out, self.matcher.terms.replacements)
        return out

    def check_file(self, path: Path, profile: str | None = None, round_number: int | None = None) -> dict:
        """Check a MyST or notebook file. The profile comes from, in order: the `profile`
        argument, the file's own `tekstniveau.profile` setting, and its folder."""
        path = Path(path)
        profile, source = self.resolve_profile(path, profile)
        result = self.check_text(read_course_file(path), profile, round_number)
        return {"file": str(path), "profile_source": source, **result}

    def resolve_profile(self, path: Path, profile: str | None = None) -> tuple[str, str]:
        if profile is not None:
            return profile, "option"
        own = file_settings(path).get("profile")
        if own is not None:
            return own, "file"
        folder = self.profiles.for_path(path)
        if folder is not None:
            return folder, "folder"
        raise ValueError(f"{path}: no profile; pass one, or set tekstniveau.profile in the file")


# ============================================================================
# brief: A writing brief for an AI writer, given before it writes, and a check of a rewrite.
# ============================================================================

FRAGMENT_RISE = 0.05  # a rise in the share of fragments worth flagging
CONNECTIVE_DROP = 0.25  # a relative drop in connectives worth flagging
MIN_SCORE_CHANGE = 0.3


def brief(checker: Checker, profile: str, current: dict | None = None) -> str:
    """Markdown instructions for writing a text in this profile."""
    profiles, ref = checker.profiles, checker.reference
    limit = profiles.limit(profile)
    limit_score = ref.limit(limit)
    pct = profiles.feedback.target_percentiles

    def rng(column: str, digits: int = 1, percent: bool = False) -> str:
        lo, hi = ref.target_range(limit.level, limit_score, column, pct)
        if percent:
            return f"{100 * lo:.0f}-{100 * hi:.0f}%"
        return f"{lo:.{digits}f}-{hi:.{digits}f}"

    terms = checker.matcher.terms
    protected = ", ".join(sorted(terms.protected))
    replacements = "\n".join(f"  - **{t}**, not *{v}*" for v, t in sorted(terms.replacements.items()))
    lines = [
        f"# Writing brief: `{profile}`",
        "",
        f"The text will be checked with LiNT-II. Target: a score at or below {limit_score:.1f}"
        + (f": {ref.describe(limit)}" if ref.describe(limit) else "")
        + ". Write for first-year HBO-ICT students with a HAVO or MBO-4 diploma."
        + (f" {profiles.guides[profile]} The targets below decide; the level is only a guide."
           if profile in profiles.guides else ""),
        "",
        "## Sentences",
        "",
        f"- Average about {rng('sentence_len', 0)} words per sentence. Vary the length, but split a sentence that carries two ideas.",
        f"- Keep related words close. In exam texts at this level, the longest link between two related words "
        f"averages {rng('max_sdl')} words per sentence. Put the verb near its subject and object, and move long insertions to their own sentence.",
        f"- Use about {rng('content_per_clause')} content words per clause: one idea per clause. "
        "Unpack long noun phrases into a clause with a verb.",
        "",
        "## Words",
        "",
        "- Use everyday words for everything that isn't a listed term.",
        f"- Use concrete examples: in exam texts at this level, {rng('prop_concrete', percent=True)} of nouns are concrete. "
        "Name things a student can picture or type, around the abstract ideas.",
        "",
        "## Terms",
        "",
        "- Keep listed terms exactly as listed, and never replace them with simpler words. They count towards the "
        "score, so the rest of the text has to be simpler to make room for them.",
        "- Introduce new terms one at a time, with a short explanation at first use and an example in between.",
        f"- Listed terms: {protected}.",
    ]
    if replacements:
        lines += ["- Use the listed term, not a variant the course has rejected. Some variants are fine in their "
                  "ordinary meaning, such as *tekst* for what a string contains; `begrippen.md` gives the details.",
                  replacements]
    lines += [
        "",
        "## Connections",
        "",
        f"- Link sentences with connectives, about {rng('connectives_per_100')} per 100 words, such as {CONNECTIVE_EXAMPLES}.",
        "- Don't reach a lower score by chopping sentences into fragments, lists or labels.",
        "",
        "## Process",
        "",
        f"- After writing, run `tekstniveau check` and act on its feedback. Stop after {profiles.feedback.max_rounds} rounds, "
        "and have a person review the text.",
        "- The limits haven't been validated for programming texts. Clarity and correctness come first.",
    ]
    if current and current.get("lint"):
        lines += ["", "## The current text", ""] + [f"- {m}" for m in current["feedback"]]
        hardest = current.get("hardest_sentences") or []
        if hardest:
            lines += ["", "Hardest sentences, by what can change:", ""]
            lines += [f"- \"{s['sentence']}\" ({'; '.join(s['reasons']) or 'mainly long or dense'})" for s in hardest]
    return "\n".join(lines) + "\n"


def compare(before: dict, after: dict) -> dict:
    """Compare two check results of the same text, before and after a rewrite."""
    if not before.get("lint") or not after.get("lint"):
        return {"problems": ["One of the texts couldn't be scored."], "ok": False}
    b_terms, a_terms = before["terms"]["counts"], after["terms"]["counts"]
    lost = sorted(t for t in b_terms if t not in a_terms)
    fewer = {t: [n, a_terms[t]] for t, n in sorted(b_terms.items()) if t in a_terms and a_terms[t] < n}
    b_conn, a_conn = before["connectives"]["per_100_words"], after["connectives"]["per_100_words"]
    change = round(after["lint"]["score"] - before["lint"]["score"], 1) + 0.0
    b_frag, a_frag = before["lint"]["fragment_share"], after["lint"]["fragment_share"]
    problems = []
    if lost:
        problems.append("Listed terms disappeared: " + ", ".join(lost) + ". Put them back; terms are never replaced.")
    if b_conn and a_conn < b_conn * (1 - CONNECTIVE_DROP) and a_conn < after["connectives"]["target_range"][0]:
        problems.append(f"Connectives dropped from {b_conn} to {a_conn} per 100 words. Link the sentences again.")
    if a_frag - b_frag > FRAGMENT_RISE:
        problems.append(f"The share of fragments rose from {b_frag} to {a_frag}. Don't lower the score with fragments or labels.")
    if change > -MIN_SCORE_CHANGE and before["limit"]["status"] != "under":
        problems.append(f"The score barely moved or rose ({before['lint']['score']} → {after['lint']['score']}).")
    new_variants = sorted({v["variant"] for v in after["terms"]["rejected_variants"]}
                          - {v["variant"] for v in before["terms"]["rejected_variants"]})
    if new_variants:
        problems.append("New rejected variants: " + ", ".join(new_variants) + ".")
    return {
        "score": {"before": before["lint"]["score"], "after": after["lint"]["score"], "change": change},
        "status": {"before": before["limit"]["status"], "after": after["limit"]["status"]},
        "term_cost": {"before": before["lint"]["term_cost"], "after": after["lint"]["term_cost"]},
        "terms": {"lost": lost, "fewer": fewer},
        "connectives_per_100_words": {"before": b_conn, "after": a_conn},
        "fragment_share": {"before": b_frag, "after": a_frag},
        "problems": problems,
        "ok": not problems,
    }

# These names are reused by the command line below.
_brief_brief = brief
_brief_compare = compare


# ============================================================================
# cli: Command line: `tekstniveau check`, `tekstniveau brief` and `tekstniveau compare`.
# ============================================================================

TERMS_FILE = Path("conventies") / "begrippen.md"


def _find_terms() -> Path:
    """The course's begrippen.md, looked for upwards from the working folder and this file."""
    for start in (Path.cwd(), Path(__file__).resolve().parent):
        for folder in (start, *start.parents):
            if (folder / TERMS_FILE).is_file():
                return folder / TERMS_FILE
    raise click.UsageError(f"can't find {TERMS_FILE}; pass --terms")


def _files(paths: tuple[Path, ...]) -> list[Path]:
    files = []
    for path in paths:
        if path.is_dir():
            files += sorted(
                p for p in path.rglob("*")
                if p.suffix in SUFFIXES and ".ipynb_checkpoints" not in p.parts and p.is_file()
            )
        else:
            files.append(path)
    return files


def _text_report(r: dict) -> str:
    head = f"{r['file']}  ({r['profile']}, from {r['profile_source']})"
    if r.get("error"):
        return f"{head}\n  error: {r['error']}"
    if r["lint"] is None:
        return "\n".join([head] + [f"  ! {w}" for w in r["warnings"][1:]])
    lint, limit, terms = r["lint"], r["limit"], r["terms"]
    pos = ", ".join(f"{100 * v:.0f}% of {k.split('_')[0]}" for k, v in r["harder_than"].items())
    lines = [
        head,
        f"  score {lint['score']} (LiNT level {lint['level']}), {r['words']} words; harder than {pos} exam texts",
        f"  limit {limit['reference']} = {limit['score']} (interval {limit['interval'][0]}-{limit['interval'][1]}): "
        f"{limit['status']}, {limit['over_by']:+.1f}",
        f"  term cost {lint['term_cost']} points; {terms['per_100_words']} terms per 100 words; "
        f"{r['connectives']['per_100_words']} connectives per 100 words",
    ]
    lines += [f"  ! {w}" for w in r["warnings"][1:]]
    lines += ["", "  Feedback:"] + [f"  - {m}" for m in r["feedback"]]
    if r["hardest_sentences"]:
        lines += ["", "  Hardest sentences, by what can change:"]
        for s in r["hardest_sentences"]:
            why = "; ".join(s["reasons"]) or "long or dense overall"
            lines.append(f"  - {s['without_terms']}: \"{s['sentence']}\" ({why})")
    return "\n".join(lines)


def _checker(terms_path, extra_terms, profile=None):
    with contextlib.redirect_stdout(sys.stderr):  # LiNT-II prints while loading its model
        from lint_ii.linguistic_data import nlp_model  # noqa: F401

    profiles = builtin_profiles()
    terms_path = terms_path or _find_terms()
    if profile:
        profiles.limit(profile)  # fail early on an unknown name
    return Checker(TermMatcher(load_terms(terms_path, extra_terms)), builtin_reference(), profiles)


def common_options(command):
    """Options every command takes: the term list."""
    @click.option("--terms", "terms_path", type=click.Path(exists=True, path_type=Path),
                  help=f"The course's begrippen.md. Default: the nearest {TERMS_FILE} upwards.")
    @click.option("--extra-terms", type=click.Path(exists=True, path_type=Path),
                  help="Extra YAML term list with 'protected' and 'rejected' lists.")
    @functools.wraps(command)
    def wrapper(*args, **kwargs):
        return command(*args, **kwargs)
    return wrapper


def _emit(data, fmt: str, text: str) -> None:
    click.echo(json.dumps(data, indent=2, ensure_ascii=False) if fmt == "json" else text)


FORMAT = click.option("--format", "fmt", type=click.Choice(["text", "json"]), default="text", show_default=True)


@click.group()
def main() -> None:
    """Position Dutch course texts against 2F, 3F and 4F exam texts."""


@main.command()
@click.argument("paths", nargs=-1, required=True, type=click.Path(exists=True, path_type=Path))
@common_options
@click.option("--profile", help="Profile for every file, overriding file settings and folders.")
@click.option("--round", "round_number", type=click.IntRange(min=1),
              help="Rewrite round; feedback says to stop at the configured maximum.")
@FORMAT
@click.option("--strict", is_flag=True, help="Exit with status 1 if any file is over its limit.")
def check(paths, terms_path, extra_terms, profile, round_number, fmt, strict) -> None:
    """Check MyST and notebook files, or every such file in a folder."""

    checker = _checker(terms_path, extra_terms, profile)
    results = []
    for path in _files(paths):
        try:
            results.append(checker.check_file(path, profile, round_number))
        except ValueError as e:
            results.append({"file": str(path), "profile": None, "profile_source": None, "error": str(e)})
    text = f"Note: {ADVISORY}\n\n" + "\n\n".join(_text_report(r) for r in results)
    _emit(results if len(results) != 1 else results[0], fmt, text)
    if strict and any(r.get("limit", {}).get("status") == "over" for r in results):
        sys.exit(1)


@main.command()
@common_options
@click.option("--profile", help="Profile to write for. Defaults to the file's profile.")
@click.option("--file", "path", type=click.Path(exists=True, path_type=Path),
              help="An existing text to rewrite; its current feedback is added to the brief.")
def brief(terms_path, extra_terms, profile, path) -> None:
    """Print a writing brief for an AI writer, as Markdown."""
    make_brief = _brief_brief

    if not profile and not path:
        raise click.UsageError("pass --profile, --file or both")
    checker = _checker(terms_path, extra_terms, profile)
    current = None
    if path:
        try:
            current = checker.check_file(path, profile)
        except ValueError as e:
            raise click.UsageError(str(e)) from e
        profile = current["profile"]
    click.echo(make_brief(checker, profile, current), nl=False)


@main.command()
@click.argument("before", type=click.Path(exists=True, path_type=Path))
@click.argument("after", type=click.Path(exists=True, path_type=Path))
@common_options
@click.option("--profile", help="Profile for both files. Defaults to the profile of AFTER.")
@FORMAT
def compare(before, after, terms_path, extra_terms, profile, fmt) -> None:
    """Check a rewrite against the text it replaces. Exits with status 1 if it has problems."""
    compare_results = _brief_compare

    checker = _checker(terms_path, extra_terms, profile)
    try:
        profile, _ = checker.resolve_profile(after, profile)
    except ValueError as e:
        raise click.UsageError(str(e)) from e
    result = compare_results(checker.check_file(before, profile), checker.check_file(after, profile))
    if "score" in result:
        text = "\n".join([
            f"score {result['score']['before']} -> {result['score']['after']} ({result['score']['change']:+.1f}); "
            f"{result['status']['before']} -> {result['status']['after']}",
            f"connectives per 100 words {result['connectives_per_100_words']['before']} -> "
            f"{result['connectives_per_100_words']['after']}",
        ] + [f"! {p}" for p in result["problems"]] + (["ok"] if result["ok"] else []))
    else:
        text = "\n".join(f"! {p}" for p in result["problems"])
    _emit(result, fmt, text)
    if not result["ok"]:
        sys.exit(1)


if __name__ == "__main__":
    main()

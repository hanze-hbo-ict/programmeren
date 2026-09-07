"""Sphinx directive for interactive code cells."""

from __future__ import annotations

import base64
from html import escape
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


def build_element(
    code: str,
    *,
    pyodide_url: str,
    assignment: str,
    solution: str,
    dormant: bool = False,
) -> str:
    """Return the raw HTML for an ``<interactive-code-cell>`` element."""
    solution_b64 = base64.b64encode(solution.encode()).decode() if solution else ""
    attrs = {
        "data-pyodide-url": pyodide_url,
        "data-assignment": assignment,
        "data-solution": solution_b64,
    }
    if dormant:
        attrs["data-dormant"] = "true"
    attr_str = " ".join(
        f'{k}="{escape(v, quote=True)}"' for k, v in attrs.items()
    )
    return f"<interactive-code-cell {attr_str}>{escape(code)}</interactive-code-cell>\n"


class InteractiveCodeDirective(SphinxDirective):
    """Renders an interactive code cell powered by Pyodide.

    Usage::

        .. interactive-code::
           :assignment: Schrijf een recursieve fibonacci functie.
           :solution: _solutions/fibonacci.py

           def fibonacci(n):
               pass
    """

    has_content = True
    optional_arguments = 0
    option_spec = {  # type: ignore[assignment]
        "assignment": directives.unchanged,
        # Path to a solution file, relative to the document source directory.
        "solution": directives.path,
    }

    def run(self) -> list[nodes.Node]:
        config = self.env.config

        html = build_element(
            "\n".join(self.content),
            pyodide_url=config.interactive_code_pyodide_url,
            assignment=self.options.get("assignment", ""),
            solution=self._read_solution(),
        )
        return [nodes.raw("", html, format="html")]

    def _read_solution(self) -> str:
        path_str = self.options.get("solution", "")
        if not path_str:
            return ""

        doc_dir = Path(self.env.doc2path(self.env.docname)).parent
        solution_path = doc_dir / path_str
        if not solution_path.is_file():
            self.state_machine.reporter.warning(
                f"interactive-code: solution file not found: {solution_path}",
                line=self.lineno,
            )
            return ""
        return solution_path.read_text(encoding="utf-8")

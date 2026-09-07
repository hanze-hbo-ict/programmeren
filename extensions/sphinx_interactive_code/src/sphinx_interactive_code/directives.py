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
    proxy_url: str,
    pyodide_url: str,
    coach_open: bool,
    assignment: str,
    solution: str,
    dormant: bool = False,
) -> str:
    """Return the raw HTML for an ``<interactive-code-cell>`` element."""
    solution_b64 = base64.b64encode(solution.encode()).decode() if solution else ""
    attrs = {
        "data-proxy-url": proxy_url,
        "data-pyodide-url": pyodide_url,
        "data-assignment": assignment,
        "data-solution": solution_b64,
    }
    if coach_open:
        attrs["data-coach-open"] = "true"
    if dormant:
        attrs["data-dormant"] = "true"
    attr_str = " ".join(
        f'{k}="{escape(v, quote=True)}"' for k, v in attrs.items()
    )
    return f"<interactive-code-cell {attr_str}>{escape(code)}</interactive-code-cell>\n"


class InteractiveCodeDirective(SphinxDirective):
    """Renders an interactive code cell powered by Pyodide and an LLM coach.

    Usage::

        .. interactive-code::
           :assignment: Schrijf een recursieve fibonacci functie.
           :solution: _solutions/fibonacci.py
           :coach-open:

           def fibonacci(n):
               pass
    """

    has_content = True
    optional_arguments = 0
    option_spec = {  # type: ignore[assignment]
        "assignment": directives.unchanged,
        # Path to a solution file, relative to the document source directory.
        "solution": directives.path,
        # Override the site-wide interactive_code_coach_open setting.
        "coach-open": directives.flag,
        "coach-closed": directives.flag,
    }

    def run(self) -> list[nodes.Node]:
        config = self.env.config

        if "coach-open" in self.options:
            coach_open = True
        elif "coach-closed" in self.options:
            coach_open = False
        else:
            coach_open = bool(config.interactive_code_coach_open)

        html = build_element(
            "\n".join(self.content),
            proxy_url=config.interactive_code_proxy_url,
            pyodide_url=config.interactive_code_pyodide_url,
            coach_open=coach_open,
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

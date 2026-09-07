"""Tests for the interactive-code Sphinx directive."""

from __future__ import annotations

import base64
import textwrap
from pathlib import Path

import pytest
from sphinx.application import Sphinx
from sphinx_interactive_code.directives import build_element

# ---------------------------------------------------------------------------
# Unit tests — build_element() in isolation
# ---------------------------------------------------------------------------


def make_element(
    code: str = "pass",
    pyodide_url: str = "https://cdn.example.com/pyodide.js",
    assignment: str = "",
    solution: str = "",
) -> str:
    return build_element(
        code,
        pyodide_url=pyodide_url,
        assignment=assignment,
        solution=solution,
    )


class TestBuildElement:
    def test_contains_custom_element_tag(self):
        html = make_element()
        assert "<interactive-code-cell" in html
        assert "</interactive-code-cell>" in html

    def test_code_is_escaped(self):
        html = make_element("x = a < b")
        assert "a &lt; b" in html
        assert "a < b" not in html

    def test_assignment_present(self):
        html = make_element(assignment="Write fibonacci.")
        assert 'data-assignment="Write fibonacci."' in html

    def test_assignment_special_chars_escaped(self):
        html = make_element(assignment='Say "hello"')
        assert "&quot;" in html or "&#" in html

    def test_solution_base64_encoded(self):
        solution = "def fib(n): return n"
        html = make_element(solution=solution)
        expected = base64.b64encode(solution.encode()).decode()
        assert f'data-solution="{expected}"' in html

    def test_empty_solution_attribute_is_empty(self):
        assert 'data-solution=""' in make_element(solution="")

    def test_multiline_solution_roundtrips(self):
        solution = "def fib(n):\n    if n <= 1: return n\n    return fib(n-1)+fib(n-2)"
        html = make_element(solution=solution)
        b64 = html.split('data-solution="')[1].split('"')[0]
        assert base64.b64decode(b64).decode() == solution


# ---------------------------------------------------------------------------
# Integration tests — full Sphinx HTML build
# ---------------------------------------------------------------------------


@pytest.fixture()
def sphinx_build(tmp_path: Path):
    """Build a minimal Sphinx project and return the rendered index.html."""

    def _build(rst: str, conf_extra: str = "") -> str:
        src = tmp_path / "src"
        out = tmp_path / "out"
        src.mkdir(exist_ok=True)
        (src / "conf.py").write_text(
            textwrap.dedent(f"""\
                extensions = ["sphinx_interactive_code"]
                {conf_extra}
            """)
        )
        (src / "index.rst").write_text("Test\n====\n\n" + rst)
        app = Sphinx(str(src), str(src), str(out), str(tmp_path / "doctrees"), "html")
        app.build()
        return (out / "index.html").read_text(encoding="utf-8")

    return _build


class TestDirectiveIntegration:
    def test_element_present_in_output(self, sphinx_build):
        html = sphinx_build(
            """\
.. interactive-code::

   x = 1
"""
        )
        assert "interactive-code-cell" in html

    def test_assignment_in_output(self, sphinx_build):
        html = sphinx_build(
            """\
.. interactive-code::
   :assignment: Write a fibonacci function.

   pass
"""
        )
        assert "Write a fibonacci function." in html

    def test_solution_file_read_and_encoded(self, sphinx_build, tmp_path):
        solution = "def fibonacci(n): return n\n"
        solutions_dir = tmp_path / "src" / "_solutions"
        solutions_dir.mkdir(parents=True, exist_ok=True)
        (solutions_dir / "fib.py").write_text(solution, encoding="utf-8")

        html = sphinx_build(
            """\
.. interactive-code::
   :solution: _solutions/fib.py

   pass
"""
        )
        expected_b64 = base64.b64encode(solution.encode()).decode()
        assert expected_b64 in html

    def test_missing_solution_file_does_not_crash(self, sphinx_build):
        # Should build successfully (with a warning), not raise
        html = sphinx_build(
            """\
.. interactive-code::
   :solution: _solutions/nonexistent.py

   pass
"""
        )
        assert "interactive-code-cell" in html

"""Tests for the myst_nb integration (sphinx_interactive_code.myst_nb)."""

from __future__ import annotations

import json
import textwrap
from pathlib import Path

import pytest
from sphinx.application import Sphinx


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture()
def nb_build(tmp_path: Path):
    """Build a minimal myst_nb Sphinx project and return the rendered HTML."""

    def _build(nb: dict, conf_extra: str = "") -> str:
        src = tmp_path / "src"
        out = tmp_path / "out"
        src.mkdir(exist_ok=True)
        (src / "conf.py").write_text(
            textwrap.dedent(f"""\
                extensions = ["myst_nb", "sphinx_interactive_code", "sphinx_interactive_code.myst_nb"]
                nb_execution_mode = "off"
                {conf_extra}
            """)
        )
        (src / "index.rst").write_text("Test\n====\n\n.. toctree::\n\n   notebook\n")
        (src / "notebook.ipynb").write_text(json.dumps(nb), encoding="utf-8")
        app = Sphinx(str(src), str(src), str(out), str(tmp_path / "doctrees"), "html")
        app.build()
        return (out / "notebook.html").read_text(encoding="utf-8")

    return _build


def make_notebook(*cells: dict) -> dict:
    """Build a minimal nbformat 4 notebook from a list of cell dicts."""
    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"}, "language_info": {"name": "python"}},
        "cells": [
            {
                "id": f"cell-{i}",
                "cell_type": c.get("cell_type", "code"),
                "metadata": c.get("metadata", {}),
                "source": c.get("source", ""),
                "outputs": [],
                "execution_count": None,
            }
            for i, c in enumerate(cells)
        ],
    }


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestNotebookCellTransform:
    def test_code_cell_becomes_interactive_component(self, nb_build):
        html = nb_build(make_notebook({"source": "x = 1"}))
        assert "interactive-code-cell" in html

    def test_code_content_is_present(self, nb_build):
        html = nb_build(make_notebook({"source": "print('hello')"}))
        assert "print(&#39;hello&#39;)" in html or "print('hello')" in html

    def test_markdown_cell_is_not_transformed(self, nb_build):
        html = nb_build(
            make_notebook(
                {"cell_type": "markdown", "source": "## Just text"},
                {"source": "x = 1"},
            )
        )
        # Markdown cell renders as a heading, not as a web component
        assert "<h2" in html or "Just text" in html

    def test_assignment_from_cell_metadata(self, nb_build):
        nb = make_notebook({
            "source": "pass",
            "metadata": {"interactive-code": {"assignment": "Schrijf een lus."}},
        })
        html = nb_build(nb)
        assert "Schrijf een lus." in html

    def test_solution_from_cell_metadata(self, nb_build):
        import base64
        solution = "def fib(n): return n"
        nb = make_notebook({
            "source": "pass",
            "metadata": {"interactive-code": {"solution": solution}},
        })
        html = nb_build(nb)
        expected = base64.b64encode(solution.encode()).decode()
        assert expected in html

    def test_multiple_code_cells_all_transformed(self, nb_build):
        html = nb_build(
            make_notebook({"source": "x = 1"}, {"source": "y = 2"})
        )
        assert html.count("interactive-code-cell") >= 4  # open + close tag × 2

    def test_code_cell_is_dormant_by_default(self, nb_build):
        html = nb_build(make_notebook({"source": "x = 1"}))
        assert 'data-dormant="true"' in html

    def test_static_pygments_view_present(self, nb_build):
        html = nb_build(make_notebook({"source": "x = 1"}))
        assert "sic-nb-static" in html
        # Source container is kept and rendered by Sphinx/Pygments
        assert "highlight" in html

    def test_interactive_view_hidden(self, nb_build):
        html = nb_build(make_notebook({"source": "x = 1"}))
        assert 'sic-nb-interactive" style="display:none"' in html

    def test_activation_bar_injected(self, nb_build):
        html = nb_build(make_notebook({"source": "x = 1"}))
        assert "sic-bar" in html
        assert "Activate" in html

    def test_activation_bar_absent_when_no_code_cells(self, nb_build):
        html = nb_build(make_notebook({"cell_type": "markdown", "source": "just text"}))
        assert "sic-bar" not in html

        # A cell with only whitespace should not produce a component
        html = nb_build(make_notebook({"source": "   \n   "}))
        assert "interactive-code-cell" not in html

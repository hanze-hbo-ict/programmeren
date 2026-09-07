"""myst_nb integration — transforms notebook code cells into interactive-code-cell components.

Usage in conf.py::

    extensions = ["myst_nb", "sphinx_interactive_code", "sphinx_interactive_code.myst_nb"]

Cell-level metadata (optional, in Jupyter cell metadata)::

    {
      "interactive-code": {
        "assignment": "Schrijf een recursieve functie faculteit(n).",
        "solution": "def faculteit(n):\\n    return 1 if n == 0 else n * faculteit(n - 1)"
      }
    }
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, Any

from docutils import nodes
from sphinx.locale import get_translation
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx_design.icons import get_octicon

from sphinx_interactive_code.directives import build_element

if TYPE_CHECKING:
    from sphinx.application import Sphinx

_ = get_translation("sphinx_interactive_code")

_META_KEY = "interactive-code"


def _activate_bar_html() -> str:
    info = _("This page contains executable code cells.")
    button = _("Activate")
    return (
        '<div class="sic-bar">'
        f"<span>{info}</span>"
        f'<button class="sic-btn-activate" onclick="sicActivate(this)">'
        f"{get_octicon('rocket', height='1em')} {button}</button>"
        "</div>\n"
    )


class NotebookCellTransform(SphinxPostTransform):
    """Replace myst_nb ``cell_code`` containers with interactive-code-cell web components."""

    default_priority = 100
    formats = ("html",)

    def run(self, **kwargs: Any) -> None:
        config = self.env.config

        cells = list(
            self.document.findall(
                lambda n: isinstance(n, nodes.container)
                and n.get("nb_element") == "cell_code"
            )
        )
        if not cells:
            return

        # Inject activation bar: after title in first section, or at document start
        bar = nodes.raw("", _activate_bar_html(), format="html")
        for section in self.document.findall(nodes.section):
            insert_at = 1 if section.children and isinstance(section.children[0], nodes.title) else 0
            section.insert(insert_at, bar)
            break
        else:
            self.document.insert(0, bar)

        nb_cells = self._load_nb_cells()

        for cell_node in cells:
            code = self._extract_code(cell_node)
            if not code.strip():
                continue

            # Keep the cell_code_source container — Sphinx/Pygments renders it with
            # syntax highlighting. This becomes the dormant (static) view.
            source_node = next(
                (c for c in cell_node.children
                 if isinstance(c, nodes.container) and c.get("nb_element") == "cell_code_source"),
                None,
            )
            if source_node is None:
                continue

            meta = self._cell_meta(cell_node.get("cell_index", -1), nb_cells)

            interactive_html = build_element(
                code,
                pyodide_url=config.interactive_code_pyodide_url,
                assignment=meta.get("assignment", ""),
                solution=meta.get("solution", ""),
                dormant=True,
            )

            # Replace only cell_code_source — keep the outer cell_code container so
            # myst_nb cell styling (border, green left bar, etc.) is preserved.
            # cell_code_source becomes:
            #   <div class="sic-nb-static">  [Pygments source]  </div>
            #   <div class="sic-nb-interactive" style="display:none"> [web component] </div>
            static_wrapper = nodes.container("", source_node.deepcopy())
            static_wrapper["classes"] = ["sic-nb-static"]
            source_node.replace_self([
                static_wrapper,
                nodes.raw(
                    "",
                    f'<div class="sic-nb-interactive cell_input" style="display:none">'
                    f'{interactive_html}</div>',
                    format="html",
                ),
            ])

    def _extract_code(self, cell_node: nodes.Node) -> str:
        for child in cell_node.children:
            if (
                isinstance(child, nodes.container)
                and child.get("nb_element") == "cell_code_source"
            ):
                for block in child.findall(nodes.literal_block):
                    return block.astext()
        return ""

    def _load_nb_cells(self) -> list:
        nb_path = Path(self.env.srcdir) / f"{self.env.docname}.ipynb"
        if not nb_path.exists():
            return []
        try:
            return json.loads(nb_path.read_text(encoding="utf-8")).get("cells", [])
        except Exception:
            return []

    def _cell_meta(self, cell_index: int, nb_cells: list) -> dict[str, str]:
        if cell_index < 0 or cell_index >= len(nb_cells):
            return {}
        return nb_cells[cell_index].get("metadata", {}).get(_META_KEY, {})


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_post_transform(NotebookCellTransform)
    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

"""Sphinx extension entry point."""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, Any

from sphinx.locale import get_translation

if TYPE_CHECKING:
    from sphinx.application import Sphinx

_STATIC = Path(__file__).parent / "static"
_LOCALES = Path(__file__).parent / "locales"

_ = get_translation("sphinx_interactive_code")


def _add_static_path(app: Sphinx) -> None:
    app.config.html_static_path.append(str(_STATIC))


def _inject_i18n(app: Sphinx) -> None:
    strings = {
        "run": _("Run"),
        "help": _("Help"),
        "askPlaceholder": _("Ask a question\u2026"),
        "loadingPython": _("Loading Python\u2026"),
        "running": _("Running\u2026"),
        "editorLoadError": _("Could not load editor: "),
        "pythonLoadError": _("Could not load Python: "),
        "pyodideLoadError": _("Could not load Pyodide from "),
        "httpError": _("Error: HTTP "),
        "connectionError": _("Connection error: "),
        "error": _("Error: "),
    }
    app.add_js_file(None, body=f"window.SIC_I18N = {json.dumps(strings, ensure_ascii=False)};")


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_message_catalog("sphinx_interactive_code", str(_LOCALES))

    # Proxy / runtime
    app.add_config_value("interactive_code_proxy_url", "/llm-proxy", "html")
    app.add_config_value(
        "interactive_code_pyodide_url",
        "https://cdn.jsdelivr.net/pyodide/v0.27.0/full/pyodide.js",
        "html",
    )

    # Coach panel — initial state and default open/closed
    app.add_config_value("interactive_code_coach_open", False, "html")

    app.connect("builder-inited", _add_static_path)
    app.connect("builder-inited", _inject_i18n)
    app.add_js_file("interactive-code.js", type="module")
    app.add_css_file("interactive-code.css")

    from sphinx_interactive_code.directives import InteractiveCodeDirective

    app.add_directive("interactive-code", InteractiveCodeDirective)

    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

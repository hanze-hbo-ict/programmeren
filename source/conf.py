import os

# Configuration file for Sphinx documentation

# -- Project information -----------------------------------------------------
project = "Programmeren"
author = "Harvey Mudd College / Hanze University of Applied Sciences"
copyright = "CC BY-NC-SA 4.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_nb",
    "sphinx_exercise",
    "sphinx_design",
    "sphinx.ext.mathjax",
    "sphinx_external_toc",
    "sphinxcontrib.bibtex",
    "sphinx_immaterial",
]

external_toc_path = "_toc.yml"
language = "nl"

exclude_patterns = ["_build", "**.ipynb_checkpoints"]

# -- MyST configuration ------------------------------------------------------
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "colon_fence",
    "html_image",
]
# Nodig om binnen-pagina links naar een heading (bijv. `[Web](#web)`) op te
# lossen; genereert anker-labels voor h1 t/m h3.
myst_heading_anchors = 3

# -- MyST-NB configuration ---------------------------------------------------
nb_execution_mode = "cache"
nb_execution_timeout = 60

# -- Bibliography -------------------------------------------------------------
bibtex_bibfiles = ["references.bib"]

# -- HTML output options -----------------------------------------------------
html_theme = "sphinx_immaterial"
html_title = "Programmeren"
html_logo = "_static/lightbulb.svg"

html_theme_options = {
    "repo_url": "https://github.com/hanze-hbo-ict/programmeren",
    "repo_name": "programmeren",
    "edit_uri": "blob/master/source",

    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "indigo-blue",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/brightness-7",
                "name": "Schakel naar dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "indigo-blue",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/brightness-4",
                "name": "Schakel naar light mode",
            },
        },
    ],
}

html_static_path = ["_static"]
html_css_files = ["custom.css"]

# Voor GitHub Pages subpath
html_baseurl = os.environ.get("SPHINX_BASE_URL", "")

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
    "sphinxcontrib.mermaid",
    "sphinxcontrib.bibtex",
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
html_theme = "furo"
html_title = "Programmeren"
html_theme_options = {
    "source_repository": "https://github.com/hanze-hbo-ict/programmeren",
    "source_branch": "master",
    "source_directory": "source/",
    "light_logo": "lightbulb.svg",
    "dark_logo": "lightbulb-dark.svg",
    "light_css_variables": {
        "color-brand-primary": "#3f51b5",
        "color-brand-content": "#3f51b5",
    },
    "dark_css_variables": {
        "color-brand-primary": "#7986cb",
        "color-brand-content": "#7986cb",
    },
}

html_static_path = ["_static"]
html_css_files = ["custom.css"]

# Voor GitHub Pages subpath
html_baseurl = os.environ.get("SPHINX_BASE_URL", "")

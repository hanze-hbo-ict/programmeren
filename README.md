# Programmeren

Cursusmateriaal voor Programmeren 1 & 2 (Hanze Hogeschool, HBO-ICT), gebaseerd op het CS5-materiaal van Harvey Mudd College.

De site wordt gebouwd met [Sphinx](https://www.sphinx-doc.org/) + [MyST](https://myst-parser.readthedocs.io/) en het [sphinx-immaterial](https://sphinx-immaterial.readthedocs.io/)-thema, en automatisch gepubliceerd naar GitHub Pages bij elke push naar `master`.

## Lokaal bouwen

Dit project gebruikt [uv](https://docs.astral.sh/uv/) als package manager.

```bash
uv sync
uv run make html      # bouwt de site naar build/html
uv run make livehtml   # bouwt en herbouwt automatisch bij wijzigingen
```

## Structuur

- `source/` — alle content (lectures, practicals, opgaven, oplossingen, projecten) en de Sphinx-configuratie (`conf.py`, `_toc.yml`).
- `.github/workflows/deploy_sphinx.yml` — bouwt en publiceert de site naar GitHub Pages.
- `.pre-commit-config.yaml` — lint-hooks (markdown, code in codeblokken, notebook-output stripping) die voor elke commit draaien.

## Bijdragen

Commits direct op `master` zijn geblokkeerd door een pre-commit hook; werk in een feature branch en maak een pull request.

# Programmeren

Cursusmateriaal voor Programmeren 1 & 2 (Hanze Hogeschool, HBO-ICT), gebaseerd op het CS5-materiaal van Harvey Mudd College.

De up-to-date build van het boek [kan hier gevonden worden](https://hanze-hbo-ict.github.io/programmeren/about/syllabus.html).

De site wordt gebouwd met [Sphinx](https://www.sphinx-doc.org/) + [MyST](https://myst-parser.readthedocs.io/) en het [furo](https://pradyunsg.me/furo/)-thema, en automatisch gepubliceerd naar GitHub Pages bij elke push naar `master`.

## Aanpassingen

Hoewel we ons best doen het boek up-to-date te houden, kan het soms toch gebeuren dat er een foutje in sluipt. Spot je zo'n foutje? Help ons dan vooral! Je kan problemen, suggesties, etc. melden via het [anonieme feedback formulier](https://hanze-hbo-ict.github.io/programmeren/about/feedback.html), maar natuurlijk is het ook een optie deze repo te forken, de fout te herstellen, en een PR te openen (zie [Bijdragen](#bijdragen) hieronder).

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

## Curriculum

Het ontwerp van de leerlijn staat in [`curriculum/`](curriculum/): de
[leeruitkomsten en toetsmatrijs](curriculum/leeruitkomsten.md) als bindende laag,
de [leerlijn](curriculum/leerlijn.md) per week, en de
[uitgangspunten](curriculum/uitgangspunten.md) met het besluitenregister.

## Werkwijze

Hoe een herziening verloopt staat in [`rollen/`](rollen/), gebonden door
[`rollen.md`](rollen/rollen.md): welke stappen er zijn, wie wat doet, en wat er
tussen die stappen wordt overgedragen.

## Conventies

De afspraken voor auteurs staan in [`conventies/`](conventies/), gebonden door
[`conventies.md`](conventies/conventies.md): een
[schrijfwijzer](conventies/schrijfwijzer.md), een
[begrippenlijst](conventies/begrippen.md),
[codeconventies](conventies/codeconventies.md) en
[technische conventies](conventies/technische-conventies.md). Deze documenten
horen niet bij het studentenmateriaal en worden niet meegebouwd in de site.

## Bijdragen

Activeer na het clonen eerst de hooks:

```bash
uv sync
uv run pre-commit install
```

Commits direct op `master` zijn geblokkeerd door een pre-commit hook; werk in een feature branch en maak een pull request.

## Bronnen

- Dit boek is gebaseerd op [deze template repository](https://github.com/firasm/jupyterbook_course_template).
- De inhoud van het vak steunt op het boek [Think Python. How to Think Like a Computer Scientist van Allen Downey](https://greenteapress.com/wp/think-python-3rd-edition/).

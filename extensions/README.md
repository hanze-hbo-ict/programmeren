# Extensies

Sphinx-extensies die bij dit materiaal horen. **Geen subprojecten**: het is code van
deze repository, met een eigen map maar zonder eigen `pyproject.toml`, lockfile of
virtuele omgeving. Wat zij nodig hebben staat in de hoofd-`pyproject.toml`.

Importeerbaar zonder installatie via `pythonpath = ["extensions"]` in
`[tool.pytest.ini_options]`, en in de build via `sys.path` in `source/conf.py`.

## Twee dingen om te weten bij het werken hieraan

**Sphinx merkt een wijziging in een extensie niet.** Verander je een tekst, een stijl
of de JavaScript, dan slaagt `make html` en toont de pagina gewoon de oude versie -
de bronbestanden in `source/` zijn immers niet veranderd. Gebruik
`make clean && make html`, of herstart `make livehtml`.

**De vertaalcatalogus wordt niet door de build gemaakt.** De teksten van de knoppen
staan in `locales/nl/LC_MESSAGES/`; de `.po` is de bron en de `.mo` is wat Sphinx
leest. Na een wijziging in de `.po`:

```sh
msgfmt -o extensions/sphinx_interactive_code/locales/nl/LC_MESSAGES/sphinx_interactive_code.mo \
        extensions/sphinx_interactive_code/locales/nl/LC_MESSAGES/sphinx_interactive_code.po
```

`msgfmt` staat op het systeem. Er is geen stap in de pipeline die dit doet, en daarom
gaat de `.mo` mee in git - vandaar de uitzondering op `*.mo` in `.gitignore`. Zonder
dat bestand vallen de knoppen stil terug op Engels.

Nederlands is de enige taal die dit materiaal ondersteunt. De vertaallaag zou dus ook
weg kunnen, met de teksten rechtstreeks in de bron; dat is niet gedaan en blijft een
open optie.

## `sphinx_interactive_code`

Maakt de codecellen van een notebook uitvoerbaar in de browser, met Pyodide. Zie
[#96](https://github.com/hanze-hbo-ict/programmeren/issues/96).

**Wat het is:** live coderen als handige functionaliteit, zonder op dat moment een
editor te hoeven opstarten. Niets meer dan dat. De student werkt op zijn eigen
machine in VS Code — zie `curriculum/uitgangspunten.md` r593 — dus de cel op de
pagina is een kladblok en geen werkboek. **Wat de student typt gaat verloren zodra
hij doorklikt, en de pagina mag niet anders suggereren.**

**De LLM-coaching is eruit.** De extensie combineerde het uitvoeren met een
AI-coachpaneel; dat gebruiken we hier niet. De bron ging daarmee van 837 naar 599
regels. Het pakket `sphinx_interactive_code_proxy` uit de oorspronkelijke werkruimte
— de gateway naar een LLM — is niet overgenomen.

**Aangesloten.** `source/conf.py` zet `extensions/` op `sys.path` en laadt
`sphinx_interactive_code` en `sphinx_interactive_code.myst_nb`. Week 2 is daarmee
interactief: 41 cellen in `practicals/2_sequenties_en_data`, 30 in
`problems/2_opstap`, 28 in `lectures/2b_strings_en_lists`, 25 in `2a_var_con`, 20 in
`solutions/2_opstap` en 6 in `problems/2_basis`.

## Wat er van de tests bekend is

`uv run pytest` geeft **20 geslaagd, 2 gevallen**.

**Die twee falen al vóór de refactor.** Gemeten op de onaangeraakte versie: 29
geslaagd, dezelfde 2 gevallen. Het zijn `test_code_content_is_present` en
`test_interactive_view_hidden` in `test_myst_nb.py`, en ze verwachten de celinhoud
terug in de gebouwde HTML. Een bestaande conditie in deze omgeving (Sphinx 9.1.0,
myst-nb 1.4.0), geen gevolg van het weghalen van de coaching.

**Dat moet zijn opgelost voordat de extensie wordt aangesloten**, want die twee
toetsen precies het mechanisme waar het om gaat: staat de code van de cel op de
pagina, en is de interactieve weergave in eerste instantie verborgen.

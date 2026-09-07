# Extensies

Sphinx-extensies die bij dit materiaal horen en in deze repository leven, zodat de
build self-contained is en niet van een pad buiten de repo afhangt.

## `sphinx_interactive_code`

Maakt de codecellen van een notebook uitvoerbaar in de browser, met Pyodide. Zie
[#96](https://github.com/hanze-hbo-ict/programmeren/issues/96).

**Nog niet aangesloten.** De extensie staat hier zoals zij is overgenomen; zij
staat niet in `source/conf.py` en niet in `pyproject.toml`, en de build raakt haar
dus niet. Drie dingen moeten gebeuren voordat zij meedoet:

1. **De LLM-coaching eruit.** De extensie combineert het uitvoeren met een
   AI-coachpaneel. Dat gebruiken we hier niet, en het mag niet blijven staan: de
   JavaScript valt terug op `${this.dataset.proxyUrl || "/llm-proxy"}/chat`, dus
   zonder refactor post een pagina stilletjes naar een pad dat niet bestaat. Dat
   faalt voor de student op het moment dat hij het paneel aanraakt.
2. **Bewaren wat de student typt.** Dat bestaat nog niet; zie #96.
3. **De Python-versie verzoenen.** De extensie eist `>=3.14`, deze repo `>=3.13`.

### Waar de coaching zit

| Bestand | Wat eruit moet |
|---|---|
| `extension.py` | de configwaarden `interactive_code_proxy_url` en `interactive_code_coach_open`; de i18n-sleutels `help`, `askPlaceholder`, `httpError`, `connectionError` |
| `directives.py` | de parameters `proxy_url` en `coach_open` van `build_element`, de attributen `data-proxy-url` en `data-coach-open`, en de opties `:coach-open:` en `:coach-closed:` |
| `myst_nb.py` | twee argumenten in de aanroep van `build_element` |
| `static/interactive-code.js` | de sectie `// ---- LLM chat ----` (r284-373), de helpers `#md`, `#addMessage` en `#scrollMessages`, het `coachOpen`-blok in `#renderActive`, het hulpknop- en formulierbinding in `#bindEvents`, en het bijbehorende deel van `buildLightHtml()` |
| `tests/` | `test_directives.py` (23 treffers) en `test_myst_nb.py` (6) moeten mee worden herschreven |

Het is een **snijlijn en geen ontwarring**: de coaching loopt als een parallelle
laag van configwaarde naar directive-optie naar data-attribuut naar paneel, en
raakt het uitvoeren zelf niet.

### Wat er niet meekomt

Het pakket `sphinx_interactive_code_proxy` uit de oorspronkelijke werkruimte. Dat
is de gateway naar een LLM en die hebben we hier niet.

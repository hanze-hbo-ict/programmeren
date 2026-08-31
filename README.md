# Programmeren

Cursusmateriaal voor Programmeren 1 & 2 (Hanze Hogeschool, HBO-ICT), gebaseerd op het CS5-materiaal van Harvey Mudd College.

De up-to-date build van het boek [kan hier gevonden worden](https://hanze-hbo-ict.github.io/programmeren/about/syllabus.html).

De site wordt gebouwd met [Sphinx](https://www.sphinx-doc.org/) + [MyST](https://myst-parser.readthedocs.io/) en het [furo](https://pradyunsg.me/furo/)-thema, en automatisch gepubliceerd naar GitHub Pages bij elke push naar `master`.

## Aanpassingen

Hoewel we ons best doen het boek up-to-date te houden, kan het soms toch gebeuren dat er een foutje in sluipt. Spot je zo'n foutje? Help ons dan vooral: open een issue, of fork deze repo, herstel de fout en open een pull request (zie [Bijdragen](#bijdragen) hieronder).

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

## Werkwijze: de rollenlus

Herzieningen lopen via een vaste werkwijze, en die is **een experiment**. Het idee
erachter is contextisolatie: in plaats van één assistent die meet, ontwerpt,
schrijft en beoordeelt, doet elke rol één ding met een eigen, verse context. Wie
meet weet niet wat de uitkomst zou moeten zijn. Wie beoordeelt heeft de worsteling
van de schrijver niet gezien. Tussen twee rollen gaat precies één artefact, in de
vorm die een contract voorschrijft; wat daar niet in staat, is niet overgedragen.

Dat is trager en duurder dan het in één gesprek doen, en dat is de bedoeling. Deze
repo is niet stukgegaan aan één slechte wijziging maar aan veel wijzigingen die
ieder op zich verdedigbaar waren en samen de samenhang hebben opgegeten. Daar helpt
geen betere reviewer tegen; daar helpt tegen dat iemand vóór elke wijziging meet wat
er staat, dat elk besluit ergens landt waar de volgende het terugvindt, en dat wie
beoordeelt niet dezelfde is als wie het bedacht.

Of het werkt, weten we niet zeker. Het is bijgesteld terwijl we het gebruikten en
dat zal het blijven; wat we onderweg leren staat in de roldefinities zelf.

Hoe het in de praktijk gaat staat in [`rollen/rollen.md`](rollen/rollen.md): de
stappen, de contracten ertussen, en waarom de vakdeskundige er middenin zit. De lus
draai je met `/orc <issuenummer>`; werkitems zijn GitHub-issues, en de stap waarin
het werk zit staat op het
[projectbord](https://github.com/orgs/hanze-hbo-ict/projects/4). De rolprompts en
contracten staan in `.claude/agent-role-loop/core/`, de subagents in
`.claude/agents/`.

**Niet alles hoeft door de lus.** Een typefout, een dode link of een naam
rechtzetten doe je gewoon, in een branch met een pull request. De lus is voor een
sectie of een week.

## Onderzoek

Deze werkwijze is een experiment, en wat we erover leren staat apart in
[`onderzoek/`](onderzoek/): de [metingen](onderzoek/metingen.md) per rol per ronde,
en de [bevindingen](onderzoek/bevindingen.md) over de werkwijze zelf, elk met het
bewijs en met wat het veranderde.

Dat staat los van het werk aan het materiaal, want het is een andere lezer. Wie het
cursusmateriaal onderhoudt heeft niets aan een tokentelling; wie de werkwijze wil
begrijpen of overnemen heeft niets aan de vraag of week 5 een raster doorloopt.

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

### Wil je met de rollenlus werken?

Dan is er meer nodig dan `uv sync`. Drie dingen:

**1. Toegang tot de issues en het bord.** Werkitems zijn GitHub-issues en de lus
zet de stap in het veld Status op het projectbord. Zorg dat `gh` is
geauthenticeerd (`gh auth status`) en dat je schrijfrechten hebt op
[bord 4](https://github.com/orgs/hanze-hbo-ict/projects/4).

**2. Het referentiemateriaal.** Meerdere rollen vergelijken met de oorspronkelijke
vertaalde CS5-opgaven uit tag `v1.0.0`. Die staan niet in de werkboom en zijn
gitignored, dus pak ze zelf uit:

```bash
mkdir -p referentie/cs5
git archive v1.0.0 topics course problems readings _toc.yml | tar -x -C referentie/cs5
```

Omdat `referentie/` gitignored is, moet je er met `rg --no-ignore` in zoeken. Zie
[`curriculum/uitgangspunten.md`](curriculum/uitgangspunten.md).

**3. Weten wat er al vastligt.** Lees [`rollen/rollen.md`](rollen/rollen.md) voor
de werkwijze, en het besluitenregister in
[`curriculum/uitgangspunten.md`](curriculum/uitgangspunten.md) voor wat er over het
vak besloten is. Een besluit dat daar niet staat, is niet genomen.

Werk je met Claude Code, dan wordt [`CLAUDE.md`](CLAUDE.md) automatisch geladen en
weet de assistent hiervan; de subagents en het `/orc`-commando komen met de repo
mee.

## Bronnen

- Dit boek is gebaseerd op [deze template repository](https://github.com/firasm/jupyterbook_course_template).
- De inhoud van het vak steunt op het boek [Think Python. How to Think Like a Computer Scientist van Allen Downey](https://greenteapress.com/wp/think-python-3rd-edition/).

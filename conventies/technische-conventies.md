# Technische conventies

Dit document beschrijft hoe het bronmateriaal onder `source/` technisch is
opgebouwd: welke opmaak we gebruiken, hoe bestanden en afbeeldingen zijn
belegd, en waaraan de build en de linters toetsen.

Het grootste deel hiervan wordt al mechanisch afgedwongen door de pre-commit
hooks en de Sphinx-build. Dit document legt vast *wat* de regel is, zodat je
haar niet hoeft te ontdekken uit een falende hook.

Dit document is voor auteurs, niet voor studenten. Het staat bewust buiten
`source/` en maakt geen deel uit van het boek.

## Bouwomgeving

Het boek is een Sphinx-site met MyST voor Markdown en myst-nb voor notebooks,
op het thema sphinx-immaterial. Python-afhankelijkheden worden beheerd met uv en
`uv.lock` staat in de repository.

```sh
uv sync                 # omgeving opzetten of bijwerken
uv run pre-commit install   # hooks activeren; eenmalig na het clonen
make html               # bouwt naar build/html
make livehtml           # bouwt en ververst automatisch bij wijzigingen
make clean              # verwijdert build/ en de notebook-cache
```

Het Makefile roept zelf `uv run sphinx-build` aan, dus `make` volstaat.

De build hoort **zonder waarschuwingen** te draaien. Dat is nu het geval en het
is de norm: een waarschuwing wijst vrijwel altijd op een kapotte verwijzing, een
onbekende directive of een afbeelding die niet gevonden wordt.

> **Twee aanbevelingen, nog niet doorgevoerd.**
>
> 1. De build faalt nu niet op waarschuwingen. Met `-W --keep-going` in het
>    Makefile-doel wordt "schoon" afdwingbaar in plaats van een afspraak.
>    Overwegen zodra de inhoudelijke revisie begint, want dan neemt het aantal
>    wijzigingen per week toe.
> 2. `pyproject.toml` zet `[tool.uv] upgrade = true`. Daardoor zoekt uv bij elke
>    aanroep naar nieuwere versies en verandert `uv.lock` spontaan, ook als je
>    niets aan de afhankelijkheden doet. Een lockfile hoort juist te garanderen
>    dat iedereen dezelfde versies bouwt; overweeg de instelling te verwijderen
>    en bewust te upgraden met `uv lock --upgrade`.

## Controles voor elke commit

Vier hooks draaien via pre-commit. Ze werken alleen op `source/`.

> **Activeer ze eerst.** `.pre-commit-config.yaml` staat in de repository, maar
> een git-hook wordt niet meegekloond. Zonder `uv run pre-commit install` draait
> er bij het committen niets en merk je dat pas als de build op GitHub faalt.

| Hook | Waarop | Wat het controleert |
|---|---|---|
| `no-commit-to-master` | altijd | Blokkeert directe commits op `master`; werk in een branch |
| `check-code-blocks` | `.md`, `.ipynb` | Python in ` ```python `-fences: syntax en ruff-opmaak |
| `pymarkdown` | `.md` | Markdown-linting volgens de configuratie in `pyproject.toml` |
| `nbstripout` | `.ipynb` | Verwijdert celuitvoer, zodat die niet in git belandt |

Draai ze handmatig met `uv run pre-commit run --all-files`.

### Wat `check-code-blocks` wel en niet ziet

De hook leest ` ```python `-fences in Markdown-bestanden en in de **markdown-cellen**
van notebooks. Voor elk blok controleert hij of het geldige Python is en of het
overeenkomt met `ruff format`.

Hij slaat blokken over die herkenbaar een fragment zijn: een blok dat met
inspringing begint, dat met `except`, `elif`, `else` of `finally` opent, of dat
uit één onvolledige regel bestaat. Dat is bewust, want lesmateriaal staat vol
losse fragmenten.

De hook kijkt **niet** naar uitvoerbare codecellen van notebooks. Die worden
geverifieerd doordat ze bij de build daadwerkelijk draaien, behalve wanneer ze
de tag `skip-execution` dragen.

Bevat een blok met opzet ongeldige of niet-conventionele Python, bijvoorbeeld
een vraag waarin de student een indentatiefout moet vinden, zet er dan direct
boven:

```markdown
<!-- codecontrole:skip -->
```

## Indeling van `source/`

| Map | Inhoud |
|---|---|
| `about/` | Syllabus, FAQ, feedback, literatuurverwijzingen |
| `course/` | Weekpagina's, practicum-, opgaven- en oplossingenoverzichten |
| `lectures/` | Collegemateriaal |
| `practicals/` | Practicumopdrachten |
| `problems/` | Huiswerkopgaven (opstap, instap, basis, extra) |
| `solutions/` | Uitwerkingen |
| `projects/` | Projectbeschrijvingen |
| `extra/`, `support/` | Verdiepend en ondersteunend materiaal |
| `_static/`, `_templates/` | Thema-aanpassingen, geen lesinhoud |

De inhoudsopgave staat in `source/_toc.yml`, in het `jb-book`-formaat dat
`sphinx-external-toc` leest. Een nieuwe pagina die niet in dit bestand staat,
levert een build-waarschuwing op.

Weekpagina's tonen hun onderliggende pagina's met:

````markdown
```{tableofcontents}
```
````

### Afbeeldingen en bijlagen

- **Bij de inhoud horende afbeeldingen** staan naast het bestand, in
  `images/<weeknummer>/`, en worden relatief aangehaald: `images/6/binarize.png`.
- **Site-brede afbeeldingen** staan in `source/images/` en worden root-relatief
  aangehaald: `/images/saucer.png`.
- **Bijlagen** (`.py`, `.zip`, `.jar`) staan in een `assets/`-map naast de
  inhoud.

Geef elke afbeelding een alt-tekst die beschrijft wat er te zien is.

> `source/about/syllabus.md` gebruikt nog `../images/...`. Dat werkt, maar wijkt
> af; zet het bij de eerstvolgende bewerking om naar `/images/...`.

## Markdown en MyST

### Admonitions

Gebruik uitsluitend de types die het thema kent. Andere waarden renderen wel,
maar krijgen de standaardopmaak in plaats van een eigen kleur en pictogram, en
vallen daardoor uit de toon.

`abstract`, `bug`, `danger`, `example`, `failure`, `info`, `note`, `question`,
`quote`, `success`, `tip`, `warning`

Twee schrijfwijzen, beide goed:

````markdown
:::{admonition} Eigen kop
:class: tip

De tekst van het kader.
:::
````

````markdown
```{tip}
De tekst van het kader, met de standaardkop "Tip".
```
````

Gebruik de eerste vorm wanneer de kop iets toevoegt, de tweede wanneer de
standaardkop volstaat.

> **`notice` is geen geldig type.** Het komt nog 18 keer voor in het materiaal
> en levert stille verkeerde opmaak op. Vervang het door `note` zodra je een
> bestand aanraakt. Hetzelfde geldt voor `seealso`, `important`, `caution` en
> `attention`: die renderen, maar vallen buiten het palet van het thema.

### Codeblokken

| Taal | Waarvoor |
|---|---|
| `python` | Python die de student leest of overneemt. **Wordt gecontroleerd.** |
| `text` | Uitvoer, pseudocode, en alles wat geen geldige Python is |
| `ipython` | Transcripten van een interactieve sessie (`In [1]:` / `Out[1]:`) |
| `console` | Shell-commando's |

Kies `ipython` alleen wanneer het blok schoon lext. Bevat de uitvoer tekens
waar de lexer over struikelt, zoals `!` of `€` op een onverwachte plek, gebruik
dan `text`. Anders geeft de build een lexer-waarschuwing.

Zet nooit uitvoer in een `python`-blok: dat is geen Python en de hook keurt het
terecht af.

### Verwijzingen tussen pagina's

Verwijs root-relatief en zonder extensie:

```markdown
[Board](/practicals/11_vier_op_rij_board)
```

Verwijs je naar een kop *binnen* een andere pagina, dan gelden twee afwijkende
regels tegelijk:

```markdown
[power](/extra/examples/recursie.md#powerb-p)
```

1. **De extensie is verplicht.** Zonder `.md` herkent MyST de link niet als
   documentverwijzing en wordt het anker nooit opgezocht.
2. **De slug is die van MyST, niet die van de HTML.** MyST maakt zijn anker
   door leestekens te *verwijderen*, niet te vervangen. De kop
   `` ## `power(b, p)` `` krijgt in de HTML `id="power-b-p"`, maar MyST zoekt
   op `powerb-p`. Kopieer het anker dus niet uit de gerenderde pagina.

Ankers werken tot en met kopniveau 3 (`myst_heading_anchors = 3`).

### Downloads

Een bestand dat geen pagina is, koppel je met de `download`-rol. Een gewone
Markdown-link geeft een build-waarschuwing.

```markdown
{download}`begincode voor de klasse Board </problems/assets/board.py>`
```

### Overige middelen

- **Wiskunde** met `$...$` en `$$...$$` (`dollarmath`, `amsmath`).
- **Diagrammen** met de ` ```{mermaid} `-directive.
- **Definitielijsten** en **colon fences** (`:::`) zijn beschikbaar.
- **HTML in Markdown** is beperkt tot: `br`, `sub`, `sup`, `code`, `iframe`,
  `a`, en commentaar. Andere tags keurt de linter af.
- **Literatuurverwijzingen** via `sphinxcontrib-bibtex` uit
  `source/references.bib`.

## Notebooks

- **Geen uitvoer in git.** `nbstripout` verwijdert die bij elke commit.
- **Codecellen draaien bij de build** (`nb_execution_mode = "cache"`, time-out
  60 seconden). Een cel die faalt, breekt de build. Verwijst een cel via `%run`
  naar een bestand, dan moet dat bestand op de juiste plek in `source/` staan.
- **Celtags** sturen dat gedrag:

  | Tag | Effect |
  |---|---|
  | `skip-execution` | Cel draait niet. Voor stubs die de student invult |
  | `raises-exception` | Cel mag falen; de fout hoort bij de les |
  | `remove-cell` | Cel verschijnt niet op de site |

## Markdown-linting

De configuratie staat in `pyproject.toml`, onder `[tool.pymarkdown]`. Een paar
regels zijn bewust uitgezet, elk met de reden erbij in het bestand. Kort
samengevat:

- **MD013** (regellengte) en **MD001** (kopniveaus) uit: passen niet bij dit
  materiaal.
- **MD046** uit: de linter herkent MyST colon-fences niet en ziet ingesprongen
  directive-inhoud aan voor een codeblok.
- **MD011** uit: valse meldingen op code-spans als `` `text.split(".")[:-1]` ``.
- **MD025** wijst naar een ongebruikte front-matter-sleutel, zodat een pagina
  zowel een `title` in de front matter als een `#`-kop mag hebben.

Een MyST-label direct boven een kop botst met MD022, dat een witregel eist waar
het label er juist geen mag hebben. Onderdruk dat gericht:

```markdown
<!--pyml disable-num-lines 2 md022-->
(picobot-start)=
### Begin
```

## Python in het materiaal

Alle Python in ` ```python `-fences volgt `ruff format`. Dat is geen stijlkeuze
die je per blok afweegt; de hook dwingt het af.

Wat de code *inhoudelijk* moet zijn, zoals naamgeving, taal van commentaar en
docstrings, hoort niet hier maar in de codeconventies. Dat document is nog niet
geschreven.

## Bekende valkuilen

| Verschijnsel | Oorzaak |
|---|---|
| Build-waarschuwing "document isn't included in any toctree" | Pagina ontbreekt in `source/_toc.yml` |
| Lexer-waarschuwing op een `ipython`-blok | Uitvoer bevat tekens die de lexer niet aankan; gebruik `text` |
| Kaderopmaak klopt niet | Ongeldig admonition-type, meestal `notice` |
| Anker naar een andere pagina werkt niet | Extensie vergeten, of de HTML-`id` gekopieerd in plaats van de MyST-slug |
| Build-waarschuwing bij een link naar een `.py` of `.zip` | Gewone link gebruikt in plaats van de `download`-rol |
| Notebook faalt bij de build | Een `%run`-bestand of afbeelding staat niet mee onder `source/` |

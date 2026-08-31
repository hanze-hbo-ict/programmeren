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
op het thema furo. Python-afhankelijkheden worden beheerd met uv en
`uv.lock` staat in de repository.

```sh
uv sync                 # omgeving opzetten of bijwerken
uv run pre-commit install   # hooks activeren; eenmalig na het clonen
make html               # bouwt naar build/html
make livehtml           # bouwt en ververst automatisch bij wijzigingen
make clean              # verwijdert build/ en de notebook-cache
make review PR=87       # haalt een pull request op, bouwt, opent de gewijzigde pagina's
make terug              # terug naar master na een review
```

Het Makefile roept zelf `uv run sphinx-build` aan, dus `make` volstaat.

De build hoort **zonder waarschuwingen** te draaien. Dat is nu het geval en het
is de norm: een waarschuwing wijst vrijwel altijd op een kapotte verwijzing, een
onbekende directive of een afbeelding die niet gevonden wordt.

> **Nog te overwegen.** De build faalt niet op waarschuwingen. Met
> `-W --keep-going` in het Makefile-doel wordt "schoon" afdwingbaar in plaats van
> een afspraak. Dat is het overwegen waard nu de inhoudelijke revisie loopt en
> het aantal wijzigingen per week toeneemt.

## Het thema

De site draait op **furo**. Daarvoor stond er sphinx-immaterial, en het is de
moeite waard op te schrijven waarom dat is gewisseld, want anders wordt die
keuze over twee jaar opnieuw gevoerd zonder de metingen erbij.

### Waarom furo

Sphinx-immaterial gaf in één week drie problemen, en ze kwamen alle drie uit
dezelfde hoek:

| | sphinx-immaterial | furo |
|---|---|---|
| Zoeken op Sphinx 9.1 | **0 resultaten** | 13 resultaten |
| JavaScript-fouten per pagina | 2 | geen |
| Mermaid | botste met `sphinxcontrib-mermaid` | werkt |

De zoekfunctie was geen theorie: op de gepubliceerde site gaf een zoekopdracht
op *picobot* niets terug, op een site waar Picobot een heel hoofdstuk is.

Beide problemen staan bovenstrooms open en zijn door de maintainers bevestigd:
[#485](https://github.com/jbms/sphinx-immaterial/issues/485) voor het zoeken en
[#435](https://github.com/jbms/sphinx-immaterial/issues/435) voor mermaid, waar
de maintainer schrijft dat ondersteuning voor `sphinxcontrib-mermaid` niet
gepland is.

### De les die breder geldt

Sphinx-immaterial declareert `sphinx>=6`, **zonder bovengrens**. Daardoor
installeert uv het naast Sphinx 9, een versie die het thema niet aankan. Furo
declareert `sphinx>=7,<10`: die dichte bovengrens betekent dat iemand 9 heeft
getest.

**Een open bovengrens op een afhankelijkheid die diep in de build zit, is een
risicosignaal.** Kijk ernaar voordat je iets toevoegt.

### Wat eraan vastzit

Weinig, en dat is met opzet zo gehouden:

| | |
|---|---|
| `html_theme_options` | ~20 regels in `conf.py` |
| Eigen CSS | `source/_static/custom.css`, een handvol regels |
| Logo | `light_logo` en `dark_logo`; twee versies van dezelfde tekening, de donkere met een opgelichte vulling |

Al het andere is standaard MyST en `sphinx-design`, en dat werkt in elk thema.
Toen we wisselden was de hele koppeling 28 regels opties, 7 mermaid-directives
en 4 regels CSS.

Gebruik daarom **geen themaspecifieke directives** in het materiaal. Mermaid gaat
via `sphinxcontrib.mermaid`, tabs en kaarten via `sphinx-design`, admonitions via
MyST. Dan blijft een volgende wissel een dag werk.

## Controles voor elke commit

Vier hooks draaien via pre-commit. Ze werken alleen op `source/`.

> **Activeer ze eerst.** `.pre-commit-config.yaml` staat in de repository, maar
> een git-hook wordt niet meegekloond. Zonder `uv run pre-commit install` draait
> er bij het committen niets en merk je dat pas als de build op GitHub faalt.

| Hook | Waarop | Wat het controleert |
|---|---|---|
| `no-commit-to-master` | altijd | Blokkeert directe commits op `master`; werk in een branch |
| `check-code-blocks` | `.md`, `.ipynb` | Python in ` ```python `-fences: syntax en ruff-opmaak |
| `check-notebook-tags` | `.ipynb` | Celtags: opgaven leeg, uitwerkingen draaien |
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

| Directory | Inhoud |
|---|---|
| `about/` | Syllabus, FAQ, literatuurverwijzingen |
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

## Markdown of notebook

Het materiaal gebruikt beide formaten. Dat is geen toeval maar een keuze met een
geschiedenis, en die geschiedenis bepaalt de regel.

**Markdown is de standaard.** Kies een notebook alleen wanneer minstens één van
deze drie gronden geldt:

1. **Het document wordt als sheets gepresenteerd.** De colleges zijn opgezet om
   in de les als sheets te draaien, met cellen van het type `notes` als
   spreeknotities. Die notities renderen op de site als gewone tekst, waardoor
   hetzelfde bestand in de les een presentatie is en daarna een doorlopend
   verhaal dat de student zelfstandig kan lezen.
2. **De code moet uitvoeren.** Codecellen draaien bij de build, wat het
   materiaal automatisch controleert, en ze zijn de basis voor code die de
   student in de browser kan uitvoeren.
3. **De student werkt in het document.** Een opgave met invulcellen is een
   werkboek; dat werkt alleen als notebook.

Geldt geen van drieën, dan is het een markdown-bestand.

### Waarom dit zo gegroeid is

In de oorspronkelijke opzet waren de colleges notebooks omdat ze als sheets
werden gebruikt, en waren de opgaven markdown omdat de student ze in VSCode
uitwerkte. Toen bleek dat de tooling voor beginners een drempel is, en toen de
opgaven werden opgesplitst in opstap, basis en extra, is geprobeerd de code in
de browser uitvoerbaar te maken. Dat liep via MyBinder, werd door veel studenten
gebruikt, maar was niet betrouwbaar. Het uitgangspunt blijft overeind; de
uitvoering wordt bij de herziening vervangen door Pyodide.

> **Op dit moment ontbreekt die mogelijkheid.** De oude Jupyter Book-opzet had
> `launch_buttons` met thebe en een Colab-koppeling. Sphinx-immaterial heeft die
> niet, en bij de migratie zijn ze niet vervangen. Een notebook levert de student
> op de site nu dus niets extra's op boven markdown. Drie bestanden verwijzen de
> student nog wel naar Colab. Dit staat open tot de Pyodide-oplossing er is.

### Wat het formaat betekent voor de controle

De twee formaten worden verschillend gecontroleerd, en geen van beide volledig:

| Waar de code staat | Syntax en opmaak | Wordt uitgevoerd |
|---|---|---|
| ` ```python ` in een markdown-bestand | ja, door de hook | nee |
| ` ```python ` in een markdown-cel van een notebook | ja, door de hook | nee |
| Codecel **zonder** `skip-execution` | nee | ja, bij de build |
| Codecel **met** `skip-execution` | nee | nee |

De laatste rij is de enige plek waar code door niets wordt gecontroleerd. Dat is
geen ontwerpfout maar de prijs van interactiviteit: een cel die de lezer zelf
moet uitvoeren, moet leeg aankomen.

Dat verschil is niet vrijblijvend. Een uitwerking als codecel wordt bij elke
build daadwerkelijk uitgevoerd; dezelfde uitwerking als markdown-blok wordt
alleen op syntax en opmaak bekeken. Van de 22 uitwerkingen staan er nu 11 als
markdown-blok en zijn dus nooit gedraaid; het waren er 15, tot de vier van week 5
werden omgezet.

**Vandaar de regel: uitwerkingen draaien, opgaven niet.** Een cel kan niet
tegelijk leeg aankomen en geverifieerd zijn. Voor een opgave weegt leeg het
zwaarst, en komt de verificatie van de bijbehorende uitwerking. Het materiaal
doet dit al grotendeels: van de codecellen in `solutions/` draaien er 109 en
staan er 2 op `skip`, terwijl `practicals/` juist 60 overgeslagen cellen heeft
tegen 1 die draait.

De ongedekte flank in die tabel, de opmaak van codecellen, is op dit moment geen
probleem: alle 525 uitvoerbare cellen voldoen al aan `ruff format`. De hook
uitbreiden zou dat vastleggen in plaats van erop te vertrouwen.

### Huidige verdeling

| Grond voor notebook | Aantal | Waar |
|---|---|---|
| Sheets, met of zonder code | 6 | uitsluitend `lectures/` |
| Uitvoerbare code, geen sheets | 23 | verspreid |
| Alleen invulcellen (werkboek) | 12 | `problems/` 10, `practicals/` 2 |
| **Geen van drieën** | **34** | `solutions/` 11, `problems/` 11, `practicals/` 7, `lectures/` 4, `extra/` 1 |

Die laatste 34 zijn markdown-documenten in een notebook-jasje; het waren er 39,
tot de vijf van week 5 uitvoerbare cellen kregen. Twee colleges springen eruit
omdat ze in `lectures/` geen enkele grond hebben:
`10a_knapzak_probleem.ipynb` en `4b_midterm.ipynb`.

Dit wordt niet in één actie omgezet. Per document wordt bij de herziening
bepaald welke grond geldt, en daarmee welk formaat. Voor uitwerkingen speelt de
verificatietabel hierboven daarin mee.

### Afbeeldingen en bijlagen

- **Bij de inhoud horende afbeeldingen** staan naast het bestand, in
  `images/<weeknummer>/`, en worden relatief aangehaald: `images/6/binarize.png`.
- **Site-brede afbeeldingen** staan in `source/images/` en worden root-relatief
  aangehaald: `/images/saucer.png`.
- **Bijlagen** (`.py`, `.zip`, `.jar`) staan in een `assets/`-directory naast de
  inhoud.

Geef elke afbeelding een alt-tekst die beschrijft wat er te zien is.

> `source/about/syllabus.md` gebruikt nog `../images/...`. Dat werkt, maar wijkt
> af; zet het bij de eerstvolgende bewerking om naar `/images/...`.

## Markdown en MyST

### Admonitions

Gebruik uitsluitend de standaardtypes. Andere waarden renderen wel, maar krijgen
de standaardopmaak in plaats van een eigen kleur en pictogram, en vallen daardoor
uit de toon.

`attention`, `caution`, `danger`, `error`, `hint`, `important`, `note`, `seealso`,
`tip`, `warning`

Dit zijn de types van Sphinx zelf, dus ze werken ongeacht het thema. Gebruik geen
themaspecifieke types, want die vervallen zodra het thema wisselt.

`notice` en `info` bestaan niet en zijn nergens meer in gebruik. Kom je ze
tegen in materiaal van buiten, kijk dan naar de kop van het kader: die zegt
meestal welk type bedoeld is.

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

> **Alle tien de types hebben in furo hun eigen opmaak.** De eerdere waarschuwing
> dat `seealso`, `important`, `caution` en `attention` buiten het palet zouden
> vallen, stamde uit de tijd van sphinx-immaterial en klopt niet meer. Gemeten in
> `build/html/_static/styles/furo.css`: alle acht gecontroleerde types krijgen er
> evenveel regels. Kies dus het type dat de inhoud dekt, niet het type dat er
> zeker uitziet.

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
  | `skip-execution` | Cel draait niet en bereikt de lezer leeg |
  | `raises-exception` | Cel mag falen; de fout hoort bij de les |
  | `remove-cell` | Cel verschijnt niet op de site |

### `skip-execution` is niet alleen een build-instelling

Deze tag draagt het interactieve ontwerp. Draait een cel bij de build, dan staat
de uitvoer in de HTML en valt er voor de lezer niets meer te doen. Draagt hij de
tag, dan komt hij leeg aan en kan de student hem op de pagina zelf uitvoeren.
Dat werkte eerder via MyBinder en wordt straks Pyodide.

#### Wanneer zet je hem

De tag zegt één ding: **deze cel is er om door de student uitgevoerd te worden.**
Dat is de vraag die je jezelf stelt, niet of de build ermee overweg kan.

Er zijn twee gevallen, en ze zien er verschillend uit maar vragen hetzelfde:

**Uitleg.** Een compleet, werkend voorbeeld. De student voert het uit en kijkt
wat eruit komt. Het gaat om de handeling: uitvoer lezen die er al staat is iets
anders dan hem zien verschijnen, zeker wanneer de student eerst mag voorspellen
wat er gaat gebeuren.

**Opdracht.** Een lege of halve cel die de student invult en draait.

In beide gevallen moet de cel leeg aankomen, en dus mag hij bij de build niet
draaien.

Zet hem **niet** op een cel waarvan de lezer de uitvoer alleen hoeft te lezen;
die hoort te draaien, dan staat er tenminste iets dat klopt. En niet in
`solutions/`, want daar is de uitvoering juist het bewijs dat de uitwerking
werkt.

#### Hoe het er nu voor staat

Gemeten over `source/`, per aanleiding:

| Aanleiding | Aantal | Toelichting |
|---|---|---|
| Opdracht: stub die de student invult | 100 | Het werkboekmodel |
| Uitleg: compleet voorbeeld dat de student uitvoert | 89 | |
| Zou de build blokkeren of laten falen | 4 | `input()`, turtle, bestanden openen |

Die laatste groep is een noodgreep en geen bedoeling. De eerste twee zijn de
regel hierboven.

En daarom is dit geen implementatiedetail: deze tag bepaalt straks welke cellen
voor de student uitvoerbaar worden, zie
[#96](https://github.com/hanze-hbo-ict/programmeren/issues/96). Een cel die de
tag ten onrechte mist, staat er dan dood bij; een cel die hem ten onrechte
draagt, is een leeg vakje zonder opdracht.

Omdat deze fout onzichtbaar is in de gerenderde pagina, bewaakt een hook hem:
`check-notebook-tags` controleert dat een codecel in `problems/` of
`practicals/` de tag draagt en dat een codecel in `solutions/` hem juist niet
draagt. Twee uitzonderingen kent hij:

- Een cel met `raises-exception` mag draaien; de fout hoort bij de les.
- Een uitwerking die `input()` vraagt of niet uit zichzelf eindigt, kan niet
  onbewaakt draaien en mag overgeslagen worden.

> **Bekende afwijking.** 15 cellen voldoen nog niet, verdeeld over
> `problems/8_basis.ipynb` (10 skeletcellen met `return [...]`),
> `problems/2_opstap.ipynb` (4) en `practicals/2_sequenties_en_data.ipynb` (1).
> Omdat de hook alleen kijkt naar bestanden die je aanraakt, blokkeert dit niets
> tot het betreffende document aan de beurt is.

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
| Kaderopmaak klopt niet | Ongeldig admonition-type; alleen de tien standaardtypes hebben eigen opmaak |
| Anker naar een andere pagina werkt niet | Extensie vergeten, of de HTML-`id` gekopieerd in plaats van de MyST-slug |
| Build-waarschuwing bij een link naar een `.py` of `.zip` | Gewone link gebruikt in plaats van de `download`-rol |
| Notebook faalt bij de build | Een `%run`-bestand of afbeelding staat niet mee onder `source/` |

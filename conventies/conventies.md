# Projectconventies

Dit document bindt de conventies die gelden voor het cursusmateriaal onder
`source/`. Het legt vast *welke* afspraken gelden en *hoe* ze geborgd zijn; de
inhoud van elke afspraak staat in haar eigen document.

Zo hangt de toepassing niet af van wie een taak uitvoert of wie hem beoordeelt.

## Welke conventies gelden

Voor al het werk aan `source/` gelden:

| Document | Waarover |
|---|---|
| [schrijfwijzer.md](schrijfwijzer.md) | Register, aanspreekvorm, terminologiebeleid, opbouw van een tekst |
| [begrippen.md](begrippen.md) | De vaste term per begrip |
| [codeconventies.md](codeconventies.md) | Taal, naamgeving, docstrings en assertions in de voorbeeldcode |
| [technische-conventies.md](technische-conventies.md) | MyST-opmaak, bestandsindeling, build en controles |

## Reikwijdte

De conventies gelden voor `source/`, het materiaal dat de student ziet.

Ze gelden **niet** voor de documenten in `conventies/` zelf, en niet voor de
verzameling niet-gemigreerd materiaal buiten `source/` (`ontwikkeling/`,
`readings/`, `teacher_guides/`, `topics/`, `problems/context/` en verwante
directories). Dat materiaal staat bewust stil in afwachting van een beslissing over
wat ermee gebeurt.

## Hoe dit geborgd is

Op twee manieren, en dat onderscheid is opzettelijk.

### Mechanisch, waar dat kan

De pre-commit hooks controleren wat een machine kan controleren: Python-syntax
en opmaak in codeblokken, Markdown-linting, en het weghouden van celuitvoer uit
git. De Sphinx-build vangt kapotte verwijzingen en onbekende directives.

Wat deze controles precies doen, en hoe je ze activeert, staat in
[technische-conventies.md](technische-conventies.md). Activeer ze eerst:
zonder `uv run pre-commit install` draait er bij het committen niets.

### Door beoordeling, waar dat moet

Register, terminologie, naamgeving en didactische opbouw kan geen hook toetsen.
Daarvoor geldt de afspraak dat elk werkitem voor dit materiaal het volgende als
vast acceptatiecriterium opneemt:

> Voldoet aan de conventies in `conventies/conventies.md`, en de build is schoon.

Daarmee kan werk niet worden goedgekeurd zonder dat eraan getoetst is, ongeacht
wie of wat het uitvoert. Wie materiaal schrijft, leest de betreffende conventies
vooraf, zodat het resultaat er meteen aan voldoet in plaats van achteraf.

## Bekende afwijkingen

Het materiaal is over jaren door verschillende auteurs bewerkt en voldoet nog
niet overal. Die afwijkingen zijn vastgelegd in de documenten waar ze thuishoren,
met per geval het aantal:

- 10 kaders met het ongeldige type `notice`, zie de technische conventies. Het
  waren er 16; week 5 heeft er 6 rechtgezet.
- Twee naamgevingssystemen naast elkaar, zie de codeconventies.
- 48 keer de kleine letter `l` als variabelenaam, en een functie `blaat`, zie de
  codeconventies.
- Een aankondiging in week 2 dat we in het Engels programmeren, wat vooruitloopt
  op de afgesproken overgang, zie de codeconventies.
- `Opgave` en `Opdracht` door elkaar als kop, zie de begrippenlijst.
- 34 notebooks zonder grond om notebook te zijn, en het ontbreken van de
  browser-uitvoering die notebooks voor de student zinvol maakt, zie de
  technische conventies. Het waren er 39; de vijf van week 5 hebben nu
  uitvoerbare cellen.
- 11 van de 22 uitwerkingen staan als markdown-blok en worden dus nooit
  uitgevoerd, en 10 skeletcellen missen `skip-execution`, zie de technische
  conventies. Het waren er 15; de vier uitwerkingen van week 5 draaien nu bij de
  build.

Deze worden niet in een aparte opruimactie weggewerkt maar per bestand
rechtgezet tijdens de inhoudelijke herziening. Ze staan hier zodat ze niet
opnieuw ontdekt hoeven te worden.

## Een conventie toevoegen of wijzigen

Komt er een afspraak bij, voeg haar toe aan het document waar ze thuishoort, en
neem het document zo nodig op in de tabel hierboven. Dit document legt de
gelding vast; de inhoud hoort ergens anders.

Blijkt een bestaande conventie in de praktijk niet te werken, wijzig haar dan
hier in plaats van er in losse bestanden van af te wijken. Een conventie waarvan
op drie plekken stilzwijgend wordt afgeweken, is geen conventie meer.

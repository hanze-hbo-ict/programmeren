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
wat ermee gebeurt. Voor `teacher_guides/` geldt dat nog steeds voor de `.docx` die
er staan; wat daaruit is herschreven, verhuist naar `handleidingen/` en valt onder
het regime hieronder.

**Eén uitzondering binnen `source/`:** de vier oefententamens
(`extra/practice/pgm1_examen.ipynb`, `extra/practice/PGM2_examen.md`,
`solutions/PGM1_examen.ipynb` en `solutions/PGM2_examen.ipynb`) houden hun
`Opgave N`-koppen. Een tentamenvraag is geen opgave, opdracht of stap in de zin
van [begrippen.md](begrippen.md), en het oefententamen is bij besluit bevroren;
zie `curriculum/uitgangspunten.md`. De hook `check-kopwoord` slaat deze vier
bestanden daarom over, en die uitsluiting hoort hier te staan en niet alleen in
de hookconfiguratie.

**Het zijn er precies vier, en de lijst hierboven is uitputtend.**
`extra/practice/1_recursie.ipynb` en `2_list_comprehension.ipynb` staan er
níet bij: dat zijn oefenbestanden en geen oefententamens. Bij werkitem #178 zijn
ze een ronde lang op die verkeerde grond buiten de kopwoordregel gehouden. Ze
vallen er gewoon onder, en hun `## Opgaven` blijft staan omdat het een
rubriekkop is - zie [begrippen.md](begrippen.md), *Opgave, opdracht, stap*, en
niet omdat er een uitzondering voor ze zou gelden.

Voor `handleidingen/` geldt een eigen regime. Die documenten richten zich tot de
docent en niet tot de student, en zijn geen onderdeel van het boek: de
Sphinx-build raakt ze niet. Van de vier conventiedocumenten binden de
begrippenlijst, de codeconventies voor de codefragmenten die een handleiding
toont, en de markdownopmaak en de lintregels uit de technische conventies. De
schrijfwijzer bindt ze niet, en de MyST-directives, de celtags en de indeling van
`source/` uit de technische conventies evenmin: die gaan over het boek en zijn
build. Mechanisch geborgd is alleen de Markdown-linting - `handleidingen/` staat
in het `pymarkdown`-patroon.

## Hoe dit geborgd is

Op twee manieren, en dat onderscheid is opzettelijk.

### Mechanisch, waar dat kan

De pre-commit hooks controleren wat een machine kan controleren: Python-syntax
en opmaak in codeblokken, celtags, het kopwoord en de niveaunaam,
Markdown-linting, en het weghouden van celuitvoer uit git. De Sphinx-build vangt kapotte verwijzingen en onbekende directives.

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

- Twee naamgevingssystemen naast elkaar, zie de codeconventies.
- De kleine letter `l` als variabelenaam, en een functie `blaat`, zie de
  codeconventies. Beide zijn met de herziening van week 3 uit `source/`
  verdwenen; het getal 48 dat hier stond is bij die herziening nagemeten en niet
  te reproduceren.
- Een aankondiging in week 2 dat we in het Engels programmeren, wat vooruitloopt
  op de afgesproken overgang, zie de codeconventies.
- 33 notebooks zonder grond om notebook te zijn, en het ontbreken van de
  browser-uitvoering die notebooks voor de student zinvol maakt, zie de
  technische conventies. Het waren er 39; de vijf van week 5 hebben nu
  uitvoerbare cellen, en `lectures/3b_functies_aanroepen` is een `.md` geworden.
- 11 van de 22 uitwerkingen staan als markdown-blok en worden dus nooit
  uitgevoerd, en 10 skeletcellen missen `skip-execution`, zie de technische
  conventies. Het waren er 15; de vier uitwerkingen van week 5 draaien nu bij de
  build.

Deze vijf worden niet in een aparte opruimactie weggewerkt maar per bestand
rechtgezet tijdens de inhoudelijke herziening. Ze staan hier zodat ze niet
opnieuw ontdekt hoeven te worden.

Een zesde stond hier tot 8 september 2026: `Opgave` en `Opdracht` door elkaar
als kop. Die is met werkitem #178 wél in één keer rechtgezet, en het verschil
zit in de aard van de ingreep. De vijf hierboven vragen per geval een oordeel
over de inhoud - welke naam hoort deze variabele, welke cel hoort te draaien -
en dat oordeel valt alleen te vellen door wie het bestand toch al herziet. Het
kopwoord vroeg dat niet: er was één regel nodig, en zodra die er lag was de
toepassing mechanisch. Wie hier een afwijking bij wil schrijven, toetst dus
eerst welk van de twee het is.

## Een conventie toevoegen of wijzigen

Komt er een afspraak bij, voeg haar toe aan het document waar ze thuishoort, en
neem het document zo nodig op in de tabel hierboven. Dit document legt de
gelding vast; de inhoud hoort ergens anders.

Blijkt een bestaande conventie in de praktijk niet te werken, wijzig haar dan
hier in plaats van er in losse bestanden van af te wijken. Een conventie waarvan
op drie plekken stilzwijgend wordt afgeweken, is geen conventie meer.

# Uitgangspunten en besluiten

Dit document legt vast waaróm het curriculum is zoals het is. De leerlijn zegt
wat er wanneer gebeurt; hier staan de principes eronder en de besluiten die tot
afwijkingen hebben geleid.

Dat laatste is de belangrijkste functie van dit document. Een besluit waarvan
de grond niet is opgeschreven, wordt vroeg of laat opnieuw gevoerd, meestal door
iemand die de oorspronkelijke discussie niet heeft meegemaakt.

Dit document is voor auteurs en docenten, niet voor studenten. Het staat buiten
`source/` en maakt geen deel uit van het boek.

## Herkomst

Het materiaal is een bewerking van **CS5** van Harvey Mudd College. De
ontwerpgedachten daarachter zijn beschreven in twee artikelen, en die zijn nog
steeds bruikbaar om keuzes te dragen:

- Alvarado, Dodds & Libeskind-Hadas, *Increasing Women's Participation in
  Computing at Harvey Mudd College*, ACM Inroads 3(4), december 2012.
- Klawe, *Increasing Female Participation in Computing: The Harvey Mudd College
  Story*, IEEE Computer, maart 2013.

Daarnaast geldt **Think Python** van Allen Downey als begeleidend boek.

### De oorspronkelijke opbouw van CS5

| Weken | Paradigma |
|---|---|
| 0 | State-machine programming (Picobot) |
| 1-3 | Functioneel programmeren |
| 4-6 | Machine-organisatie |
| 7-9 | Imperatief programmeren |
| 10-12 | Object-georiënteerd programmeren |
| 13-14 | Theoretische onderwerpen |

## De context waarin het vak draait

Twee gegevens die het materiaal zelf nergens vermeldt, maar die bij vrijwel elke
keuze meewegen.

### Een gemengde doelgroep

Het vak wordt gevolgd door studenten van drie profielen tegelijk: **software
engineering**, **netwerk- en security engineering** en **business en IT
management**. Ze krijgen hierna niet hetzelfde vervolg. Wat voor de ene groep een
opstap is naar een later vak, is voor de andere groep het enige moment waarop ze
het onderwerp zien.

Dat maakt relevantie geen retorische kwestie maar een harde eis: een onderwerp
dat alleen te verdedigen is vanuit één profiel, is voor een derde van de zaal
niet te verdedigen. Wie hier een onderwerp voorstelt, moet het voor alle drie
kunnen dragen.

### Drie bijeenkomsten per week

| Bijeenkomst | Vorm | Wat er gebeurt |
|---|---|---|
| 1 | College | Het onderwerp wordt geïntroduceerd |
| 2 | Werkcollege | Een opgave wordt gezamenlijk uitgewerkt |
| 3 | Practicum | Zelfstandig werken onder begeleiding aan de opgaven |

Deze indeling verklaart de mappen: `lectures/` hoort bij de eerste bijeenkomst,
`practicals/` bij het werkcollege, `problems/` bij het practicum. Ze is ook
relevant voor de vraag waar context hoort te zitten, want het werkcollege is de
plek waar een probleem gezamenlijk stap voor stap wordt opgebouwd.

## Het referentiemateriaal: tag `v1.0.0`

Tag **`v1.0.0`** (juni 2023) bevat de vertaalde CS5-opgaven zoals ze
oorspronkelijk waren. Dat is de referentie bij de herziening: niet om naar terug
te keren, maar om op terug te vallen wanneer onduidelijk is wat een opgave
oorspronkelijk deed.

Die terugval is nodig omdat bij de latere bewerking de opbouw van veel opgaven is
gebroken. Op de oorspronkelijke opgaven viel genoeg aan te merken, ze vragen
veel leeswerk en zijn niet altijd strak geordend, maar ze hebben wel een
doorlopende lijn. Waar het huidige materiaal een fragment is, staat in `v1.0.0`
het geheel waar dat fragment uit komt.

Drie momenten zijn te onderscheiden:

| Tag | Wanneer | Opzet |
|---|---|---|
| `v1.0.0` | juni 2023 | 12 weken, CS5 zoals vertaald. Per week een reeks opgaven plus één leesopgave. Geen niveaus. |
| `v1.1.0` | april 2024 | De niveaus `opstap`, `basis` en `context` ingevoerd. De opgavenbibliotheek staat er nog; de leesopgaven staan nog in de repo maar niet meer in de inhoudsopgave. |
| nu | — | `context` heet `extra`. De bibliotheek en de leesopgaven zijn verdwenen. |

### De opgavenbibliotheek

In `v1.0.0` staat elke opgave als een eigen eenheid in `problems/<naam>/index.md`,
met eigen afbeeldingen, los van een week. De inhoudsopgave wijst er per week
naar. Ruim veertig opgaven, waarvan een aantal in het huidige materiaal niet meer
voorkomt.

Die opzet is op zichzelf het overwegen waard: een opgave die niet aan een
weeknummer vastzit, kan verplaatst worden zonder verbouwd te worden.

### De leesopgaven

`v1.0.0` heeft **twaalf leesopgaven, één per week**, in `readings/`. Artikelen
over waar het vakgebied op ingrijpt: algoritmen die discrimineren, een computer
die Jeopardy wint, zelfrijdende auto's, taal en denken.

Ze zijn volledig verdwenen. Dat is het meest directe verlies aan relevantie in
het hele materiaal, want dit was de plek waar het vak buiten zichzelf wees
zonder dat er een regel code aan te pas kwam. De vraag of ze terugkomen hoort in
de herziening thuis.

## Principes die we aanhouden

**Probleemoplossen, niet programmeerles.** Klawe vat de kern zo samen: *"Instead
of the typical focus on learning to program, CS5 emphasizes problem solving using
computational approaches."* Problemen komen bij voorkeur uit een ander vakgebied,
zodat de relevantie zichtbaar is. Bruikbaar als toets op een opgave: lost ze een
probleem op, of oefent ze alleen syntaxis?

**Meteen iets kunnen maken.** *"Students should be writing interesting programs
from day 1 (or perhaps day 0)."* Python heeft een week of twee nodig voordat een
student iets boeiends kan schrijven; daarom opent CS5 met Picobot.

**Gelijke startpositie.** Picobot staat vooraan omdat *"none of the students have
seen it before"*. Wie zonder ervaring binnenkomt, kan er net zo goed in zijn als
wie al programmeert. Dat neemt het effect weg dat sommigen alles al lijken te
weten, wat in de literatuur als demotiverend wordt aangemerkt.

**Ruimte om te herstellen.** De modules zijn tamelijk onafhankelijk gehouden,
*"to give students a reset"*: wie op één onderwerp vastloopt, kan het loslaten en
bij het volgende opnieuw instappen. Een strak lineaire opbouw waarin alles op
alles voortbouwt, verliest die eigenschap.

**Objecten laat.** *"The idea of covering objects late (or not at all) in an
introductory course has recently received positive attention, particularly in
light of educating computational thinkers rather than software engineers."*
Studenten begrijpen het ontwerp van klassen beter nadat ze de bouwstenen van
computatie beheersen. Dit houden we aan: objecten zitten in PGM2.

**Tooling is een drempel.** Editor, bestandssysteem en commandoregel zijn voor
beginners een obstakel op zichzelf. Dat rechtvaardigt aandacht voor tooling in
het materiaal én de wens code in de browser uitvoerbaar te maken.

**Code leren lezen.** Begrip van bestaande code is een eigenstandig doel, niet
alleen een opstapje naar zelf schrijven.

**Worked examples.** De opbouw leunt op voorgedane uitwerkingen.

## Besluitenregister

Per besluit staat de **aard** erbij, want die bepaalt of en hoe het heropend kan
worden. Een didactisch besluit weerleg je met argumenten of resultaten; een
organisatorisch besluit niet.

| Besluit | Aard | Status |
|---|---|---|
| Recursie is naar PGM2 verplaatst; imperatief komt eerst | organisatorisch | gesloten |
| De theoretische afsluiting is geschrapt | ervaring | gesloten |
| Schakelingen zijn geschrapt, binair is afgeslankt | organisatorisch | gesloten |
| Objecten pas in PGM2 | didactisch | staand, onderbouwd |
| Picobot opent PGM1 | didactisch | staand, onderbouwd |
| Opgaven in opstap, basis en extra | didactisch | **open** |
| Code uitvoerbaar in de browser | praktisch | open, uitvoering wijzigt |

### Recursie na de lussen

CS5 zet functioneel programmeren voorop met een expliciet argument: *"students
generally find recursion simpler to learn when it is the first programming
paradigm encountered, rather than learning it in comparison to the idioms of
looping and iteration."*

Wij wijken daarvan af. De reden is **niet didactisch maar organisatorisch**: bij
docenten en verantwoordelijken bestond onvoldoende draagvlak voor beginnen met
recursie. In hun eigen ervaring is het een laat en tamelijk esoterisch onderwerp,
en die ervaring wordt op eerstejaars geprojecteerd.

De resultaten geven geen aanleiding om dat te bestrijden: metingen met en zonder
recursie-eerst laten geen verschil zien, zeker niet voor studenten die zonder
voorkennis binnenkomen. Eerlijk geformuleerd is de afweging dus niet dat
recursie-eerst slechter is, maar dat het hier niet aantoonbaar beter is en het
verdedigen ervan meer kostte dan het opleverde.

**Dit besluit staat en wordt niet op didactische gronden heropend.** Wie het toch
ter discussie stelt, heeft nieuw draagvlak nodig, geen nieuw artikel.

Twee dingen die er wél uit volgen:

1. **Recursie krijgt een eigen verhaal.** In plaats van "een alternatief voor een
   lus" wordt het gebracht als *algoritmisch denken*: een andere kijk op hetzelfde
   probleem. Daarmee staat het op eigen benen in plaats van als vreemde variant
   op iets dat de student net geleerd heeft, en dat is precies de framing die het
   esoterisch doet lijken.
2. **Recursie wordt in PGM1 niet onderwezen.** Wat er in PGM1 week 3 over te
   vinden is, is bewust smal: bij de functies wordt getoond dát een functie
   zichzelf kan aanroepen, en niets meer. Het gedrag zelf wordt pas in PGM2
   bestudeerd. Dat is geen omissie maar het besluit in uitvoering.

   Daaruit volgt wel dat leeruitkomst **A4** in de verkeerde toetsmatrijs staat:
   PGM1 belooft ontwerpen van recursieve oplossingen op creëren-niveau voor 10%
   van het tentamen, terwijl het vak het onderwerp niet aanbiedt. Zie
   [leeruitkomsten.md](leeruitkomsten.md).

### De theoretische afsluiting

CS5 sluit af met computeerbaarheid en de grenzen van berekening, en keert daarbij
terug naar de eindige toestandsmachine die de student in week 0 als Picobot
tegenkwam: *"After students have twelve weeks of hands-on experience in creating
computation and building confidence, they are often surprised to learn (in a good
way) that there are some things that a computer provably cannot accomplish."*

Picobot opent die boog, de theorie sluit hem.

Bij hbo-studenten sloeg dat niet aan: te abstract. Het is geprobeerd en
losgelaten. Gevolg: Picobot blijft, de sluiting komt niet terug, en leeruitkomst
A5 over eindige toestandsmachines hoort daarmee uit de toetsmatrijs. Zie
[leeruitkomsten.md](leeruitkomsten.md).

### Schakelingen en binair

Binair en talstelsels stonden er niet op zichzelf. Ze hoorden bij **schakelingen**:
een inkijk in hoe een computer werkt, waarbij binaire representatie vanzelf ter
sprake komt. Toen de schakelingen verdwenen, bleef de rekenkunde over zonder de
vraag die haar betekenis gaf.

Daar kwam de doelgroep bij. Voor software- en netwerkstudenten komt het onderwerp
terug in een apart vak computerarchitectuur; business- en IT-managementstudenten
krijgen dat vak niet, en voor hen is de relevantie moeilijk hard te maken. Het
management beoordeelt het daarom als minder passend voor deze groep.

Het onderwerp is dus niet slecht, maar het is zijn drager kwijt. Wie het wil
behouden, moet ofwel de context terugbrengen ofwel het voor alle drie de
profielen kunnen verdedigen.

### De verdeling in opstap, basis en extra

De indeling komt van de docent die het oorspronkelijke materiaal heeft bewerkt.
Het idee erachter is bruikbaar en blijft:

| Niveau | Bedoeling |
|---|---|
| **opstap** | Vingeroefeningen: de syntaxis onder de knie krijgen |
| **basis** | Wat wij verwachten dat je kunt, oftewel toetsniveau |
| **extra** | De uitdaging |

De uitvoering is het probleem, niet het idee. Vrijwel alle oorspronkelijke
CS5-opgaven zijn onder *extra* geplaatst, en een ander deel is naar het
werkcollege verhuisd. Daarmee zit het merendeel van het materiaal, en vrijwel
alle context, in de laag die optioneel voelt. Zie [leerlijn.md](leerlijn.md) voor
de meting.

> **De derde laag heette eerst `context`.** Bij de invoering van de niveaus, in
> tag `v1.1.0`, waren het `opstap`, `basis` en `context`. De laag die het
> onderwerp in context bracht is daarna hernoemd naar *extra*. Die hernoeming
> beschrijft de verschuiving beter dan welke analyse ook: van *de toepassing*
> naar *het facultatieve*.

Twee gevolgen die in de herziening moeten worden opgelost:

1. **De uitdaging is optioneel geworden.** PGM1 wordt als rustig ervaren en PGM2
   komt hard aan. PGM1 hoort een vriendelijke introductie te blijven, maar de
   oplopende lijn erin moet scherper.
2. **Het onderwerp in context is verdwenen uit opstap en basis.** Een concreet
   ICT-probleem dat stap voor stap wordt opgelost is een dragend idee van CS5:
   zo wordt de relevantie van het vak zichtbaar. Opstap en basis zijn nu
   overwegend droge opgaven zonder context. Dat is voor opstap verdedigbaar,
   want vingeroefeningen zijn nu eenmaal kaal, maar voor basis niet.

Dit is een spanningsveld en geen eenvoudige keuze: syntaxis moet geoefend worden
en dat gaat het snelst kaal, terwijl relevantie juist context vereist.

## Een besluit toevoegen

Neem het op in de tabel met zijn aard en status, en licht het eronder toe als de
grond niet in één regel past. Vermeld bij een gesloten besluit ook wat er zou
moeten veranderen om het te heropenen. Dat is het verschil tussen een archief en
een bruikbaar register.

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
2. **De volgorde van introductie is intact gebleven, de diepte niet.** Recursie
   wordt nog steeds vóór de lussen geïntroduceerd, in PGM1 week 3. Wat verdween
   is de uitwerking: CS5 gaf er drie weken aan, hier is het één college. Zie de
   leerlijn voor het gat dat dat oplevert ten opzichte van leeruitkomst A4.

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

## Een besluit toevoegen

Neem het op in de tabel met zijn aard en status, en licht het eronder toe als de
grond niet in één regel past. Vermeld bij een gesloten besluit ook wat er zou
moeten veranderen om het te heropenen. Dat is het verschil tussen een archief en
een bruikbaar register.

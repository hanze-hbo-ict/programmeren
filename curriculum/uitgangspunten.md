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

Deze indeling verklaart de directories: `lectures/` hoort bij de eerste bijeenkomst,
`practicals/` bij het werkcollege, `problems/` bij het practicum. Ze is ook
relevant voor de vraag waar context hoort te zitten, want het werkcollege is de
plek waar een probleem gezamenlijk stap voor stap wordt opgebouwd.

#### Twee erkende afwijkingen

De indeling is het uitgangspunt en niet een rooster dat elke week haalt. Bij het
schrijven van de docentenhandleidingen (#182) zijn twee afwijkingen vastgesteld en
erkend; ze staan hier zodat een volgende weekherziening ze niet opnieuw als
conflict afleidt.

**Week 1 volgt een flexibele indeling.** Er is geen `problems/` en geen
`solutions/` voor week 1, en de Picobot-opdrachten beginnen in bijeenkomst 2 als
plan (`source/lectures/1b_picobot.md`) en worden in bijeenkomst 3 geprogrammeerd
(`source/practicals/1_picobot.md`). De twee bijeenkomsten lopen dus in elkaar
over; wat in bijeenkomst 2 blijft liggen, gaat naar bijeenkomst 3. De tijdsblokken
in de handleiding van week 1 zijn daarom richtsnoer en geen strak rooster.

**Week 2 laat een practicum naar de derde bijeenkomst vallen.** Week 2 draagt twee
onderwerpen, en het werkcollege wordt gevuld door `2b` plus
`practicals/2_rochambeau`; `practicals/2_sequenties_en_data` schuift daardoor naar
de derde bijeenkomst, naast de drie opgavebundels.

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

### Het materiaal doorzoekbaar maken

De tag zelf is lastig doorzoekbaar; `git show` per bestand werkt niet als je nog
niet weet wat je zoekt. Pak het daarom lokaal uit:

```bash
mkdir -p referentie/cs5
git archive v1.0.0 topics course problems readings _toc.yml | tar -x -C referentie/cs5
```

`referentie/` staat in `.gitignore`: het materiaal zit al in de
geschiedenis en hoeft niet nog een keer in de boom. Ripgrep slaat genegeerde
directories over, dus zoek er expliciet in met `rg --no-ignore ... referentie/`.

Begin bij `_toc.yml`. Daar staat welke opgaven bij welke week hoorden, en dat is
de snelste ingang naar wat er omheen stond.

### De opgavenbibliotheek

In `v1.0.0` staat elke opgave als een eigen eenheid in `problems/<naam>/index.md`,
met eigen afbeeldingen, los van een week. De inhoudsopgave wijst er per week
naar. Ruim veertig opgaven, waarvan een aantal in het huidige materiaal niet meer
voorkomt.

Die opzet is op zichzelf het overwegen waard: een opgave die niet aan een
weeknummer vastzit, kan verplaatst worden zonder verbouwd te worden.

### De leesopgaven

`v1.0.0` heeft **twaalf leesopgaven, één per week**, in `readings/`: artikelen
over waar het vakgebied op ingrijpt, zoals algoritmen die discrimineren, een
computer die Jeopardy wint, zelfrijdende auto's, taal en denken.

Ze zijn bewust losgelaten. Interessant materiaal, maar het bleek niet in de
beschikbare tijd in te passen. Zie het besluitenregister.

Wat er wel uit volgt: CS5 liet de relevantie van het vak langs twee wegen zien,
via de opgaven én via de leesopgaven. Nu die tweede weg is vervallen, rust dat
volledig op de opgaven. Dat maakt het hierboven beschreven probleem met de laag
`extra` zwaarder dan het op zichzelf al is.

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

## Mutabiliteit: een grens die we bewaken

CS5 kreeg deze grens gratis. De eerste weken zijn functioneel programmeren, en
daarin bestaan side effects niet: een functie rekent iets uit en geeft het terug.
Begint daarna het imperatieve deel, dan is verandering een *nieuw vermogen* dat
je kunt benoemen, voordoen en nuttig inzetten. De student heeft een wereld zonder
gekend, dus hij ziet wat erbij komt.

Door de herordening zijn die functionele weken weg. De **vorm** bleek echter nog
intact. Gemeten over PGM1 week 1 tot en met 6 wordt een lijst nergens ter plekke
gewijzigd, op één plek na, en muterende methodes komen helemaal niet voor. De
eerste echte mutatie staat in `lectures/7a_lists_advanced`, en daar staat ze
meteen naast `deepcopy`.

Wat verdwenen is, is dus niet de grens maar het **label**. Niemand wijst hem aan.
De student merkt niet dat hij zes weken in een wereld zonder verandering heeft
gewerkt, en krijgt in week 7 mutatie en aliasing in één adem, als techniek in
plaats van als begrip. `deepcopy` lost dan een probleem op waarvan hij niet wist
dat het bestond.

**Besluit: de grens blijft, en wordt benoemd.**

| Waar | Wat geldt |
|---|---|
| PGM1 week 2 tot en met 6 | Een functie rekent iets uit en geeft het terug. Wat je meegeeft verandert niet. |
| PGM1 week 7 | De grens, voor mutatie. Eerst *dat* je een lijst kunt wijzigen en wat dat oplevert, daarna pas dat twee namen naar dezelfde lijst kunnen wijzen, en daarna pas het kopiëren. Objectmethoden vallen niet op deze grens; die verschuiven naar PGM2 week 1. |
| PGM2 | Een object is data plus de handelingen daarop, en dus een bundel staat die verandert. Het woord ervoor bestaat dan al. |

Drie dingen volgen hieruit.

**Week 3 zegt het één keer hardop.** Bij de functies: hier rekent een functie iets
uit en geeft het terug, en verandert niets aan wat je meegeeft. De BSN-opgave
demonstreert dat al zonder er iets voor te hoeven doen; alle zes functies geven
een waarde terug en geen van alle verandert iets.

**Week 7 keert de volgorde om.** Nu komen mutatie en aliasing tegelijk. Het
vermogen hoort eerst, de valkuil daarna. Game of Life in `problems/7_extra`
draait volledig om bijwerken en is daarmee de natuurlijke aanleiding.

**Objectmethoden vallen niet op dezelfde grens.** `L.append(x)` is én een
methode én een mutatie, maar week 7 laat mutatie zien via `L[i] = x`: dat
vraagt geen methodeaanroep. Methodeaanroep wordt voor het eerst geïntroduceerd
in PGM2 week 1, samen met dictionaries en sets. Tot en met PGM1 week 7 leeft de
student dus in een wereld zonder objecten.

Leeruitkomst P4 vroeg lange tijd letterlijk om "lijsten en strings en de
bijbehorende methodes" in PGM1, maar wordt daar al jaren niet meer op getoetst.
Dat staat als voorgestelde correctie in
[leeruitkomsten.md](leeruitkomsten.md#voorgestelde-correcties); dit besluit
loopt op die correctie vooruit. Zie
[codeconventies.md](../conventies/codeconventies.md).

### Het bord verandert niet in week 5

Boter-kaas-en-eieren in week 5 bouwt een bord en wijzigt het nooit. Dat past bij
de grens, maar het betekent wel dat de student een raster leert *lezen* en niet
*bijwerken*, terwijl week 7 vervolgens Game of Life vraagt, wat volledig om
bijwerken draait. De vraag was of die mutatievrije weken een verworvenheid zijn
die we beschermen, of een gevolg van het uitdunnen van het materiaal.

**Besluit: het bord verandert niet in week 5, en die grens wordt daar benoemd.**

Drie gronden. De mutatiegrens in week 7 is een gesloten, onderbouwd besluit, en
het hele punt ervan is dat de student een wereld zonder verandering heeft gekend
voordat verandering een nieuw vermogen wordt. Week 5 heeft zonder mutatie ruim
genoeg te doen. En `problems/7_extra.md` leert `create_board` en `print_board`
zelf opnieuw aan; wat week 7 werkelijk nodig heeft is dat de student een raster
kan bouwen en doorlopen.

De prijs is benoemd: de student leert een raster lezen en niet bijwerken, en
week 7 draagt dan drie nieuwe dingen tegelijk. De verzachting is dat week 5
afsluit op precies dat ene probleem - één vakje van een raster veranderen
terwijl de rest blijft staan - en het bij naam doorverwijst naar week 7. Die
afsluiting staat in `source/lectures/5a_geneste_lus.ipynb` en, woordelijk
dezelfde zin, in `source/problems/5_basis.ipynb`.

Wat er zou moeten veranderen om dit te heropenen: dat de mutatiegrens zelf
verschuift. Zolang die op week 7 ligt, volgt dit besluit eruit. Blijkt in de
zaal dat week 7 met drie nieuwe onderwerpen tegelijk te zwaar wordt, dan is dat
een reden om de grens te heroverwegen, niet om week 5 er alvast overheen te
laten stappen.

### De parameternamen van `board.py` blijven zoals ze zijn

`source/problems/assets/board.py` roept op regels 91-94 vier zoekfuncties aan en
definieert ze op regels 173-224 zelf opnieuw, met de signature
`(ch, r_start, c_start, a, n)`. Practicum 5b laat de student dezelfde functies
schrijven met de signature `(char, row_start, col_start, array, n)`.

**Besluit: de parameternamen in week 5 blijven zoals de opgave ze heeft, en
`board.py` wordt niet aangeraakt.** Omdat `board.py` de functies zelf definieert,
importeert het nooit het werk van de student en breekt de afwijking mechanisch
niets. `board.py` wordt op precies één plek aangeboden:
`practicals/13_vier_op_rij_speler.md` regel 343, PGM2 week 6.

## Besluitenregister

Per besluit staat de **aard** erbij, want die bepaalt of en hoe het heropend kan
worden. Een didactisch besluit weerleg je met argumenten of resultaten; een
organisatorisch besluit niet.

**Status gaat over het besluit, niet over het materiaal.** `gesloten` betekent dat
de discussie voorbij is, niet dat de repository het volgt. Dat verschil is geen
haarkloverij: schakelingen stonden sinds de herindeling op `gesloten` terwijl er
25 MB logisimmateriaal in de inhoudsopgave zat, en "recursie naar PGM2" is in het
materiaal en beide tentamens uitgevoerd maar in de toetsmatrijs niet.

Zet daarom achter de status of het materiaal al volgt, zodra dat bekend is:
**uitgevoerd**, **deels uitgevoerd** (met erbij wat er nog niet volgt), of **nog niet
uitgevoerd**. Staat er niets, dan is het niet vastgesteld en niet: het is gedaan.
Wie een besluit neemt weet meestal nog niet of het is uitgevoerd; wie een veegronde
draait wel.

| Besluit | Aard | Status |
|---|---|---|
| Recursie is naar PGM2 verplaatst; imperatief komt eerst | organisatorisch | gesloten, uitgevoerd; de matrijs volgt sinds 1 september 2026 |
| De theoretische afsluiting is geschrapt | ervaring | gesloten |
| Schakelingen zijn geschrapt, binair is afgeslankt | organisatorisch | gesloten, uitgevoerd |
| De wekelijkse leesopgaven zijn vervallen | praktisch | gesloten |
| Bestanden naar PGM1, excepties blijven in PGM2 | didactisch | staand, onderbouwd |
| Mutatie pas vanaf PGM1 week 7, en als grens benoemd | didactisch | staand, onderbouwd |
| Canonieke Python aanbieden, mechanisme later uitleggen | didactisch | staand, onderbouwd |
| Het bord verandert niet in week 5; de grens wordt daar benoemd | didactisch | gesloten |
| De parameternamen van `board.py` blijven zoals ze zijn | praktisch | gesloten |
| De vastgestelde matrijs wijzigt niet als bijvangst; bevindingen gaan naar *Voorgestelde correcties* | organisatorisch | staand, onderbouwd |
| Het oefententamen is representatief en verandert voorlopig niet | organisatorisch | staand |
| Leesvragen mogen fout aflopen; de fout is het antwoord | didactisch | staand, onderbouwd |
| Onderdompeling mag vooraf gaan aan uitleg | didactisch | staand; de grens is nog een afleiding |
| Studenten leveren geen werk in; opdrachten zijn oefening | organisatorisch | gesloten, **nog niet uitgevoerd**: `source/` draagt nog inleverinstructies |
| Tot en met week 4 ligt de nadruk op lezen en begrijpen; schrijven begint wel | didactisch | staand, onderbouwd |
| Een weekpagina vat samen wat volgt en waarop het voortbouwt | praktisch | gesloten, nog niet uitgevoerd (#167) |
| Elk opgaveniveau hoort een uitwerking te hebben | didactisch | gesloten, nog niet uitgevoerd; 17 van de 31 ontbreken |
| Week 4 krijgt een lusrecept van vijf vragen, in `4a_lussen` | didactisch | gesloten, **uitgevoerd** met #153; week 5 pikt het nog niet op (#163) |
| Recursie gaat uit PGM1 week 4, op alle vier de plekken | organisatorisch | gesloten, **deels uitgevoerd**: 1 van 4 met #153 (midtermopdracht 13). `unique` (2×) en `find_number_of_decimals` staan er nog; zie ronde twee en #126 |
| Eerst de weken van PGM1 afronden; het materiaal moet zo snel mogelijk live | organisatorisch | staand |
| Een docentenhandleiding gaat per week en dekt het materiaal en de opgaven, met een didactische invalshoek | didactisch | gesloten, deels uitgevoerd: week 1 staat er, week 2 nog niet |
| Handleidingen zijn repo-materiaal en geen onderdeel van het boek | organisatorisch | gesloten, uitgevoerd |
| Objectmethoden pas vanaf PGM2 week 1, los van de mutatiegrens in PGM1 week 7 | didactisch | staand, onderbouwd |
| Dictionaries en de Markov-opgave verhuizen van PGM1 week 7 naar PGM2 week 1 | didactisch | staand, nog niet uitgevoerd |
| Objecten pas in PGM2 | didactisch | staand, onderbouwd |
| Picobot opent PGM1 | didactisch | staand, onderbouwd |
| Opgaven in opstap, basis en extra | didactisch | **open** |
| De student werkt lokaal in VS Code; de browser is verrijking | didactisch | staand, onderbouwd |
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

Wel moet de prijs ervan bekend zijn, want die is bij de uitvoering onzichtbaar
gebleven. In CS5 zijn functies en recursie hetzelfde onderwerp: het functionele
paradigma komt in de weken 1 tot en met 3, en vrijwel elke opgave over functies
gebruikt recursie. `feest_met_functies`, `python_turtles` en `caesar_op_orde`
doen dat allemaal. Met recursie zijn dus ook de functie-opgaven meeverhuisd naar
PGM2.

Daardoor heeft **PGM1 week 3 geen inhoudelijke opgave meer**, ook niet in het
referentiemateriaal: alles wat er lag is elders terechtgekomen. Het is de dunste
week van de cursus terwijl ze P5 en A2 draagt, samen 20% van het tentamen. Dat is
geen slordigheid maar een gevolg van dit besluit, en het betekent dat hier nieuw
materiaal geschreven moet worden in plaats van teruggehaald.

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

   Leeruitkomst **A4** stond daardoor in de verkeerde toetsmatrijs: PGM1 beloofde
   ontwerpen van recursieve oplossingen op creëren-niveau voor 10% van het
   tentamen, terwijl het vak het onderwerp niet aanbiedt. Op 1 september 2026 is
   zij verplaatst naar de PGM2-matrijs, waar zij **A6** heet. Zie
   [leeruitkomsten.md](leeruitkomsten.md).

### De theoretische afsluiting

CS5 sluit af met computeerbaarheid en de grenzen van berekening, en keert daarbij
terug naar de finite state machine die de student in week 0 als Picobot
tegenkwam: *"After students have twelve weeks of hands-on experience in creating
computation and building confidence, they are often surprised to learn (in a good
way) that there are some things that a computer provably cannot accomplish."*

Picobot opent die boog, de theorie sluit hem.

Bij hbo-studenten sloeg dat niet aan: te abstract. Het is geprobeerd en
losgelaten. Gevolg: Picobot blijft, de sluiting komt niet terug, en leeruitkomst
A5 over finite state machines hoort daarmee uit de toetsmatrijs. Zie
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

Het materiaal is op 31 augustus 2026 ook daadwerkelijk verwijderd. Het besluit
stond al sinds de herindeling op *gesloten*, maar `support/logisim.md` stond nog in
de inhoudsopgave, met een Java-applicatie van 22 MB, de schakelbestanden en tien
schermafbeeldingen; geen enkele week verwees ernaar. Daarnaast zijn acht
afbeeldingen bij `lectures/images/6/` weggehaald die bij binair en talstelsels
hoorden en nergens meer werden aangehaald. Wie het onderwerp ooit terugbrengt, haalt
het uit tag `v1.0.0`; dat is de weg die dit document voor al het geschrapte
materiaal voorschrijft.

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

### Eén opgave over drie niveaus

De manier om beide gevolgen tegelijk op te lossen: **breek een grote opgave op en
verdeel haar over de drie niveaus**, zodat de student al oefenend naar een complete
oplossing toewerkt.

De opstap oefent dan de losse handelingen die de opgave nodig heeft, de basis lost
er een werkzame kern mee op, en de extra is de uitbreiding voor wie verder wil.
Alle drie in dezelfde context, met hetzelfde probleem. Wie alleen de basis doet,
heeft iets af; wie doorgaat, bouwt verder op wat hij al heeft in plaats van aan iets
nieuws te beginnen.

Dat lost allebei de gevolgen hierboven op. De uitdaging is niet meer optioneel maar
de bovenste tree van een trap die de student al beklimt, en de context zit in alle
drie de lagen in plaats van alleen in de laatste - precies waar de derde laag
oorspronkelijk `context` voor heette.

**De meting wijst aan waar dit het meest oplevert.** Gemeten op 1 september 2026,
in woorden per laag:

| week | opstap | basis | extra | extra-aandeel |
|---|---|---|---|---|
| 2 | 1.078 | 1.100 | 463 | 18% |
| 3 | 229 | 1.108 | 162 | 11% |
| 4 | 574 | 1.020 | 1.025 | 39% |
| **5** | 649 | 2.897 | **5.354** | **60%** |
| 6 | 337 | 1.319 | 760 | 31% |
| **7** | 504 | 1.087 | **3.713** | **70%** |

De basislaag is opmerkelijk stabiel, rond de 1.100 woorden per week. De scheefheid
zit niet in te dunne opstap en basis maar in **twee uitschieters**: Mandelbrot
(5.354 woorden) en Game of Life (3.713). Die twee opgaven zijn samen groter dan alle
basisopgaven van PGM1 bij elkaar, en het zijn allebei opgaven die in CS5 het
*practicum* van hun week waren - het dragende werk, niet het optionele.

Daar is dit dus geen herverdeling maar een herstel: materiaal dat ooit droeg, weer
laten dragen.

**Wat het niet is.** Niet elke extra-opgave hoeft opgebroken. Een korte uitdaging
naast een volle basis is prima; week 2 en 3 laten zien dat het kan. En opbreken is
geen reden om een opgave langer te maken - de bedoeling is dat dezelfde inhoud over
drie niveaus wordt verdeeld, niet dat er drie keer zoveel komt te staan.

### Bestanden en excepties

De twee gaten in de toetsing worden verschillend opgelost, en dat is opzet.

**Bestanden gaan naar PGM1.** Het lezen en schrijven van een bestand vraagt geen
enkel begrip dat de student daar nog niet heeft, en er ligt al materiaal: de
beeldbewerking leest en schrijft bestanden, en de Markov-opgave in week 7 leest
een tekstbestand.

**Excepties blijven in PGM2**, om twee redenen die elkaar versterken. Ze horen bij
robuustheid, en die vraag komt pas op als een programma groot genoeg is om ergens
te breken. En zwaarderwegend: een exceptie *is* een object, en de klassenhiërarchie
is precies wat het mogelijk maakt om specifiek af te vangen in plaats van alles.
Excepties onderwijzen vóór objecten en overerving betekent de constructie
aanleren zonder de reden waarom ze werkt.

Daaruit volgt dat de twee leeruitkomsten van plaats wisselen met recursie:

| Vak | Eruit | Erin |
|---|---|---|
| PGM1 | A4 recursie, 10% | P3 bestanden, 10% |
| PGM2 | P3 bestanden, 10% | recursie, 10% (heet daar **A6**) |

Beide matrijzen blijven op 100% sluiten, en beide vakken toetsen voortaan wat ze
onderwijzen. PGM2 moet excepties dan wel daadwerkelijk gaan behandelen; nu staat
`try`/`except` daar uitsluitend in gegeven code.

### Canonieke vormen, mechanisme later

De cursus legt nadruk op logische handelingen: open een bestand, lees het, sluit
het. In de praktijk combineert Python die handelingen tot één constructie:

```python
with open(filename) as file:
    for line in file:
        ...
```

De keuze is dan of je de losse handelingen voorop stelt of meteen de vorm
aanleert die iedereen gebruikt. **Wij bieden de canonieke vorm aan**, om drie
redenen.

**Er valt niets af te leren.** Wie `open` en `close` los leert, moet later zowel
een nieuwe vorm leren als de oude afwennen. Wie `with` leert, krijgt er alleen
uitleg bij.

**Als frase is het wel degelijk een logische handeling**: *open dit bestand
zolang dit blok duurt*. Dat is eerder duidelijker dan twee statements die de
student zelf moet onthouden te paren.

**Het mechanisme kan wachten, net als bij `open` zelf.** Niemand legt in week 6
uit wat een filedescriptor is. `with` bestaat om het sluiten te garanderen ook
als er iets misgaat, en dat is exceptieterritorium: in PGM2 landt het naast de
excepties en heeft het daar zijn reden.

Prettige bijkomstigheid: deze vorm roept geen enkele methode aan, en past dus
binnen de regel dat objectmethoden in PGM1 wegblijven. De variant zonder `with`
zou dat ook doen, maar laat het bestand open en leert precies de gewoonte aan
waarvoor `with` bestaat.

### Wat er aan de leeruitkomsten mag veranderen

De leeruitkomsten in [leeruitkomsten.md](leeruitkomsten.md) zijn tot nu toe als
volledig gegeven behandeld. Dat is te strikt. Het gaat niet om een slot maar om een
**procedure**, en die staat in dat document zelf: er is een **vastgestelde matrijs**,
en daaronder een lijst met **voorgestelde correcties**.

**Wat er niet gebeurt.** De vastgestelde matrijs wordt niet gewijzigd als bijvangst
van materiaalwerk. Wie bij het herzien van een week merkt dat een uitkomst niet
klopt, past de matrijs niet aan; dat zou de bindende laag laten meebewegen met wat
er toevallig is geschreven, en dan bindt zij niets meer.

**Wat er wel gebeurt.** Zo'n bevinding gaat naar *Voorgestelde correcties*, met de
bevinding en een voorstel. Dat geldt voor alles: een weging die niet klopt met wat
er getoetst wordt, een uitkomst die in de verkeerde matrijs staat, en ook een
formulering die niet meer beschrijft wat het vak doet - zie de rij over PGM1 P4, die
bij de knip tussen mutatie en methodeaanroep is toegevoegd. Er staat op dit moment
niets in de weg dat een voorstel later wordt overgenomen; wat vastligt is dat het
een besluit vraagt en geen zijdelingse wijziging is.

**Met de gewichten binnen een vak** is meer ruimte, want die raken geen externe
afspraak: weegt een uitkomst zwaarder dan het materiaal rechtvaardigt, dan is dat te
herverdelen zolang het totaal per vak klopt. Schuiven tussen PGM1 en PGM2 kan niet.

Wat dit betekent voor een ontwerper: kan een week een uitkomst niet dragen, dan is
dat een bevinding en geen vrijheid. Ze gaat als open vraag naar de poort, en wat
daar wordt besloten landt in de matrijs of in de correctielijst. Wat níét mag is de
matrijs stilzwijgend anders lezen dan hij staat.

### Waar de student werkt

De student werkt op zijn eigen machine, in VS Code. Dat is niet alleen praktisch:
het is een competentie. Een ICT'er werkt met een echte ontwikkelomgeving, en hoe
eerder hij daar thuis raakt, hoe minder die omgeving hem later in de weg zit. Week
0 is er dan ook grotendeels aan gewijd.

Uitvoering in de browser is een **verrijking**, geen vervanging. Zij was er in de
Jupyter Book-versie via het raketicoon en veel studenten gebruikten haar
daadwerkelijk; sinds de Sphinx-migratie ontbreekt zij. Zie het werkitem over
Pyodide.

Dit besluit is genomen omdat het materiaal het tegendeel liet zien. Twee practica
in week 2 stonden na elkaar in de inhoudsopgave met onverenigbare werkwijzen: het
eerste opende met een checklist "Python geïnstalleerd, VS Code geïnstalleerd", het
tweede stuurde de student naar een raketicoon dat niet meer bestaat. Wie materiaal
schrijft dat een omgeving veronderstelt, gaat uit van de lokale; komt de
browseruitvoering terug, dan is dat winst en geen ander uitgangspunt.

### Wat er nu voorgaat: de weken afmaken

De prioriteit ligt bij het **afronden van PGM1 per week**: onderwerp, opgaven,
uitwerkingen en docentenhandleiding compleet, zodat het materiaal live kan. Wat
daar niet aan bijdraagt, wacht.

Dat betekent twee dingen voor wat er openstaat.

**Het oefententamen verandert voorlopig niet.** Het is representatief voor het
tentamen dat wordt afgenomen; de onderwerpen en de aard van de vragen wijken
nauwelijks af. Vastgesteld door de vakdeskundige, want het echte tentamen staat
niet in de repository.

**De weging in de toetsmatrijs wacht.** Met de verplaatsing van de
recursie-uitkomst naar PGM2 telt PGM1 90% en is er geen uitkomst op
creëren-niveau meer. Dat is een reële vraag, maar niet er een die het afronden
van een week in de weg staat, en zij is beter te beantwoorden als de weken af
zijn. Zie *Voorgestelde correcties* in [leeruitkomsten.md](leeruitkomsten.md).

Bij die weging hoort één meting die de afweging bepaalt en die eerder verkeerd is
weergegeven. Van de negentig punten in het PGM1-oefententamen vraagt alleen
**opgave 6** (15 punten) om zelf een aanpak bedenken. Opgave 7 is met 25 punten de
grootste, maar schrijft de opdeling voor: *"Maak gebruik van lus(sen), de functie
`count_char(zin, let)` en een lijst met alle letters van het alfabet."* De student
voert daar een gegeven ontwerp uit.

Dat raakt twee uitkomsten. **A3** (ontwerpen, analyseren, 10%) wordt met 15 punten
iets zwaarder getoetst dan de matrijs zegt - niet genoeg voor een verdubbeling.
En **A2** (problemen opdelen, 10%) zou juist door opgave 7 gedragen moeten worden,
maar die opgave doet het opdelen voor de student. Vijfentwintig punten die een
uitkomst zouden moeten dragen en het niet doen.

Wie de weging later herziet: de vraag is niet alleen hoe de percentages moeten,
maar of de toets toetst wat hij zegt te toetsen. Zolang het oefententamen niet
verandert, is dat een vraag over de matrijs en niet over de toets.

### Wat een docentenhandleiding is, en waar hij staat

Twee besluiten, genomen door de vakdeskundige bij de poort van #182 op
5 september 2026.

**Een docentenhandleiding gaat per week en dekt het materiaal en de opgaven, met
een didactische invalshoek.** Dus niet een handleiding per college, ook niet in de
weken met twee colleges. Hij beschrijft hoe je een onderdeel brengt, hoeveel tijd
eraan gaat, waar studenten op vastlopen en wat je doet als een opdracht niet
uitkomt. Hij is geen uitwerkingenboek: de uitwerkingen staan in `solutions/`, en
waar die voor een collegeopdracht niet bestaan, geeft de handleiding een kort
antwoord van hooguit een regel. Dit besluit heropent wie kan laten zien dat een
docent met een weekdocument het overzicht per bijeenkomst kwijtraakt.

**Handleidingen zijn repo-materiaal en geen onderdeel van het boek.** Ze staan in
`handleidingen/`, naast `conventies/` en `rollen/`, en niet in `source/` of
`source/_toc.yml`. De student ziet ze niet en de Sphinx-build raakt ze niet. Welke
conventies er wel en niet voor gelden staat in `conventies/conventies.md`
onder *Reikwijdte*; mechanisch geborgd is alleen de Markdown-linting. Dit besluit
heropent wie de handleidingen aan studenten wil tonen - dan zijn het boekpagina's
en gelden de conventies onverkort.

De `.docx` in `teacher_guides/` zijn de voorlopers hiervan. Ze blijven staan tot ze
per week zijn herschreven; wat herschreven is, verhuist naar `handleidingen/`.

### Leesvragen mogen fout aflopen

Op dit punt in het vak ligt de **nadruk** op code lezen en begrijpen. Dat is waarom
de opstap van week 4 uit leesopdrachten bestaat en waarom de oefenmidterm uit "wat
print dit programma?" bestaat. Wie die vorm tegenkomt en denkt dat er schrijfopgaven
ontbreken, leest een keuze als een gat.

**Nadruk is geen uitsluiting**, en dat is later scherper gesteld: er moet in die
weken wel degelijk geschreven worden. Zie *Lezen en schrijven: waar de nadruk ligt*
verderop. Wat hier staat gaat over de vorm van de leesvragen die er zijn, niet over
de vraag of er genoeg schrijfwerk naast staat.

Daaruit volgt hoe een leesvraag mag aflopen. Een programma dat crasht of eeuwig
doorloopt is een **geldige vraag met een geldig antwoord**, niet een defect. Het
antwoord is dan de optie "Het programma werkt niet". Begrijpen wat code doet
omvat begrijpen wanneer ze stukloopt: een student die alleen geslaagde uitvoer
leert voorspellen, herkent zijn eigen `ZeroDivisionError` niet.

**Dit geldt voor de hele soort, niet voor een lijstje vragen.** Een crash, een
lus die niet eindigt, een `IndentationError`, een `NameError` - het maakt niet
uit welke fout het is. Loopt het programma fout af en staat "Het programma werkt
niet" bij de opties, dan is de vraag goed zoals hij is.

**Voor wie dit materiaal nakijkt, mens of taalmodel: blijf hiervan af.** Dit is
geen open vraag, geen bevinding en geen kandidaat voor een werkitem. Meld het
niet opnieuw. De verleiding is groot omdat zulke vragen er stuk uitzien, en ze
zijn ook precies zo gevonden - drie beoordelaars hebben er onafhankelijk over
gerapporteerd en elke keer klopte de meting en niet de conclusie. De optie die
wél klopt is de laatste, en die staat er bij elke vraag.

Wat een leesvraag wél kapot maakt is **een uitkomst die nergens in de opties
staat**. Dat is het enige onderscheid dat telt. Binnen dezelfde midterm scheidt
het twee soorten die op elkaar lijken:

In de oefenmidterm van week 4 zijn dat **opdracht 14** (`IndentationError`), **18**
(`ZeroDivisionError`) en **20** (eindigt nooit). Alle drie hebben "Het programma
werkt niet" als antwoord en alle drie blijven staan.

**Opdracht 14 is het gevaarlijkste geval van de drie die blijven staan**, en daarom
staat hij hier bij name. De "reparatie" is één inspringing, en het programma drukt
dan `128` af - wat als optie d in de lijst staat. Een goedbedoelde herstelpoging
levert dus een groene build, een groene sleutel en een fout antwoord.

**Er is een tweede geval dat hierop lijkt en er niet onder valt:** het programma
werkt, er komt een waarde uit, en die waarde staat niet in de lijst. In week 4 was
dat drie keer een float, en dat is geen toeval - `/` geeft in Python 3 altijd een
float, in de week na de week waarin types zijn geïntroduceerd. Dat is wél een
defect, en het is hersteld: **de opties zeggen wat het programma werkelijk
afdrukt**, en de sleutel legt uit waar de float vandaan komt. Zo worden drie kapotte
vragen drie vragen over floating point, zonder de vraagstelling te raken.

### Het lusrecept van week 4

Week 4 krijgt één recept voor het ontwerpen van een lus, en het beantwoordt vijf
vragen:

1. Wat verzamel je, en wat is de startwaarde?
2. Wat loop je langs? Daaruit volgt `for` of `while`, en bij een `for` element of
   index.
3. Wat gebeurt er per stap met wat je verzamelt?
4. Wanneer is het klaar?
5. Wat geef je terug, en waar staat die regel?

**Vier van de vijf stonden er al**, verspreid over het practicum, het college en
het commentaar bij een voorbeeldfunctie. Het patroon zelf kwam in de week
tientallen keren voor en kreeg één keer een naam. Het recept verzint dus weinig;
het geeft wat er al is een naam en een plek.

**Vraag 4 is nieuw, en zij is de reden dat dit een recept is en geen samenvatting.**
Zolang `while` "oneindige herhaling" heet, is stoppen een eigenschap van de
constructie. Het is het tegenovergestelde: bij een `while` levert de schrijver het
stopmoment. Dat idee komt uit *How to Design Programs*, waar het aantonen dát een
functie eindigt een aparte ontwerpstap is.

**Het landt in `4a_lussen`**, na "Denken in lussen", en niet in een tweede college.
Een tweede college verplaatst de oefenmidterm naar de practicumsleuf, en die is
bezet door CodingBat - het enige zelfcontrolerende schrijfwerk van de week.

**Het gearchiveerde `lectures/4b_lussen_ontwerpen.ipynb` is niet overgenomen.**
Dat notebook (commit `587e3800`, verwijderde branch `pgm1-25-26`, juli 2025) deed
hetzelfde met zes stappen. De regel *terughalen gaat vóór verzinnen* veronderstelt
beproefd materiaal, en die aanname geldt daar niet: de cel die het recept moet
voordoen is fout (`index_of` belooft `-1` in docstring én commentaar en geeft
`False`), het plan wijkt af van de code eronder, er staat geen enkele assertion in,
en de codeconventies worden op vier punten overtreden. Wel is de **vorm**
overgenomen, dezelfde die `extra/examples/design_recipe.md` heeft: genummerde
stappen, uitgewerkte voorbeelden met de stapnamen als regelcommentaar, en
opdrachten die eerst om een plan vragen en dan om de code.

### Lezen en schrijven: waar de nadruk ligt

**Tot en met week 4 ligt de nadruk op code lezen en begrijpen.** Dat is een opbouw
naar de midterm, die in week 5 wordt afgenomen: tot dat punt oefent de student
vooral het voorspellen van wat code doet, inclusief de fouten die code kan
opleveren.

**Nadruk is geen uitsluiting.** Er moet in die weken wel degelijk geschreven worden,
en er moet een begin mee worden gemaakt - waar het nodig is, hoort het er te zijn.
Wat hier niet staat is een streefverhouding, en dat is met opzet: het gaat om waar
het zwaartepunt ligt en niet om een getal dat een ontwerp moet halen.

De aanleiding was een week waarin het voorspellen het schrijven ruim vijf keer
overtrof, met een kwart van die leesvragen letterlijk uit het college overgenomen.
Die verhouding is op zichzelf geen bezwaar - de nadruk hóórt daar te liggen - maar
de dubbelingen zijn het wel, en of er genoeg geschreven wordt is een inhoudelijke
vraag per week en geen rekensom.

Dit verklaart ook waarom een opstap uit leesopdrachten mag bestaan en waarom de
oefenmidterm uit leesvragen bestaat; zie *Leesvragen mogen fout aflopen*.

### Wat een weekpagina draagt

De weekpagina's van `source/course/` zijn nu een kop, een plaatje en een
inhoudsopgave. Ze horen kort samen te vatten **wat er die week volgt en wat de
student leert**, met een **terugverwijzing naar de vorige week** zodat de lijn
zichtbaar wordt.

**Over de status.** De vakdeskundige bracht dit aanvankelijk als een gedachte
("een gedachte is om ... mss. ook een terugverwijzing") en heeft het op 2 september
2026 desgevraagd bevestigd als besluit, inclusief de terugverwijzing en inclusief
dat het voor alle weken geldt. Het staat hier dus als `gesloten` en niet als
voorstel, maar de bron was een overweging en dat hoort zichtbaar te zijn.

De terugverwijzing is de reden dat dit een besluit is en geen redactie: zij maakt
van twaalf losse weken een leerlijn, en zij is precies wat een student mist die
niet weet waarom hij doet wat hij doet. Vergelijk *Wat een week aan een latere
week aflevert* in [leerlijn.md](leerlijn.md), dat hetzelfde doet voor auteurs.

**Dit geldt voor alle twaalf de weken**, niet alleen voor de week die op dat moment
wordt herzien. Uitvoeren mag per week meeliften met de herziening; het besluit
wacht daar niet op. Let op: `source/_toc.yml` heeft dertien weeksecties, want PGM2
week 6 heeft geen weekpagina.

**Te heropenen wanneer** blijkt dat studenten de samenvatting overslaan, of wanneer
de terugverwijzing bij herordening van de weken structureel achterloopt op het
materiaal - dan is zij een onderhoudslast in plaats van een leerlijn.

### Elk opgaveniveau hoort een uitwerking te hebben

**Een niveau zonder uitwerking is een omissie, geen keuze.** Ziet een lezer dat
opgaven geen uitwerking hebben, dan is dat een gebrek van de auteurs en het hoort
gerepareerd te worden. Er is dus geen "de opstap heeft er met opzet geen".

Bij de vaststelling ontbrak ruim de helft van de uitwerkingen. Dat is te veel voor
één ingreep en het hoeft ook niet in één keer: het liftt mee met de herziening van
de week waar het bij hoort. De inventarisatie hoort in de werkitems, niet hier.

**De vorm:** een uitwerking is een draaiende codecel en geen markdown-blok, zodat
de build haar controleert. Programma's die met opzet stuklopen tonen hun
foutmelding in plaats van een beschrijving ervan.

**Te heropenen wanneer** blijkt dat een gepubliceerde uitwerking bij een bepaald
niveau het leereffect schaadt - de opstap is de kandidaat, want daar controleert de
student nu door de cel te draaien. Dat is dan een besluit per niveau met een reden,
en niet de huidige toestand die zichzelf verdedigt.

### Studenten leveren niets in

**Er is geen inlevermoment en geen inleverplatform.** In `v1.0.0` was dat er wel -
het CS5-materiaal droeg per opgave een tabel met een bestandsnaam en een
inleverkanaal, en in de lopende tekst een weging in punten - maar dat geldt niet meer. Opdrachten zijn
oefening.

Twee dingen volgen daaruit voor wie materiaal herziet.

**Haal geen inlevertabellen terug uit het referentiemateriaal.** Ze staan nog in
`referentie/cs5/`, ze zien eruit als iets dat bij de migratie is weggevallen, en bij
de herziening van week 1 zijn ze ook zo aangemerkt. Dat was een terechte waarneming
en een verkeerde conclusie: ze zijn niet weggevallen maar vervallen.

**En ze staan nog in `source/` zelf**, dus het besluit is nog niet uitgevoerd. Bij
de vaststelling droegen `problems/opdrachten/rij_van_conway/index.md` en
`problems/opdrachten/tekst_genereren/index.md` nog de volledige tabel met
bestandsnaam en inleverkanaal, `problems/5_extra.md` een inleversectie, en
`projects/picobot.md` en `projects/textid.md` elk een inleversectie met
weeknummers. Die liften mee met de herziening van de week waar ze bij horen.

**Een opdracht die geen becijfering draagt, kan nog steeds verdieping zijn.** Waar
het materiaal onderscheid maakt tussen wat iedereen doet en wat extra is, gebeurt
dat op didactische grond en niet op puntentelling - het zegt iets over de opbouw,
niet over het cijfer. Zonder zo'n markering staan opdrachten van ongelijk gewicht
er ogenschijnlijk gelijkwaardig bij, en is de aflopende steun die het materiaal
biedt niet uitgelegd.

Vastgesteld bij de poort van #168.

### Onderdompeling gaat vooraf aan uitleg

**Een begrip mag in het materiaal voorkomen voordat het wordt uitgelegd.** De
student ziet het dan een paar keer in het wild, en pas later wordt expliciet
gemaakt wat het is. Dat is geen slordigheid maar een keuze: wie een vorm al een
paar keer heeft zien staan, heeft bij de uitleg iets om haar aan op te hangen.

Het geval waarop dit is vastgesteld: de **docstring**. Die staat in week 2 in de
gegeven code bij de basisopgave, zonder dat de vorm wordt uitgelegd, en wordt pas
bij de functies van week 3 benoemd. Vastgesteld door de vakdeskundige op
3 september 2026.

**Afleiding, niet vastgesteld** - waar de grens ligt is niet uitgesproken; wat
hierna staat is de lezing van de orkestrator, en zij hoort bij de eerstvolgende
poort te worden bevestigd of bijgesteld.

*Leg uit waar de student over struikelt, dompel onder waar hij alleen leest.* Een
docstring die hij ziet staan kost hem niets. Een `assert` die hij uitvoert stopt
zijn programma met een `AssertionError`, en dan heeft hij een verklaring nodig op
het moment dat het gebeurt - vandaar dat assertions in week 2 wél worden
geïntroduceerd en docstrings niet, terwijl ze allebei in dezelfde week voorkomen.
Kan de student er overheen lezen, dan mag het onderdompeling zijn; loopt hij erop
vast, dan hoort er uitleg bij.

Dit gaat over iets anders dan de "langzame onderdompeling" in
`conventies/codeconventies.md`: die gaat over de overgang van Nederlands naar
Engels in code, deze over een vorm tonen vóór de uitleg.

## Een besluit toevoegen

Neem het op in de tabel met zijn aard en status, en licht het eronder toe als de
grond niet in één regel past. Vermeld bij een gesloten besluit ook wat er zou
moeten veranderen om het te heropenen. Dat is het verschil tussen een archief en
een bruikbaar register.

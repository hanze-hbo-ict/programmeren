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
| PGM1 week 7 | De grens, voor mutatie én voor objectmethoden. Eerst *dat* je een lijst kunt wijzigen en wat dat oplevert, daarna pas dat twee namen naar dezelfde lijst kunnen wijzen, en daarna pas het kopiëren. |
| PGM2 | Een object is data plus de handelingen daarop, en dus een bundel toestand die verandert. Het woord ervoor bestaat dan al. |

Drie dingen volgen hieruit.

**Week 3 zegt het één keer hardop.** Bij de functies: hier rekent een functie iets
uit en geeft het terug, en verandert niets aan wat je meegeeft. De BSN-opgave
demonstreert dat al zonder er iets voor te hoeven doen; alle zes functies geven
een waarde terug en geen van alle verandert iets.

**Week 7 keert de volgorde om.** Nu komen mutatie en aliasing tegelijk. Het
vermogen hoort eerst, de valkuil daarna. Game of Life in `problems/7_extra`
draait volledig om bijwerken en is daarmee de natuurlijke aanleiding.

**Objectmethoden vallen op dezelfde grens.** `L.append(x)` is én een methode én
een mutatie; dat is geen toeval maar hetzelfde ding van twee kanten bekeken. Tot
en met week 6 leeft de student in een wereld zonder neveneffecten en zonder
objecten, en vanaf week 7 komen ze allebei tegelijk. Eén grens dus, geen twee.

Zonder die samenval is week 7 niet te maken: leeruitkomst P4 vraagt letterlijk om
"lijsten en strings en de bijbehorende methodes". Zie
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

| Besluit | Aard | Status |
|---|---|---|
| Recursie is naar PGM2 verplaatst; imperatief komt eerst | organisatorisch | gesloten |
| De theoretische afsluiting is geschrapt | ervaring | gesloten |
| Schakelingen zijn geschrapt, binair is afgeslankt | organisatorisch | gesloten |
| De wekelijkse leesopgaven zijn vervallen | praktisch | gesloten |
| Bestanden naar PGM1, excepties blijven in PGM2 | didactisch | staand, onderbouwd |
| Mutatie pas vanaf PGM1 week 7, en als grens benoemd | didactisch | staand, onderbouwd |
| Canonieke Python aanbieden, mechanisme later uitleggen | didactisch | staand, onderbouwd |
| Het bord verandert niet in week 5; de grens wordt daar benoemd | didactisch | gesloten |
| De parameternamen van `board.py` blijven zoals ze zijn | praktisch | gesloten |
| Objectmethoden pas vanaf week 7, samen met mutatie | didactisch | staand, onderbouwd |
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
| PGM2 | P3 bestanden, 10% | A4 recursie, 10% |

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

## Een besluit toevoegen

Neem het op in de tabel met zijn aard en status, en licht het eronder toe als de
grond niet in één regel past. Vermeld bij een gesloten besluit ook wat er zou
moeten veranderen om het te heropenen. Dat is het verschil tussen een archief en
een bruikbaar register.

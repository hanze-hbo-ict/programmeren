# Leerlijn

Wat er per week gebeurt, welke leeruitkomsten er landen, en welke begrippen er
voor het eerst worden geïntroduceerd.

Die laatste kolom is het dragende deel van dit document. Zolang vastligt waar een
begrip voor het eerst hoort, is een vooruitverwijzing te detecteren: materiaal
dat iets gebruikt wat volgens dit document later pas komt.

Voor PGM2 is de planning voor studiejaar 2026 leidend. Voor PGM1 liggen de
onderwerpen nog niet vast; wat hieronder staat is het huidige materiaal, gemeten
aan de inhoudsopgave en aan het eerste voorkomen van begrippen in de tekst.

Dit document is voor auteurs en docenten, niet voor studenten.

## Programmeren I

De onderwerpen liggen vast. De laatste kolom is de norm voor
vooruitverwijzingen: een begrip hoort niet eerder in het materiaal voor te komen
dan de week waarin het hier staat.

| Week | Onderwerp | Leeruitkomsten | Voor het eerst geïntroduceerd |
|---|---|---|---|
| 1 | Introductie, Picobot | - | state machine, staat, regels, string, algoritme |
| 2 | Variabelen en condities | P1, P2, P3 | toekenning, variabele, operatoren, `if`, lijst, assertion |
| 3 | Functies | P5, P6, P7, A2 | functiedefinitie, parameter, zelfaanroep |
| 4 | Lussen | A1 | `for`, `while`, begrensde en onbegrensde lus, `break`, `continue`, het lusrecept |
| 5 | Geneste lussen | A1, A3 | geneste lus, 2D-lijst, ASCII-art, bordrepresentatie |
| 6 | Bestanden en data | bestanden † | bits, bytes, ASCII, newline, `with open`, beeldbewerking |
| 7 | Mutabiliteit en algoritmeontwerp | P4, A3 | mutatie, functiecompositie, deelprobleem, algoritmeontwerp, tuple |

† De leeruitkomst over tekstbestanden staat nu in de PGM2-matrijs en wisselt van
plaats met recursie. Zie [leeruitkomsten.md](leeruitkomsten.md).

Vier dingen die aan deze indeling zijn veranderd, en waarom:

**Week 3 heeft een opgave met context gekregen**, de controle van een
burgerservicenummer met de elfproef. De week droeg P5 en A2 op het dunste
materiaal van de cursus, en er lag nergens iets om op terug te vallen. Zie
[uitgangspunten.md](uitgangspunten.md) voor waarom niet.

**De termen zijn *begrensde* en *onbegrensde* lus.** Het materiaal noemde
`while` tot 1 september 2026 "oneindige herhaling", overgeërfd uit CS5. Dat is
onjuist en het is precies de misvatting die het materiaal verderop bestrijdt. De
vaste termen komen uit `leeruitkomsten.md` r83, waar PGM2 P1 luidt: *"Student
past begrensde en onbegrensde lusconstructies toe."* Zij staan dus in de bindende
laag, en zij dragen het onderscheid dat het lusrecept nodig heeft: bij een `for`
staat de grens vast, bij een `while` levert de schrijver hem.

**Niet *herhaling*, maar *lus*.** Een lus is een vorm van herhaling en niet een
synoniem ervoor, en `conventies/begrippen.md` schrijft *lus* voor. Dit document
schreef tot 2 september 2026 "begrensde herhaling"; dat week af van zowel de
begrippenlijst als van `leeruitkomsten.md`, dat "lusconstructies" zegt.
Vastgesteld bij de poort van #146 en rechtgezet daarna.

**Het begrip *algoritme* valt in week 1, het *ontwerpen* ervan in week 7.**
`lectures/1a_intro_programmeren.md` geeft de naam aan wat de planstap van de 3 p's
oplevert, en zonder die naam heeft die draad geen woord voor zijn eigen product.
Week 7 gaat over algoritme**ontwerp** en het opdelen in deelproblemen, en dat is
iets anders dan het begrip. Vastgesteld bij de poort van #168.

**Een docstring komt in week 2 voor zonder uitleg.** De student ziet er een in het
skelet dat hij bij de basisopgave krijgt, en dat is genoeg; wat een docstring *is*
wordt pas expliciet gemaakt bij de functies van week 3. Daarom staat *docstring*
niet in de kolom hiernaast: die kolom gaat over waar een begrip wordt
geïntroduceerd, en dit is onderdompeling. Zie *Onderdompeling gaat vooraf aan
uitleg* in [uitgangspunten.md](uitgangspunten.md).

**Recursie wordt in PGM1 niet onderwezen.** Week 3 laat bij de functies alleen
zien dát een functie zichzelf kan aanroepen. De leesopdrachten daarover zijn naar
de PGM2-recursieweek verplaatst.

**Binair en talstelsels vervallen**, en week 6 wordt de week van bestanden. De
beeldbewerking blijft, maar dan als wat het al is: een bestand inlezen, bewerken
en wegschrijven.

**Week 7 is de grens waar mutatie binnenkomt.** De weken daarvoor rekenen en
geven terug, en veranderen niets aan wat ze meekrijgen. Dat was tot nu toe
feitelijk zo maar nergens gezegd. Objectmethoden vallen niet op deze grens:
week 7 laat mutatie zien via `L[i] = x`, wat geen methodeaanroep vraagt. Zie
[uitgangspunten.md](uitgangspunten.md).

**Dictionaries en de Markov-opgave verhuizen naar PGM2 week 1.** CS5
introduceert dictionaries in PGM1 als een verbijzondering van een lijst,
index-gebaseerd tegenover key-gebaseerd, en scheert er verder overheen. Dat is
te weinig voor wat PGM2 er in week 1 op bouwt, dus landen dictionaries daar in
plaats van in PGM1 week 7. Methodeaanroep wordt voor het eerst geïntroduceerd
in diezelfde week, samen met sets; de Markov-opgave gaat mee. Week 7 draagt
vanaf nu de mutatiegrens, functiecompositie en algoritmeontwerp.

**Tuples landen in week 7, niet in PGM2.** Daar zijn twee redenen voor, en ze
wijzen dezelfde kant op.

Een tuple is onveranderlijk, en dat is precies het contrast dat de mutatieles
nodig heeft: naast `L[i] = x` (mag) staat dat een tuple dat niet toelaat. De
introductie hoort daarom bij dezelfde les als mutatie.

En PGM2 week 1 heeft het er nodig. Dictionaries doorlopen gaat via `.items()`,
en dat levert paren op die je uitpakt met `for word, count in ...`. Zowel het
tuple als het uitpakken ervan is daar dus veronderstelde kennis. Vastgesteld met
de docent van PGM2 op 1 september 2026.

**Het materiaal van week 7 levert dit nog niet.** Gemeten op 1 september 2026:
het woord *tuple* komt in `source/` voor in vier bestanden, en geen daarvan is
een week 7-bestand; de enige plek vóór PGM2 week 1 is `problems/5_extra.md`, de
optionele laag van week 5, ongemarkeerd. Dat is werk voor #102 en geen gebrek in
PGM2 week 1: die week mag vooruitlopen op wat hier is afgesproken. Zie de rij in
*Wat een week aan een latere week aflevert*.

### Verdeling van het opgavemateriaal

Omvang in woorden per niveau, gemeten over `problems/` voor de weken 2 tot en met
7. Een ruwe maat, maar de verhoudingen zijn te groot om aan de meetmethode te
liggen. Hermeten bij de herziening van week 5; de weken 3, 6 en 7 waren sinds de
vorige meting ook veranderd.

| Week | opstap | basis | extra | Totaal |
|---|---|---|---|---|
| 2 | 1.145 | 1.089 | 463 | 2.697 |
| 3 | 242 | 1.143 | 176 | **1.561** |
| 4 | 616 | 1.034 | 1.048 | 2.698 |
| 5 | 674 | 2.940 | **5.354** | 8.968 |
| 6 | 353 | 1.343 | 772 | 2.468 |
| 7 | 532 | 1.110 | **3.713** | 5.355 |
| **Totaal** | **3.562** | **8.659** | **11.526** | 23.747 |

Drie dingen vallen op.

**Het zwaartepunt ligt in de optionele laag.** Extra is 49% van het materiaal en
een derde groter dan basis. Daar zitten Mandelbrot, Game of Life, Pi met
pijltjes en beeldcompressie: precies de opgaven waarin een probleem stap voor
stap wordt opgebouwd. Zie [uitgangspunten.md](uitgangspunten.md) voor de
achtergrond. De scheefheid is kleiner dan bij de vorige meting, doordat basis in
de weken 3 en 5 is gegroeid.

**Week 3 is de dunste week van de cursus.** Met 1.561 woorden is ze bijna zes
keer kleiner dan week 5, terwijl ze functies draagt: P5 en A2, samen 20% van het
tentamen.

**De structuur is compleet.** Twee beweringen die hier eerder stonden zijn
nagemeten en bleken onjuist. Week 7 heeft wél een opstap, met dertien
opdrachten, sinds commit `8190d95c`. En de nummering van de opstap van week 5
loopt door zonder gat; dat is ze in de hele geschiedenis van
`source/problems/5_opstap.ipynb` geweest. Sinds de herziening van week 5 telt die
opstap twaalf opgaven: acht om te lezen en vier om te schrijven.

## Programmeren II

**De planning voor 2026 is leidend.** Wat het materiaal nu doet is de
uitgangssituatie, niet de norm; het verschil tussen beide kolommen is het werk.

| Week | Leidend voor 2026 | Verantwoordelijk | Materiaal nu |
|---|---|---|---|
| 1 | Datastructuren (lists ter herhaling, dictionaries, sets, methodeaanroep, Markov) | BRRA | Datastructuren |
| 2 | Comprehensions (list, dict, set, range, enumerate) | HOEM | Recursie |
| 3 | Recursie | HOEM | Algoritmen (knapzak, wisselgeld) |
| 4 | Use it or lose it, lambda | HOEM | Objecten en dictionaries |
| 5 | OO, klassen, encapsulatie | BRRA | Kunstmatige intelligentie |
| 6 | Polymorfisme, overerving, duck typing | BRRA | Vier op een rij, AI-speler |
| 7 | Operator overloading, oefentoets | BRRA | - |

Een deel van deze onderwerpen komt in het huidige materiaal niet of nauwelijks
voor. Dat is bekend en verwacht: de planning beschrijft waar PGM2 heen gaat, niet
waar het staat.

## Volgorde van het werk

**Eerst wordt PGM1 herzien, met de PGM2-lijn als randvoorwaarde.**

Dat betekent dat PGM1 niet op zichzelf ontworpen wordt: wat PGM2 in week 1
veronderstelt, moet PGM1 hebben geleverd. Bij elke keuze in PGM1 is de vraag dus
niet alleen of ze op zichzelf klopt, maar ook of ze de bovenstaande lijn
ondersteunt.

De onderwerpen voor PGM1 liggen nog niet vast; de tabel hierboven voor PGM1
beschrijft het huidige materiaal. Ze vaststellen is het eerste inhoudelijke werk,
en de twee gaten hieronder horen daarin te worden meegenomen.

## Gaten tussen toetsing en materiaal

Gemeten op het voorkomen van de betreffende constructies in `source/`.

| Leeruitkomst | Weging | Bevinding | Besluit |
|---|---|---|---|
| **PGM2 P3** tekstbestanden | 10% | Drie plekken, waarvan twee in de Markov-opgave van PGM1 week 7. | Naar PGM1 week 6 |
| ~~**PGM1 A4** recursie~~ | | **Uitgevoerd op 1 september 2026**: staat nu als PGM2 A6. Wat resteert is de 10% die in PGM1 vrijkomt. | Zie `leeruitkomsten.md`, *Voorgestelde correcties* |
| **PGM2 P4** excepties | 10% | Bij de herziening van week 5 is `try`/`except` uit de gegeven code van `problems/5_basis` gehaald; de menukeuze wordt daar nu als string vergeleken. Excepties worden nergens in PGM1 onderwezen. | Blijft in PGM2, moet daar onderwezen worden |
| **PGM2 P1** lussen | 5% | Wordt in PGM1 onderwezen (week 4 en 5) en in PGM2 getoetst. Kan bedoeld zijn als herhaling, maar staat niet in de planning voor 2026. | open |
| **PGM2 A5** finite state machines | geen | Komt nergens voor. | Schrappen; zie [leeruitkomsten.md](leeruitkomsten.md) |

Van de twee gaten die samen 20% van het PGM2-tentamen zijn, is er daarmee één
belegd en één belegd maar nog niet gemaakt: PGM2 moet excepties daadwerkelijk
gaan behandelen.

## Vooruitverwijzingen om na te lopen

Begrippen die eerder in het materiaal opduiken dan waar ze volgens de leerlijn
thuishoren. Niet elk geval is fout; een vooruitwijzing kan bewust zijn, mits ze
als zodanig is gemarkeerd.

| Begrip | Hoort in | Duikt op in | Opmerking |
|---|---|---|---|
| `while` | PGM1 week 4 | PGM1 week 2, `practicals/2_rochambeau` | Bewust; de tekst zegt erbij dat lussen later komen |
| list comprehension | PGM2 week 1 | PGM1 week 6, `practicals/6b_images` | Onderwerp van een hele PGM2-week |
| functiedefinitie | PGM1 week 3 | PGM1 week 2, `problems/2_basis` | Mogelijk als gegeven voorbeeld |
| tuple | PGM1 week 7 | PGM1 week 5, laag extra, `problems/5_extra.md` | Ongemarkeerd; introduceert ook *methode* en *object*. Buiten bereik van de herzieningen in #102/#134 |

Twee regels stonden hier eerder en zijn nagemeten en geschrapt.

**2D-lijst in `problems/3_opstap`.** Nagemeten bij de herziening van week 5, met
een patroon op dubbele indexering en een patroon op een 2D-literal: beide geven
nul treffers op dat bestand. De enige treffer op het woord was het stringliteraal
`x = function("lol")`. Er staat daar geen 2D-lijst.

**`lectures/4b_midterm` opgave 19**, die de student vroeg de uitvoer te
voorspellen van een lus die `my_list[ix]` overschrijft. Die is herschreven met
het patroon `result = result + [...]`, hetzelfde patroon dat opgave 18 ernaast al
gebruikte. Het goede antwoord is niet veranderd.

Deze lijst is met tekstpatronen gemaakt en dus indicatief. Ze is het uitgangspunt
voor de controle die dit wil mechaniseren, niet het eindoordeel.

## Wat een week aan een latere week aflevert

Wat in de ene week wordt geleerd en in een latere week nodig is, staat hier. Zo
blijft een raakvlak vindbaar zonder dat het in een werkitem verstopt zit.

| Van week | Naar week | Wat | Status |
|---|---|---|---|
| PGM1 week 7 | PGM2 week 1 | Week 7 levert **tuples en tuple unpacking**. PGM2 week 1 doorloopt dictionaries met `.items()` en pakt de paren uit met `for word, count in ...`; `lectures/8a_datastructuren.ipynb` verwijst er expliciet naar terug. Het materiaal van week 7 bevat op dit moment geen enkele tuple. | Besloten met beide docenten op 1 september 2026. Uit te voeren bij de herziening van week 7 (#102). PGM2 week 1 loopt hier met opzet op vooruit; dat is geen defect in die week. |
| PGM1 week 4 | PGM2 week 1 | Week 4 levert de termen **begrensde** en **onbegrensde lus**, die `leeruitkomsten.md` r83 als PGM2 P1 toetst (5%, toepassen). Het materiaal gebruikte ze tot 1 september 2026 nergens. | Besloten bij de poort van #146, uit te voeren in datzelfde werkitem. |
| PGM1 week 4 | PGM1 week 5 | Week 4 levert het **lusrecept**: vijf vragen waarvan de **vierde** het stopmoment is (*"Wanneer is het klaar?"*); de vijfde gaat over wat je teruggeeft. Week 5 bouwt erop voort met geneste lussen, en `unique` sluit week 4 af op precies het probleem dat week 5 opent - een lus in een lus. | Besloten bij de poort van #146. |
| PGM1 week 5 | PGM2 week 6 | De vier zoekfuncties uit `practicals/5b_boter_kaas_eieren.ipynb` hebben andere parameternamen dan de gelijknamige functies in `source/problems/assets/board.py` regels 173-224. | Besloten, laten zoals het is: `board.py` definieert ze zelf en importeert het werk van de student nooit. Zie het besluitenregister in [uitgangspunten.md](uitgangspunten.md). |
| PGM1 week 5 | PGM1 week 7 | Week 5 levert `create_board` en `print_board` als vermogen; `source/problems/7_extra.md` regels 36-114 leert ze nu vanaf nul aan. | Voorstel: laat week 7 ernaar verwijzen in plaats van ze opnieuw aan te leren. |
| PGM1 week 5 | PGM1 week 7 | `[[0] * 3] * 3` en de waarschuwing daarbij horen in week 7, naast aliasing en `deepcopy`. De constructie bijt pas zodra je erin toewijst, en dat gebeurt in week 5 niet. | Besloten in het weekontwerp van week 5, uit te voeren bij de herziening van week 7. |
| PGM1 week 5 | PGM1 week 7 | Week 5 sluit af op één probleem: één vakje van een raster veranderen terwijl de rest blijft staan. Beide afsluitingen verwijzen naar `source/problems/7_extra.md`, de optionele extra-laag. | Voorstel: laat `source/lectures/7a_lists_advanced.ipynb` datzelfde probleem opnemen, zodat ook de student die extra overslaat het vervolg krijgt. |

## Onderhoud

Verandert er iets aan de weekindeling of aan waar een begrip wordt
geïntroduceerd, werk dan dit document bij in dezelfde wijziging. Dit is de bron
waartegen coherentie over weken heen wordt getoetst; loopt hij achter, dan
controleert de toets niets meer.

# Docentenhandleiding PGM1 week 2

Deze week schrijft de student zijn eerste regels Python. Hij leert een waarde in
een variabele bewaren, ermee rekenen en vergelijken, en een programma een keuze
laten maken met `if`. Daarna komen strings en lijsten: twee rijtjes waaruit je
stukken kunt opvragen.

Het is ook de eerste week op de eigen machine. Week 1 was papier en een
browsersimulator; vanaf nu heeft iedereen Python en een editor nodig. Reken erop
dat dat bij een deel van de zaal niet af is - zie *Wat je nodig hebt*.

De week draagt twee onderwerpen en niet één. Dat is de reden dat er twee colleges
en twee practica staan, en het verklaart de indeling hieronder.

## 1. De week in het kort

| Bijeenkomst | Vorm | Materiaal |
|---|---|---|
| 1 | College | `source/lectures/2a_var_con.ipynb` |
| 2 | Werkcollege | `source/lectures/2b_strings_en_lists.ipynb` + `source/practicals/2_rochambeau.ipynb` |
| 3 | Practicum | `source/practicals/2_sequenties_en_data.ipynb` + `source/problems/2_opstap.ipynb`, `2_basis.ipynb`, `2_extra.ipynb` |

Daarnaast staan er vier overzichtspagina's die je zelf niet hoeft te behandelen:
`source/course/week_2.md` (`## Variabelen en condities`) vat de week samen voor de
student, en `source/course/practical_2.md`, `source/course/opgaven_2.md` en
`source/course/solutions_2.md` zijn de omslagpagina's boven de practica, de
opgaven en de uitwerkingen. De vijf bestanden in `source/solutions/` staan in die
laatste; ze zijn openbaar voor de student en daarom geen materiaal dat je zelf
brengt.

### Deze week valt één practicum naar de derde bijeenkomst

De indeling college - werkcollege - practicum uit
`curriculum/uitgangspunten.md` §`### Drie bijeenkomsten per week` gaat ervan uit
dat een week één practicum heeft. Week 2 heeft er twee, en daarom is daar een
erkende afwijking vastgelegd: `source/practicals/2_rochambeau.ipynb` vult het
werkcollege en `source/practicals/2_sequenties_en_data.ipynb` schuift naar de
derde bijeenkomst, naast de drie opgavebundels.

De grond staat in het materiaal zelf. Rochambeau is één programma dat je met een
klas stap voor stap opbouwt - precies wat een werkcollege is. Sequenties en data
is een lange begeleide reeks cellen met `assert`-regels eronder: zelfstandig werk
onder begeleiding, en dus een practicum.

### Over de tijden

De blokken van bijeenkomst 1 en 2 komen uit de handleidingen van 2023
(`teacher_guides/2a_var_con.docx` en `teacher_guides/2b_strings_en_lists.docx`).
De blokken van bijeenkomst 3 zijn richttijden zonder bron - daarvoor bestaat geen
oude handleiding. Voor het Rochambeau-deel van bijeenkomst 2 geldt hetzelfde; dat
staat bij het blokschema erbij.

Beide bronnen tellen op tot **90 minuten**, met een ongetimede pauze. Bij `2a` is
dat een gecorrigeerd getal: **blok 6 van die bron heeft geen minutenaantal** - er
staat letterlijk "Terug naar maximum probleem (min)". De negen blokken die er wél
een hebben tellen samen op tot 85. Ik heb dat blok op 5 minuten gezet, waarmee de
bijeenkomst op 90 uitkomt en gelijk loopt met `2b`. Dat is een schatting en geen
overgeleverd getal.

**Hoe lang een bijeenkomst werkelijk duurt staat nergens in de repository.** Duurt
die van jou korter of langer, schaal de blokken dan mee.

### Wat je nodig hebt

- **Een werkende Python en een editor, bij iedereen.** Dit is de eerste week
  waarin de student op zijn eigen machine werkt.
  `source/practicals/2_rochambeau.ipynb` opent met een checklist
  (§`## Opgelet: is je omgeving opgezet?`); die is er niet voor niets. Verwijs
  wie vastloopt naar `source/lectures/0b_install_python.md` en naar
  `source/lectures/0a_command-line.md`.
- **Een scherm waarop je code kunt uitvoeren terwijl de klas kijkt.** Vrijwel elk
  blok van deze week is "wat denk je dat hier uitkomt?", en het antwoord haal je
  bij Python, niet bij jezelf.
- **Papier.** De collegeopdrachten van beide colleges zijn leesvragen. Ze werken
  beter als de student het antwoord eerst opschrijft en pas daarna uitvoert.

**De notebooks van deze week draai je niet in de browser.** Dat is de bedoeling,
maar het kan nu nog niet; `source/practicals/2_sequenties_en_data.ipynb`
§`## Waar je werkt` zegt dat ook tegen de student. Werk in VS Code, of neem een
cel over in een bestand.

## 2. Bijeenkomst 1 - College: variabelen en condities

Materiaal: `source/lectures/2a_var_con.ipynb`.

De dragende lijn is **één probleem dat de hele bijeenkomst in stappen
terugkeert**: gegeven twee getallen, welke is de grootste? Je opent ermee, je
komt er halverwege op terug zodra input en variabelen er zijn, en je maakt het af
zodra `if`-`else` er is. Alles wat ertussen zit is er om die volgende stap
mogelijk te maken. Houd die lijn vast; hij is het enige wat de losse onderwerpen
van dit college aan elkaar knoopt.

### Blokschema bijeenkomst 1

| # | Min | Blok | Waar in `2a_var_con.ipynb` |
|---|---|---|---|
| 1 | 5 | Lesdoel en het maximumprobleem: probeer en plan, en waarom de derde stap Python nodig heeft | `# Maximum` |
| 2 | 5 | Input en output | `## Input en output` |
| 3 | 15 | Variabelen, datatypes en operatoren | `## Variabelen`, `## Datatypes`, `## Operatoren` |
| 4 | 10 | Opdracht 1 en 2, in duo's | `## Opdrachten`, `### Opdracht 1`, `### Opdracht 2` |
| 5 | 5 | Terug naar het maximumprobleem: stap 1 is af | `### Opdracht 3` |
| | | **Pauze** | |
| 6 | 10 | Het if-statement, en de syntax die erbij hoort | `## If then else`, `### Het if-statement`, `### Syntax`, `### Opdracht 4` |
| 7 | 10 | If-else | `### Het if-else statement`, `### Opdracht 5` |
| 8 | 15 | De if-elif-else-boom | `### De if-then-else boom`, `### Opdracht 6` |
| 9 | 10 | Twee voorwaarden tegelijk: `and` en `or` | `### Twee voorwaarden tegelijk`, `### Opdracht 7` |
| 10 | 5 | Het maximumprobleem afmaken, en vooruitblik | `## Maximum probleem` |

Tien blokken, 90 minuten. De bron had er ook tien, maar niet dezelfde.

**Wat er ten opzichte van 2023 is veranderd.** De twee openingsblokken van toen
(*Start les* en *Introductie Maximum probleem*, samen 10 minuten) zijn hier één
blok van 5 geworden; het materiaal zet het lesdoel en het probleem in dezelfde
alinea's. Die vijf minuten gaan naar blok 9, dat **nieuw** is:
§`### Twee voorwaarden tegelijk` bestond in 2023 niet in dit college. `and` en
`or` stonden toen in het eerste college van week 1 en zijn naar hier verhuisd -
de handleiding van week 1 noemt dat blok als vervallen. En het huiswerk waarmee
de bron afsloot, *Opdracht 8*, bestaat niet meer; zie blok 10.

**Blok 9 staat later dan het materiaal.** In het notebook staat
§`### Twee voorwaarden tegelijk` onder §`## Operatoren`, dus vóór
§`## If then else` - terwijl het voorbeeld dat er staat een `if`-statement is.
Behandelen in leesvolgorde betekent dus vooruitwijzen naar iets wat de klas nog
niet heeft gehad. Noem `and` en `or` in blok 3 alleen als de laatste regel van de
operatorentabel, en doe de uitleg pas in blok 9, waar Opdracht 7 ze nodig heeft.
Zeg hardop dat je een stukje van de pagina overslaat en er later op terugkomt.

### Hoe je het brengt

**Blok 1.** Stel het probleem als vraag aan de zaal en laat ze het plan zelf
formuleren: neem twee getallen, en als de een groter is dan de ander, dan is die
de grootste. Dat plan staat in twee regels op het bord en blijft daar de hele
bijeenkomst staan. Zeg erbij dat de eerste twee stappen af zijn en dat de rest
van het college over de derde gaat.

**Blok 2.** `input()` en `print()`, meer niet. Voer ze een keer uit zodat de klas
ziet dat het programma stilstaat en op je wacht.

**Blok 3.** Dit is het langste blok en het bevat het meeste nieuwe. De volgorde
van het materiaal is goed: eerst de variabele als doos met een naam, dan de
datatypes, dan de operatorentabel. Doe de doos op het bord, met de naam erop en
de waarde erin, en schrijf `getal_A = 5` ernaast.

Het punt waar dit blok om draait is dat `input()` **altijd een string
teruggeeft**. Voer `getal_A = input("Geef getal a")` uit, typ `5`, en druk dan
`getal_A * 2` af. Er staat `55` en niet `10`. Pas daarna komt `int()` binnen als
de oplossing, en dan snapt de klas waarom hij er is.

**Blok 4.** Nu beginnen de opdrachten, en dit is het moment om de werkwijze mee
te geven waarmee ze in week 1 hebben leren werken: **probeer, plan,
programmeer** - de drie p's uit `source/lectures/1a_intro_programmeren.md`
§`## 3 p's`, waar ze ook vlak vóór de opdrachten staan. Leg ze hier niet
opnieuw uit als theorie: zeg dat het de werkwijze is voor wat nu komt, en dat
deze week de derde p er voor het eerst bij hoort. Staan ze bij jou nog boven aan de collegepagina, lees ze daar dan
niet voor maar pak ze hier op.

Laat de studenten Opdracht 1 en 2 eerst **op papier** maken en bespreek daarna
pas. Zo zie je wat ze dachten, en niet wat Python zei. Geef bij het bespreken de
beurt willekeurig; anders geeft de sterkste student alle antwoorden en zakt de
rest onderuit.

**Blok 5.** Terug naar het bord. Stap 1 van het plan is af: met `input()` en
`int()` heb je twee getallen in variabelen. Opdracht 3 is de brug naar de tweede
helft - de code die er nu staat drukt alleen `True` of `False` af, en dat is nog
geen antwoord op de vraag welk getal het grootste is. Laat de klas zelf zeggen
wat er ontbreekt.

**Blok 6.** Het `if`-statement in drie delen: de conditie, de dubbele punt, en
het inspringen. Schrijf één statement volledig uit op het bord en wijs de drie
delen aan. Opdracht 4 hoort er direct achteraan: **d** geeft een
`IndentationError`, en die wil je live laten zien.

**Blok 7.** `if`-`else`. Kort blok; het materiaal is hier makkelijk. Opdracht 5
**c** is de interessante: de laatste `print` staat buiten de keuze en gaat dus
altijd aan.

**Blok 8.** De `if`-`elif`-`else`-boom, met het cijfervoorbeeld uit het
materiaal. Het punt is dat Python **stopt bij de eerste conditie die waar is**.
Reken het cijfervoorbeeld voor met een 8: die is ook hoger dan 5,5, en toch komt
er `Goed` uit en niet ook `Voldoende`. Opdracht 6 test precies dat, en **d** laat
zien dat een geneste `if`-`else` hetzelfde doet als een `elif` - dezelfde
uitkomst, andere vorm.

**Blok 9.** `and` en `or`. Twee zinnen volstaan: `and` is waar als beide kanten
waar zijn, `or` zodra er één waar is. Waar je tijd in stopt is de vorm: aan
allebei de kanten van `and` moet een hele vergelijking staan. Het materiaal zet
`if getal > 5 and < 10` er als fout naast; laat die fout één keer uitvoeren zodat
de foutmelding erbij hoort. Opdracht 7 is hierna de zwaarste van het college.

**Blok 10.** Maak het maximumprobleem af: het plan van blok 1 staat er nog, en nu
past de code eronder. Sluit af met "wat hebben we geleerd?" en laat de klas het
antwoord geven. Wijs vooruit naar het werkcollege: daar bouw je samen een
programma dat steen, papier en schaar speelt.

Dat vooruitzicht was in 2023 het huiswerk - *Opdracht 8*, een programma voor
steen, papier en schaar dat in het volgende werkcollege werd nagekeken. Die
opdracht bestaat niet meer; hetzelfde programma is nu
`source/practicals/2_rochambeau.ipynb` en je bouwt het samen op in plaats van het
na te kijken. Geef het dus als vooruitblik mee en niet als huiswerk.

### Waar het vastloopt

- **`input()` geeft een string, ook als je een getal typt.** Dit is de fout van de
  week. `"5" * 2` is `55` en niet `10`; `"5" + "2"` is `52` en niet `7`.
  Opdracht 1 **b** en **d** gaan hier precies over. Wie `int()` vergeet, krijgt
  geen foutmelding maar een verkeerd antwoord - en dat is erger.
- **De aanhalingstekens om een string.** Hamer erop dat een string
  aanhalingstekens heeft, en dat een woord zonder aanhalingstekens voor Python een
  variabelenaam is. Welke soort het zijn maakt niet uit: het materiaal staat
  dubbele en enkele toe, zolang je binnen één stuk code consequent bent. Wat niet
  mag is ze mengen, zoals `"hoi'`.
- **Inspringen.** Dit is de tweede grote van de week, en hij komt in drie
  vermommingen: te weinig inspringen, waardoor een regel buiten de `if` valt die
  erbinnen hoort; te véél inspringen, waardoor een regel binnen een tak valt waar
  hij niet hoort; en wisselend inspringen binnen hetzelfde blok, wat een
  `IndentationError` geeft. Alleen de derde loopt luid af. De eerste twee geven
  gewoon een verkeerd antwoord. Zeg dat er hardop bij.
- **`=` tegen `==`.** Eén gelijkteken kent toe, twee vergelijken. In een conditie
  hoort er altijd twee te staan.
- **`elif` wordt gelezen als "nog een `if`".** Bij een keten stopt Python zodra
  er één waar is; bij losse `if`-statements wordt elke test apart uitgevoerd.
  Opdracht 7 **c** heeft twee losse `if`-statements en die gaan dan ook allebei
  aan - dat is het verschil met **a** en **b** eronder.
- **Delen geeft altijd een floating-point getal.** `12 / 2` is `6.0` en niet `6`.
  Bij Opdracht 7 schrijft bijna iedereen `6` en `21` op waar `6.0` en `21.0` uit
  Python komt. Reken het niet in je hoofd voor: voer het uit.
- **`and` met een halve vergelijking rechts.** `x > 5 and < 10` ziet er logisch
  uit en is een `SyntaxError`. Het moet twee keer een hele vergelijking zijn.

### Als het niet uitkomt

- **Blok 3 loopt uit.** Dat mag; het is het blok dat je níét moet inkorten.
  Haal de tijd bij blok 8 vandaan: Opdracht 6 heeft vier deelvragen en je kunt er
  twee klassikaal doen en twee meegeven.
- **Je komt niet aan blok 9 toe.** Sla `### Twee voorwaarden tegelijk` en
  Opdracht 7 over en doe ze aan het begin van het werkcollege. Ze zijn daar
  meteen nodig: wie steen, papier en schaar in `if`-statements uitschrijft, komt
  vanzelf bij `and`. Wat je niet doet is blok 10 laten vallen - dan eindigt het
  college zonder dat het probleem waarmee het begon is opgelost.
- **Je houdt tijd over.** Laat duo's die klaar zijn Opdracht 6 **d** omschrijven
  naar een `elif`-keten, of andersom. Dat is dezelfde stof van de andere kant en
  kost je geen voorbereiding.
- **Een deel van de zaal heeft geen werkende Python.** Laat ze meekijken met een
  buurman en verwijs ze naar `source/lectures/0b_install_python.md`. Dit college
  is nog te volgen zonder eigen machine; het werkcollege van morgen niet.

## 3. Bijeenkomst 2 - Werkcollege: strings, lijsten en Rochambeau

Materiaal: `source/lectures/2b_strings_en_lists.ipynb` en
`source/practicals/2_rochambeau.ipynb`.

De bijeenkomst heeft twee helften met een verschillend karakter. De eerste is
uitleg met leesvragen, net als het college van gisteren. De tweede is het
werkcollege in eigenlijke zin: je bouwt samen met de klas één programma op.

### Blokschema bijeenkomst 2

| # | Min | Blok | Waar |
|---|---|---|---|
| 1 | 5 | Lesdoel: strings en lijsten, en wat je aan het eind samen bouwt | `2b`: `# Strings` |
| 2 | 10 | Strings optellen en vermenigvuldigen | `2b`: ``## `str`ings: tekstuele data``, `### Opdracht 1` |
| 3 | 10 | Lijsten: lengte, index, positie, en een lijst in een lijst | `2b`: `## Lists`, `### Lengte`, `### Index`, `### Positie`, `### Alle data` |
| 4 | 10 | Strings zijn ook geïndexeerd, en negatieve indices | `2b`: `## Strings en indexering`, `### Positie`, `### Negatieve indices` |
| | | **Pauze** | |
| 5 | 20 | Slicen, stappen en achteruit lopen | `2b`: `### Slicing`, `### Stappen`, `### Achteruit lopen`, `### Opdracht 2`, `### Opdracht 3`, `### Opdracht 4` |
| 6 | 10 | Vergelijken: wat is groter, en waarom | `2b`: `` ## `max` of `min` ``, `` ### `str`ings to the `max` ``, `### Opdracht 5` |
| 7 | 5 | Het spel, de regels, en de begincode lezen | `2_rochambeau`: `# Rochambeau`, `## De regels`, `## Een begin` |
| 8 | 15 | Samen opbouwen: drie wapens, drie uitkomsten | `2_rochambeau`: `## En verder!`, `### Opgave` |
| 9 | 5 | Afronden, en waar ze verder werken | `2_rochambeau`: `## Uitbreidingen`, `## Blijven spelen` |

Negen blokken, 90 minuten. **Blok 7 tot en met 9 hebben geen bron**: voor
Rochambeau bestaat geen oude handleiding, dus die 25 minuten zijn richttijden.

De bron van `2b` had acht blokken van samen 90 minuten. Waar de 25 minuten voor
het Rochambeau-deel vandaan komen: het blok *Bespreken huiswerk - Opdracht 8*
(10 min) **vervalt**, want die opdracht bestaat niet meer en het programma
waarover het ging is nu dit practicum; *Slicing* gaat van 25 naar 20 minuten en
*Min of max* van 15 naar 10, omdat de bijbehorende opdrachten in het huidige
materiaal korter zijn dan de bron veronderstelde; en het afsluitblok van 5
minuten is blok 9 geworden.

**Twee koppen in `2b` bestaan twee keer.** `### Positie` en `### Slicing` staan
allebei één keer onder `## Lists` en één keer onder `## Strings en indexering`.
Dat is opzet - het is dezelfde bewerking op een ander type - maar zeg er in de
klas altijd bij welke van de twee je bedoelt.

### Hoe je het brengt

**Blok 1.** Eén zin over wat er komt, en één over waar het naartoe gaat: aan het
eind van deze bijeenkomst staat er een programma dat steen, papier en schaar met
je speelt. Dat maakt de eerste helft minder los.

**Blok 2.** Strings optellen en vermenigvuldigen is de vreemdste bewerking van de
week: `2 * "ha"` is `haha`. Voer de twee voorbeeldcellen uit het materiaal uit en
laat de klas de tweede eerst voorspellen. Opdracht 1 kan hier direct achteraan.

**Blok 3.** Een lijst is een rijtje met een vaste volgorde, en tellen begint bij
0. De tabel in het materiaal met de indices eronder is het beeld dat blijft
hangen; teken hem over op het bord. Het element `[4, 2]` binnen een lijst is de
verrassing: `len()` telt de buitenste lijst en kijkt niet naar binnen.

**Blok 4.** Nu hetzelfde voor strings, en dat is het punt van dit blok: het is
**exact dezelfde syntaxis**. Als de klas dat ziet, is de helft van dit college
klaar. Negatieve indices erachteraan, met de tabel waarin beide nummeringen onder
elkaar staan.

**Blok 5.** Het zwaarste blok. Neem de twintig minuten en volg de volgorde van
het materiaal: eerst `[start:stop]`, dan de weggelaten grenzen, dan de stap, dan
de negatieve stap. Zeg één zin drie keer: **de stopindex hoort er niet meer bij**.
Opdracht 2, 3 en 4 horen bij dit blok; doe Opdracht 2 klassikaal en laat 3 en 4
in duo's maken.

**Blok 6.** Vergelijken. Begin met `"w" > "e"` en laat de klas denken dat het over
alfabetvolgorde gaat. Doe daarna `"Mug" > "Muis"`: gelijk, gelijk, en dan beslist
de derde letter. Opdracht 5 test alle gevallen die je nodig hebt.

**Blok 7.** Schakel om. Laat de begincode van Rochambeau zien en lees hem regel
voor regel voor. Vraag wat dit programma doet als je `papier` intypt - het
antwoord is: niets bijzonders, want er is maar één `if`. En vraag wat het doet
als je `steen` intypt: dan beweert het te hebben gewonnen, ongeacht wat het zelf
koos. Dat is een grap in het materiaal, en het is meteen de opgave: maak er een
eerlijk spel van.

**Blok 8.** Dit is het werkcollege. Bouw het samen op, aan het bord of in een
bestand op het scherm, en laat de klas de volgende regel zeggen. Werk één wapen
volledig uit - drie uitkomsten: winnen, verliezen, gelijk - en laat de andere
twee wapens open. Dat is precies genoeg om de vorm te laten zien en niet zoveel
dat je het hele programma weggeeft. Zeg erbij dat er meer dan één goede vorm is:
een `if` per wapen met daarbinnen een keuze, of één lange keten met `and`.

**Blok 9.** Laat kort zien waar het nog naartoe kan (`## Uitbreidingen`) en dat
je een spel kunt laten doorlopen (`## Blijven spelen`) - allebei als vooruitblik,
niet als stof. Zeg waar ze verder werken: het programma afmaken doen ze zelf, de
uitwerking staat in `source/solutions/2_rochambeau.ipynb`.

### Waar het vastloopt

- **De stopindex hoort er niet bij.** `pi[2:4]` geeft twee elementen en niet
  drie. Dit is de fout die het vaakst wordt gemaakt en de enige die zich in elke
  latere week blijft wreken.
- **`pi[1]` en `pi[1:2]` zien er hetzelfde uit en zijn het niet.** Het eerste is
  een getal, het tweede een lijst met dat getal erin. Opdracht 4 zet de twee
  naast elkaar: `15` tegenover `[1, 4, 1, 4, 1, 4]`. Dat verschil is het hele
  punt van die opdracht.
- **Bij een negatieve stap moeten start en stop omgekeerd.** `s[0:5:-1]` geeft
  een leeg resultaat en geen foutmelding. Het materiaal zet er een kader bij;
  wijs erop voordat ze beginnen.
- **Vergelijken is geen alfabetvolgorde.** Hoofdletters komen vóór kleine
  letters, dus `"Hogeschool" < "hanze"` is waar. Dat is ook de reden dat het
  antwoord bij Opdracht 1 **b** een hoofdletter H in het midden heeft.
- **De kortste is de kleinste.** `"F" < "Fiets"` is waar, want `"F"` is het begin
  van `"Fiets"`. Studenten verwachten hier "gelijk". Deze komt in bijeenkomst 3
  terug bij de opstap, en daar kost hij een verkeerd busnummer.
- **Bij lijsten beslist het eerste element.** `[4, "m&m's"] < [1, "koffie"]` is
  onwaar, en naar de strings wordt niet meer gekeken.
- **Rochambeau: geneste `if`-statements die elkaar overlappen.** Wie per wapen
  een tak schrijft, schrijft er twee soorten fouten in. De eerste is een tak die
  nooit aan kan gaan, omdat een tak erboven hetzelfde geval al afvangt. De tweede
  is een geval dat helemaal ontbreekt - meestal het derde wapen, of het
  gelijkspel. Allebei lopen ze stil af: het programma werkt, en zegt af en toe
  iets verkeerds. Laat ze alle negen combinaties aflopen als het misgaat.
- **De omgeving is niet af.** Een deel van de zaal krijgt vandaag pas door dat
  Python nog niet werkt. Zie *Als het niet uitkomt*.

### Als het niet uitkomt

- **De eerste helft loopt uit.** Kort blok 6 in tot `"Mug" > "Muis"` en geef
  Opdracht 5 mee; hij komt in bijeenkomst 3 in de opstap terug, onder
  `## Strings en lijsten`. Wat je níét inkort is blok 5, want daar zit alles op
  vast.
- **Je komt niet aan Rochambeau toe.** Schuif blok 7 tot en met 9 door naar het
  begin van bijeenkomst 3. Dat kost daar 25 minuten van het zelfstandige werk en
  is de goedkoopste ingreep van de week - het practicum van bijeenkomst 3 heeft
  drie bundels waarvan er geen enkele af hoeft.
- **Je houdt tijd over.** Laat duo's het tweede wapen van Rochambeau zelf
  uitwerken, of laat ze het programma zo maken dat de speler altijd wint. Dat
  laatste mag van de opgave en het is didactisch dezelfde oefening.
- **Iemand heeft nog steeds geen Python.** Laat hem in een duo werken en zet het
  installeren op zijn huiswerklijst voor vandaag. Bijeenkomst 3 is niet te volgen
  zonder.

## 4. Bijeenkomst 3 - Practicum: sequenties, data en de opgaven

Materiaal: `source/practicals/2_sequenties_en_data.ipynb`, en de drie
opgavebundels `source/problems/2_opstap.ipynb`, `source/problems/2_basis.ipynb`
en `source/problems/2_extra.ipynb`.

Dit is zelfstandig werk onder begeleiding. Je legt weinig uit en loopt veel rond.

**Verwijs naar de bundels op naam en niveau, niet op opgavenummer.** De drie
bundels hebben elk een eigen doel - de opstap is er voor wie de stof nog niet
vertrouwt, de basis is de zelftest, de extra is een uitdaging - en dat staat ook
zo op `source/course/opgaven_2.md`. De nummering binnen de bundels is niet
uniform; zie sectie 5.

### Blokschema bijeenkomst 3

Deze bijeenkomst heeft **geen handleiding uit 2023**. De tijden hieronder zijn
richttijden, geschat op de omvang van het materiaal, en geen overgeleverde
lesindeling. Het totaal van 90 minuten is overgenomen van de twee bijeenkomsten
hiervoor.

| # | Min | Blok | Waar |
|---|---|---|---|
| 1 | 10 | Aftrap: waar je werkt, en wat de drie bundels van elkaar onderscheidt | `2_sequenties_en_data`: `## Waar je werkt` · `source/course/opgaven_2.md` |
| 2 | 20 | De cellen doorlopen, en daarna zelf foutmeldingen uitlokken | `2_sequenties_en_data`: `## Bewerkingen met Python`, `## Fouten` |
| 3 | 20 | De opgaven met lijsten, en `assert` als nakijkregel | `2_sequenties_en_data`: `## Opgaven`, `### Lijsten maken en bewerken`, `` ### Jezelf nakijken met `assert` `` |
| | | **Pauze** | |
| 4 | 15 | Dezelfde opgaven, nu met strings | `2_sequenties_en_data`: `### Strings slicen en indexeren` |
| 5 | 20 | Zelfstandig aan de bundels, ieder op zijn eigen niveau | `source/problems/2_opstap.ipynb`, `2_basis.ipynb`, `2_extra.ipynb` |
| 6 | 5 | Afronden: wat af moet, en wat huiswerk is | - |

Zes blokken, 90 minuten als richttijd.

### Hoe je het brengt

**Blok 1.** Twee dingen, kort. Ten eerste waar ze werken: VS Code, en de
notebookcellen neem je over in een bestand. Ten tweede de drie bundels, en dan
vooral dat ze **niet alle drie voor iedereen zijn**. De basis is de zelftest; wie
daar vastloopt gaat naar de opstap; wie er doorheen vliegt gaat naar de extra.
Zeg dat expliciet, anders begint iedereen bij de opstap en komt niemand aan de
basis toe.

Weet daarbij dat de tweede reeks van de opstap grotendeels het tweede college
overdoet; zie sectie 5. Voor wie die stof nog niet vertrouwt is dat precies goed,
maar wie hem wél vertrouwt stuur je erheen voor niets.

**Blok 2.** Laat ze de cellen van `## Bewerkingen met Python` één voor één
uitvoeren. Het is bewust saai en het gaat snel. Waar je bij stilstaat is het paar
`my_list == 42` en `my_list != 42`: één of twee gelijktekens maakt uit, en dat is
dezelfde fout als gisteren in een conditie.

`## Fouten` is het beste stuk van dit practicum en het krijgt vaak te weinig
tijd. De opdracht is niet om fouten te vermijden maar om ze **met opzet te
maken** - zes soorten, elk apart. Ga rond en vraag bij elke foutmelding wat er
staat en op welke regel. Wie hier leert een foutmelding te lezen, heeft de rest
van de cursus minder aan jou nodig.

**Blok 3.** De opgaven met lijsten. De eerste is voorgedaan; laat die als vorm
zien. Behandel `assert` klassikaal en in twee zinnen: het is een bewering, klopt
hij dan gebeurt er niets, klopt hij niet dan stopt Python met een foutmelding.
Zolang er nog niets is ingevuld faalt hij dus - dat is de bedoeling en niet een
kapotte cel. Zeg erbij dat ze `assert` de hele cursus terugzien en er vanaf week
3 zelf schrijven.

**Blok 4.** Hetzelfde met strings. Het aantal bewerkingen dat erbij staat is een
record en geen eis; het materiaal zegt dat zelf. Gebruik het als uitdaging voor
wie snel klaar is.

**Blok 5.** Rondlopen. Wie bij de basis vastloopt stuur je naar de opstap en niet
naar het antwoord. Wie klaar is met de basis mag naar de extra, en die is
bedoeld om níét af te komen.

**Blok 6.** Vijf minuten. Wat moet er af: de basis. Wat is aanbod: de opstap.
Wat is een uitdaging: de extra. Wijs erop dat de uitwerkingen openbaar zijn en
dat zelf proberen vóór kijken het hele punt is.

### Waar het vastloopt

- **De `assert` faalt en de student denkt dat de cel stuk is.** Hij is stuk
  zolang het antwoord er niet staat; dat is het idee. Wijs op
  `` ### Jezelf nakijken met `assert` `` en laat de tekst achter de `assert` lezen,
  want daar staat wat er had moeten uitkomen.
- **`answer1 = ...` blijft staan.** De drie puntjes zijn geldige Python, dus
  `print(answer1)` drukt gewoon `Ellipsis` af. Dat ziet eruit als een
  foutmelding en is het niet.
- **`+` gebruiken om getallen op te tellen.** Bij de lijstopgaven mag `+` alleen
  om lijsten aan elkaar te plakken; dat staat in de opgave en wordt overgelezen.
- **De kortste is de kleinste, en dat kost een busnummer.** In
  `## Conditionele statements` van de opstap staat een naam die met de
  grensletter zelf begint; die valt niet in de groep waarin de student hem
  verwacht. Precies dezelfde valkuil zit in `## Debuggen`: één van de zeven
  uitwerkingen gaat er stil op onderuit, en een andere ontloopt hem juist doordat
  de grens er anders is geschreven.
- **De debugopgave met één naam testen.** Drie van de zeven uitwerkingen lopen
  luid af: Python weigert ze te lezen. De andere vier werken en drukken een
  verkeerd busnummer af, en twee daarvan geven bij de naam die in het materiaal
  staat toevallig het juiste antwoord. `source/solutions/2_opstap.ipynb` geeft een lijstje namen waarmee je ze
  wél betrapt; wijs daarop zodra iemand zegt dat een uitwerking klopt.
- **De interactieve fictie in de basis loopt uit de hand.** Het materiaal
  waarschuwt er zelf voor. De eis is vijf soorten controlestructuren, niet een
  goed verhaal. Zeg dat er hardop bij, anders is een deel van de zaal een uur
  later nog aan het schrijven.
- **De extra: vier vieren is verslavend.** Dat is de bedoeling en het is geen
  reden om er de hele middag aan te besteden. Er staat expliciet dat je er een
  paar mag overslaan.

### Als het niet uitkomt

- **Blok 7 tot en met 9 van gisteren zijn blijven liggen.** Doe ze hier, vóór
  blok 1, en haal de tijd bij blok 2 en blok 5 vandaan. De bundels zijn ook thuis te maken;
  Rochambeau samen opbouwen is dat niet.
- **Blok 2 loopt uit omdat iedereen fouten aan het maken is.** Laat het lopen.
  Kort blok 4 in en geef de stringopgaven mee als huiswerk; de uitwerking staat
  in `source/solutions/2_sequenties_en_data.ipynb`, dus ze kunnen zichzelf
  nakijken.
- **De helft komt niet aan de bundels toe.** Prima. Alleen de basis hoort af te
  komen, en die is huiswerk. Wat je wel doet is in blok 6 vijf minuten nemen om
  te zeggen wat af moet.
- **Iemand is na een halfuur met alles klaar.** De extra, en daarna de
  uitbreidingen van Rochambeau (`## Uitbreidingen`). Die zijn er precies
  hiervoor.

## 5. Wat je verder moet weten

### Eigenaardigheden in het materiaal

- **De koppen `### Opdracht 1` tot en met `### Opdracht 5` bestaan twee keer**,
  in `source/lectures/2a_var_con.ipynb` en in
  `source/lectures/2b_strings_en_lists.ipynb`. Noem in de klas altijd het bestand
  of het college erbij; een verwijzing zonder wijst naar twee plekken. Hetzelfde
  geldt voor `### Opgave`, die zowel in `source/practicals/2_rochambeau.ipynb`
  als in `source/problems/2_opstap.ipynb` staat.
- **`### Positie` en `### Slicing` staan allebei twee keer in
  `source/lectures/2b_strings_en_lists.ipynb`**, één keer voor lijsten en één
  keer voor strings.
- **De tweede reeks van de opstap is het tweede college nog een keer.** De vijf
  opdrachten van `source/lectures/2b_strings_en_lists.ipynb` staan bijna
  letterlijk terug in `source/problems/2_opstap.ipynb`: `### Opdracht 1` als
  `### Opgave 2-A`, `2-B` en `2-C`, en `### Opdracht 2` tot en met
  `### Opdracht 5` als `2-F` tot en met `2-I`. Drie ervan zijn woordelijk gelijk;
  de rest verschilt alleen in variabelenaam. Alleen `2-D` en `2-E` zijn nieuw.
  Handig om te weten voordat je iemand naar de opstap stuurt.
- **De nummering verschilt per bundel, en binnen een bundel.** Drie gevallen
  waar je tegenaan loopt zodra je naar een opgave verwijst:
  - `source/problems/2_opstap.ipynb` heeft `### Opgave 1-A` tot en met `1-J` en
    `### Opgave 2-A` tot en met `2-I`, maar **geen** `Opgave 3-x`. De derde reeks
    bestaat alleen als `#### Uitwerking 3-A` tot en met `3-G`, onder één
    ongenummerde `### Opgave`. Zeg dus "de debugopgave" en niet "opgave 3".
  - `source/problems/2_basis.ipynb` heeft `### Opdracht 1`, `2` en `3` onder
    `## Formules en variabelen`, en daarnaast een **ongenummerde** `### Opdracht`
    onder `## Interactieve fictie`. "Opdracht 4" bestaat niet.
  - `source/practicals/2_rochambeau.ipynb` heeft één ongenummerde `### Opgave`
    plus vier uitbreidingen zonder nummer.
- **In de uitwerkingen staat de debugopgave een kopniveau hoger.**
  `source/problems/2_opstap.ipynb` schrijft `#### Uitwerking 3-A`,
  `source/solutions/2_opstap.ipynb` schrijft `### Uitwerking 3-A`. Dezelfde
  namen, ander niveau.
- **`source/course/practical_2.md` heeft als titel `# Werkcollege`**, maar draagt
  beide practica - ook het practicum van bijeenkomst 3. Dat is een restant; de
  begrippenlijst legt `practicals/` bij het practicum. Week 1 heeft hetzelfde.
- **`### Twee voorwaarden tegelijk` staat vóór `## If then else`** en gebruikt
  toch een `if`-statement als voorbeeld. Zie de aantekening bij het blokschema
  van bijeenkomst 1.
- **"Opdracht 8" bestaat niet meer.** De handleiding van 2023 sloot het eerste
  college ermee af als huiswerk en opende het tweede met het nakijken ervan. Lees
  een oude verwijzing dus niet letterlijk: het programma dat het was, is nu
  `source/practicals/2_rochambeau.ipynb`.

### Korte antwoorden bij de collegeopdrachten

Voor de collegeopdrachten van deze week bestaat geen `solutions/`-bestand; die
zijn er wel voor de practica en de bundels. De antwoorden hieronder zijn voor
jou, niet om uit te delen, en ze zijn **uitgevoerd en niet uitgerekend**: waar
het antwoord uit de handleiding van 2023 afweek van wat Python nu doet, staat
hier wat Python doet.

| Opdracht | Bestand | Antwoord |
|---|---|---|
| `### Opdracht 1` | `2a_var_con.ipynb` | **a** `10`; **b** `55`; **c** `False`; **d** `52`; **e** `1`; **f** `2` en `5`; **g** `2.5` en `2` - `/` deelt gewoon, `//` gooit de rest weg |
| `### Opdracht 2` | `2a_var_con.ipynb` | Het berekent het kwadraat van het ingevoerde getal: invoer `7` geeft `49` |
| `### Opdracht 3` | `2a_var_con.ipynb` | Het drukt alleen `True` of `False` af, en dat vertelt de gebruiker niet wélk getal het grootste is |
| `### Opdracht 4` | `2a_var_con.ipynb` | **a** `2`; **b** `5` en `2`; **c** geen uitvoer; **d** een `IndentationError` |
| `### Opdracht 5` | `2a_var_con.ipynb` | **a** `2`; **b** `5`; **c** `3` en `7` |
| `### Opdracht 6` | `2a_var_con.ipynb` | **a** `bonjour`; **b** `hello`; **c** `bonjour`; **d** `hello` |
| `### Opdracht 7` | `2a_var_con.ipynb` | **a** `42`; **b** `4`; **c** `6.0`; **d** `21.0`; **e** `12` - let op de nullen bij **c** en **d**, want `/` levert altijd een floating-point getal |
| `### Opdracht 1` | `2b_strings_en_lists.ipynb` | **a** `123123`; **b** `hanzehanzeHogeschool`; **c** `123 456` |
| `### Opdracht 2` | `2b_strings_en_lists.ipynb` | **1** `6`; **2** `3`; **3** `5`; **4** `[4, 1]`; **5** `pi[:3]`; **6** `pi[::2]` |
| `### Opdracht 3` | `2b_strings_en_lists.ipynb` | **1** `'pi'`; **2** `'i'`; **3** `['pi']`; **4** `'parent'`; **5** `'Yeah cs!'`; **6** `M[-5:-2]`; **7** `M[30:14:-4]` |
| `### Opdracht 4` | `2b_strings_en_lists.ipynb` | **1** `15`; **2** `[1, 4, 1, 4, 1, 4]`; **3** `pi[0] * pi[::2]` |
| `### Opdracht 5` | `2b_strings_en_lists.ipynb` | **1** `False`; **2** `True`; **3** `False`; **4** `True`; **5** `True`; **6** `False` |

**Drie antwoorden uit 2023 klopten niet meer.** Bij Opdracht 7 **c** en **d** van
`2a` stond `6` en `21`; er komt `6.0` en `21.0` uit, omdat `/` een
floating-point getal oplevert. En bij Opdracht 1 **b** van `2b` stond
`hanzehanzehogeschool`; in het huidige materiaal staat er een hoofdletter in de
tweede string, dus het antwoord is `hanzehanzeHogeschool`. Dat laatste is meteen
de valkuil van dat blok, want hoofdletters vergelijken anders dan kleine letters.

De nummering van Opdracht 2 tot en met 5 van `2b` volgt de lijst zoals de student
hem ziet. In de bron van het notebook staan de nummers van Opdracht 3 in de
volgorde 1, 2, 3, 6, 7, 4, 5; Markdown hernummert die bij het renderen naar 1 tot
en met 7.

### Wat er uit de handleidingen van 2023 niet is overgenomen

**Prowise Presenter** is de grootste post: de oude handleiding raadde aan
studenten hun antwoorden via die software naar het bord te laten sturen. Dat
hangt aan een hulpmiddel dat niet in elke zaal staat en niet bij dit vak hoort,
dus het staat er niet meer in. De twee andere tips uit datzelfde rijtje - de
beurt willekeurig geven, en de opdrachten eerst op papier laten maken - staan wel
in sectie 2. Verder is **Opdracht 8** niet als opdracht overgenomen omdat hij
niet meer bestaat; de vijf fouten die er in de oude uitwerking met de hand bij
waren geschreven staan hier terug als valkuilen, bij het onderwerp waar ze
optreden en niet bij een opdrachtnummer. De **antwoordenlijsten** uit beide
documenten zijn nagerekend en staan hierboven.

De volledige verantwoording per aanwijzing staat in werkitem #182.

### Wat er nog loopt

- **Week 2 wordt herzien in werkitem #169.** Op 5 september 2026 is daar nog geen
  weekontwerp voor vastgesteld. Twee dingen daaruit raken deze handleiding. Het
  eerste is dat de drie p's uit de opening van
  `source/lectures/2a_var_con.ipynb` verdwijnen; de aanwijzing in sectie 2 is zo
  geschreven dat ze klopt of ze er nu nog staan of niet. Het tweede is de
  terminologie. De vraag of alles `Opgave` of `Opdracht` gaat heten ligt bij de
  vakdeskundige en raakt veel koppen van deze week; en `## Lists` is Engels waar
  `conventies/begrippen.md` *lijst* voorschrijft, dus ook die kop kan nog
  wijzigen. Controleer bij twijfel de kop in het bestand voordat je ernaar
  verwijst.
- De vier `.docx` in `teacher_guides/` voor week 1 en 2 staan er nog. Ze worden
  verwijderd zodra er een besluit ligt over wat er nog uit moet; tot die tijd
  zijn ze de bron en niet de handleiding.
- Deze handleiding beschrijft het materiaal zoals het op 5 september 2026 in de
  repository staat.

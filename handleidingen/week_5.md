# Docentenhandleiding PGM1 week 5

Deze week wordt één lus twee lussen. Vorige week kreeg een lus haar recept van
vijf vragen; deze week gaat vraag 4 - wanneer ben je klaar? - opeens over twee
bereiken tegelijk, en dat is de enige echt nieuwe vaardigheid van de week.
Alles verderop - een bord afdrukken, een bord veranderen, twee elementen van
een lijst met elkaar vergelijken - is diezelfde vaardigheid toegepast op een
ander probleem.

De duurste aanname van de week gaat niet over lussen maar over lijsten. Een
functie die een 2D-lijst "verandert" geeft in werkelijkheid een nieuwe 2D-lijst
terug en laat de oude ongemoeid - precies zoals elke functie tot nu toe in de
cursus. Dat is geen toeval: de mutatiegrens die in week 7 wordt doorbroken
staat deze week nog overeind, en het is een vastgesteld besluit om haar hier te
laten staan. Zie `curriculum/uitgangspunten.md`
§`### Het bord verandert niet in week 5`.

**Bijeenkomst 3 van deze week is geen lesmoment.** Die sessie wordt gebruikt
voor het afnemen van het tentamen, en er is dus geen derde gelegenheid om
lesstof in te halen die bij bijeenkomst 1 of 2 blijft liggen. Sectie 1 en
sectie 4 leggen uit wat dat voor de indeling van de week betekent; het is een
erkende afwijking, vastgelegd in `curriculum/uitgangspunten.md`
§`#### Vijf erkende afwijkingen`.

## 1. De week in het kort

| Bijeenkomst | Vorm | Materiaal |
|---|---|---|
| 1 | College | `source/lectures/5a_geneste_lus.ipynb` |
| 2 | Werkcollege | `source/practicals/5b_boter_kaas_eieren.ipynb` |
| 3 | Tentamen | Geen nieuw lesmateriaal - zie sectie 4 |

**Twee bestanden dragen deze week geen begeleide bijeenkomst.**
`source/practicals/5a_ascii_art.ipynb` (6 opdrachten) en de vijf opgavebundels
in `source/problems/` zijn zelfstandig werk, dat plaatsvindt náást bijeenkomst
1 en 2 in plaats van in een eigen derde bijeenkomst. `5_opstap.ipynb`,
`5_basis.ipynb`, `5_mandelbrot_opstap.md` en `5_mandelbrot_basis.md` horen bij
de verplichte route; de eerste twee bouwen het rasterwerk op en de twee
Mandelbrot-opgaven vormen samen de verplichte kern. `5_extra.md` is de
facultatieve PNG-verkenning en heeft geen inlever- of tentamenroute. Zie *De
bijeenkomstindeling van week 5* hieronder voor de reden.

Daarnaast staan er vier overzichtspagina's die je zelf niet hoeft te
behandelen: `source/course/week_5.md` (`## Geneste lussen en 2D-lijsten`) vat
de week samen voor de student, en `source/course/practical_5.md`,
`source/course/opgaven_5.md` en `source/course/solutions_5.md` zijn de
omslagpagina's boven het werkcollege, de opgaven en de uitwerkingen. Alle zeven
uitwerkingen in `source/solutions/` - `5a_ascii_art.ipynb`,
`5b_boter_kaas_eieren.ipynb`, `5_opstap.ipynb`, `5_basis.ipynb`,
`5_extra.ipynb`, `5_mandelbrot_opstap.md` en `5_mandelbrot_basis.md` - staan
onder die laatste; ze zijn openbaar voor de student.

### De bijeenkomstindeling van week 5

**Bijeenkomst 3 is het tentamen, niet het practicum.** Dit is vastgesteld door
de vakdeskundige, geciteerd in `curriculum/uitgangspunten.md`
§`#### Vijf erkende afwijkingen`: *"de planning is dat de laatste (derde)
sessie van die week gebruikt wordt voor het afnemen van de midterm. er blijven
in die week dus twee bijeenkomsten over voor het materiaal."* Dat is een ander
soort afwijking dan de vier die er al stonden - die gingen over welke map bij
welke bijeenkomst hoort, deze gaat over dat een bijeenkomst geen lesmoment is.

Daarmee vervalt de plek waar het materiaal dat de moedertabel niet kwijt kan
normaal naartoe schuift. Bij week 2, 3 en 4 viel het overtollige
`practicals/`-bestand naar het practicum van bijeenkomst 3, naast de
opgavebundels. Week 5 heeft die derde bijeenkomst niet meer beschikbaar, dus
schuift het overtollige bestand niet door naar een andere bijeenkomst maar naar
zelfstandig werk zonder begeleide sessie - dezelfde plek waar de opgavebundels
al stonden.

**Welk van de twee `practicals/`-bestanden het werkcollege vult, is aan mij om
vast te stellen.** Dat is geen open vraag maar een voorstel, ter bevestiging
bij de poort:

`source/practicals/5b_boter_kaas_eieren.ipynb` hoort bij bijeenkomst 2. Het
bestand geeft onder `### Voorbeeld` een volledig uitgewerkte functie voor de
richting "oost", inclusief grenscontroles en lus - en de uitwerking van
`### Opdracht 1` in `source/solutions/5b_boter_kaas_eieren.ipynb` is die functie
woordelijk. Dat is het duidelijkst denkbare signaal voor een werkcollege: de
docent doet de eerste met de klas voor, en de klas herhaalt en typt mee. De
acht opdrachten vallen bovendien in twee groepen van vier bijna identieke
functies - drie op een rij, dan de generalisatie naar `n` op een rij - wat zich
twee keer leent voor "samen de eerste, de rest zelf".

`source/practicals/5a_ascii_art.ipynb` hoort bij het zelfstandige werk, naast
de opgavebundels. De zes opdrachten lopen op in moeilijkheid zonder gegeven
tussenstap - van een rechthoek naar een driehoek, naar heuvels die de
driehoek hergebruiken, naar een ruit, naar een gestreepte ruit, naar de
laatste die het materiaal zelf "een uitdaging!" noemt - en het materiaal
waarschuwt expliciet tegen "debuggen door willekeurige wijzigingen" en
adviseert "eerst ontwerpen". Dat is een opgave die om rustig, zelfstandig
redeneren vraagt en niet om een gezamenlijk opgebouwde eerste stap; ze past bij
het karakter van de opgavebundels waarmee ze nu de bijeenkomst deelt, niet bij
het karakter van het werkcollege.

Dit voorstel wijkt af van de moedertabel in `curriculum/uitgangspunten.md`
§`### Drie bijeenkomsten per week`, die `practicals/` aan bijeenkomst 2 koppelt.
Bij week 5 doet één van de twee `practicals/`-bestanden dat niet: het landt bij
zelfstandig werk, om de reden hierboven. Zie
§`#### Vijf erkende afwijkingen` voor de vastlegging.

### Over de tijden

De blokschema's hieronder zijn ontworpen op wat bijeenkomst 1 en 2 nodig
hebben. De twee Word-handleidingen van 2023 zijn daarna als controle ernaast
gelegd en niet als vertrekpunt gebruikt, volgens de regel in
`curriculum/uitgangspunten.md`
§`### Wat een docentenhandleiding is, en waar hij staat`.

**Elk blok draagt zijn herkomst.** In de kolom *Herkomst* betekent **B** dat het
blok op een blok uit de handleiding van 2023 steunt, en **R** dat het een
richttijd zonder bron is.

| Bijeenkomst | Blokken | B: bron 2023 | R: richttijd zonder bron |
|---|---|---|---|
| 1 | 8 | 0 | 8 (90 min) |
| 2 | 6 | 0 | 6 (90 min) |
| **samen** | **14** | **0** | **14** |

**Beide handleidingen van 2023 gaan volledig over recursie, en die stof komt in
PGM1 helemaal niet meer voor.** `5a_recursie lezen.docx` behandelt het lezen
van recursieve functies, `5b_feest_met_functies.docx` het schrijven ervan.
Recursie is bij het besluit `### Recursie na de lussen` in zijn geheel naar
PGM2 verplaatst - niet naar een latere PGM1-week, maar eruit - en het huidige
week 5-materiaal bevat nul treffers op de stam `recursi`. Van de twee
handleidingen van week 4 die over recursie gingen, leverde dat toen ook al nul
B-tijden op; hier geldt dezelfde meting voor allebei de handleidingen van deze
week.

Ook een overgenomen **werkvorm** - zoals bij de oefenmidterm van week 4, waar
niet de tijden maar wel "eerst zelf voorspellen, dan de uitwerking" overeind
bleef - levert hier niets op. `5a_recursie lezen.docx` beschrijft "eerst
zelfstandig, dan duo's, dan klassikaal bespreken" voor leesopdrachten, maar het
individuele voorspel-en-controleer-patroon staat al onafhankelijk in het
huidige materiaal zelf (`5a_geneste_lus.ipynb`, cel bij
`### Tellen in een raster`: *"Voorspel eerst wat hier uit komt, en voer het
daarna uit"*) en niet als iets dat uit deze bron is overgenomen.
`5b_feest_met_functies.docx` beschrijft "eerst samen een plan maken, dan
zelfstandig, dan een student presenteert", maar diezelfde beweging - samen de
eerste opbouwen, dan zelfstandig de rest - staat al in de opdrachtstructuur van
`5b_boter_kaas_eieren.ipynb` zelf, via de gegeven `### Voorbeeld`-cel. Beide
werkvormen zijn dus al aanwezig in het huidige materiaal, om redenen die niets
met de bron van 2023 te maken hebben; ze als overgenomen aanmerken zou een
verzonnen herkomst zijn. `5b_feest_met_functies.docx` noemt onder "Opties" ook
drie differentiatietechnieken - kleine groepjes, een ervaren met een onervaren
student koppelen, kapotte code op het bord laten debuggen - maar die zijn
generiek en aan geen tijdsblok gebonden; ze zijn bekeken en bewust niet
overgenomen, en raken het B/R-cijfer niet. Vandaar 0 van de 14 blokken met een
**B**.

Alle veertien blokken tellen op tot **90 minuten** per bijeenkomst, met een
ongetimede pauze. **Hoe lang een bijeenkomst werkelijk duurt staat nergens in
de repository.** Duurt die van jou korter of langer, schaal de blokken dan mee.

### Wat je nodig hebt

- **Een scherm waarop je code kunt uitvoeren terwijl de klas kijkt.** Het
  college draait op cellen die je voordoet en cellen die de klas eerst
  voorspelt; zonder scherm valt dat weg.
- **Een raster op het bord, of iets dat er één kan tekenen.** Een bord van
  boter, kaas en eieren is een 3-bij-3-raster van tekens, en de indices `row`
  en `col` zijn precies waar bijeenkomst 1 en 2 om draaien. Een geschetst
  raster met rij- en kolomnummers erlangs bespaart je vanaf blok 2 van het
  college telkens opnieuw uitleggen.
- **Python Tutor in de browser, als uitwijk.** Geen van beide bijeenkomsten
  vraagt er standaard om, maar `source/problems/5_opstap.ipynb` verwijst er
  zelf naar voor wie de dubbele lus van Opdracht 1 tot en met 4 niet in één
  keer ziet, en dat geldt evengoed voor een student die in de klas vastloopt.
- **Papier of een geschreven kladversie.** De voorspel-cellen van het college
  en het samen opbouwen van `in_a_row_3_east` in het werkcollege zijn beide
  alleen iets waard als de klas een antwoord heeft vóórdat de cel draait of
  jij typt.

## 2. Bijeenkomst 1 - College: geneste lussen

Materiaal: `source/lectures/5a_geneste_lus.ipynb`.

De dragende lijn is de stap van één bereik naar twee: eerst een korte
opfrisser met één lus over één lijst, dan het raster als nieuw soort gegeven,
dan twee lussen om het te bouwen en te lezen, en dan twee lussen die over
dezélfde lijst lopen om paren te vergelijken. Open met de vraag hoe je vorige
week een lijst met één lus doorliep, en zeg dat je aan het eind van deze
bijeenkomst weet wanneer je daar een tweede lus bovenop zet en wanneer je twee
lussen over hetzelfde ding laat lopen.

### Blokschema

| # | Min | Wat er gebeurt | Materiaal, met de letterlijke kop | Werkvorm | Herkomst |
|---|---:|---|---|---|---|
| 1 | 5 | Opfrissen: `compute_sum` en `compute_avg` over `scores`, één lus, één verzamelvariabele | `## Lijsten` | docent, cel uitvoeren | R |
| 2 | 10 | Het raster als gegeven: spreadsheets en afbeeldingen als 2D-lijst, en `L[row][col]` tegenover schaakbordnotatie | `## 2D-lijsten`, `### Afbeeldingen zijn rasters van pixels`, `### Indices` | docent, klas leest mee | R |
| 3 | 15 | Het bord als toestand, `print_board` met twee geneste lussen, en vraag 4 van het lusrecept over twee bereiken | `## Een raster doorlopen`, `### Een bord als toestand`, `### Het bord afdrukken` | docent doet voor, bord erbij | R |
| 4 | 10 | Tellen in een raster: voorspellen wat een geneste lus met een `if` erin telt | `### Tellen in een raster` | voorspellen, dan uitvoeren | R |
| | | **Pauze** | | | |
| 5 | 15 | Van toestand naar toestand: `place` bouwt een nieuw bord, het oude blijft ongewijzigd | `### Van de ene toestand naar de volgende` | docent doet voor, klas voorspelt de asserts | R |
| 6 | 5 | Korte opfrisser: `max_value` met één lus, als brug terug naar één bereik | `` ## Loop to the `max` `` | docent, cel uitvoeren | R |
| 7 | 10 | Twee lussen over dezelfde lijst: aandelenkoersen, het All Pairs-algoritme als schets, en waarom "alle paren vormen" nog niet klopt | `## Een reeks analyseren`, `### TR Investeringen`, `## All Pairs algoritme`, `### Alle paren vormen` | docent doet voor, klas voorspelt | R |
| 8 | 20 | De functie `min_diff`: startwaarde, `ix2 = ix1 + 1` om dubbels te vermijden, van schets naar code, en de lus stap voor stap | `## Het kleinste verschil in een lijst`, `### Waarde bijhouden`, `### Paarsgewijs`, `` ### De functie `min_diff` ``, `### Van de schets naar de code`, `### De lussen stap voor stap`, `## Waar deze week ophoudt` | docent doet voor, klas vult tabel op bord in | R |

Acht blokken, 90 minuten, alle acht richttijd. Voor het college van week 5
bestaat geen bruikbare bron: zie *Over de tijden*.

**Eén volgorde-eis.** Blok 5 (`place`) blijft vóór blok 8, ook als de tijd
knelt. Het is de plek waar de klas voor het eerst ziet dat een functie die een
raster "verandert" in werkelijkheid een nieuw raster teruggeeft, en die
gewoonte draagt de rest van de week: `problems/5_basis.ipynb` bouwt bij
`add_fund` en `chart` op precies hetzelfde patroon, en de uitwerking van
`in_a_row_3_east` in het werkcollege van morgen leest en verandert nooit het
meegegeven bord.

### Hoe je het brengt

**Blok 1.** Voer de cel met `compute_sum(scores)` en `compute_avg(scores)` uit
en vraag niets nieuws - dit is vorige week. Eén lus, één verzamelvariabele,
`range(len(numbers))`. Zeg dat je dat patroon vandaag twee keer tegelijk gaat
gebruiken.

**Blok 2.** Laat het scoreformulier-voorbeeld zien: een lijst van lijsten, met
per student een rij en per vraag een kolom. Ga dan naar de indices: `L[3]` is
een hele rij, `L[3][3]` is één getal uit die rij. Zet het schaakbord ernaast en
wijs op het verschil: bij een schaakbord tellen rijen van 8 naar 1 en kolommen
van a naar h, bij een 2D-lijst tellen beide gewoon vanaf 0 en staat de rij
altijd eerst. Dat verschil is precies waar studenten hun eigen ervaring met
rasters op projecteren.

**Blok 3.** Zet het bord `L = [["X", " ", "O"], [" ", "X", " "], ["O", " ",
"X"]]` op het scherm en herinner aan het gegevensformaat: drie strings van één
teken, `"X"`, `"O"` of `" "`. Loop dan `print_board` regel voor regel langs:
de buitenste lus kiest de rij, de binnenste de kolom. Stel de vraag van vraag
4 van het lusrecept twee keer: wanneer is de binnenste lus klaar (na de laatste
kolom van de huidige rij), wanneer de buitenste (na de laatste rij). Wijs erop
dat `len(L)` het aantal rijen is en `len(L[0])` het aantal kolommen - de lengte
van de eerste rij.

**Blok 4.** Laat de klas eerst voorspellen wat de tel-cel bij
`### Tellen in een raster` aflevert, vóórdat je hem uitvoert. Het antwoord is
`3` - drie keer `"X"` in het bord van blok 3. Vraag daarna hardop: wat is hier
de verzamelvariabele, en wat is de startwaarde? `count` en `0`.

**Blok 5.** Dit is het blok dat de week draagt. Voer `place(L, 0, 1, "O")` uit
en laat de klas vóór het draaien voorspellen wat er met `L` zelf gebeurt.
Draai de cel en loop de vier asserts langs: `after[0]` is veranderd,
`after[1]` niet, en `L[0]` is nog steeds het origineel. Zeg met zoveel woorden
wat de functie doet: ze bouwt een heel nieuw bord op, positie voor positie, en
kiest per positie tussen het nieuwe symbool en wat er al stond. Dat is geen
kortere manier om één vakje te veranderen - dat kán deze week niet - maar de
enige manier die met het gereedschap van deze week beschikbaar is. Koppel dat
expliciet aan het besluit in `curriculum/uitgangspunten.md`
§`### Het bord verandert niet in week 5`: die grens is bewust gehandhaafd, en
week 7 laat zien wat er verandert als ze wordt losgelaten.

**Blok 6.** Kort. `max_value = numbers[0]` als startwaarde, dan één lus die
`max_value` bijwerkt zodra ze een groter element ziet. Dit is geen nieuw
onderwerp maar een adempauze tussen twee dichte blokken, en de brug naar de
rest van het college: zo meteen lopen er weer twee lussen, maar nu over
dezelfde lijst.

**Blok 7.** Introduceer `prices = [40, 80, 10, 30, 27, 52, 5, 15]` met het
verhaal van TR Investeringen: de beste dag om te kopen, de beste dag om te
verkopen. Zet de schets van het All Pairs-algoritme op het scherm en laat zien
dat "alle paren vergelijken" met twee lussen over dezelfde lijst gaat, in
plaats van met een buitenste en een binnenste lus over rijen en kolommen zoals
in blok 3. Draai dan de cel bij `### Alle paren vormen` (`numbers = [1, 2, 3]`)
en laat de klas de uitvoer voorspellen vóór je hem uitvoert. Bespreek waarom ze
nog niet klopt: er staan paren van een element met zichzelf tussen (`1 1`,
`2 2`), en elk paar komt twee keer voor (`1 3` én `3 1`).

**Blok 8.** Bouw `min_diff` in stappen op. Begin met de startwaarde
`mdiff = abs(numbers[0] - numbers[1])` en vraag waarom die niet `0` kan zijn:
omdat je dan een verschil zou kunnen "vinden" dat niet in de lijst voorkomt.
Zet daarna `for ix2 in range(ix1 + 1, len(numbers))` tegenover blok 7's versie
zonder die verschuiving, en laat de klas benoemen wat er verdwijnt: de paren
met zichzelf en de dubbele paren. Loop dan de tabel *Van de schets naar de
code* op het bord langs, kolom voor kolom, en trace daarna `min_diff([42, 3,
100, -9, 7])` uit de cel bij `### De lussen stap voor stap` op het bord mee:
elke regel toont `ix1`, `ix2` en de nieuwe waarde van `mdiff` zodra die
verandert. Sluit af met de laatste alinea van `## Waar deze week ophoudt`: wat
je vandaag kunt (een raster bouwen, lezen, en er een nieuw raster uit
afleiden) en wat met dit gereedschap niet lukt (één vakje veranderen zonder de
rest opnieuw op te bouwen) - en dat daar in week 7 een nieuw vermogen bij komt.

### Waar het vastloopt

- **`place` lijkt het bord te veranderen, maar geeft een nieuw bord terug**
  (`### Van de ene toestand naar de volgende`). **Stil**: er komt geen
  foutmelding, en wie het resultaat niet opvangt met `L = place(L, ...)` ziet
  domweg niets gebeuren. Zeg hardop dat dit hetzelfde patroon is als bij elke
  functie tot nu toe in de cursus - niets nieuws, alleen nu op een raster.
- **`len(L)` en `len(L[0])` verwisseld** (`### Het bord afdrukken`). **Stil**,
  en juist onopvallend deze week: het bord van boter, kaas en eieren is altijd
  3 bij 3, dus `len(L)` en `len(L[0])` leveren toevallig hetzelfde getal.
  Verwissel je ze, dan merkt niemand het vandaag. Zeg erbij dat dat bij een
  rechthoekig raster - zoals het koersenraster van `problems/5_basis.ipynb` -
  wél meteen fout gaat.
- **`min_diff` op een lijst van één element** (`` ### De functie `min_diff` ``).
  **Luid**: `abs(numbers[0] - numbers[1])` vraagt om een tweede element, en
  `min_diff([5])` geeft een `IndexError`. De functie gaat er stilzwijgend van
  uit dat de lijst minstens twee elementen heeft; dat staat nergens
  gecontroleerd.

### Als het niet uitkomt

- **Blok 8 loopt uit.** Laat de stap-voor-stap-trace op het bord vervallen en
  geef de tabel *Van de schets naar de code* mee als leeswerk; die tabel is de
  kern, de trace is herhaling ervan met concrete getallen.
- **Je komt niet aan blok 7 en 8 toe.** Haal de tijd dan bij **blok 6**
  vandaan door hem over te slaan - `max_value` is letterlijk vorige week in
  een nieuw jasje en de klas heeft hem niet nodig om blok 7 te volgen - en
  niet bij blok 5: zonder `place` mist bijeenkomst 2 morgen de reden waarom
  `in_a_row_3_east` het meegegeven bord nooit verandert.
- **Blok 3 of 4 loopt uit.** Haal de tijd bij **blok 2** vandaan door de
  vergelijking met het schaakbord over te slaan; de indices `L[row][col]` zelf
  komen in blok 3 vanzelf nog een keer langs.
- **Je houdt tijd over.** Laat de klas bij blok 8 ook `min_diff(prices)`
  narekenen (de lijst met aandelenkoersen uit blok 7) en controleren dat het
  antwoord `3` is, vóór je de assert-cel uitvoert.

**Wat je niet inkort.** Blok 5, om de reden die hierboven bij het blokschema
staat. En de laatste alinea van blok 8, `## Waar deze week ophoudt`: dat is de
enige plek waar de grens van deze week met zoveel woorden bij naam wordt
genoemd en vooruitgewezen naar week 7.

## 3. Bijeenkomst 2 - Werkcollege: boter, kaas en eieren

Materiaal: `source/practicals/5b_boter_kaas_eieren.ipynb`, met de acht
uitwerkingen in `source/solutions/5b_boter_kaas_eieren.ipynb`.

Dit is het werkcollege in de zin van `curriculum/uitgangspunten.md`: de plek
waar een probleem gezamenlijk stap voor stap wordt opgebouwd. Deze bijeenkomst
doet dat twee keer, met dezelfde beweging beide keren: **samen de eerste
opbouwen, dan de rest van de groep zelf.** De acht functies controleren of er
drie, en later `n`, gelijke tekens op een rij staan vanaf een startpositie, in
een van vier richtingen.

### Blokschema

| # | Min | Wat er gebeurt | Materiaal, met de letterlijke kop | Werkvorm | Herkomst |
|---|---:|---|---|---|---|
| 1 | 10 | Aftrap: de gegeven functies `print_2d` en `create_array` overnemen, het gegevensformaat, en het `Voorbeeld` voor de richting oost doorlopen | `## Gegeven code: een 2D-lijst afdrukken en aanmaken`, `## Drie op een rij`, `### Voorbeeld` | docent doet voor | R |
| 2 | 20 | **Samen `in_a_row_3_east` opbouwen**: eerst de twee grenscontroles, dan de lus over drie posities | `### Opdracht 1` | klassikaal, klas dicteert, docent typt | R |
| 3 | 15 | Zelf `in_a_row_3_south`, `in_a_row_3_southeast` en `in_a_row_3_northeast`: dezelfde vorm, een andere richting en een andere grenscontrole | `### Opdracht 2`, `### Opdracht 3`, `### Opdracht 4` | zelfstandig, docent loopt rond | R |
| | | **Pauze** | | | |
| 4 | 15 | **Samen naar `in_a_row_n_east`**: wat verandert als "drie" de variabele `n` wordt, wat blijft hetzelfde | `## Van 3 naar N: N op een rij`, `### Opdracht 5` | klassikaal | R |
| 5 | 20 | Zelf `in_a_row_n_south`, `in_a_row_n_southeast` en `in_a_row_n_northeast`: dezelfde overgang op de drie andere richtingen | `### Opdracht 6`, `### Opdracht 7`, `### Opdracht 8` | zelfstandig | R |
| 6 | 10 | Afronden: de randgevallen bespreken en het bestand met alle acht functies bewaren | `### Randgevallen` (in `source/solutions/5b_boter_kaas_eieren.ipynb`) | klassikaal, docent doet voor | R |

Zes blokken, 90 minuten, alle zes richttijd. Voor deze bijeenkomst bestaat geen
bruikbare bron: zie *Over de tijden*.

### Hoe je het brengt

**Blok 1.** Laat de klas `print_2d` en `create_array` overnemen in hun eigen
bestand en uitvoeren - dit is gegeven code, geen opdracht. Wijs op het
gegevensformaat: elke 2D-lijst bestaat uit rijen die zelf lijsten zijn, en elk
element is een string van precies één teken, `"X"`, `"O"` of `" "`. Loop dan de
cel bij `### Voorbeeld` langs: eerst `if row_start >= n_rows`, dan
`if col_start > n_cols - 3`, en pas daarna de lus `for ix in range(3)` die
`char` drie keer naar het oosten controleert. Zeg dat Opdracht 1 zo meteen
precies deze functie is.

**Blok 2.** Samen, jij typt, de klas dicteert. Herhaal eerst waaróm de
grenscontroles vóór de lus staan: de opdrachttekst eist dat een positie zonder
ruimte `False` teruggeeft, en dat moet je vaststellen vóórdat je in het bord
gaat kijken. Bouw `in_a_row_3_east` op zoals het Voorbeeld dat deed, en laat de
klas vóór elke regel voorspellen wat er moet staan. Loop daarna de vier
asserts van Opdracht 1 (`create_array(3, 4, "XXOXXXOOOOOO")`) één voor één na
en laat de klas voorspellen wat elke aanroep teruggeeft vóór je de cel draait.

**Blok 3.** Zelfstandig, Opdracht 2 (zuid), 3 (zuidoost) en 4 (noordoost).
Loop rond en vraag bij elke functie hetzelfde: welke twee getallen verander je
per stap van de lus, en welke kant op? Bij zuid is dat `row_start + ix` met
`col_start` vast; bij zuidoost allebei `+ ix`. Noordoost is de lastigste van de
vier, want daar draait de richting van de telling om: wijs erop dat de
grenscontrole naar boven moet kijken (`row_start` mag niet te klein zijn) in
plaats van naar onderen.

**Blok 4.** Samen. Vraag eerst wat er verandert als "drie op een rij"
"`n` op een rij" wordt: de grenscontrole rekent voortaan met `n` in plaats van
`3`, en de lus loopt `range(n)` keer in plaats van `range(3)`. Vraag dan wat
hetzelfde blijft: de richting, en de vorm van de twee controles. Bouw
`in_a_row_n_east` samen op door in de oplossing van Opdracht 1 de twee keer
`3` te vervangen door `n`, en laat de klas de nieuwe asserts (met `n = 4` en
`n = 5` op een 5 bij 5-raster) vóór het draaien voorspellen.

**Blok 5.** Zelfstandig, Opdracht 6, 7 en 8: dezelfde overgang van 3 naar `n`,
toegepast op de drie richtingen uit blok 3. Wie blok 3 goed had, past hier
alleen de twee `3`'en aan; wie daar vastliep, loopt hier tegen dezelfde
grenscontrole aan als toen.

**Blok 6.** Bespreek de cel bij `### Randgevallen` in de uitwerking: een
positie net buiten de grenzen voor alle acht functies, en dat `n = 1` altijd
`True` geeft op de startpositie zelf - er is dan immers maar één teken nodig.
Zeg waarom dat laatste zo is en niet toevallig: bij `n = 1` valt de lus samen
met de allereerste stap. Laat iedereen zijn acht functies in één bestand
bewaren; zeg erbij dat boter, kaas en eieren met deze functies al op te lossen
is, en dat dezelfde functies straks een speler nodig heeft die zelf zet.

### Waar het vastloopt

- **De vier richtingen lijken identiek maar wisselen welke as je controleert
  en in welke richting je optelt of aftrekt** (Opdracht 1 tot en met 4 en 5 tot
  en met 8). **Stil**: een verwisselde `+` en `-` bij noordoost geeft geen
  foutmelding, alleen een verkeerd antwoord, en de gegeven tests vangen dat
  pas als de testcase toevallig die combinatie raakt.
- **Een vergeten of verkeerde grenscontrole** (`col_start > n_cols - n`, of nog
  met `- 3` terwijl `n` al gebruikt wordt). **Luid**: de lus indexeert dan
  buiten de rij en geeft een `IndexError`. De asserts van Opdracht 5 raken dit
  direct, want die testen met `n = 4` en `n = 5` op een raster van vijf
  kolommen.
- **Noordoost zonder de controle op de bovengrens** (`row_start < n - 1`).
  **Stil**, en het gevaarlijkste geval van de twee: `array[row_start - ix]`
  wordt bij een te kleine `row_start` een negatieve index, en Python leest een
  negatieve index niet als fout maar als "tel vanaf het einde". Er komt dus
  een plausibele maar volledig verkeerde waarde uit, zonder enige melding.

### Als het niet uitkomt

- **Blok 2 loopt uit.** Laat het lopen. Haal de tijd bij **blok 3** vandaan
  door Opdracht 4 (noordoost, de lastigste van de vier) mee te geven: Opdracht
  8 herhaalt exact dezelfde overgang en vangt het probleem dus nog een keer.
- **Je komt niet aan blok 5 toe.** Doe Opdracht 5 (oost, met `n`) nog samen in
  blok 4 en geef Opdracht 6 tot en met 8 mee; begin de volgende keer niet met
  bespreken, want er is geen volgende keer voor deze stof.
- **Iemand raakt in blok 3 of 5 de tel van grenscontroles kwijt.** Verwijs
  terug naar het Voorbeeld van blok 1: dezelfde twee vragen - is er ruimte in
  de rij, is er ruimte in de kolom - komen bij elke richting terug, alleen in
  een andere volgorde.
- **Je houdt tijd over.** Laat duo's bij blok 6 ook `n = 0` proberen op elke
  functie en voorspellen wat er gebeurt vóórdat ze het draaien: de lus
  `range(0)` doet dan niets en de functie geeft meteen `True` terug, ook al is
  er niets gecontroleerd.

**Wat je niet inkort.** Blok 2 en blok 4, de twee "samen"-momenten. Dat zijn de
enige twee plekken in de week waar een probleem gezamenlijk van nul af wordt
opgebouwd, en het is de reden dat dit het werkcollege is.

## 4. Bijeenkomst 3 - Tentamen

Bijeenkomst 3 van week 5 draagt geen lesmateriaal. De sessie wordt gebruikt om
het tentamen af te nemen; zie *De bijeenkomstindeling van week 5* in sectie 1
en de vastlegging in `curriculum/uitgangspunten.md`
§`#### Vijf erkende afwijkingen`. De planning en organisatie van het tentamen
zelf lopen buiten deze repository en buiten deze handleiding.

### Wat hier gebeurt

Er is geen nieuw materiaal om te brengen en dus geen blokschema. Voor de
docent van bijeenkomst 1 en 2 betekent dit vooral dat er geen derde moment
meer is om iets in te halen: wat in het college of het werkcollege van deze
week blijft liggen, komt niet "morgen" aan de beurt. Zie de uitwijkopties in
sectie 2 en 3 voor wat je in dat geval laat vallen en wat niet.

### Wat je als docent doet

Er is voor deze bijeenkomst inhoudelijk niets voor te bereiden uit het
materiaal van week 5 - de logistiek van het afnemen van een tentamen is aan de
opleiding en valt buiten wat deze handleiding beschrijft. Wat wel bij jou
hoort: zeg in bijeenkomst 2 expliciet waar het zelfstandige werk van deze week
staat - `source/practicals/5a_ascii_art.ipynb` en de vijf opgavebundels in
`source/problems/` - en dat daar, anders dan in andere weken, geen begeleide
derde bijeenkomst meer voor is. Wie moeite heeft, moet dat vóór het tentamen
weten, niet erna.

## 5. Wat je verder moet weten

### Eigenaardigheden in het materiaal

- **"Opdracht 1" wijst deze week naar drie plekken op twee kopniveaus.** In
  `source/practicals/5a_ascii_art.ipynb` is het een `## Opdracht 1`; in
  `source/practicals/5b_boter_kaas_eieren.ipynb` is het een `### Opdracht 1`,
  want daar staat hij genest onder `## Drie op een rij`; en in
  `source/problems/5_opstap.ipynb` is het weer een `## Opdracht 1`. Noem dus
  altijd het bestand erbij, niet alleen het opdrachtnummer.
- **Dezelfde slotalinea staat letterlijk in twee bestanden.** De laatste
  alinea van `## Waar deze week ophoudt` in
  `source/lectures/5a_geneste_lus.ipynb` en de laatste alinea van
  `## Tot slot` in `source/problems/5_basis.ipynb` zijn woordelijk dezelfde
  tekst over de grens van deze week en de vooruitwijzing naar Game of Life in
  week 7. Dat is met opzet: `curriculum/uitgangspunten.md`
  §`### Het bord verandert niet in week 5` noemt beide vindplaatsen met name
  als de vastgelegde afsluiting van de week.
- **`source/practicals/5b_boter_kaas_eieren.ipynb` geeft de oplossing van
  Opdracht 1 al weg.** De cel bij `### Voorbeeld` en de uitwerking van
  Opdracht 1 in `source/solutions/5b_boter_kaas_eieren.ipynb` zijn identiek.
  Dat is geen lek maar de aanleiding voor blok 2 van bijeenkomst 2: het is
  precies het materiaal dat je samen met de klas opnieuw opbouwt.
- **De schaakbordvergelijking in het college wijst op een verschil, geen
  gelijkenis.** `source/lectures/5a_geneste_lus.ipynb` zet `L[row][col]`
  naast schaaknotatie juist om te laten zien dat rijen en kolommen bij een
  2D-lijst anders tellen dan bij een schaakbord (rijen 8 tot en met 1, kolommen
  a tot en met h). Wie de afbeelding zonder die uitleg laat zien, wekt het
  tegenovergestelde beeld.
- **`source/problems/5_extra.md` is de enige "extra" van de week, en zij is
  geen losstaande uitdaging.** Anders dan in de meeste weken vormen opstap,
  basis en extra hier geen drie gelijkwaardige niveaus voor hetzelfde
  probleem: `5_mandelbrot_opstap.md` en `5_mandelbrot_basis.md` bouwen de
  rekenkern op, en `5_extra.md` (*"Extra: Mandelbrot verkennen"*) is de
  afbeelding die daarmee wordt getekend. Wie er twee van de drie mist, mist
  een stap in dezelfde lijn en geen los onderwerp.

### Korte antwoorden bij de collegeopdrachten

**Deze subsectie is bij week 5 leeg, en dat is geen omissie.**
`source/lectures/5a_geneste_lus.ipynb` bevat geen enkele genummerde
`## Opdracht`-kop; de twee plekken waar de klas iets voorspelt -
`### Tellen in een raster` en `### Alle paren vormen` - zijn cellen binnen de
doorlopende collegetekst, geen aparte opdrachten met een eigen uitwerking. Er
is dus dit keer niets om als kort antwoord te geven: het college draagt geen
opdrachten die om een uitwerking vragen.

### Wat er uit de handleidingen van 2023 niet is overgenomen

Er zijn twee Word-handleidingen voor week 5 geweest, en er is van geen van
beide een tijd of een werkvorm overgenomen. Dat is geen oordeel over die
documenten maar het gevolg van één verschuiving: beide gaan volledig over
recursie, en recursie is bij het besluit `### Recursie na de lussen` in zijn
geheel naar PGM2 verplaatst.

`5a_recursie lezen.docx` beschrijft een les van 90 minuten waarin de klas tien
leesopdrachten over recursieve functies individueel voorspelt, in duo's
vergelijkt en klassikaal bespreekt. `5b_feest_met_functies.docx` beschrijft een
les waarin de klas eerst samen een plan van aanpak maakt - basisgeval,
recursief geval - en daarna zelfstandig vier recursieve functies schrijft, met
een student die zijn oplossing presenteert. Beide werkvormen zijn op zichzelf
bruikbaar lesontwerp, maar ze staan al onafhankelijk in het huidige materiaal:
het voorspel-en-controleer-patroon zit al in de collegecellen van
`5a_geneste_lus.ipynb`, en het patroon "samen de eerste opbouwen, dan
zelfstandig de rest" zit al in de opzet van `5b_boter_kaas_eieren.ipynb`, via
de gegeven `### Voorbeeld`-cel. Ze als overgenomen uit de bron van 2023
vastleggen zou dus een herkomst verzinnen die er niet is; zie *Over de tijden*
in sectie 1 voor de volledige afweging.

`teacher_guides/5a_recursie lezen.docx` en
`teacher_guides/5b_feest_met_functies.docx` zijn met dit werkitem verwijderd,
volgens de regel in `curriculum/uitgangspunten.md`
§`### Wat een docentenhandleiding is, en waar hij staat`: zodra een handleiding
er is, gaat de `.docx` van die week weg. Wie ze wil nalezen vindt ze in de
git-geschiedenis.

### Wat er nog loopt

- **De bijeenkomstindeling van week 5 is met dit werkitem voorgesteld**, als
  vijfde erkende afwijking in `curriculum/uitgangspunten.md`
  §`#### Vijf erkende afwijkingen`. Het deel over bijeenkomst 3 als tentamen is
  al vastgesteld door de vakdeskundige, geciteerd in diezelfde paragraaf; het
  deel over de verdeling van `5a_ascii_art.ipynb` en
  `5b_boter_kaas_eieren.ipynb` over het werkcollege en het zelfstandige werk is
  mijn eigen meting en voorstel, ter bevestiging bij de poort van #276.
- **`curriculum/uitgangspunten.md` bevat een niet meer kloppende statusregel.**
  Het besluitenregister zegt bij *Week 4 krijgt een lusrecept van vijf vragen*:
  *"week 5 pikt het nog niet op (#163)"*. Dat klopt niet meer: het huidige
  materiaal verwijst er acht keer naar, over vijf bestanden - eenmaal in
  `5a_geneste_lus.ipynb`, driemaal in `problems/5_basis.ipynb`, eenmaal in
  `problems/5_extra.md`, tweemaal in `problems/5_opstap.ipynb` en eenmaal in
  `solutions/5_opstap.ipynb`. Dit valt buiten de afbakening van dit werkitem
  (alleen `handleidingen/week_5.md` en de bijeenkomstindeling in
  `curriculum/uitgangspunten.md`) en is hier gemeld, niet gerepareerd.
- **De twee Word-handleidingen van week 6 zijn met #280 verdwenen**, en daarmee
  bestaat `teacher_guides/` niet meer.
- **Deze week levert geen enkele overgeleverde tijd op.** Tot een docent haar
  geeft en de klok erbij houdt, staan alle veertien blokken als richttijd, en
  zo horen ze gelezen te worden.
- Deze handleiding beschrijft het materiaal zoals het op **23 september 2026**
  in de repository staat.

# Docentenhandleiding PGM1 week 6

Deze week gaat over wat er onder een waarde ligt: bits, een type dat zegt hoe
je ze leest, en een bestand dat niets anders is dan een rij bytes. Het college
loopt van de doos in het geheugen naar het tekstbestand, het werkcollege leest
een afbeelding in als lijst van lijsten en schrijft een nieuwe terug, en het
practicum leest en schrijft tekstbestanden.

De draad die de drie bijeenkomsten verbindt is één teken: het regeleinde, `\n`.
Het college laat zien dat regels in een bestand niet bestaan en dat er alleen
tekens staan; de opstap begint ermee (`### Opdracht 1`), de basis ook
(`` ## Stap 1: `strip_newline(line)` ``). Wie dat teken ziet, begrijpt de week.

Twee grenzen gelden deze week. **Binair en talstelsels zijn vervallen**; week 6
is de week van bestanden geworden (`curriculum/leerlijn.md`, en
`curriculum/uitgangspunten.md` §`### Schakelingen en binair`). Binair komt in
het materiaal nog voor als voorstelling van data, niet als rekenkunde om te
oefenen. En **er verandert nog steeds niets ter plekke**: elke bewerking in het
werkcollege bouwt een nieuwe lijst op, net als in week 5. De mutatiegrens ligt
in week 7.

## 1. De week in het kort

| Bijeenkomst | Vorm | Materiaal |
|---|---|---|
| 1 | College | `source/lectures/6a_data.ipynb` |
| 2 | Werkcollege | `source/practicals/6b_images.ipynb` |
| 3 | Practicum | `source/problems/6_opstap.ipynb`, `source/problems/6_basis.ipynb` en `source/problems/6_extra.ipynb` |

Daarnaast staan er vier overzichtspagina's die je zelf niet hoeft te
behandelen: `source/course/week_6.md` (`## Data en bestanden`) vat de week
samen voor de student, en `source/course/practical_6.md`,
`source/course/opgaven_6.md` en `source/course/solutions_6.md` zijn de
omslagpagina's boven het werkcollege, de opgaven en de uitwerkingen. Er zijn
twee uitwerkingen, `source/solutions/6_basis.ipynb` en
`source/solutions/6_extra.ipynb`, en ze zijn openbaar voor de student. Voor
de opstap bestaat er (nog) geen uitwerking (#194), en voor het werkcollege
staat er geen in het boek; zie sectie 5.

### Deze week volgt de moedertabel

Week 6 wijkt niet af van de indeling in `curriculum/uitgangspunten.md`
§`### Drie bijeenkomsten per week`, en staat daarom niet onder
§`#### Vijf erkende afwijkingen`. Er is één bestand in `lectures/`, één in
`practicals/` en er zijn drie opgavebundels in `problems/`, en het materiaal
spreekt de tabel nergens tegen: `source/course/practical_6.md` heeft als titel
`# Werkcollege`, en `source/problems/6_extra.ipynb` begint met *"In het
werkcollege heb je afbeeldingen bewerkt"*. Anders dan in week 5 is de derde
bijeenkomst weer een gewoon practicum; het tentamen lag in week 5.

### Over de tijden

De blokschema's hieronder zijn ontworpen op wat de drie bijeenkomsten nodig
hebben. De twee Word-handleidingen van 2023 voor deze week zijn daarna als
controle ernaast gelegd en niet als vertrekpunt gebruikt, volgens de regel in
`curriculum/uitgangspunten.md`
§`### Wat een docentenhandleiding is, en waar hij staat`.

**Elk blok draagt zijn herkomst.** In de kolom *Herkomst* betekent **B** dat het
blok op een blok uit de handleiding van 2023 steunt, en **R** dat het een
richttijd zonder bron is.

| Bijeenkomst | Blokken | B: bron 2023 | R: richttijd zonder bron |
|---|---|---|---|
| 1 | 7 | 0 | 7 (90 min) |
| 2 | 7 | 0 | 7 (90 min) |
| 3 | 5 | 0 | 5 (90 min) |
| **samen** | **19** | **0** | **19** |

**Beide handleidingen van 2023 gaan over stof die niet meer in week 6 staat.**
De eerste, *Ceasar op orde*, liet de klas `rot13` doornemen en een
Caesar-code kraken; die opgave staat nu in
`source/problems/opdrachten/caesar_op_orde/index.md`, onder
`source/course/opgaven_10.md` in PGM2 week 3. In de elf bestanden van week 6
komen `Caesar`, `rot13`, `encipher` en `decipher` nul keer voor. De tweede,
*Decimaal en verder*, liet de klas getallen omrekenen naar binair en ternair,
en die rekenkunde is met het besluit over binair vervallen. Beide gebruikten
bovendien recursieve oplossingen, en de stam `recursi` komt in het huidige
week 6-materiaal nul keer voor; zie §`### Recursie na de lussen`.

Beide begonnen met *"Start les (5 min)"* en een leerdoel. Dat blok zegt niets
over dit materiaal en is om die reden gewogen en niet overgenomen, net als de
openingsminuten bij week 4. Vandaar 0 van de 19 blokken met een **B**.

Wat wél is overgenomen is een **werkvorm** uit *Ceasar op orde*: bij een
probleem zonder gegeven stappen eerst laten bedenken hoe je het op papier zou
oplossen, en pas daarna programmeren (*"Probeer, plan, programmeer"*). Die
beweging staat niet in het huidige materiaal; in geen van de elf bestanden
komt `papier`, `plan`, `ontwerp` of `schets` voor. Ze staat in blok 5 en 6 van
sectie 3, bij de spiegelingen, en een werkvorm draagt geen herkomstmerk.

Alle negentien blokken tellen op tot **90 minuten** per bijeenkomst, met een
ongetimede pauze. **Hoe lang een bijeenkomst werkelijk duurt staat nergens in
de repository.** Duurt die van jou korter of langer, schaal de blokken dan mee.

### Wat je nodig hebt

- **Een scherm waarop je code kunt uitvoeren terwijl de klas kijkt.** Het
  college heeft maar één codecel; de voorbeelden bij `### Een bestand lezen` en
  `### Een bestand schrijven` staan als leestekst op de pagina. Die voer je zelf
  uit, in een eigen bestand.
- **Een bestand `namen.txt` met de drie namen uit het college**, `Anouk`,
  `Bram` en `Chiara`, elk op een eigen regel. Het staat niet in de repository.
  Zet het klaar in de map waar je je code uitvoert.
- **De bestanden van het practicum, klaar om te verspreiden.** De opstap leest
  `source/problems/assets/woorden.txt` en `source/problems/assets/metingen.txt`,
  de basis de vier sequenties in `source/problems/assets/dna/`. Geen van beide
  bundels geeft de student een downloadlink; zie sectie 4. Hoe je ze
  verspreidt, staat nergens in de repository.
- **Pillow bij de student.** Het werkcollege draait op `png.py`, en dat bestand
  gebruikt Pillow. De student is het al tegengekomen in
  `source/problems/5_mandelbrot_opstap.md`, dat zegt het te installeren zodra
  Python meldt dat het ontbreekt; of iedereen dat heeft gedaan, weet je niet.
  Controleer het aan het begin van bijeenkomst 2 en niet halverwege.
- **Papier.** Voor de voorspellingen in het college en voor de spiegelingen in
  het werkcollege, waar de klas eerst een klein raster tekent.

## 2. Bijeenkomst 1 - College: data

Materiaal: `source/lectures/6a_data.ipynb`.

De dragende lijn is de weg omlaag en weer omhoog: van een variabele naar de
doos in het geheugen, naar bits en bytes, naar het type dat zegt hoe je die
bits leest, en dan terug naar boven, naar een bestand dat ook niets anders is
dan bytes. Open met de vraag wat er eigenlijk gebeurt als je `x = 41` typt, en
zeg dat je aan het eind van deze bijeenkomst een bestand kunt lezen en
schrijven en weet waarom er dan een lege regel verschijnt.

### Blokschema

| # | Min | Wat er gebeurt | Materiaal, met de letterlijke kop | Werkvorm | Herkomst |
|---|---:|---|---|---|---|
| 1 | 5 | Syntax tegenover semantiek, en `x = 41`, `y = x + 1` als opstap naar het geheugen | `## Informatica`, `## Handelingen en data` | docent, cel uitvoeren | R |
| 2 | 15 | De doos als beeld van een variabele: naam, waarde, type en geheugenlocatie; het geheugen als lange rij dozen en als raster op een RAM-kaart | `## Achter het doek`, `### Geheugen` | docent, klas kijkt mee | R |
| 3 | 10 | Een bit is één condensator, een byte acht bits op een rij | `### Bits`, `### Bytes` | docent | R |
| 4 | 15 | Dezelfde bits, een ander type: `1000011` is 67 of `"C"` | `## Hoe zijn gegevens opgeslagen?`, `### ASCII` | docent, klas zoekt op in de tabel | R |
| | | **Pauze** | | | |
| 5 | 10 | Een tekstbestand is een rij bytes; regels bestaan niet, `\n` wel | `## Bestanden`, `### Wat er in een tekstbestand staat` | docent | R |
| 6 | 20 | Lezen met `with open`: de klas voorspelt de uitvoer, en de lege regels worden verklaard | `### Een bestand lezen` | voorspellen, dan uitvoeren | R |
| 7 | 15 | Schrijven met `"w"` en `print(..., file=file)`, en zien dat `"w"` weggooit | `### Een bestand schrijven` | docent doet voor, klas voorspelt | R |

Zeven blokken, 90 minuten, alle zeven richttijd. Voor het college van week 6
bestaat geen bruikbare bron: zie *Over de tijden*.

**Eén volgorde-eis.** Blok 5 komt vóór blok 6, ook als de tijd knelt. De lege
regels in blok 6 zijn alleen te verklaren als de klas al weet dat `\n` een
teken in het bestand is, en die verklaring is precies waar de opstap en de
basis van bijeenkomst 3 mee beginnen.

### Hoe je het brengt

**Blok 1.** Kort. Voer de enige codecel van het notebook uit en vraag waar `41`
en `42` nu staan. Het antwoord is *in het geheugen*, en de rest van de
bijeenkomst gaat over wat dat betekent.

**Blok 2.** Laat de doos zien: een naam op de buitenkant, een waarde erin, en
daarnaast een type en een geheugenlocatie. Zeg dat het geheugen een hele lange
rij van zulke dozen is, en laat dan de foto van de RAM-kaart en het raster
eronder zien. Het raster is geen detail om te onthouden; het is de brug naar
blok 3.

**Blok 3.** Eén kruispunt in het raster is een bit: geladen of niet, `1` of
`0`. Acht naast elkaar is een byte. De vraag *"waarom acht?"* staat zelf in het
materiaal; het antwoord is historisch en loopt via ASCII, en daarmee ben je bij
blok 4.

**Blok 4.** Dit is het blok dat de week draagt. Laat bij `### ASCII` zien dat
de bits `1000011` het getal 67 zijn, en dat de tabel bij 67 het teken `C` zet.
Laat de klas daarna in de tabel opzoeken welk teken bij 68 hoort (`D`). Zeg dan
met zoveel woorden wat de afbeelding met de twee dozen laat zien: de inhoud is
hetzelfde, en het type bepaalt of je er een getal of een teken in leest.

**Blok 5.** Terug naar boven. Het geheugen is leeg zodra je programma stopt, en
een bestand is de plek waar gegevens blijven. Loop het voorbeeld met de drie
namen langs: wat eruitziet als drie regels, is in het bestand
`Anouk\nBram\nChiara\n`. Zeg dat `\n` één teken is, met ASCII-waarde 10, en dat
een regel niets anders is dan de afspraak "hier houdt het op".

**Blok 6.** Laat de klas eerst op papier voorspellen wat de code bij
`### Een bestand lezen` afdrukt, en voer hem dan uit op je eigen `namen.txt`.
De uitvoer is

```text
Anouk

Bram

Chiara

```

met een lege regel na elke naam. Vraag waar die lege regels vandaan komen,
en laat de klas het antwoord uit blok 5 halen: de regel draagt haar eigen
`\n`, en `print` zet er nog een achter. Lees de eerste regel van de code voor
zoals het materiaal dat doet - *open dit bestand, en noem het `file` zolang dit
blok duurt* - en leg niet uit hoe `with` het sluiten regelt. Het materiaal
zegt zelf dat dat in Programmeren 2 komt, en dat is een vastgesteld besluit;
zie `curriculum/uitgangspunten.md` §`### Canonieke vormen, mechanisme later`.

**Blok 7.** Voer het schrijfvoorbeeld uit op hetzelfde `namen.txt`, en laat de
klas vóór het draaien voorspellen wat er daarna in het bestand staat. Lees het
bestand dan opnieuw in: er staan nog twee namen, `Anouk` en `Bram`. `Chiara` is
weg, want `"w"` maakt het bestand leeg zodra het wordt geopend, en daarna staat
er alleen wat het voorbeeld schrijft. Dat is precies het waarschuwingskader
onderaan het notebook, en nu hebben ze het gezien in plaats van gelezen. Sluit
af met de brug naar morgen: een afbeelding is ook een bestand, en in het
werkcollege lees je er een in, verander je hem en schrijf je hem terug.

### Waar het vastloopt

- **De lege regels bij het lezen** (`### Een bestand lezen`). **Stil**: er
  komt geen foutmelding, en de student denkt dat het bestand lege regels
  bevat. Het is dezelfde verwarring waar `### Opdracht 1` van de opstap mee
  begint.
- **`"w"` maakt het bestand leeg, ook als je er niets in schrijft**
  (`### Een bestand schrijven`). **Stil**: een `with open("namen.txt", "w")`
  waarvan het blok niets schrijft, laat een leeg bestand achter, zonder
  melding.
- **Het bestand staat niet waar Python zoekt.** **Luid**:
  `open("namen.txt")` zoekt in de map van waaruit het programma draait, en
  vindt het daar niets, dan volgt
  `FileNotFoundError: [Errno 2] No such file or directory: 'namen.txt'`. Dat
  hoeft niet de map te zijn waarin het bestand met de code staat. Dit kom je
  morgen en overmorgen opnieuw tegen.

### Als het niet uitkomt

- **Blok 2 of 3 loopt uit.** Haal de tijd bij **blok 3** vandaan door alleen
  "een bit is 0 of 1, een byte is er acht" te zeggen en de RAM-afbeeldingen
  over te slaan. Bits en bytes zijn hier aanloop naar blok 4, geen onderwerp
  op zich.
- **Je komt niet aan blok 7 toe.** Laat het schrijven dan niet vallen, maar
  kort blok 6 in tot de uitvoer en de verklaring van de lege regels. Schrijven
  staat in de opstap (`## Bestanden schrijven`) en niet in het werkcollege; wie
  het hier niet ziet, ziet het pas in het practicum.
- **Je houdt tijd over.** Laat de klas na blok 7 voorspellen wat er gebeurt als
  je het leesvoorbeeld van blok 6 nog eens uitvoert: twee namen, elk gevolgd
  door een lege regel.

**Wat je niet inkort.** Blok 4, want het is de enige plek in de week waar
gezegd wordt dat het type bepaalt hoe je bits leest. En blok 5, om de reden
die bij het blokschema staat.

## 3. Bijeenkomst 2 - Werkcollege: fraaie plaatjes

Materiaal: `source/practicals/6b_images.ipynb`, met `fraaie_plaatjes.zip` uit
`source/problems/assets/`.

Dit is het werkcollege in de zin van `curriculum/uitgangspunten.md`: de plek
waar een probleem gezamenlijk stap voor stap wordt opgebouwd. De gegeven
functie `invert` heeft de vorm die alle opdrachten delen - een afbeelding
inlezen, een nieuwe lijst van rijen opbouwen, die wegschrijven - en het
materiaal zegt dat zelf: *"het is het gemakkelijkst om bij deze functies
dezelfde structuur te gebruiken"*. De bijeenkomst doet het daarom twee keer op
dezelfde manier: **samen de eerste, dan de rest zelf.**

### Blokschema

| # | Min | Wat er gebeurt | Materiaal, met de letterlijke kop | Werkvorm | Herkomst |
|---|---:|---|---|---|---|
| 1 | 10 | Aftrap: de zip uitpakken, Pillow controleren, `fraaie_plaatjes.py` draaien en `out.png` bekijken | `## Voorbereiding`, `## Onze PNG module`, `## Opdracht 1: Uitproberen` | docent doet voor, klas doet mee | R |
| 2 | 10 | De vorm van `im_pix`: een lijst van rijen, een rij van pixels, een pixel van drie getallen; en luminantie | `### Datastructuur`, `### Luminantie`, `### Spelen met pixels` | docent, raster op het bord | R |
| 3 | 20 | **Samen `greyscale`**: alleen wat er per pixel gebeurt, verandert | `` ## Opdracht 2: `greyscale()` `` | klassikaal, klas dicteert, docent typt | R |
| 4 | 10 | Zelf `binarize`: `greyscale` met een `if` erin | `` ## Opdracht 3: `binarize(thresh)` `` | zelfstandig, docent loopt rond | R |
| | | **Pauze** | | | |
| 5 | 15 | **Samen `flip_vert`**, eerst op papier: welke rij komt waar; daarna zelf `flip_horiz` | `## Geometrische transformaties`, `` ### Opdracht 4: `flip_vert()` ``, `` ### Opdracht 5: `flip_horiz()` `` | op papier, dan klassikaal, dan zelfstandig | R |
| 6 | 20 | Zelf `mirror_vert` en `mirror_horiz`, na een getekend raster van vier rijen | `` ### Opdracht 6: `mirror_vert()` ``, `` ### Opdracht 7: `mirror_horiz()` `` | op papier, dan zelfstandig | R |
| 7 | 5 | Afronden: `scale` en de vrije opdracht gaan mee naar het practicum | `` ### Opdracht 8: `scale()` ``, `### Opdracht 9 Meer transformaties` | docent | R |

Zeven blokken, 90 minuten, alle zeven richttijd. Voor deze bijeenkomst bestaat
geen bruikbare bron: zie *Over de tijden*.

### Hoe je het brengt

**Blok 1.** Laat iedereen de zip uitpakken en `fraaie_plaatjes.py` draaien
vanuit de map waar de bestanden staan. Het programma meldt de afmeting van
`in.png`, drukt de eerste twee pixels af en schrijft `out.png` weg:

```text
in.png bevat een afbeelding 42x16 PNG in RGB modus.
De eerste twee pixels van de eerste rij zijn [(255, 0, 0), (255, 0, 0)]
Bestand out.png opslaan...out.png opgeslagen.
```

Wie hier een `ModuleNotFoundError` krijgt, mist Pillow; zie *Als het niet
uitkomt*. Zeg erbij dat het materiaal `spam.png` "het bestand dat je gaat
bewerken" noemt, maar dat `invert` `in.png` leest: wie op `spam.png` wil
werken, verandert die bestandsnaam.

**Blok 2.** Teken het voorbeeld uit `### Datastructuur` op het bord, twee rijen
van drie pixels, en zet het naast het bord van vorige week. Een pixel op rij
`r` en kolom `c` is `im_pix[r][c]`, precies zoals `L[row][col]`; het enige
nieuwe is dat er op elke plek geen teken staat maar drie getallen. Loop dan de
twee lussen van `invert` langs - `for row in im_pix`, `for pixel in row` - en
wijs erop dat er een **nieuwe** rij en een **nieuwe** afbeelding worden
opgebouwd, en dat `im_pix` zelf niet verandert. Eindig bij `### Luminantie`:
21% rood, 72% groen, 7% blauw, samen precies 1.

**Blok 3.** Samen, jij typt, de klas dicteert. Neem `invert` over als
`greyscale` en vraag wat er moet veranderen. Het antwoord is: alleen wat er
per pixel gebeurt. Laat de klas de berekening dicteren - de luminantie van de
pixel, en dan die ene waarde drie keer als nieuwe pixel - en voer het uit op
`spam.png`. Blijf staan bij de `int()`: zonder die afronding loopt het
programma pas bij het wegschrijven vast, en dat is het eerste punt onder
*Waar het vastloopt*.

**Blok 4.** Zelfstandig. `binarize` is `greyscale` met een `if`: onder de
drempel zwart, anders wit. Loop rond en vraag bij elke oplossing wat er
gebeurt bij drempel 0 en bij drempel 255; het materiaal belooft een volledig
witte en een volledig zwarte afbeelding, en of dat klopt, hangt af van de
vraag aan welke kant van de vergelijking de gelijkheid valt.

**Blok 5.** Eerst op papier. Laat iedereen een raster van vier rijen tekenen,
de rijen genummerd 0 tot en met 3, en ernaast opschrijven waar elke rij terecht
moet komen als je de afbeelding op de horizontale as omdraait. Pas daarna
samen `flip_vert`: het materiaal geeft zelf de hint dat `lst[::-1]` een lijst
omdraait, en de rijen omdraaien is één regel. Laat `flip_horiz` dan zelf doen,
met dezelfde vraag op papier voor één rij. Het materiaal zegt erbij dat
`in.png` horizontaal gespiegeld niet verandert; laat de klas het controleren op
`spam.png`.

**Blok 6.** Zelfstandig, en weer eerst op papier: welke rijen blijven staan,
welke worden vervangen, en waardoor. `mirror_vert` vraagt de hoogte via
`get_wh()`; wie daar vastloopt, laat je het raster van blok 5 nog eens
bekijken. Het waarschuwingskader bij `` ### Opdracht 6: `mirror_vert()` `` gaat
over `list1 = list2`; zeg daar niet meer over dan dat slicen een nieuwe lijst
oplevert. Wat een verwijzing is en waarom dat ertoe doet, is de stof van week
7.

**Blok 7.** Zeg dat `scale` - elke tweede rij en daarin elke tweede pixel - en
de vrije `### Opdracht 9 Meer transformaties` morgen in het practicum een
plek hebben, en dat `source/problems/6_extra.ipynb` over dezelfde vraag gaat
van de andere kant: hoe maak je zo'n bestand kleiner.

### Waar het vastloopt

- **Luminantie zonder `int()`** (`` ## Opdracht 2: `greyscale()` ``). **Luid**,
  maar op de verkeerde plek: de fout
  `TypeError: 'float' object cannot be interpreted as an integer` komt pas uit
  `save_rgb` in `png.py`, niet uit de regel waar de berekening staat. Een
  witte pixel levert zonder afronding `254.99999999999997` op.
- **Percentages die samen meer dan 1 zijn**
  (`` ## Opdracht 2: `greyscale()` ``). **Stil**. Het materiaal belooft hier
  een `OverflowError`, maar met Pillow 12.3.0, de versie in de omgeving van
  deze repository, komt die niet: waarden boven 255 worden zonder melding op
  255 gezet, en de afbeelding wordt alleen te licht. Zeg dat de hint in het
  materiaal hier niet meer klopt.
- **Een pixel is geen lijst maar een tuple.** **Luid**: wie de pixel ter
  plekke wil aanpassen met `pixel[0] = ...`, krijgt
  `TypeError: 'tuple' object does not support item assignment`. Het materiaal
  schrijft "een lijst van drie integers", maar de uitvoer van blok 1 laat
  ronde haakjes zien. Dat is geen ramp: het dwingt precies af wat deze week de
  regel is, een nieuwe pixel maken in plaats van de oude veranderen.
- **`spam.png` heeft vier getallen per pixel.** **Luid**, en alleen op dat
  bestand: `spam.png` is RGBA, en `red, green, blue = pixel` geeft
  `ValueError: too many values to unpack (expected 3, got 4)`. Op `in.png` gaat
  het goed. Wie met `pixel[0]`, `pixel[1]` en `pixel[2]` werkt, merkt niets.
- **`binarize` met de gelijkheid aan de verkeerde kant**
  (`` ## Opdracht 3: `binarize(thresh)` ``). **Stil**: wie schrijft "wit als de
  luminantie groter is dan de drempel", krijgt bij drempel 0 op `spam.png`
  geen volledig witte afbeelding (89042 van de 93174 pixels wit), want zwarte
  pixels hebben luminantie 0. "Zwart als de luminantie kleiner is dan de
  drempel, anders wit" haalt beide beloften uit het materiaal.
- **`mirror_vert` bij een oneven hoogte**
  (`` ### Opdracht 6: `mirror_vert()` ``). **Stil**: `spam.png` is 293 rijen
  hoog, en de bovenste helft plus haar spiegelbeeld is 292 rijen. De
  afbeelding wordt één rij korter en niemand krijgt een melding.

### Als het niet uitkomt

- **Pillow ontbreekt bij een deel van de klas.** Laat hen `pip install Pillow`
  draaien, zoals `## Onze PNG module` zegt, en laat hen tot blok 3 meekijken
  bij een buur. Blok 3 is klassikaal, dus ze missen niets wat ze niet kunnen
  inhalen.
- **Blok 3 loopt uit.** Laat het lopen en haal de tijd bij **blok 4** vandaan:
  `binarize` is `greyscale` met een `if` en past in het practicum van morgen.
- **Je komt niet aan blok 6 toe.** Doe `flip_vert` nog samen in blok 5 en geef
  `flip_horiz`, `mirror_vert` en `mirror_horiz` mee naar het practicum. Laat
  wel de tekening op papier maken voordat ze weggaan; die maakt de spiegelingen
  morgen zonder docent te doen.
- **Je houdt tijd over.** Doe `scale` nog in de zaal, en laat de klas vooraf
  voorspellen hoe groot `in.png` wordt: van 42 bij 16 naar 21 bij 8.

**Wat je niet inkort.** Blok 3, het samen opbouwen van `greyscale`: dat is de
enige plek in de bijeenkomst waar de gedeelde vorm van alle opdrachten
gezamenlijk wordt neergezet, en het is de reden dat dit het werkcollege is. En
de stap op papier in blok 5.

## 4. Bijeenkomst 3 - Practicum: bestanden lezen en schrijven

Materiaal: de drie opgavebundels `source/problems/6_opstap.ipynb`,
`source/problems/6_basis.ipynb` en `source/problems/6_extra.ipynb`, met de
uitwerkingen `source/solutions/6_basis.ipynb` en
`source/solutions/6_extra.ipynb`.

Dit is zelfstandig werk onder begeleiding. Je legt weinig uit en loopt veel
rond. De opstap oefent lezen en schrijven in zeven kleine opdrachten, de basis
bouwt in zes stappen een programma dat een DNA-profiel herkent, en de extra
comprimeert een zwart-witafbeelding.

**Regel de bestanden vóór de bijeenkomst.** De opstap zegt *"In `assets/`
staan twee bestandjes"* en de basis *"De sequenties ... staan in
`assets/dna/`"*, maar geen van beide pagina's geeft een downloadlink. De enige
downloadlink van de week is de zip van het werkcollege. De twee bestanden van
de opstap staan wel op de pagina en zijn over te typen; de vier sequenties van
de basis staan nergens op de pagina.

### Blokschema

| # | Min | Wat er gebeurt | Materiaal, met de letterlijke kop | Werkvorm | Herkomst |
|---|---:|---|---|---|---|
| 1 | 10 | Aftrap: waar de bestanden vandaan komen en waar ze moeten staan, en wat de drie bundels van elkaar onderscheidt | `source/course/opgaven_6.md`, `### De gegevens` | docent | R |
| 2 | 25 | Zelfstandig: de opstap bij `## Bestanden lezen`, of de basis tot en met stap 3 | `## Bestanden lezen`, `` ## Stap 1: `strip_newline(line)` `` t/m `` ## Stap 3: `count_repeats(sequence, pattern, start)` `` | zelfstandig, docent loopt rond | R |
| | | **Pauze** | | | |
| 3 | 10 | Peilmoment, klassikaal: wat er aan het eind van een regel hangt | opstap `### Opdracht 7`, basis `` ## Stap 1: `strip_newline(line)` `` | klassikaal | R |
| 4 | 35 | Vrije ruimte: de basis afmaken, de extra, of wat van het werkcollege is blijven liggen | `` ## Stap 4: `longest_match(sequence, pattern)` `` t/m `` ## Stap 6: `identify(sequence, patterns, database)` ``, `## Beeldcompressie` | zelfstandig | R |
| 5 | 10 | Afronden: wat het programma níet zegt, en waar de database straks staat | `## Tot slot` | docent | R |

Vijf blokken, 90 minuten, alle vijf richttijd. Voor deze bijeenkomst bestaat
geen bruikbare bron: zie *Over de tijden*.

**Dit is een ritme en geen rooster.** Blok 2 en 4 zijn één doorlopend werkblok
met een peilmoment ertussen. Bij de overgang naar blok 4 zeg je hardop dat wie
nog in de opstap zit daar gewoon mag blijven - er hoeft niets af.

### Hoe je het brengt

**Blok 1.** Drie dingen, kort. Ten eerste de bestanden: zorg dat iedereen
`woorden.txt` en `metingen.txt`, en voor de basis de vier sequenties, in een
map `assets` naast zijn eigen bestand heeft, en het programma uit die map
draait. Het pad `"assets/dna/1.txt"` in de opgave gaat daarvan uit.

Ten tweede de drie bundels, en vooral dat ze **niet alle drie voor iedereen
zijn**. De basis is de zelftest; wie daar vastloopt gaat naar de opstap; wie er
doorheen vliegt gaat naar de extra. Dat staat ook zo op
`source/course/opgaven_6.md`. Zeg het expliciet, anders begint iedereen bij de
opstap.

Ten derde de basis in één zin: zes functies, en `### Wat je gaat maken` laat
de hele vorm in één tabel zien voordat de student begint. Wijs die tabel aan.

**Blok 2.** Rondlopen. Bij de opstap vraag je bij elke opdracht wat er in
`line` zit, en laat je `print(repr(line))` gebruiken zodra iemand het niet
weet; `### Opdracht 1` leert dat trucje zelf. Bij de basis vraag je bij
`count_repeats` waar `position` na elke ronde staat. Het is een `while`-lus,
en wie `position` niet ophoogt, heeft een programma dat niet stopt.

**Blok 3.** Het peilmoment, en het gaat over één teken. Zet `### Opdracht 7`
van de opstap op het scherm en vraag welke woorden in `lang.txt` komen als je
`len(line) > 4` schrijft zonder het regeleinde eraf te halen. Het antwoord is:
alle vijf, want `"peer\n"` en `"kiwi\n"` zijn vijf tekens lang. Zet daar
`` ## Stap 1: `strip_newline(line)` `` naast: dat is precies waarom de basis
daarmee begint. Het regeleinde uit het college is hier geen detail meer maar
de reden dat een antwoord fout is.

**Blok 4.** Rondlopen. Wie bij de basis vastloopt stuur je naar de opstap en
niet naar de uitwerking. Wie de basis af heeft mag naar de extra, en die is
bedoeld om níét af te komen; zie *Als het niet uitkomt* voor wat die student
van je nodig heeft. Wie in het werkcollege niet aan de spiegelingen en `scale`
toekwam, doet dat hier.

**Blok 5.** Gebruik `## Tot slot` van `source/problems/6_basis.ipynb`. Twee
dingen staan er, en beide zijn het zeggen waard. De database staat nu in de
code; in werkelijkheid staat hij in een bestand, en wie een rij dan bij naam
wil opvragen in plaats van met `row[1]`, heeft een dictionary nodig - dat is
PGM2. En het programma zegt dat een profiel overeenkomt, niet dat iemand
schuldig is. Laat die laatste alinea staan; het is de enige plek in de week
waar het materiaal zegt waar de grens van een uitkomst ligt.

### Waar het vastloopt

- **Het bestand is er niet, of Python zoekt op een andere plek.** **Luid**:
  `FileNotFoundError`. Dit wordt deze bijeenkomst de meest gestelde vraag,
  omdat de pagina's geen downloadlink geven. Vraag altijd eerst: waar staat het
  bestand, en vanuit welke map draai je?
- **`"w"` binnen de lus in `### Opdracht 7` van de opstap.** **Stil**: wie
  `lang.txt` voor elk woord opnieuw opent, houdt aan het eind alleen `mango`
  over. Het waarschuwingskader van de opgave zegt het, maar staat onder de
  opdracht.
- **`len(line)` met het regeleinde er nog aan** (`### Opdracht 7`). **Stil**:
  alle vijf woorden komen erdoor, ook `peer` en `kiwi`. Zie blok 3.
- **`### Opdracht 5` van de opstap zonder `int()`.** **Stil**, en onzichtbaar:
  strings vergelijken geeft hier toevallig hetzelfde antwoord, `226`, omdat
  alle getallen in `metingen.txt` drie cijfers hebben. Alleen de lege regel
  achter het antwoord verraadt dat er `"226\n"` is afgedrukt. Vraag erbij wat
  er gebeurt als er een dag met 1000 bezoekers bij komt.
- **`"Geen match"` binnen de lus in**
  `` ## Stap 6: `identify(sequence, patterns, database)` ``. **Luid** via de
  asserts, maar pas bij de tweede: sequentie 1 (Anouk, de eerste rij) en
  sequentie 4 (geen match) geven toevallig het goede antwoord, sequentie 2 en 3
  niet. De uitwerking legt uit waarom de regel ná de lus hoort.

### Als het niet uitkomt

- **De bestanden zijn niet op tijd verspreid.** De opstap kan door: de inhoud
  van `woorden.txt` en `metingen.txt` staat op de pagina en is in een paar
  minuten over te typen. De basis kan tot en met stap 1 door, en
  `count_repeats` in stap 3 werkt op gewone strings; `read_sequence` en alles
  daarna heeft de vier sequenties echt nodig.
- **Blok 2 loopt uit omdat de helft nog bij de opstap zit.** Prima. Haal de
  tijd bij **blok 4** vandaan en niet bij blok 3; het peilmoment is het enige
  moment waarop de hele zaal hetzelfde teken bekijkt.
- **Het werkcollege is blijven liggen.** Doe de spiegelingen hier, in blok 4,
  met de tekening op papier van gisteren erbij.
- **Iemand is na een halfuur met de basis klaar.** Stuur hem naar
  `source/problems/6_extra.ipynb` en laat hem eerst op papier de
  streepjesafbeelding beschrijven: vier runs van 16 worden
  `[["0", 16], ["1", 16], ["0", 16], ["1", 16]]`. De student hoeft geen
  getallen naar binair om te zetten; vraag daarna naar de lege invoer en de
  inverse-eigenschap.

**Wat je niet inkort.** Blok 3, het peilmoment. En blok 1, want zonder
bestanden op de goede plek begint niemand.

## 5. Wat je verder moet weten

### Eigenaardigheden in het materiaal

- **`source/practicals/6b_images.ipynb` noemt `invert` drie keer `convert`.**
  In de cel onder `### Datastructuur` en in het kader onder
  `### Spelen met pixels` staat *"de geneste lus in de functie `convert`"* en
  *"zoals in `convert`"*, maar de gegeven functie heet `invert`. Zeg het
  voordat iemand ernaar zoekt.
- **Het werkcollege beschrijft een pixel anders dan hij is.** Het materiaal
  zegt "een lijst van drie integers"; `get_rgb` geeft tuples, en bij
  `spam.png` vier getallen in plaats van drie. Zie *Waar het vastloopt* in
  sectie 3.
- **Er staan twee zinnen dubbel in het werkcollege.** Onder
  `## Opdracht 1: Uitproberen` staat *"Door dit te doen wordt de functie
  `invert()` uitgevoerd"* twee keer, en onder `` ## Opdracht 2: `greyscale()` ``
  staat de hint over `filename is not defined` twee keer. Daar staat ook de
  hint over een `OverflowError` die met Pillow 12.3.0 niet meer optreedt.
- **`` ### Opdracht 4: `flip_vert()` `` noemt een list comprehension** - *"de
  hulpfunctie aanroept in een list comprehension"* - terwijl er in de gegeven
  code geen staat. List comprehensions zijn PGM2-stof;
  `curriculum/leerlijn.md` noemt deze vindplaats al onder de
  vooruitverwijzingen. Leg ze niet uit; de opdracht is zonder te maken.
- **De opdrachten van het werkcollege staan op twee kopniveaus.**
  Opdracht 1 tot en met 3 zijn koppen van niveau `##`, Opdracht 4 tot en met 9
  van niveau `###`, onder `## Geometrische transformaties`, en
  `### Opdracht 9 Meer transformaties` mist de dubbele punt van de andere. En
  "Opdracht 1" wijst deze week naar twee plekken: het werkcollege en
  `### Opdracht 1` van de opstap. Noem het bestand erbij.
- **De opstap en de basis geven geen downloadlink** voor de bestanden die ze
  lezen; zie sectie 4. In de elf bestanden van de week staat één
  `{download}`, die van `fraaie_plaatjes.zip`.
- **De extra gebruikt run-length encoding.** `source/problems/6_extra.ipynb`
  beschrijft een run als een aaneengesloten blok gelijke tekens of pixels en een
  geldige invoer als een binaire string van maximaal 64 tekens en
  geeft de runs terug als tweeelementige lijsten `[pixel, aantal]`. De lege
  invoer is expliciet beschreven. Studenten hoeven geen getallen naar binair
  om te rekenen; de lijst is hier een compacte beschrijving van de pixels.
- **De uitwerking van de extra draait.** `source/solutions/6_extra.ipynb` bevat
  codecellen voor `compress` en `uncompress`, met assertions voor lege invoer,
  enkele en afwisselende runs, de maximale lengte en de inverse-eigenschap. De
  runs worden in hun oorspronkelijke volgorde teruggezet.
- **Buiten het boek staat een oude uitwerking van het werkcollege**,
  `solutions/6b_images.ipynb` in de hoofdmap van de repository, niet in
  `source/`. Haar `mirror_vert` loopt vast op `im_pix.get_wh()`
  (`AttributeError: 'list' object has no attribute 'get_wh'`). Gebruik de
  korte antwoorden hieronder.

### Korte antwoorden bij de collegeopdrachten

Het college, `source/lectures/6a_data.ipynb`, heeft geen enkele kop
*Opdracht*; daar is dus niets te beantwoorden. Het werkcollege heeft negen
opdrachten en **geen uitwerking in `source/solutions/`**, en omdat je
`greyscale` in bijeenkomst 2 samen met de klas opbouwt, staan de antwoorden
hier. Ze zijn voor jou, niet om uit te delen, en ze zijn **uitgevoerd op
`in.png` en `spam.png` en niet uitgerekend**. Elk antwoord zit in de vorm van
`invert`: dezelfde twee lussen, of een bewerking op de hele lijst van rijen.

| Opdracht | Antwoord |
|---|---|
| `` ## Opdracht 2: `greyscale()` `` | per pixel `lum = int(0.21 * p[0] + 0.72 * p[1] + 0.07 * p[2])` en als nieuwe pixel `[lum, lum, lum]` |
| `` ## Opdracht 3: `binarize(thresh)` `` | zelfde `lum`; `[0, 0, 0]` als `lum < thresh`, anders `[255, 255, 255]`. Drempel 0 geeft dan op beide afbeeldingen volledig wit, drempel 255 volledig zwart |
| `` ### Opdracht 4: `flip_vert()` `` | `new_pix = im_pix[::-1]` |
| `` ### Opdracht 5: `flip_horiz()` `` | elke rij omgedraaid, `row[::-1]`; op `in.png` is de uitkomst gelijk aan het origineel |
| `` ### Opdracht 6: `mirror_vert()` `` | `w, h = get_wh(im_pix)`, `top = im_pix[:h // 2]`, `new_pix = top + top[::-1]`; `spam.png` wordt 292 rijen in plaats van 293 |
| `` ### Opdracht 7: `mirror_horiz()` `` | per rij `left = row[:len(row) // 2]` en als nieuwe rij `left + left[::-1]` |
| `` ### Opdracht 8: `scale()` `` | elke rij uit `im_pix[::2]`, en daarvan `row[::2]`; `in.png` gaat van 42 bij 16 naar 21 bij 8 |

`## Opdracht 1: Uitproberen` vraagt alleen om het programma te draaien, en
`### Opdracht 9 Meer transformaties` is vrij; die hebben geen antwoord.

De opstap heeft ook geen uitwerking; die hoort bij #194. Een kort antwoord is
daar niet nodig, want elke opdracht geeft zijn verwachte uitvoer zelf, en die
klopt: `5` regels, totaal `1393`, drukste dag `226`, en `lang.txt` met
`appel`, `banaan` en `mango`.

### Wat er uit de handleidingen van 2023 niet is overgenomen

Er zijn twee Word-handleidingen voor week 6 geweest, en er is van geen van
beide een tijd overgenomen. Dat is geen oordeel over die documenten maar het
gevolg van twee verschuivingen: de stof van de ene is naar PGM2 verhuisd, die
van de andere is vervallen.

*Ceasar op orde* beschreef een les met tien minuten uitleg over de
Caesar-code en `rot13`, twee opdrachten om zelf te maken en te bespreken, vijf
minuten over lijsten van lijsten, en een derde opdracht waarin de klas een
versleutelde tekst kraakt door de meest voorkomende letter als `e` te nemen.
Die opgave staat nu in PGM2 week 3; zie *Over de tijden*. Wat overeind blijft
is de werkvorm van die derde opdracht, *"Probeer, plan, programmeer"*: eerst
bedenken hoe je het op papier oplost, dan pas programmeren. Die staat nu bij de
spiegelingen van het werkcollege en bij de extra van het practicum.

*Decimaal en verder* beschreef een les met tien minuten herhaling van binaire
getallen en zeven opdrachten: een test op oneven, getallen omrekenen naar
binair en terug, een binaire teller, en hetzelfde voor het drietallig stelsel,
alle recursief. Die rekenkunde is vervallen met het besluit §`### Schakelingen
en binair` in `curriculum/uitgangspunten.md`. De extra gebruikt nog wel binaire
strings als pixels, maar leert geen binaire omzetting: de run-lijst bevat gewone
decimale aantallen.

Beide documenten zijn met dit werkitem uit de repository verwijderd, volgens de
regel in `curriculum/uitgangspunten.md`
§`### Wat een docentenhandleiding is, en waar hij staat`. Wie ze wil nalezen,
vindt ze in de git-geschiedenis, bijvoorbeeld met
`git show 5d101066:teacher_guides/6a_Ceasar_op_orde.docx`.

### Wat er nog loopt

- **Er staan geen Word-handleidingen meer.** Met de twee van week 6 is de map
  `teacher_guides/` leeg en verdwenen, en daarmee is het laatste deel van #95
  voor PGM1 gedaan. De meldingen daarover in `handleidingen/week_3.md`,
  `week_4.md` en `week_5.md` zijn met dit werkitem bijgewerkt, net als
  *Reikwijdte* in `conventies/conventies.md`.
- **De extra is facultatief en gebruikt run-length encoding.** De uitwerking
  bevat uitvoerbare codecellen en tests; zie de eigenaardigheden hierboven.
- **De opstap en de basis hebben geen downloadlink** voor hun bestanden.
  Gemeld, niet gerepareerd.
- **De opstap van week 6 heeft nog geen uitwerking.** Dat staat in #194.
- **Het werkcollege heeft geen uitwerking in het boek.** Volgens
  `curriculum/uitgangspunten.md`
  §`### Elk opgaveniveau hoort een uitwerking te hebben` is dat bij een
  practicumbestand geen vastgesteld tekort; de korte antwoorden in deze
  handleiding vullen het voor de docent.
- **Deze week levert geen enkele overgeleverde tijd op.** Tot een docent haar
  geeft en de klok erbij houdt, staan alle negentien blokken als richttijd, en
  zo horen ze gelezen te worden.
- Deze handleiding beschrijft het materiaal zoals het op **23 september 2026**
  in de repository staat.

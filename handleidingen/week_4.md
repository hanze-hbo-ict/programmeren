# Docentenhandleiding PGM1 week 4

Deze week herhaalt code zichzelf. Week 3 gaf code een naam; deze week krijgt ze
een lus, en daarmee de vraag waar de rest van het vak op staat: wat verzamel je
terwijl je ergens langsloopt, en wanneer ben je klaar?

De lijn die de drie bijeenkomsten bij elkaar houdt is het lusrecept van vijf
vragen. Het wordt in het college voorgedaan, in het werkcollege drie keer samen
toegepast, en in het practicum gebruikt om te verklaren waarom een programma
niet stopt. Het is een vastgelegd besluit; zie `curriculum/uitgangspunten.md`
§`### Het lusrecept van week 4`.

De duurste fout van deze week gaat niet over herhalen maar over stoppen. Een
`for` stopt omdat de lijst opraakt; bij een `while` levert de schrijver het
stopmoment, en waar dat ontbreekt loopt het programma door zonder één
foutmelding. Dat is vraag 4 van het recept, en zij komt in alle drie de
bijeenkomsten terug.

## 1. De week in het kort

| Bijeenkomst | Vorm | Materiaal |
|---|---|---|
| 1 | College | `source/lectures/4a_lussen.ipynb` |
| 2 | Werkcollege | `source/practicals/4_python_bat.md` |
| 3 | Practicum | `source/lectures/4b_midterm.md` met `source/solutions/4_midterm.ipynb`, naast `source/problems/4_opstap.ipynb`, `source/problems/4_basis.ipynb` en `source/problems/4_extra.ipynb` |

Daarnaast staan er vier overzichtspagina's die je zelf niet hoeft te behandelen:
`source/course/week_4.md` (`## Lussen`) vat de week samen voor de student, en
`source/course/practical_4.md`, `source/course/opgaven_4.md` en
`source/course/solutions_4.md` zijn de omslagpagina's boven het werkcollege, de
opgaven en de uitwerkingen. De zes bestanden in `source/solutions/` staan in die
laatste; ze zijn openbaar voor de student en daarom geen materiaal dat je zelf
brengt. Dat weegt deze week zwaarder dan anders, want de oefenmidterm van
bijeenkomst 3 heeft zijn uitwerking openbaar staan. Dat is geen lek maar een
keuze, en het bepaalt hoe je die bijeenkomst inricht.

### Deze week valt de oefenmidterm naar de derde bijeenkomst

De indeling college - werkcollege - practicum uit
`curriculum/uitgangspunten.md` §`### Drie bijeenkomsten per week` gaat ervan uit
dat het werkcollege door een bestand uit `practicals/` wordt gevuld. Dat doet
week 4 ook: `source/practicals/4_python_bat.md` vult het werkcollege. Wat
afwijkt is het tweede collegebestand: `source/lectures/4b_midterm.md` schuift
naar de derde bijeenkomst, naast de drie opgavebundels.

Dat is een erkende afwijking, vastgelegd in `curriculum/uitgangspunten.md`
§`#### Vier erkende afwijkingen` en vastgesteld door de vakdeskundige op
**18 september 2026**. De grond is de midterm zelf: die wordt in week 5
afgenomen, dus is het practicum van week 4 het oefenmoment. Het materiaal wijst
dezelfde kant op: `source/practicals/4_python_bat.md` noemt zichzelf in zijn
eerste zin een werkcollege.

Wat de moedertabel wél bepaalt, en wat deze week gewoon geldt: de tweede
bijeenkomst is de plek waar een probleem **gezamenlijk stap voor stap wordt
opgebouwd**, en de derde is **zelfstandig werken onder begeleiding**. Die derde
bijeenkomst is dus twee dingen tegelijk - er wordt in de zaal gewerkt, en er
wordt meegenomen wat niet af komt. Dat is de reden dat de oefenmidterm daar niet
van voor naar achter wordt doorgelopen; zie het blokschema van sectie 4.

### Over de tijden

De blokschema's hieronder zijn ontworpen op wat deze week nodig heeft. De drie
Word-handleidingen van 2023 zijn daarna als controle ernaast gelegd en niet als
vertrekpunt gebruikt. Dat is de regel die in `curriculum/uitgangspunten.md`
§`### Wat een docentenhandleiding is, en waar hij staat` staat: zo'n document is
een bron om uit te putten, geen voorloper om te volgen. Wie ze wil nalezen
vindt ze in de git-geschiedenis.

**Elk blok draagt zijn herkomst.** In de kolom *Herkomst* betekent **B** dat het
blok op een blok uit de handleiding van 2023 steunt, en **R** dat het een
richttijd zonder bron is - een verdedigbare schatting, en niets meer dan dat.

| Bijeenkomst | Blokken | B: bron 2023 | R: richttijd zonder bron |
|---|---|---|---|
| 1 | 8 | 0 | 8 (90 min) |
| 2 | 7 | 0 | 7 (90 min) |
| 3 | 5 | 0 | 5 (90 min) |
| **samen** | **20** | **0** | **20** |

**Week 4 is de eerste week waarvan de handleiding geen enkele overgeleverde tijd
draagt, en de kolom B is dus leeg.** Die kolom staat er toch, zodat je kunt zien
dat er niets in staat in plaats van dat het vergeten is. De reden is meetbaar en
geen oordeel over de oude documenten: van de drie handleidingen van 2023 gingen
er twee volledig over recursie, en die stof ligt sinds het besluit
§`### Recursie na de lussen` in `curriculum/uitgangspunten.md` in week 9. De
derde beschreef een klassikale lesvorm voor de oefenmidterm - op papier, geen
overleg, daarna in duo's, daarna twintig minuten samen bespreken - en die vorm
heeft deze week niet meer, nu de oefenmidterm in het practicum ligt. Wat van die
bron overeind blijft is dus geen tijd maar een **werkvorm**: eerst zelf
voorspellen, dan pas de uitwerking openen. Die staat in *Hoe je het brengt* van
sectie 4, en een werkvorm draagt geen herkomstmerk.

Ter vergelijking: week 3 haalde 70 van zijn 270 minuten uit een bron en week 4
nul. Alle twintig blokken zijn schattingen op de omvang van het materiaal. Wie
deze week geeft en de klok erbij houdt, levert de eerste B-tijden op.

Alle drie de bijeenkomsten tellen op tot **90 minuten** met een ongetimede
pauze. **Hoe lang een bijeenkomst werkelijk duurt staat nergens in de
repository.** Duurt die van jou korter of langer, schaal de blokken dan mee.

### Wat je nodig hebt

- **Een scherm waarop je code kunt uitvoeren terwijl de klas kijkt.** Het college
  heeft negen cellen met code erin en een reeks quizvragen die zich lenen voor
  voorspellen-en-uitvoeren. Dat is deze week de werkvorm, en zonder scherm valt
  hij weg.
- **Een bord waarop een tabel past.** Bij de tweede quizvraag van het college
  staat de tabel al in het materiaal, met `result`, `string[ix - 1]`,
  `string[ix]` en `ix` naast elkaar. Die tabel is het gereedschap van de hele
  week: één regel per ronde.
- **CodingBat en een Python-omgeving, voor bijeenkomst 2.** De twaalf problemen
  staan op twee pagina's van één externe site, en de student zet zijn code
  daarna over naar een eigen bestand. Probeer de site vóór de bijeenkomst; hij
  draait zonder TLS en de hele bijeenkomst hangt eraan. In
  *Als het niet uitkomt* van sectie 3 staat wat je doet als hij eruit ligt.
- **Python Tutor in de browser, voor bijeenkomst 3.** Het peilmoment over de
  vier programma's die fout aflopen werkt het beste als de klas de toestand per
  ronde ziet bewegen. `source/problems/4_opstap.ipynb` verwijst studenten er zelf
  ook naar.
- **Papier.** Zowel de quiz van het college als de twintig leesopdrachten van de
  oefenmidterm beginnen met een voorspelling. Die is alleen iets waard als hij
  opgeschreven is voordat de cel wordt uitgevoerd.

## 2. Bijeenkomst 1 - College: lussen

Materiaal: `source/lectures/4a_lussen.ipynb`.

De dragende lijn is de opbouw van het notebook zelf: eerst de `for` als vorm,
dan de verzamelvariabele, dan de `while`, en pas daarna het recept dat de twee
onder één noemer brengt. Open met de vraag waar week 3 op uitkwam - je hebt een
functie met een naam, maar je moet nog steeds elke stap zelf opschrijven - en
zeg dat je aan het eind van deze bijeenkomst vijf vragen hebt waarmee je elke lus
van deze week kunt ontwerpen.

### Blokschema

| # | Min | Wat er gebeurt | Materiaal, met de letterlijke kop | Werkvorm | Herkomst |
|---|---:|---|---|---|---|
| 1 | 5 | Lesdoel en opfris: vorige week kreeg code een naam, deze week herhaalt ze zichzelf | `# Lussen`, `` ## `for` lussen `` | docent, eerste cel uitvoeren | R |
| 2 | 10 | `for` over een lijst en over `range`, en de verkorte toekenning | `## Iteratief ontwerp`, `### Variabelen`, `### In het kort` | voorspellen, dan uitvoeren | R |
| 3 | 15 | De vier stappen van een `for`, code ná de lus, en `fac` als eerste verzamelvariabele | `` ## `for`! ``, `### Stap voor stap`, `` ### Faculteit met `for` `` | bord plus cel uitvoeren | R |
| 4 | 10 | Quiz: twee voorspellingen, de tweede met de indextabel op het bord | `## Quiz` | individueel op papier, dan klassikaal | R |
| | | **Pauze** | | | |
| 5 | 10 | Element of index: wat de index toevoegt, en wanneer je hem niet nodig hebt | `` ## Twee typen `for` ``, `### Op basis van element`, `### Op basis van index`, `### Welke van de twee?` | docent, klas kiest | R |
| 6 | 10 | `while`: de conditie, de lus die niet stopt, en `break` en `continue` als naslag | `## Extreme lussen`, `` ## `while` lussen ``, `### Ontsnappen`, `` ## `continue` en `break` `` | voorspellen, dan uitvoeren | R |
| 7 | 15 | Begrensd tegenover onbegrensd, en het lusrecept twee keer voorgedaan | `## Denken in lussen`, `### Verschillen`, `## Het lusrecept`, `` ### Voorbeeld: `total(L)` ``, `` ### Voorbeeld: `power_of_two(limit)` `` | docent doet voor, klas beantwoordt vraag voor vraag | R |
| 8 | 15 | Opdracht 1 en 2 klassikaal lezen, Opdracht 3 in duo's schrijven, 4 en 5 mee naar huis | `## Opdracht 1` t/m `## Opdracht 5` | duo's, docent loopt rond | R |

Acht blokken, 90 minuten, alle acht richttijd. Voor het college van week 4
bestaat geen bron: de twee handleidingen van 2023 die erover hadden kunnen gaan
behandelen recursie, en die stof staat in week 9.

**Eén volgorde-eis die niet onderhandelbaar is.** Blok 7 blijft in deze
bijeenkomst, ook als de tijd knelt. Het lusrecept draagt de hele week: het
werkcollege van morgen loopt `double_char` er expliciet langs in
`source/practicals/4_python_bat.md`, en de uitwerking van opdracht 20 van de
oefenmidterm verwijst er in `source/solutions/4_midterm.ipynb` naar om uit te
leggen waarom die lus nooit eindigt. Zonder blok 7 mist bijeenkomst 2 en 3 hun
gemeenschappelijke taal.

### Hoe je het brengt

**Blok 1.** Voer de eerste cel uit - `for number in [0, 1, 2]` - en vraag niet
wat eruit komt maar hoeveel regels eruit komen. Drie, want er staan drie
elementen in de lijst. Zet daar meteen de tweede cel naast, met `range(0, 3)`,
en laat zien dat er precies hetzelfde uitkomt. Dat is het lesdoel in één
oogopslag: een lus loopt langs iets, en `range` is een manier om dat iets te
maken zonder het op te schrijven.

**Blok 2.** Twee dingen, en het tweede is een gewoonte en geen onderwerp. Eerst
`for` over een lijst tegenover `for` over een `range`; zeg hardop dat `range`
**tot** en niet tot en met telt, want dat is de meting die morgen en overmorgen
telkens terugkomt. Daarna de verkorte toekenning: `x += 1` is `x = x + 1`. Het
materiaal doet dat met drie voorbeelden onder `### In het kort`; loop ze snel
langs en blijf er niet hangen.

**Blok 3.** Het langste uitlegblok en het belangrijkste. Het materiaal knipt de
`for` in vier stappen, en de vierde is de stap die studenten overslaan: code ná
de lus wordt pas uitgevoerd als de lus klaar is. Zet dat op het bord met
`print("Done!")` eronder en vraag hoe vaak die regel wordt uitgevoerd. Het
antwoord is één keer, en dat is de reden dat `return result` bij `fac` buiten de
lus staat.

Voer daarna `fac(5)` uit. Er komt `120` uit. Loop de functie regel voor regel
langs met de tabel op het bord: `number` van 1 tot en met 5, en `result` dat
meegroeit. Wijs de startwaarde `result = 1` aan en vraag waarom die niet `0` is.
Dit is de eerste verzamelvariabele van het vak, en de term zelf valt hier.

**Blok 4.** De quiz, en dit is het blok waar de klas iets moet doen. Laat de
eerste vraag - `x += 10`, vier rondes - individueel op papier beantwoorden.
Vrijwel iedereen heeft `40` goed, en dat is de bedoeling: de vraag warmt op voor
de tweede.

De tweede vraag is een andere orde. `string[ix - 1] == " "` verzamelt de letters
die op een spatie volgen, en het antwoord is `'tttto'`. Laat de klas voorspellen
en vraag daarna hoeveel rondes de lus maakt: vijfentwintig, want de string is
vijfentwintig tekens lang. Zet de tabel uit het materiaal op het bord tot
`ix = 8` en laat de klas de volgende drie regels zelf invullen. Wat je wilt dat
ze meenemen is niet het antwoord maar de tabel.

**Blok 5.** Element of index, en dit is een keuze en geen regel. Zet de twee
vormen naast elkaar op het scherm, allebei met dezelfde uitvoer, en vraag welke
van de twee ze morgen nog willen lezen. Geef dan het tegenvoorbeeld dat het
materiaal zelf noemt: in de quizvraag van blok 4 kon je met `string[ix - 1]`
terugkijken naar de vorige positie, en dat kan een elementlus niet. De regel is
dus: elementen tenzij je de positie nodig hebt.

**Blok 6.** Begin met de extreme lus en voer hem **niet** uit. Laat de klas
lezen en zeggen wat er gebeurt: `guess` is 42, de conditie `guess == 42` klopt,
en in de body verandert niets aan `guess`. Vraag welke variabele de conditie zou
moeten veranderen; het antwoord is dat er geen is. Voer daarna de cel onder
`### Ontsnappen` wél uit, waar `random.choice` de conditie uiteindelijk onwaar
maakt.

`break` en `continue` zijn hier naslag en geen onderwerp. Twee zinnen volstaan,
maar de wóórden moeten vallen: `### Opdracht 13` en `### Opdracht 14` van
`source/problems/4_opstap.ipynb` laten de student ze allebei lezen, en dat is
morgen of overmorgen.

**Blok 7.** Hier komt de week bij elkaar. Zet de `for` en de `while` uit
`## Denken in lussen` naast elkaar en laat de klas het verschil benoemen: bij de
eerste ligt het aantal rondes vast voordat de lus begint, bij de tweede niet.
Gebruik de woorden **begrensd** en **onbegrensd**, en zeg erbij dat een `while`
niet oneindig is - het aantal herhalingen ligt alleen niet vooraf vast.

Doe daarna het recept twee keer voor, vraag voor vraag, en laat de klas
antwoorden. Bij `total(L)` zijn alle vijf de antwoorden makkelijk; dat is het
punt, want je wilt dat de vorm blijft hangen. Bij `power_of_two(limit)` doet
vraag 4 het werk: deze lus stopt omdat `result` elke stap verdubbelt en `limit`
dus een keer passeert. Haal die vermenigvuldiging weg, vraag wat er gebeurt, en
zeg dat dat geen eigenschap van `while` is maar een fout in stap 3.

**Blok 8.** Lees Opdracht 1 klassikaal, maar alleen **a** en **b**. Die twee
verschillen in één inspringing en lopen totaal anders af. Laat de klas allebei
voorspellen voordat je de cellen uitvoert, en vooral **b**: vrijwel iedereen
verwacht daar iets. De uitwerking staat in `source/solutions/4a_lussen.ipynb`
onder `### a.` en `### b.`. Opdracht 2 lees je er snel achteraan.

Opdracht 3 is het schrijfwerk: `factors(n)`, in duo's, en met de vijf vragen
eerst. De lege cel eronder heeft de vijf vragen al als commentaar staan, dus
wijs daarop en loop rond. Wat je vraagt terwijl ze typen is niet "werkt het" maar
"wat is je verzamelvariabele en wanneer is hij klaar". Opdracht 4 en 5 gaan mee
naar huis.

### Waar het vastloopt

- **`return` helemaal links, buiten de functie** (Opdracht 1 **d**). Dit loopt
  **luid** af met een `SyntaxError`, en het bijzondere is dat Python niet eens
  aan uitvoeren toekomt: hij leest eerst het hele bestand. Dat is een andere
  soort fout dan **a**, **b** en **c**, en `source/solutions/4a_lussen.ipynb`
  zegt dat ook met zoveel woorden onder `### d.`.
- **`return` in de body van de lus** (Opdracht 1 **b**). Dit loopt **stil** af,
  en het is het stilste geval van de week: er komt niets uit. Een cel zonder
  uitvoer ziet eruit als een cel die niet is uitgevoerd. De uitwerking
  waarschuwt daar expliciet voor onder `### b.`; zeg het hardop voordat de klas
  het zelf concludeert.
- **De `while` waarvan de conditie nooit verandert** (`## Extreme lussen`).
  **Stil**: geen foutmelding, geen uitkomst, alleen een cel die blijft draaien.
  Laat de klas aanwijzen wélke variabele de conditie zou moeten veranderen; het
  antwoord is dat er geen is, en dat is vraag 3 van het recept die niet
  beantwoord is.

### Als het niet uitkomt

- **Blok 7 loopt uit.** Laat het lopen. Haal de tijd bij **blok 2** vandaan door
  `### In het kort` als leeswerk mee te geven: `+=`, `-=` en `*=` komen elders in
  de week vanzelf terug - `*=` bij `fac` in blok 3, `+=` bij `### Opdracht 6` en
  `-=` bij `### Opdracht 15` van `source/problems/4_opstap.ipynb` - en `/=` komt
  in heel week 4 nergens anders voor. Dat is vijf minuten.
- **Je komt niet aan blok 8 toe.** Geef Opdracht 1 tot en met 5 mee en begin
  morgen niet met bespreken. Haal in dat geval geen tijd bij blok 7 weg: het
  werkcollege van morgen begint met het recept en niet met deze opdrachten.
- **Blok 4 loopt uit op de tweede quizvraag.** Zet de tabel op het bord tot
  `ix = 8` en zeg dat de rest op de pagina staat, met het antwoord erbij. Wil je
  toch verder, haal de tijd dan bij **blok 5** door `### Welke van de twee?` tot
  één zin terug te brengen.
- **Je houdt tijd over.** Laat duo's bij Opdracht 3 ook `factors(0)` proberen. Er
  komt een lege lijst uit, want `range(1, 1)` is leeg, en dat gesprek gaat over
  vraag 4 van het recept.

**Wat je niet inkort.** Blok 7, om de reden die hierboven bij het blokschema
staat. En de twee woorden `break` en `continue` in blok 6: de uitleg eromheen
mag tot twee zinnen, maar de woorden moeten vallen.

## 3. Bijeenkomst 2 - Werkcollege: lussen schrijven in CodingBat

Materiaal: `source/practicals/4_python_bat.md`, en de twaalf uitwerkingen in
`source/solutions/4_python_bat.ipynb`.

Dit is het werkcollege in de zin van `curriculum/uitgangspunten.md`: de plek
waar een probleem gezamenlijk stap voor stap wordt opgebouwd. Deze bijeenkomst
doet dat drie keer, en elke keer met dezelfde beweging: **samen er één
opbouwen, daarna de rest van die groep zelf.** Elk gezamenlijk probleem gaat
over één vraag van het lusrecept, zodat het college van gisteren het werkcollege
van vandaag draagt.

De twaalf problemen vallen uiteen in vier groepen, en die groepen zijn af te
lezen aan de uitwerkingen en niet bedacht:

| Groep | Welke vraag van het recept hij moeilijk maakt | Problemen |
|---|---|---|
| A | geen; één verzamelvariabele, elementlus | `count_evens`, `double_char` |
| B | vraag 1 - de startwaarde komt uit de lijst | `big_diff`, `centered_average` |
| C | vraag 3 - naast de verzamelvariabele loopt een vlag mee | `sum13`, `sum67`, `has22`, `count_hi` |
| D | vraag 2 - je moet langs de indices, want je kijkt naar een buurpositie | `cat_dog`, `count_code`, `end_other`, `xyz_there` |

### Blokschema

| # | Min | Wat er gebeurt | Materiaal, met de letterlijke kop | Werkvorm | Herkomst |
|---|---:|---|---|---|---|
| 1 | 10 | Aftrap: `double_char` langs de vijf vragen - het materiaal doet hem zelf voor - en `count_evens` erachteraan als de kale vorm. En wat een groen vinkje wél en niet zegt | `# Lussen in PythonBat`, `## Opdracht` | docent doet voor | R |
| 2 | 15 | **Samen `big_diff` opbouwen**: vraag 1 van het recept. De startwaarde komt uit de lijst en niet uit het niets | List-2, en `# Lussen in PythonBat` | klassikaal, klas dicteert, docent typt | R |
| 3 | 10 | Zelf `centered_average`: dezelfde twee startwaarden, met een aftrekstap erachter | List-2 | zelfstandig, docent loopt rond | R |
| | | **Pauze** | | | |
| 4 | 15 | **Samen `sum13` opbouwen**: vraag 3 van het recept. Naast de verzamelvariabele loopt een vlag mee, en die moet ook weer terugvallen | List-2 | klassikaal | R |
| 5 | 10 | Zelf `sum67`, `has22` en `count_hi`: alle drie dezelfde vlag, drie keer anders | List-2 en String-2 | zelfstandig | R |
| 6 | 15 | **Samen `xyz_there` opbouwen**: vraag 2 van het recept. Waarom hier een index móét en een elementlus niet kan | String-2 | klassikaal | R |
| 7 | 15 | Zelf `cat_dog`, `count_code` en `end_other`, en je code bewaren in een `.py` | String-2, en `## Opdracht` stap 2 | zelfstandig | R |

Zeven blokken, 90 minuten, alle zeven richttijd. Voor deze bijeenkomst bestaat
geen bron: het materiaal en zijn uitwerking zijn na 2023 geschreven, en geen van
de drie handleidingen van dat jaar gaat over CodingBat.

**Waarom de drie gezamenlijke blokken even lang zijn.** Ze duren alle drie
vijftien minuten omdat ze alle drie hetzelfde doen: één probleem van nul af
opbouwen, met de klas die dicteert. De zelfstandige blokken lopen juist op, van
tien naar vijftien, want de eerste groep is één probleem en de laatste drie zijn
de zwaarste van de twaalf. De twaalf hoeven niet af: stap 1 van `## Opdracht`
loopt thuis door.

### Hoe je het brengt

**Blok 1.** Open `source/practicals/4_python_bat.md` en laat zien dat het
materiaal `double_char` al helemaal voordoet, inclusief de vijf vragen van het
recept eronder. Lees die vijf hardop mee: verzamelvariabele `result` begint op
de lege string, je loopt langs de tekens, er komt per stap `char * 2` bij, je
bent klaar als de string op is, en `return result` staat na de lus. Zet daar
`count_evens` naast - dezelfde vorm met een getal in plaats van een string - en
zeg dat dit de kale vorm is waar de rest van de middag varianten op zijn.

Zeg in dit blok ook wat een groen vinkje op CodingBat betekent. Het betekent dat
de voorbeelden slagen. Het betekent niet dat de student kan uitleggen wat zijn
lus verzamelt, en dat laatste is waar jij vanmiddag naar vraagt.

**Blok 2.** `big_diff`, samen, en jij typt. Laat de klas beginnen bij vraag 1:
wat verzamel je? Er komt meestal "het verschil" uit, en dat is nog niet genoeg -
je verzamelt twee dingen, de grootste en de kleinste tot nu toe. Stel dan de
vraag waar dit blok om draait: wat is de startwaarde? Wie `0` zegt krijgt bij
`big_diff([10, 3, 5, 6])` een verkeerd antwoord op de kleinste. De startwaarde
moet uit de lijst zelf komen, `nums[0]`, en dat is de eerste keer deze week dat
vraag 1 een echt antwoord vraagt.

**Blok 3.** `centered_average`, zelfstandig. Het is `big_diff` met een
aftrekstap erachter: dezelfde twee startwaarden uit de lijst, plus een gewone
som, en aan het eind gaan de grootste en de kleinste eraf. Loop rond en vraag
naar de startwaarden. Wie daar `0` heeft staan, heeft blok 2 niet meegenomen.

**Blok 4.** `sum13`, samen. De vlag is nieuw en hij is lastiger dan hij eruit
ziet. Bouw hem stap voor stap op: een verzamelvariabele `result` op `0`, en
daarnaast een `skip` die begint op `False`. Kom je een 13 tegen, dan gaat `skip`
aan; is `skip` aan, dan tel je niet op **en gaat hij weer uit**. Dat laatste is
waar de klas op struikelt, dus laat het ze voordoen op `[1, 2, 2, 1, 13]` en op
`[13, 1, 13]`.

**Blok 5.** `sum67`, `has22` en `count_hi`, zelfstandig. Alle drie dezelfde vlag,
drie keer anders gebruikt: bij `sum67` gaat hij pas uit bij een 7, bij `has22`
geeft de functie meteen `True` terug zodra hij voor de tweede keer aan zou gaan,
en bij `count_hi` telt hij mee bij een `i` die op een `h` volgt. Zeg erbij dat
`count_hi` op de andere CodingBat-pagina staat.

**Blok 6.** `xyz_there`, samen, en dit is het blok waar de bijeenkomst om
draait. Begin met de vraag waarom je hier niet met `for char in string` weg
komt: je moet naar drie tekens naast elkaar kijken, en een elementlus geeft je
er één. Dus een index, dus `range`. Schrijf dan de conditie op het bord, en
loop aan het eind van de string vast: `string[ix + 2]` bestaat niet meer als
`ix` de laatste positie is. De uitwerking lost dat op met
`range(0, len(string) - 2)`, en dat is de prijs van vraag 2 van het recept.

**Blok 7.** `cat_dog`, `count_code` en `end_other`, zelfstandig, en dan stap 2
van `## Opdracht`: de code overzetten naar een `.py`-bestand. Dat is de enige
plek in de week waar de student zijn eigen werk uit de browser haalt en
bewaart; neem er de laatste vijf minuten voor en controleer dat iedereen het
gedaan heeft.

### Waar het vastloopt

- **Groen bij CodingBat als bewijs dat het af is.** **Stil**: de site
  controleert de uitkomst op de voorbeelden, niet de strategie. Wie
  `count_code` met wat schuiven aan indices bij elkaar raadt, krijgt hetzelfde
  vinkje als wie het recept heeft gevolgd. Vraag bij het rondlopen
  niet "werkt het" maar "wat is je verzamelvariabele en wanneer is hij klaar".
- **`string[ix + 2]` zonder te kijken of die positie bestaat.** **Luid**, met
  een `IndexError`, en het is de prijs van vraag 2 van het recept: wie langs de
  indices loopt om naar de buurpositie te kijken, loopt aan het eind de lijst
  uit. Drie van de twaalf uitwerkingen hebben er een expliciete grens voor
  nodig - `cat_dog` met `if x + 2 < len(string)`, `count_code` met
  `if x + 3 < len(string)` en `xyz_there` met `range(0, len(string) - 2)`. Dat
  valt in blok 6 en 7, en het is de reden dat `xyz_there` het gezamenlijke
  probleem is.

### Als het niet uitkomt

- **Blok 2 loopt uit omdat de klas de twee startwaarden niet meteen ziet.** Laat
  het lopen. Haal de tijd bij **blok 3** vandaan door `centered_average` mee te
  geven: het is dezelfde twee startwaarden met een aftrekstap erachter, en
  CodingBat controleert hem thuis net zo goed als hier.
- **De groep loopt vast op de vlag in blok 4.** Haal de tijd bij **blok 5**
  vandaan - `sum67`, `has22` en `count_hi` zijn alle drie diezelfde vlag, dus
  wie blok 4 heeft begrepen kan ze thuis - en niet bij blok 6.
- **CodingBat is onbereikbaar.** De hele bijeenkomst hangt aan één externe site,
  zonder TLS. Houd blok 2, 4 en 6 overeind, want die gaan over de vorm van de
  lus en niet over de site, en haal de tijd voor de zelfstandige blokken uit
  `source/problems/4_basis.ipynb`: `### Opdracht 1` **b** (`power`) en
  `### Opdracht 2` **b** (`summed_odds`) zijn dezelfde elementlus met een `if`
  en draaien lokaal met assertions. Meld het aan wie morgen het practicum geeft,
  want die twee zijn dan al gezien.
- **Je houdt tijd over.** Laat duo's `end_other` een tweede keer schrijven met
  een index die vanaf achteren telt in plaats van met `[::-1]`. Dezelfde stof
  van de andere kant, en het kost je geen voorbereiding.

**Wat je niet inkort.** Blok 6. Dat is de enige plek in de hele week waar samen
wordt uitgelegd waarom een index nodig is, het is de reden dat deze bijeenkomst
het werkcollege is, en het is de enige les die de `IndexError` hierboven vóór
is. Kort liever blok 5 in tot `sum67` alleen.

## 4. Bijeenkomst 3 - Practicum: de oefenmidterm en de opgaven

Materiaal: `source/lectures/4b_midterm.md` met
`source/solutions/4_midterm.ipynb`, en de drie opgavebundels
`source/problems/4_opstap.ipynb`, `source/problems/4_basis.ipynb` en
`source/problems/4_extra.ipynb`.

Dit is zelfstandig werk onder begeleiding, en het is tegelijk materiaal om thuis
aan door te werken. Die tweede helft bepaalt wat je in de zaal doet en wat niet.

**De oefenmidterm wordt hier niet van voor naar achter doorgelopen.** De eigen
*Toetst:*-regels in `source/solutions/4_midterm.ipynb` splitsen de twintig
vragen in drie groepen: `## Opdracht 1` tot en met `## Opdracht 7` toetsen
types, `/`, `if`/`elif` en slices, en dat is stof van week 2; `## Opdracht 8`
tot en met `## Opdracht 12` toetsen functies, `return` en `None`, en dat is week
3; `## Opdracht 13` tot en met `## Opdracht 20` toetsen lussen, en dat is deze
week. Alleen die laatste groep vraagt een docent in de zaal. De eerste twaalf
zijn opfris met een openbare uitwerking, en dat is precies het werk dat thuis
doorloopt.

### Blokschema

| # | Min | Wat er gebeurt | Materiaal, met de letterlijke kop | Werkvorm | Herkomst |
|---|---:|---|---|---|---|
| 1 | 10 | Aftrap: wat de oefenmidterm is en hoe je hem gebruikt; dat de uitwerkingen openbaar zijn en waarom je ze pas ná je eigen voorspelling opent; en wat de drie bundels van elkaar onderscheidt | `# Oefenmidterm`, `source/course/opgaven_4.md` | docent | R |
| 2 | 25 | Opdracht 13 tot en met 20 zelfstandig: eerst de toestand per ronde op papier, dan pas de uitwerking erbij | `## Opdracht 13` t/m `## Opdracht 20`, `source/solutions/4_midterm.ipynb` | zelfstandig, docent loopt rond | R |
| | | **Pauze** | | | |
| 3 | 15 | Peilmoment, klassikaal: de vier programma's die fout aflopen, en waarom "Het programma werkt niet" een echt antwoord is | `# Uitwerkingen oefenmidterm` | klassikaal, Python Tutor | R |
| 4 | 30 | Vrije ruimte: opstap, basis of extra, ieder op zijn eigen niveau; wie de oefenmidterm wil afmaken doet 1 tot en met 12 | `source/problems/4_opstap.ipynb`, `source/problems/4_basis.ipynb`, `source/problems/4_extra.ipynb` | zelfstandig | R |
| 5 | 10 | Afronden: wat je mee naar huis neemt, waar de uitwerkingen staan, en de vooruitblik naar week 5 | `` ## De functie `while_pi(accuracy)` `` | docent | R |

Vijf blokken, 90 minuten, alle vijf richttijd. De handleiding van 2023 voor de
oefenmidterm beschreef een klassikale cyclus van 45 minuten waarin de hele groep
in de pas liep; onder deze vorm meet die cyclus niet meer hetzelfde en staat er
daarom geen minuut van in de tabel. De reden staat in *Over de tijden*.

**Dit is een ritme en geen rooster.** Blok 2 en 4 zijn één doorlopend werkblok
met een peilmoment ertussen. Bij de overgang naar blok 4 zeg je hardop dat wie
nog in de oefenmidterm zit daar gewoon mag blijven zitten - er hoeft niets af.

### Hoe je het brengt

**Blok 1.** Drie dingen, kort. Ten eerste wat de oefenmidterm is: twintig
leesopdrachten, meerkeuze, en in week 5 komt de echte. Ten tweede de werkvorm,
en die is de enige die deze week uit 2023 overeind blijft: **eerst zelf
voorspellen en opschrijven, dan pas de uitwerking openen.** De uitwerkingen
staan openbaar in `source/solutions/4_midterm.ipynb` en dat is met opzet - ze
zijn er om je voorspelling tegenaan te leggen, niet om hem te vervangen. Zeg dat
in zoveel woorden, want wie het niet hoort leest de sleutel en denkt dat hij het
begrepen heeft.

Ten derde de drie bundels, en vooral dat ze **niet alle drie voor iedereen
zijn**. De basis is de zelftest; wie daar vastloopt gaat naar de opstap; wie er
doorheen vliegt gaat naar de extra. Dat staat ook zo op
`source/course/opgaven_4.md`. Zeg het expliciet, anders begint iedereen bij de
opstap.

**Blok 2.** Opdracht 13 tot en met 20, zelfstandig, en verder niets van jou.
Loop rond en vraag bij elke vraag hetzelfde: laat je tabel zien. Eén regel per
ronde, met de variabelen die veranderen erin. Bij `## Opdracht 15` lopen `x` en
`n` samen op, en wie dat in zijn hoofd doet kiest een van de buuropties. Dat is
de gewoonte die deze bijeenkomst moet opleveren, en ze is alleen af te dwingen
terwijl ze bezig zijn.

**Blok 3.** Het peilmoment, klassikaal, en het gaat over precies vier vragen.
Het `important`-kader boven aan de uitwerkingen noemt ze bij naam: `## Opdracht
8` loopt op een `NameError`, `## Opdracht 14` op een `IndentationError`,
`## Opdracht 18` op een `ZeroDivisionError`, en `## Opdracht 20` eindigt nooit.
Bij alle vier is "Het programma werkt niet" het goede antwoord.

Doe `## Opdracht 18` met Python Tutor op het scherm en klik één ronde. De
student kijkt naar de lijst aan het eind en ziet niet dat `range(0, 48)` bij nul
begint; met de eerste ronde zichtbaar ziet hij het wel. Zeg daarna dat
voorspellen wat code doet ook voorspellen is wanneer ze stukloopt. Dat is
vastgelegd beleid en geen mening van deze handleiding; zie
`curriculum/uitgangspunten.md` §`### Leesvragen mogen fout aflopen`.

**Blok 4.** Rondlopen. Wie bij de basis vastloopt stuur je naar de opstap en niet
naar de uitwerking. Wie klaar is met de basis mag naar de extra, en die is
bedoeld om níét af te komen. Wie de oefenmidterm wil afmaken doet
`## Opdracht 1` tot en met `## Opdracht 12`; die zijn korter dan ze eruitzien.

**Blok 5.** Tien minuten, en dit blok is de helft van waarvoor deze bijeenkomst
is vastgesteld. Zeg wat er thuis te doen is: de eerste twaalf vragen van de
oefenmidterm, de bundels die niet af zijn, en waar de uitwerkingen staan. Sluit
af met `` ## De functie `while_pi(accuracy)` `` uit
`source/problems/4_extra.ipynb` als vooruitblik: een lus die gooit tot de
schatting goed genoeg is, met een stopmoment dat de schrijver zelf levert. Zeg
dat volgende week de midterm is en dat lussen daarna in elkaar komen te staan.

### Waar het vastloopt

- **`/` levert altijd een floating-point getal.** **Stil**, en drie keer dezelfde
  oorzaak: wie `## Opdracht 1`, `## Opdracht 2` en `## Opdracht 17` op papier
  narekent komt uit op iets als 3.7, 1 en 7, terwijl Python
  `3.6999999999999997`, `1.0` en `7.0` afdrukt. Die papieren antwoorden staan
  bij geen van de drie in de opties, en dat is precies het signaal: er is
  ergens gedeeld. De uitwerking legt bij alle drie uit waar de float vandaan
  komt.
- **De foutmelding is het antwoord, en hij komt uit een hoek die de student niet
  verwacht** (`## Opdracht 8` en `## Opdracht 18`). **Luid**, maar dat helpt
  hier niet. Bij 8 staat de aanroep boven de definitie en de student ziet de
  functie wél staan - hij leest het bestand als geheel en Python van boven naar
  beneden. Bij 18 begint `range(0, 48)` bij nul en klapt de eerste ronde eruit,
  terwijl de student naar de lijst aan het eind kijkt.
- **De "reparatie" van `## Opdracht 14`.** De fout is **luid**, een
  `IndentationError`, maar de valkuil is de reparatie: zet die ene inspringing
  erbij en het programma drukt `128` af - en dat is optie **d**. Een
  goedbedoelde herstelpoging levert dus een fout antwoord.
  `curriculum/uitgangspunten.md` §`### Leesvragen mogen fout aflopen` noemt deze
  opdracht bij name en zegt: blijf ervan af. Zeg dat in de zaal ook.
- **`## Opdracht 20` eindigt nooit.** **Stil**: `x` doorloopt 1, 4, 2.0, 1.0,
  4.0 en dan weer 2.0. Wie drie rondes narekent ziet een groeiende lijst en
  kiest er een; dat het rondgaat zie je pas bij de vijfde waarde. Hier heeft
  vraag 4 van het recept geen antwoord, en dat is precies wat de uitwerking
  erover zegt.
- **`until_a_repeat` in `source/problems/4_basis.ipynb` `### Opdracht 3`.** Dit
  is geen fout maar een **blokkade**: de student weet niet waar hij begint. Het
  materiaal geeft `unique(L)` cadeau en twee tips, maar die staan ónder de
  opdrachttekst en worden overgelezen. Wijs erop in plaats van de oplossing te
  geven.

### Als het niet uitkomt

- **Blok 2 loopt uit.** Laat het lopen tot ongeveer 35 minuten en haal de tijd
  bij **blok 4** vandaan. De bundels zijn thuis te maken en hun uitwerkingen
  staan openbaar in `source/solutions/`; de oefenmidterm met een docent in de
  zaal is precies het oefenmoment waarvoor deze bijeenkomst is vastgesteld.
- **Je komt niet aan blok 3 toe.** Kort dan blok 2 in tot `## Opdracht 13` tot
  en met `## Opdracht 18` en geef 19 en 20 mee - niet omgekeerd. De vier
  programma's die fout aflopen zijn het enige deel dat een student niet uit de
  openbare uitwerking haalt zonder het misverstand eerst gehad te hebben.
- **De helft komt niet aan de bundels toe.** Prima. Dit is vrije ruimte en er
  hoeft niets af. Wat je wel doet is in blok 5 zeggen waar de uitwerkingen staan
  en dat `## Opdracht 1` tot en met `## Opdracht 12` opfris van week 2 en 3 is
  die zich goed thuis laat maken.
- **Blok 6 en 7 van gisteren zijn blijven liggen.** Doe `xyz_there` hier, vóór
  blok 1, en haal de tijd bij **blok 4** vandaan. Samen een index opbouwen is
  niet thuis te doen; de drie zelfstandige problemen en de bundels wel.
- **Iemand is na een halfuur klaar.** Stuur hem naar
  `` ## De functie `while_pi(accuracy)` `` in `source/problems/4_extra.ipynb`:
  een onbegrensde lus waarvan hij het stopmoment zelf levert. Laat hem het
  voorbeeld in het materiaal nakijken, waar `while_pi(0.1)` na negen worpen `9`
  teruggeeft - een schatting kan de nauwkeurigheid per toeval halen.

**Wat je niet inkort.** Blok 3, het peilmoment. En blok 5, de tien minuten
waarin je zegt wat er thuis te doen is: dat is de helft van waarvoor deze
bijeenkomst is vastgesteld, en het is het deel dat als eerste sneuvelt als je
het niet inroostert.

## 5. Wat je verder moet weten

### Eigenaardigheden in het materiaal

- **De koppen van `source/lectures/4a_lussen.ipynb` dragen backticks.** Het is
  `` ## `for` lussen ``, met backticks om het sleutelwoord, en zo ook
  `` ## `for`! ``, `` ## Twee typen `for` `` en `` ## `while` lussen ``. Dat is
  correct, maar een verwijzing die de backticks weglaat wijst nergens heen. In
  `source/problems/4_opstap.ipynb` staat er bovendien een streepje in:
  `` ## `for`-lussen `` en `` ## `while`-lussen ``. Kopieer zo'n kop, typ hem
  niet over.
- **"Opdracht 1" wijst deze week naar acht plekken.** Een kop *Opdracht 1* staat
  in `source/lectures/4a_lussen.ipynb`, `source/lectures/4b_midterm.md`,
  `source/problems/4_opstap.ipynb`, `source/problems/4_basis.ipynb` en in de
  vier bijbehorende bestanden onder `source/solutions/`. Noem dus altijd het
  bestand of de bijeenkomst erbij.
- **Opgave en uitwerking staan een kopniveau uit elkaar.**
  `source/problems/4_basis.ipynb` schrijft `### Opdracht 1`,
  `source/solutions/4_basis.ipynb` schrijft `## Opdracht 1`. Dezelfde namen,
  ander niveau; in de klas hoor je dat verschil niet.
- **`source/practicals/4_python_bat.md` heeft één ongenummerde `## Opdracht`
  met drie stappen.** "Opdracht 2 van het werkcollege" bestaat dus niet. Verwijs
  naar de stappen - "stap 2, je code bewaren" - of naar het CodingBat-probleem
  bij naam.
- **`### Opdracht 4` van `source/problems/4_opstap.ipynb` geeft 9 bij beide
  lezingen.** Er staat `result + lst[1]`, en over `[5, 3, 1]` levert dat drie
  keer een 3 op: 9. Wie het als `lst[ix]` leest, telt 5 + 3 + 1 op en komt ook
  op 9. De student kan aan het antwoord dus niet zien of hij goed gelezen heeft.
  Vraag erbij welke waarde er per ronde wordt opgeteld.
- **Het lusrecept staat in twee formuleringen in het college.** Onder
  `## Het lusrecept` luidt vraag 2 *"Wat loop je langs?"*; bij `## Opdracht 3`
  en `## Opdracht 5` staat *"Waar loop je langs?"*. Het besluit in
  `curriculum/uitgangspunten.md` schrijft *Wat*, en deze handleiding volgt dat.
- **`source/solutions/4_python_bat.ipynb` wijkt af van de codeconventies.** Er
  staan drie namen in camelCase - `totalSum` (5×), `hFound` (5×) en `twoFound`
  (4×) - en vijf functies gebruiken `string` als parameternaam. Dat is een
  repo-breed verschijnsel en geen week 4-defect; het is hier gemeld en niet
  gerepareerd. Neem die namen niet over als je op het bord typt.
- **`source/_toc.yml` zet `lectures/4b_midterm` bij het college.** In de
  inhoudsopgave staat het bestand onder `course/week_4`, naast
  `lectures/4a_lussen`, terwijl het de derde bijeenkomst draagt. Dat is de
  boekstructuur en niet de bijeenkomststructuur, en het is geen defect - maar
  wie de inhoudsopgave als rooster leest, leest hem verkeerd.

### Korte antwoorden bij de collegeopdrachten

**Deze subsectie is bij week 4 leeg, en dat is geen omissie.** Waar de andere
weken hier korte antwoorden geven omdat er geen uitwerking bestaat, is week 4 de
week waarin die noodgreep niet nodig is: `source/solutions/4a_lussen.ipynb`
dekt alle vijf de collegeopdrachten plus de extreme lus, en
`source/solutions/4_midterm.ipynb` alle twintig van de oefenmidterm. Dat zijn
precies de twee collegebestanden die de hele cursus rijk is - samen goed voor 25
van de 58 collegeopdrachten - en het is nagemeten. Antwoorden horen in
`source/solutions/`, daar hoort een docent ze te kunnen halen, en voor deze week
kan dat.

### Wat er uit de handleidingen van 2023 niet is overgenomen

Er zijn drie Word-handleidingen voor week 4 geweest, en er is van geen van
drieën een tijd overgenomen. Er valt hier dus meer af dan bij week 1, 2 en 3.
Dat is geen oordeel over die documenten maar het gevolg van twee verschuivingen.

Twee van de drie gingen volledig over recursie: de een over oefenen met turtles
in 45 minuten, de ander over recursief problemen oplossen zonder computer in 90.
Recursie staat sinds het besluit *Recursie na de lussen* in week 9, en in het
week 4-materiaal komt het woord niet meer voor. Die 135 minuten vervallen dus in
hun geheel.

De derde beschreef de oefenmidterm en had als enige een expliciete lesindeling:
5 minuten opening, 15 minuten op papier zonder overleg, 5 minuten overleg in
duo's en 20 minuten klassikaal bespreken met Python Tutor, samen 45 van de 90.
Die cyclus meet een les waarin de hele groep in de pas loopt, en onder de
vastgestelde indeling valt de oefenmidterm in het practicum: zelfstandig, in
eigen tempo, met meenemen wat niet af komt. *Geen overleg* is precies wat een
practicum niet is, en twintig minuten álles bespreken is een andere handeling
dan een peilmoment over vier vragen. Die tijden zijn daarom gewogen en niet
overgenomen; het zouden geleende getallen zijn geweest en geen overgeleverde.

Wat wél is overgenomen is de **werkvorm**: eerst zelf voorspellen, dan pas de
uitwerking erbij. Die staat in blok 1 en 2 van sectie 4. De antwoorden uit die
bron zijn niet bruikbaar, want ze horen bij een andere set opdrachten dan de
twintig die er nu staan.

### Wat er nog loopt

- **De drie Word-handleidingen van week 4 zijn verwijderd**, en deze handleiding
  is er de opvolger van; wie ze wil nalezen vindt ze in de git-geschiedenis. Dat
  volgt de regel in `curriculum/uitgangspunten.md`: zo'n document is een bron om
  uit te putten, elk exemplaar verdwijnt uiteindelijk, en het uitgangspunt is
  nieuw ontwerp op de gewijzigde weekopzet. Er staan er nu nog **vier**, van
  week 5 en 6. Ze wachten op werkitem #95.
- **De bijeenkomstindeling van week 4 is met dit werkitem vastgelegd** als
  vierde erkende afwijking in `curriculum/uitgangspunten.md`. Tegelijk is daar
  één bijzin rechtgezet die van de oude indeling uitging: het besluit over het
  lusrecept redeneerde vanuit een practicumsleuf die door CodingBat bezet zou
  zijn, en dat is sinds deze vaststelling niet meer zo. De conclusie van dat
  besluit is niet veranderd.
- **`handleidingen/week_3.md` verwijst nog naar de oude kopnaam.** Die
  handleiding haalt de afwijkingensectie van `curriculum/uitgangspunten.md` aan
  onder haar vorige naam, *Drie erkende afwijkingen*, en die kop heet sinds dit
  werkitem *Vier erkende afwijkingen*. De verwijzing loopt daardoor **stil**
  dood: er staat nog iets, het klopt alleen niet meer. Het is één woord, en het
  valt buiten de afbakening van dit werkitem.
- **Deze week levert geen enkele overgeleverde tijd op en is daarmee de eerste.**
  Wie hem geeft en meet, kan de eerste **B**-tijden van week 4 aanleveren. Tot
  die er zijn staan alle twintig blokken als richttijd, en zo horen ze gelezen te
  worden.
- Deze handleiding beschrijft het materiaal zoals het op **21 september 2026** in
  de repository staat.

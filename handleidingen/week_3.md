# Docentenhandleiding PGM1 week 3

Deze week geeft de student code een naam. Hij schrijft zijn eerste eigen
functies, geeft ze een docstring, test ze met `assert`, en ziet wat Python doet
terwijl een functie een andere functie aanroept.

Het is de week waarin `return` binnenkomt, en daarmee de eerste echt
onzichtbare fout van de cursus: een functie die niets teruggeeft werkt, en levert
`None`. De student ziet iets op het scherm en denkt dat het goed is.

De lijn die de drie bijeenkomsten bij elkaar houdt is het probleem waarmee week 2
eindigde. Dat probleem - welk van twee getallen is het grootste - is deze week
Opdracht 1 van het eerste college, en het is nu een functie met een naam.

## 1. De week in het kort

| Bijeenkomst | Vorm | Materiaal |
|---|---|---|
| 1 | College | `source/lectures/3a_functies.ipynb` |
| 2 | Werkcollege | `source/lectures/3b_functies_aanroepen.md` |
| 3 | Practicum | `source/practicals/3_fijne_functies.ipynb` + `source/problems/3_opstap.ipynb`, `3_basis.ipynb`, `3_extra.ipynb` |

Daarnaast staan er vier overzichtspagina's die je zelf niet hoeft te behandelen:
`source/course/week_3.md` (`## Functies`) vat de week samen voor de student, en
`source/course/practical_3.md`, `source/course/opgaven_3.md` en
`source/course/solutions_3.md` zijn de omslagpagina's boven het practicum, de
opgaven en de uitwerkingen. De vier bestanden in `source/solutions/` staan in die
laatste; ze zijn openbaar voor de student en daarom geen materiaal dat je zelf
brengt.

### Deze week valt het practicum naar de derde bijeenkomst

De indeling college - werkcollege - practicum uit
`curriculum/uitgangspunten.md` §`### Drie bijeenkomsten per week` gaat ervan uit
dat het werkcollege door een bestand uit `practicals/` wordt gevuld. Week 3 doet
dat anders: `source/lectures/3b_functies_aanroepen.md` vult het werkcollege, en
`source/practicals/3_fijne_functies.ipynb` schuift naar de derde bijeenkomst,
naast de drie opgavebundels.

Dat is een erkende afwijking, vastgelegd in `curriculum/uitgangspunten.md`
§`#### Vijf erkende afwijkingen` en vastgesteld door de vakdeskundige op
**11 september 2026**. De grond staat in het materiaal zelf: `3b` laat de student
zijn code opslaan als `wk3wc2.py` - werkcollege 2 - terwijl het bestand in
`source/lectures/` staat.

Wat de moedertabel wél bepaalt, en wat deze week gewoon geldt: de tweede
bijeenkomst is de plek waar een probleem **gezamenlijk stap voor stap wordt
opgebouwd**, en de derde is **zelfstandig werken onder begeleiding**. Die derde
bijeenkomst is dus vrije ruimte en geen af te vinken lijst.

### Over de tijden

De blokschema's hieronder zijn ontworpen op wat deze week nodig heeft. De twee
Word-handleidingen van 2023, die tot dit werkitem in `teacher_guides/` stonden,
zijn daarna als controle ernaast gelegd en niet als vertrekpunt gebruikt. Dat is
de regel die in `curriculum/uitgangspunten.md` staat: zo'n document is een bron om
uit te putten, geen voorloper om te volgen. Wie ze wil nalezen vindt ze in de
git-geschiedenis.

Bij week 3 is dat geen formaliteit. In de bron voor het eerste college lag 45 van
de 90 minuten bij opdrachten die nu in bijeenkomst 3 staan, en in die voor het
tweede ging 55 van de 90 minuten over recursie, die naar week 9 is verhuisd.

**Elk blok draagt daarom zijn herkomst.** In de kolom *Herkomst* betekent **B**
dat het blok op een blok uit de handleiding van 2023 steunt, en **R** dat het een
richttijd zonder bron is - een verdedigbare schatting, en niets meer dan dat.

| Bijeenkomst | Blokken | B: bron 2023 | R: richttijd zonder bron |
|---|---|---|---|
| 1 | 8 | 2 (20 min) | 6 (70 min) |
| 2 | 8 | 4 (50 min) | 4 (40 min) |
| 3 | 5 | 0 | 5 (90 min) |
| **samen** | **21** | **6** | **15** |

Van de vier bronblokken in bijeenkomst 2 zijn 45 van die 50 minuten werkelijk
overgeleverd; de vijf overige staan bij het blokschema van die bijeenkomst
verantwoord. Over de hele week valt dus 70 van de 270 minuten in een blok met een
bron - ruim een kwart - en de rest is schatting. Lees de tabellen zo.

Alle drie de bijeenkomsten tellen op tot **90 minuten** met een ongetimede pauze.
**Hoe lang een bijeenkomst werkelijk duurt staat nergens in de repository.** Duurt
die van jou korter of langer, schaal de blokken dan mee.

### Wat je nodig hebt

- **Een scherm waarop je code kunt uitvoeren terwijl de klas kijkt.** Het eerste
  college heeft vier cellen die zich lenen voor voorspellen-en-draaien: twee
  waarbij de vraag is welke waarde eruit komt, en twee die met opzet een
  foutmelding geven. Dat is deze week de werkvorm, en zonder scherm valt hij weg.
- **Turtle, voor bijeenkomst 2.** Opdracht 2 van `3b` tekent een driehoek in een
  eigen venster. Dat is de eerste keer in het vak dat turtle voorkomt, en
  `source/lectures/0b_install_python.md` noemt turtle noch tkinter. Op de machine
  waarop deze handleiding is gemaakt importeert turtle zonder fout; of dat op elke
  studentmachine geldt is **niet vastgesteld**. Probeer het vóór de bijeenkomst
  op een studentmachine, en houd er rekening mee dat een deel van de zaal
  meekijkt in plaats van zelf tekent.
- **Een editor, en niet alleen de notebooks.** Bij Opdracht 2 van `3b` zet de
  student zijn code voor het eerst over naar een los bestand, `wk3wc2.py`. Wie
  daar nog nooit is geweest, is daar de hele twintig minuten mee bezig.
- **Papier.** De twee opdrachten van `3b` beginnen allebei met "wat doet deze
  functie" en "wat is de output". Die werken beter als het antwoord eerst op
  papier staat.

## 2. Bijeenkomst 1 - College: functies

Materiaal: `source/lectures/3a_functies.ipynb`.

De dragende lijn komt uit het materiaal zelf. Week 2 sloot af met het
maximumprobleem, en Opdracht 1 van dit college is precies `maximum()`. Open dus
met dat probleem op het bord en met de vraag hoe je zoiets een naam geeft; blok 7
geeft het antwoord. Die opening is tegelijk de korte opfris van vorige week -
terugkijken en zeggen waar het naartoe gaat - en zij zit daarom ín blok 1 en is
geen apart blok.

### Blokschema

| # | Min | Blok | Waar in `3a_functies.ipynb` | Herkomst |
|---|---:|---|---|---|
| 1 | 10 | Opfris en lesdoel: het maximumprobleem van vorige week terug op het bord, en de vraag hoe je zoiets een naam geeft | `# Functies`, `## Computing` | B |
| 2 | 10 | Van `f(x) = 2x + 3` naar `def f(x):` - structuur tegenover procedure, en de signatuur | `## Handelen`, `## Structuur versus procedure` | R |
| 3 | 15 | `flipside` van binnen: docstring, lokale variabele, en waarom je die variabele zet | `## Binnen een functie`, `### Docstrings`, `### Gebruik variabelen`, `### Variabelen opnieuw definiëren` | R |
| 4 | 15 | `return` tegen `print`, en de `TypeError` die daaruit volgt | `### Return versus print`, `#### Het verschil` | R |
| | | **Pauze** | | |
| 5 | 10 | Testen met `assert`: de aanname, de `AssertionError`, en `None` testen | `### Testen`, `### None?` | R |
| 6 | 10 | `range`, `sum` en `choice`, en wat een import doet | `## Belangrijke functies`, `### Range`, `### Sum`, `### Choice`, `## Imports` | B |
| 7 | 15 | Opdracht 1 klassikaal begonnen, daarna Opdracht 2 en 3 in duo's | `## Opdracht 1`, `## Opdracht 2`, `## Opdracht 3` | R |
| 8 | 5 | Bespreken, en vooruitblik: morgen roepen functies elkaar aan | - | R |

Acht blokken, 90 minuten. Twee ervan steunen op de bron, samen 20 minuten; de
andere zes zijn richttijd.

**Wat er ten opzichte van 2023 is veranderd.** De bron besteedde 45 van zijn 90
minuten aan `interp`, `convert_from_seconds` en `checkends`. Die drie zijn nu
Opdracht 2, 5 en 3 van `source/practicals/3_fijne_functies.ipynb` en liggen dus
in bijeenkomst 3. Die 45 minuten gaan hier naar `## Binnen een functie`, dat in
de bron geen enkel blok had terwijl het de moeilijkste stof van het college
draagt. Het bronblok over de opfris van week 2 is van 15 naar 10 minuten gegaan,
omdat het naar "opdracht 8 van week 2" verwees en die opdracht niet meer bestaat.
En het bronblok over de main-functie verhuist naar bijeenkomst 2, met het
materiaal mee.

**Eén volgorde-eis die niet onderhandelbaar is.** Blok 6 blijft in deze
bijeenkomst, ook als de tijd knelt. Opdracht 1 van
`source/lectures/3b_functies_aanroepen.md` gebruikt morgen `list(range(n + 1))`
en `sum(lst)`, en Opdracht 1 en 3 van
`source/problems/3_opstap.ipynb` doen hetzelfde. Wat binnen dat blok wél kan
vallen is `## Imports`: de drie opties daar zijn naslag.

### Hoe je het brengt

**Blok 1.** Zet het maximumprobleem van vorige week terug op het bord, met de
`if`-`else` die de klas toen schreef. Vraag wat je doet als je dat op drie
plekken in een programma nodig hebt. Het antwoord dat je wilt horen is "opnieuw
opschrijven", en dat is het probleem waar dit college het gereedschap voor geeft.
Zeg erbij dat ze aan het eind van de bijeenkomst precies dit als functie
schrijven.

**Blok 2.** De brug van wiskunde naar Python. `f(x) = 2x + 3` beschrijft wat iets
*is*; `def f(x): return 2 * x + 3` beschrijft wat iets *doet*. Wijs op de drie
delen van de eerste regel - `def`, de naam, de parameters tussen haakjes - en op
de dubbele punt, met dezelfde inspringregel als bij `if` van vorige week.

**Blok 3.** Het langste uitlegblok en het belangrijkste. Loop `flipside` regel
voor regel langs: de docstring, dan `x = len(s) // 2`, dan de returnregel. Het
punt van dit blok is de lokale variabele. Zet de returnregel er zoals het
materiaal doet ook een keer zonder variabele naast en vraag welke van de twee je
morgen nog wilt lezen.

Het materiaal heeft hier een kadertje dat vraagt welke naam beter is dan `x`.
Laat de klas dat beantwoorden en accepteer meer dan één antwoord; het gaat om de
gewoonte, niet om het woord.

**Blok 4.** Hier staan de twee cellen waar dit college om draait, en ze werken
alleen als je ze draait.

Doe eerst de cel met `a_dbl = dbl(20) + 20`. Laat de klas voorspellen wat
`a_dbl` wordt, draai hem, en druk `a_dbl` af - de cel zelf toont niets, want er
staat alleen een toekenning. Er komt `60` uit.

Doe daarna de cel met `a_dbl_pr = dbl_pr(20) + 20`, en **laat de klas weer eerst
voorspellen**. Vrijwel iedereen zegt opnieuw 60, want `dbl_pr(20)` zet keurig
`40` op het scherm. Draai hem dan: er komt `40` op het scherm én een `TypeError`.
Dat verschil - het scherm klopt en de waarde bestaat niet - is de duurste fout
van deze week, en hij kost je hier twee minuten.

**Blok 5.** `assert` in twee zinnen: het is een aanname, klopt hij dan gebeurt er
niets, klopt hij niet dan stopt Python met een `AssertionError`. Draai daarna de
cel met `assert flipside("") == "ergfout"`, die met opzet faalt, en laat zien dat
de melding de regel noemt. Sluit het blok af met `assert dbl_pr(20) is None` en
vraag waarom die aanname klopt; dat is de brug terug naar blok 4.

**Blok 6.** `range`, `sum` en `choice`, en wat een import doet. Kort en
zakelijk - dit is gereedschap voor morgen, geen onderwerp. Zeg één ding hardop:
`range` telt **tot** en niet tot en met. De drie importopties zijn naslag; noem
ze en ga door.

**Blok 7.** Begin Opdracht 1 klassikaal en niet verder dan de eerste twee regels:
de signatuur en de docstring. Schrijf er één assertion onder en vraag de klas om
de tweede, die een randgeval dekt. Laat ze daarna Opdracht 1 afmaken en Opdracht
2 en 3 in duo's doen, en loop rond. De drie opdrachten staan alle drie
onderaan het notebook met een lege cel eronder, dus ze kunnen meteen typen.

Wat je tijdens het rondlopen vraagt is niet "werkt het al" maar "welk randgeval
heb je getest". Twee gelijke getallen bij Opdracht 1, nul seconden bij Opdracht
2, twee gelijke strings bij Opdracht 3 - het materiaal noemt ze zelf.

**Blok 8.** Bespreek Opdracht 1 en sluit de lijn van blok 1: het probleem van
vorige week heeft nu een naam en je kunt hem zo vaak aanroepen als je wilt. Wijs
vooruit: morgen roepen functies elkáár aan, en dan ga je zien wat de computer
daarbij doet.

### Waar het vastloopt

- **`return` tegen `print`.** Dit is de fout van de week, en hij loopt **luid**
  af op een plek waar de student de melding niet begrijpt: `dbl_pr(20) + 20`
  geeft een `TypeError`, terwijl er wél `40` op het scherm staat. De student
  concludeert dat de functie werkt en dat Python zeurt. Draai die cel klassikaal
  voordat iemand er zelf op stuit.
- **`None` als returnwaarde van een functie zonder `return`.** Dezelfde fout van
  de andere kant, en deze loopt **stil** af. De functie "werkt", drukt iets af en
  levert niets, en een programma dat daarmee verder rekent doet dat met niets.
  Laat `assert dbl_pr(20) is None` zien: `None` is de waarde die eruit komt, niet
  de afwezigheid van een antwoord.

### Als het niet uitkomt

- **Blok 3 loopt uit.** Dat mag; het is het blok dat je níét moet inkorten. Haal
  de tijd bij blok 6 vandaan door `## Imports` over te slaan - de drie opties zijn
  naslag en de student heeft morgen alleen `from random import ...` nodig, die in
  blok 6 bij `### Choice` al langskomt.
- **Je komt niet aan blok 7 toe.** Geef Opdracht 1, 2 en 3 mee en begin morgen
  met het bespreken van Opdracht 1. Wat je niet doet is blok 6 laten vallen: `3b`
  Opdracht 1 en de hele opstap staan op `range` en `sum`, en zonder die twee kost
  het je morgen meer tijd dan het je nu oplevert.
- **Je houdt tijd over.** Laat duo's die klaar zijn een derde assertion bij hun
  eigen functie schrijven die wél faalt, en de melding lezen. Dat is dezelfde
  stof van de andere kant en kost je geen voorbereiding.
- **De klas komt niet los bij Opdracht 1.** Doe `maximum` dan helemaal voor en
  geef Opdracht 3 als het zelfstandige werk; die lijkt er het meest op, met
  strings in plaats van getallen.

## 3. Bijeenkomst 2 - Werkcollege: functies aanroepen

Materiaal: `source/lectures/3b_functies_aanroepen.md`.

Dit is het werkcollege in de zin van `curriculum/uitgangspunten.md`: de plek waar
een probleem gezamenlijk stap voor stap wordt opgebouwd. Dat probleem is Opdracht
2 - de turtle-code die de klas samen in `wk3wc2.py` opbouwt. Dat is ook de grond
onder de erkende afwijking van deze week, en de reden dat blok 7 het zwaarste
blok is en het laatste dat je inkort.

### Blokschema

| # | Min | Blok | Waar in `3b_functies_aanroepen.md` | Herkomst |
|---|---:|---|---|---|
| 1 | 5 | Lesdoel: functies roepen functies aan, en je gaat zien wat de computer daarbij doet | `# Functies aanroepen` | B |
| 2 | 10 | De quiz: `demo(15)` eerst zelf narekenen, dan pas het antwoord | `## Quiz` | R |
| 3 | 20 | De stack, stap voor stap: zeven afbeeldingen, zeven keer één frame erbij of eraf | `## Hoe functies werken` | R |
| 4 | 10 | De main-functie, en de `NameError` die je krijgt als de volgorde niet klopt | `## De main-functie` | B |
| | | **Pauze** | | |
| 5 | 5 | Waar je assertions neerzet: `testing()` naast `main()` | `## Assertions in een eigen functie` | R |
| 6 | 15 | Opdracht 1: `triangle`, en narekenen met Python Tutor | `## Opdracht 1` | B |
| 7 | 20 | Opdracht 2: samen opbouwen in `wk3wc2.py`, tot de driehoek er staat | `## Opdracht 2` | B |
| 8 | 5 | Afronden, en vooruitblik naar het practicum | - | R |

Acht blokken, 90 minuten. Vier ervan steunen op de bron, samen 50 minuten
waarvan 45 werkelijk overgeleverd; de andere vier zijn richttijd.

**Wat er ten opzichte van 2023 is veranderd.** Van de 90 bronminuten ging 55 over
recursie, en die stof staat nu in `source/lectures/9a_intro_recursie.ipynb` en
`source/lectures/9b_recursief.ipynb`. Die 55 minuten vervallen dus volledig.
Daarvoor komen de vier secties die in het huidige materiaal het meeste dragen en
in de bron geen blok hadden: de quiz (10), de stack (20), de assertions (5) en
het afsluitblok (5). Blok 6 kreeg er 5 minuten bij op het bronblok, omdat de
huidige Opdracht 1 een deelvraag **c** heeft die de bron niet had: de student
schrijft daar zelf twee assertions. Die vijf minuten zijn dus richttijd binnen
een bronblok.

**De twee getallen die niemand kan naslaan, en waarom ze zo staan.** De stack
krijgt 20 minuten omdat het zeven discrete stappen zijn die elk hardop gezegd
moeten worden, en omdat het de enige plek in het vak is waar de student de
machine zelf ziet - een investering die zich in week 9 terugbetaalt. De
assertions krijgen 5 minuten omdat het één idee is op vijfentwintig regels
materiaal. Allebei richttijden, en zo staan ze in de tabel.

**Blok 4 is een overgeleverd getal uit de ándere docx.** De tien minuten voor de
main-functie kwamen uit het blok *Main functie* van de bron voor het eerste
college; het
materiaal is naar `3b` verhuisd en het blok verhuist mee. Dat is de enige plek
waar een bronminuut tussen twee bijeenkomsten is verplaatst, en het staat hier
zodat het niet als toeval wordt gelezen.

**Twee dingen die deze bijeenkomst anders maken dan de andere twee.** `3b` is
geen notebook maar een `.md`-bestand; er zijn dus geen cellen om uit te voeren en
alle code in het materiaal is leeswerk. En Opdracht 2 draait niet in de browser
of in een cel, maar als `wk3wc2.py` in een eigen venster, met turtle. Reken erop
dat het overzetten naar een los bestand voor een deel van de zaal nieuw is.

### Hoe je het brengt

**Blok 1.** Eén zin over wat er komt en één over waar het naartoe gaat: aan het
eind van deze bijeenkomst heb je samen een programma gebouwd dat uit meerdere
functies bestaat en dat in een eigen bestand draait.

**Blok 2.** Laat de klas `demo(15)` eerst zelf narekenen, op papier, en zeg erbij
dat het antwoord een paar regels verderop op dezelfde pagina staat, onder
`### Antwoord` - dan zoeken ze het niet stiekem op. Het antwoord is `42.0`. De `.0`
is het halve punt van de vraag: `x / 3` levert een floating-point getal op, en
dat werkt door tot in het eindantwoord.

**Blok 3.** De stack, en dit is het blok waar de bijeenkomst om draait. Doorloop
de zeven afbeeldingen zelf en laat de klas bij elke stap zeggen wat erbij komt of
eraf gaat. Wijs bij het derde frame aan dat de `x` daar een ándere variabele is
dan de `x` in `demo`, met een eigen waarde; dat is wat "lokaal" betekent en het
is de reden dat het hele plaatje werkt.

**Blok 4.** De volgorde-eis. Laat het eerste voorbeeld uit het materiaal zien,
waarin de aanroep boven de definitie staat, en lees de `NameError` hardop voor.
Zeg erbij dat dit dezelfde melding is als bij een variabele die nog niet bestaat.
Daarna de main-functie als antwoord: alles wordt eerst geladen, en de laatste
regel zet het in gang.

**Blok 5.** Kort. `testing()` naast `main()`, en de assertions daarbinnen, zodat
je in één oogopslag ziet waar getest wordt. Meer is het niet.

**Blok 6.** Opdracht 1 zoeken ze zelf uit - **a** en **b** op papier, dan **c**
erbij, en loop rond. Deelvraag **c** is de eerste keer deze week dat een student
zelf een assertion schrijft; vraag bij het rondlopen welk randgeval de tweede
dekt. Bespreek daarna klassikaal met Python Tutor op het scherm, zoals deelvraag
**d** vraagt. De output is `15`.

**Blok 7.** Dit is het werkcollege. Bouw het samen op: laat ze de code
overnemen in `wk3wc2.py`, draai hem, en zorg dat er bij iedereen een driehoek in
een eigen venster staat voordat je verdergaat. Dat is het punt waar de tijd
verdwijnt en het is de moeite waard.

Doe daarna deelvraag **c** - de parameter voor de zijdelengte - klassikaal voor,
inclusief het aanpassen van de docstring. Deelvraag **d** is voor henzelf: twee
assertions die vastleggen dat `tri()` `None` teruggeeft, voor twee verschillende
zijdelengtes. Dat is dezelfde `None` als gisteren, nu in hun eigen code.

**Blok 8.** Vijf minuten. Zeg wat er morgen gebeurt: het practicum met vijf
functies, en daarnaast de drie bundels. Zeg erbij dat morgen zelfstandig werken
is en dat jij rondloopt.

### Waar het vastloopt

- **De volgorde: een functie moet geladen zijn vóór je hem aanroept.** Dit loopt
  **luid** af - `NameError: name 'dbl' is not defined` - maar hij raakt vandaag
  iedereen, want dit is de eerste keer dat ze een eigen bestand schrijven en zelf
  bepalen waar de regels staan. Het antwoord is de main-functie, met de aanroep
  onderaan.
- **De assertion die faalt zolang het antwoord er niet staat.** Dit loopt
  **luid** af, en juist daarom denkt de student dat de cel of het bestand stuk
  is. Dat is hij niet: een `AssertionError` betekent dat de functie iets anders
  teruggeeft dan de aanname zegt, en één van die twee klopt niet. Zeg erbij dat
  ze zelf moeten uitzoeken wélke, want vanaf Opdracht 1 **c** schrijven ze de
  aannames zelf en kan de fout ook daar zitten.
- **`range` telt tót en niet tot en met.** **Stil**, en daarom duur. In Opdracht 1
  is `triangle(5)` gelijk aan `15` en niet aan `10`, want `list(range(n + 1))`
  loopt van 0 tot en met 5. Wie de `+ 1` over het hoofd ziet, krijgt een
  antwoord dat er geloofwaardig uitziet. Dezelfde valkuil zit morgen in Opdracht
  1 en 3 van `source/problems/3_opstap.ipynb`.

### Als het niet uitkomt

- **Blok 3 loopt uit.** Laat het lopen tot ongeveer 25 minuten en haal de tijd
  bij blok 6 vandaan: doe daar alleen **a** en **b** klassikaal en geef **c** en
  **d** mee. De stack samen doorlopen is niet thuis te doen; Opdracht 1 wel.
- **Je komt niet aan blok 7 toe.** Dit is de ingreep die je niet moet doen. Blok
  7 is de enige plek in de week waar samen een programma wordt opgebouwd, en het
  is de reden dat deze bijeenkomst het werkcollege is. Kort liever blok 2 in tot
  het antwoord en de `.0`, en sla blok 5 over - assertions naast `main()` komen
  morgen in het practicum vanzelf terug.
- **Turtle werkt niet bij een deel van de zaal.** Laat die studenten meekijken
  met een buurman en de code wél overnemen; deelvraag **d** gaat over de
  returnwaarde en die is ook zonder tekening te testen. Meld het, want het is
  geen bekende storing: `source/lectures/0b_install_python.md` noemt turtle niet.
- **Je houdt tijd over.** Laat duo's `tri()` een tweede parameter geven voor de
  kleur, of de driehoek twee keer tekenen vanuit `main()`. Allebei laten zien dat
  een functie met een naam herbruikbaar is, en dat is de boodschap van vandaag.

## 4. Bijeenkomst 3 - Practicum: fijne functies en de opgaven

Materiaal: `source/practicals/3_fijne_functies.ipynb`, en de drie opgavebundels
`source/problems/3_opstap.ipynb`, `source/problems/3_basis.ipynb` en
`source/problems/3_extra.ipynb`.

Dit is zelfstandig werk onder begeleiding. Je legt weinig uit en loopt veel rond.

**Verwijs naar de bundels op naam en niveau, niet op opgavenummer.** De drie
bundels hebben elk een eigen doel - de opstap is er voor wie de stof nog niet
vertrouwt, de basis is de zelftest, de extra is een uitdaging - en dat staat ook
zo op `source/course/opgaven_3.md`. De nummering binnen de bundels is deze week
extra onbetrouwbaar: `source/problems/3_basis.ipynb` heeft helemaal geen
"Opdracht 1", en de naam "Opdracht 1" wijst deze week naar vier verschillende
plekken. Zie sectie 5.

### Blokschema

Deze bijeenkomst heeft **geen handleiding uit 2023**, net als bijeenkomst 3 van
week 1 en van week 2. Alle tijden hieronder zijn richttijden, geschat op de
omvang van het materiaal, en geen overgeleverde lesindeling.

| # | Min | Blok | Waar | Herkomst |
|---|---:|---|---|---|
| 1 | 10 | Aftrap: `tpl` samen voordoen, en wat de drie bundels van elkaar onderscheidt | `3_fijne_functies`: `## Voorbeeldopgave` · `source/course/opgaven_3.md` | R |
| 2 | 25 | Het practicum, getallen eerst: `sq`, `interp`, `checkends` | `3_fijne_functies`: `` ### Opdracht 1: `sq(x)` `` t/m `` ### Opdracht 3: `checkends(s)` `` | R |
| | | **Pauze** | | |
| 3 | 20 | Het practicum, strings en de lijst van vier: `swap_ends`, `convert_from_seconds` | `3_fijne_functies`: `` ### Opdracht 4: `swap_ends(s)` ``, `` ### Opdracht 5: `convert_from_seconds(seconds)` `` | R |
| 4 | 30 | Vrije ruimte in de bundels, ieder op zijn eigen niveau | `source/problems/3_opstap.ipynb`, `3_basis.ipynb`, `3_extra.ipynb` | R |
| 5 | 5 | Afronden: waar het volgende week naartoe gaat | `3_basis`: `## Tot slot` | R |

Vijf blokken, 90 minuten als richttijd.

**Dit is een ritme en geen rooster.** Blok 2, 3 en 4 zijn één doorlopend werkblok
met twee peilmomenten erin: na blok 2 kijk je waar de zaal staat, en bij de
overgang naar blok 4 zeg je hardop dat wie nog in het practicum zit daar gewoon
mag blijven. De moedertabel noemt deze bijeenkomst zelfstandig werken onder
begeleiding, en dat is precies wat het is - er hoeft niets af.

### Hoe je het brengt

**Blok 1.** Twee dingen, kort. Ten eerste `tpl`: het materiaal zegt zelf *"Deze
doen we samen voor"*, dus doe hem samen voor, inclusief de twee assertions
eronder. Die twee assertions zijn de vorm die je de rest van de middag van
iedereen wilt zien - één gewoon geval, één randgeval.

Ten tweede de drie bundels, en vooral dat ze **niet alle drie voor iedereen
zijn**. De basis is de zelftest; wie daar vastloopt gaat naar de opstap; wie er
doorheen vliegt gaat naar de extra. Zeg dat expliciet, anders begint iedereen bij
de opstap.

**Blok 2.** De eerste drie opdrachten van het practicum, en verder niets van jou.
Loop rond en vraag bij elke functie twee dingen: staat er een docstring, en welk
randgeval dekt je tweede assertion. Dat zijn de twee gewoontes die deze week moet
opleveren, en ze zijn alleen af te dwingen terwijl ze typen.

**Blok 3.** Hetzelfde voor de twee stringopdrachten. `convert_from_seconds` is de
zwaarste van de vijf en de enige die een lijst teruggeeft; het materiaal geeft de
eerste twee regels cadeau, dus wie vastloopt kijk je met die regels mee en vraag
je wat er nu nog in `seconds` zit.

**Blok 4.** Rondlopen. Wie bij de basis vastloopt stuur je naar de opstap en niet
naar de uitwerking. Wie klaar is met de basis mag naar de extra, en die is
bedoeld om níét af te komen.

**Blok 5.** Vijf minuten, en gebruik `## Tot slot` van
`source/problems/3_basis.ipynb` als vooruitblik. Daar staat het probleem dat de
student met het gereedschap van deze week net niet kan oplossen: negen bijna
gelijke termen uitschrijven kan nog, maar een IBAN is achttien tekens in
Nederland en eenendertig op Malta. Zeg dat daar volgende week het antwoord op
komt, en noem het woord lus.

### Waar het vastloopt

- **`swap_ends("q")` geeft `"qq"`.** **Stil**, en het is precies het randgeval
  dat de opdracht vraagt te testen. Zonder de controle op de lengte wijzen `s[0]`
  en `s[-1]` naar hetzelfde karakter, en de functie plakt dat karakter twee keer
  achter elkaar. Wie alleen `"hond"` en `"python"` test, ziet niets.
- **De lengtecontrole die bij `has_nine_digits` vooraan moet.** In
  `source/problems/3_basis.ipynb` roept `is_valid` eerst `has_nine_digits` aan en
  pas daarna `weighted_sum`. Staat die volgorde andersom, dan knalt index 8
  eruit bij een te kort nummer. Dat loopt **luid** af, met een
  `IndexError` op een regel waar de reden niet zichtbaar is - de fout zit in de
  aanroep erboven en niet in de functie die stukloopt.
- **`interp` zonder `if` schrijven.** Dit is geen fout maar een blokkade: de
  opdracht vraagt nadrukkelijk om het zonder `if` te doen, en de student weet niet
  hoe hij moet beginnen. Het materiaal geeft de tip zelf - begin bij
  `(hi - low)` - maar dat kader staat onder de opdrachttekst en wordt
  overgelezen. Wijs erop in plaats van de oplossing te geven.

### Als het niet uitkomt

- **Blok 2 loopt uit omdat de helft nog bij `interp` zit.** Laat het lopen en
  haal de tijd bij blok 4 vandaan. De bundels zijn ook thuis te maken en de
  uitwerkingen staan in `source/solutions/`; het practicum onder begeleiding
  maken is de reden dat deze bijeenkomst bestaat.
- **Blok 7 tot en met 8 van gisteren zijn blijven liggen.** Doe ze hier, vóór
  blok 1, en haal de tijd bij blok 4 vandaan. Opdracht 2 van `3b` samen opbouwen
  is niet thuis te doen; aan de bundels werken wel.
- **De helft komt niet aan de bundels toe.** Prima. Deze bijeenkomst is vrije
  ruimte en er hoeft niets af. Wat je wel doet is in blok 5 vijf minuten nemen om
  te zeggen wat de bundels zijn en waar de uitwerkingen staan.
- **Iemand is na een halfuur met alles klaar.** Stuur hem naar
  `source/problems/3_extra.ipynb`, en daarbinnen naar Opdracht 2 - de
  schrikkeljaren. Die vraagt om het probleem zelf in functies op te delen, en dat
  is de vaardigheid waar de rest van het vak op staat.

## 5. Wat je verder moet weten

### Eigenaardigheden in het materiaal

- **"Opdracht 1" wijst deze week naar vier plekken, en "Opdracht 2" ook.**
  `## Opdracht 1` staat in `source/lectures/3a_functies.ipynb`, in
  `source/lectures/3b_functies_aanroepen.md` en in
  `source/problems/3_extra.ipynb`, en `### Opdracht 1` staat in
  `source/problems/3_opstap.ipynb` - een kopniveau lager, maar in de klas hoor je
  dat verschil niet. Met de uitwerkingen erbij zijn het er zes. Noem dus altijd
  het bestand of de bijeenkomst erbij.
- **`source/lectures/3a_functies.ipynb` heeft geen rubriekkop boven de
  opdrachten.** Waar `source/practicals/3_fijne_functies.ipynb` een
  `## Opdrachten` heeft, staan de drie van het college als `## Opdracht 1`,
  `## Opdracht 2` en `## Opdracht 3` op hetzelfde niveau als `## Computing` en
  `## Imports`, en alle drie helemaal aan het eind van het notebook. Dat raakt je
  blokschema: de opdrachten zitten niet bij het onderwerp waar ze bij horen, dus
  je springt in blok 7 terug naar boven.
- **Drie koppen in `source/lectures/3a_functies.ipynb` hebben geen titel.** De
  drie importopties heten *Optie 1:*, *Optie 2:* en *Optie 3:* - een volgnummer,
  een dubbele punt, en daarachter niets. Ze zijn niet bruikbaar als verwijzing;
  zeg "de eerste importoptie" en wijs hem aan.
- **`source/problems/3_basis.ipynb` heeft geen "Opdracht 1".** De bundel loopt van
  `` ## Stap 1: `is_digit(c)` `` tot `` ## Stap 6: `check(bsn)` ``, en daarnaast staat er
  één **ongenummerde** `### Opdracht` onder `## De parkeerautomaat`. Dat is
  correct volgens `conventies/begrippen.md` - een stap is een stap - maar je moet
  het weten voordat je "opdracht 7" zegt.
- **De uitwerking van de basis draagt de zes stappen niet als kop.**
  `source/solutions/3_basis.ipynb` heeft alleen `## Het burgerservicenummer` en
  `## De parkeerautomaat`. Wie een student naar "de uitwerking van stap 4" wil
  sturen, moet in die eerste sectie zoeken.
- **Practicum en uitwerking staan een kopniveau uit elkaar.**
  `source/practicals/3_fijne_functies.ipynb` schrijft
  `` ### Opdracht 1: `sq(x)` ``, `source/solutions/3_fijne_functies.ipynb`
  schrijft `` ## Opdracht 1: `sq(x)` ``. Dezelfde namen, ander niveau.
- **`source/course/practical_3.md` heeft als titel `# Werkcollege`**, maar draagt
  het practicum van bijeenkomst 3. Dat is een restant; de begrippenlijst legt
  `practicals/` bij het practicum. Week 1 en week 2 hebben hetzelfde.
- **`source/lectures/3b_functies_aanroepen.md` is een `.md` en geen notebook.**
  Er zijn dus geen cellen om uit te voeren, en alle code op die pagina is
  leeswerk. Dat is ook de reden dat Opdracht 2 de student naar een los bestand
  stuurt, en daarmee de grond onder de erkende afwijking van deze week.
- **De quiz in `3b` geeft het antwoord op dezelfde pagina**, een paar regels
  onder de vraag, onder `### Antwoord`. Zeg dat erbij voordat de klas begint te
  rekenen, anders scrollt de helft door.
- **Turtle komt deze week voor het eerst voor en staat niet in de
  installatiepagina.** `source/lectures/0b_install_python.md` noemt turtle noch
  tkinter. Zie *Wat je nodig hebt*.

### Korte antwoorden bij de collegeopdrachten

Voor de vijf collegeopdrachten van deze week bestaat geen `solutions/`-bestand;
die zijn er wel voor het practicum en de bundels. De antwoorden hieronder zijn
voor jou, niet om uit te delen, en ze zijn **uitgevoerd en niet uitgerekend**.

| Opdracht | Bestand | Antwoord |
|---|---|---|
| `## Opdracht 1` | `3a_functies.ipynb` | `return a if a > b else b`; randgeval twee gelijke getallen: `maximum(4, 4)` is `4` |
| `## Opdracht 2` | `3a_functies.ipynb` | `return seconds // 60`; randgeval nul seconden: `minutes(0)` is `0`, en `minutes(59)` is ook `0` |
| `## Opdracht 3` | `3a_functies.ipynb` | `return s if s > t else t`; randgeval twee gelijke strings: `alphabetic("peer", "peer")` is `"peer"` - let op dat hoofdletters vóór kleine letters komen, dus `alphabetic("Peer", "appel")` is `"appel"` |
| `## Opdracht 1` | `3b_functies_aanroepen.md` | **a** `triangle` telt de getallen 0 tot en met `n` op; **b** het programma drukt `15` af; **c** bijvoorbeeld `assert triangle(5) == 15` en als randgeval `assert triangle(0) == 0` |
| `## Opdracht 2` | `3b_functies_aanroepen.md` | **b** een gelijkzijdige driehoek in een eigen venster, in een willekeurige kleur; **c** `def tri(side):` met `forward(side)` in plaats van `forward(100)`; **d** `tri()` geeft `None` terug, dus `assert tri(100) is None` |

De antwoorden bij Opdracht 1 tot en met 3 van `3a` geven de returnregel en niet
de hele functie: de docstring en de assertions horen de student zelf te
schrijven, en dat is de opdracht.

**Deze sectie is een noodgreep voor een gat.** Over de hele cursus dragen twaalf
collegebestanden samen 58 genummerde opdrachten, en twee van die twaalf hebben
een uitwerking in `source/solutions/` - die van week 4, samen goed voor 25 van de
58. Voor de tien andere collegebestanden, waaronder beide van deze week, bestaat
er geen. Antwoorden horen in `source/solutions/`, en daar hoort een docent ze te
kunnen halen; zolang die er voor deze week niet zijn, staan ze hier.

### Wat er uit de handleidingen van 2023 niet is overgenomen

Hier valt meer af dan bij week 1 en week 2, en dat is geen oordeel over de oude
documenten maar een gevolg van de gewijzigde weekopzet.

Uit de bron voor het eerste college zijn de drie opdrachtblokken **niet**
overgenomen: 45 van
de 90 minuten gingen over `interp`, `convert_from_seconds` en `checkends`, en die
drie zijn nu Opdracht 2, 5 en 3 van het practicum en liggen dus in bijeenkomst 3.
De uitwerking van `interp` in die docx staat bijna woordelijk in het huidige
practicum, dus er gaat niets verloren. Het blok *Opfris week 2* verwees naar
"opdracht 8 van week 2 eerste werkcollege", en die opdracht bestaat niet meer;
wat ervan overblijft is de opfris zelf, in blok 1. Het blok *Main functie* is
niet vervallen maar verhuisd, naar bijeenkomst 2, met het materiaal mee. En de
drie huidige opdrachten van `3a` komen in de bron helemaal niet voor.

Uit de bron voor het tweede college is **het lesdoel zelf** niet overgenomen. Dat
luidde
*"Introductie recursie met behulp van turtles"*, en 55 van de 90 minuten ging
daarover. Recursie staat nu in week 9, in
`source/lectures/9a_intro_recursie.ipynb` en
`source/lectures/9b_recursief.ipynb`; in de week 3-bestanden komen de woorden
recursie en recursief geen enkele keer voor. Wat van die docx overeind blijft is
de openingsstructuur en het idee om met turtle te werken - dat laatste zit in
Opdracht 2 van het huidige `3b`.

Van de vier secties die het huidige `3b` het zwaarst maken - de quiz, de stack
met zeven afbeeldingen, de main-functie en de assertions in een eigen functie -
had er in de bron **geen enkele** een blok. Die vier zijn dus nieuw ontworpen, en
ze staan als richttijd in het blokschema.

Voor bijeenkomst 3 bestaat geen bron. Het practicum en de drie bundels zijn na
2023 geschreven.

### Wat er nog loopt

- **De twee `.docx` van week 3 zijn met dit werkitem uit `teacher_guides/`
  verwijderd**, en deze handleiding is er de opvolger van; wie ze wil nalezen
  vindt ze in de git-geschiedenis. Dat volgt de regel in
  `curriculum/uitgangspunten.md`: een `.docx` is een bron om uit te putten, elke
  `.docx` verdwijnt uiteindelijk, en het uitgangspunt is nieuw ontwerp op de
  gewijzigde weekopzet. Na deze wijziging staan er nog **zeven** `.docx` in
  `teacher_guides/`: drie van week 4 en vier van week 5 en 6. Ze wachten op
  werkitem #95. De drie van week 4 zijn er inmiddels uit en `handleidingen/week_4.md`
  citeert ze niet meer. Met #276 en #280 verdwenen ook die van week 5 en 6; sindsdien
  bestaat `teacher_guides/` niet meer.
- **Kruisverwijzingen lopen stil achter als materiaal verschuift.** Eén zin in
  `source/lectures/3a_functies.ipynb` zei dat `convert_from_seconds` in het
  werkcollege wordt geschreven, terwijl die functie Opdracht 5 van het practicum
  is en dus in bijeenkomst 3 ligt. Die zin is met dit werkitem rechtgezet. Het is
  het tweede geval op rij - `source/course/week_4.md` verwees eerder naar "de
  lijsten uit week 3" terwijl lijsten uit week 2 komen - en het is de reden om na
  elke verschuiving de verwijzingen na te lopen.
- Deze handleiding beschrijft het materiaal zoals het op **23 september 2026** in
  de repository staat.

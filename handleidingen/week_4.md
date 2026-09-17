# Docentenhandleiding PGM1 week 4

Deze week leert de student lussen lezen, voorspellen en ontwerpen. De nadruk
ligt op code begrijpen: eerst voorspelt de student wat een programma doet en
wanneer een lus stopt, daarna schrijft hij lussen voor kleine problemen. Het
lusrecept uit het college verbindt de drie bijeenkomsten.

## 1. De week in het kort

| Bijeenkomst | Vorm | Materiaal |
|---|---|---|
| 1 | College | `source/lectures/4a_lussen.ipynb` |
| 2 | Werkcollege | `source/lectures/4b_midterm.md` en `source/solutions/4_midterm.ipynb` |
| 3 | Practicum | `source/practicals/4_python_bat.md` en `source/problems/4_opstap.ipynb`, `4_basis.ipynb`, `4_extra.ipynb` |

De student ziet daarnaast `source/course/week_4.md` als overzichtspagina. De
opstap-, basis- en extra-opgaven hebben uitwerkingen in de overeenkomstige
bestanden onder `source/solutions/`. Gebruik die om antwoorden na te kijken,
niet als extra lesmateriaal.

De tijden hieronder zijn richttijden. Alleen de oude docx voor de oefenmidterm
geeft een expliciete lesindeling; voor het college en het practicum is in de
repository geen tijdsmeting beschikbaar. Schaal de blokken mee met je rooster.

### Wat je nodig hebt

- Een scherm waarop je code kunt uitvoeren en een bord waarop je een lusronde
  kunt bijhouden.
- Papier voor voorspellingen. Laat studenten eerst schrijven en pas daarna
  uitvoeren.
- Voor bijeenkomst 2 een browser met Python Tutor als visueel hulpmiddel.
- Voor bijeenkomst 3 toegang tot CodingBat en een werkende Python-omgeving om
  code te bewaren. CodingBat controleert de uitkomst, maar vervangt het
  uitleggen van de lus niet.

## 2. Bijeenkomst 1 - College: lussen ontwerpen

Materiaal: `source/lectures/4a_lussen.ipynb`.

### Blokschema

| # | Min | Blok | Waar in het notebook |
|---|---:|---|---|
| 1 | 5 | Lesdoel en een eerste `for`-lus lezen | `# Lussen`, `## for lussen` |
| 2 | 15 | `for`, `range` en de waarden per ronde | `## for lussen` |
| 3 | 15 | Iteratief ontwerp: `for` of `while` | `## Iteratief ontwerp`, `### Variabelen` |
| 4 | 10 | Pauze en korte voorspellingsoefening | `### In het kort` |
| 5 | 15 | Het lusrecept en de plaats van `return` | `## for!`, `### Stap voor stap` |
| 6 | 10 | Een element- of indexlus kiezen | `## Twee typen for` |
| 7 | 10 | `while`, conditie en stopmoment | `## Extreme lussen`, `## while lussen` |
| 8 | 10 | Collegeopdrachten en vooruitblik | `## Quiz` en opdrachten onderaan |

Gebruik bij het lusrecept steeds dezelfde vijf vragen:

1. Wat verzamel je en wat is de startwaarde?
2. Waar loop je langs? Daaruit volgt `for` of `while`, en bij een `for` een
   element- of indexlus.
3. Wat gebeurt er per stap met wat je verzamelt?
4. Wanneer is het klaar?
5. Wat geef je terug, en waar staat die regel?

De vierde vraag verdient extra aandacht. Bij een `while` ligt het aantal rondes
niet vooraf vast, maar de lus moet wel een stopmoment hebben. Een `while` is dus
geen synoniem voor een oneindige lus.

### Hoe je het brengt

Laat bij een `for` één tabel op het bord staan met de waarde van de lusvariabele
en de waarde van de verzamelvariabele per ronde. Zo zien studenten het verschil
tussen de waarde vóór de ronde, de wijziging in de body en de code na de lus.
Vraag bij `range` expliciet welke eindwaarde niet meedoet.

Gebruik het voorbeeld van de faculteit om het recept te demonstreren. Laat de
studenten eerst de vijf vragen beantwoorden en voer daarna de functie uit. De
uitwerking van de collegeopdrachten (`source/solutions/4a_lussen.ipynb`) geeft
hiervoor ook `factors` en `count_vowels`: twee functies waarbij de
verzamelvariabele pas na alle rondes kan worden teruggegeven.

Bij een indexlus vraag je wat de index toevoegt. Als de code alleen de waarden
leest, is een elementlus eenvoudiger. Een index is nodig wanneer de positie zelf
nodig is, bijvoorbeeld om een vorige positie in een string te bekijken.

Sluit af met een korte extreme lus. Laat de klas aanwijzen welke variabele de
conditie verandert. In de uitwerking staat waarom de lus met `guess == 42` niet
stopt: de body verandert `guess` niet. Dat is een bruikbare overgang naar de
vierde vraag van het recept.

### Waar het vastloopt

- Studenten tellen `range(5)` als zes waarden. Schrijf de reeks uit: `0` tot en
  met `4`.
- Een `return` in de lus beëindigt de hele functie. Laat het verschil zien met
  een `return` op dezelfde inspringing als de `for`.
- Studenten verwarren de lusvariabele met de verzamelvariabele. Vraag welke
  waarde na de lus het antwoord bevat.
- Bij een indexlus wordt `range(len(lijst))` gelezen als de elementen van de
  lijst. Benoem dat dit indices zijn; de elementen komen pas met `lijst[ix]`.
- Bij `while` letten studenten op de conditie, maar niet op de wijziging in de
  body. Vraag na elke ronde opnieuw of de conditie nog waar is.

## 3. Bijeenkomst 2 - Werkcollege: de oefenmidterm lezen

Materiaal: `source/lectures/4b_midterm.md` en
`source/solutions/4_midterm.ipynb`.

De oefenmidterm bestaat uit twintig leesopdrachten. De student leest een
programma en kiest wat het afdrukt of dat het programma niet werkt. Behandel dit
als leesonderwijs: de waarde zit in voorspellen, uitleggen en fouten herkennen,
niet in zo snel mogelijk de antwoorden verzamelen.

### Blokschema

| # | Min | Blok |
|---|---:|---|
| 1 | 5 | Doel, werkwijze en antwoordvorm uitleggen |
| 2 | 15 | Opdrachten 1 tot en met 7 zelfstandig op papier |
| 3 | 5 | Antwoorden vergelijken in duo's |
| 4 | 20 | Opdrachten 1 tot en met 7 klassikaal bespreken |
| 5 | 15 | Opdrachten 8 tot en met 13 zelfstandig of in duo's |
| 6 | 10 | Opdrachten 8 tot en met 13 bespreken met Python Tutor |
| 7 | 15 | Opdrachten 14 tot en met 20: stopmoment en fouten |
| 8 | 5 | Terugblik op het lusrecept en voorbereiding practicum |

De oude `teacher_guides/4_midterm.docx` gebruikt dezelfde werkvorm: eerst
individueel werken, daarna antwoorden in duo's vergelijken en vervolgens
klassikaal bespreken met Python Tutor. De antwoordlijst in die docx hoort bij
een oudere versie. Gebruik voor inhoudelijke antwoorden de actuele
`source/solutions/4_midterm.ipynb`.

### Hoe je het brengt

Laat studenten bij elke vraag drie dingen noteren: de toestand vóór de eerste
ronde, de toestand na elke relevante ronde en het moment waarop de lus stopt.
Bespreek niet alle twintig vragen even lang. Kies vragen die een denkstap
zichtbaar maken en laat de overige antwoorden kort controleren.

Gebruik Python Tutor pas nadat studenten hun voorspelling hebben opgeschreven.
De animatie is bewijs voor een redenering, geen vervanging ervan. Laat een
student de volgende stap voorspellen voordat je op *next* klikt.

Besteed extra aandacht aan de actuele uitwerking van opdrachten 8, 14, 18 en
20. Daar eindigt het programma met respectievelijk een `NameError`, een
`IndentationError`, een `ZeroDivisionError` en een lus die niet eindigt. In alle
gevallen is "Het programma werkt niet" het juiste soort antwoord. Bij opdracht
20 ontbreekt het stopmoment uit vraag 4 van het lusrecept; de lijst blijft
groeien en de `print` wordt nooit bereikt.

Laat bij opdrachten waarin `/` voorkomt de werkelijke uitvoer controleren. In
Python 3 geeft `/` een floating-point getal, ook als de deling precies uitkomt.
Dat verklaart enkele antwoorden die op papier als integer lijken.

### Bespreekpunten

- Staat de `return` binnen of buiten de lus?
- Welke variabele verandert de conditie van de `while`?
- Wordt een element gebruikt of alleen een index?
- Welke foutmelding ontstaat bij het lezen van de code, en komt Python dan nog
  aan uitvoeren toe?
- Is de laatste `print` bereikbaar?

Als de groep veel tijd nodig heeft voor de eerste vragen, bespreek dan minder
vragen plenair. Laat de rest afmaken als voorbereiding op het practicum. Houd
het onderscheid tussen "ik weet de uitvoer" en "ik kan uitleggen waarom" vast.

## 4. Bijeenkomst 3 - Practicum: lussen schrijven

Materiaal: `source/practicals/4_python_bat.md` en de drie opgavebundels onder
`source/problems/`.

Begin met de twaalf CodingBat-opgaven uit het practicum. De eerste zes zijn
list-problemen en de laatste zes string-problemen. De voorbeeldfunctie
`double_char` is geschikt om het lusrecept nog één keer hardop langs te lopen.
Laat studenten daarna de opgaven verdelen over elementlussen, indexlussen en
een `while` wanneer het stopmoment pas tijdens het uitvoeren ontstaat.

### Blokschema

| # | Min | Blok |
|---|---:|---|
| 1 | 10 | CodingBat openen, voorbeeld en lusrecept herhalen |
| 2 | 25 | Zelfstandig werken aan list-problemen |
| 3 | 15 | Bespreken van strategieën en veelgemaakte fouten |
| 4 | 25 | Zelfstandig werken aan string-problemen |
| 5 | 10 | Een oplossing bewaren en met eigen tests controleren |
| 6 | 5 | Keuze van opstap, basis of extra en afsluiting |

De opstap is leeswerk: tien `for`-opdrachten en tien `while`-opdrachten waarin
de student uitvoer en stopmoment voorspelt. De basis vraagt drie programma's te
lezen en te wijzigen: machtsverheffen, een som met een conditie en een
`while`-programma dat een herhaling zoekt. De extra-opgave gebruikt een
Monte-Carlo-benadering van pi met een begrensde `for`-lus en een onbegrensde
`while`-lus. Verwijs naar de uitwerking als hulpmiddel bij nakijken; geef de
student niet vooraf de volledige code.

### Waar je op let

- Laat studenten hun CodingBat-code kopiëren naar een Python-bestand. Een groen
  CodingBat-resultaat zegt dat de voorbeelden slagen, niet dat de student de
  strategie kan uitleggen.
- Vraag bij iedere functie naar de startwaarde van de verzamelvariabele en naar
  de regel die haar per ronde bijwerkt.
- Laat studenten minstens één extra test bedenken, bijvoorbeeld een lege string,
  een lijst zonder passende elementen of de kleinste geldige invoer.
- Bij een `while` moet de student aanwijzen welke waarde de conditie dichter bij
  stoppen brengt. Een programma dat alleen tijdens de les stopt is geen goede
  uitleg van het stopmoment.

Als studenten vastlopen, laat ze eerst het probleem in één zin formuleren, dan
de vijf vragen van het lusrecept invullen en pas daarna code schrijven. Wie
klaar is, vergelijkt een elementlus met een indexlus waar beide kunnen en legt
uit waarom één vorm leesbaarder is.

## 5. Terugblik en valkuilen van de week

De belangrijkste lijn is: een lus voert een stap herhaald uit, een
verzamelvariabele bewaart het resultaat en de code na de lus gebruikt het
volledige resultaat. Laat studenten aan het einde één programma uit de week in
die termen uitleggen.

Let op deze terugkerende fouten:

- `return` staat te vroeg in de lus;
- de eindwaarde van `range` wordt meegeteld;
- de conditie van een `while` verandert nooit;
- de student kiest een index terwijl alleen het element nodig is;
- de startwaarde heeft niet het juiste type, bijvoorbeeld `0` waar een lijst of
  lege string nodig is;
- een CodingBat-voorbeeld wordt letterlijk nagebouwd zonder het probleem te
  lezen.

Wijs vooruit naar week 5: lussen kunnen daar in elkaar staan. Een student die
deze week de toestand per ronde en het stopmoment kan verwoorden, heeft
daarvoor een bruikbare basis.

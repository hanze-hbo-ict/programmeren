# Docentenhandleiding PGM2 week 2 — List comprehensions (cursusweek 9)

Deze week leert de student een bekend lusrecept korter opschrijven en weer
teruglezen. De hoofdvraag is telkens wat wordt verzameld en wat wordt
weggelaten. Het register in het practicum verbindt die keuze aan woorden en
regelnummers. Korter schrijven is pas geslaagd als de student de oorspronkelijke
lus nog kan uitleggen.

## De week in één oogopslag

| Bijeenkomst | Product om op te controleren |
|---|---|
| College 1 — list comprehensions | Een comprehension naar een lus terugvertalen. |
| College 2 — dict en set comprehensions | Een collectie kiezen en een lus behouden waar die beter past. |
| Practicum — tekstregister | Woorden aan regelnummers koppelen en het register afdrukken. |

Elke bijeenkomst duurt netto 90 minuten. De blokken hieronder zijn
ontwerpinschattingen, geen gemeten behandeltijden of garantie dat iedereen klaar
komt. Pauzes vallen buiten deze 90 minuten. De volgorde is die van dit lesplan;
de opgaven onder `problems/` blijven huiswerk.

## Voorbereiding en middelen

Bronstatus: gecontroleerd tegen `adfdc5c8` van `origin/master`. De actuele
[weekpagina](../source/course/week_9.md) geeft de studentroute. Open de
collegenotebooks, voer je eigen demonstraties vooraf uit en houd de hieronder
genoemde uitwerkingen bij de hand voor je begeleiding. Gebruik een werkende
Python-/editor-/notebookomgeving en papier of bord voor voorspellingen. Vraag
eerst iedereen iets op te schrijven voordat je antwoorden uit de groep ophaalt.

Open het [registerpracticum](../source/practicals/9_register.ipynb) inclusief de
gegeven tekst en testcellen. Leg de uitwerkingen van [register](../source/solutions/9_register.ipynb),
[opstap](../source/solutions/9_opstap.ipynb), [basis](../source/solutions/9_basis.ipynb) en
[extra](../source/solutions/9_extra.ipynb) klaar. Controleer vóór college 1 met een
kleine vraag of studenten het lusrecept met een verzamelvariabele herkennen.

## College 1 — een lus korter schrijven

Doel: de expressie, lusvariabele en het filter kunnen terugvinden

Gebruik [9a, van *Een lus die een nieuwe lijst verzamelt* tot en met *Opdrachten*](../source/lectures/9a_list_comprehensions.ipynb).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Laat het gegeven lusrecept eerst zelfstandig annoteren: startwaarde, doorgangen en verzameld element. | Student kan zeggen wat na één doorgang aan de lijst is toegevoegd. |
| 25 | Zet lus en comprehension uit het college naast elkaar. Dek om beurten één versie af en laat duo’s die terugschrijven. | De verzamelde expressie en het filter krijgen elk een plek in de lus. |
| 20 | Laat bij `range`, `enumerate` en `zip` eerst één geleverde waarde of één paar opschrijven. Voer daarna de bestaande voorbeelden uit. | Student onderscheidt positie en element en koppelt de juiste twee waarden. |
| 20 | Vergelijk filteren met de conditionele expressie. Laat voor één element beslissen of het verdwijnt of een andere waarde krijgt; gebruik daarna de collegeopdrachten. | Student voorspelt of de lengte verandert en kan de keuze verklaren. |
| 15 | Laat individueel een bestaande comprehension terugvertalen. Bespreek een verschil zonder direct een complete oplossing te tonen. | Student herstelt een fout via de lusbetekenis. |

**Controlepunt.** Vraag bij de terugvertaling wat één doorgang oplevert. Alleen de juiste haakjes opschrijven is onvoldoende; het filter en de waarde-keuze moeten afzonderlijk verklaard worden.

## College 2 — de passende collectie

Doel: dict/set comprehensions gebruiken en weten wanneer de lus blijft

Gebruik [9b, *Een set verzamelen*, *Een dictionary verzamelen*, *Tellen met sum*, *Een lijst van lijsten* en *Wanneer je een lus houdt*](../source/lectures/9b_dict_en_set_comprehensions.ipynb).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Haal een list comprehension op en laat aangeven welke informatie een lijst bewaart. | Student kan volgorde en herhaling onderscheiden van setinhoud. |
| 25 | Laat dezelfde collegegegevens als set en dictionary verzamelen; vraag bij de dictionary eerst naar sleutel en waarde. | De collectie past bij de vraag; een dictionarypaar wordt als paar verklaard. |
| 20 | Laat bij tellen de lijst binnen `sum([...])` benoemen en bij de lijst van lijsten één rij apart volgen. | Student ziet eerst de verzamelde waarden en daarna de som of buitenlijst. |
| 25 | Bespreek *Wanneer je een lus houdt*. Laat duo’s de collegeopdrachten maken en bij een bijwerking of onthouden tussen stappen de lus verdedigen. | Student kiest op leesbaarheid en afhankelijkheden, zonder alles in een comprehension te persen. |
| 10 | Laat één keuze voor een lus en één voor een comprehension individueel motiveren. | Student noemt wat per doorgang moet worden onthouden of verzameld. |

**Controlepunt.** Houd de weekgrens aan: één `for` met eventueel filter, ook in een geneste comprehension; geen twee `for`-clausules in één comprehension en geen generator expressions. Laat een onleesbare versie naar de gegeven lus terugbrengen.

## Korte antwoorden bij collegeopdrachten

### 9a

| Opdracht | Antwoordkern |
|---|---|
| Opdracht 1 | De vier lijsten zijn `[0, 1, 4, 9]`, `["vuurtoren", "hoog"]`, `[1, 3, 4]` en `["kort", "lang", "kort"]`. |
| Opdracht 2 | `positions = [i for i, word in enumerate(words) if word != "spam"]`. |
| Opdracht 3 | Start `result = []`; loop langs `zip(names, scores)`, voeg bij `score < 8` met `result.append([name, score + 1])` toe; klaar na de lus, met `result` als antwoord. |
| Opdracht 4 | `results = ["voldoende" if grade >= 5.5 else "onvoldoende" for grade in grades]`. |

### 9b

| Opdracht | Antwoordkern |
|---|---|
| Opdracht 1 | De uitvoer is een set met `2`, `3`, `4`, dan `{"ja": "j", "nee": "n"}`, `[[0, 1, 2], [1, 2, 3]]` en `2`; setvolgorde ligt niet vast. |
| Opdracht 2 | `first_year = {animal: years[0] for animal, years in zodiac_years.items()}`. |
| Opdracht 3 | Gebruik `{word: len(word) for word in words}` en `{word for word in words if len(word) > 4}` voor nieuwe verzamelingen; bewaar voor `longest` in een lus het beste woord en vervang het alleen bij strikt grotere lengte. |

## Practicum — een register bij een tekst

Doel: de registerfuncties in samenhang bouwen en testen

Gebruik [9_register, stappen 1–5](../source/practicals/9_register.ipynb).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Bekijk het gegeven tekstregister. Laat studenten voor één woord aanwijzen welke regelnummers bij de waarde horen. | Sleutel en lijst van regelnummers krijgen een concrete betekenis. |
| 25 | Laat stappen 1–2, `index_words` en `lines_with`, maken. Laat eerst de unieke woorden op tekstvolgorde aanwijzen en daarna met `enumerate` één gevonden regelnummer volgen. | Student bewaart eerste voorkomens bij `index_words` en vindt regelnummers vanaf 1 met `lines_with`. |
| 25 | Begeleid stap 3, `register`. Laat eerst de twee reeds geteste functies in het plan plaatsen. | Student gebruikt de deelresultaten in plaats van dezelfde zoeklus opnieuw te bedenken. |
| 20 | Laat stappen 4–5, `on_more_lines` en `print_register`, maken. Vraag welke functie selecteert en welke afdrukt. | Student houdt selectie en uitvoer gescheiden. |
| 10 | Laat testcellen uitvoeren en één falend geval naar een deelfunctie herleiden. Noteer het vervolg. | Teststatus en eerstvolgende reparatie zijn zichtbaar. |

**Controlepunt.** Vraag bij een correct register om één waarde met de oorspronkelijke tekst te controleren. Laat daarna de bijbehorende comprehension teruglezen als een lus; zo controleer je begrip naast tests.

## Huiswerk en begeleiding

Plan het eerste deel van [de opstap](../source/problems/9_opstap.ipynb) na college 1
en het dict-/setdeel na college 2. [De basis](../source/problems/9_basis.ipynb) bouwt
woordenanalyse korter op; stap 4, `ngram_loop`, vraagt juist de terugvertaling naar
een lus. Vraag daar bij begeleiding naar de oorspronkelijke verzameling voordat
je syntax bespreekt. [Het toernooi](../source/problems/9_extra.ipynb) en de
[aanvullende oefeningen](../source/extra/practice/2_list_comprehension.ipynb) zijn
verdieping. De `key=`-vooruitblik in de extra is geen schrijfvereiste: functie
als argument en lambda-functies komen in week 4.

## Voorkennis, nieuwe begrippen en vervolg

Voorkennis: dictionaries, sets en tuple-uitpakken uit week 1 en het
PGM1-lusrecept. Nieuw: comprehensions, `enumerate`, `zip` en de conditionele
expressie. Voor het directorypracticum van week 3 levert deze week dictionaries
en `sum([...])` op. Laat die som kunnen uitleggen zonder al recursie in te voeren.

## Verwachte vastloopmomenten

Dit zijn verwachtingen om tijdens de les te toetsen, geen gerapporteerde
ervaringen met deze PGM2-lessen.

| Signaal bij de student | Kleine docentinterventie |
|---|---|
| Student zet de waarde-keuze op de plaats van het filter. | Laat één element door de lus volgen: gaat het element weg, of krijgt het een andere waarde? |
| Student gebruikt bij `enumerate` het element als index. | Laat één werkelijk paar uit het college opschrijven en de twee namen daarboven zetten. |
| Student kan zijn geneste comprehension niet meer voorlezen. | Laat eerst één binnenlijst als gewone lus herstellen en daarna de buitenste lus; verkort pas als de betekenis klopt. |

## Als de route niet afkomt

Bij tijdgebrek beperk je het aantal vergelijkbare bespreekvoorbeelden en laat
je de extra liggen. Bewaar beide vertaalrichtingen en het onderscheid tussen
filter en waarde-keuze. Laat bij een onaf register precies noteren welke stap en
test nog openstaan; maak daarvan vervolgwerk, geen nieuwe standaardbijeenkomst.
Wie zonder voorbereiding begint, krijgt eerst de bestaande lus uit college 1 om
te annoteren en werkt daarna mee aan dezelfde vertaling. Voeg geen nieuw
comprehensionrecept toe om de achterstand te omzeilen.

# Docentenhandleiding PGM2 week 1 — Datastructuren (cursusweek 8)

De student kent een lijst op volgorde en het veranderen van één element. Nu
komt daar zoeken op betekenis bij: een dictionary koppelt een sleutel aan een
waarde. Het taalmodel maakt zichtbaar waarom die waarde ook een lijst kan zijn.
Het eerste college bouwt het tellen op; het tweede verandert tellen in opvolgers
bewaren. Het practicum gebruikt precies die stap om tekst te genereren.

## De week in één oogopslag

| Bijeenkomst | Product om op te controleren |
|---|---|
| College 1 — methoden en dictionaries | Sleutel, waarde en bijgewerkte telling kunnen aanwijzen. |
| College 2 — sets en taalmodel | Een opvolgerslijst en de rol van herhaling kunnen verklaren. |
| Practicum — Markov | Een gecontroleerd model gebruiken voor gegenereerde tekst. |

Elke bijeenkomst duurt netto 90 minuten. De blokken hieronder zijn
ontwerpinschattingen, geen gemeten behandeltijden of garantie dat iedereen klaar
komt. Pauzes vallen buiten deze 90 minuten. De volgorde is die van dit lesplan;
de opgaven onder `problems/` blijven huiswerk.

## Voorbereiding en middelen

Bronstatus: gecontroleerd tegen `adfdc5c8` van `origin/master`. De actuele
[weekpagina](../source/course/week_8.md) geeft de studentroute. Open de
collegenotebooks, voer je eigen demonstraties vooraf uit en houd de hieronder
genoemde uitwerkingen bij de hand voor je begeleiding. Gebruik een werkende
Python-/editor-/notebookomgeving en papier of bord voor voorspellingen. Vraag
eerst iedereen iets op te schrijven voordat je antwoorden uit de groep ophaalt.

Open vooraf [het Markovpracticum](../source/practicals/8a_text_genereren.md),
[de voorbeeldcode](../source/practicals/assets/file_and_dictionary_examples.py) en
[a.txt](../source/practicals/assets/a.txt). Zet Python-bestand en invoertekst in dezelfde
directory; controleer dat de tekst platte UTF-8-tekst is. Voor de huiswerkbegeleiding
staat de [Markov-uitwerking](../source/solutions/8a_text_genereren.ipynb) klaar, naast de bestaande uitwerkingen van [opstap](../source/solutions/8_opstap.ipynb),
[basis](../source/solutions/8_basis.ipynb) en [extra](../source/solutions/8_extra.ipynb).

## College 1 — methoden en dictionaries

Doel: lijstpositie en dictionarysleutel onderscheiden en een telling volgen

Gebruik [8a, *Terug naar lijsten*, *Dictionaries*, *Woorden tellen* en *Opdrachten*](../source/lectures/8a_datastructuren.ipynb).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Laat een lijstmutatie en tuple-uitpakken uit PGM1 op papier ophalen. Laat twee studenten hun verwijzingen tekenen. | Student onderscheidt de lijst zelf en de namen die ernaar verwijzen. |
| 20 | Demonstreer bij *Terug naar lijsten* een methodeaanroep. Laat de klas vóór uitvoeren de lijst na `append` tekenen. | Student wijst de data links van de punt en de handeling rechts aan. |
| 25 | Werk bij *Dictionaries* met het bestaande voorbeeld. Laat duo’s een sleutel kiezen, de waarde opzoeken en één paar toevoegen. | Student zoekt met een sleutel en probeert geen lijstpositie te gebruiken. |
| 25 | Laat bij *Woorden tellen* één woord tegelijk verwerken. Laat daarna collegeopdrachten maken en vraag bij de bespreking waarom een waarde verandert. | Student onderscheidt een nieuwe sleutel van een reeds geteld woord. |
| 10 | Laat ieder zonder overleg één opzoeking en één telstap verklaren; verbind resterende vragen aan de opstap. | Student benoemt wat sleutel en waarde betekenen. |

**Controlepunt.** Ga door als de student bij een bestaande telstap kan aanwijzen wat wordt opgezocht en wat wordt bijgewerkt. Vraag bij een onjuist antwoord eerst naar de concrete sleutel; herhaal niet meteen de hele lus.

## College 2 — sets en taalmodel

Doel: onderscheiden welke woorden voorkomen en welke woorden op elkaar volgen

Gebruik [8b, *Sets*, *Van tellen naar opvolgers*, *Tekst genereren* en *Opdrachten*](../source/lectures/8b_taalmodel.ipynb).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Haal de dictionarytelling op. Laat één student sleutel en waarde aanwijzen en een ander diens uitleg aanvullen. | De waarde is een aantal; de sleutel is het woord. |
| 20 | Laat bij *Sets* eerst unie en doorsnede op papier bepalen, dan met de notebook vergelijken. | Student vergelijkt inhoud zonder een vaste setvolgorde te eisen. |
| 30 | Vervang bij *Van tellen naar opvolgers* de telwaarde door een opvolgerslijst. Laat duo’s het bestaande tekstfragment woord voor woord volgen. | Student bewaart herhaalde opvolgers en kan uitleggen waarom één opvolger onvoldoende is. |
| 20 | Laat vóór uitvoeren één volgende stap van *Tekst genereren* aanwijzen. Gebruik de opdrachten voor zelfstandig voorspellen en bespreek afwijkende redeneringen. | Student kiest uit de lijst bij het huidige woord, niet uit alle woorden. |
| 10 | Open de practicumstart en laat de twee functies elk in één zin beschrijven. | Student scheidt model maken en model gebruiken. |

**Controlepunt.** Vraag welke opvolgers bij één sleutel horen en wat er verloren gaat als je die lijst door een set vervangt. Laat het antwoord aan het bestaande model aanwijzen.

## Korte antwoorden bij collegeopdrachten

### 8a

| Opdracht | Antwoordkern |
|---|---|
| Opdracht 1 | `append` verandert `L` in `[3, 1, 4, 1]` en geeft `None`; beide `get`-aanroepen laten `d` intact en geven respectievelijk `3` en `0`. |
| Opdracht 2 | Begin met `total = 0` en tel per `item` in `shopping_list` de waarde `prices.get(item, 0)` erbij op: totaal `7`. |
| Opdracht 3 | Loop met `for animal, years in zodiac_years.items()` langs de dieren en druk alleen bij `year in years` het dier af; zonder treffer volgt geen uitvoer. |

### 8b

| Opdracht | Antwoordkern |
|---|---|
| Stappenplannen taalmodel en tekst genereren | Voeg bij het model `new_word` toe aan de lijst van `previous_word`, bij generatie aan de uitvoertekst; na zinseindpunctuatie wordt `previous_word` weer `"$"`. |
| Opdracht 1 | `add` voegt `"koekje"` aan `s` toe en geeft `None`; `union` geeft een nieuwe set met `"spam"`, `"taart"`, `"koekje"` en `"thee"` en verandert `s` niet. |
| Opdracht 2 | `both = monday & thursday`, `at_least_once = monday \| thursday`; een set bewaart alleen aanwezigheid, zonder waarde per naam. |
| Opdracht 3 | `my_model = {"$": ["De", "De", "De"], "De": ["kat", "kat", "hond"], "kat": ["slaapt.", "eet."], "hond": ["blaft."]}`. |
| Opdracht 4 | Zinnen 1 en 3 kunnen; zin 2 niet, omdat `"taarten!"` niet direct op `"krijg"` volgt. |
| Opdracht 5 | De lijst is `["wil", "krijg", "wil"]`, de set bevat `"wil"` en `"krijg"`: kansen `2/3` en `1/2`; de lijst bewaart frequenties. |

## Practicum — tekst genereren

Doel: een model controleren voordat er een langere tekst mee wordt gemaakt

Gebruik [het practicum, opdracht 1 `create_dictionary`, opdracht 2 `generate_text` en de essayafronding](../source/practicals/8a_text_genereren.md).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Laat de startercode overnemen en a.txt openen vanuit de werkdirectory. Vraag beide functies in de editor aan te wijzen. | Bestand is leesbaar; de twee functies hebben ieder een eigen taak. |
| 35 | Begeleid opdracht 1. Laat eerst het kleine testbestand uit *Je code controleren* gebruiken en de opvolgerslijsten met de gegeven controle vergelijken. | Herhaalde opvolgers blijven behouden; na een eindleesteken wordt het startsymbool gebruikt. |
| 30 | Laat opdracht 2 bouwen. Vraag eerst de startkeuze en daarna de keuze na een gewoon woord en na een zinseinde aan te wijzen. | Student gebruikt het model, begint opnieuw na eindleestekens en kan een woord zonder opvolger opvangen via het startsymbool. |
| 10 | Laat in duo’s één gecontroleerde modelovergang tonen en daarna het gegenereerde resultaat bespreken. Start de bestaande essayafronding van circa 500 woorden. | Student verklaart een overgang aan de hand van de dictionary, ook als de zin vreemd klinkt. |
| 5 | Laat de teststatus en de nog te voltooien essaytaak noteren. | Vervolg noemt een concrete functie of de essayafronding. |

**Controlepunt.** Controleer modelconstructie afzonderlijk van willekeurige generatie. Een vloeiende tekst alleen bewijst niet dat de opvolgers goed worden bewaard. Leestekens blijven aan woorden vastzitten; na een terminaal woord zonder opvolgers volgt de bestaande terugkeer naar het startsymbool.

## Huiswerk en begeleiding

Na college 1: het dictionarydeel van [de opstap](../source/problems/8_opstap.ipynb)
en [de basis over woordenanalyse](../source/problems/8_basis.ipynb). Na college 2:
het setdeel van de opstap. Laat studenten bij een vastgelopen `count_words`
aanwijzen welke telstap uit het college terugkomt. De basis bouwt via inlezen,
woorden splitsen en tellen naar een rapport; laat een mislukte eindtest terugvoeren
op de afzonderlijke functies. [Woordenschat vergelijken](../source/problems/8_extra.ipynb)
is facultatief. Gebruik de tekstbestanden die de opgaven zelf aanbieden; voeg
geen dataset toe.

## Voorkennis, nieuwe begrippen en vervolg

Voorkennis: PGM1-lussen, functies, tekstbestanden, mutatie en tuple-uitpakken.
Nieuw: methoden, dictionaries, sets en een taalmodel. Controleer bij de afronding
of de student sleutel en waarde samen kan doorlopen met `.items()`: week 2
gebruikt die collectieopbouw. Introduceer deze week geen comprehensions of eigen
klassen.

## Verwachte vastloopmomenten

Dit zijn verwachtingen om tijdens de les te toetsen, geen gerapporteerde
ervaringen met deze PGM2-lessen.

| Signaal bij de student | Kleine docentinterventie |
|---|---|
| Student gebruikt een positie als dictionarysleutel. | Laat in het bestaande voorbeeld eerst de letterlijke sleutel aanwijzen en daarna de waarde; vergelijk pas dan met lijstindexering. |
| Student bewaart slechts één opvolger per woord. | Loop hetzelfde tekstfragment opnieuw door en laat bij iedere ontmoeting de lijst aanvullen. |
| Student beoordeelt een set als fout omdat de volgorde anders is. | Laat met unie/doorsnede uitsluitend bepalen welke elementen aanwezig zijn. |

## Als de route niet afkomt

Bij tijdgebrek verkort je de klassikale bespreking van vergelijkbare
collegeopdrachten en stel je de extra uit. Bewaar de modelcontrole en noteer
onvoltooide functies en de essayafronding als vervolg; een essay vervangt de
modelconstructie niet. Bij ontbrekende Python- of bestandsvoorbereiding laat je
de student tijdelijk in een werkend duo met de bestaande startercode meedoen.
Laat hem daarna zijn eigen bestand en werkdirectory herstellen. Voeg geen
exceptioncode toe; dat mechanisme hoort bij week 7.

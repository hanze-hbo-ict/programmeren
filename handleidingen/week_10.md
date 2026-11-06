# Docentenhandleiding PGM2 week 3 — Recursie (cursusweek 10)

Een functie kan het kleinere probleem aan een nieuwe aanroep overlaten. De
student moet daarbij niet alleen de afdaling volgen, maar ook kunnen zeggen wat
er terugkomt. Het eerste college maakt dat zichtbaar met frames en naspelen;
het tweede gebruikt die blik om zelf te ontwerpen. Het directorypracticum houdt
de datastructuur bekend, zodat de aandacht naar de recursieve stap kan gaan.

## De week in één oogopslag

| Bijeenkomst | Product om op te controleren |
|---|---|
| College 1 — recursie lezen | Afdaling én terugkeer kunnen volgen. |
| College 2 — recursief ontwerpen | Basisgeval, kleiner probleem en combinatie vooraf benoemen. |
| Practicum — directory doorzoeken | Recursieve functies op een directoryrepresentatie testen. |

Elke bijeenkomst duurt netto 90 minuten. De blokken hieronder zijn
ontwerpinschattingen, geen gemeten behandeltijden of garantie dat iedereen klaar
komt. Pauzes vallen buiten deze 90 minuten. De volgorde is die van dit lesplan;
de opgaven onder `problems/` blijven huiswerk.

## Voorbereiding en middelen

Bronstatus: gecontroleerd tegen `adfdc5c8` van `origin/master`; route bijgewerkt volgens [C4 van #481](https://github.com/hanze-hbo-ict/programmeren/issues/481#issuecomment-6685696981). De actuele
[weekpagina](../source/course/week_10.md) geeft de studentroute. Open de
collegenotebooks, voer je eigen demonstraties vooraf uit en houd de hieronder
genoemde uitwerkingen bij de hand voor je begeleiding. Gebruik een werkende
Python-/editor-/notebookomgeving en papier of bord voor voorspellingen. Vraag
eerst iedereen iets op te schrijven voordat je antwoorden uit de groep ophaalt.

Open [het directorypracticum](../source/practicals/10_directory_doorzoeken.ipynb) en
controleer de gegeven dictionaryrepresentatie; dit practicum gebruikt die data,
geen nieuwe opdracht om de eigen schijf te doorzoeken. Houd uitwerkingen van
[directory doorzoeken](../source/solutions/10_directory_doorzoeken.ipynb),
[opstap](../source/solutions/10_opstap.ipynb), [basis](../source/solutions/10_basis.ipynb) en
[extra](../source/solutions/10_extra.ipynb) gereed. Maak ruimte op het bord voor frames
met elk hun eigen argument en een terugkeerwaarde. Leg voor *Recursie unplugged*
een beker met getallen op papiertjes klaar; laat deelnemers de doorgeef- en
fluisterregels uit het college volgen.

## College 1 — lezen en naspelen

Doel: basisgeval en terugkeer van recursieve aanroepen herkennen

Gebruik [10a, *Een directory vol directories*, *Faculteit*, *Elke aanroep krijgt zijn eigen frame* en *Recursie unplugged*](../source/lectures/10a_recursie.ipynb).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Haal het directoryprobleem en functieframes op. Laat eerst individueel aanwijzen welk deelprobleem weer op het geheel lijkt. | Student herkent hetzelfde probleem in een kleinere directory. |
| 25 | Gebruik *Faculteit*: laat vóór uitvoeren het basisgeval zoeken en een kleine aanroep voorspellen. Laat duo’s hun voorspelling vergelijken. | Student kan aanwijzen waar geen volgende aanroep meer nodig is. |
| 20 | Speel de frames na. Laat bij elk frame zowel het argument als de later ontvangen waarde noteren. | Student hervat het wachtende frame en combineert de terugkeerwaarde. |
| 25 | Laat *Recursie unplugged* uitvoeren en de bijbehorende opdrachten eerst individueel lezen, daarna in duo’s bespreken. | Student volgt niet alleen wie aanroept, maar ook wie daarna antwoord krijgt. |
| 10 | Vraag een student één kleine trace af te maken en een ander de terugkeer te verklaren. | Basisgeval, aanroep en teruggeven zijn afzonderlijk herkenbaar. |

**Controlepunt.** Vraag wat de eerste aanroeper uiteindelijk ontvangt. Als de uitleg bij het diepste frame stopt, laat je dezelfde trace teruglopen voordat je een nieuw voorbeeld neemt.

## College 2 — ontwerpen vóór programmeren

Doel: drie ontwerpvragen toepassen op verschillende teruggeeftypen

Gebruik [10b, `power`, `vwl`, `keepvwl`, `largest`, `strip_end`, `only_digits` en *Opdrachten*](../source/lectures/10b_recursief_ontwerpen.ipynb).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Laat de drie vragen ophalen: wanneer klaar, wat wordt kleiner, hoe combineer je? Verzamel antwoorden op papier. | Student benoemt een basisgeval zonder meteen code te schrijven. |
| 25 | Werk het bestaande plan van `power` door. Laat een onvolledig plan eerst door duo’s aanvullen en pas daarna met de uitwerking vergelijken. | Student kan het kleinere argument en de resterende bewerking aanwijzen. |
| 20 | Zet `vwl` naast `keepvwl`. Vraag vooraf welk type antwoord de volgende aanroep teruggeeft. | Student kiest tellen of een string opbouwen vanuit het gevraagde type. |
| 20 | Verdeel `largest`, `strip_end` en `only_digits` over duo’s. Laat ieder duo basisgeval, kleiner probleem en combinatie aanwijzen en kort uitwisselen. | Student ziet dat niet elk geval dezelfde optelling of hetzelfde stopcriterium gebruikt. |
| 10 | Laat een bestaande collegeopdracht zelfstandig plannen; bespreek eerst de drie vragen en dan pas code. | Het plan noemt een uitvoerbare combinatie. |
| 5 | Verbind de plannen met directories; markeer de muntvraag aan het slot als vooruitblik. | Student weet wat deze week wordt ontworpen en wat pas week 4 wordt. |

**Controlepunt.** Laat een student vóór een codewijziging de drie ontwerpvragen beantwoorden. De muntvraag is nog geen opdracht om twee keuzes recursief uit te schrijven.

## Practicum — een directory doorzoeken

Doel: de recursieve stap op de gegeven representatie toepassen

Gebruik [10_directory_doorzoeken, stappen 1–5](../source/practicals/10_directory_doorzoeken.ipynb).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Laat in de dictionaryrepresentatie één bestand en één subdirectory aanwijzen; vraag wat bij een subdirectory opnieuw moet gebeuren. | Student onderscheidt een bestandsgrootte van een volgende directory. |
| 20 | Laat stap 1, `count_files`, plannen en testen. Vraag het aantal uit een subdirectory als deelresultaat te behandelen. | Student telt bestanden en combineert resultaten uit subdirectories. |
| 20 | Laat stap 2, `total_size`, maken. Vraag wat verandert ten opzichte van het tellen en wat gelijk blijft. | Student kan de verzamelwaarde en het teruggeeftype benoemen. |
| 20 | Laat stappen 3–4, `safe_name` en `unsafe_names`, maken. Controleer eerst het naamcriterium voordat de recursie wordt uitgebreid. | Student scheidt de test op één naam van het verzamelen door de directory. |
| 15 | Laat stap 5, `depth`, plannen. Laat een leeg geval en één geneste directory met de gegeven tests vergelijken. | Student kiest een dieptecombinatie in plaats van bestanden op te tellen. |
| 5 | Laat per functie de teststatus en de eerstvolgende reparatie vastleggen. | Onvoltooid werk heeft een benoemde stap en controlegeval. |

**Controlepunt.** Laat bij een falende test de eerstvolgende recursieve aanroep als een al opgelost deelprobleem beschrijven: wat zou die moeten teruggeven en wat doet de aanroeper daarmee?

## Huiswerk en begeleiding

De basis is verplicht. De opstap en de extra zijn facultatief. Studenten vinden de drie niveaus via de
[opgaven](../source/course/opgaven_10.md) en de
[uitwerkingen](../source/course/solutions_10.md). De aanvullende oefeningen zijn facultatief
en bevatten hun eigen uitwerkingen.

Gebruik bij [de opstap](../source/problems/10_opstap.ipynb) eerst *Lezen en naspelen*
en daarna *Schrijven*. Laat wie veel code probeert eerst één leesvraag uitwerken
met frames. [De basis over Scrabble](../source/problems/10_basis.ipynb) verbindt
letterscores met recursieve functies en woordenlijsten; begeleid door naar het
teruggeeftype van de vastgelopen functie te vragen. [Potjeslatijn](../source/problems/10_extra.ipynb)
en [de aanvullende recursieoefeningen](../source/extra/practice/1_recursie.ipynb) zijn
facultatief. Haal geen oude opdrachten terug uit historische handleidingen.

## Voorkennis, nieuwe begrippen en vervolg

Voorkennis: PGM1-functies, frames en `return`, dictionaries uit week 1 en een
som over een lijst uit week 2. Nieuw: recursieve aanroep, basisgeval en recursief
geval. De aflevering is één recursief probleem kunnen ontwerpen; week 4 voegt
het onderzoeken van twee keuzes toe. Laat deze week nog geen use it or lose it
schrijven.

## Verwachte vastloopmomenten

Dit zijn verwachtingen om tijdens de les te toetsen, geen gerapporteerde
ervaringen met deze PGM2-lessen.

| Signaal bij de student | Kleine docentinterventie |
|---|---|
| Student volgt de afdaling en stopt bij het basisgeval. | Laat terugkeerwaarden op de wachtende frames schrijven en de trace teruglopen. |
| Student krijgt geen bruikbaar resultaat omdat `return` ontbreekt. | Vraag welke waarde de aanroeper ontvangt en laat de betreffende teruggeefplek aanwijzen. |
| Student roept zichzelf met hetzelfde probleem aan. | Leg de twee argumenten naast elkaar en vraag wat aantoonbaar kleiner wordt. |
| Student telt waar een string of een grootste waarde nodig is. | Laat eerst het verwachte teruggeeftype noemen en pas daarna de combinatie kiezen. |

## Als de route niet afkomt

Bij tijdgebrek bespreek je minder vergelijkbare collegevoorbeelden volledig;
bewaar één complete trace met terugkeer en één zelfstandig ontwerp. Extra’s
blijven liggen. Noteer onvoltooide practicumstappen als vervolg en laat de basis
niet verdwijnen. Bij ontbrekende voorbereiding speel je eerst het bestaande
kleine faculteitvoorbeeld samen na. Laat de student daarna bij dezelfde drie
ontwerpvragen aansluiten; geef geen compleet recursierecept zonder dat hij de
terugkeer kan verklaren.

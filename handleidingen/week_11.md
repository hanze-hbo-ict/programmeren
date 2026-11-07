# Docentenhandleiding PGM2 week 4 — Functies van functies (cursusweek 11)

Recursie volgt nu twee mogelijkheden: een element gebruiken of laten liggen.
Daarna wordt de vraag hoe je het beste antwoord kiest verbonden met een functie
als argument. Behandel die twee lijnen beide; alleen een werkende knapzak is
geen bewijs dat een student ook een functie kan meegeven. Het practicum maakt
het verschil tussen een eerste oplossing en de beste oplossing zichtbaar.

## De week in één oogopslag

| Bijeenkomst | Product om op te controleren |
|---|---|
| College 1 — use it or lose it | Beide keuzes en hun vervolgproblemen aanwijzen. |
| College 2 — functie als argument | Een functie meegeven onderscheiden van haar aanroepen. |
| Practicum — wisselgeld | Een mogelijke oplossing van het minimum onderscheiden. |

Elke bijeenkomst duurt netto 90 minuten. De blokken hieronder zijn
ontwerpinschattingen, geen gemeten behandeltijden of garantie dat iedereen klaar
komt. Pauzes vallen buiten deze 90 minuten. De volgorde is die van dit lesplan;
de opgaven onder `problems/` blijven huiswerk.

## Voorbereiding en middelen

Bronstatus: gecontroleerd tegen `adfdc5c8` van `origin/master`; verwijzingen bijgewerkt na de samenvoeging van week 4. De actuele
[weekpagina](../source/course/week_11.md) geeft de studentroute. Open de
collegenotebooks, voer je eigen demonstraties vooraf uit en houd de hieronder
genoemde uitwerkingen bij de hand voor je begeleiding. Gebruik een werkende
Python-/editor-/notebookomgeving en papier of bord voor voorspellingen. Vraag
eerst iedereen iets op te schrijven voordat je antwoorden uit de groep ophaalt.

Open [wisselgeld](../source/practicals/11_wisselgeld.ipynb) en de gegeven
muntvoorraad en onmogelijke gevallen. Houd de uitwerkingen van
[wisselgeld](../source/solutions/11_wisselgeld.ipynb), [opstap](../source/solutions/11_opstap.ipynb) en
[de basis](../source/solutions/11_basis.ipynb) klaar. Zet twee kolommen op
het bord: gebruiken en laten liggen. Daarin moet per tak het kleinere probleem
zichtbaar blijven.

## College 1 — twee keuzes onderzoeken

Doel: beide recursieve takken plannen en hun resultaten combineren

Gebruik [11a, *Precies betalen*, *De knapzak* en de twee opdrachten](../source/lectures/11a_use_it_or_lose_it.ipynb).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Haal de muntvraag uit week 3 op. Laat ieder eerst opschrijven wat met de eerste munt kan gebeuren. | Student onderscheidt gebruiken en laten liggen. |
| 30 | Werk `exact_change` door met twee bordkolommen. Laat duo’s per tak bedrag en overgebleven munten aanwijzen voordat je code uitvoert. | Student gebruikt dezelfde munt niet opnieuw in een vervolgprobleem. |
| 25 | Laat bij de knapzak eerst beide kandidaten beschrijven. Vergelijk daarna met *Probeer beide en kies de beste*. | Student onderzoekt beide keuzes en kan de selectie van het beste resultaat uitleggen. |
| 20 | Laat de bestaande opdrachten `count_ways` en `most_items` in duo’s plannen. Vraag wat de twee takken teruggeven. | Student kiest de combinatie vanuit de vraag: tellen of het beste aantal. |
| 5 | Vraag ieder één tak en de combinatie in woorden te noteren. | Student noemt het kleinere probleem en de betekenis van het resultaat. |

**Controlepunt.** Laat per tak de resterende invoer aanwijzen. Vraag daarna waarom één geslaagde tak bij een optimalisatievraag nog niet genoeg is.

## College 2 — een functie meegeven

Doel: een benoemde functie en een lambda-functie op dezelfde plek gebruiken

Gebruik [11b, *Een functie meegeven met key=*, *lambda*, *Zelf een functie met een functieparameter*, *Terug naar de knapzak* en *Opdrachten*](../source/lectures/11b_functie_als_argument.ipynb).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Open het sorteerprobleem en herinner aan de gemarkeerde `key=`-vooruitblik uit week 2. Laat opschrijven waarop moet worden vergeleken. | Student onderscheidt een object van de vergelijkingswaarde. |
| 25 | Laat bij `key=` eerst een benoemde functie meegeven. Vraag wie die functie aanroept en met welk argument. | Student geeft de functie zelf mee en voert haar niet voortijdig uit. |
| 20 | Zet dezelfde kleine functie naast haar lambda-vorm. Laat duo’s parameter en teruggegeven expressie aanwijzen. | Student verklaart dezelfde berekening in beide vormen. |
| 20 | Volg de eigen functieparameter en keer terug naar `subset_items` bij de knapzak. Vraag welke taak de meegegeven functie verricht. | Student kan zeggen waar de functie wordt aangeroepen en hoe de beste kandidaat wordt gekozen. |
| 10 | Laat de twee collegeopdrachten, afspeellijst sorteren en `count_matching`, zelfstandig starten; bespreek één keuze voor een functie. | Student kiest een functie passend bij de gevraagde bewerking. |
| 5 | Laat een aanroep met functieargument verklaren zonder hem uit te voeren. | Student onderscheidt meegeven en aanroepen. |

**Controlepunt.** Wijs bij een voortijdige aanroep naar de haakjes: wordt hier een functie meegegeven of al haar resultaat? Laat de student de aanroepende plek aanwijzen.

## Korte antwoorden bij collegeopdrachten

### 11a

| Opdracht | Antwoordkern |
|---|---|
| Opdracht 1 — `count_ways` | Bedrag `0` geeft `1`, negatief bedrag of geen munten geeft `0`; tel anders `count_ways(amount - coins[0], coins[1:])` en `count_ways(amount, coins[1:])` op. |
| Opdracht 2 — `most_items` | Geen items geeft `0`; sla een te zwaar eerste item over, kies anders het maximum van `1 + most_items(capacity - items[0], items[1:])` en `most_items(capacity, items[1:])`. |

### 11b

| Opdracht | Antwoordkern |
|---|---|
| Opdracht 1 | Gebruik `max(songs, key=lambda song: song[1])`, `sorted(songs, key=lambda song: song[1])` en `max(songs, key=lambda song: len(song[0]))` voor respectievelijk a, b en c. |
| Opdracht 2 — `count_matching` | De functie geeft `len([x for x in L if test(x)])` terug: roep de meegegeven functie voor elk element aan. |

## Practicum — wisselgeld

Doel: de eerste werkende muntkeuze onderscheiden van het kleinste aantal

Gebruik [11_wisselgeld, stappen 1–2](../source/practicals/11_wisselgeld.ipynb).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Laat de gegeven muntvoorraad, het nulbedrag en een onmogelijk geval lezen. Vraag wat de functie voor elk soort geval moet betekenen. | Student verwart geen munten nodig hebben niet met niet kunnen betalen. |
| 30 | Begeleid stap 1, `num_coins`. Laat eerst één tak volledig naspelen en daarna de bestaande tests gebruiken. | Student kan aanwijzen dat de eerste gevonden mogelijkheid niet noodzakelijk de beste is. |
| 35 | Laat stap 2, `min_coins`, maken. Vraag beide deelresultaten naast elkaar te zetten voordat het minimum wordt gekozen. | Student behandelt onmogelijke takken afzonderlijk en vergelijkt de bruikbare mogelijkheden. |
| 10 | Bespreek tests voor onmogelijke gevallen en het verschil tussen beide functies. | Student verklaart waarom een onmogelijke uitkomst geen gewone nul is. |
| 5 | Laat teststatus en een open geval noteren. | De vervolgstap is een benoemd geval, geen ongerichte herschrijving. |

**Controlepunt.** Gebruik de bestaande tests om een onmogelijke tak van bedrag nul te onderscheiden. Voeg geen dynamisch programmeren of memoization toe; het doel is het tweekeuzenontwerp.

## Huiswerk en begeleiding

Verdeel [de opstap](../source/problems/11_opstap.ipynb) in naspelen, lezen en
schrijven. [De basis](../source/problems/11_basis.ipynb) heeft twee delen: geef na
college 1 *De nacht van het nijlpaard* (stappen 1–3) en na college 2 *De uitslag van
de schoolrun* (stappen 4–8 en opdracht 1) mee. Vraag bij het nijlpaard naar de keuze
en het resterende probleem; vraag bij de schoolrun welke functie aan `select` of
`winner` wordt meegegeven. [De extra](../source/problems/11_extra.ipynb) is verdieping
en bevat *Pijlenpad*, *Periodiek T-shirt* en *Caesar op orde*. De uitwerkingen van alle
drie staan in [één extra-uitwerking](../source/solutions/11_extra.ipynb).

## Voorkennis, nieuwe begrippen en vervolg

Voorkennis: recursie, collecties en functieaanroepen. Nieuw: twee keuzes
recursief onderzoeken, een functie als argument meegeven en lambda-functies.
De student levert zelfstandig gecombineerde functies af. Week 5 gebruikt de
methodeaanroep uit week 1, maar begint eigen klassen opnieuw; geef deze week
geen OOP vooruit.

## Verwachte vastloopmomenten

Dit zijn verwachtingen om tijdens de les te toetsen, geen gerapporteerde
ervaringen met deze PGM2-lessen.

| Signaal bij de student | Kleine docentinterventie |
|---|---|
| De eerste munt blijft in beide vervolgproblemen beschikbaar. | Laat per tak de overgebleven lijst aanwijzen voordat je de berekening verder volgt. |
| Student gebruikt nul voor een onmogelijk geval. | Leg de bestaande test voor bedrag nul naast een onmogelijke betaling en vraag waarom de betekenis verschilt. |
| Student schrijft `key=f()` en geeft zo een resultaat mee. | Vraag wie de functie later moet aanroepen en laat de functie zonder aanroephaakjes aanwijzen. |

## Als de route niet afkomt

Bij tijdgebrek behoud je één goede trace van beide takken en één diagnose van
functie meegeven. Verkort vergelijkbare besprekingen en stel de extra uit; beide
basisdelen blijven huiswerk. Leg onvoltooide practicumtests vast. Bij ontbrekende
recursievoorbereiding speel je één bestaand klein geval uit het college samen na,
inclusief terugkeer, en laat de student daarna het duo-ontwerp hervatten. Herhaal
niet de volledige vorige week binnen deze bijeenkomst.

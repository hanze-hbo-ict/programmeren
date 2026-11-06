# Docentenhandleiding PGM2 week 6 — Klassen uitbreiden (cursusweek 13)

Dezelfde aanroep krijgt deze week ander gedrag afhankelijk van het object.
Overerving kan gedeeld gedrag bewaren, maar is geen automatische keuze voor
alles wat samenwerkt. Laat bij duck typing steeds vragen welke handelingen er
werkelijk nodig zijn. Het creatures-practicum maakt die grens zichtbaar met een
wachttoren die wel meevecht maar niet alle vragen van een party beantwoordt.

## De week in één oogopslag

| Bijeenkomst | Product om op te controleren |
|---|---|
| College 1 — overerving | Een constructor en overschreven methode kunnen volgen. |
| College 2 — polymorfisme en duck typing | Gedrag verklaren en overerving van compositie onderscheiden. |
| Practicum — soorten wezens | Gemengde strijders in een begrensd gevecht gebruiken. |

Elke bijeenkomst duurt netto 90 minuten. De blokken hieronder zijn
ontwerpinschattingen, geen gemeten behandeltijden of garantie dat iedereen klaar
komt. Pauzes vallen buiten deze 90 minuten. De volgorde is die van dit lesplan;
de opgaven onder `problems/` blijven huiswerk.

## Voorbereiding en middelen

Bronstatus: gecontroleerd tegen `adfdc5c8` van `origin/master`; route bijgewerkt volgens [C4 van #481](https://github.com/hanze-hbo-ict/programmeren/issues/481#issuecomment-6685696981). De actuele
[weekpagina](../source/course/week_13.md) geeft de studentroute. Open de
collegenotebooks, voer je eigen demonstraties vooraf uit en houd de hieronder
genoemde uitwerkingen bij de hand voor je begeleiding. Gebruik een werkende
Python-/editor-/notebookomgeving en papier of bord voor voorspellingen. Vraag
eerst iedereen iets op te schrijven voordat je antwoorden uit de groep ophaalt.

Open [13_creatures](../source/practicals/13_creatures.md) op *Waar je begint*.
Controleer dat [de uitwerking van week 5](../source/solutions/12_creatures.ipynb)
beschikbaar is. Wie zijn eigen week-5-code niet af heeft, neemt de klassen en
assertions in dezelfde volgorde daaruit over in `creatures.py`; de cel die met
opzet een foutmelding geeft wordt niet gekopieerd. Laat de beginstand uitvoeren
voordat iemand nieuwe subklassen toevoegt. Houd de uitwerkingen van
[creatures week 6](../source/solutions/13_creatures.ipynb),
[opstap](../source/solutions/13_opstap.ipynb), [kassabon](../source/solutions/13_basis.ipynb)
en [spelers](../source/solutions/13_extra.ipynb) voor begeleiding gereed.
Controleer ook dat uitwerking 13 vóór practicum week 7 voor studenten beschikbaar
zal zijn. De actuele studentstappen gaan vóór de historische code in de
[OOP-opzet](../curriculum/practicum-oop.md).

## College 1 — overerving

Doel: gedeelde staat behouden terwijl gedrag wordt uitgebreid

Gebruik [13a, *Een subklasse*, *Een methode overschrijven*, *De constructor uitbreiden*, *Een standaardwaarde voor een parameter* en *Opdrachten*](../source/lectures/13a_overerving.ipynb).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Haal `Student` op en vraag wat een deeltijdstudent deelt en wat verschilt. | Student benoemt gedeelde staat en specifiek gedrag apart. |
| 25 | Introduceer de subklasse en laat een bestaande overschreven methode volgen. Laat duo’s voorspellen welke versie wordt aangeroepen. | Student onderscheidt geërfd en overschreven gedrag. |
| 20 | Volg de constructor met `super()`. Gebruik ook *Als super().__init__ ontbreekt*: vraag waar het ontbrekende attribuut had moeten ontstaan. | Student verbindt de staat aan de juiste constructor. |
| 15 | Laat een standaardwaarde voor een parameter met en zonder expliciet argument gebruiken. | Student kan uitleggen welke waarde wordt gebruikt bij weglaten. |
| 15 | Laat collegeopdrachten zelfstandig starten en vraag bij de bespreking naar de soortrelatie. | Student motiveert waarom de nieuwe klasse een subklasse is. |
| 5 | Laat de constructorvolgorde individueel in woorden noteren. | Student weet welke initialisatie moet behouden blijven. |

**Controlepunt.** Vraag wat er ontbreekt als de superklasseconstructor niet wordt aangeroepen. Los niet alleen de foutmelding op; laat aanwijzen welk object welk attribuut nodig heeft.

## College 2 — één aanroep, ander gedrag

Doel: polymorfisme en de grens van duck typing verklaren

Gebruik [13b, *Eén aanroep, ander gedrag*, *Duck typing*, *Wat duck typing niet belooft*, *Van welke klasse is een object?* en *Overerving of compositie*](../source/lectures/13b_polymorfisme.ipynb).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Haal twee objecten met verschillend gedrag op. Laat eerst hun gemeenschappelijke aanroep opschrijven. | Student ziet dezelfde handeling zonder aparte aanroep per soort. |
| 25 | Volg *De studiegroep hoeft niets te weten*. Laat duo’s voorspellen wat de groepscode per object aanroept. | Student verklaart het verschil vanuit het object, zonder typevertakking in de groepslus. |
| 20 | Gebruik duck typing en de begrenzing ervan. Laat aanwijzen welke methode in een gegeven gebruik wel of niet nodig is. | Student verbindt geschiktheid aan de gebruikte handelingen. |
| 15 | Laat `self.__class__.__name__` en `isinstance` in de bestaande voorbeelden lezen. Vraag hoe een typecontrole de toegelaten objecten verandert. | Student onderscheidt een klasse opvragen van op gedrag vertrouwen. |
| 15 | Laat overerving of compositie kiezen bij de bestaande opdrachten. Vraag eerst: is dit een soort, of heeft dit iets als onderdeel? | De keuze volgt de betekenis van het domein. |
| 5 | Vraag één individuele keuze met onderbouwing en één beperking van duck typing. | Student claimt geen algemene uitwisselbaarheid. |

**Controlepunt.** Laat een student zeggen voor welke concrete handeling het object geschikt is. Een algemene uitspraak dat twee objecten “hetzelfde kunnen” is onvoldoende.

## Practicum — soorten wezens

Doel: voortbouwen op de beginstand en de duck-typinggrens testen

Gebruik [13_creatures, stappen 1–8 en *Wat duck typing niet belooft*](../source/practicals/13_creatures.md).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Controleer eigen week-5-code of de overgenomen beginstand. Laat de bestaande assertions uitvoeren. | Student begint met een complete werkende basis; de opzettelijk falende cel ontbreekt. |
| 20 | Laat stappen 1–2 maken: `special_move`, soorten en de klassenaam in `__repr__`. | Student kan bij een aanroep de gekozen versie aanwijzen. |
| 20 | Laat stappen 3–5 maken: gemengde aanroepen, `Beast`, `Dragon` en `Wolf`. Vraag waar gedeeld gedrag nu leeft. | Student onderscheidt gedeeld gedrag en een eigen overschrijving. |
| 20 | Laat stappen 6–7 maken: `Turret` en `battle_round`. Vraag welke methoden de gewone gevechtsfunctie van haar argumenten gebruikt. | Student laat de toren meedoen zonder er een `Creature` van te maken. |
| 15 | Laat stap 8, `battle`, bouwen of gericht starten. Bewaak eerste levende doelwit en maximaal aantal rondes; bespreek de grens met `heal_all`. | Student kan de eindconditie aanwijzen en noemt waarom meedoen aan `battle` niet alle party-methoden belooft. |
| 5 | Laat open stappen en teststatus vastleggen en de route voor week 7 aanwijzen. | Student weet welke beginstand en assertions de volgende keer nodig zijn. |

**Controlepunt.** Bewaar de assertions van week 5 en voeg die van week 6 toe. `special_move` van `Creature` valt deze week nog stil terug op een gewone aanval. Gebruik `battle(side_a, side_b, max_rounds)` met vaste doelkeuze; stel exceptions uit tot week 7.

## Huiswerk en begeleiding

De opstap en de basis zijn verplicht. De extra is facultatief. Studenten vinden de drie niveaus via de
[opgaven](../source/course/opgaven_13.md) en de
[uitwerkingen](../source/course/solutions_13.md).

Gebruik [de opstap](../source/problems/13_opstap.ipynb) voor overerving,
standaardwaarden en introspectie. [De basis over een kassabon](../source/problems/13_basis.ipynb)
laat soorten producten en een `Receipt` samenwerken. Vraag bij een fout welke
klasse de prijs moet leveren en welke klasse de producten bewaart; zo blijft
het onderscheid tussen overerving en compositie zichtbaar.
[De spelers-extra](../source/problems/13_extra.md) bouwt facultatief op `Board` van
week 5 voort. Laat die route alleen kiezen als de basis ruimte overlaat; zij is
geen verplichte voorbereiding voor het creatures-practicum.

## Voorkennis, nieuwe begrippen en vervolg

Voorkennis: klassen, objecten, encapsulatie, compositie en de creatures-eindstand
van week 5. Nieuw: overerving, overschrijven, standaardwaarden, polymorfisme,
duck typing en introspectie. De aflevering naar week 7 bestaat uit soorten
wezens, `Turret`, gevechtsfuncties en de assertions van beide weken. `battle_round`
krijgt geen `isinstance`-controle; de beperkte belofte van duck typing moet
zichtbaar blijven.

## Verwachte vastloopmomenten

Dit zijn verwachtingen om tijdens de les te toetsen, geen gerapporteerde
ervaringen met deze PGM2-lessen.

| Signaal bij de student | Kleine docentinterventie |
|---|---|
| Een subklasse mist een attribuut na het maken van een object. | Laat aanwijzen waar dat attribuut ontstaat en volg daarna de ontbrekende `super().__init__`-aanroep. |
| Student splitst de groepslus per soort met `isinstance` uit. | Laat dezelfde methodeaanroep op twee bestaande objecten voorspellen en vraag welk object het gedrag kiest. |
| Student verwacht dat `Turret` overal een `Creature` kan vervangen. | Open *Wat duck typing niet belooft* en laat de methode die ontbreekt bij de gekozen party-handeling aanwijzen. |
| Student laat `Party` van `Creature` erven. | Vraag of een party een soort wezen is of wezens als onderdeel heeft, en laat het bestaande ontwerp ermee vergelijken. |

## Als de route niet afkomt

Bij tijdgebrek stel je de extra uit en noteer je onvoltooide verplichte
practicumstappen. De gevechtslimiet blijft nodig, ook als de bespreking korter
wordt. Bij ontbrekende beginstand reconstrueert de student week 5 uit
[uitwerking 12](../source/solutions/12_creatures.ipynb), zonder de opzettelijk falende
cel. Laat de bestaande assertions de start controleren. Voor week 7 staat
[uitwerking 13](../source/solutions/13_creatures.ipynb) tijdig beschikbaar. Gebruik
die route voor onaf werk; verwijs niet naar verwijderde assets-downloads.

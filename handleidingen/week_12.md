# Docentenhandleiding PGM2 week 5 — Klassen en objecten (cursusweek 12)

Een dictionary bewaart gegevens; een eigen object krijgt ook handelingen die
bij die gegevens horen. Laat de student steeds aanwijzen welk object verandert
en welke regel die verandering bewaakt. Het practicum begint met een leeg
bestand. `Creature` en `Party` groeien vanaf hier drie weken door; de kalender
in de basis is een afzonderlijke toepassing.

## De week in één oogopslag

| Bijeenkomst | Product om op te controleren |
|---|---|
| College 1 — objecten ontwerpen | Eigen staat van een object en het gedeelde klasseontwerp aanwijzen. |
| College 2 — Date, waarde en identiteit | Een kopie onderscheiden van een tweede naam voor hetzelfde object. |
| Practicum — creatures beginnen | Creature en Party met de bestaande assertions opbouwen. |

Elke bijeenkomst duurt netto 90 minuten. De blokken hieronder zijn
ontwerpinschattingen, geen gemeten behandeltijden of garantie dat iedereen klaar
komt. Pauzes vallen buiten deze 90 minuten. De volgorde is die van dit lesplan;
de opgaven onder `problems/` blijven huiswerk.

## Voorbereiding en middelen

Bronstatus: gecontroleerd tegen `adfdc5c8` van `origin/master`. De actuele
[weekpagina](../source/course/week_12.md) geeft de studentroute. Open de
collegenotebooks, voer je eigen demonstraties vooraf uit en houd de hieronder
genoemde uitwerkingen bij de hand voor je begeleiding. Gebruik een werkende
Python-/editor-/notebookomgeving en papier of bord voor voorspellingen. Vraag
eerst iedereen iets op te schrijven voordat je antwoorden uit de groep ophaalt.

Open [het practicum](../source/practicals/12_creatures.md) en begin voor de
demonstratie met een leeg `creatures.py`. Houd de uitwerkingen van
[creatures](../source/solutions/12_creatures.ipynb), [opstap](../source/solutions/12_opstap.ipynb),
[Date](../source/solutions/12_basis.ipynb) en [Board](../source/solutions/12_extra.ipynb)
klaar. Controleer vóór het practicum van week 6 dat de creatures-uitwerking voor
studenten beschikbaar is: zij is de vastgestelde beginstandroute, geen optionele
extra voorziening. Gebruik de actuele studentpagina en de
[besluiten vóór de historische sessieopzet](../curriculum/practicum-oop.md)
voor de inhoudelijke grenzen.

## College 1 — eigen objecten

Doel: klasse, object en encapsulatie aan concrete handelingen verbinden

Gebruik [12a, *Data*, *Een klasse Student ontwerpen*, *Encapsulatie*, *Compositie* en *Opdrachten*](../source/lectures/12a_objecten.ipynb).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Haal de dictionary met studentgegevens op. Laat studenten benoemen welke handelingen bij die data horen. | Student formuleert gedrag naast losse opgeslagen waarden. |
| 25 | Bouw de bestaande `Student` op. Laat twee objecten tekenen en de constructor en een methodeaanroep volgen. | Student wijst de eigen attributen van elk object en het gedeelde klasseontwerp aan. |
| 25 | Behandel *Encapsulatie* en het afschermen van een attribuut. Laat de publieke toegang en de property aanwijzen. | Student kan vertellen welke toegang de klasse aanbiedt en welke staat intern wordt bewaard. |
| 20 | Gebruik *Compositie* en de collegeopdrachten. Laat duo’s aanwijzen welk object een ander object als onderdeel heeft. | Student vraagt het onderdeel om gedrag in plaats van zelf diens interne staat te bewerken. |
| 10 | Laat ieder bij één object aanwijzen waar staat ontstaat en door welke handeling die verandert. | Student onderscheidt klasse, object, attribuut en methode. |

**Controlepunt.** Vraag bij een wijziging: welk object is hier `self`? Laat de student dat object in de tekening aanwijzen voordat je de volgende regel bespreekt.

## College 2 — Date, waarde en identiteit

Doel: de betekenis van self, kopiëren en verwijzingen volgen

Gebruik [12b, *Stap voor stap*, *f"strings"*, *Quiz*, *Waarde en identiteit* en *Identiteit bij compositie*](../source/lectures/12b_data_object.ipynb).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Haal constructor en methode op; laat een bestaande aanroep in woorden uitleggen. | Student koppelt de aanroep aan één object. |
| 30 | Volg de bestaande `Date`-opbouw. Laat bij iedere methode eerst het object voor `self` aanwijzen en daarna de overige argumenten. | Student behandelt `self` niet als een extra los in te voeren object bij de gewone methodeaanroep. |
| 15 | Laat de f-string en quiz voorspellen, dan uitvoeren en bespreken. Haal eenvoudige interpolatie op en laat de bestaande datumweergave lezen. | Student herkent de ingevoegde waarden en kan de bestaande weergave lezen. |
| 25 | Laat bij *Waarde en identiteit* twee namen en een kopie tekenen. Gebruik daarna *Identiteit bij compositie* en de opdracht. | Student kan voorspellen welke verwijzing een verandering zichtbaar maakt. |
| 10 | Vraag individueel of een bestaande vergelijking waarde of identiteit onderzoekt en laat de keuze toelichten. | Student maakt een onderscheid tussen hetzelfde object en dezelfde waarde. |

**Controlepunt.** Eenvoudige f-stringinterpolatie is PGM1-voorkennis. Maak de bestaande opmaak leesbaar, maar voeg geen zelfstandig opmaakleerdoel toe. Bewaar tijd voor de verwijzingsvraag.

## Practicum — Creature en Party

Doel: het project vanuit een leeg bestand opbouwen

Gebruik [12_creatures, stappen 1–5 en *Wat de property van hp verandert*](../source/practicals/12_creatures.md).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Laat een leeg `creatures.py` openen en de vijf stappen bekijken. Spreek af de assertions onder de klassen te bewaren. | Student start met eigen bouw en weet waar de controles komen. |
| 20 | Begeleid stap 1, `Creature`. Vraag waar de constructor de staat vastlegt en wat `__repr__` voor de controle zichtbaar maakt. | Student maakt twee afzonderlijke objecten en voert de bestaande assertions uit. |
| 15 | Laat stap 2, hp veranderen en ernaar vragen, maken. Vraag welke vraag of actie aan het object wordt gesteld. | Student gebruikt gedrag voor schade en genezing. |
| 15 | Laat stap 3, properties, uitvoeren. Bespreek het verschil tussen directe hp-toewijzing en schade na verdediging. | Student wijst aan welke grens de setter bewaakt en welke domeinregel bij `take_damage` hoort. |
| 15 | Laat stap 4, aanvallen en groeien, maken. Vraag voor iedere aanroep welk object verandert. | Student kan aanvaller en doelwit onderscheiden en test de stap. |
| 10 | Start stap 5, `Party`. Laat aanwijzen welke objecten de party bewaart en via welke methoden zij worden gebruikt. | Student herkent compositie; onvoltooide functies worden expliciet genoteerd. |
| 5 | Laat teststatus per stap vastleggen en de beginstandroute voor week 6 openen. | Student weet welke eigen code nog af moet en waar de bestaande uitwerking staat. |

**Controlepunt.** Een geteste stap is het lokale checkpoint, geen garantie dat alle vijf stappen binnen het practicum afkomen. Bewaar de verplichting tot het vervolg en de route naar een complete beginstand.

## Huiswerk en begeleiding

De opstap en de basis zijn verplicht. De extra is facultatief. Studenten vinden de drie niveaus via de
[opgaven](../source/course/opgaven_12.md) en de
[uitwerkingen](../source/course/solutions_12.md).

Laat [de opstap over klassen](../source/problems/12_opstap.ipynb) gebruiken om
constructor, methoden en properties afzonderlijk te oefenen. De verplichte
[basis over Date](../source/problems/12_basis.ipynb) loopt door tot en met het afschermen
van de datum in stap 13. Laat bij begeleiding eerst een test naar een concrete
methode herleiden; laat kopiëren en waarde/identiteit niet ondersneeuwen onder de
kalenderberekening. [Board](../source/problems/12_extra.md) is facultatief en begint de
extra-lijn voor de komende weken. Die extra is geen beginstand voor creatures.

## Voorkennis, nieuwe begrippen en vervolg

Voorkennis: functies, methodeaanroepen uit week 1, mutatie en dictionaries.
Nieuw: eigen klassen, `self`, constructor, magische methoden zoals `__repr__`,
waarde en identiteit, encapsulatie, properties en compositie. De aflevering naar
week 6 is `Creature`, `Party` en de bijbehorende assertions. Voeg nu geen
overerving, standaardparameter voor `Party` of exceptions toe.

## Verwachte vastloopmomenten

Dit zijn verwachtingen om tijdens de les te toetsen, geen gerapporteerde
ervaringen met deze PGM2-lessen.

| Signaal bij de student | Kleine docentinterventie |
|---|---|
| Student verandert de klasse waar één object bedoeld wordt. | Laat twee bestaande objecten tekenen en vraag bij welk exemplaar de staat hoort. |
| Student wil `self` als extra argument meegeven. | Schrijf één bestaande methodeaanroep uit en laat het object links van de punt aanwijzen. |
| Student noemt een tweede naam een kopie. | Laat vóór uitvoeren de verwijzingen tekenen en voorspellen waar de wijziging zichtbaar wordt. |
| Student verwart de publieke property met het private attribuut. | Laat de publieke toegang en interne opslag naast elkaar aanwijzen; vraag welke methode de grens bewaakt. |

## Als de route niet afkomt

Bij tijdgebrek markeer je onvoltooide verplichte practicumstappen als vervolg;
vervang de basis niet door Board. Wie de voorbereiding mist, bouwt eerst samen
met jou één `Creature` en vervolgt daarna zelfstandig de actuele stappen.
Wie week 5 niet af heeft, gebruikt vóór practicum week 6 de
[uitwerking van week 5](../source/solutions/12_creatures.ipynb): klassen en assertions
in dezelfde volgorde overnemen in `creatures.py`, de opzettelijk falende cel
niet kopiëren. Laat daarna het bestand uitvoeren. Bied geen verdwenen losse
assets-download aan. Noteer eigen onaf werk afzonderlijk, zodat de complete
beginstand de resterende leervraag niet onzichtbaar maakt.

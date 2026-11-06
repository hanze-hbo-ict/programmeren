# Docentenhandleiding PGM2 week 7 — Fouten afhandelen (cursusweek 14)

De student geeft eigen objecten nu betekenis voor operatoren en maakt fouten
zichtbaar waar ze ontstaan. Houd gooien en afvangen uit elkaar: creatures gooit,
de Date-basis oefent het afhandelen. Deze week heeft één college; de derde
bijeenkomst is het oefententamen. Dat verandert de hoeveelheid klassikale uitleg,
maar vervangt de basis niet.

## De week in één oogopslag

| Bijeenkomst | Product om op te controleren |
|---|---|
| College — operatoren en exceptions | Vergelijkingsgedrag en gooien/afvangen onderscheiden. |
| Practicum — creatures afronden | Operatoren en nieuwe foutgrenzen met passende assertions controleren. |
| Oefententamen | Zelfstandig oefenen en eigen vervolgvragen kiezen. |

Elke bijeenkomst duurt netto 90 minuten. De blokken hieronder zijn
ontwerpinschattingen, geen gemeten behandeltijden of garantie dat iedereen klaar
komt. Pauzes vallen buiten deze 90 minuten. De volgorde is die van dit lesplan;
de opgaven onder `problems/` blijven huiswerk.

## Voorbereiding en middelen

Bronstatus: route bijgewerkt volgens [C4 van #472](https://github.com/hanze-hbo-ict/programmeren/issues/472#issuecomment-6683936872), op basis van `c1fbba46` van `origin/master`, en volgens [C4 van #481](https://github.com/hanze-hbo-ict/programmeren/issues/481#issuecomment-6685696981). De actuele
[weekpagina](../source/course/week_14.md) geeft de studentroute. Open de
collegenotebooks, voer je eigen demonstraties vooraf uit en houd de hieronder
genoemde uitwerkingen bij de hand voor je begeleiding. Gebruik een werkende
Python-/editor-/notebookomgeving en papier of bord voor voorspellingen. Vraag
eerst iedereen iets op te schrijven voordat je antwoorden uit de groep ophaalt.

Controleer vóór het practicum dat [uitwerking 13](../source/solutions/13_creatures.ipynb)
voor studenten beschikbaar is. Wie week 6 niet af heeft, neemt `import random`,
de klassen, functies en assertions van week 5 en 6 in dezelfde volgorde over
naar `creatures.py`; de opzettelijk falende cel niet kopiëren. Houd
[uitwerking 14](../source/solutions/14_creatures.ipynb),
[de opstapuitwerking](../source/solutions/14_opstap.ipynb) en
[de Date-uitwerking](../source/solutions/14_basis.ipynb) gereed. Open ook de
[tentameninformatie](../source/course/pgm2_tentamen.md),
[het oefententamen](../source/extra/practice/PGM2_examen.md) en
[de bestaande uitwerking](../source/solutions/PGM2_examen.ipynb). De
[actuele OOP-besluiten](../curriculum/practicum-oop.md) gaan vóór de historische
voorbeeldcode: geen `NotImplemented` en geen eigen `__iadd__` op `Party` bouwen.

## College — operatoren en exceptions

Doel: operatorgedrag en het afhandelen van foutcondities onderscheiden

Gebruik [14a, operatoren, exceptions en de bijbehorende opdrachten](../source/lectures/14a_operatoren_en_exceptions.ipynb).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Haal `Date.equals` en het nog niet kunnen sorteren van wezens op. Laat studenten benoemen wat Python voor een vergelijking zou moeten weten. | Student koppelt de operator aan een betekenis van de klasse. |
| 25 | Volg `__eq__`, `__lt__`, sorteren en vergelijken met een ander type. Laat eerst voorspellen welke magische methode nodig is. | Student onderscheidt waarde en identiteit en herkent de typegrens. |
| 20 | Laat bij `raise` een foutgrens in de bestaande code aanwijzen. Vraag welke invoer wordt geweigerd en waarom verder rekenen niet passend is. | Student wijst de plek aan waar de exception ontstaat. |
| 20 | Volg `try`/`except` uit het college. Laat duo’s benoemen welke handeling bij geldige invoer en welke bij een fout plaatsvindt. | Student noemt een bruikbare afhandeling in plaats van alleen de melding weg te laten. |
| 10 | Behandel `NotImplementedError` en laat de bestaande opdrachten gericht starten. Vraag welke klasse haar eigen gedrag moet leveren. | Student onderscheidt een ontbrekende overschrijving van gewone ongeldige invoer. |
| 5 | Laat ieder gooien en afvangen aan twee concrete plekken aanwijzen. Verbind dat met practicum en basis. | Student weet dat de basis het afvangdeel bevat. |

**Controlepunt.** Vraag wie de fout constateert en wie ermee verder moet. Eén college moet beide kanten zichtbaar maken; plan geen tweede uitlegbijeenkomst achter het oefententamen.

## Practicum — operatoren en nieuwe foutgrenzen

Doel: de creatures-keten afronden zonder oude controles willekeurig weg te halen

Gebruik [14_creatures, *Waar je begint*, stappen 1–8 en *Wat duck typing niet belooft, opnieuw*](../source/practicals/14_creatures.md).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 10 | Laat de week-6-beginstand uitvoeren en aanwijzen welke assertions uit eerdere weken komen. | Klassen, functies en controles staan in dezelfde volgorde; de opzettelijk falende cel ontbreekt. |
| 20 | Laat stappen 1–3, kracht vergelijken en sorteren, maken. Vraag welke vergelijking Python omdraait bij `>` en `>=`. | Student verklaart vergelijking zonder voor elke operator een eigen methode toe te voegen. |
| 30 | Laat stappen 4–5 maken: constructor en `special_move` gooien nu. Open de vervangingsaanwijzingen naast de oude assertions. | Student wijzigt alleen de genoemde oude controles en behoudt controles voor geldig gedrag. |
| 15 | Laat stap 6 en de `Turret`-grens bekijken. Laat de student de setterkeuze noteren en tijdelijke foutdemonstraties weer verwijderen. | De gekozen hp-grens past bij de assertions; meedoen aan een gevecht belooft geen sorteerbaarheid. |
| 10 | Laat bij resterende tijd starten aan stappen 7–8: partijen optellen/aftrekken en wezens vermenigvuldigen. Laat verwijzingen tekenen vóór aftrekken en kopiëren. | Student onderscheidt identiteit, waarde en nieuwe wezens. |
| 5 | Laat teststatus, setterkeuze en resterende stappen noteren. | Student kan het verschil tussen een bedoelde foutdemonstratie en een defect uitleggen. |

**Controlepunt.** Volg voor vervallen assertions uitsluitend de actuele stappen 4–6. Bij een gooiende setter vervallen alleen de daar genoemde toewijzingscontroles. Het practicum gooit exceptions en vangt ze niet af; geef geen nieuw afvangwerk in creatures.

De kernroute is stappen 1–6 met de `Turret`-sorteergrens. Werk aan stappen 7–8
als er tijd over is; label deze stappen niet afzonderlijk als facultatief en
maak er geen verplichte thuisinhaalslag van. De reflectievragen over deze
slotoperatoren horen alleen bij studenten die dat deel hebben gemaakt.

## Oefententamen — zelfstandig oefenen

Doel: eigen begrip controleren en concrete vervolgvragen kiezen

Gebruik [het oefententamen](../source/extra/practice/PGM2_examen.md) en [de bestaande uitwerking](../source/solutions/PGM2_examen.ipynb).

| Minuten | Docenthandeling en werkvorm | Waarneembaar signaal |
|---:|---|---|
| 5 | Toon doel en vindplaatsen. Laat studenten een eigen startpunt kiezen en de uitwerking voorlopig dicht houden. | Iedere student kan de opgaven openen en begint aan eigen werk. |
| 70 | Laat zelfstandig oefenen. Loop rond, noteer vragen en vraag bij vastlopen welk begrip of welke tussenstap ontbreekt. | Er ontstaat eigen werk met gemarkeerde onzekerheden; de docent neemt het oplossen niet over. |
| 10 | Laat eigen antwoorden met de bestaande uitwerking vergelijken en verschillen als vragen markeren. | Student onderscheidt een gemist begrip van een uitvoeringsfout. |
| 5 | Laat ieder één vervolgoefening en één vraag kiezen; laat onaf werk meenemen. | Student heeft een concreet vervolg voor de eigen voorbereiding. |

**Controlepunt.** De 5/70/10/5 minuten zijn een voorgestelde werkvorm binnen deze bijeenkomst, geen nieuw toetsvoorschrift of claim over de volledige tentamenduur. Gebruik de bestaande tentameninformatie; voeg geen toetsvragen of antwoorden toe.

## Huiswerk en begeleiding

Studenten vinden de drie niveaus via de [opgaven](../source/course/opgaven_14.md)
en de [uitwerkingen](../source/course/solutions_14.md).

Geef [de opstap](../source/problems/14_opstap.ipynb) en
[de basis over Date met operatoren](../source/problems/14_basis.ipynb) mee. Bewaak
speciaal stappen 7–8, datums uit tekst inlezen met `try`/`except`: de constructor gooit
bij een ongeldige datum en de inleescode handelt dat af door ongeldige datums
te melden en over te slaan. Laat studenten bij begeleiding aanwijzen welke stap doorloopt na
een ongeldige invoer. Bespreek bij `+=` in Date ook stap 4, waarom `return self`
nodig is. Het oefententamen vervangt dit basiswerk niet.
[Min-max](../source/problems/14_extra.md) is facultatief vervolg op Board en de spelers;
de [uitwerking](../source/solutions/14_extra.ipynb) staat bij de overige uitwerkingen.

De opstap (tien opdrachten) en alle acht basisstappen blijven verplicht; min-max
blijft facultatief. Resterende collegeopdrachten, kernstappen van het practicum
en de bijbehorende reflectievragen zijn zichtbaar nawerk. Onvoltooide
oefententamenopgaven zijn eigen vervolgvoorbereiding. Circa acht uur zelfstudie
per week is het algemene planningsuitgangspunt, geen afzonderlijke begroting
voor W7. De C2-inschatting voor opstap/basis, college-nawerk en reflectie is
165–285 minuten, exclusief onafgemaakte kernstappen en toetsvoorbereiding.
Werkelijke studenttijd is niet beschikbaar; deze raming garandeert geen afronding.

## Voorkennis, nieuwe begrippen en vervolg

Voorkennis: `Date`, waarde en identiteit uit week 5, en klassen, introspectie en
creatures uit week 6. Nieuw: operator overloading en exceptions gooien, afvangen
en afhandelen. Er volgt geen nieuwe vakweek; laat studenten eigen oefenpunten
voor de voorbereiding benoemen zonder nieuwe toetsdekking te claimen. Voor de
facultatieve min-max-lijn zijn Board en spelers nodig; voor de basis niet.

## Verwachte vastloopmomenten

Dit zijn verwachtingen om tijdens de les te toetsen, geen gerapporteerde
ervaringen met deze PGM2-lessen.

| Signaal bij de student | Kleine docentinterventie |
|---|---|
| Bij `Party.__sub__` verdwijnen twee even sterke wezens. | Laat twee even sterke maar verschillende objecten aanwijzen en vraag of de opdracht waarde of identiteit bedoelt. |
| Student behandelt `+=` als gewone `+`. | Volg het bestaande Date-geval en laat de rol van `return self` bij mutatie verklaren. |
| Student noemt afvangen hetzelfde als een fout negeren. | Vraag welke bruikbare actie stap 8 van de basis na een ongeldige datum uitvoert. |
| Een oude assertion faalt na de nieuwe foutgrens. | Open exact de vervangingsaanwijzing in de practicumstap en laat uitleggen welk gedrag bewust is veranderd. |

## Als de route niet afkomt

Bij tijdgebrek blijven stappen 7–8 voor als er tijd over is; ze worden geen
verplicht huiswerk. Stel min-max en uitgebreide plenaire bespreking uit. Noteer
onvoltooide verplichte stappen, maar schrap het afvangdeel uit de basis niet.
Wie creatures niet af heeft, gebruikt [uitwerking 13](../source/solutions/13_creatures.ipynb)
volgens de kopieerinstructie hierboven, zonder de opzettelijk falende cel. Wie
Date mist, begint bij de bestaande klasse in de basis; maak geen losse
startdownload. Laat bij de afsluiting onderscheid maken tussen nog te bouwen
operatoren, een ontbrekend afvangdeel en tentamenvragen voor eigen oefening.

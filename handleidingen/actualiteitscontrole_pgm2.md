# Actualiteitscontrole PGM2-docentenhandleidingen

Controle voor [#486](https://github.com/hanze-hbo-ict/programmeren/issues/486),
7 november 2026. Meetbasis: `cd1c7f95006b15b56ba1a0c26caf5c121280162c`.
Doelgroep: docent en vakdeskundige. Dit verslag helpt bepalen welke handleidingen
bruikbaar zijn en welk herstel nog nodig is. Het wijzigt geen handleiding of
studentmateriaal.

## Uitkomst en reikwijdte

Alle zeven handleidingen zijn beschikbaar in de repository. Hun weekroute,
verwijzingen en practicum-/huiswerknummers sluiten aan op de meetbasis, inclusief
de uiteindelijke consolidatie van #481. Alle zeven krijgen **aanpassing nodig**:
de docent krijgt niet overal het korte antwoord op collegeopdrachten waarvoor
geen uitwerking bestaat. De concrete hiaten staan bij F1–F7. Er is dus geen week
zonder bevinding; geen handleiding ontbreekt. De bestaande routes zijn bruikbaar
voor lesvoorbereiding, met de beperking dat de docent deze antwoorden zelf moet
voorbereiden totdat het vervolg is uitgevoerd.

Deze controle betreft PGM2 week 1–7, cursusweken 8–14. Beschikbaarheid van
handleidingen buiten de repository is niet beschikbaar. PGM1, nieuw lesontwerp,
reparaties aan bronmateriaal en nieuwe handleidingen vallen buiten scope.

## Toetsingskader en leeswijze

De norm [Wat een docentenhandleiding is, en waar hij staat](../curriculum/uitgangspunten.md#wat-een-docentenhandleiding-is-en-waar-hij-staat)
vraagt één weekdocument met docenthandelingen, tijdsindeling, studentproblemen en
uitvalpaden. Waar een college- of practicumopdracht geen uitwerking heeft, geeft
de handleiding een kort antwoord van hooguit één regel. Een test, hint of
leerdoel is daarbij geen antwoord op een open ontwerp- of verklaringsvraag.

De bijeenkomsten zijn getoetst aan *Drie bijeenkomsten per week* in
[uitgangspunten.md](../curriculum/uitgangspunten.md), de PGM2-tabel en
*Huiswerkindeling na #481* in [leerlijn.md](../curriculum/leerlijn.md), en
*Programmeren II* in [leeruitkomsten.md](../curriculum/leeruitkomsten.md).
Week 7 heeft één college, één practicum en een oefententamenbijeenkomst. Er is
geen tweede college achter het oefententamen gepland.

De uiteindelijke [C4-correctie van #481](https://github.com/hanze-hbo-ict/programmeren/issues/481#issuecomment-6695203285)
en [laatste begrensde ronde](https://github.com/hanze-hbo-ict/programmeren/issues/481#issuecomment-6695593974)
gaan vóór de oorspronkelijke routeconsolidatie: de W4-samenvoeging blijft; de
route van de andere zes weken is teruggezet; verplichte ontwerp- en analysetaken
zijn als statustekst verwijderd, de taken blijven. De bestaande leerlijnregel en
overig toegestaan gebruik van 'verplicht' zijn geen nieuwe bevinding. De
norm vereist na #483 geen plan en vergelijking in uitwerkingen.

[Conventies: reikwijdte](../conventies/conventies.md#reikwijdte) bepaalt het eigen
regime voor `handleidingen/`: begrippen, Markdown-opmaak en linting; codeconventies
waar code wordt getoond. Dit verslag bevat geen uitvoerbare code. De schrijfwijzer
voor studenten bindt deze docenttekst niet. De rapportagestijl volgt de korte,
feitelijke formuleringen van [week 8](week_8.md) en [week 14](week_14.md).

De onderstaande matrices vormen de eindige controlelijst. 'Sluit aan' betekent
een vergelijking van broninhoud op deze meetbasis, geen bewijs van gemeten
lesduur, werkende publicatie of bereikt studentbegrip. Notebookvindplaatsen
vermelden een kop en waar nodig het celnummer, geteld vanaf 1 in `cells`.

## Inventarisatie en gecontroleerde bronsets

De namen in deze tabel zijn de daadwerkelijk aanwezige handleidingen. Iedere
rij omvat de weekpagina, beide colleges (W7 één), het practicum, de drie
huiswerksets, hun uitwerkingen en eventuele aanvullende oefeningen. De aparte
opgavenpagina is ook gelezen voor functie en status van de niveaus.

| PGM2 / cursusweek | Handleiding en oordeel | Weekroute en colleges | Practicum en uitwerking | Huiswerkroute |
|---|---|---|---|---|
| 1 / 8 | [week_8.md](week_8.md), **aanpassing nodig** (F1) | [Weekpagina](../source/course/week_8.md); [8a_datastructuren](../source/lectures/8a_datastructuren.ipynb); [8b_taalmodel](../source/lectures/8b_taalmodel.ipynb) | [8a_text_genereren](../source/practicals/8a_text_genereren.md); [uitwerking](../source/solutions/8a_text_genereren.ipynb) | [opgaven_8](../source/course/opgaven_8.md); sets en uitwerkingen hieronder. |
| 2 / 9 | [week_9.md](week_9.md), **aanpassing nodig** (F2) | [Weekpagina](../source/course/week_9.md); [9a_list_comprehensions](../source/lectures/9a_list_comprehensions.ipynb); [9b_dict_en_set_comprehensions](../source/lectures/9b_dict_en_set_comprehensions.ipynb) | [9_register](../source/practicals/9_register.ipynb); [uitwerking](../source/solutions/9_register.ipynb) | [opgaven_9](../source/course/opgaven_9.md); sets en uitwerkingen hieronder. |
| 3 / 10 | [week_10.md](week_10.md), **aanpassing nodig** (F3) | [Weekpagina](../source/course/week_10.md); [10a_recursie](../source/lectures/10a_recursie.ipynb); [10b_recursief_ontwerpen](../source/lectures/10b_recursief_ontwerpen.ipynb) | [10_directory_doorzoeken](../source/practicals/10_directory_doorzoeken.ipynb); [uitwerking](../source/solutions/10_directory_doorzoeken.ipynb) | [opgaven_10](../source/course/opgaven_10.md); sets en uitwerkingen hieronder. |
| 4 / 11 | [week_11.md](week_11.md), **aanpassing nodig** (F4) | [Weekpagina](../source/course/week_11.md); [11a_use_it_or_lose_it](../source/lectures/11a_use_it_or_lose_it.ipynb); [11b_functie_als_argument](../source/lectures/11b_functie_als_argument.ipynb) | [11_wisselgeld](../source/practicals/11_wisselgeld.ipynb); [uitwerking](../source/solutions/11_wisselgeld.ipynb) | [opgaven_11](../source/course/opgaven_11.md); sets en uitwerkingen hieronder. |
| 5 / 12 | [week_12.md](week_12.md), **aanpassing nodig** (F5) | [Weekpagina](../source/course/week_12.md); [12a_objecten](../source/lectures/12a_objecten.ipynb); [12b_data_object](../source/lectures/12b_data_object.ipynb) | [12_creatures](../source/practicals/12_creatures.md); [uitwerking](../source/solutions/12_creatures.ipynb) | [opgaven_12](../source/course/opgaven_12.md); sets en uitwerkingen hieronder. |
| 6 / 13 | [week_13.md](week_13.md), **aanpassing nodig** (F6) | [Weekpagina](../source/course/week_13.md); [13a_overerving](../source/lectures/13a_overerving.ipynb); [13b_polymorfisme](../source/lectures/13b_polymorfisme.ipynb) | [13_creatures](../source/practicals/13_creatures.md); [uitwerking](../source/solutions/13_creatures.ipynb) | [opgaven_13](../source/course/opgaven_13.md); sets en uitwerkingen hieronder. |
| 7 / 14 | [week_14.md](week_14.md), **aanpassing nodig** (F7) | [Weekpagina](../source/course/week_14.md); [14a_operatoren_en_exceptions](../source/lectures/14a_operatoren_en_exceptions.ipynb) | [14_creatures](../source/practicals/14_creatures.md); [uitwerking](../source/solutions/14_creatures.ipynb) | [opgaven_14](../source/course/opgaven_14.md); sets en uitwerkingen hieronder. |

### Huiswerk, aanvullende oefeningen en aansluiting van uitwerkingen

Per niveau zijn de opdracht-/stapkoppen en nummering van opgave en uitwerking
vergeleken; functies en gegeven controles zijn op aansluiting bekeken. De aantallen
hieronder tellen genummerde opdrachten/stappen, geen studielast. Een analyseopdracht
naast stappen telt mee. Er is geen algemene heruitvoering van ongewijzigde code
gedaan en er worden geen nieuwe claims over concrete programma-uitvoer gedaan.

| PGM2-week | Opstap: opgave / uitwerking | Basis: opgave / uitwerking | Extra: opgave / uitwerking | Aansluiting en aanvullend materiaal |
|---|---|---|---|---|
| 1 | [opstap](../source/problems/8_opstap.ipynb) / [uitwerking](../source/solutions/8_opstap.ipynb) | [basis](../source/problems/8_basis.ipynb) / [uitwerking](../source/solutions/8_basis.ipynb) | [extra](../source/problems/8_extra.ipynb) / [uitwerking](../source/solutions/8_extra.ipynb) | 15 / 6 / 3 genummerde onderdelen. Woorden inlezen, splitsen, tellen en rapporteren; setbewerkingen in de extra. Geen afzonderlijke aanvullende oefenset aangetroffen in de weekroute. |
| 2 | [opstap](../source/problems/9_opstap.ipynb) / [uitwerking](../source/solutions/9_opstap.ipynb) | [basis](../source/problems/9_basis.ipynb) / [uitwerking](../source/solutions/9_basis.ipynb) | [extra](../source/problems/9_extra.ipynb) / [uitwerking](../source/solutions/9_extra.ipynb) | 13 / 6 / 6 onderdelen. `ngram_loop` blijft stap 4; toernooi sluit aan. [Aanvullende comprehensions](../source/extra/practice/2_list_comprehension.ipynb): 12 opdrachten en ingebouwde uitwerkingen, verdieping. |
| 3 | [opstap](../source/problems/10_opstap.ipynb) / [uitwerking](../source/solutions/10_opstap.ipynb) | [basis](../source/problems/10_basis.ipynb) / [uitwerking](../source/solutions/10_basis.ipynb) | [extra](../source/problems/10_extra.ipynb) / [uitwerking](../source/solutions/10_extra.ipynb) | 12 / 7 / 5 onderdelen. Scrabble omvat stap 6 eigen tegels en analyseopdracht 1; Potjeslatijn sluit aan. [Aanvullende recursie](../source/extra/practice/1_recursie.ipynb): 11 opdrachten en ingebouwde uitwerkingen, facultatief. |
| 4 | [opstap](../source/problems/11_opstap.ipynb) / [uitwerking](../source/solutions/11_opstap.ipynb) | [basis](../source/problems/11_basis.ipynb) / [uitwerking](../source/solutions/11_basis.ipynb) | [extra](../source/problems/11_extra.ipynb) / [uitwerking](../source/solutions/11_extra.ipynb) | 9 / 9 / 15 onderdelen. Basis: nijlpaard 1–3, schoolrun 4–8 en analyseopdracht 1. Extra: Pijlenpad 1–5, Periodiek T-shirt 6–8, Caesar opdrachten 1–7. Alle onderdelen staan in de bijbehorende samengevoegde uitwerking. Geen afzonderlijke aanvullende oefenset in de route. |
| 5 | [opstap](../source/problems/12_opstap.ipynb) / [uitwerking](../source/solutions/12_opstap.ipynb) | [basis](../source/problems/12_basis.ipynb) / [uitwerking](../source/solutions/12_basis.ipynb) | [extra](../source/problems/12_extra.md) / [uitwerking](../source/solutions/12_extra.ipynb) | 12 / 13 / 10 onderdelen. Date loopt tot afschermen in stap 13; Board begint de facultatieve extra-lijn. Geen afzonderlijke aanvullende oefenset in de route. |
| 6 | [opstap](../source/problems/13_opstap.ipynb) / [uitwerking](../source/solutions/13_opstap.ipynb) | [basis](../source/problems/13_basis.ipynb) / [uitwerking](../source/solutions/13_basis.ipynb) | [extra](../source/problems/13_extra.md) / [uitwerking](../source/solutions/13_extra.ipynb) | 13 / 11 / 7 onderdelen. Kassabon omvat aanbieding in stap 10 en gewogen aanbieding in stap 11; spelers bouwen op Board voort. Geen afzonderlijke aanvullende oefenset in de route. |
| 7 | [opstap](../source/problems/14_opstap.ipynb) / [uitwerking](../source/solutions/14_opstap.ipynb) | [basis](../source/problems/14_basis.ipynb) / [uitwerking](../source/solutions/14_basis.ipynb) | [extra](../source/problems/14_extra.md) / [uitwerking](../source/solutions/14_extra.ipynb) | 10 / 8 / 8 onderdelen. Date bevat `return self`, constructorvalidatie en `parse_dates`; min-max bouwt op spelers voort. Geen afzonderlijke aanvullende oefenset in de route. |

De zeven practicumuitwerkingen volgen de genoemde opdrachten: Markov 1–2;
register 1–5; directory 1–5; wisselgeld 1–2; creatures 12 stappen 1–5,
creatures 13 stappen 1–8 en creatures 14 stappen 1–8. De creatures-uitwerkingen
12 en 13 zijn tevens de aangewezen beginstand van de volgende week. De
handleidingen wijzen deze route aan, inclusief het niet kopiëren van de
opzettelijk falende cel. De W7-instructies voor het vervangen van oude assertions
verwijzen naar de actuele stappen 4–6. Geen ontbrekende niveau- of
practicumuitwerking vastgesteld. Dat bewijst aansluiting, geen nieuwe uitvoering.

## Controlematrix: lesvolgorde, voorkennis, status en toetsing

| PGM2-week | Lesvolgorde en aangewezen taken | Voorkennis en weekgrenzen | Functie, status en toetsmoment | Bevinding |
|---|---|---|---|---|
| 1 | Methoden/dictionaries → sets/opvolgers → Markov 1–2 en essay. Sluit aan op weekpagina en colleges. | PGM1-lussen, functies, bestanden en mutatie; nog geen comprehensions of klassen. | Dictionarydeel en basis na college 1, setdeel na college 2; extra facultatief. Geen toetsbijeenkomst in de weekroute. | Geen verschil in deze aspecten. F1 betreft docentantwoorden. |
| 2 | List comprehension → dict/set en luskeuze → register 1–5. | Dictionaries/sets en lusrecept; één `for` per comprehension, geen generator expressions. | Opstap verdeeld over colleges; basis na de benodigde stof; toernooi en aanvullende oefeningen verdieping. Geen toetsbijeenkomst. | Geen verschil in deze aspecten. F2 betreft docentantwoorden. |
| 3 | Lezen/naspelen → drie ontwerpvragen → directory 1–5. | Functieframes, dictionaries en `sum([...])`; twee keuzes pas volgende week. | Opstap lezen/schrijven; Scrabble-basis blijft; Potjeslatijn en aanvulling facultatief. Geen toetsbijeenkomst. | Geen verschil in deze aspecten. F3 betreft docentantwoorden. |
| 4 | Twee keuzes → functieargument/lambda → wisselgeld 1–2. | Recursie en collecties; nog geen OOP. `Pijlenpad` gebruikt de lus over keuzes uit W3. | Nijlpaard na college 1, schoolrun na college 2; samengevoegde extra is verdieping met drie delen. Geen toetsbijeenkomst. | Geen verschil in route of nummers na #481. F4 betreft docentantwoorden. |
| 5 | Eigen objecten → Date/identiteit → creatures 1–5. | Methoden uit W1; geen overerving, standaardparameter voor Party of exceptions. | Opstap en Date; Board facultatief en geen creatures-beginstand. Geen toetsbijeenkomst. | Geen verschil in deze aspecten. F5 betreft docentantwoorden. |
| 6 | Overerving → polymorfisme/duck typing → creatures 1–8. | Werkende W5-beginstand; compositie blijft onderscheiden van overerving. Exceptions pas W7. | Kassabon als basis, spelers facultatief vervolg op Board; geen verplichte voorbereiding voor creatures. Geen toetsbijeenkomst. | Geen verschil in deze aspecten. F6 betreft docentantwoorden. |
| 7 | Eén college → creatures 1–6 en sorteergrens → 7–8 bij resterende tijd; derde bijeenkomst oefententamen. | Date uit W5 en creatures uit W6; `NotImplemented` en eigen `Party.__iadd__` blijven buiten de route. | Bestaande W7-status: opstap en acht Date-stappen verplicht; min-max facultatief. Slotoperatoren geen verplichte thuisinhaalslag. Afvangen blijft in Date, practicum gooit. | Sluit aan op #472 en de begrensde correctie #481. F7 betreft docentantwoorden. |

De handleidingen gebruiken geen verouderde dertien-uitkomstenmatrijs en stellen
geen nieuwe toetsgewichten vast. Voor W3, W4 en W6 verwijst de huiswerkroute naar
de huidige basis met ontwerp-/analysetaken; deze zijn niet uit de sets verdwenen.
Dit verslag claimt geen nieuwe volledige toetsdekking of verplichte taaklabels.
Het oefententamen van W7 en de [uitwerking](../source/solutions/PGM2_examen.ipynb)
zijn aanwezig; [de opgaven](../source/extra/practice/PGM2_examen.md) bevatten de zes
huidige opgaven. De handleiding legt een oefenwerkvorm vast en claimt geen duur
of inhoud van het echte tentamen. De gekoppelde [tentameninformatie](../source/course/pgm2_tentamen.md)
is een navigatiepagina, geen bron van aanvullende toetsregels.

## Controlematrix: tijd en docentbruikbaarheid

Alle 21 tijdtabellen tellen op tot netto 90 minuten per bijeenkomst. Voor weken
1–6 zijn dit twee colleges en één practicum; voor W7 één college, één practicum
en het oefententamen. Dat is een gemeten som van voorgestelde minuten, geen
waarneming van behandeltijd. Werkelijke studenttijd is **niet beschikbaar**.

| PGM2-week | Docenthandeling en controlepunt | Verwachte studentproblemen en interventie | Uitvalpad en beoordeling van tijd |
|---|---|---|---|
| 1 | Voorspellen, sleutel/waarde aanwijzen, modelbouw los van willekeurige generatie controleren. | Positie als sleutel, één opvolger bewaren, setvolgorde beoordelen; terug naar concreet voorbeeld. | Minder gelijksoortige bespreking, extra uitstellen; onvoltooide functies/essay noteren; werkend duo bij bestandsproblemen. 3 × 90, inhoudelijk herkenbare prioritering; essayafronding is vervolg, geen afrondgarantie. |
| 2 | Comprehension teruglezen als lus; register tegen tekst controleren. | Filter versus waarde-keuze, index/element, onleesbare nesting; één lus herstellen. | Vertaalrichtingen bewaren, extra uitstellen, precieze registertest noteren; lus annoteren bij ontbrekende voorbereiding. 3 × 90, met concreet uitvalpad. |
| 3 | Frames met terugkeerwaarde, drie ontwerpvragen, functies afzonderlijk testen. | Alleen afdalen, ontbrekende `return`, geen kleiner probleem, verkeerd teruggeeftype. | Complete trace en zelfstandig ontwerp bewaren, minder voorbeelden; open practicumstappen noteren, basis behouden. 3 × 90; geen extra bijeenkomst verondersteld. |
| 4 | Twee takken op bord, meegeven versus aanroepen onderscheiden, onmogelijk geval testen. | Munt hergebruiken, nul als onmogelijk resultaat, `key=f()`; kleinere invoer en aanroepende plek aanwijzen. | Eén trace en functieargumentdiagnose bewaren, extra uitstellen, beide basisdelen als huiswerk; kleine trace bij achterstand. 3 × 90; beide leerlijnen blijven zichtbaar. |
| 5 | Object voor `self` aanwijzen; verwijzingen tekenen; assertions per stap. | Klasse/object, extra self-argument, alias/kopie, property/interne opslag. | Onvoltooide stappen noteren, Date behouden; uitwerking 12 als complete W6-beginstand. 3 × 90; Party krijgt een startblok, geen claim dat het practicum af is. |
| 6 | Constructorvolgorde, concrete duck-typingbelofte, gevechtslimiet. | Ontbrekende `super()`, typevertakking, te brede Turret-belofte, Party als subklasse. | Extra uitstellen, limiet bewaren, open stappen noteren; uitwerking 12 herstellen en 13 tijdig aanbieden voor W7. 3 × 90, met herstelroute. |
| 7 | Gooien/afvangen op twee plekken aanwijzen; vervangen assertions naast actuele stap leggen; setterkeuze noteren. | Waarde/identiteit bij aftrekken, `+=`, afvangen als negeren, oude assertions. | 7–8 alleen bij tijd; min-max/plenaire bespreking uitstellen; Date-afvangen bewaren; beginstand 13 overnemen. 3 × 90, oefenblok 5/70/10/5 gereserveerd. Raming 165–285 minuten is bestaand #472-ontwerp, geen gemeten studenttijd of totaal inclusief alle toetsvoorbereiding. |

**Beoordeling:** de handelingen, signalen en uitvalpaden maken de documenten meer
dan leeswijzers. Er is op basis van de bronvergelijking geen grond voor een nieuw
roosterbesluit. Of de blokken in een echte groep haalbaar zijn, is niet
vastgesteld. De concrete tekortkoming in de docentondersteuning is hieronder
begrensd tot ontbrekende antwoorden; geen algemene herschrijving nodig.

## Afwijkingen en benodigd herstel

Voor alle onderstaande bevindingen geldt dezelfde norm: een kort antwoord bij
collegeopdrachten zonder uitwerking, onder *Wat een docentenhandleiding is, en
waar hij staat*. De volledige respectieve handleiding bevat deze antwoorden niet;
verwijzingen naar niveau-uitwerkingen beantwoorden deze collegeopdrachten niet.
De tabel noemt per week een concreet aantoonbaar hiaat. Het vervolg moet ook de
overige collegeopdrachten van die week op deze norm nalopen, zonder de lessen
te herontwerpen of volledige uitwerkingen in de handleiding te plaatsen.

| ID / week | Concrete vindplaats | Verschil met huidige ondersteuning | Benodigd herstel |
|---|---|---|---|
| F1 / 1 | [8a](../source/lectures/8a_datastructuren.ipynb), *Opdracht 3*, cel 42; [handleiding](week_8.md), *College 1* en *Huiswerk en begeleiding*. | De student moet van jaar naar dier zoeken; de handleiding noemt collegeopdrachten en de dictionarytelling maar geeft geen kort antwoord op deze zoekrichting. Het notebook geeft een hint en uitvoerdoelen, geen ingevulde oplossing. | Voeg bij deze opdracht de korte oplossingskern toe en controleer overige onbeantwoorde opdrachten van 8a/8b. |
| F2 / 2 | [9a](../source/lectures/9a_list_comprehensions.ipynb), *Opdracht 3*, cel 47; [handleiding](week_9.md), *College 1*. | De student vertaalt de bonus-comprehension terug naar een lus. Tests noemen het eindresultaat; de handleiding vraagt vertalen maar geeft geen korte oplossingskern van die lus. | Voeg het korte docentantwoord bij de terugvertaling toe; loop 9a/9b na op overige onbeantwoorde collegeopdrachten. |
| F3 / 3 | [10a](../source/lectures/10a_recursie.ipynb), *Recursie unplugged*, *Opdracht 3*, cel 30; [handleiding](week_10.md), *College 1*. | De somstrategie voor geblinddoekte dieven wordt gevraagd, maar niet beantwoord. De bestaande uitwerking bij *Recursie unplugged* betreft zoeken naar 42. De handleiding geeft uitsluitend een algemeen terugkeercontrolepunt. | Geef de korte antwoordkern voor de somstrategie en loop ook de overige opdrachten van 10a/10b na. |
| F4 / 4 | [11b](../source/lectures/11b_functie_als_argument.ipynb), *Opdracht 2*, cel 30; [handleiding](week_11.md), *College 2*. | `count_matching` heeft een hint en tests; de handleiding laat de opdracht starten en vraagt naar de functieparameter, maar bevat geen kort antwoord op de implementatie. De basisuitwerking behandelt schoolrun, niet deze functie. | Voeg het korte antwoord bij `count_matching` toe en controleer overige opdrachten van 11a/11b. Behoud W4-basis/extra en hun nummering. |
| F5 / 5 | [12a](../source/lectures/12a_objecten.ipynb), *Opdracht 2*, cel 71; [handleiding](week_12.md), *College 1*. | De student moet een leesbaar maar niet wijzigbaar studentnummer ontwerpen. De handleiding noemt de publieke property in algemene zin, maar geeft niet het korte antwoord op deze concrete opdracht. | Voeg de korte ontwerpantwoordkern toe en controleer overige opdrachten van 12a/12b; geen nieuwe verplichte ontwerpstatus invoeren. |
| F6 / 6 | [13b](../source/lectures/13b_polymorfisme.ipynb), *Opdracht 2*, cel 29; [handleiding](week_13.md), *College 2*. | Een toehoorder wordt toegevoegd aan `latest_graduation`; gevraagd wordt waar het misgaat en of aanvullen passend is. De handleiding bespreekt de duck-typinggrens, maar geeft geen concrete docentantwoordkern op deze ontwerpvraag. | Voeg het korte antwoord bij deze vraag toe en controleer overige opdrachten van 13a/13b. |
| F7 / 7 | [14a](../source/lectures/14a_operatoren_en_exceptions.ipynb), *Opdracht 2*, cel 41; [handleiding](week_14.md), *College*. | Het college vraagt een constructorgrens en een lus die ongeldige jaren meldt en overslaat. De handleiding behandelt beide kanten en verwijst naar Date, maar geeft geen kort antwoord voor deze Student-opdracht. | Voeg de korte oplossingskern bij deze opdracht toe en controleer opdrachten 1 en 3. Behoud de prioriteit en oefententamenruimte van #472. |

## Vervolg en beslispunten

**V1 — begrensd herstel van F1–F7.** Voorstel voor één afgebakend vervolgwerkitem
onder de bestaande verzamelzaak [#95](https://github.com/hanze-hbo-ict/programmeren/issues/95):
*Vul korte docentantwoorden bij PGM2-collegeopdrachten aan*. Omvang: zeven
handleidingen, uitsluitend de antwoordnorm en noodzakelijke opdrachtverwijzingen.
Acceptatie: iedere collegeopdracht heeft een aanwezige antwoordbron of een
antwoord van hooguit één regel in de weekhandleiding; de tabel maakt de dekking
herleidbaar. Behoud routes, tijdblokken, huiswerksets en vastgestelde besluiten.
Uitwerkingen en benodigde docentantwoorden zijn verschillende normen; #483
ontheft niet van deze docentnorm. Laat het herstel onafhankelijk beoordelen en
voer de toepasselijke controles uit.

De orkestrator heeft V1 met F1–F7 geregistreerd in
[#487 — korte docentantwoorden bij PGM2-collegeopdrachten](https://github.com/hanze-hbo-ict/programmeren/issues/487),
onder de bestaande verzamelzaak #95. **AC5 is hiermee belegd.** Dit registreert
het noodzakelijke herstel; uitvoering en beoordeling van dat herstel blijven
vervolgwerk. Er zijn geen GitHub-mutaties door de auteur gedaan.

**Inhoudelijk beslispunt:** geen nieuw inhoudelijk besluit nodig voor deze
feitelijke controle of het toepassen van de bestaande antwoordnorm. Mocht het
vervolg een andere didactische route of een ruimere antwoordvorm nodig achten,
dan gaat die concrete keuze naar de vakdeskundige. Haalbaarheid in de klas en
werkelijke studenttijd blijven niet vastgesteld; dat is geen aanleiding om nu
planning, prioriteit of leerinhoud te wijzigen. Merge blijft een menselijk besluit.

## Verificatie en grenzen

- Aanwezigheid: 7/7 weekhandleidingen; de koppen koppelen PGM2 1–7 aan cursusweek 8–14.
- Lokale handleidinglinks: 100 verwijzingen gecontroleerd, alle doelen bestaan.
  Dit controleert bestanden, geen externe URL-bereikbaarheid of publicatie.
- Tijdtabellen: 21/21 tellen op tot 90 minuten; niet als gemeten studenttijd aangemerkt.
- Niveaudekking: 21/21 opgave-/uitwerkingparen; alle genummerde koppen komen per
  paar in dezelfde volgorde overeen. De concrete inhoudsaansluiting staat in de
  huiswerkmatrix; kopovereenkomst alleen bewijst geen uitvoerbaarheid.
- Practica: zeven passende uitwerkingen; aanvullende W2/W3-oefeningen houden hun
  ingebouwde uitwerkingen. Collegeantwoordhiaten blijven afzonderlijk zichtbaar.
- Verschillen: F1–F7 hebben ieder een vindplaats, verschil en herstelactie;
  V1 verwijst naar de geregistreerde herstelopdracht #487. Ontbrekend bewijs heet niet actueel.
- Alleen dit verslag is gewijzigd. Voor dit document buiten het studentenboek is
  geen Sphinx-build vereist; de build zou de handleidingen niet controleren.
  Markdown-linting, branchcontrole en basisdiff worden vóór C5 uitgevoerd; het
  concrete resultaat en de commando's staan in C5-kern.

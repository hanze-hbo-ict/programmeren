# Leeruitkomsten en toetsmatrijs

De bindende laag: wat de student moet kunnen en hoe zwaar het meetelt in het
tentamen. Alle overige keuzes moeten hiermee te rijmen zijn.

Dit document is de kopie onder versiebeheer van de toetsmatrijzen die eerder
alleen in `ontwikkeling/` stonden, een directory die niet in git zit. Daardoor was het
bindende document niet gedeeld en niet gevolgd in de tijd.

> **Formele status.** Een toetsmatrijs wordt vastgesteld en is geen document dat
> je terloops bijwerkt. PGM2 is op 4 november 2026 expliciet opnieuw vastgesteld;
> de nog open correcties hieronder blijven voorstellen.

## Programmeren I

### Competenties (HBO-i-model)

| Code | Omschrijving |
|---|---|
| **SOn1** | Maken van een ontwerp voor een softwaresysteem, inclusief database, met modelleertechnieken volgens een standaardmethode. |
| **SRe1** | Bouwen, testen en beschikbaar stellen van een eenvoudig softwaresysteem. Het opzetten, vullen en bevragen van een database maakt onderdeel uit van het softwaresysteem. |
| **OP-I** | Het identificeren van het probleem, richting van de oplossing bepalen en een passende aanpak kiezen. |
| **OP-II** | Gedurende het hele oplosproces nieuwsgierig zijn en vragen stellen vanuit verschillende perspectieven, deze vragen met een passende aanpak pragmatisch, kritisch en gebaseerd op bronnen beantwoorden. |

### Leeruitkomsten en weging

| Code | Omschrijving | Competentie | Niveau | Weging |
|---|---|---|---|---|
| **P1** | Student past toekenningen en variabelen toe. | SRe1 | Toepassen | 5% |
| **P2** | Student past rekenkundige en logische operatoren toe. | SRe1 | Toepassen | 10% |
| **P3** | Student past conditionele statements toe. | SRe1 | Toepassen | 10% |
| **P4** | Student past lijsten en strings en de bijbehorende methodes toe. | SRe1 | Toepassen | 10% |
| **P5** | Student definieert functies met positionele parameters en past ze toe. | SRe1 | Toepassen | 10% |
| **P6** | Student past assertions toe om fouten in functies op te sporen. | SRe1 | Toepassen | 10% |
| **P7** | Student past docstrings toe om functies te documenteren. | SRe1 | - | **geen** |
| **A1** | Student implementeert eenvoudige algoritmes door middel van functioneel programmeren. | SRe1 | Toepassen | 15% |
| **A2** | Student verdeelt eenvoudige computationele problemen in kleinere deelproblemen. | SRe1 | Toepassen | 10% |
| **A3** | Student ontwerpt algoritmes om eenvoudige computationele problemen op te lossen. | OP-I | Analyseren | 20% |

Totaal: 80% toepassen, 20% analyseren. **Samen 100%.** PGM1 heeft geen uitkomst
op creëren-niveau; dat is een besluit en geen gat. Zie
[uitgangspunten.md](uitgangspunten.md), *De weging van de PGM1-matrijs*, voor
die twee besluiten en voor de meting waarop ze rusten. Diezelfde sectie draagt een
derde besluit, van 27 oktober 2026: een vastgelegde uitzondering waarin een
concrete PGM1-toets de gemeten niveauverdeling van het oefententamen volgt in
plaats van deze 80% en 20%. De matrijs hierboven verandert daar niet door.

> De eerder vermelde verdeling "70% toepassen" klopte niet met de som van de rijen,
> ook vóór deze wijziging niet.

## Hoe de percentages zich tot de toets verhouden

De matrijzen sluiten op 100%. Het PGM1-oefententamen telt 90 punten; de
herziene PGM2-oefentoets telt 100 punten, volgens C4 van #470.
Het cijfer wordt met het betreffende toetstotaal berekend:

$$
\text{cijfer} = 1 + 9 \times \frac{\text{behaalde punten}}{\text{totaal aantal punten}}
$$

De **+1** is de basis en wordt niet over leeruitkomsten verdeeld. Nul punten
levert een 1 op, alle punten een 10. Een aandeel van 10% betekent bij PGM1
9 punten en bij deze PGM2-oefentoets 10 punten. De bestaande PGM1-uitzondering
op de niveauverdeling blijft gelden. De PGM2-oefentoets volgt de zes vastgestelde
LU-gewichten; dit doet geen uitspraak over het echte tentamen.

## Programmeren II

### Vastgesteld voor dit jaar

De zes-uitkomstenmatrijs is op 4 november 2026 vastgesteld voor dit jaar.
De letterlijke menselijke besluiten en hun exacte bronnen staan in
[uitgangspunten.md](uitgangspunten.md#zes-pgm2-uitkomsten-vastgesteld-voor-dit-jaar).
De oude dertien P/A-rijen gelden hierdoor niet meer als PGM2-matrijs; hun herkomst
blijft hieronder volledig verantwoord. Vaststelling bewijst geen gerealiseerde
oefen- of toetsdekking. De uitvoering daarvan volgt in #468–#472.

### Competenties (HBO-i-model)

| Code | Omschrijving |
|---|---|
| **SAn1** | Software analyseren niveau 1: functionele eisen en acceptatiecriteria bepalen voor één stakeholder; bestaande software op aanpasbaarheid analyseren; nagaan of een dataset informatie oplevert voor een toepassing. |
| **SOn1** | Maken van een ontwerp voor een softwaresysteem, inclusief database, met modelleertechnieken volgens een standaardmethode. |
| **SRe1** | Bouwen, testen en beschikbaar stellen van een eenvoudig softwaresysteem. Het opzetten, vullen en bevragen van een database maakt onderdeel uit van het softwaresysteem. |

SAn1 is hierboven samengevat uit de officiële
[HBO-i-domeinbeschrijving 2023, Software / Analyseren / niveau 1](https://www.hbo-i.nl/wp-content/uploads/2024/02/24040_HBOi_Domeinbeschrijving_NL.pdf).
Voor L5 gaat de aansluiting over bestaande software analyseren op mogelijkheden
voor aanpassing. De brede competentieomschrijvingen voegen geen database- of
standaardmodelleervereisten aan PGM2 toe. Geen nieuwe OP-koppeling is besloten;
de bestaande OP-labelverschillen tussen de vakken zijn hiermee niet gecorrigeerd.
Meervoudige competentiekoppeling telt punten niet dubbel.

### Leeruitkomsten en weging

| Code | Omschrijving | Competentie | Niveau | Weging |
|---|---|---|---|---|
| **II-L1** | De student past dictionaries en sets met de bijbehorende bewerkingen en methoden toe om gegevens op te slaan, op te zoeken en te verwerken. | SRe1 | Toepassen | **15%** |
| **II-L2** | De student past comprehensions, functies als argument en eenvoudige recursieve oplossingen toe om gegevens te transformeren, te selecteren, te ordenen of samen te vatten. | SRe1 | Toepassen | **20%** |
| **II-L3** | De student implementeert samenwerkende objecten en klassen volgens gegeven gedragsafspraken, met passende methoden, overerving of polymorfisme en operator overloading. | SRe1 | Toepassen | **25%** |
| **II-L4** | De student gebruikt exceptions om ongeldige toestanden te signaleren en handelt foutcondities gericht af. | SRe1 | Toepassen | **10%** |
| **II-L5** | De student analyseert een gegeven applicatie met samenwerkende functies en/of objecten, verklaart de taakverdeling en afhankelijkheden en onderbouwt waar een wijziging moet worden aangebracht. | SAn1 | Analyseren | **15%** |
| **II-L6** | De student ontwerpt en implementeert een applicatie voor een computationeel probleem, kiest zelfstandig een passende oplossingsstrategie en structuur en gebruikt daarbij functionele of objectgeoriënteerde programmeerconstructies. | SOn1, SRe1 | Creëren | **15%** |

Totaal: 70% toepassen, 15% analyseren, 15% creëren; samen 100%.

### Bewijsgrenzen

- **L1:** gevraagde gegevens in dictionary én set passend opslaan, opzoeken en verwerken; resultaat controleerbaar aan concrete invoer/uitvoer.
- **L2:** gegeven of geoefende aanpak correct uitvoeren met comprehensions, functieargumenten en eenvoudige recursie. Keuze binnen een opgegeven functie- of algoritmestructuur blijft hier toepassing.
- **L3:** gegeven gedragscontracten implementeren en controleren, inclusief objecttoestand, samenwerking, uitbreidbaar gedrag en operatoren. Geen tweede beloning voor dezelfde ontwerpkeuze onder L6.
- **L4:** ongeldige toestand zelf signaleren met passende exception; specifieke fout gericht afvangen, melden/herstellen/overslaan en gewenste voortgang aantonen.
- **L5:** op gegeven werkende software verantwoordelijkheden en afhankelijkheden verklaren, een wijziging lokaliseren en de gevolgen onderbouwen. Alleen uitvoer voorspellen of code aanvullen is onvoldoende.
- **L6:** kies zelfstandig een niet voorgeschreven oplossingsstrategie en structuur, verantwoord de keuze kort en implementeer haar functioneel of objectgeoriënteerd. Eén zelf ontworpen functie met comprehension of recursie telt ook, mits die vorm niet voorgeschreven was. Een `def` rond volledig imperatieve code of een voorgeschreven comprehension bewijst deze keuze niet. Zelfstandig recursief ontwerp en combinatie van drie paradigma's zijn geen afzonderlijke verplichtingen. In het oefenen zijn zowel functioneel ontwerp in W3/4 als OO-ontwerp in W6 verplicht; voor één L6-toetsprestatie volstaat functioneel of OO.

### Eenmalige weektoerekening

Alle getallen zijn procentpunten van het hele vak, geen lestijdmeting.
Hergebruik van voorkennis in een andere week krijgt geen tweede budget.

| LU | W1 | W2 | W3 | W4 | W5 | W6 | W7 | Totaal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| II-L1 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 15 |
| II-L2 | 0 | 10 | 5 | 5 | 0 | 0 | 0 | 20 |
| II-L3 | 0 | 0 | 0 | 0 | 10 | 10 | 5 | 25 |
| II-L4 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 10 |
| II-L5 | 0 | 0 | 5 | 5 | 5 | 0 | 0 | 15 |
| II-L6 | 0 | 0 | 5 | 5 | 0 | 5 | 0 | 15 |
| Week | 15 | 10 | 15 | 15 | 15 | 15 | 15 | 100 |

Week 7 houdt 5% L3 en 10% L4. Er komt geen aanvullende L5/L6-taak zonder
nieuw menselijk besluit. De haalbaarheid naast het oefententamen wordt afzonderlijk
onderzocht in #472; 15% toetsgewicht is geen bewijs van passende belasting.

### Herkomst van de dertien oorspronkelijke uitkomsten

| Oude rij | Status/opvolging |
|---|---|
| P1 lussen | PGM1-voorkennis, geen eigen PGM2-basisbudget; geen claim dat PGM2 geen lussen oefent. |
| P2 dictionaries | L1, inhoudelijk uitgebreid met sets. |
| P3 tekstbestanden | PGM1-voorkennis, afstemming #465; PGM2 leest daadwerkelijk bestanden, maar krijgt hier geen eigen basisbudget. |
| P4 exceptions | L4, gooien/afvangen/afhandelen behouden. |
| P5 klassen/objecten | L3. |
| P6 operator overloading | L3, zichtbaar W7-budget. |
| P7 bibliotheken | Vervallen als afzonderlijke leeruitkomst; bibliotheken blijven waar nodig hulpmiddel bij opdrachten. |
| A1 imperatieve algoritmen | Basis naar PGM1-voorkennis, functionele verwerking expliciet L2; inhoudswijziging, geen woordruil. |
| A2 OO-algoritmen toepassen | L3. |
| A3 applicatie met drie paradigma's | Vervangen door L5/L6; verplichte combinatie vervalt. |
| A4 complex algoritmeontwerp | Breder L6; specifieke oude complexiteitsnorm niet ongewijzigd behouden. |
| A5 taal-FSM | Vervallen; taal-FSM wordt niet meer onderwezen of getoetst. |
| A6 recursie ontwerpen/toepassen | Toepassing L2; ontwerp optioneel L6, afzonderlijke verplichting vervalt. |

### Verplichte oefening en toetsdekking

Dit is de gerichte stand op basis van snapshot `d2301eb7`, 4 november 2026,
uit C2 van #466. Historische metingen van #361 en #376 blijven historische bronnen;
hun resterende afhandeling ligt in de vijf gekoppelde vervolgitems.
Basis is iedere week verplicht, opstap behalve W3; extra is facultatief.
Facultatieve extra's garanderen geen prestatie van iedere student.
Paden in onderstaande tabel zijn relatief aan `source/`.

| Doel | Actuele verplichte oefening en toetsbewijs | Inhoudelijk oordeel / ontbrekend bewijs |
|---|---|---|
| II-L1 | `problems/8_opstap.ipynb` c2–20: dictionary maken, opzoeken, wijzigen, doorlopen en tellen; c25–31: set maken, lidmaatschap, toevoegen en aantallen vergelijken. `8_basis` c10/14/17: dictionary verwerken. Toets: geen gerichte dictionary-/setvraag. | Handgrepen en verwerking worden verplicht geoefend. Vrij gebruik in opgave 6 garandeert toetsdekking niet. |
| II-L2 | `9_basis` c6/13/16/22: comprehension schrijven, terugvertalen, filteren; `9_opstap` c22/25/28 draagt ook set-/dictcomprehensions. `10_basis` c7/10/13/16: recursieve som, buurvergelijking, filter en maximum met aangereikte vormen. `11_lambda_basis` c5/8/11/14: `key`, doorgeven en zelf aanroepen van functieargumenten. Toets 1, 2b/2c en 3: 30 punten expliciete toepassing. | Reële verplichte toepassing. Moeilijkheid, meerdere aanroepen of een lambda maken de handeling niet tot zelfstandig applicatieontwerp. Functieargumenten en dict-/setcomprehensions worden niet gericht getoetst. |
| II-L3 | `12_basis`: `Date` met gegeven gedragsafspraken, samenwerking tussen methoden; `13_basis` stappen 1–7/9–11: subklassen, overschrijven, `Receipt`, duck typing; `14_basis` stappen 1–6: operatoren. Toets 4: eenvoudige klasse en gegeven spellus (20 punten). | Brede oefenlijn aanwezig; Nim verplicht geen overerving, polymorfisme, operatorgedrag of meerdere samenwerkende objectsoorten. |
| II-L4 | `14_basis` c27: ongeldige datum weigeren met `ValueError`; c32: `parse_dates` met gerichte afhandeling en doorgaan. Opstap introduceert nieuwe syntaxis. `practicals/14_creatures.md` laat gooien oefenen en verwijst voor afvangen naar de basis. Geen gerichte toetsvraag. | De oude diagnose ‘uitsluitend gegeven code’ is achterhaald. Gooien én afhandelen zijn verplichte oefening; toetsdekking ontbreekt. |
| II-L5 | W4 `11_opstap` c2/6/11/15 vraagt aanroepen/uitvoer verklaren; `11_lambda_basis` c14 schrijft de samenwerking `winner`–`select`–`fastest` voor. W5 `12_basis` stap 12 onderzoekt externe mutatie; W6 `13_basis` stappen 3/8 en c32 vragen dispatch, vereiste interface en gevolgen van wijziging te verklaren. Nim vraagt aanvullen. | W5/6 bevatten echte analyse-elementen; geen nuldekkingclaim. Losse uitvoervragen en het volgen van opgegeven samenwerking garanderen nog geen integrale analyse van taakverdeling, afhankelijkheden én onderbouwde wijzigingsplaats. Die combinatie in W3/4/5 expliciteren in #469; W3 analyseert gegeven functies/recursie zonder OOP-voorkennis. Bestaande W6-analyse verdwijnt niet automatisch. |
| II-L6 | `10_basis` geeft functies, opsplitsing, basisgevallen en analogieën. `11_algoritmen_basis` c3/7/10 geeft drie functies en use-it/lose-it-strategie; `practicals/11_wisselgeld` c2–7 geeft basisgevallen, kleinere problemen en combinatie. `10_extra` laat randgevallen kiezen, maar is facultatief. Toets 5 vraagt recursie zonder gegeven algoritme; toets 6 laat ook geheel imperatief werken. | Geen gegarandeerd zelfstandig strategie- én structuurontwerp voor iedereen in W3/4 aangetoond. Dit zegt niets over feitelijke beheersing of wat een student zonder hints doet. Toets 5 schrijft recursie voor en garandeert daardoor geen vrije vormkeuze volgens C4-deelbesluit 1; één zelf ontworpen functie blijft geldig L6-bewijs mits de vorm niet voorgeschreven was; toets 6 biedt vrijheid maar eist de nieuwe paradigma-/ontwerpgrens niet. |

### Historische basis: alle 90 oude punten

Deze historische tabel bewaart de uitgangssituatie vóór #470. De gerealiseerde vervanging naar 100 punten staat in `handleidingen/PGM2_oefententamen_rubric.md`, inclusief alle oude eenheden; docstring/assertions hebben geen retrospectieve deelverdeling.

| Eenheid | Bestaande punten | Prestatie en afhandeling in vervolg #470 |
|---|---:|---|
| 1 Extensies | 10 | Gegeven recursief algoritme → L2; behouden als toepassingsbron, uitwerkingsdefect apart herstellen. |
| 2a lus | 5 | PGM1-voorkennis; zichtbaar als 5 overgangspunten, herbestemming/vervanging vraagt toetsbesluit. |
| 2b comprehension | 5 | L2-toepassing; behouden als bron. |
| 2c recursie | 5 | L2-toepassing; behouden als bron. |
| 3 Bonus | 10 | L2-toepassing; behouden als bron. |
| 4.1 `player_takes` | 5 | L3 eenvoudige klassentoestand. |
| 4.2 `AI_turn` | 5 | Gegeven strategie toepassen binnen klasse; L3-context, geen zelfstandig ontwerp. |
| 4.3 `game_over` | 5 | L3 methode volgens contract. |
| 4.4 computerbeurt | 5 | Gegeven klassengebruik/spellus aanvullen; geen analysebewijs. |
| 5 Alfabetisch | 15 | Ongesplitst blok recursie plus docstring/3 assertions. Hoogstens kandidaat voor zelfstandig algoritmeontwerp; geen 15 creërenpunten boeken. Rubric-/niveaukeuze uitstellen, blok volledig administreren. |
| 6 Moeilijke woorden | 20 | Ongesplitst vrije implementatie met gegeven formule/splitinstructie; kandidaat L6 na expliciete strategie-/structuurvrijheid, bewijs en functioneel-of-OO-grens. Huidige imperatieve vrijheid geen gegarandeerde L6. |

Som oude punten: 10+5+5+5+10+5+5+5+5+15+20=90. Deze historische
bronopgaven zijn vervangen volgens C4 van #470; de oude 2b/2c zijn elk voor
5 punten behouden als de huidige 2a/2b. De oude 2a is vervallen; de huidige 2c
is de toegevoegde functieargumentvraag. Alfabetisch is als geheel vervangen door het nieuwe
ongesplitste blok van 5 punten. De overige vervangingen en nieuwe deelpunten
staan in de docentrubric; oude en nieuwe punten worden niet opgeteld.

### Gerealiseerde oefentoetsdekking na #470

De oefenbeschrijvingen in de historische tabel hierboven zijn niet opnieuw
onderzocht. De toetsuitspraken daar beschrijven de situatie vóór deze herziening.
Onderstaande gerichte registratie vervangt die toetsuitspraken, zonder nieuwe
weekclaims of wijziging aan de matrijs of bewijsgrenzen.

| LU | Opgave | Gevraagde prestatie | Punten |
|---|---|---|---:|
| II-L1 | 3 Bonus | Dictionary maken, opzoeken, wijzigen en verwerken; set, lidmaatschap en verschil. | 15 |
| II-L2 | 2 en 5 | Comprehension, eenvoudige recursie en functieargument toepassen; alfabetische recursie met vormvereisten. | 20 |
| II-L3 | 4 Nim | Gegeven toestand en samenwerking, overerving/polymorfisme en operatorvergelijking implementeren. | 25 |
| II-L4 | 4 Nim | Zelf ongeldige zet gooien, gericht afvangen en met intacte toestand doorgaan. | 10 |
| II-L5 | 1 Extensies | Werkende applicatie analyseren: verantwoordelijkheden, afhankelijkheden en onderbouwde wijzigingsplaats. | 15 |
| II-L6 | 6 Moeilijke woorden | Zelf strategie en structuur kiezen, kort verantwoorden en functioneel of OO implementeren. | 15 |

Opgaven: 15/15/15/35/5/15 = 100. Niveaus: 70/15/15. Geen punt telt dubbel.
Dit is toetsopdrachtbewijs, geen uitspraak over feitelijke studentbeheersing,
studenttijd of het echte tentamen. Bron: [C4 #470](https://github.com/hanze-hbo-ict/programmeren/issues/470#issuecomment-6662338378)
en [deelpuntenaddendum](https://github.com/hanze-hbo-ict/programmeren/issues/470#issuecomment-6662364884).

### Vervolgwerk en samenhang

| Item | Begrensde opdracht en eindpunt | Status |
|---|---|---|
| [#468](https://github.com/hanze-hbo-ict/programmeren/issues/468) | V1: verplicht zelfstandig functioneel ontwerp W3/4 én OO-ontwerp W6; maximaal één ontwerptaak per betrokken week, toepassingssteun behouden; strategie, structuur en implementatie aantoonbaar zelfstandig. | Aangemaakt; afzonderlijke uitvoering. |
| [#469](https://github.com/hanze-hbo-ict/programmeren/issues/469) | V2: maximaal één expliciete analyseprestatie in W3/4/5: taakverdeling, afhankelijkheden, wijzigingsplaats en gevolgen; W3 zonder OOP-voorkennis. Bestaande W5/6-vragen behouden waar passend. | Aangemaakt; afzonderlijke uitvoering. |
| [#470](https://github.com/hanze-hbo-ict/programmeren/issues/470) | V3: zes bestaande toetsopgaven en noodzakelijke vervangende dekking, alle 90 punten eenmaal verantwoorden; eigen eindige toets/rubric en menselijk scopebesluit. Hergebruik 4 als L3/L4-contract en 6 als zelfstandig L6-ontwerp besloten. | Uitgevoerd binnen vijfbestandscope; zie gerealiseerde oefentoetsdekking.  |
| [#471](https://github.com/hanze-hbo-ict/programmeren/issues/471) | V4: vergelijkingsvoorbeeld opgave 5 en basisgevalvolgorde plus uitleg opgave 1 herstellen; lokale termen methode/basisgeval corrigeren; interfaces en punten behouden, contractgevallen uitvoeren. | Aangemaakt; afzonderlijke uitvoering. |
| [#472](https://github.com/hanze-hbo-ict/programmeren/issues/472) | V5: bestaande W7-taken plaatsen in college, practicum, oefententamen en huiswerk; expliciet haalbaarheidsbesluit of begrensde reductie-/verplaatsingsvraag, geen extra L5/L6. | Aangemaakt; afzonderlijke uitvoering. |

De defecten in het suffixbasisgeval en het lettervergelijkingsvoorbeeld zijn in
Werkitem #471 hersteld; deze herziening behoudt die reparaties. De toets/rubric is in #470
uitgevoerd; lesmateriaal en de overige vervolgitems vallen buiten die scope.
Er is geen claim over het echte tentamen of een rubric buiten de repository.

Deze variant houdt exceptions inclusief `raise` in PGM2. #465 is een afzonderlijk
toekomstscenario: eventuele verhuizing vraagt vervangende PGM1-dekking, een
afzonderlijk besluit over gevolgen voor L3/L4 en herverdeling. #356 over
PGM1-omvang/niveaus wordt hier niet beslecht.

## Voorgestelde correcties

De onderstaande doorlichtingsbevindingen bevatten ook historische PGM2-rijen.
De vaststelling van 4 november 2026 is leidend voor hun actuele afhandeling;
deze tabel bewaart de herkomst en de nog open PGM1-vragen.

| Uitkomst | Bevinding | Voorstel |
|---|---|---|
| **PGM1 P7** (docstrings) | Wél onderwezen en overal in het materiaal toegepast. Niet gewogen, maar wél bepunt: het tentamen keert punten uit voor een docstring, als eenvoudig werk dat zelfdiscipline beloont. Vastgesteld door de vakdeskundige op 21 oktober 2026; zie [uitgangspunten.md](uitgangspunten.md), *Punten voor docstring en signatuur*. Een puntentoekenning is geen weging, zie daar. | Weging geven, of de uitkomst laten zoals zij nu is: bepunt zonder weging. De variant *vormeis zonder punten* is door dat besluit afgevallen. |
| ~~**PGM1: de weging van de matrijs**~~ | **Uitgevoerd op 4 oktober 2026.** Het gewicht dat A4 achterliet is aan A3 toegekend: A3 weegt 20% en de matrijs sluit op 100%. Dat PGM1 geen uitkomst op creëren-niveau heeft, is daarbij als keuze vastgelegd en niet als restant. De grond, de niveaumeting van het oefententamen en wat beide besluiten zou heropenen staan in [uitgangspunten.md](uitgangspunten.md), *De weging van de PGM1-matrijs*. | Gedaan. |
| **PGM1 P4** (lijsten/strings en de bijbehorende methodes) | Het methodes-deel wordt al jaren niet meer in PGM1 onderwezen of getoetst. Vanaf de herziening van PGM1 week 7 en PGM2 week 1 introduceert PGM1 geen objectmethoden meer; dat verschuift volledig naar PGM2 week 1. Zie [leerlijn.md](leerlijn.md) en [uitgangspunten.md](uitgangspunten.md). | Herformuleren tot wat lijsten/strings betreft zonder de methodes, of het methodes-deel schrappen. |
| **PGM1 A1** (*functioneel*) | De oorspronkelijke vakindeling past niet bij het huidige materiaal: lussen zijn PGM1, functionele verwerking staat nu expliciet in PGM2 L2. | De PGM1-formulering wordt in #465 afzonderlijk behandeld; hier niet aangepast. |
| **PGM1 week 6** (bestanden) | De week onderwijst bestanden, terwijl de PGM1-matrijs hiervoor nog geen eigen rij noemt. De oude PGM2 P3 is sinds 4 november 2026 PGM1-voorkennis zonder eigen PGM2-basisbudget. | Afzonderlijke PGM1-afstemming via #465; geen PGM1-matrijswijziging in #466. |

Daarnaast staat één uitkomst in de verkeerde matrijs:

| Uitkomst | Bevinding | Voorstel |
|---|---|---|
| ~~**PGM1 A4** (recursie)~~ | **Uitgevoerd op 1 september 2026.** De uitkomst staat nu als **PGM2 A6**. Zij stond op creëren-niveau voor 10% van het PGM1-tentamen terwijl recursie in PGM1 niet wordt onderwezen; het PGM2-tentamen besteedt er 30 van de 90 punten aan. PGM2 telde vóór de verplaatsing 90% en komt er nu mee op 100% uit. | Gedaan. Het gewicht dat in PGM1 achterbleef is op 4 oktober 2026 aan A3 toegekend; zie de rij over de weging van de matrijs hierboven. |

## Gaten tussen toetsing en onderwijs

De actuele PGM2-dekking en begrensde vervolgen staan hierboven bij de zes
vastgestelde uitkomsten. De oude diagnose dat exceptions uitsluitend als gegeven
code voorkomen is achterhaald: `source/problems/14_basis.ipynb` laat zelf gooien
én gericht afhandelen verplicht oefenen. Gerichte oefentoetsdekking voor L1 en L4 is in #470 gerealiseerd. Bestanden zijn PGM1-voorkennis; PGM2 leest daadwerkelijk bestanden,
zonder afzonderlijk PGM2-basisbudget. Dit is geen besluit over de PGM1-matrijs.

# Docentenhandleiding PGM1 week 7

Deze week is de grens waar mutatie binnenkomt. Tot en met week 6 bouwden
functies een nieuwe waarde en gaven die terug; nu leert de student ook een
bestaande lijst op een vaste plek veranderen. Dat nieuwe vermogen vraagt meteen
om zorgvuldigheid: twee namen kunnen naar dezelfde lijst verwijzen, en een
onafhankelijke kopie vraagt om een nieuwe buitenlijst én nieuwe rijen.

De tweede lijn van de week is algoritmeontwerp. De student deelt een probleem op
in functies, test die functies afzonderlijk en gebruikt ze daarna in
functiecompositie. De basisopgave maakt die lijn concreet met een volgende
rastertoestand. Een tuple is daarbij een klein retourpaar: de student leert een
tuple teruggeven, lezen en uitpakken.

De verplichte route bestaat uit de opstap en de basis. Game of Life is een
zelfstandige, facultatieve extra. Als de tijd krap is, is één geteste
basisgeneratie het eindpunt; de extra mag de kern niet verdringen.

## 1. De week in één oogopslag

| Bijeenkomst | Vorm | Materiaal | Product aan het einde |
|---|---|---|---|
| 1 | College en begeleide start | `source/lectures/7a_lists_advanced.ipynb`, `source/problems/7_opstap.ipynb` | De student kan één cel muteren, verwijzingen en kopiëren uitleggen en een tuple teruggeven en uitpakken. |
| 2 | Werkcollege | `source/problems/7_basis.ipynb` | `count_neighbors` en `next_cell` zijn getest; de student heeft de invoer- en uitvoergrens van `next_generation` gepland. |
| 3 | Zelfstandig werk met gerichte begeleiding | `source/problems/7_basis.ipynb`, daarna `source/problems/7_extra.md` | De basis levert één correcte generatie op en laat het invoerbord onveranderd; daarna kan de student zelfstandig aan Game of Life beginnen. |

De drie bijeenkomsten zijn elk een referentierooster van 90 minuten. Het
rooster legt niet vast of een docent een bijeenkomst als één blok van 90 minuten
of als twee blokken van 45 minuten organiseert. Houd de volgorde van de
begripsstappen wel aan: directe mutatie, verwijzing, onafhankelijke kopie,
tuple en uitpakken, daarna functiecompositie en de rastertoestand.

De actuele studentroute staat in `source/course/week_7.md`. Daar staan ook het
uitvalpad en de overgang naar PGM2. Deze handleiding vult die route aan met
docentkeuzes, signalen van begrip en interventies; de studentinstructies blijven
in `source/`.

## 2. Leerdoelen en voorkennis

Aan het einde van de week kan de student:

- met een directe toekenning één cel in een 2D-lijst veranderen en voorspellen
  welke waarde daarna in het bord staat;
- uitleggen dat `ander = bord` een verwijzing naar dezelfde lijst oplevert, en
  een onafhankelijke rasterkopie maken met een nieuwe buitenlijst en nieuwe
  rijen;
- een tuple met twee samenhangende waarden teruggeven, indexeren en uitpakken
  in twee namen;
- een rasterprobleem opdelen in deelproblemen en per functie de invoer, uitvoer
  en een kleine assertion beschrijven;
- `count_neighbors`, `next_cell` en `next_generation` in de afgesproken volgorde
  opbouwen en één volledige generatie testen;
- uitleggen dat `next_generation` waarden uit het oude bord leest en naar een
  onafhankelijk resultaat schrijft.

De noodzakelijke voorkennis komt uit week 5: lijsten van lijsten, rij- en
kolomindexen, geneste lussen, functies en assertions. In [week
5](../source/course/week_5.md) heeft de student een raster gebouwd en
doorgelopen, maar bleef de oude lijst ongemoeid. Die grens maakt de eerste
mutatie van week 7 zichtbaar. Week 6 levert de ervaring met bestanden en data;
pixelrepresentaties hoeven deze week niet opnieuw te worden behandeld.

Controleer vóór de eerste bijeenkomst vooral of studenten `bord[rij][kolom]`
als één cel kunnen lezen en of zij weten dat een functie een nieuwe waarde kan
teruggeven. Wie daar nog onzeker over is, begint met de opstap; de opstap is een
diagnose en instap, niet een extra verplichte week vóór de basis.

## 3. Referentierooster en producten

De tijden hieronder zijn richttijden binnen een bijeenkomst van 90 minuten. Ze
geven de docent een houvast voor de volgorde en de minimale producten. Ze zijn
geen voorschrift voor de interne verdeling van de bijeenkomst.

### Bijeenkomst 1 - mutatie, verwijzing en tuple

| Richttijd | Docentaccent | Product of controlepunt |
|---:|---|---|
| 0-15 min | Haal het week-5-raster op: rij, kolom, buitenste lijst en binnenste rij. Laat studenten eerst voorspellen wat één directe toekenning doet. | `bord[1][2] = 1` verandert precies één cel. De overige cellen blijven gelijk. |
| 15-30 min | Zet `ander = bord` naast het oorspronkelijke bord. Vraag welke namen naar welk object verwijzen voordat de cel via `ander` wordt gewijzigd. | De student voorspelt dat de wijziging via `ander` ook zichtbaar is via `bord`. |
| 30-45 min | Bouw een onafhankelijke kopie met een nieuwe buitenlijst en `rij[:]` voor iedere rij. Laat eerst één verkeerde ondiepe kopie bespreken. | Alleen `kopie[0][0]` verandert; `bord` blijft gelijk. |
| 45-60 min | Introduceer het contrast tussen een veranderbare lijst en een onveranderlijke tuple. Voer de gecontroleerde `TypeError` pas uit nadat de klas heeft voorspeld. | De student kan zeggen dat een tuple wel gelezen en uitgepakt, maar niet op een positie gewijzigd kan worden. |
| 60-75 min | Laat `midden_van` een tuple `(rij, kolom)` teruggeven. Vraag waar de twee waarden voor staan. | `midden_van` geeft `(1, 1)` voor het gegeven 3x3-bord terug. |
| 75-90 min | Laat de tuple uitpakken in `rij, kolom` en verbind dit met het grotere rasterprobleem van de basis. | De student heeft de opstap afgerond of kan precies aanwijzen welk begrip nog niet vaststaat. |

Gebruik het college voor de gezamenlijke voorbeelden en laat de student daarna
de overeenkomstige opstapstappen zelf uitvoeren. De kern van deze bijeenkomst
is niet een definitie uit het hoofd, maar een voorspelling die de student aan
de hand van de zichtbare lijsten controleert.

### Bijeenkomst 2 - deelproblemen en één cel

| Richttijd | Docentaccent | Product of controlepunt |
|---:|---|---|
| 0-15 min | Laat studenten de mutatiegrens en de kopieergrens in één zin herhalen. Bespreek het doel van `next_generation`: lezen uit `board`, schrijven naar `result`. | Student benoemt dat tussentijdse nieuwe waarden niet terug het invoerbord in mogen. |
| 15-35 min | Begin met `count_neighbors`. Teken een hoek, rand en binnen-cel en houd de acht relatieve posities zichtbaar. | Assertions voor een hoek, rand en binnen-cel zijn groen. |
| 35-55 min | Bouw `next_cell` op uit de huidige cel en de buurttelling. Laat de regels eerst in gewone taal toepassen op één levende en één dode cel. | De student kan de uitkomst van één cel voorspellen vóór de functie wordt uitgevoerd. |
| 55-75 min | Bespreek `copy_board` als gegeven hulpmiddel en laat de student de volledige generatie plannen. | Er is een lus over alle cellen die leest uit `board` en schrijft naar `result`. |
| 75-90 min | Laat de student één hoek- of randstap hardop uitleggen en de blinkertransitie tekenen. | Het plan voor `next_generation` gebruikt de twee eerder geteste deelproblemen. |

De docent hoeft de buurttelling niet opnieuw als theorie te behandelen. De
waarde van het werkcollege zit in het expliciet maken van de deelproblemen en
hun contracten. Vraag bij iedere functie: welke gegevens komen erin, wat wordt
teruggegeven, en welke kleine test maakt de verwachting zichtbaar?

### Bijeenkomst 3 - kern afronden en extra kiezen

| Richttijd | Docentaccent | Product of controlepunt |
|---:|---|---|
| 0-20 min | Herneem de assertions uit de basis. Laat studenten eerst één generatie op papier voorspellen. | `count_neighbors`, `next_cell` en de blinkerassertion zijn aanwezig. |
| 20-45 min | Begeleid `next_generation`: maak de kopie eerst, lees alle cellen uit het oude bord en schrijf alleen naar het resultaat. | De verwachte horizontale blinker verschijnt en het oorspronkelijke bord is onveranderd. |
| 45-60 min | Bespreek de korte functiecompositie `generaties` alleen nadat één generatie werkt. | Twee generaties van de blinker leveren het oorspronkelijke bord op. |
| 60-70 min | Doe een kerncheck en bepaal wie aan de extra kan beginnen. | Student kan de route en het minimale eindpunt verwoorden. |
| 70-90 min | Laat studenten zelfstandig verdergaan met de extra; geef korte interventies bij de start en controleer het stopcriterium. | De student heeft de Game-of-Life-scaffolding gelezen en kiest een eerste test, of stopt verantwoord na de basis. |

De grens bij minuut 60 is bewust: een student die de basis nog niet kan testen,
gaat niet alvast de extra kopiëren. Een student die de basis groen heeft, hoeft
geen toestemming voor een facultatieve uitdaging te vragen, maar moet wel weten
dat één generatie en het onveranderde invoerbord het verplichte eindpunt zijn.

## 4. De opstap als diagnose en instap

De opstap in `source/problems/7_opstap.ipynb` bestaat uit vier korte
begripsstappen. Gebruik haar om verschillen in voorkennis zichtbaar te maken.
Een student die de eerste drie opdrachten moeiteloos en met uitleg uitvoert,
kan daarna naar de basis. Een student die nog twijfelt over rij/kolom,
verwijzing of kopiëren blijft bij de opstap tot de betreffende controle groen
is.

### Eén cel veranderen

Laat de student het 3x3-bord tekenen of afdrukken en vóór de toekenning zeggen
welke cel verandert. De juiste handeling is een directe toekenning aan
`bord[rij][kolom]`; er is geen nieuwe functie, lus of kopie nodig. Het signaal
van begrip is dat de student de precieze cel aanwijst en daarna de volledige
assertion leest.

Een veelgemaakte fout is dat de student een hele rij vervangt, of de indexen in
de verkeerde volgorde leest. Vraag dan: “Welke rij kies je eerst, en welke kolom
binnen die rij?” Laat de student de oorspronkelijke en nieuwe lijst naast elkaar
leggen.

### Twee namen, één lijst

Laat eerst `ander = bord` uitvoeren en vraag of hiermee een tweede bord is
gemaakt. Gebruik het woord *verwijzing*: beide namen wijzen naar dezelfde lijst.
Laat daarna via `ander[0][0]` muteren en vraag waarom de assertion over `bord`
juist groen wordt.

Als een student zegt dat `ander` een kopie is, laat de student de identiteit
van de twee namen niet als nieuw theorieonderwerp onderzoeken, maar opnieuw de
wijziging voorspellen en uitvoeren. Het zichtbare gevolg is hier de beste
diagnose.

### Een onafhankelijke kopie

De gegeven aanpak maakt eerst een nieuwe buitenlijst en voegt voor iedere rij
een nieuwe lijst toe met `rij[:]`. Laat studenten expliciet benoemen dat alleen
de buitenlijst kopiëren onvoldoende is: dan zouden de binnenste rijen nog
dezelfde verwijzingen bevatten.

De controle is tweezijdig: `kopie[0][0]` verandert wel, `bord[0][0]` niet.
Wanneer alleen de kopie wordt bekeken, ontbreekt precies het bewijs dat de
kopie onafhankelijk is. Vraag daarom altijd naar beide lijsten.

### Tuple en uitpakken

De tuple-oefening blijft klein. `midden_van` geeft voor een 3x3-bord
`(1, 1)` terug. Laat studenten eerst het paar lezen met indexen en daarna de
vorm `rij, kolom = midden_van(bord)` uitvoeren. Gebruik *teruggeven* voor de
waarde die de functie levert en *uitpakken* voor het toewijzen van de twee
elementen aan namen.

Laat de poging `positie[0] = 9` gecontroleerd falen. De student hoeft geen
nieuwe foutsoorten te leren; één zin volstaat: een tuple kan op een positie niet
worden gewijzigd. Als de student de tuple als een lijst probeert te behandelen,
wijs dan terug naar het contrast met de directe mutatie uit het begin van de
bijeenkomst.

## 5. De basis als verplichte kern

De basis in `source/problems/7_basis.ipynb` is de verplichte route. De volgorde
is onderdeel van de didactiek:

1. `count_neighbors` telt de acht relatieve buurposities, waarbij een positie
   buiten het bord als `0` telt.
2. `next_cell` gebruikt de buurttelling en de regels van de levende of dode cel.
3. `next_generation` maakt met de gegeven `copy_board` een onafhankelijk
   resultaat en berekent iedere cel uit het oorspronkelijke `board`.
4. `generaties` past `next_generation` herhaald toe, pas nadat één generatie
   afzonderlijk is getest.

De student moet geen nieuwe rasterregels verzinnen. De docent bewaakt vooral
dat de student het probleem niet in één grote functie probeert op te lossen.
Laat bij elke stap de interface en de assertion hardop benoemen.

### Controle van de buurttelling

Gebruik de drie gegeven gevallen als vaste controlepunten:

- hoek: `count_neighbors(bord, 0, 0) == 1`;
- rand: `count_neighbors(bord, 0, 2) == 2`;
- binnen-cel: `count_neighbors(bord, 2, 2) == 2`.

Vraag bij een fout niet meteen om de lus opnieuw te schrijven. Laat de student
de acht relatieve posities op papier zetten en markeren welke coördinaten binnen
het bord liggen. De randafspraak is steeds dezelfde: buiten het bord lezen geeft
`0`, buiten het bord schrijven gebeurt nooit.

### Controle van de celregel

De student moet voor `next_cell` eerst het onderscheid maken tussen de huidige
waarde van de cel en het aantal buren. Een levende cel blijft leven bij twee of
drie buren; een dode cel wordt levend bij precies drie buren; in alle andere
gevallen is de uitkomst `0`. Laat een student die de regels door elkaar haalt
één levende en één dode cel met hetzelfde buurtaantal vergelijken.

### Controle van de volledige generatie

De gegeven `copy_board` is de scaffolding voor de mutatiegrens. `next_generation`
moet alle cellen uit `board` berekenen en naar `result` schrijven. De minimale
bewijsset is:

- de verticale 5x5-blinker wordt de horizontale blinker;
- twee generaties brengen de blinker terug naar zijn beginstand;
- een kopie van het oorspronkelijke bord blijft gelijk na de aanroep.

Wanneer de eerste generatie bijna goed is maar het invoerbord verandert, vraag
welke lijst de student leest op het moment dat een cel wordt berekend. Een
waarschijnlijk probleem is dat de student al berekende waarden opnieuw uit het
zelfde bord leest. Laat dan de namen `board` en `result` boven de lus zetten en
per naam de lees- en schrijfactie aanwijzen.

## 6. Game of Life als zelfstandige extra

`source/problems/7_extra.md` is een volledige instap voor de extra. De student
krijgt daar het rastermodel, de randafspraak, een startbord, `copy_board`, het
functieskelet en testborden. De docent hoeft geen tweede variant van de opgave
te ontwerpen en mag de extra pas aanraden nadat de basisassertions groen zijn.

De extra bestaat inhoudelijk uit dezelfde drie deelproblemen als de basis:

- `count_neighbors(board, row, col)` telt acht relatieve posities;
- `next_cell(board, row, col)` past de Game-of-Life-regel toe;
- `next_generation(board)` leest uit het oude bord en schrijft naar een kopie.

De student krijgt daarmee scaffolding, maar de functies zijn zelfstandig werk.
Begin bij de test voor een hoek, rand en binnen-cel. Laat daarna de gegeven
verticale blinker één generatie draaien. De verwachte horizontale generatie en
de assertion dat `bord == origineel` zijn de eerste stopcontrole.

Pas daarna zijn meerdere generaties of een afdrukfunctie zinvol. Als de tijd
opraakt, stopt de student na de gegeven generatie en de assertions. Visualisatie,
extra patronen en meerdere generaties zijn facultatief. Het uitvalpad is dus
concreet: de basis eerst, vervolgens hoogstens de eerste geteste extra
generatie, en daarna stoppen zonder de student een onvolledige kern te laten
vervangen door extra werk.

Een student die meteen de extra wil doen, krijgt eerst drie vragen:

1. Welke functies uit de basis zijn al getest?
2. Waar staat de kopie die onafhankelijk van het invoerbord wordt opgebouwd?
3. Welke assertion laat zien dat de eerste generatie klopt?

Kan de student die vragen beantwoorden, laat dan zelfstandig werken. Bij een
fout vraagt de docent eerst om de betrokken hoek-, rand- of binnen-celtest te
isoleren. Geef de volledige uitwerking niet vooruit; de meegeleverde
tussenstappen zijn het bedoelde steunpunt.

## 7. Docentinterventies en verwachte fouten

| Signaal | Waarschijnlijke fout | Kleine interventie |
|---|---|---|
| Een student maakt na `bord[rij][kolom] = waarde` een tweede bord. | Directe mutatie wordt verward met kopiëren. | Vraag welke bestaande lijst de toekenning verandert en laat de student één cel vóór en na de regel aanwijzen. |
| `ander = bord` lijkt volgens de student een kopie. | De twee namen worden als twee objecten gezien. | Laat via `ander` wijzigen en voorspellen wat `bord` toont; gebruik het woord *verwijzing*. |
| Alleen de eerste rij wordt gekopieerd. | De binnenste rijen delen nog een verwijzing. | Laat zowel `kopie[0][0]` als `bord[0][0]` wijzigen of controleren; wijs op `rij[:]` voor elke rij. |
| Een tuple krijgt een nieuwe waarde op een index. | De student past lijstmutatie toe op een tuple. | Laat de gecontroleerde `TypeError` lezen en formuleer samen: lezen en uitpakken kan, wijzigen op positie niet. |
| `count_neighbors` telt de cel zelf mee. | De acht relatieve posities zijn niet gescheiden van de huidige cel. | Teken het 3x3-venster en markeer het midden als geen buur. |
| Een hoek of rand geeft een indexfout. | Buiten-het-bord is niet als `0` behandeld. | Laat alleen de geldige coördinaten voor één hoek opsommen voordat de lus wordt aangepast. |
| `next_cell` rekent met de verkeerde huidige cel. | De waarde en de buurttelling zijn door elkaar gehaald. | Vraag eerst: leeft deze cel nu, en hoeveel buren heeft zij? |
| De eerste generatie verandert ook het invoerbord. | Er wordt naar het bord geschreven waaruit nog gelezen moet worden. | Laat `board` alleen als bron en `result` alleen als doel aanwijzen. |
| De student springt direct naar meerdere generaties of visualisatie. | De facultatieve extra verdringt de basis. | Vraag om de blinkerassertion en de onveranderde-bronassertion; pas bij groen werk uitbreiden. |
| Een grote functie bevat alles tegelijk. | Deelproblemen en functiecompositie zijn nog niet toegepast. | Laat de student de invoer, uitvoer en één assertion voor één kleiner deelprobleem opschrijven. |

Houd interventies klein. De docent helpt de student de volgende controle uit te
voeren; de docent neemt de algoritmische ontwerpkeuze niet over. Laat de student
bij een fout steeds eerst een verwachting formuleren en daarna de assertion of
het kleine bord gebruiken om die verwachting te toetsen.

## 8. Controlepunten voor de docent

Gebruik deze lijst aan het einde van iedere bijeenkomst:

- [ ] De student leest `bord[rij][kolom]` in de juiste volgorde.
- [ ] De student kan het verschil tussen directe mutatie, verwijzing en een
      onafhankelijke kopie met een zichtbaar bord uitleggen.
- [ ] De student kan een tuple met `(rij, kolom)` teruggeven, indexeren en
      uitpakken.
- [ ] De drie buurttellingen voor hoek, rand en binnen-cel zijn getest.
- [ ] `next_cell` is als afzonderlijk deelprobleem getest.
- [ ] `next_generation` schrijft naar een onafhankelijk resultaat en laat het
      invoerbord onveranderd.
- [ ] De verticale blinker wordt horizontaal na één generatie.
- [ ] Twee generaties brengen de blinker terug naar de beginstand.
- [ ] De student weet dat opstap en basis verplicht zijn en Game of Life
      facultatief is.
- [ ] De student die aan de extra begint kent het stopcriterium: de gegeven
      generatie en de assertions zijn genoeg als de tijd opraakt.

Een student die aan het eind van de week de kern nog niet rond heeft, krijgt
geen opdracht om de extra af te maken. Noteer welke van de drie basisfuncties
nog niet groen is en laat de student daar verdergaan.

## 9. Overgang naar PGM2

Week 7 levert precies de voorkennis die PGM2 week 1 nodig heeft: een tuple kan
een samenhangend paar waarden bevatten en kan in één stap worden uitgepakt.
Daar wordt die vaardigheid opnieuw gebruikt bij paren uit datastructuren. De
student hoeft in deze week geen nieuwe datastructuur of methode te leren; houd
de overgang bij de tuple en het uitpakken.

Zeg bij de afronding ook expliciet waar de grens ligt: de student heeft in week
7 mutabiliteit, verwijzingen, kopiëren en functiecompositie geleerd. De volgende
PGM1-stap is niet een uitbreiding van deze extra, maar de overgang naar de
volgende cursusfase. Verwijs voor de planning naar [PGM2 week
1](../source/course/week_8.md), zonder onderwerpen uit die week alsnog als
PGM1-stof te behandelen.

## 10. Bronnen voor docentvoorbereiding

- actuele weekroute: `source/course/week_7.md`;
- college: `source/lectures/7a_lists_advanced.ipynb`;
- diagnose en instap: `source/problems/7_opstap.ipynb`;
- verplichte kern: `source/problems/7_basis.ipynb`;
- zelfstandige extra en uitvalpad: `source/problems/7_extra.md`;
- uitwerkingen voor voorbereiding: `source/solutions/7_basis.ipynb` en
  `source/solutions/7_extra.ipynb`.

Gebruik de uitwerkingen om de verwachte tussenstappen te kennen, niet als een
vervanging voor de diagnose. De studentroute blijft de bron voor wat de
student moet doen; deze handleiding beschrijft hoe je ziet of die route werkt
en wanneer je haar verkort.

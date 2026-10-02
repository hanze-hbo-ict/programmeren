# Leerlijn

Wat er per week gebeurt, welke leeruitkomsten er landen, en welke begrippen er
voor het eerst worden geïntroduceerd.

Die laatste kolom is het dragende deel van dit document. Zolang vastligt waar een
begrip voor het eerst hoort, is een vooruitverwijzing te detecteren: materiaal
dat iets gebruikt wat volgens dit document later pas komt.

Voor PGM2 is de planning voor studiejaar 2026 leidend. Voor PGM1 liggen de
onderwerpen nog niet vast; wat hieronder staat is het huidige materiaal, gemeten
aan de inhoudsopgave en aan het eerste voorkomen van begrippen in de tekst.

Dit document is voor auteurs en docenten, niet voor studenten.

## Programmeren I

De onderwerpen liggen vast. De laatste kolom is de norm voor
vooruitverwijzingen: een begrip hoort niet eerder in het materiaal voor te komen
dan de week waarin het hier staat.

| Week | Onderwerp | Leeruitkomsten | Voor het eerst geïntroduceerd |
|---|---|---|---|
| 1 | Introductie, Picobot | - | state machine, staat, regels, string, algoritme |
| 2 | Variabelen en condities | P1, P2, P3 | toekenning, variabele, operatoren, `if`, lijst, assertion |
| 3 | Functies | P5, P6, P7, A2 | functiedefinitie, parameter, docstring, `return`, `None`/`NoneType`, `TypeError`, `NameError`, stack, frame, heap, lokale variabele, module en `import`, `range`, `sum`, `choice`, iterator, signatuur, main-functie |
| 4 | Lussen | A1 | `for`, `while`, begrensde en onbegrensde lus, `break`, `continue`, het lusrecept, de operator `in`, `_` als wegwerpvariabele |
| 5 | Geneste lussen | A1, A3 | geneste lus, 2D-lijst, ASCII-art, bordrepresentatie |
| 6 | Bestanden en data | bestanden † | bits, bytes, ASCII, newline, `with open`, beeldbewerking |
| 7 | Mutabiliteit en algoritmeontwerp | P4, A3 | mutatie, functiecompositie, deelprobleem, algoritmeontwerp, tuple |

† De leeruitkomst over tekstbestanden staat nu in de PGM2-matrijs en wisselt van
plaats met recursie. Zie [leeruitkomsten.md](leeruitkomsten.md).

Vier dingen die aan deze indeling zijn veranderd, en waarom:

**Week 3 heeft een opgave met context gekregen**, de controle van een
burgerservicenummer met de elfproef. De week droeg P5, P6 en A2, en er lag nergens
iets om op terug te vallen. Zie [uitgangspunten.md](uitgangspunten.md) voor waarom
niet. Hier stond *"De week droeg P5 en A2 op het dunste materiaal van de cursus"*;
dat liet P6 weg, en de superlatief klopt niet met de woordentabel hieronder, die
week 3 derde van onder zet. Rechtgezet bij #351 op 1 oktober 2026.

**De termen zijn *begrensde* en *onbegrensde* lus.** Het materiaal noemde
`while` tot 1 september 2026 "oneindige herhaling", overgeërfd uit CS5. Dat is
onjuist en het is precies de misvatting die het materiaal verderop bestrijdt. De
vaste termen komen uit `leeruitkomsten.md` r83, waar PGM2 P1 luidt: *"Student
past begrensde en onbegrensde lusconstructies toe."* Zij staan dus in de bindende
laag, en zij dragen het onderscheid dat het lusrecept nodig heeft: bij een `for`
staat de grens vast, bij een `while` levert de schrijver hem.

**Niet *herhaling*, maar *lus*.** Een lus is een vorm van herhaling en niet een
synoniem ervoor, en `conventies/begrippen.md` schrijft *lus* voor. Dit document
schreef tot 2 september 2026 "begrensde herhaling"; dat week af van zowel de
begrippenlijst als van `leeruitkomsten.md`, dat "lusconstructies" zegt.
Vastgesteld bij de poort van #146 en rechtgezet daarna.

**Het begrip *algoritme* valt in week 1, het *ontwerpen* ervan in week 7.**
`lectures/1a_intro_programmeren.md` geeft de naam aan wat de planstap van de 3 p's
oplevert, en zonder die naam heeft die draad geen woord voor zijn eigen product.
Week 7 gaat over algoritme**ontwerp** en het opdelen in deelproblemen, en dat is
iets anders dan het begrip. Vastgesteld bij de poort van #168.

**Een docstring komt in week 2 voor zonder dat de vorm wordt uitgelegd.** De
student ziet er twee in de gegeven code bij de basisopgave, en het wóórd valt daar
ook al: `practicals/2_rochambeau.ipynb` schrijft over "comments en docstrings". Wat
een docstring *is* wordt pas expliciet gemaakt bij de functies van week 3, en
daarom staat *docstring* in de kolom van week 3 en niet van week 2. Zie
*Onderdompeling gaat vooraf aan uitleg* in [uitgangspunten.md](uitgangspunten.md).

**Recursie gaat naar PGM2 en wordt in PGM1 niet onderwezen.** PGM1 laat geen
zelfaanroepende functie zien, ook niet in week 3. De leesopdrachten daarover zijn
naar de PGM2-recursieweek verplaatst, en sinds #162 staat er in week 4 geen
recursieve functie meer: `unique` is daar iteratief. PGM2 week 3 begint daarom
bij nul, en PGM1 wordt niet aangevuld. Hier stond eerder dat week 3 bij de
functies laat zien dát een functie zichzelf kan aanroepen. Gemeten bij #332, met
een AST-scan op zelfaanroepende functies in `source/`, doet geen enkel
PGM1-bestand dat; de enige vondst buiten PGM2 is de terugvalfunctie `count_char`
in het oefententamen `extra/practice/pgm1_examen.ipynb`. Rechtgezet op besluit
van de vakdeskundige, 30 september 2026, bij de poort van #332 (VP7). De
afbakening zelf staat als besluit in [uitgangspunten.md](uitgangspunten.md).

**Binair en talstelsels vervallen**, en week 6 wordt de week van bestanden. De
beeldbewerking blijft, maar dan als wat het al is: een bestand inlezen, bewerken
en wegschrijven.

**Week 7 is de grens waar mutatie binnenkomt.** De weken daarvoor rekenen en
geven terug, en veranderen niets aan wat ze meekrijgen. Dat was tot nu toe
feitelijk zo maar nergens gezegd. Objectmethoden vallen niet op deze grens:
week 7 laat mutatie zien via `L[i] = x`, wat geen methodeaanroep vraagt. Zie
[uitgangspunten.md](uitgangspunten.md).

**Dictionaries en de Markov-opgave verhuizen naar PGM2 week 1.** CS5
introduceert dictionaries in PGM1 als een verbijzondering van een lijst,
index-gebaseerd tegenover key-gebaseerd, en scheert er verder overheen. Dat is
te weinig voor wat PGM2 er in week 1 op bouwt, dus landen dictionaries daar in
plaats van in PGM1 week 7. Methodeaanroep wordt voor het eerst geïntroduceerd
in diezelfde week, samen met sets; de Markov-opgave gaat mee. Week 7 draagt
vanaf nu de mutatiegrens, functiecompositie en algoritmeontwerp.

**Tuples landen in week 7, niet in PGM2.** Daar zijn twee redenen voor, en ze
wijzen dezelfde kant op.

Een tuple is onveranderlijk, en dat is precies het contrast dat de mutatieles
nodig heeft: naast `L[i] = x` (mag) staat dat een tuple dat niet toelaat. De
introductie hoort daarom bij dezelfde les als mutatie.

En PGM2 week 1 heeft het er nodig. Dictionaries doorlopen gaat via `.items()`,
en dat levert paren op die je uitpakt met `for word, count in ...`. Zowel het
tuple als het uitpakken ervan is daar dus veronderstelde kennis. Vastgesteld met
de docent van PGM2 op 1 september 2026.

**Het materiaal van week 7 levert dit nog niet.** Gemeten op 1 september 2026:
het woord *tuple* komt in `source/` voor in vier bestanden, en geen daarvan is
een week 7-bestand; de enige plek vóór PGM2 week 1 is `problems/5_extra.md`, de
optionele laag van week 5, ongemarkeerd. Dat is werk voor #102 en geen gebrek in
PGM2 week 1: die week mag vooruitlopen op wat hier is afgesproken. Zie de rij in
*Wat een week aan een latere week aflevert*.

### Verdeling van het opgavemateriaal

Omvang in woorden per niveau, gemeten over `problems/`, voor de weken 2 tot en
met 7. De maat: per notebook de som van `len("".join(cel["source"]).split())`
over alle cellen, en bij een `.md`-bestand het aantal woorden van het hele
bestand. Een ruwe maat, maar de verhoudingen zijn te groot om aan de meetmethode
te liggen.

Alle zes rijen zijn in één ronde hermeten, op 1 oktober 2026 bij #346, op commit
`5e4bd0ba`. Week 5 telt vijf bestanden en niet drie: `5_mandelbrot_opstap` en
`5_mandelbrot_basis` staan in `source/_toc.yml` onder de opgaven van die week en
heten in `source/course/week_5.md` verplichte kernopgaven, dus ze tellen bij opstap
en basis mee. De rijen van week 4 en week 7 komen op dezelfde getallen uit als
bij #102 en dienden hier als ijkpunt voor de meetmethode.

| Week | opstap | basis | extra | Totaal |
|---|---|---|---|---|
| 2 | 1.161 | 1.119 | 510 | 2.790 |
| 3 | 252 | 1.326 | 741 | 2.319 |
| 4 | 678 | 1.066 | 1.048 | 2.792 |
| 5 | 958 | 3.224 | 389 | 4.571 |
| 6 | 396 | 1.386 | 312 | 2.094 |
| 7 | 316 | 464 | 447 | 1.227 |
| **Totaal** | **3.761** | **8.585** | **3.447** | 15.793 |

Drie dingen vallen op.

**Extra is de kleinste van de drie lagen.** Extra meet 3.447 woorden, 21,8% van het
materiaal: 5.138 minder dan basis en 314 minder dan opstap. Hier stond eerder *"Het
zwaartepunt ligt in de optionele laag"*, met 48% en een derde meer dan basis; bij de
hermeting van week 7 voor #102 werd dat 40,5% en 257 woorden minder dan basis, en na
deze volledige hermeting is het 21,8%. Het verschil zit in week 5 en week 7: hun
extra meet 389 en 447 woorden, waar 5.354 en 3.713 stonden. In de extra zitten
Mandelbrot, Game of Life, Pi met pijltjes en tekst-naar-beeld: precies de opgaven
waarin een probleem stap voor stap wordt opgebouwd. Of het zwaartepunt hier hoort te
liggen, beslist deze meting niet; die vraag ligt bij de vakdeskundige. Zie
[uitgangspunten.md](uitgangspunten.md) voor de herverdeling die hierachter zit - de
tabel daar is van 1 september 2026 en beschrijft de toestand ervóór.

**Week 3 is de derde week van onder af.** Onderaan staan week 7 (1.227) en week 6
(2.094), dan week 3 met 2.319 woorden, ongeveer de helft van week 5 (4.571). Hier
stond dat ze na week 7 de dunste week was en bijna zes keer kleiner dan week 5, en
dat rustte op de rijen van week 3, 5 en 6 die toen achterliepen. Week 3 draagt
functies: P5, P6 en A2, samen **30%** van het tentamen. Hier stond eerder *"P5 en A2,
samen 20%"*; dat liet P6 weg, terwijl die uitkomst in de PGM1-tabel bovenaan wel bij
week 3 staat. Nagemeten tegen [leeruitkomsten.md](leeruitkomsten.md): P5 10%, P6 10%,
A2 10%, P7 zonder weging. Rechtgezet bij #198 op 11 september 2026. Wat deze omvang
bij dat gewicht betekent, beslist deze meting niet; die vraag ligt bij #356.

**De structuur is compleet.** Twee beweringen die hier eerder stonden zijn
nagemeten en bleken onjuist. Week 7 heeft wél een opstap, sinds commit
`8190d95c`; die telde er toen dertien en telt er sinds de herziening van de week
met `92df099e` vier. En de nummering van de opstap van week 5
loopt door zonder gat; dat is ze in de hele geschiedenis van
`source/problems/5_opstap.ipynb` geweest. Sinds de herziening van week 5 telt die
opstap twaalf opdrachten: acht om te lezen en vier om te schrijven.

## Programmeren II

**De planning voor 2026 is leidend.** Wat het materiaal nu doet is de
uitgangssituatie, niet de norm; het verschil tussen beide kolommen is het werk.

| Week | Leidend voor 2026 | Verantwoordelijk | Leeruitkomsten | Voor het eerst geïntroduceerd | Materiaal nu |
|---|---|---|---|---|---|
| 1 | Datastructuren (lists ter herhaling, dictionaries, sets, methodeaanroep, Markov) | BRRA | P2, A1 | dictionary, sleutel en waarde, set, methodeaanroep | Datastructuren: colleges `8a_datastructuren` (methodeaanroep en dictionaries) en `8b_taalmodel` (sets en het Markov-model), practicum `8a_text_genereren`, opstap, basis (woorden tellen) en extra (woordenschat vergelijken) (#273) |
| 2 | Comprehensions (list, dict, set, range, enumerate) | HOEM | A1; zie de opmerking bij *Voorgestelde correcties* in [leeruitkomsten.md](leeruitkomsten.md) | list comprehension, dict comprehension, set comprehension, `enumerate`, `zip`, de conditionele expressie `a if c else b` | Comprehensions: colleges `9a_list_comprehensions` (list comprehension met `range`, `enumerate`, `zip` en `a if c else b`) en `9b_dict_en_set_comprehensions` (dict en set comprehension, geneste comprehension, lus of comprehension), werkcollege `9_register`, opstap, basis (van lus naar comprehension en terug) en extra (een toernooi) (#326) |
| 3 | Recursie | HOEM | A6 | recursie, basisgeval, recursief geval, recursieve aanroep | Recursie: colleges `10a_recursie` (hoe een recursieve functie werkt, het basisgeval, frames op de stack) en `10b_recursief_ontwerpen` (basisgeval, kleiner probleem, combineren), werkcollege `10_directory_doorzoeken`, opstap (lezen en naspelen, schrijven), basis (Scrabble) en extra (potjeslatijn) (#332) |
| 4 | Use it or lose it, lambda | HOEM | A4, A6 | use it or lose it, `lambda`, functie als argument | Use it or lose it en `lambda`: colleges `11a_use_it_or_lose_it` (*use it or lose it* met `exact_change` en de knapzak) en `11b_functie_als_argument` (`sorted`, `max` en `min` met `key=`, `lambda`, een eigen functie met een functieparameter), werkcollege `11_wisselgeld`, opstap, twee basisniveaus (*Basis: algoritmen*, het nijlpaarddiner, en *Basis: lambda*, een uitslag), twee extra's (*Extra: algoritmen*, het pijlenpad, en de periodieke tshirt) en de verdiepende opdracht `caesar_op_orde` (#335). De klassenstof staat sinds #160 in week 5 |
| 5 | OO, klassen, encapsulatie | BRRA | P5, A2 | klassedefinitie, object, attribuut, constructor en `__init__`, `self`, een methode schrijven, `__repr__`, waarde en identiteit, `is`, encapsulatie, `_` voor een attribuut dat niet van buiten wordt gebruikt, `@property` en decorator, compositie | OO, klassen, encapsulatie: colleges `12a_objecten` en `12b_data_object`, practicum sessie 1 (`12_creatures`), opstap, basis (`Date`) en extra (`Board`) (#160) |
| 6 | Polymorfisme, overerving, duck typing | BRRA | A2, A3 | overerving, subklasse en superklasse, `super()`, een methode overschrijven, standaardwaarde voor een parameter, polymorfisme, duck typing, `isinstance`, `self.__class__` en `__name__` | Polymorfisme, overerving, duck typing: colleges `13a_overerving` en `13b_polymorfisme`, practicum sessie 2 (`13_creatures`), opstap, basis (kassabon) en extra (spelers voor `Board`) (#270) |
| 7 | Operator overloading, excepties, oefentoets | BRRA | P4, P6 | operator overloading, magische methode, `__eq__`, exception, `try`/`except`, `raise` | Operator overloading en exceptions: college `14a_operatoren_en_exceptions`, practicum sessie 3 (`14_creatures`), opstap, basis (`Date` met operatoren, en datums inlezen met `try`/`except`) en extra (min-max), en het oefententamen onder dezelfde week (#271) |

Een deel van deze onderwerpen komt in het huidige materiaal niet of nauwelijks
voor. Dat is bekend en verwacht: de planning beschrijft waar PGM2 heen gaat, niet
waar het staat.

**De kolom *Voor het eerst geïntroduceerd* is de norm voor vooruitverwijzingen,
net als bij PGM1.** Ze volgt *Leidend voor 2026* en niet het huidige materiaal:
een begrip hoort niet eerder voor te komen dan de week waarin het hier staat. Wat
PGM1 al levert, staat hier niet opnieuw. De woorden in de kolom zijn geen
termbesluit; welke vorm het materiaal gebruikt, staat in `conventies/begrippen.md`.
Voor week 5 is dat vastgesteld (*object*, *attribuut*, *constructor*,
*encapsulatie*, *compositie*, *waarde*, *identiteit*, *verwijzing*), en voor
week 6 ook (*overerving*, *subklasse*, *superklasse*, *overschrijven*,
*polymorfisme*, *duck typing*, #270) en week 7 (*magische methode*, *operator
overloading*, een exception *gooien*, *afvangen* en *afhandelen*, #271) en week 2
(*comprehension*, *list comprehension*, *dict comprehension* en *set
comprehension*, #326) en week 3 (*basisgeval*, *recursief geval* en *recursieve
aanroep*, #332) en week 4 (*use it or lose it*, *lambda-functie* en *functie als
argument*, #335).

**De kolom *Leeruitkomsten* wijst elke gewogen PGM2-uitkomst een week toe**,
behalve twee die in PGM1 worden onderwezen en in PGM2 worden getoetst: P1
(lussen, zie *Gaten tussen toetsing en materiaal*) en P3 (tekstbestanden, PGM1
week 6). P7 (externe bibliotheken) heeft geen weging en geen week.

**De klassenstof van week 4 gaat naar week 5.** Gemeten op 23 september 2026
gaan de lezingen `11a_objecten` en `11b_data_object`, het practicum
`11_vier_op_rij_board` (de klasse `Board`) en de basisopgave `11_basis` (de
klasse `Date`) over klassen; de extra-opgave `11_extra` (Text-ID) niet, en die
blijft in week 4. In week 5 wordt het practicum sessie 1 van
[practicum-oop.md](practicum-oop.md), en `Board` wordt de extra-opgave. Van
`11_basis` gaat alleen mee wat bij week 5 hoort: de onderdelen over operator
overloading (`__eq__`, `__lt__`, `__gt__`, `__iadd__`, `__isub__`, `__sub__`)
horen bij week 7. Het AI-materiaal van week 5, `12_ai` en `12_vier_op_rij_AI`,
verdwijnt uit die week naar een plek buiten `source/`. Week 4 houdt daarna alleen
Text-ID en heeft nog geen materiaal voor *use it or lose it* en `lambda`.
Besloten bij de voorbereiding van de poort van #160, en **uitgevoerd** in #160.
Sinds #332 staat het algoritmemateriaal uit week 3 in week 4, naast Text-ID.
Sinds #335 is week 4 herzien en staat Text-ID niet meer in week 4; zie hieronder.

**Week 2 is de week van comprehensions; het recursiemateriaal staat tijdelijk in
week 3.** Tot #326 ging het materiaal van week 2 over recursie, terwijl de
planning daar comprehensions zet en recursie in week 3. Bij #326 besloot de
vakdeskundige op 30 september 2026: *"Alleen week 2."* Week 2 kreeg nieuw
materiaal over comprehensions. Het recursiemateriaal verhuisde ongewijzigd naar
week 3, in de inhoudsopgave en op de weekpagina, en staat daar naast het
knapzak- en wisselgeldmateriaal; herzien is het niet. De zes bestanden kregen
een naam van week 10: `lectures/10b_intro_recursie`, `lectures/10c_recursief`,
`practicals/10_recursieve_functies` en `problems/10_recursie_opstap`,
`10_recursie_basis` en `10_recursie_extra`. Dat de gepubliceerde URL's daardoor
veranderen, is aanvaard (VP5). Week 3 draagt daarom tijdelijk twee onderwerpen,
met twee reeksen niveaus die in de inhoudsopgave het onderwerp in hun titel
hebben. Tijdelijk, omdat week 3 en 4 op de planning brengen een apart werkitem
is. **Uitgevoerd** in #326. Het tijdelijke is met #332 opgeheven; zie de alinea
hieronder.

**Week 3 is de week van recursie; het algoritmemateriaal staat in week 4.** Bij
#332 besloot de vakdeskundige op 30 september 2026 over de afbakening: *"Alleen
week 3."* Het recursiemateriaal is herzien. Het algoritmemateriaal verliet week 3
en staat ongewijzigd in week 4; week 4 zelf is niet herzien. Week 4 op de
planning brengen, met *use it or lose it* en `lambda`, is een apart werkitem. Bij
de poort van #332 besloot de vakdeskundige verder:

- het oefenbestand `extra/practice/1_recursie.ipynb` is bron voor de
  schrijfopdrachten in de opstap, en is daarna verwijderd; de Support-pagina
  `extra/examples/recursie.md` blijft, met Nederlandse docstrings en de termen
  hieronder (VP1);
- de termen zijn *basisgeval* en *recursief geval*, naast *recursieve aanroep*
  voor de aanroep zelf. *Base case*, *recursieve case*, *recursie case* en
  *recursive case* verdwijnen uit het materiaal van week 3. Het verhuisde college
  `11a_knapzak_probleem`, `caesar_op_orde` en het bevroren oefententamen, met
  uitwerking, zeggen *base case* tot hun eigen herziening (VP2; zie
  `conventies/begrippen.md`);
- de bestanden van week 3 heten `lectures/10a_recursie`,
  `lectures/10b_recursief_ontwerpen`, `practicals/10_directory_doorzoeken` en
  `problems/10_opstap`, `10_basis` en `10_extra`; die van week 4
  `lectures/11a_knapzak_probleem`, `practicals/11a_wissel_geld`,
  `practicals/11b_periodieke_tshirt`, `problems/11_algoritmen_basis` en
  `problems/11_algoritmen_extra`. Aanvaard is dat `/problems/10_basis` en
  `/problems/10_extra` sindsdien recursie tonen, waar eerst algoritmen stonden
  (VP3);
- het werkcollege wordt *een directory doorzoeken*, naar het model van
  `9_register`, met uitwerking. De verzamelingsbewerkingen op lijsten en de ggd
  via delers vervallen; het algoritme van Euclides staat in het tweede college
  (VP4);
- de laatste opdracht van de opstap oefent dezelfde functie als lus, als list
  comprehension en recursief, gemarkeerd als voorbereiding op het oefententamen.
  Dat is de enige plek waar week 3 recursie naast een lus zet (VP5);
- `caesar_op_orde` staat ongewijzigd in week 4, onder `opgaven_11` (VP6);
- het tweede college sluit af met een gemarkeerde vooruitblik op week 4, zonder
  de term *use it or lose it*; zie *Vooruitverwijzingen om na te lopen* (VP8).

**Week 4 is de week van *use it or lose it* en `lambda`.** Tot #335 stond in
week 4 alleen het algoritmemateriaal uit week 3, ongewijzigd: een college over
*use it or lose it* (`rem_all`, `rem_one`, `rem_up_to` en de subset-knapzak), een
practicum over wisselgeld (`exact_change`, `num_coins`, `min_coins`) met de
periodieke tshirt als tweede opdracht, een basis (het nijlpaarddiner) en een extra
(het pijlenpad), naast Text-ID en `caesar_op_orde`, zonder opstap, zonder `lambda`
en zonder uitwerkingen van de twee algoritmeniveaus. Bij #335 besloot de
vakdeskundige op 2 oktober 2026, bij de poort:

- twee colleges: `11a_knapzak_probleem` is herzien tot `11a_use_it_or_lose_it`, en
  er is een nieuw college `11b_functie_als_argument` (VP1). Het ritme is dat van
  week 2 en 3: eerst `11a`, dan `11b`, en het werkcollege als derde bijeenkomst.
  HOEM heeft het rooster niet vooraf bevestigd; wijkt het later af, dan verandert
  alleen de weekpagina (VP10);
- `11a` opent met de vooruitblik uit `10b` en behandelt `exact_change` en `subset`.
  De top-down-reeks, `rem_all`, `rem_one`, `rem_up_to` en de eigen `def max`
  vervallen; `11a` introduceert de ingebouwde `max` met twee argumenten.
  `caesar_op_orde` geeft `rem_one` zelf (VP2);
- wisselgeld is het werkcollege `11_wisselgeld`, in stapvorm en met uitwerking,
  zonder `key=`. De periodieke tshirt blijft in week 4, als extra opgave. Of
  `num_coins` en `exact_change` bijdragen aan het werkcollege of een basisopgave
  worden, liet de vakdeskundige aan de auteur, binnen twee voorwaarden: geen functie
  wordt in twee onderdelen van week 4 als nieuwe taak gevraagd, en de eigenaardigheid
  van `num_coins`, 0 voor *onmogelijk* én voor bedrag 0, is opgelost of verantwoord
  (VP3);
- de niveaus: `11_opstap` over `lambda` en functie als argument, met een deel
  waarin de student *use it or lose it* naspeelt; twee basisniveaus, *Algoritmen:
  basis* (`11_algoritmen_basis`) en *Lambda: basis* (`11_lambda_basis`); en
  *Algoritmen: extra* (VP4). Het model voor twee basisniveaus met het onderwerp in
  de bestandsnaam is PGM1 week 5 (`5_basis` naast `5_mandelbrot_basis`). Elk
  basisniveau heeft een eigen context; week 4 wijkt daarmee af van *Eén opgave over
  drie niveaus* in [uitgangspunten.md](uitgangspunten.md);
- Text-ID (`problems/11_extra`) gaat uit week 4 en is verwijderd: het onderwerp is
  dat van week 1, en de tekst staat grotendeels al in `8a_text_genereren`.
  `problems/assets/file_and_dictionary_examples.py` blijft, want
  `8a_text_genereren` en `opdrachten/tekst_genereren` gebruiken het ook (VP5);
- `caesar_op_orde` blijft één verdiepende opdracht onder *Opgaven*: geen niveau en
  zonder uitwerking. `exact_change` is eruit, `decipher` kiest de beste rotatie met
  `max(..., key=...)`, en de bonusopgave is een gewone laatste functie zonder punten
  (VP6);
- het nijlpaard volgt de regel afstand ≥ k, en het tweede voorbeeld geeft 3 (VP7).
  Zoals het goedgekeurde ontwerp voorstelde, levert de opgave de plaatsen oplopend
  aan, zodat ze geen `sorted` vraagt;
- de termen *use it or lose it*, *lambda-functie* en *functie als argument* staan in
  `conventies/begrippen.md` (VP8);
- het werk is in één oplevering uitgevoerd (VP9).

**Uitgevoerd** in #335, met deze keuzes van de auteur. `num_coins` en `exact_change`
dragen bij aan het werkcollege, niet aan een basisopgave. `exact_change` staat
daar alleen als gegeven code uit het college, niet als taak. `num_coins` is de
eerste stap: het geeft `-1` als het bedrag niet kan, zodat 0 alleen nog voor bedrag
0 staat, en het neemt de eerste manier die lukt. `min_coins` is de tweede stap en
vergelijkt beide keuzes; samen laten ze zien waarom je voor het beste antwoord
beide keuzes moet proberen. De periodieke tshirt is `problems/11_tshirt_extra`, met
de titel *Periodieke tshirt: extra* en een uitwerking, in drie stappen:
`is_element`, `can_spell` en `count_spellings`. Week 4 heeft daarmee twee extra's,
elk met een eigen context. De basis over algoritmen bouwt `hippo_dinner` op in drie
stappen, de extra over het pijlenpad `arrow_path` in vijf; in het eerste
pijlenpadvoorbeeld is de dubbele 1 een 0 geworden, zoals in het plaatje. `11a`
sluit af met twee opdrachten (`count_ways` en `most_items`), `11b` met twee (een
afspeellijst sorteren en `count_matching`). `11b` verbindt de twee onderwerpen met
`subset_items` en `max(use_it, lose_it, key=sum)`.

Na de beoordeling besloot de vakdeskundige op 2 oktober 2026, in
[PR #360](https://github.com/hanze-hbo-ict/programmeren/pull/360#issuecomment-5951946263):
*"Maak de paginatitels basis en extra onderscheidend."* Na de nalezing besloot de
vakdeskundige dezelfde dag dat die titels met het niveauwoord beginnen, zoals in
PGM1 week 5 (`# Basis: Mandelbrot op een raster`):
*"Draai de volgorde hier om, zodat het ook met niveau begint"*
([PR #360](https://github.com/hanze-hbo-ict/programmeren/pull/360#issuecomment-5952253135)).
De titels zijn daarmee *Basis: algoritmen*, *Basis: lambda*, *Extra: algoritmen*
en *Extra: periodieke tshirt*; de eerdere titels hierboven zijn daardoor
vervangen.
Het niveauwoord staat erin, zoals [begrippen.md](../conventies/begrippen.md),
*De drie opgaveniveaus*, vraagt.

**Uitgevoerd** in #335, met deze keuze van de auteur: de eerste kop van de vier
niveaubestanden en van hun uitwerkingen is gelijk aan hun titel in de
inhoudsopgave. Alleen in week 4 hadden twee niveaubestanden dezelfde kop; andere
weken zijn niet aangepast.

**Uitgevoerd** in #332, met deze keuzes van de auteur: de basis heeft één
context, Scrabble, en `transcribe` is vervallen; de extra is potjeslatijn in drie
stappen.

**De opzet van week 2.** Besloten door de vakdeskundige op 30 september 2026,
bij de poort van #326:

- *"twee colleges; het werkcollege is het derde college"* (VP4);
- een extra-opgave, *"maar liever niet weer opnieuw over tekst vergelijken.
  Bedenk iets creatiefs om met wat complexere comprehensions te doen (bv genest
  of meerdere types combineren)"* (VP6). De extra heeft daarmee een andere
  context dan de basis, en wijkt voor deze opgave af van *Eén opgave over drie
  niveaus* in [uitgangspunten.md](uitgangspunten.md);
- het losse oefenbestand over list comprehensions in `extra/practice/` is bron
  voor het nieuwe materiaal en wordt daarna verwijderd, met zijn afbeelding
  (VP1): week 3 en 4 gaan niet over comprehensions.

Uitgevoerd in #326, met deze keuzes van de auteur: het eerste college behandelt
de list comprehension, met een filter, `range`, `enumerate`, `zip` en de
conditionele expressie; het tweede dict en set comprehensions, de lijst van
lijsten en de geneste comprehension, en wanneer een lus de betere keuze blijft.
De context van de extra is een toernooi.

**Welke syntaxis week 2 draagt.** Een comprehension met één `for` en een
optioneel filter, over een lijst, een string, `range`, `.items()`, `enumerate`
en `zip`; de conditionele expressie `a if c else b`, ook in de expressie van een
comprehension; en de geneste comprehension, een comprehension in een
comprehension. Twee `for`-clausules in één comprehension komen niet in de week;
de vakdeskundige: *"Dubbele for hoeft niet (dat kan denk ik altijd geschreven
worden als een geneste lc)"*. Generator expressions ook niet: *"je kan in sum ook
een echte lc stoppen immers"*; waar een som of telling nodig is, gebruikt het
materiaal `sum([...])` met een list comprehension. Een ongebruikte lusvariabele heet `_`,
ook in een comprehension (`conventies/codeconventies.md`). `zip` en
`a if c else b` zijn daarmee nieuwe syntaxis van week 2, en staan zo in de tabel
hierboven en in de tabel *Welk niveau een week hoort te hebben*. Vastgesteld door de
vakdeskundige op 30 september 2026, bij de poort van #326 (VP7).

**Excepties landen in week 7**, naast operator overloading. Vastgesteld bij de
voorbereiding van de poort van #160; zie *Gaten tussen toetsing en materiaal*.
De eigen opgave voor het afvangen staat in de **basisopgave**: de constructor van
`Date` gooit een `ValueError` bij een datum die niet bestaat, en de student zet
een lijst datumstrings om naar `Date`-objecten en vangt de ongeldige af. De
syntaxis staat in de opstap. Het practicum gooit alleen exceptions en vangt er
geen af (`practicum-oop.md`). Vastgesteld door de vakdeskundige op 25 september
2026, bij de poort van #271 (VP1).

**`NotImplemented` komt niet in de leerlijn.** Een operator van een eigen klasse
die een argument van een ander type krijgt, geeft bij `__eq__` `False` terug; de
andere operators controleren het type met `isinstance` en gooien een
`TypeError`. Dat `a > b` werkt met alleen `__lt__`, legt het materiaal uit
zonder dat de student `NotImplemented` schrijft. Vastgesteld door de
vakdeskundige op 25 september 2026, bij de poort van #271 (VP8); dit wijkt af van
de code in sessie 3 van `practicum-oop.md`.

**Min-max is de extra-opgave van week 7.** De extra-opgaven van week 5 tot en met
7 vormen één lijn over objectgeoriënteerd programmeren, en min-max sluit die af.
Week 5 levert `Board`. Week 6 levert in `problems/13_extra.md` de spelers die
`Board.host_game(px, po)` polymorf gebruikt, waaronder `SimpleAIPlayer`, die één
zet vooruitkijkt. Week 7 voegt de min-max-speler toe, op basis van
`practicals/13_vier_op_rij_speler.md` en de sectie *Min-max* van
`lectures/12_ai.ipynb`. Min-max past niet helemaal bij het onderwerp van week 7;
`__lt__` kan dienen om bordtoestanden te vergelijken. Het vraagt recursie, en die staat
sinds week 3 ter beschikking. Vastgesteld door de vakdeskundige op 23 september
2026; week 6 is **uitgevoerd** in #270, week 7 in #271.
Op 24 september 2026 voegde de vakdeskundige toe: min-max past goed bij de
extra-opgaven van week 5 en 6. Heropenen als die worden vervangen.

Bij de poort van #271 (25 september 2026) besloot de vakdeskundige over de
uitvoering. Min-max wordt uitgelegd in de extra-opgave zelf; de sectie *Min-max*
komt niet terug in een college, en de genetische algoritmen uit `12_ai` blijven
buiten `source/` (VP3). Het toernooi vervalt ook in week 7 (VP2). `Board` krijgt
een methode `score()` met een absolute schaal: `-100` als X wint, `0` bij
onbeslist, `100` als O wint. De recursie geeft waarden op die schaal terug; X
kiest het minimum en O het maximum. Dat vervangt de schaal 0/50/100 en *"100 min
de beste score van de tegenstander"*. De min-max-speler is een subklasse van
`Player` met de constructor `(ox, tbt, ply)`, en `host_game` verandert niet.
`next_move` maakt voor elke kolom waarin een zet mag een `ScoredMove(col,
waarde)`, een kleine klasse met `__lt__` en `__eq__`; X bepaalt de beste waarde
met `min`, O met `max`, en uit de zetten met die waarde kiest `tiebreak_move`
volgens `tbt`: `'LEFT'`, `'RIGHT'` of `'RANDOM'` (VP10). **Uitgevoerd** in #271, in
`problems/14_extra.md`; `practicals/13_vier_op_rij_speler.md` staat sinds #271
buiten `source/` (VP11).

**Compositie hoort bij week 5.** Week 5 past het begrip sinds #160 al toe:
`Party` in het practicum `12_creatures` (stap 5) bewaart `Creature`-objecten in
`self._members` en stuurt ze aan via hun methoden. Het besluit legt dus vast wat
er al staat. De term is *compositie*, omdat dat de gangbare term is; wat het
begrip inhoudt en welke varianten zijn afgewezen, staat in
`conventies/begrippen.md`. *Functiecompositie* uit PGM1 week 7 wordt voluit
geschreven, zodat de twee begrippen uit elkaar blijven. Aggregatie wordt niet
benoemd: het voegt in week 5 niets toe wat *waarde en identiteit* niet al dekt.
Vastgesteld door de vakdeskundige op 23 september 2026, met #267, en
**uitgevoerd** in #268.

**De standaardwaarde voor een parameter hoort bij week 6.** Week 5 vermeed haar
bij `Party`, omdat het begrip niet in de leerlijn stond (`practicum-oop.md`).
Sessie 2 en 3 van het practicum steunen er wel op: `attack(target, bonus=0)`, de
constructors van `Dragon`, `Wolf`, `Goblin` en `Healer`, en `Dragon("Ember")` in
sessie 3. Week 6 introduceert haar daarom, in de opstap en in het college
`13a_overerving`. Vastgesteld door de vakdeskundige op 24 september 2026, bij de
poort van #270, en **uitgevoerd** in #270.

**`isinstance`, `self.__class__` en `__name__` horen bij week 6.** Ze gaan over
de klasse van een object, en daarmee over polymorfisme. Week 6 introduceert ze in
het college `13b_polymorfisme` en in het practicum `13_creatures`: `__repr__` van
`Creature` gebruikt voortaan `self.__class__.__name__`, zodat een `Dragon` zich
als `Dragon(...)` afdrukt. `isinstance` wordt ingevoerd naast duck typing: code
die met `isinstance` controleert, laat een object dat alleen de goede methoden
heeft niet meer meedoen. Daarom blijven `battle_round` en `host_game` zonder die
controle. Week 7 gebruikt `self.__class__(...)` in `Creature.__mul__`. Dit
herroept de keuze bij de poort van #270 dat `type(self).__name__` in week 6
vermeden wordt (V10). Vastgesteld door de vakdeskundige op 25 september 2026, bij
de poort van #271 (VP7 en VP8). Op 25 september 2026, bij de herstelronde van #271,
besloot de vakdeskundige dat ze ook in de opstap van week 6 komen: *"Ja, ook in de
opstap"*. Daarom staan ze ook in de tabel onder *Welk niveau een week hoort te
hebben*, bij de syntaxis die de opstap van week 6 draagt.

## Welk niveau een week hoort te hebben

De niveaus zelf staan in [uitgangspunten.md](uitgangspunten.md); hun namen in
`conventies/begrippen.md`. Hier staat *wanneer* een niveau verplicht is.

| Niveau | Wanneer verplicht |
|---|---|
| **basis** | Elke week die een leeruitkomst draagt. Basis is toetsniveau: draagt een week een leeruitkomst en heeft ze geen basis, dan wordt er getoetst op iets waar niet mee geoefend is |
| **opstap** | Elke week die nieuwe syntaxis introduceert. Een vingeroefening zonder nieuwe syntaxis is oefenen op niets |
| **extra** | Nooit verplicht |

**PGM1 is hiermee ingevuld.** Week 1 draagt geen leeruitkomst en introduceert
geen Python - Picobot heeft een eigen regeltaal - en hoort dus geen opstap en
geen basis te hebben. Dat week 1 geen opgaven heeft is daarmee geen gat maar de
juiste uitkomst, en dat hoort te staan waar de volgende het terugvindt; zonder
deze zin leest iedere volgende lezer het als een gat. De weken 2 tot en met 7
dragen elk een leeruitkomst en introduceren elk nieuwe syntaxis: daar zijn opstap
en basis allebei verplicht en is extra facultatief. Gemeten in
`source/problems/` op 8 september 2026 hebben die zes weken alle drie de niveaus,
dus er ontbreekt niets.

**PGM2 is hiermee ook ingevuld.** Dit stond uitgesteld zolang niet vaststond wát
elke PGM2-week behandelt. Sinds de PGM2-tabel een leeruitkomst en de nieuwe
begrippen per week noemt, is de regel toe te passen. Elke PGM2-week draagt een
leeruitkomst, dus basis is overal verplicht. Opstap is verplicht behalve in
week 3: recursie vraagt geen nieuwe syntaxis, want een recursieve functie is een
gewone `def` die zichzelf aanroept.

| PGM2-week | Verplicht | Nieuwe syntaxis die de opstap draagt |
|---|---|---|
| 1 | opstap, basis | dictionary- en set-literals, methodeaanroep |
| 2 | opstap, basis | comprehensions, `zip`, de conditionele expressie `a if c else b` |
| 3 | basis | - |
| 4 | opstap, basis | `lambda`, functie als argument |
| 5 | opstap, basis | `class`, `__init__`, `self`, `@property` |
| 6 | opstap, basis | subklasse, `super()`, standaardwaarde voor een parameter, `isinstance`, `self.__class__.__name__` |
| 7 | opstap, basis | magische methoden, `try`/`except`, `raise` |

Een bestaand niveau telt alleen als het over het onderwerp van *Leidend voor
2026* gaat. Gemeten in `source/problems/` op 23 september 2026 hebben de weken 1
en 2 opstap, basis en extra, de weken 3 en 4 basis en extra, en de weken 5 tot en
met 7 niets. Maar de opgaven van week 2 gaan over recursie en die van week 4 over
klassen, dus die tellen voor een andere week. Wat een week mist, stelt de
herziening van die week vast. Vastgesteld door de vakdeskundige op 23 september
2026. Sindsdien hebben de weken 5, 6 en 7 opstap, basis en extra gekregen, in
werkitem #160, #270 en #271, en week 2 in #326; de opgaven over recursie staan
sinds #326 in week 3. Sinds #332 heeft week 3 opstap, basis en extra over
recursie, en staan de basis en de extra over algoritmen in week 4, naast Text-ID.
Sinds #335 heeft week 4 een opstap, twee basisniveaus en twee extra's over *use it
or lose it* en `lambda`, en is Text-ID weg.

**Wat er wél uit volgt: één ontbrekende niveau-uitwerking.** Dat volgt niet uit
de regel hierboven maar uit het besluit *Elk opgaveniveau hoort een uitwerking te
hebben*, dat elk **bestaand** niveau bindt en dus onafhankelijk is van welke
niveaus een week verplicht heeft. De meting telt 43 niveau-opgaven in
`source/problems/`, waarvan 42 een gelijknamige uitwerking in `source/solutions/`
hebben en 1 nog niet. Dit is
werkitem #194 en geen werk voor de herziening van dit document. Die ene
ontbrekende uitwerking is de opstap van PGM2 week 1 (`8_opstap`). Hermeten bij
werkitem #335: vóór #335 41, 37 en 4; #335 gaf de basis en de extra over
algoritmen een uitwerking, verwijderde Text-ID (`11_extra`), en voegde
`11_opstap`, `11_lambda_basis` en `11_tshirt_extra` toe, alle drie met
uitwerking: 43, 42 en 1. Tot #335 hoorden bij de ontbrekende ook de drie niveaus
van PGM2 week 4: de basis en de extra over algoritmen (`11_algoritmen_basis` en
`11_algoritmen_extra`, tot #332 `10_basis` en `10_extra`) en de extra Text-ID
(`11_extra`). Hermeten bij #102: 41, 36 en 5 werden 41, 37 en 4, want #102
voegde de uitwerking van de opstap van PGM1 week 7 toe. Hermeten bij #332: vóór #332
41, 33 en 8; #332 voegde uitwerkingen toe voor opstap, basis en extra van
PGM2 week 3 en verhuisde de twee algoritmeniveaus zonder uitwerking naar week 4:
41, 36 en 5. Tot #332 hoorden daar ook de opstap, de basis en de extra over
recursie bij (`10_recursie_*`, tot #326 `9_*`). Hermeten bij #160: hier
stond 30, 19 en 11, maar vóór #160 waren het er al 30, 20 en 10, omdat de opstap
van week 5 inmiddels een uitwerking had. #160 haalde `11_basis` weg en voegde
opstap, basis en extra van PGM2 week 5 toe, alle drie met uitwerking. Hermeten
bij #270: 32, 23 en 9 werden 35, 26 en 9, want #270 voegde opstap, basis en
extra van PGM2 week 6 toe, alle drie met uitwerking. Hermeten bij #271: 38, 29 en
9, want #271 voegde opstap, basis en extra van PGM2 week 7 toe, alle drie met
uitwerking. Hermeten bij #326: vóór #326 waren het 38, 30 en 8, en niet 38, 29 en
9; de kop zei toen negen en de lopende tekst 35, 27 en 8. #326 voegde opstap,
basis en extra van PGM2 week 2 toe, alle drie met uitwerking: 41, 33 en 8. De
maat: elk bestand in `source/problems/` waarvan de naam zonder extensie eindigt
op `_opstap`, `_basis` of `_extra`, met of zonder gelijknamig bestand in
`source/solutions/`. College- en
practicumopdrachten vallen niet automatisch onder deze norm.

## Volgorde van het werk

**Eerst wordt PGM1 herzien, met de PGM2-lijn als randvoorwaarde.**

Dat betekent dat PGM1 niet op zichzelf ontworpen wordt: wat PGM2 in week 1
veronderstelt, moet PGM1 hebben geleverd. Bij elke keuze in PGM1 is de vraag dus
niet alleen of ze op zichzelf klopt, maar ook of ze de bovenstaande lijn
ondersteunt.

De onderwerpen voor PGM1 liggen nog niet vast; de tabel hierboven voor PGM1
beschrijft het huidige materiaal. Ze vaststellen is het eerste inhoudelijke werk,
en de twee gaten hieronder horen daarin te worden meegenomen.

## Gaten tussen toetsing en materiaal

Gemeten op het voorkomen van de betreffende constructies in `source/`.

| Leeruitkomst | Weging | Bevinding | Besluit |
|---|---|---|---|
| **PGM2 P3** tekstbestanden | 10% | Drie plekken, waarvan twee in de Markov-opgave van PGM1 week 7. | Naar PGM1 week 6 |
| ~~**PGM1 A4** recursie~~ | | **Uitgevoerd op 1 september 2026**: staat nu als PGM2 A6. Wat resteert is de 10% die in PGM1 vrijkomt. | Zie `leeruitkomsten.md`, *Voorgestelde correcties* |
| **PGM2 P4** excepties | 10% | Bij de herziening van week 5 is `try`/`except` uit de gegeven code van `problems/5_basis` gehaald; de menukeuze wordt daar nu als string vergeleken. Excepties worden nergens in PGM1 onderwezen. | PGM2 week 7, naast operator overloading; vastgesteld op 23 september 2026, **uitgevoerd** in #271: opstap, college en basisopgave |
| **PGM2 P1** lussen | 5% | Wordt in PGM1 onderwezen (week 4 en 5) en in PGM2 getoetst. Kan bedoeld zijn als herhaling, maar staat niet in de planning voor 2026. | open |
| **PGM2 A5** finite state machines | geen | Komt nergens voor. | Schrappen; zie [leeruitkomsten.md](leeruitkomsten.md) |

Van de twee gaten die samen 20% van het PGM2-tentamen zijn, zijn er daarmee twee
belegd. Excepties behandelt PGM2 sinds #271 in week 7.

## Vooruitverwijzingen om na te lopen

Begrippen die eerder in het materiaal opduiken dan waar ze volgens de leerlijn
thuishoren. Niet elk geval is fout; een vooruitwijzing kan bewust zijn, mits ze
als zodanig is gemarkeerd.

| Begrip | Hoort in | Duikt op in | Opmerking |
|---|---|---|---|
| `while` | PGM1 week 4 | PGM1 week 2, `practicals/2_rochambeau` | Bewust; de tekst zegt erbij dat lussen later komen |
| `choice`, en daarmee `import` | PGM1 week 3 | PGM1 week 2, `practicals/2_rochambeau` en `solutions/2_rochambeau` | Bewust; de opgave geeft de regel in de begincode met de uitleg als commentaar erachter, en de uitwerking zegt erbij hem voor nu aan te nemen. Vastgesteld door de vakdeskundige, 15 september 2026 |
| `time.sleep` en math-functies | PGM1 week 3 | PGM1 week 2, `problems/2_basis`, `solutions/2_basis`, `problems/2_extra` en `solutions/2_extra` | Bewust; als gegeven begincode, met de uitleg als commentaar erachter. Vastgesteld door de vakdeskundige, 16 september 2026 |
| functie als argument (`key=`) | PGM2 week 4 | PGM2 week 2, laag extra, `problems/9_extra` | Bewust; als vooruitblik aan het eind, met een functieverwijzing en zonder lambda, niet om te schrijven. Vastgesteld door de vakdeskundige, 30 september 2026. Ingelost in `lectures/11b_functie_als_argument` (#335), dat naar de vooruitblik terugverwijst |
| *use it or lose it*: bij elk element kiezen of je het gebruikt, met twee recursieve aanroepen | PGM2 week 4 | PGM2 week 3, `lectures/10b_recursief_ontwerpen`, *Tot slot* | Bewust; als gemarkeerde vooruitblik aan het eind (*kan ik dit bedrag precies betalen?*), zonder de term, niet om te schrijven. Vastgesteld door de vakdeskundige, 30 september 2026, bij de poort van #332 (VP8). Ingelost in `lectures/11a_use_it_or_lose_it` (#335), dat met die vraag opent |
| functiedefinitie | PGM1 week 3 | PGM1 week 2, `problems/2_basis` | Als gegeven code, niet om te schrijven. De docstring in datzelfde blok is onderdompeling; of dat ook voor de `def` geldt is nog niet besloten |
| tuple | PGM1 week 7 | PGM1 week 5, laag extra, `problems/5_extra.md` | Ongemarkeerd; introduceert ook *methode* en *object*. Buiten bereik van de herzieningen in #102/#134 |

De rij over list comprehension wees tot #326 naar `practicals/6b_images`. Daar
staat sinds `d85d30a` (24 september 2026) geen comprehension meer; de rij wees
daarna naar de uitwerking van de extra-opgave van dezelfde week, waar de
vakdeskundige er een zag en waar ook een generator expression stond. Die twee
zijn in #328 vervangen door `for`-lussen en de rij is geschrapt. PGM1 week 6
heeft nu geen comprehension en geen generator expression meer. Gemeten op
1 oktober 2026 met een AST-scan (list-, set- en dict-comprehension en
generator expression) over de codecellen en `python`-blokken van de twaalf
bestanden van week 6 (`lectures/6*`, `practicals/6*`, `problems/6_*`,
`solutions/6_*`, `course/*6*`): twee treffers vóór de wijziging, beide in
`solutions/6_extra.ipynb`, nul erna. Geschrapt op besluit van de vakdeskundige,
30 september 2026, bij de poort van #326 (VP8): die vorm moet uit week 6, ook
als `for`-lus.

Twee regels stonden hier eerder en zijn nagemeten en geschrapt.

**2D-lijst in `problems/3_opstap`.** Nagemeten bij de herziening van week 5, met
een patroon op dubbele indexering en een patroon op een 2D-literal: beide geven
nul treffers op dat bestand. De enige treffer op het woord was het stringliteraal
`x = function("lol")`. Er staat daar geen 2D-lijst.

**`lectures/4b_midterm` opdracht 19**, die de student vroeg de uitvoer te
voorspellen van een lus die `my_list[ix]` overschrijft. Die is herschreven met
het patroon `result = result + [...]`, hetzelfde patroon dat opdracht 18 ernaast al
gebruikte. Het goede antwoord is niet veranderd.

Deze lijst is met tekstpatronen gemaakt en dus indicatief. Ze is het uitgangspunt
voor de controle die dit wil mechaniseren, niet het eindoordeel.

## Wat een week aan een latere week aflevert

Wat in de ene week wordt geleerd en in een latere week nodig is, staat hier. Zo
blijft een raakvlak vindbaar zonder dat het in een werkitem verstopt zit.

| Van week | Naar week | Wat | Status |
|---|---|---|---|
| PGM1 week 7 | PGM2 week 1 | Week 7 levert **tuples en tuple unpacking**. PGM2 week 1 doorloopt dictionaries met `.items()` en pakt de paren uit met `for word, count in ...`; `lectures/8a_datastructuren.ipynb` verwijst er expliciet naar terug. Het materiaal van week 7 bevat op dit moment geen enkele tuple. | Besloten met beide docenten op 1 september 2026. Uit te voeren bij de herziening van week 7 (#102). PGM2 week 1 loopt hier met opzet op vooruit; dat is geen defect in die week. |
| PGM1 week 4 | PGM2 week 1 | Week 4 levert de termen **begrensde** en **onbegrensde lus**, die `leeruitkomsten.md` r83 als PGM2 P1 toetst (5%, toepassen). Het materiaal gebruikte ze tot 1 september 2026 nergens. | Besloten bij de poort van #146, uit te voeren in datzelfde werkitem. |
| PGM1 week 4 | PGM1 week 5 | Week 4 levert het **lusrecept**: vijf vragen waarvan de **vierde** het stopmoment is (*"Wanneer is het klaar?"*); de vijfde gaat over wat je teruggeeft. Week 5 bouwt erop voort met geneste lussen, en `unique` sluit week 4 af op precies het probleem dat week 5 opent - een lus in een lus. | Besloten bij de poort van #146. |
| PGM1 week 5 | PGM2 week 7 | De vier zoekfuncties uit `practicals/5b_boter_kaas_eieren.ipynb` hebben andere parameternamen dan de gelijknamige functies in `board.py` regels 173-224, tot #271 `source/problems/assets/board.py` en sindsdien `practicals/assets/board.py`. | Besloten, laten zoals het is: `board.py` definieert ze zelf en importeert het werk van de student nooit. Zie het besluitenregister in [uitgangspunten.md](uitgangspunten.md). Tot #270 stond hier PGM2 week 6. Sinds #271 staan `board.py` en `practicals/13_vier_op_rij_speler.md`, het enige bestand dat het aanbiedt, buiten `source/` in `practicals/` (VP11); het raakvlak met het boek is daarmee vervallen. |
| PGM1 week 5 | PGM1 week 7 | Week 5 levert `create_board` en `print_board` als vermogen; `source/problems/7_extra.md` regels 36-114 leert ze nu vanaf nul aan. | Voorstel: laat week 7 ernaar verwijzen in plaats van ze opnieuw aan te leren. |
| PGM1 week 5 | PGM1 week 7 | `[[0] * 3] * 3` en de waarschuwing daarbij horen in week 7, naast aliasing en `deepcopy`. De constructie bijt pas zodra je erin toewijst, en dat gebeurt in week 5 niet. | Besloten in het weekontwerp van week 5, uit te voeren bij de herziening van week 7. |
| PGM1 week 5 | PGM1 week 7 | Week 5 sluit af op één probleem: één vakje van een raster veranderen terwijl de rest blijft staan. Beide afsluitingen verwijzen naar `source/problems/7_extra.md`, de optionele extra-laag. | Voorstel: laat `source/lectures/7a_lists_advanced.ipynb` datzelfde probleem opnemen, zodat ook de student die extra overslaat het vervolg krijgt. |
| PGM2 week 5 | PGM2 week 6 | Het practicum is één project over drie weken: `creatures.py`, beschreven in [practicum-oop.md](practicum-oop.md). Week 5 levert de klassen `Creature` en `Party`; week 6 bouwt er subklassen, `Beast` en een duck-typed `Turret` op. Wie week 5 niet af heeft, begint met de eindstand in `source/practicals/assets/creatures.py`. | Besloten bij de voorbereiding van de poort van #160. Week 5 is uitgevoerd in #160, week 6 in #270 (`practicals/13_creatures.md`). |
| PGM2 week 6 | PGM2 week 7 | Week 7 geeft de klassen uit week 6 operatoren en vervangt de stille terugvalwaarden uit week 5 en 6 door `raise`. Het practicum gooit alleen exceptions en vangt er geen af, terwijl P4 het *afhandelen* van foutcondities vraagt. Week 6 levert (#270): `Beast`, `Dragon`, `Wolf`, `Goblin`, `Healer`, `Turret`, `battle_round` en `battle(side_a, side_b, max_rounds)`; `special_move` op `Creature` valt stil terug op een gewone aanval. Wat afwijkt van de opzet van sessie 3: alle vier de wezens hebben standaardwaarden, dus `Dragon("Ember")` werkt; `__repr__` noemde tot #271 `Creature(...)`, ook bij een subklasse, en `type(self).__name__` was in week 6 vermeden, dus de zin in sessie 3 dat `__repr__` "al sinds Sessie 1" `self.__class__` gebruikt, klopte niet; de limieten van `Turret` zijn attributen van het object, geen klasse-attributen. | Besloten als opzet. De afwijkingen zijn besloten bij de poort van #270 (V8, V9, V10). **Uitgevoerd** in #271 (`practicals/14_creatures.md`): het afvangen staat in de basisopgave (VP1); V10 is herroepen, en `__repr__` gebruikt sinds week 6 `self.__class__.__name__` (VP7). |
| PGM2 week 5 | PGM2 week 6 | `practicals/13_vier_op_rij_speler.md` verwijst op r37 naar het AI-practicum van week 5 en op r338 naar `host_game`, dat alleen daar wordt gebouwd. Sinds #160 wijst r37 naar `Board`, nu de extra-opgave van week 5. | Afgehandeld in #270: week 6 bouwt `host_game(px, po)` in `problems/13_extra.md`, en `13_vier_op_rij_speler` staat sinds #270 in de inhoudsopgave onder PGM2 week 7, met ongewijzigde inhoud (V5). Het bestand zelf, met `play_game` en de controle op `'human'` op r338, staat sinds #271 buiten `source/` (VP11); de inhoud leeft voort in `problems/14_extra.md`. |
| PGM2 week 6 | PGM2 week 7 | De extra-opgave `problems/13_extra.md` legt de spelersinterface vast waarop week 7 voortbouwt: elke speler heeft een attribuut `ox` en een methode `next_move(board)` die een kolom teruggeeft waarin een zet mag; `Board.host_game(px, po)` gebruikt van een speler alleen die twee, zonder typecontrole; `Player.next_move` valt terug op de meest linkse kolom, en `Board` heeft `cols_to_win(ox)`. Een volgende speler, in #271, past in deze structuur als subklasse van `Player`, waarvoor `host_game` niet verandert. Het toernooi vervalt (V3). | Besloten bij de poort van #270 (24 september 2026). **Uitgevoerd** in #271: `MinimaxPlayer` is een subklasse van `Player`, en `host_game` is ongewijzigd. Het toernooi vervalt ook in week 7 (VP2). |
| PGM2 week 2 | PGM2 week 3, 4, 5, 6 en 7 | Week 2 levert comprehensions. Latere weken gebruiken ze zonder ze uit te leggen, alle met één `for` en eventueel een filter: `practicals/10_directory_doorzoeken` en de laatste opdracht van `problems/10_opstap` (week 3, sinds #332), `caesar_op_orde` (tot #332 in week 3, sindsdien in week 4), `practicals/12_creatures.md` r290 en `problems/12_extra.md` r87 (week 5), `problems/13_opstap` (week 6), en `problems/14_opstap`, `problems/14_basis` en `practicals/14_creatures.md` (week 7). | Uitgevoerd in #326; de latere weken zijn daarvoor niet aangepast. |
| PGM2 week 2 | PGM2 week 5 | Week 2 leert `_` voor een ongebruikte lusvariabele, ook in een comprehension. `Board` in `problems/12_extra.md` r87 schrijft `[[" "] * width for row in range(height)]`, met `row` in plaats van `_`. | Besloten door de vakdeskundige op 30 september 2026 (VP7). Uitgevoerd in #327. |
| PGM2 week 3 | PGM2 week 4 | Week 4 rekent op week 3. `lectures/11a_use_it_or_lose_it` opent met de vooruitblik uit `10b`, zet de twee recursieve aanroepen van *use it or lose it* af tegen de ene aanroep per geval van `keepvwl` en `largest`, en legt de takken van `subset` terug naar de frames op de stack. `lectures/11b_functie_als_argument` bouwt `best(L, score)` op `largest` en `best_word`, en de opstap verwijst voor `all_pass` naar `only_digits`. Week 3 levert (#332): `largest(L)`, `keepvwl` en `only_digits` in `lectures/10b_recursief_ontwerpen`, `best_word` in de basis, frames op de stack in `lectures/10a_recursie`, en de termen *basisgeval*, *recursief geval* en *recursieve aanroep*, die week 4 sinds #335 ook gebruikt. | Besloten bij de poort van #332. Week 3 is uitgevoerd in #332. Het termverschil is opgelost in #335: in week 4 staat geen *base case* meer. |
| PGM2 week 3 | PGM2 week 7 | Min-max in `problems/14_extra.md` roept de recursie aan binnen een lus over de kolommen, met één ply minder, en stopt bij ply `0`. Week 3 levert de recursieve aanroep binnen een lus of comprehension over keuzes: `print_files` in `lectures/10a_recursie`, en `count_files`, `total_size`, `unsafe_names` en `depth` in `practicals/10_directory_doorzoeken`, waar een directory zonder subdirectories het basisgeval is zonder `if`. | Uitgevoerd in #332; week 7 is daarvoor niet aangepast. |
| PGM2 week 4 | PGM2 week 7 | Week 4 levert het maximum over de uitkomsten van twee recursieve aanroepen (`max(use_it, lose_it)` in `subset`) en `key=` met `lambda`. Min-max in `problems/14_extra.md` neemt per kolom het maximum of minimum over recursieve uitkomsten, en vergelijkt `ScoredMove`-objecten via `__lt__`, niet via `key=`. | Vastgelegd in #335; week 7 is daarvoor niet aangepast. |
| PGM2 week 6 | PGM2 week 7 | De extra-opgave van week 7 voegt een min-max-speler toe aan de spelers uit week 6, als volgende speler in de spelersinterface van `problems/13_extra.md`. | Besloten door de vakdeskundige op 23 september 2026. **Uitgevoerd** in #271 (`problems/14_extra.md`). |

## Onderhoud

Verandert er iets aan de weekindeling of aan waar een begrip wordt
geïntroduceerd, werk dan dit document bij in dezelfde wijziging. Dit is de bron
waartegen coherentie over weken heen wordt getoetst; loopt hij achter, dan
controleert de toets niets meer.

# Docentenhandleiding PGM1 week 1

Deze week gaat over problemen oplossen, en nog niet over Python. De student leert
wat informatica is, hoe hij een probleem eerst op papier aanpakt, en hoe hij een
plan opschrijft als beslissingsboom of state machine. Daarna programmeert hij
Picobot: een bijziend robotje dat een kamer moet verkennen en dat met een
handjevol regels wordt gestuurd.

Er wordt deze week geen regel Python geschreven. Dat is opzet - zie
`source/course/week_1.md` §`### Waarom Picobot en niet meteen Python?`.

## 1. De week in het kort

| Bijeenkomst | Vorm | Materiaal |
|---|---|---|
| 1 | College | `source/lectures/1a_intro_programmeren.md` |
| 2 | Werkcollege | `source/lectures/1b_picobot.md` |
| 3 | Practicum | `source/practicals/1_picobot.md` |

Daarnaast staan er twee overzichtspagina's die je zelf niet hoeft te behandelen:
`source/course/week_1.md` (`## Introductie en Picobot`) vat de week samen voor de
student, en `source/course/practical_1.md` is de omslagpagina boven het practicum.

### Deze week is bewust flexibel

Week 1 volgt de indeling college - werkcollege - practicum uit
`curriculum/uitgangspunten.md` §`### Drie bijeenkomsten per week` niet strak, en
dat is daar als erkende afwijking vastgelegd.

De reden is aanwijsbaar in het materiaal: de Picobot-opdrachten beginnen in
bijeenkomst 2 als **plan** (`source/lectures/1b_picobot.md`
§`## Opdracht 1: De lege kamer` en §`## Opdracht 2: Het doolhof`) en worden in
bijeenkomst 3 **geprogrammeerd** (`source/practicals/1_picobot.md`, dezelfde twee
titels). Het is één doorlopende opdracht over twee bijeenkomsten. Wat in
bijeenkomst 2 blijft liggen, gaat naar bijeenkomst 3; daar is ruimte voor.

De vakdeskundige voegt daar een tweede grond aan toe: *week 1 is voor studenten
even wennen*. Dat is waargenomen lesgeven en staat verder nergens in de repository
vastgelegd - herkomst: vakdeskundige, bij werkitem #182.

Behandel de tijdsblokken hieronder daarom als richtsnoer en niet als rooster.

### Over de tijden

De blokken van bijeenkomst 1 en 2 komen uit de handleidingen van 2023
(`teacher_guides/1a_problemen_oplossen.docx` en `teacher_guides/1b_picobot.docx`)
en tellen daar op tot **95 minuten** per bijeenkomst, met een ongetimede pauze.
**Hoe lang een bijeenkomst werkelijk duurt staat nergens in de repository**; duurt
die van jou korter of langer, schaal de blokken dan mee. De blokken van
bijeenkomst 3 zijn richttijden zonder bron - daarvoor bestaat geen oude
handleiding.

### Wat je nodig hebt

- **Papier en pen voor iedereen.** Bijeenkomst 1 en 2 zijn volledig unplugged, en
  het tekenen *is* de opdracht.
- **Een browser.** De Picobot-simulator draait op
  [https://www.cs.hmc.edu/picobot/](https://www.cs.hmc.edu/picobot/); er hoeft
  niets geïnstalleerd te worden.
- **Iets om op te tekenen** waar de klas bij kan: een beslissingsboom, een state
  machine en het NEWS-kruisje leg je tekenend uit, niet op een dia.

**Sluit elke bijeenkomst af met de opdracht om Python te installeren.** Dat stond
in beide handleidingen van 2023 aan het eind, met nadruk, en het is nog steeds de
enige manier waarop je week 2 niet met een half uur installatiehulp begint. Verwijs
naar `source/lectures/0b_install_python.md`; deze week is de laatste waarin het nog
zonder kan.

## 2. Bijeenkomst 1 - College: wat is informatica

Materiaal: `source/lectures/1a_intro_programmeren.md`.

### Blokschema bijeenkomst 1

| # | Min | Blok | Waar in `1a_intro_programmeren.md` |
|---|---|---|---|
| 1 | 5 | Kennismaken en lesdoel: problemen oplossen met een strategie | `# Wat is informatica`, `## Hoe kan een probleem worden opgelost?` |
| 2 | 15 | Drie strategieën, met LCS voorgedaan | `## Strategieën`, `### Longest Common Subsequence (LCS)` |
| 3 | 15 | Beslissingsboom, uitgewerkt op het algoritme van Euclides | `## Beslissingsboom` |
| 4 | 10 | State machine, uitgewerkt op de spoken van Pac-Man | `## State Machine` |
| | | **Pauze** | |
| 5 | 5 | De drie p's als werkwijze voor wat nu komt | `## 3 p's` |
| 6 | 20 | Nim en de Nim-variant, in duo's | `## Opdrachten`, `### Opdracht 1: Nim`, `### Opdracht 2: Nim variant` |
| 7 | 10 | Gevonden strategieën bespreken | idem |
| 8 | 10 | Wie liegt er?, zelfstandig | `### Opdracht 3: Wie liegt er?` |
| 9 | 5 | Bespreken, afronden en vooruitblik | `## En nu Picobot` |

Negen blokken, 95 minuten. De bron had er acht.

**Wat er ten opzichte van 2023 is veranderd.** Het blok *Boolean logica* (10 min)
**vervalt**: `and`, `or` en `not` zijn naar week 2 verhuisd en komen deze week
nergens meer voor. Nieuw zijn blok 3 en 4 - beslissingsboom en state machine
stonden in 2023 in het tweede college en zijn naar dit college verplaatst - en de
LCS-uitwerking in blok 2, die er toen niet was. Het blok *De drie p's* stond in
2023 in de introductie vooraf; in het materiaal staat het nu vlak vóór de
opdrachten, en daar hoort het ook: het is een werkwijze voor wat komt, geen theorie
vooraf.

### Hoe je het brengt

**Blok 1.** Begin met de vraag aan de zaal: wat denk je dat informatica is? Je
krijgt "programmeren" en "iets met computers" terug, en dat is precies de
misvatting waar de tekst mee opent. Het lesdoel is één zin waard: problemen
oplossen met een strategie, en de computer pas daarna.

**Blok 2.** De drie strategieën - teken het probleem, maak het kleiner, probeer
alle opties - zijn abstract tot je ze voordoet. Doe LCS voor met `HUMAN` en
`CHIMPANZEE` op het bord, en laat de klas zelf `HMAN` vinden voordat je de
uitlijning laat zien. Dat is strategie 2 in actie: het echte probleem is drie
miljard karakters DNA, en dat wordt hier eerst tot twee woorden gekrompen.

**Blok 3.** Reken Euclides voor 900 en 1140 stap voor stap voor op het bord. De
vier deelstappen staan uitgeschreven in het materiaal; schrijf ze op zoals ze daar
staan, want het is de herbenoeming van *m* en *n* per stap waar het misgaat.

**Blok 4.** Teken de Pac-Man-state-machine terwijl je hem uitlegt: zoeken - jagen -
vluchten. Vraag daarna welke overgang er ontbreekt als je hem zelf zou tekenen; de
plaatjes in het materiaal geven het antwoord weg, dus vraag het vóórdat je de
afbeelding toont.

**Blok 5.** De drie p's zijn geen theorie maar een instructie voor het volgende
halfuur: probeer, plan, programmeer. Zeg er direct bij dat de derde p deze week nog
niet aan bod komt en dat blok 6 tot en met 8 alleen de eerste twee zijn. Dat is
ook het antwoord op de student die vraagt wanneer er nou wordt geprogrammeerd.

**Blok 6.** Laat de studenten in duo's spelen. Doel is een winnende strategie, niet
een gewonnen potje. Zestien lucifers of net zo goed zestien streepjes op papier.

Kent een duo Nim al, vraag dan of ze de oplossing even voor zich houden en laat ze
doorgaan met `### Opdracht 2: Nim variant`. Die variant is aantoonbaar zwaarder -
zie sectie 4 - en houdt de snelle duo's bezig zonder dat je iets hoeft te
verzinnen.

**Blok 7.** Bespreek de gevonden strategieën klassikaal. Is de winnende strategie
níét gevonden, speel dan zelf tegen de klas en gebruik hem. Laat de klas
uitzoeken wat je doet. Dat werkt beter dan hem uitleggen, want de klas ziet je
tegenzet meteen na hun eigen zet.

**Blok 8.** Laat de studenten eerst zelf nadenken en bespreek daarna pas. De vier
puzzels lopen op in moeilijkheid; wie bij **a** blijft steken, hoeft niet aan **d**
te beginnen. Hamer erop dat ze de *redenering* opschrijven en niet alleen het
antwoord - dat staat ook zo in de opdracht, en het is het enige wat je in blok 9
kan bespreken.

**Blok 9.** Sluit af met "wat hebben we geleerd?" en laat de klas het antwoord
geven. Wijs vooruit naar Picobot (`## En nu Picobot`), en zeg dat ze Python moeten
installeren.

### Waar het vastloopt

- **Subsequence tegen substring.** Bij LCS zoekt de halve zaal een *aaneengesloten*
  stuk en komt niet verder dan `M` of `AN`. Het materiaal zegt "*maar niet
  noodzakelijk aaneengesloten*" met nadruk; zeg het er hardop bij, vóórdat ze
  beginnen.
- **Euclides zonder herbenoeming.** Studenten rekenen de eerste rest goed uit en
  gaan dan verder met de oorspronkelijke *m* en *n*. Stap 4 zegt: herhaal met *n*
  en *r*. Schrijf per stap opnieuw op wat *m* en wat *n* nu is.
- **Een staat is geen actie.** Bij de state machine tekent men "ga naar links" als
  staat. Een staat is de *situatie* waarin het programma zich bevindt; de actie
  hoort bij de overgang. Let op: in `source/lectures/1b_picobot.md` §`### De staat`
  staat "bij Picobot lees je elke staat als één gedrag" - dat is een bewuste
  vereenvoudiging voor volgende week en niet een tegenspraak. Benoem het verschil
  als een student erover valt.
- **Nim: het antwoord zonder het waarom.** Duo's vinden "pak aan tot vier" maar
  zien niet dat 16 zelf al een viervoud is en dat daarom júist speler 2 wint. Vraag
  door: wie wint er, en waarom die en niet de ander?
- **Wie liegt er?, puzzel c: de "of".** Pebbles zegt "Ik lieg, **of** Wilma spreekt
  de waarheid". Wie dat leest als "het een of het ander, niet allebei" loopt vast.
  Het is de inclusieve of. Dit is de plek waar het gemis van het geschrapte blok
  Boolean logica merkbaar is: de student heeft `and` en `or` deze week nog niet
  gehad en moet het in het Nederlands redeneren. Doe puzzel **a** klassikaal voor
  langs die lijn - "stel dat Nate de waarheid spreekt, wat volgt daaruit?" - dan
  hebben ze de vorm te pakken.
- **Puzzel d wordt als rekensom gelezen.** Studenten tellen of middelen de elf
  antwoorden. De sleutel is: het aantal mensen dat *k* zegt moet gelijk zijn aan
  *k*. Geef die zin als hint, niet het antwoord.

### Als het niet uitkomt

- **Blok 6 en 7 lopen uit.** Dat mag. Sla `### Opdracht 3: Wie liegt er?` over en
  geef hem mee als huiswerk; hij heeft geen vervolg in bijeenkomst 2 en kost je dus
  niets. Bespreek hem aan het begin van bijeenkomst 2 in vijf minuten.
- **Je houdt tijd over.** Laat duo's die klaar zijn `### Opdracht 2: Nim variant`
  bewijzen voor een opstelling die ze nog niet gespeeld hebben - dat is de eis in
  de opdracht zelf en is zwaarder dan het lijkt.
- **Niemand vindt de Nim-strategie.** Speel zelf tegen de klas (blok 7). Werkt ook
  dat niet, geef dan de winsituatie weg - vier lucifers over, speler 1 aan zet -
  en laat ze van daaruit terugredeneren.

## 3. Bijeenkomst 2 - Werkcollege: Picobot plannen

Materiaal: `source/lectures/1b_picobot.md`. Dit is de laatste bijeenkomst op
papier; geprogrammeerd wordt er in bijeenkomst 3.

### Blokschema bijeenkomst 2

| # | Min | Blok | Waar in `1b_picobot.md` |
|---|---|---|---|
| 1 | 5 | Lesdoel en de robotstofzuiger | `# Picobot` |
| 2 | 10 | Naar de hoek: welke instructies werken? In duo's | `## Naar de hoek` |
| 3 | 5 | Bespreken, en het plan als beslissingsboom | `### Oplossing` |
| 4 | 20 | De taal van Picobot: NEWS, staat, regels, wildcards | `## Picotaal`, `### De staat`, `### De regels`, `### Wildcards` |
| 5 | 10 | Hetzelfde plan, nu in picotaal | `## De hoek in` |
| | | **Pauze** | |
| 6 | 10 | De lege kamer verkennen: plan maken, in duo's | `## Opdracht 1: De lege kamer` |
| 7 | 10 | Het doolhof verkennen: plan maken, in duo's | `## Opdracht 2: Het doolhof` |
| 8 | 10 | Complexiteit, en de right hand rule voorgedaan | `## Complexiteit`, `### De right hand rule`, `### Drie situaties, drie regels` |
| 9 | 10 | De simulator: een pad voorspellen en narekenen | `## Opdracht 3: Picobot` |
| 10 | 5 | Afronden | - |

Tien blokken, 95 minuten. De bron had er negen.

**Wat er ten opzichte van 2023 is veranderd.** Het blok *Introductie -
beslissingsboom, state machine* (10 min) **vervalt hier**: het is naar bijeenkomst
1 verhuisd, blok 3 en 4 daar. De opdrachtnummers uit de oude handleiding kloppen
geen van drieën meer; zie sectie 5.

### Hoe je het brengt

**Blok 1.** De robotstofzuiger doet het werk: vrijwel blind, alleen een bumper, en
tóch komt hij overal. Dat is de hele opgave van deze week in één beeld.

**Blok 2.** Stel de vraag uit het materiaal - welke set instructies brengt Picobot
naar de linkerbovenhoek? - en laat duo's erover nadenken. Vijf regels op papier is
genoeg; het gaat om de vorm "rij tot je niet meer kan, draai, rij tot je niet meer
kan".

**Blok 3.** Bespreek de gevonden instructies en teken de bijbehorende
beslissingsboom. Dit is de terugkoppeling naar bijeenkomst 1: dezelfde vorm,
nieuw probleem.

**Blok 4.** Dit is het zwaarste blok van de week en het enige waar echt nieuwe
notatie in zit. Neem de twintig minuten. Volgorde: eerst NEWS en het `xxxx`-patroon
met het plaatje van de zestien omgevingen, dan de staat als getal, dan de
regelvorm, dan pas de sterretjes. Schrijf één regel volledig uit op het bord en
lees hem hardop als een zin: *als mijn staat 0 is en de omgeving `Nxxx`, zet dan
een stap naar het zuiden en blijf in staat 0.*

**Blok 5.** Neem het plan uit blok 2 en 3 en vertaal het regel voor regel. De drie
stappen staan uitgeschreven in het materiaal en eindigen in een volledig programma
van drie regels. Laat zien dat de twee regels van staat 0 samen alle zestien
omgevingen dekken zonder overlap - daar zit de sprong.

**Blok 6 en 7.** Duo's, papier, geen simulator. Laat ze kiezen: de lege kamer of
het doolhof. Wie de kamer af heeft gaat naar het doolhof; wie het doolhof
aandurft heeft de kamer meestal onderweg opgelost. Bespreek beide plannen
klassikaal.

**Blok 8.** Doe pas hierna de right hand rule voor - het materiaal zegt zelf dat
dit minder leerzaam is als de student het leest vóór hij zelf heeft geprobeerd.
Werk de drie situaties voor staat `0` uit zoals ze in het materiaal staan en laat
de andere drie richtingen open; dat is het huiswerk van bijeenkomst 3. Noem de
regelbudgetten: zes regels voor de lege kamer, acht voor het doolhof.

**Blok 9.** Open de simulator klassikaal, laat de voorbeeldcode staan en laat de
klas het pad **eerst tekenen**, dan pas op Go klikken. De waarde zit in het
verschil tussen voorspelling en werkelijkheid.

**Blok 10.** "Wat hebben we geleerd?", en nogmaals: installeer Python.

### Waar het vastloopt

- **`x` betekent leeg, niet "maakt niet uit".** Dit is de fout die het vaakst
  gemaakt wordt. `x` zegt: hier is géén muur. Wie "maakt niet uit" bedoelt, moet
  `*` schrijven. Zet beide op het bord naast elkaar.
- **Regels zijn geen programmaverloop.** Studenten lezen de regels als stappen die
  na elkaar worden uitgevoerd. Picobot zoekt na elke stap opnieuw de regel die bij
  zijn staat en omgeving past; volgorde in het bestand doet niets.
- **`Repeat Rule!`** De simulator weigert het hele programma als twee regels
  dezelfde combinatie van staat en omgeving dekken. Dat gebeurt bijna altijd door
  sterretjes die overlappen, niet door twee identieke regels. Laat ze de zestien
  omgevingen aflopen als het gebeurt.
- **De vier windrichtingen zijn Engels.** NEWS, niet NOWZ. Het materiaal waarschuwt
  ervoor; iemand typt toch `NxOx`.
- **De staat is één getal en niets meer.** Studenten willen erin bijhouden waar
  Picobot is geweest. Dat kan niet: staat en omgeving zijn alles wat Picobot van de
  wereld weet.

### Als het niet uitkomt

- **Blok 4 loopt uit.** Dat is het blok dat je níét moet inkorten. Schuif in plaats
  daarvan blok 8 door naar het begin van bijeenkomst 3; de right hand rule is daar
  net zo bruikbaar, en het practicum begint toch met dezelfde twee opdrachten.
- **Je houdt tijd over.** Laat duo's alvast beginnen aan
  `source/practicals/1_picobot.md` §`## Opdracht 1: De lege kamer` in de simulator.
  Dat is geen vooruitlopen maar precies de bedoeling: bijeenkomst 2 en 3 lopen in
  elkaar over.
- **Een duo komt er bij blok 6 en 7 niet uit.** Verwijs naar
  §`## Complexiteit`, waar de strategie is voorgedaan. Het practicum verwijst er
  zelf ook naar.

## 4. Bijeenkomst 3 - Practicum: Picobot programmeren

Materiaal: `source/practicals/1_picobot.md`. Hier wordt de derde p gezet:
programmeren.

### Blokschema bijeenkomst 3

Deze bijeenkomst heeft **geen handleiding uit 2023**. De tijden hieronder zijn
richttijden, geschat op de omvang van de opdrachten, en geen overgeleverde
lesindeling.

| # | Min | Blok | Waar in `1_picobot.md` |
|---|---|---|---|
| 1 | 10 | De simulator laten zien: invoeren, Enter rules, Go, het grijze spoor | `# Picobot programmeren`, `## Kennismaken`, `## De regelvorm` |
| 2 | 25 | Opdracht 1: de lege kamer, streefdoel zes regels | `## Opdracht 1: De lege kamer` |
| 3 | 30 | Opdracht 2: het doolhof, streefdoel acht regels | `## Opdracht 2: Het doolhof` |
| | | **Pauze** | |
| 4 | 15 | Opdracht 3: de ruit - verdieping | `## Opdracht 3: De ruit` |
| 5 | 10 | Opdracht 4: de grot - verdieping | `## Opdracht 4: De grot` |
| 6 | 5 | Afronden | - |

Zes blokken, 95 minuten als richttijd.

### Hoe je het brengt

**Blok 1.** Doe de simulator één keer klassikaal voor: regels in het vak rechts,
"Enter rules for Picobot", dan Go. Wijs de foutmelding met het regelnummer aan die
verschijnt als er iets niet klopt - die zien ze vandaag nog vaak. Wijs ook op de
waarschuwing in het materiaal: **sluit je het venster, dan zijn alle regels weg.**
Laat ze meteen een tekstbestand openen om in te plakken. Dat is de goedkoopste
minuut van de week.

Het succescriterium is visueel en hoef je niet zelf na te kijken: kleurt de hele
ruimte grijs en stopt Picobot vanzelf, dan is het gelukt. Blijft er wit staan, dan
niet.

**Blok 2 en 3.** Dit is zelfstandig werk onder begeleiding. Loop rond. De plannen
van bijeenkomst 2 liggen er al; wie er geen heeft, maakt er eerst een - laat
niemand meteen regels typen, dat is de fout die de hele week probeert te
voorkomen.

Het regelbudget - zes en acht - is een streven en geen eis; het materiaal zegt dat
er zelf bij. Gebruik het als uitdaging voor wie snel klaar is, niet als norm.

**Blok 4 en 5.** De ruit en de grot zijn expliciet verdieping: er hoort geen plan
uit het college bij en er is geen regelbudget. De student zet stap 1, 2 en 3 hier
helemaal zelf. Niet iedereen komt hieraan toe, en dat is de bedoeling.

**Blok 6.** Laat een paar oplossingen zien op het scherm en vraag naar het aantal
regels. Sluit af met Python installeren - dit is de laatste keer dat het nog geen
probleem is.

### Waar het vastloopt

- **Eén startpositie is geen oplossing.** Picobot kiest zelf waar hij begint. Een
  regelverzameling die het vanuit het midden doet, faalt vanuit de hoek. Het
  criterium in het materiaal is niet voor niets: drie verschillende startposities,
  via Reset.
- **De klaar-vraag.** "Ben ik klaar?" beantwoord je niet zelf: kleurt alles grijs
  en stopt hij vanzelf? Dan ja.
- **Regels kwijt.** Zie hierboven. Het gebeurt.
- **Vastlopen op het doolhof zonder plan.** Verwijs naar
  `source/lectures/1b_picobot.md` §`## Complexiteit`: daar staan de drie regels voor
  één richting voorgedaan, en de andere drie richtingen mag de student zelf
  afmaken. Dat is de bedoelde route en geen weggeefactie.

### Als het niet uitkomt

- **De helft komt niet door opdracht 2.** Prima. Opdracht 3 en 4 zijn verdieping;
  ze horen niet af te zijn. Wat wel af moet is opdracht 1.
- **Iemand is na twintig minuten met alles klaar.** Laat hem het regelaantal
  omlaag brengen naar zes en acht, en daarna de ruit en de grot doen.

## 5. Wat je verder moet weten

### Eigenaardigheden in het materiaal

- **De kop `Opdracht 1: De lege kamer` bestaat twee keer**, met bijna dezelfde
  tekst: in `source/lectures/1b_picobot.md` (daar maak je het *plan*, stap 1 en 2)
  en in `source/practicals/1_picobot.md` (daar *programmeer* je het, stap 3).
  Hetzelfde geldt voor `Opdracht 2: Het doolhof`. Noem in de klas altijd het
  bestand erbij, anders wijst een verwijzing naar twee plekken.
- **`source/course/practical_1.md` heeft als titel `# Werkcollege`**, maar draagt
  het practicum van bijeenkomst 3. Dat is een restant; de begrippenlijst legt
  `practicals/` bij het practicum.
- **De opdrachtnummers uit de handleiding van 2023 kloppen niet meer.** In het
  tweede college heette "naar de hoek" toen Opdracht 1 en is nu de voorgedane
  §`## Naar de hoek`; de lege kamer heette Opdracht 2 en is nu Opdracht 1; het
  doolhof heette "Opdracht 2+" en is nu Opdracht 2. Lees een oude verwijzing dus
  nooit letterlijk.
- **Booleaanse logica komt deze week niet meer voor.** In 2023 stond er een blok
  `and`, `or`, `not` vlak vóór de leugenaarspuzzels. Dat is naar week 2 verhuisd
  (`source/lectures/2a_var_con.ipynb`). De puzzels bleven staan; de student
  redeneert ze deze week in gewoon Nederlands. Zie de valkuil bij puzzel c.
- **`### Opdracht 2: Nim variant` is nieuw en heeft nergens een uitwerking.** Het
  korte antwoord hieronder is voor deze handleiding nagerekend.

### Korte antwoorden bij de collegeopdrachten

Voor week 1 bestaat geen `solutions/`. Deze antwoorden zijn er voor jou, niet voor
uitdelen; de redenering is bij elke opdracht de opbrengst, niet de uitkomst.

| Opdracht | Bestand | Antwoord |
|---|---|---|
| `### Opdracht 1: Nim` | `source/lectures/1a_intro_programmeren.md` | Laat na jouw zet altijd een viervoud liggen - pakt de ander er *k*, pak jij er 4−*k*; 16 is al een viervoud, dus **speler 2** wint. |
| `### Opdracht 2: Nim variant` | `source/lectures/1a_intro_programmeren.md` | Neem per groep de rest bij deling door 4 en tel die drie resten in binair zonder overdracht bij elkaar op: komt er nul uit, dan verliest wie aan zet is - dus bij (1,2,3) laat je de ander beginnen en bij (3,4,5) begin je zelf. |
| `### Opdracht 3: Wie liegt er?` | `source/lectures/1a_intro_programmeren.md` | **a** Nate en Jeff liegen allebei; **b** Suzy en Spike liegen allebei; **c** Fred, Pebbles en Wilma spreken alle drie de waarheid; **d** ja: drie ridders, want alleen bij 3 is het aantal mensen dat "3" zegt gelijk aan 3. |
| `## Opdracht 1: De lege kamer` | `source/lectures/1b_picobot.md` | Een beslissingsboom die de kamer rij voor rij afgaat; de regels erbij horen bij het practicum, en zes is er het streefaantal. |
| `## Opdracht 2: Het doolhof` | `source/lectures/1b_picobot.md` | Volg de wand consequent aan één kant - de strategie staat voorgedaan in §`## Complexiteit`, met de drie regels voor staat `0`. |
| `## Opdracht 3: Picobot` | `source/lectures/1b_picobot.md` | Geen vast antwoord: de opbrengst is het verschil tussen het getekende pad en wat de simulator doet. |

**Twee kanttekeningen bij puzzel d.** Studenten die alleen het aantal "3"-antwoorden
tellen hebben nog niets bewezen; de sluitende redenering is dat 2, 4, 5 en 7 elk
afvallen omdat het aantal mensen dat dat getal noemt er niet gelijk aan is. En
formeel is *nul* ridders ook consistent met deze elf antwoorden - niemand zei "0",
dus elf liegende schurken spreken zichzelf niet tegen. De puzzel bedoelt 3; komt
een student met nul, dan heeft hij beter gelezen dan de puzzel en verdient hij het
compliment.

### Wat er uit de handleiding van 2023 niet is overgenomen

Het spel **SoS** (het alternatief naast Nim) is vervallen: de opgave bestaat
nergens meer in het materiaal en de oude handleiding gaf er alleen een YouTube-link
bij. Het blok **booleaanse logica** is vervallen omdat de stof naar week 2 is
verhuisd. De twee uitgewerkte **leugenaarspuzzels** (Alice/Bob/Chris, en de variant
met Dave) zijn niet overgenomen omdat ze op geen van de vier huidige puzzels slaan.
De twee **Picobot-diagrammen** (de zigzagroute en de right hand rule) zijn niet
overgenomen: het waren losse Word-tekenobjecten waarvan niet af te leiden is welke
pijl welke twee vakken verbindt.

De volledige verantwoording per aanwijzing staat in werkitem #182.

### Wat er nog loopt

- De vier `.docx` in `teacher_guides/` voor week 1 en 2 staan er nog. Ze worden
  verwijderd zodra ook de handleiding van week 2 er is; tot die tijd zijn ze de
  bron en niet de handleiding.
- Een handleiding voor **week 2** bestaat nog niet.
- Deze handleiding beschrijft het materiaal zoals het op 5 september 2026 in de
  repository staat.

# Metingen

Wat een ronde kost, per rol. De getallen komen uit de tokentelling die de
orkestrator per subagent terugkrijgt; ze omvatten de rol zelf, niet het
orkestreren eromheen.

Noteer ze zodra een rol klaar is. Ze bestaan verder alleen in de sessiecontext.

## Werkitem #103 — PGM1 week 5 herzien

Volledige lus, omvang L. Eerste werkitem dat de lus in zijn geheel doorliep.

| Rol | Ronde | Tokens | Duur | Uitkomst |
|---|---|---|---|---|
| triage | | 12.611 | 22 s | VOLLEDIG, L |
| verkenner | 1 | — | — | afgebroken op een uitgavenlimiet, niets bewaard |
| verkenner | 2 | 157.971 | 16 min | C1b |
| curriculumontwerper | 1 | 83.880 | 9 min | C2 |
| verhelderaar | 1 | 80.285 | 6 min | FAAL |
| curriculumontwerper | 2 | 115.337 | 11 min | C2 |
| verhelderaar | 2 | 68.881 | 5 min | FAAL |
| curriculumontwerper | 3 | 89.500 | 12 min | C2 |
| verhelderaar | 3 | 79.871 | 5 min | FAAL |
| curriculumontwerper | 4 | 106.335 | 12 min | C2 (reparatie) |
| verhelderaar | 4 | 95.173 | 7 min | AKKOORD |
| *vakdeskundige* | | *mens* | | C4 AKKOORD |
| auteur | 1 | — | — | afgebroken op een uitgavenlimiet, lege branch |
| auteur | 2 | 342.577 | 41 min | C5, PR #105 |
| beoordelaars | | *overgeslagen* | | op verzoek van de vakdeskundige |

**Totaal: ongeveer 1.13 miljoen tokens** voor één week.

Waarvan **718k in ontwerpen en verhelderen samen** — meer dan de auteur — en dat
kwam door vier ronden, niet door omvang. Zie bevinding 1.

## Leesronde — PGM1 week 1 en 2

Twee beoordelaars op bestaand materiaal, zonder C5 en zonder ontwerp.

| Rol | Tokens | Duur | Uitkomst |
|---|---|---|---|
| beoordelaar-redacteur | 133.414 | 11 min | BLOKKEER, 3 blokkerend |
| beoordelaar-eerstejaars | 114.210 | 12 min | BLOKKEER, 9 blokkerend |

**Totaal 248k**, en het leverde twee werkitems op vol aantoonbare defecten (#106,
#107). Ter vergelijking: 1.13M voor één week door de volle lus. Zie bevinding 3.

## Leesronde — PGM1 week 4

Twee beoordelaars op bestaand materiaal, zonder C5 en zonder ontwerp. Dezelfde
opzet als bij week 1 en 2, met twee dingen erbij: de leesronde staat nu als modus
in het C6-contract, en de eerstejaars kreeg een lijst mee van wat hij op dit punt
kent en niet kent.

| Rol | Tokens | Duur | Uitkomst |
|---|---|---|---|
| beoordelaar-redacteur | 126.153 | 11 min | BLOKKEER, 5 blokkerend |
| beoordelaar-eerstejaars | 68.747 | 6 min | BLOKKEER, 6 blokkerend |

**Totaal 195k**, tegen 248k voor week 1 en 2. De eerstejaars werd 40% goedkoper,
en de aannemelijkste verklaring is de kennislijst: hij hoefde niet meer zelf af te
leiden wat een student in week 4 heeft gehad. Dat is één waarneming en geen
gemeten oorzaak.

De twee rollen zagen elkaars oordeel niet en kwamen onafhankelijk op dezelfde vijf
blokkerende punten uit: `while` als "oneindige herhaling", de midterm zonder
sleutel, `unique` die nooit is geïntroduceerd, `while_pi` die de opgave niet
oplost, en `print(lijst)` waar `lst` staat. De redacteur vond opgave 18 er
bovenop, de eerstejaars niet. Het leverde werkitem #146 op.

Twaalf bevindingen zijn nagerekend door de code te draaien, de hook te draaien of
het patroon te ijken. Negen hielden stand, **drie zijn weerlegd**: de bewering dat
een pre-commit hook zou breken (bevinding 12), en twee midtermvragen die beide
rollen voor kapot aanzagen terwijl ze met opzet fout aflopen (bevinding 7, tweede
voorval).

Die verhouding is zelf het resultaat. Een leesronde van 195k leverde negen
aantoonbare defecten en drie beweringen die het niet haalden - en de drie waren
alleen te scheiden van de negen door ze na te rekenen, niet door ze te lezen.

## Werkitem #146 — PGM1 week 4, onderdeel 1 tot en met 3

De eerste keer dat een week de volle lus doorliep **na** een leesronde. Omvang **L**
(de triage overrulede de M van de indiener).

| Rol | Tokens | Duur | Uitkomst |
|---|---|---|---|
| triage | 29.310 | 101 s | LUS, omvang L, tien rollen |
| verkenner | 200.139 | 26 min | C1b, negen bestanden doorgemeten |
| curriculumontwerper | 117.693 | 10 min | C2, negen onderdelen, tien criteria |
| verhelderaar | 130.762 | 11 min | **AKKOORD**, 13 verbeterpunten, 0 blokkerend |
| auteur | 195.211 | 24 min | C5, onderdeel 1-3, hooks en build groen |
| beoordelaar-eerstejaars | 116.595 | 10 min | **BLOKKEER**, 2 blokkerend |
| beoordelaar-redacteur | 123.215 | 10 min | AKKOORD MET PUNTJES |
| beoordelaar-onderwijskundige | 106.369 | 9 min | AKKOORD MET PUNTJES |
| beoordelaar-pragmaticus | 106.740 | 8 min | AKKOORD MET PUNTJES |

**1.126.034 tokens voor drie van de negen onderdelen.** Met de leesronde erbij
(194.900) staat week 4 op **1.32M** en is hij niet af. Week 5 kostte 1.13M voor de
volle lus in één keer.

Dat is de meting die de aanname onder bevinding 3 begrenst. Een leesronde is
goedkoper dán ontwerpen, maar hij **vervangt de lus niet** - hij gaat eraan
vooraf. De winst zit niet in minder tokens maar in een werkitem vol aantoonbare
defecten in plaats van vermoedens, en in een ontwerp dat de verhelderaar in één
ronde haalde. Dat laatste is nieuw: bij #103 kostte het drie ontwerprondes.

### Vier beoordelaars, één die het zag

De vier parallelle beoordelaars kostten samen **453.919 tokens**. Er was precies
één blokkerend defect in de oplevering: `4a_lussen` cel 60 definieerde `while`
omgekeerd - *"jij zorgt dat die ooit waar wordt"*, terwijl een `while`-conditie
juist onwaar moet worden.

**Alleen de eerstejaars zag het.** De onderwijskundige en de pragmaticus hebben
diezelfde zin gelezen en hem in hun AC1-oordeel goedkeurend geciteerd; de
redacteur ging er zonder opmerking langs. Drie rollen kenden de constructie te
goed om de tekst te kunnen lezen zoals hij er staat.

Dat is één waarneming en geen wet, maar hij pleit tegen het snoeien in het aantal
beoordelaars als er op kosten moet worden bespaard: de goedkoopste van de vier
(106k) was niet degene die het vond, en de duurste evenmin.

### Wat het vastgelegde besluit deed

**Geen van de vier meldde opdracht 14, 18 of 20 als defect.** In de drie
beoordelingen daarvóór gebeurde dat elke keer wél, met een kloppende meting en een
verkeerde conclusie (bevinding 7). Het verschil is dat het besluit tussendoor van
gevallen naar soort is herschreven, met "blijf hiervan af, meld het niet opnieuw"
erbij, en dat het in de opdracht van elke rol zat.

Dat is de eerste keer in dit onderzoek dat een tegenmaatregel meetbaar heeft
gewerkt. Zie bevinding 7 en 13.

### De meetregel van AC1 struikelde drie keer

Criterium 1 vroeg dat `while` nergens meer "oneindige herhaling" heet. De meetregel
erbij ging drie keer mis, en telkens anders:

1. De oorspronkelijke regel (`grep -rn "oneindige herhaling"`) dekte maar één van
   de twee plekken die het criterium zélf noemt. Gevonden door de triage.
2. Het ontwerp zei "elf treffers elders"; het zijn er vijftien. Gevonden door de
   verhelderaar.
3. Na oplevering is het criterium naar de letter gehaald - nul treffers op
   `oneindig` in week 4 - terwijl `# watch out for infinite loops!` één regel
   verderop blijft staan. Het patroon zocht op het Nederlandse woord en kon dat per
   constructie niet zien. Gevonden door de redacteur.

Alle drie zijn ze gevonden, en dat is het punt: het criterium is drie rollen lang
gecontroleerd door rollen die er niet aan hadden meegeschreven.

## Werkitem #107 — week 1 en 2, afgewezen bij de triage

| Rol | Tokens | Duur | Uitkomst |
|---|---|---|---|
| triage | 45.336 | 163 s | **AFWIJZEN**, omvang XL, splitsingsadvies langs drie naden |

Week 1 en week 2 delen geen enkel bestand in `_toc.yml`, en de criteria vielen
langs diezelfde naad uiteen. Voor **45k** is vastgesteld dat dit werk in drie
stukken uiteenvalt, waar het als één XL-werkitem ruim een miljoen zou hebben
gekost. Dat is de tweede keer dat triage het duurste besluit voor de laagste prijs
neemt; zie bevinding 6.

Eén kanttekening die de orkestrator ving: C1 beriep zich op de regel
*"een vak herindelen → AFWIJZEN"* uit de proportionaliteitstabel, en twee weken
herzien is dat niet. De conclusie stond wel, maar op de regel erboven.

## Werkitem #167 — vier besluiten, en de eerste keer dat stap 5b draaide

| Rol | Tokens | Duur | Uitkomst |
|---|---|---|---|
| beoordelaar-redacteur (stap 5b) | 62.499 | 7 min | **BLOKKEER**, 4 moet-punten |

Stap 5b bestaat sinds bevinding 14: niets toetste wat de orkestrator naar
`curriculum/` en `conventies/` schrijft. **Bij de eerste run verdiende hij zichzelf
terug.** Twee van de vier moet-punten waren feitelijke fouten van de orkestrator:

- "PGM2 week 9, 10 en 11" bestaat niet — `problems/9_*`, `10_*` en `11_*` zijn PGM2
  week 2, 3 en 4. Dat stond in het uitvoerbare deel van een besluit; wie het had
  nageleefd, had naar niets gezocht.
- Een nieuw besluit sprak een staand besluit tegen: *Leesvragen mogen fout aflopen*
  opende met "niet om code schrijven", terwijl het nieuwe besluit juist zegt dat er
  wél geschreven moet worden. Twee plekken in hetzelfde document, honderd regels uit
  elkaar.

## Werkitem #168 — PGM1 week 1, drie ontwerprondes

| Rol | Ronde | Tokens | Duur | Uitkomst |
|---|---|---|---|---|
| triage | | 53.589 | 4 min | LUS, omvang L (overrulet M) |
| verkenner | | 146.300 | 16 min | C1b |
| curriculumontwerper | 1 | 67.664 | 6 min | C2 |
| verhelderaar | 1 | 89.902 | 9 min | **FAAL**, 2 blokkerend |
| curriculumontwerper | 2 (herontwerp) | 86.133 | 10 min | C2 |
| verhelderaar | 2 | 90.188 | 10 min | **FAAL**, 3 blokkerend |
| curriculumontwerper | 3 (reparatie) | 72.242 | 8 min | C2 |
| verhelderaar | 3 | 77.193 | 7 min | **AKKOORD**, 9 verbeterpunten |

**683.211 tokens tot aan de poort**, voor een week van vijf markdownbestanden en
3.872 woorden. De auteur en de beoordelaars waren toen nog niet gedraaid.

### Een herontwerp is niet duurder dan een reparatie

Dit weerlegt een aanname die de orkestrator hardop maakte. `/orc` onderscheidt de
eerste `FAAL` (herontwerp, ontwerper krijgt het afgekeurde C2 niet) van de tweede
(reparatie, hij krijgt het wel), en de gedachte daarachter is dat reparatie
goedkoper is. Gemeten:

| Ronde | Wat | Tokens |
|---|---|---|
| 1 | eerste ontwerp | 67.664 |
| 2 | **herontwerp**, zonder het afgekeurde C2 | 86.133 |
| 3 | **reparatie**, mét het afgekeurde C2 | 72.242 |

Het verschil is 14k op 86k, ongeveer een zesde. De orkestrator schatte de
reparatie vooraf op 30 tot 40k en zat er ruim naast. De verklaring is dat een
reparatieronde het volledige document opnieuw oplevert; alleen het *denkwerk* is
smaller, en dat is niet waar de tokens zitten.

Wat wél verschilde is de **opbrengst**: het herontwerp loste de twee blokkades op
en introduceerde drie nieuwe, de reparatie loste er drie op en introduceerde er
geen.

### De oplevering en de beoordeling

| Rol | Tokens | Duur | Uitkomst |
|---|---|---|---|
| auteur | onbekend | 21 min | C5; **afgebroken op een verbindingsfout** ná het openen van de PR |
| beoordelaar-eerstejaars | 116.713 | 9 min | **BLOKKEER**, 1 blokkerend |
| beoordelaar-onderwijskundige | 96.273 | 8 min | AKKOORD MET PUNTJES |
| beoordelaar-redacteur | 82.563 | 8 min | AKKOORD MET PUNTJES |
| beoordelaar-pragmaticus | 78.855 | 6 min | AKKOORD MET PUNTJES |

**De tokentelling van de auteur is verloren.** Hij viel om op een verbindingsfout
nadat hij had gecommit en de pull request had geopend, dus het werk is compleet en
alleen zijn eindverslag ging weg. Dat is het verschil tussen verlies en vertraging,
en hier is het verlies beperkt tot een getal.

### Vier beoordelaars, en opnieuw één die het zag

**Alleen de eerstejaars vond het blokkerende defect**, net als bij week 4. Het is
er één en het is klein: `1b` r61 zegt *"Hieronder is staat `0` rij naar het
noorden"*, terwijl de tabel er direct onder staat 0 een stap naar het **zuiden**
laat zetten (`Nxxx -> S`). De zin die er wél mee klopt staat 65 regels verder.

Dat is de enige plek waar het lastigste begrip van de week wordt uitgelegd - het
ontwerp bracht alle uitleg daarheen - en het is precies de route waar het practicum
de student naartoe stuurt. De andere drie beoordelaars lazen dezelfde regels en
zagen het niet.

Tweede waarneming op rij dat de rol die de constructie *niet* kent, ziet wat de
rollen die haar kennen overlezen. Zie ook de meting bij #146.

### De overdracht ging opnieuw stuk, en de rol ving het

De orkestrator gaf de kern van C5 door door hem met de hand in vier prompts over te
typen, en knipte daarbij het verplichte veld *Wat dit raakt buiten deze week* eraf.
De eerstejaars **stopte daarop en gaf geen oordeel**, zoals zijn contract
voorschrijft, en onderbouwde waarom het geen formaliteit was: hij had tijdens het
lezen gezien dat twee van de zes gewijzigde bestanden geen week 1-materiaal zijn en
dat `projects/picobot.md` nog *toestand* schrijft. Hij kon niet aannemen dat het
veld leeg was.

Het veld dekte dat precies. Het gat zat in de overdracht, niet in de oplevering.

Na aanlevering van het ontbrekende veld maakte hij zijn C6 af **zonder opnieuw te
lezen**, in dezelfde draad. Hij merkte daarbij zelf op dat dit de tweede keer is dat
een stopvoorwaarde afgaat op een onvolledig doorgegeven kern, en dat de goedkoopste
ingreep niet een uitzondering in het contract is maar het **letterlijk doorgeven**
van de kern in plaats van hem over te typen. Zie bevinding 15.

### Drie verhelderaarrondes, drie keer raak

Geen van de drie oordelen was ruis. Ronde 1 ving dat het ontwerp niet zei hoeveel
van een oplossing het college mocht weggeven, terwijl het uit CS5 een sectie wilde
terughalen die drie van de acht regels van de zwaarste opdracht bevat. Ronde 2 ving
dat drie acceptatiecriteria aan geen enkel onderdeel hingen, en dat de
woordbudgetten van één criterium niet konden optellen — 3.956 tegen een plafond van
3.872 — terwijl de grond eronder onwaar was ("1.700 blijft onder 1.543"). Ronde 3
gaf `AKKOORD` en ving daarbij nog dat een ijkgetal dat de orkestrator zelf had
doorgegeven, 68, in werkelijkheid het practicum (29) plus een bestand was dat
uitdrukkelijk buiten de opdracht viel (39).

Die laatste rol deed daarbij iets wat het noteren waard is: hij meldde dat zijn
**eigen** eerste patroon nul gaf en stukgelopen bleek. Dat is de huisregel uit
`CLAUDE.md`, door een rol op zichzelf toegepast en uit zichzelf gerapporteerd.

## Werkitem #115 — de uitwerkingen

| Rol | Tokens | Duur | Uitkomst |
|---|---|---|---|
| triage | 19.671 | 84 s | AFWIJZEN, XL, met een splitsingsadvies |

Triage is de goedkoopste rol in de lus en neemt het besluit dat alle andere kosten
bepaalt. Zie bevinding 6.

## Veegronde — de hele cursus

| Rol | Tokens | Duur | Uitkomst |
|---|---|---|---|
| eindredacteur | 174.232 | 27 min | 8 zware, 8 middelzware, 8 lichte bevindingen (#124) |

Eerste keer dat deze rol draaide. Hij vond drie dingen die vanuit geen enkele week
zichtbaar waren, en één bevinding die onjuist bleek omdat hij kennis miste die
alleen de vakdeskundige had. Zie bevinding 5 en 7.

## Wat de sessie in totaal kostte

Ongeveer **1,67 miljoen tokens aan subagents** over twee dagen, plus de
orkestratie. Verdeeld over de rollen:

| Rol | Aandeel |
|---|---|
| auteur | 343k (21%) |
| ontwerper, alle ronden | 395k (24%) |
| verhelderaar, alle ronden | 324k (19%) |
| verkenner | 158k (9%) |
| eindredacteur | 174k (10%) |
| beoordelaars | 248k (15%) |
| triage, twee keer | 32k (2%) |

## Werkitem #134 — PGM2 week 1, van list comprehension naar datastructuren

Volledige lus, omvang L. Vier ontwerprondes (één FAAL, één HERZIEN bij de poort,
één tweede FAAL), twee volledige beoordelingsrondes met alle vier de
beoordelaars.

| Rol | Ronde | Tokens | Duur | Uitkomst |
|---|---|---|---|---|
| triage | | 42.380 | 2 min | LUS, L |
| verkenner | | 141.279 | 9 min | C1b |
| curriculumontwerper | 1 | 102.628 | 10 min | C2 |
| verhelderaar | 1 | 119.541 | 6 min | FAAL |
| curriculumontwerper | 2 (herontwerp) | 186.913 | 11 min | C2 |
| verhelderaar | 2 | 129.875 | 7 min | AKKOORD |
| *vakdeskundige* | | *mens* | | C4 HERZIEN |
| curriculumontwerper | 3 (reparatie na HERZIEN) | 91.632 | 8 min | C2 |
| verhelderaar | 3 | 98.315 | 9 min | FAAL |
| curriculumontwerper | 4 (reparatie, tweede FAAL) | 22.648 | 2 min | C2 |
| verhelderaar | 4 | 36.836 | 2 min | AKKOORD |
| *vakdeskundige* | | *mens* | | C4 AKKOORD |
| auteur | 1 | 293.772 | 21 min | C5, PR #148 |
| beoordelaar-onderwijskundige | 1 | 152.154 | 10 min | BLOKKEER |
| beoordelaar-pragmaticus | 1 | 131.372 | 10 min | BLOKKEER |
| beoordelaar-redacteur | 1 | 146.273 | 10 min | BLOKKEER |
| beoordelaar-eerstejaars | 1 | 151.270 | 11 min | BLOKKEER |
| hoofdredacteur | 1 | 33.793 | 4 min | C7 BLOKKEER |
| *vakdeskundige* | | *mens* | | correctie op C7, één moet-punt vervalt |
| auteur | 2 (reparatie) | 96.537 | 4 min | C5-vervolg, zelfde PR |
| beoordelaar-onderwijskundige | 2 | 171.484 | 1 min | AKKOORD MET PUNTJES |
| beoordelaar-pragmaticus | 2 | 149.122 | 1 min | AKKOORD MET PUNTJES |
| beoordelaar-redacteur | 2 | 170.495 | 2 min | AKKOORD MET PUNTJES |
| beoordelaar-eerstejaars | 2 | 177.786 | 3 min | AKKOORD MET PUNTJES |
| hoofdredacteur | 2 | 17.605 | 2 min | C7 AKKOORD MET PUNTJES |
| *vakdeskundige* | | *mens* | | merge |

**Totaal: ongeveer 2,66 miljoen tokens** voor één week — meer dan het dubbele
van werkitem #103, met dezelfde vorm van kostenopbouw: niet de omvang van het
werk, maar het aantal rondes.

Twee dingen vielen daarbij op, buiten wat al met bevinding 1 is vastgesteld:

**De poort ving iets dat de lus zelf niet kon vinden.** Tussen ontwerpronde 2
(AKKOORD van de verhelderaar) en ronde 3 zit geen FAAL maar een HERZIEN: de
vakdeskundige besliste bij de poort dat tuples naar PGM1 week 7 verhuizen, wat
het ontwerp moest verwerken. Dat is geen fout van de verhelderaar — het was een
besluit dat alleen bij de poort genomen kon worden (curriculumkeuze, niet
verifieerbaar tegen de repository) — maar het laat zien dat "AKKOORD" van de
verhelderaar niet betekent dat er bij de poort niets meer gebeurt.

**Alle vier beoordelaars vonden onafhankelijk dezelfde valse bevinding, omdat
niemand van hen het C4-besluit had.** De eerste beoordelingsronde leverde vier
keer BLOKKEER op, voor een deel op een bewering (de tuple-verwijzing naar PGM1
week 7 in `lectures/8a_datastructuren.ipynb`) die al bij de poort was
goedgekeurd als bewust vooruitlopen op issue #102. De beoordelaars kregen —
volgens het contract, met opzet — alleen de kern van C5, niet het C4-besluit
waarop die kern leunt. Drie van de vier bestempelden het als blokkerend, wat
een volledige tweede beoordelingsronde met alle vier de beoordelaars kostte
(≈669k tokens) om te herstellen. De twee overige moet-punten uit die eerste
ronde waren wel reëel en bleven staan na correctie. Dit is nieuw genoeg om apart
te noteren; zie [bevinding 14](bevindingen.md#14-beoordelaars-herhalen-een-besluit-dat-de-poort-al-nam-omdat-ze-het-besluit-niet-krijgen).

## Werkitem #182 — de docentenhandleidingen van week 1 en 2

Volledige lus, omvang M. **De eerste M die van begin tot eind is gemeten.** Tot dan waren
er alleen twee L's: 1,2 miljoen (#103) en 2,66 miljoen (#134).

| Rol | Ronde | Tokens | Duur | Uitkomst |
|---|---|---|---|---|
| triage | | 32.967 | 2 min | LUS, M |
| verkenner | | 105.825 | 11 min | C1b |
| curriculumontwerper | 1 | 58.415 | 8 min | C2 |
| verhelderaar | 1 | 64.593 | 6 min | **FAAL** |
| *vakdeskundige* | | *mens* | | twee gateantwoorden vooruitlopend op de poort |
| curriculumontwerper | 2 (herontwerp) | 60.606 | 6 min | C2 |
| verhelderaar | 2 | 80.576 | 8 min | AKKOORD |
| *vakdeskundige* | | *mens* | | C4 AKKOORD, vier besluiten, drie vragen uitgesteld |
| auteur | 1 (onderdeel 1 en 2) | 140.083 | 13 min | C5, PR #183 |
| auteur | 2 (onderdeel 3) | 245.131 | 23 min | C5, PR #184 |
| auteur | 3 (onderdeel 4) | 147.782 | 9 min | C5, PR #185 |
| **Totaal tot de beoordeling** | | **935.978** | | |

**Een M kost ongeveer een derde van een L.** Dat is de eerste keer dat die verhouding te
zien is, en zij past bij de vorm van de kostenopbouw uit bevinding 1: niet de omvang maar
het aantal rondes. Deze lus had één herontwerpronde tegen vier bij #134.

**De auteur is drie keer gedraaid omdat de oplevering bewust is geknipt.** Het ontwerp
droeg een afbreekregel voor het geval de termijn zou knellen; die is niet ingeroepen, maar
de knip is wel gebruikt om het werk over drie leveringen te verdelen. Dat kostte niets
extra's aan rondes en leverde drie keer een schone tussenstand op.

**De duurste rol was de tweede auteursronde** met 245k, de handleiding van week 2. Die
week is vier keer zo groot als week 1 (16 bestanden tegen 5, 15.114 woorden tegen 4.591),
en het verschil in kosten volgt dat vrijwel evenredig.

### Wat het draaien opleverde dat lezen niet had opgeleverd

De auteur heeft de twaalf korte antwoorden bij de collegeopdrachten uitgevoerd in plaats
van overgenomen. **Drie klopten niet meer:** `2a` Opdracht 7c en 7d geven `6.0` en `21.0`
waar de bron van 2023 `6` en `21` zei, want `x = x / 2` levert een float; en `2b` Opdracht
1b geeft `hanzehanzeHogeschool` waar de bron kleine letters zei. Die drie zouden anders aan
het bord verkeerd zijn voorgedaan.

### Twee keer werd een nul niet vertrouwd

De regel uit `CLAUDE.md` bewees zich twee keer, en beide keren zonder dat erom gevraagd
was. De verhelderaar merkte dat het voorgestelde ijkbestand voor het patroon
`\b(and|or|not)\b` de verkeerde kant op wees, en gaf het juiste getal: 13 regels in
`lectures/2a_var_con.ipynb`. En de auteur van onderdeel 4 kreeg nul op de zin *"Laat ze
kiezen: de lege kamer of het doolhof"*, zag dat de zin over twee regels afbreekt na `of`,
kortte het patroon in, en vond de regel wel.

### Wat de rollen corrigeerden aan de orkestrator

Drie keer, en dat is het argument voor de lus dat niet in de kosten zit:

- Het werkitem noteerde de `.docx` als **augustus 2024**; de verkenner las `docProps/core.xml`
  en maakte er **2023** van. Die fout stond ook in #95 en is daaruit overgenomen.
- Het werkitem zei dat de tekenobjecten **niet overzetbaar** waren; de verkenner liet zien
  dat `pandoc` alle 27 labels netjes teruggeeft en dat alleen de koppeling tussen pijl en
  vak verloren gaat.
- De orkestrator gaf de triage van #160 mee dat PGM2 geparkeerd was; die rol liet zien dat
  de parkeerreden gold voor ongevraagde veegbevindingen en niet voor een besteld werkitem.

## Werkitem #169 — PGM1 week 2, na handwerk buiten de lus

Volledige lus, omvang M. Hier staat wat er tot nu toe is gedraaid.

| Rol | Tokens | Duur | Uitkomst |
|---|---|---|---|
| triage | 53.333 | 2 min 54 s | LUS, M |
| verkenner | 163.154 | 20 min 10 s | C1b |

**De verkenner van deze M kostte meer dan die van een L.** Bij #134 was hij 141.279 in
9 minuten. Twee getallen zijn geen vergelijking, en het verschil is met de omvangklasse
niet verklaard: deze verkenner moest een echte Sphinx-build draaien om één vraag te
beantwoorden, en die van #134 niet. Wat het wél zegt is dat de omvangschatting de kosten
van deze rol niet voorspelt; het aantal metingen doet dat.

**De meting die de dure was, was ook de beslissende.** De vraag of `raises-exception` een
`SyntaxError` bij het bouwen opvangt is beantwoord met een minimaal Sphinx-project en een
cel die niet parseert - **ja**, met nul waarschuwingen, waar dezelfde cel zonder tag er
twee geeft. Die ijking is wat het nulresultaat vertrouwd maakt. Er bleek bovendien al een
precedent in de repo te staan, `solutions/4_midterm.ipynb` cel 28, dat niemand had
opgemerkt.

Daarmee verviel een besluit dat de orkestrator al bij de vakdeskundige had willen
neerleggen. **De meting was goedkoper dan het besluit**, en dat is de regel uit
`CLAUDE.md` op zijn duurste rol toegepast.

**Drie tellingen in `conventies/` bleken achterhaald**, alle drie door deze rol gevonden
en door de orkestrator nagemeten: `technische-conventies.md` r412-416 telt 193
`skip-execution`-cellen waar er 309 zijn, r436-441 meldt 5 afwijkende cellen waar er 0
zijn, en `conventies.md` r73-75 heeft twee verschillende maten onder één zin geschoven -
de 15 telde uitwerkingen zonder draaiende codecel, de 11 telt uitwerkingen met een
markdownblok.

**Een stille verkeerde meting is net vermeden.** De werkboom stond op een branch die van
een verouderde `master` was gemaakt en `solutions/2_opstap.ipynb` miste - het bestand dat
de kern van de opdracht was. De rol merkte het, mat op een schone uitdraai van `4c792e29`
met `git archive`, en meldde het in zijn artefact. Dat was geen mechanisme maar oplettendheid.

## Triageronde, 4 september 2026 — negen werkitems achter elkaar

Aanleiding: de routes waren stilgevallen. Van de 31 issues sinds de invoering van de
route-labels op 26 augustus hadden er 17 geen route, en in september waren er nog drie
toegekend. Acht daarvan waren echte werkitems; met het nieuwe #178 erbij zijn er negen
achter elkaar getrieerd, de acht van deze ronde parallel.

| Werkitem | Tokens | Duur | Besluit | Omvang |
|---|---|---|---|---|
| #178 opgaveniveaus | 40.544 | 2 min 45 s | LUS | L, bevestigt |
| #104 toetsmatrijs | 39.164 | 1 min 40 s | LUS | **S**, overruled M |
| #126 recursie week 3 | 25.963 | 1 min 2 s | LUS | **M**, overruled S |
| #136 Mandelbrot | 30.548 | 1 min 53 s | LUS | L, bevestigt |
| #144 examennotebooks | 24.678 | 1 min 23 s | LUS | M, bevestigt |
| #160 PGM2 week 5 | 41.152 | 2 min 4 s | LUS | L, bevestigt |
| #162 week 4, ronde twee | 23.180 | 1 min 29 s | LUS | L, bevestigt |
| #163 lusrecept week 5 | 26.602 | 1 min 56 s | LUS | **M**, overruled S |
| #169 week 2 | 53.333 | 2 min 54 s | LUS | M, bevestigt |
| **Totaal** | **305.164** | | 9× LUS | 3 bijgesteld |

**Negen van de negen gaan de lus in.** Geen afwijzing, geen splitsing. Dat is het
tegenovergestelde van wat de vorige twee triages opleverden - #115 kreeg AFWIJZEN met
een splitsingsadvies - en het betekent dat het overslaan van de triage de afgelopen week
geen afweging was maar een gewoonte die wegviel. Er zat niets tussen dat de lus niet
verdiende.

**Een triage kost gemiddeld 34k en nooit meer dan 53k.** Over alle elf gemeten triages
loopt de spreiding van 19.671 (#115) tot 53.333 (#169). Een volledige lus kostte 1,2
miljoen (#103) en 2,66 miljoen (#134). **Triage is daarmee ongeveer anderhalf procent van
wat hij routeert**, en hij nam hier drie keer een omvangoordeel over dat van de indiener.
Dat bevestigt bevinding 6 op een grotere steekproef dan waarop zij was geschreven.

**Wat de triages vonden dat de werkitems zelf niet wisten.** Dit is de opbrengst die niet
in het besluit zit maar in het lezen:

- **#104** — vier van de zeven criteria waren ingehaald, en de A3-bevinding uit de
  veegronde bleek per 1 september al uitgevoerd. Daarnaast draagt `leeruitkomsten.md`
  r118 nog de achterhaalde meting "40 van de 90 punten ontwerpwerk", die
  `uitgangspunten.md` r610-621 corrigeert naar 15. Twee getallen voor hetzelfde feit, in
  de laag die bindt.
- **#126** — de regelverwijzingen in het werkitem zijn verschoven: `leerlijn.md` r73-75
  in plaats van r42-44, `uitgangspunten.md` r352-355 in plaats van r325-328. De documenten
  zijn onder het issue vandaan geschoven.
- **#163** — acceptatiecriterium 2 hoort er niet in: *verzamelvariabele* is al besloten in
  `begrippen.md` r39, met de uitvoering toegewezen aan #162. Er kwam een vierde vindplaats
  bij die in geen lijst stond: `problems/11_basis.ipynb` r526.
- **#169** — het handwerk van 4 september sloot criterium 1 en 6, maar niet 2. En
  `solutions/2_rochambeau.ipynb` wordt **niet** vanzelf een draaiende cel: met `input()`
  en `while True:` valt het onder de uitzondering van `technische-conventies.md` r433-434.
- **#160** — de parkeerregel van #124 gold voor óngevraagde veegbevindingen op andermans
  weken, niet voor een besteld werkitem op een vastgelegde lijn. De orkestrator gaf die
  parkeerreden mee als aanname, en de rol weerlegde haar.

Dat laatste is het patroon van deze ronde: **vijf van de negen triages corrigeerden een
bewering in het werkitem of in de opdracht die zij meekregen.** Geen daarvan was met het
blote oog zichtbaar.

## Werkitem #178 — één stelsel voor de opgaveniveaus

Volledige lus, omvang L volgens triage. De lus is **nog niet gesloten**: het C7 luidt
BLOKKEER en er volgt een tweede auteursronde met een tweede beoordelaarsronde.

| Rol | Ronde | Tokens | Duur | Uitkomst |
|---|---|---|---|---|
| triage | | 40.544 | 2 min 45 s | LUS, L |
| verkenner | | 103.214 | 12 min 29 s | C1b |
| curriculumontwerper | 1 | 65.450 | 7 min 30 s | C2 |
| verhelderaar | 1 | 97.897 | 9 min 5 s | **FAAL** |
| curriculumontwerper | 2 | 90.305 | 11 min 36 s | C2, herontworpen |
| verhelderaar | 2 | 111.496 | 12 min 20 s | AKKOORD, geen wijzigingen |
| auteur | 1 | 254.269 | 13 min 29 s | C5 |
| beoordelaar onderwijskundige | 1 | 123.652 | 10 min 11 s | BLOKKEER |
| beoordelaar eerstejaars | 1 | 126.308 | 9 min 22 s | BLOKKEER |
| beoordelaar redacteur | 1 | 131.656 | 9 min 56 s | BLOKKEER |
| beoordelaar pragmaticus | 1 | 89.609 | 6 min 2 s | AKKOORD MET PUNTJES |
| hoofdredacteur | 1 | 76.489 | 5 min 11 s | **BLOKKEER** |
| auteur | 2 | 298.059 | 8 min 23 s | C5, moet 1 en 3 hersteld |
| auteur | 3 | 331.037 | 7 min 5 s | C5, na poortbesluit op moet 2 |
| beoordelaar pragmaticus | 2 | 116.726 | 7 min 27 s | AKKOORD MET PUNTJES |
| beoordelaar onderwijskundige | 2 | 134.792 | 10 min 50 s | BLOKKEER |
| beoordelaar eerstejaars | 2 | 190.869 | 11 min 42 s | AKKOORD MET PUNTJES |
| beoordelaar redacteur | 2 | 155.828 | 13 min 7 s | AKKOORD MET PUNTJES |
| hoofdredacteur | 2 | 60.845 | 4 min 42 s | **BLOKKEER** |
| auteur | 4 | 373.526 | 7 min 16 s | C5, elf van elf criteria |
| | **totaal** | **2.972.571** | | **gesloten zonder C7** |

**De lus is niet afgemaakt.** Na auteursronde 4 heeft de vakdeskundige hem gestopt:
*"ik heb het idee dat we wat teveel in cirkeltjes ronddraaien en veel tijd aan details
wordt besteed. ik wil door, naar week 3, handleidingen verder schrijven etc."* Er is
dus geen derde beoordelaarsronde en geen eindoordeel over ronde 4. Dat is een besluit
van de vakdeskundige en geen omissie, en het staat hier zodat het niet als een
afgeronde lus wordt gelezen. Waarom het zover kwam staat in
[bevindingen.md](bevindingen.md), bevinding 16.

**Het materiaal was na ronde 2 klaar.** Tien van de elf criteria gaan over `source/`
en stonden vanaf `6913faae` op *gehaald*; alles daarna ging over criterium 1, dat over
`conventies/begrippen.md` gaat.

**Dit is de duurste lus tot nu toe die nog niet af is.** Een volledige M kostte bij #182
935.978 in één doorloop; #178 staat op 1,31 miljoen mét een blokkade en een tweede
auteursronde nog voor de boeg. Twee dingen verklaren het grootste deel: de verhelderaar
faalde en dwong een volledig herontwerp (163.347 voor de twee ontwerprondes samen), en de
auteur is met 254.269 de duurste enkele rol die tot nu toe is gemeten — acht onderdelen
over 36 bestanden.

### De vier beoordelaars vonden alle vier hetzelfde, en dat was het punt

Alle vier vonden onafhankelijk de twintig `# Opgave N`-labels in de codecellen van
`practicals/2_sequenties_en_data.ipynb` en zijn uitwerking. Geen van hen had ze van de
orkestrator gekregen; die had ze zelf gevonden en er met opzet niets over gezegd, juist om
te zien of de ronde ze zou opleveren.

**Dat is de eerste keer dat alle vier op één bevinding uitkwamen.** Het is ook de
bevinding die de hele oplevering blokkeerde, en de enige plek waar het defect dat #178
wegneemt was blijven staan *binnen een bestand dat de ingreep zelf had aangeraakt*.

De vier deden het wel elk op een eigen manier, en dat verschil is de waarde:

- De **pragmaticus** telde: 46 treffers op `Opgave [0-9]` in `source/`, 26 in de tentamens
  en 20 in twee bestanden — en zag daarmee als eerste dat het criterium *"nul genummerde
  `Opgave N`"* het woord *koppen* niet bevat, terwijl het bewijs alleen koppen telt.
- De **eerstejaars** las de pagina en vond dat de lopende tekst beide woorden in één zin
  gebruikt: *"De eerste opgave krijg je van ons, dit is een voorbeeld van hoe je de
  opdrachten moet maken."*
- De **redacteur** telde de gevolgen door: wie practicum en uitwerking naast elkaar legt,
  leest **drie** namen voor één ding.
- De **onderwijskundige** zocht de grond op: `begrippen.md` r162 kent *opdracht* toe aan
  "een genummerde taak binnen een document", niet aan een kop. Daarmee stond vast dat het
  criterium niet in de engere lezing gered kon worden.

De pragmaticus zette het als enige onder *zou moeten*. De hoofdredacteur hief dat op, met
de grond van de onderwijskundige.

### Eén beoordelaar tegen drie, en de ene had gelijk

Bij acceptatiecriterium 1 keurden drie beoordelaars goed en de redacteur af. Alle drie de
goedkeurders baseerden zich op dezelfde waarneming — `begrippen.md` draagt het besluit, de
andere drie documenten verwijzen terug — en geen van hen trok de verwijzing na. De
redacteur wel, en vond dat `technische-conventies.md` r146-149 een doorlaatregel aan
`begrippen.md` toeschrijft die daar niet staat.

De hoofdredacteur legde de twee passages zelf naast elkaar en gaf de redacteur gelijk.
**Meerderheid is hier geen bewijs geweest:** drie rollen namen dezelfde toeschrijving over
zonder haar te toetsen, wat precies het soort fout is dat een geïsoleerde ronde hoort te
vangen en bijna niet ving.

### Wat de rollen corrigeerden aan de orkestrator

Vier keer, en drie ervan raakten iets dat al in `conventies/` of `curriculum/` was beland:

- **Het poortbesluit stelde dat PGM2 alleen in cursusweek 9 een opstap heeft.** `_toc.yml`
  r146 belegt PGM2 week 1 als cursusweek 8; het zijn er twee. De **auteur** signaleerde het
  en schreef de meting op in plaats van het getal over te nemen. De correctie staat op de
  issue.
- **De toetsbare zin die de orkestrator in het poortbesluit formuleerde** — *"elke
  werkeenheidkop in `solutions/` heeft een kop in `problems/` met hetzelfde nummer"* — is
  onwaar voor het materiaal dat zij bindt, en stond inmiddels in `begrippen.md`. De
  **eerstejaars** vond het: vier van de negen `solutions/`-bestanden met werkeenheidkoppen
  hebben helemaal geen tegenhanger onder `problems/`; zij spiegelen `lectures/` en
  `practicals/`. De auteur had de regel over de páren gedraaid en niet over de zin zoals
  die is opgeschreven.
- **Besluit 2 van het poortbesluit nam aan dat de veertien `Uitwerking N-X`-koppen bij
  opdracht 1 t/m 19 hoorden.** Ze horen alle veertien bij één ongenummerde debugopgave. De
  **auteur** paste de regel toe en niet het getal, en legde uit waarom nummeren daar juist
  misleidend zou zijn.
- **De kern noemde `extra/practice/1_recursie` en `2_list_comprehension` "de twee
  toetsbestanden"** en hield ze op die grond buiten de regel. De **onderwijskundige** en de
  **redacteur** maten dat `conventies.md` r32-39 vier andere bestanden bij naam uitzondert
  en deze twee niet.

### De verhelderaar faalde één keer, en dat was de goedkope ronde

Ronde 1 kostte 97.897 en leverde FAAL. Ronde 2 kostte 111.496 en leverde AKKOORD zonder
gevraagde wijzigingen, met tien punten om aan de auteur mee te geven. Het herontwerp
ertussen kostte 90.305. **Samen 299.698 om te voorkomen dat een auteur van 254.269 op een
ondeugdelijk ontwerp begon** — en de auteursronde is toch geblokkeerd, op iets wat geen van
beide verhelderaarrondes kon zien omdat het buiten de koppen zat.

### Wat de orkestrator zelf misdeed

Twee keer een patroon niet geijkt, allebei in dezelfde sessie:

- Een grep op `#{1,6} Opgave +[0-9]+` over `source/*.ipynb` gaf twintig treffers die als
  koppen werden gelezen. Het waren Python-commentaarregels in codecellen — in een notebook
  ziet `# Opgave 1` er hetzelfde uit als een H1. De conclusie ("de auteur heeft twintig
  koppen gemist") was fout; de vondst eronder bleek toevallig wél de bevinding die de
  ronde blokkeerde.
- Een telling van bouwwaarschuwingen gaf "1 warning" doordat er twee `make`-processen
  tegelijk liepen, en daarna "2" doordat het patroon `suppress_warnings=[]` uit de
  myst-configuratieregel meetelde. Serieel en op de samenvattingsregel gemeten: schoon.

## Werk buiten de lus om

Hier hoort wat met de hand is gedaan omdat het te klein leek voor een werkitem.

### 23 september 2026, curriculumbesluiten vóór het C4 van #160

**Wat het was.** Vijf besluiten van de vakdeskundige vastgelegd in `curriculum/` en
`conventies/`, als aparte PR vóór het poortbesluit van #160: de klassenstof van PGM2 week 4
gaat naar week 5, excepties landen in week 7, de PGM2-tabel in `leerlijn.md` krijgt een kolom
met leeruitkomsten en een met nieuwe begrippen, de verplichte opgaveniveaus worden voor heel
PGM2 ingevuld, en docstrings en commentaar blijven Nederlands zonder overgang naar Engels. De
keuzes kwamen van de vakdeskundige in het gesprek; de invulling per week van de twee nieuwe
kolommen is een voorstel van de orkestrator, ter beoordeling in de PR.

**Waarom het buiten de lus bleef.** Het zijn de antwoorden op open vragen uit het C2 van #160
die `curriculum/` en `conventies/` raken. Die horen vastgelegd te zijn voordat C4 ernaar
verwijst, en de lus heeft voor die vastlegging geen eigen stap.

**Ging er een beoordelaar overheen?** Nog niet bij het openen van de PR; de vakdeskundige
beoordeelt de kolominvulling in de PR zelf.

**Vervolg, dezelfde dag.** De begrippen van week 5 kwamen in een tweede commit op dezelfde
branch, die pas werd gepusht nadat #261 al gemerged was; ze belandden niet in `master` en
moesten via #262 alsnog. Daarna volgde een derde PR met de practicumopzet voor week 5 tot en
met 7 (`curriculum/practicum-oop.md`) en de besluiten die daaruit volgden voor de opgavenlaag
en de begrippenkolom van week 5. De referentie-oplossing uit de opzet is gedraaid; wat ze
beweert klopt op de gecontroleerde punten.

### 18 september 2026, drie directe correcties (PR #249 en #250)

**Wat het was.** Drie meldingen van de vakdeskundige, alle drie op dezelfde dag gemeld,
gerepareerd en gemerged. Twee in de interactieve cel: CodeMirror sprong twee spaties in terwijl
de code op de pagina er vier gebruikt (een `IndentationError` zodra een student in een bestaande
functie doortypte), en Sphinx' `doctools.js` kaapte `/` naar de zoekbalk omdat het alleen
`TEXTAREA`, `INPUT`, `SELECT` en `BUTTON` overslaat en `document.activeElement` bij een editor in
een schaduw-DOM het element `<interactive-code-cell>` zelf is. De derde was een kop die in week 2
*Extra* uit een code-span ontsnapte; zie de bevinding van diezelfde datum.

**Waarom het buiten de lus bleef.** Drie gemeten oorzaken met elk een ingreep van één tot drie
regels, in materiaal dat op dat moment op de site stond. Dat is de proportionaliteitsregel uit
`CLAUDE.md`: een branch met een pull request, geen werkitem.

**Ging er een beoordelaar overheen?** Nee — de vakdeskundige heeft ze zelf visueel gecontroleerd
in een `sphinx-autobuild` op een gecombineerde branch, vóór de merge. Dat was hier ook de enige
zinnige controle: twee van de drie zijn browsergedrag dat een agent niet kan waarnemen. De derde
is wél gemeten: twee `<h1>` in de gebouwde pagina vóór, één na.

**Twee splitsingen die de moeite waard bleken.** De twee onderwerpen kregen elk een eigen PR
(#249 lesmateriaal, #250 de extensie), zodat ze los terug te draaien zijn. En de visuele controle
liep op een derde, gecombineerde branch, zodat de PR's zelf ongemoeid bleven.


### 16 september 2026, #231 — de tweede S-route, en een scoperegel die te ver reikte

**Wat het was.** `source/solutions/3_opstap.ipynb` nieuw: tien cellen, drie draaiende codecellen,
437 woorden. Plus een regel in `_toc.yml` en één woord in de opgave. PR #234, drie bestanden.

**De route.** Dezelfde vorm als #230 — auteur en één beoordelaar — maar met één verschil dat
er wél toe deed: **de beoordelaar is hier de onderwijskundige en niet de eerstejaars.** Deze
oplevering bestaat uitsluitend uit uitwerkingen, en `loop.md` belegt criteria daarover bij een
rol die ze mag lezen. Een eerstejaars had hier niets kunnen toetsen.

| Rol | Tokens | Duur | Uitkomst |
|---|---|---|---|
| auteur, ronde 1 | 106.234 | 11 min 34 s | C5 |
| beoordelaar-onderwijskundige | 82.220 | 9 min 56 s | AKKOORD MET PUNTJES, 0 blokkades, 5 puntjes |
| auteur, ronde 2 (puntjes) | 127.531 | 2 min 57 s | alle vijf verwerkt |
| **totaal agents** | **315.985** | **circa 25 min** | |

Iets duurder dan #230 (236.000), en dat is te verklaren: nieuw materiaal in plaats van een
pagina, en een beoordelaar die een volledige Sphinx-build met koude cache draaide om te kunnen
zien of de uitvoer op de pagina werkelijk in díé build was uitgevoerd.

**Twee metingen die het navolgen waard zijn.**

De auteur **ontmaskerde zijn eigen nul**. Zijn eerste meting voor criterium 2 zocht op `\bin\b`
en vond drie treffers; alle drie bleken het Nederlandse voorzetsel *in* in het proza te zijn en
niet de operator uit week 4. De eindmeting draait op de AST. Dat is precies het stukgelopen
patroon waar `CLAUDE.md` voor waarschuwt, en hij liep erin en kwam eruit.

En hij **bewees de schone build in plaats van hem te greppen**. `grep -icE "warning|error"` gaf 2,
allebei de configuratiebanner van myst. Vervangen door `sphinx-build -W --keep-going` met een
exitcode, en die geijkt door de `_toc.yml`-regel tijdelijk te verwijderen: exit 1 met
`document isn't included in any toctree`. Daarmee is zowel de nul bewezen als aangetoond dat de
toc-regel nodig was.

**Waar ik het fout deed, en dat is de aantekening waar het om gaat.**

De opgave draagt een scheve deelvraag: opdracht 3 heeft een a, b én c, maar deelvraag d zei
*"om je antwoord op a en b te controleren"*. Eén woord. C0 en mijn C1 legden de opgave **hard
buiten scope**, dus de auteur hield zich eraan en meldde het als niet gedaan vervolg; de
beoordelaar deponeerde het opnieuw. **Ik heb het twee keer doorgeschoven naar een eigen
werkitem.**

De vakdeskundige: *"had dat niet door een van de rollen aangepakt moeten worden? de auteur bijv.?
ik vind dit slordig."* Hij heeft gelijk, en `CLAUDE.md` zegt het met zoveel woorden: *"Een
typefout, een dode link of een naam rechtzetten doe je gewoon, in een branch met een pull
request."*

**Wat hier misging is niet dat de auteur de regel volgde, maar dat ik hem schreef.** Een
scopegrens in C1 is er om te voorkomen dat een werkitem uitdijt tot een herziening van de hele
week. Zij hoort niet boven de proportionaliteitsregel te staan voor een woord dat aantoonbaar
fout is. Het gevolg was bovendien precies wat de vakdeskundige eerder had gevraagd te vermijden:
een enorm werkitem optuigen voor iets kleins. Rechtgezet met `8b42a59d`, in dezelfde PR.

**Of er een beoordelaar overheen is gegaan.** Over de uitwerking: ja, de onderwijskundige, met
vijf puntjes die alle vijf zijn verwerkt. Over de éénwoordscorrectie in de opgave: nee — die is
door de orkestrator gedaan nadat de beoordelaar hem zelf had aangewezen, en dat staat hier in
plaats van onzichtbaar te blijven.

**Eén ding is als eigen werkitem weggezet, en terecht.** De beoordelaar mat als ijking dat
`solutions/3_basis.ipynb` negen codecellen heeft en nul uitvoerblokken. Nagemeten: negen
functies, **34 assertions** en nul `print`-aanroepen. De assertions draaien bij elke build en
gaan door, dus de verificatie is echt; wat ontbreekt is het *zichtbare* bewijs. Dat is smaller
dan het klonk en het is een lijnvraag over alle uitwerkingen, geen defect in dit bestand — zie
**#235**.

### 16 september 2026, #230 — de eerste S-route onder de nieuwe procesversie

**Wat het was.** `source/course/week_3.md` van 7 woorden naar 267: het besluit *Wat een
weekpagina draagt* voor de vierde keer uitgevoerd. PR #232, twee bestanden.

**De route, en waarom hij kort was.** Twee rollen: **auteur → eerstejaars**. Geen
verkenner, geen ontwerper, geen verhelderaar, geen poort, geen C7. De routenorm
reserveert die voor een sectie of een week; dit was één bestand. Wat een verkenner zou
meten stond in C1 — de woordentelling van de vier bestaande weekpagina's en het patroon
dat eruit volgt — en er viel niets te ontwerpen, want het besluit lag vast en was drie
keer uitgevoerd.

| Rol | Tokens | Duur | Uitkomst |
|---|---|---|---|
| orkestrator (C1, meetbasis, PR, C7 n.v.t.) | niet beschikbaar | niet beschikbaar | route van zeven rollen naar twee |
| auteur, ronde 1 | 76.404 | 4 min 44 s | C5, 240 woorden |
| beoordelaar-eerstejaars | 119.155 | 8 min 23 s | AKKOORD MET PUNTJES, 0 blokkades, 5 puntjes |
| auteur, ronde 2 (puntjes) | circa 40.000 | 9 min | 4 van 5 puntjes, plus de registerregel |
| **totaal agents** | **circa 236.000** | **circa 22 min** | |

Ter vergelijking uit dit bestand: een volledige lus op een week kostte eerder 1,2 tot
3,0 miljoen tokens. **Een S-route die bij de omvang past kost daar ongeveer een
twaalfde van.** Dat is geen besparingspercentage — het is ander werk — maar het laat
zien wat de routetabel oplevert wanneer je hem volgt in plaats van de volle lus te
draaien omdat dat de gewoonte is.

**Wat de beoordeling opleverde.** Nul blokkades en vijf puntjes, waarvan er vier zijn
verwerkt. Twee daarvan waren het lezen waard:

- **De pagina beschreef week 2 anders dan de student hem beleefde.** Er stond dat week 2
  *"programma's die van boven naar beneden aflopen"* opleverde, terwijl de grootste
  opgave van die week van begin tot eind in `def adventure():` staat. De eerstejaars:
  *"Als ik dan lees dat ik deze week code een naam ga geven, vraag ik me af of dat
  taartprogramma dan iets anders was."* De auteur heeft de opgave op de huidige stand
  nagelezen en de alinea herschreven.
- **De pagina beloofde wat de week niet vraagt.** Gemeten: `main` komt 14 keer voor in
  `3b_functies_aanroepen.md` en 9 keer in `3_opstap.ipynb`, maar **nul** keer in
  `3a_functies`, `3_fijne_functies`, `3_basis` en `3_extra`. De student ziet en leest
  een main-functie, maar schrijft er nergens zelf een. De auteur weigerde de zin stil af
  te zwakken en meldde het als observatie. De vakdeskundige loste het anders op dan alle
  drie de rollen hadden voorzien: *"is dat niet te veel detail voor zo'n pagina? het gaat
  om functies leren gebruiken en aanroepen."* **De zin is geschrapt in plaats van
  verzwakt, en daarmee verdween de bevinding in plaats van dat zij werd weggeschreven.**

**Wat er buiten de lus om is gedaan, en door wie.** Twee dingen, allebei door de
orkestrator en allebei op expliciete instructie van de vakdeskundige: de registerregel
in `curriculum/uitgangspunten.md` r326 (*"rechtzetten maar"*, uitgevoerd door de auteur
in ronde 2) en het schrappen van de main-functie-zin (*"prima"* op het voorstel,
uitgevoerd door de orkestrator). **Over die laatste is geen beoordelaar gegaan.** De
grond: het is een schrapping die een openstaande bevinding sluit, en een weggehaalde
belofte hoeft niet opnieuw gewogen te worden. Dat is een oordeel, en het hoort hier te
staan in plaats van onzichtbaar te blijven.

**Eén ding dat de route zichtbaar maakt.** De eerstejaars meldde dat hij **geen C5-kern
had ontvangen** — zijn invoer waren C0, C1 en de repository. Dat was mijn keuze en hij
had er geen last van, maar hij heeft gelijk dat het zichtbaar hoort te zijn. Bij een
route zonder ontwerp is de C5 er pas nadat de auteur klaar is; de beoordelaar krijgt dan
de branch en de criteria, niet het verhaal van de auteur. Of dat de bedoeling is van
*"geen maakgeschiedenis"* of een gat, is een vraag voor de onderzoeker.

### 16 september 2026, de tweede CodeMirror-pin (PR #226)

**Wat het was.** Drie imports in `extensions/sphinx_interactive_code/static/interactive-code.js`
kregen de ontbrekende `?deps=`-termen, zodat `@codemirror/language` en `@codemirror/view` net zo
hard vaststaan als `@codemirror/state` sinds #222.

**Waarom buiten de lus.** Drie regels in één bestand, met een reparatie die volledig meetbaar is:
haal de zes URL's uit het bestand, volg hun eigen imports, tel de unieke module-URL's per gedeeld
pakket. Vier pakketten, vier keer precies één. Dat is de tabel in `loop.md` voor een kleine,
eenduidige correctie.

**Of er een beoordelaar overheen is gegaan.** **Nee.** Wel de vakdeskundige, en dat is hier de
controle die telt: de editor laadt weer in de browser. Wat een beoordelaar had kunnen toevoegen
is niet de meting maar de vraag of vendoren niet verstandiger is dan een derde ronde aan een
graaf die wij niet beheren; die vraag staat in `bevindingen.md`.

**De leerzame misstap zit in de aanvulling op de bevinding, niet hier.** Kort: mijn eerste opzet
gaf alle zes de imports dezelfde volledige deps-lijst, en dat breekt precies wat het oplost -
een pakket dat zichzelf in zijn eigen deps noemt, krijgt een eigen bouw en wordt daarmee de
tweede instantie. Gevonden door te meten vóór de commit, niet erna.

### 15 september 2026, de vergelijkingssectie van `2b` (één commit)

**Wat het was.** Vier redactionele ingrepen in `lectures/2b_strings_en_lists.ipynb`, cellen
57-67: de kop `` ## `max` of `min` `` heet nu `## Groter en kleiner` en `` ### `str`ings to
the `max` `` heet `### Element voor element`, een dangling zin is afgemaakt, en drie typo's
zijn weg. Plus de bijbehorende regel in `handleidingen/week_2.md`, die beide koppen bij naam
noemt.

**De aanleiding, en wat de meting ervan maakte.** De vakdeskundige signaleerde dat Opdracht 5
(`[4,2] > [42]`, `"hoi" > "doei"`) kennis veronderstelt die nergens is besproken, en vroeg of
zij te veel docentuitleg kost. **Die premisse bleek onjuist**: cellen 57-67 staan vier cellen
boven de opdracht en leggen precies de regel uit, met drie voorbeelden in dezelfde vormen. De
zes items zijn ook nagelopen op ASCII-afhankelijkheid: geen enkele kruist een
hoofdletter/kleine-lettergrens of zet cijfers naast letters, dus alfabetische volgorde plus de
prefixregel volstaat. Item 1 en 6 worden beslist op het eerste getal en raken de string nooit.

Wat er wél aan mankeerde, en waardoor de sectie niet als uitleg wordt gevonden:

- **De kop beloofde iets anders dan er stond.** `max(` en `min(` komen in het hele bestand nul
  keer voor.
- **De ASCII-belofte werd opgeworpen en laten vallen.** *"Intuïtief zou je denken dat dit een
  vergelijking is op basis van de positie in het alfabet"* kondigt een weerlegging aan die
  nooit kwam; de volgende zin bevestigde het alfabetverhaal gewoon. Daar zat de docentvraag.
- Drie slordigheden in de uitleg van `"Mug" > "Muis"`: *de twee letters*, *alfebet*, en een
  regel zonder punt.

**Waarom buiten de lus.** Vier redactionele correcties in één sectie, op instructie van de
vakdeskundige: *"mag idd als een enkele commit, geen loop op loslaten."* De zes
demonstratiecellen dragen geen `skip-execution` en draaien dus bij elke build; de uitvoer die
de student ziet is daarmee gecontroleerd.

**Of er een beoordelaar overheen is gegaan.** **Nee.** Bewust niet, en dat is hier de
aantekening waard: het contrast met de rochambeau-ingreep hierboven, waar de lezer vier
moet-punten vond, staat in dezelfde week in ditzelfde bestand.

### 15 september 2026, de uitwerking van rochambeau (PR #216)

**Wat het was.** `source/solutions/2_rochambeau.ipynb` is volledig vervangen. De oude
uitwerking is nooit door een rol geschreven: zij kwam met `79a0680e` (28 augustus 2024,
`suzanbones`) uit `referentie/cs5/problems/rochambeau/index.md` en is daarna alleen door de
Sphinx-migratie en een spellingronde aangeraakt. Zij loste een opgave van week 2 op met
`import time` en zeven `time.sleep`-pauzes, een losse docstring op moduleniveau, drie takken
die alle negen combinaties uitschrijven met regelcommentaar van 140 tekens, en een uitbreiding
van ruim honderd regels binnen `while True:` met `break` - een lus komt in week 4. Er staan nu
vier programma's, alle vier binnen wat de week biedt: de canonieke vorm, dezelfde met alleen
`if` en `else`, de compacte vorm met `and`/`or`, en RPS-5 in die compacte vorm.

**Waarom buiten de lus.** De vakdeskundige merkte de uitwerking aan als een grote red flag -
*"absurd uitgewerkt/gecompliceerd in relatie tot wat de studenten weten"* - en gaf drie
canonieke vormen woordelijk op. Daarmee zat het ontwerp er al in en bleef er één bestand over
om te schrijven; de instructie erbij was *"de rochambeau oplossing moet iig nu per direct
aangepakt worden"*, zonder meta-werkitem. Dat is de regel voor proportionaliteit uit
`loop.md`: een branch met een pull request en een onafhankelijke lezer.

**Of er een beoordelaar overheen is gegaan.** Ja, één: de eerstejaars, op commit `12c20d25`.
Oordeel **NIET AKKOORD**, met vier moet-punten, en ze waren alle vier terecht:

| | Wat hij vond | Bewijs |
|---|---|---|
| 1 | De inleiding beweerde "niets van buiten week 2" en noemde daarin `from random import choice` | `curriculum/leerlijn.md` zet *module en `import`* en `choice` in week 3; in heel week 2 komt de regel alleen voor in de gegeven begincode van het practicum |
| 2 | Het tweede programma was niet het eerste, uitgeschreven | Het eerste stelde drie vragen over `comp`, het tweede twee: `if comp == "schaar":` ontbrak |
| 3 | "Geen van de drie is beter dan de andere" werd twee keer weersproken | Cel 6 en cel 8 noemen elk een vorm slechter; cel 10 noemt de derde juist beter |
| 4 | De meerregelige voorwaarde tussen haakjes was nergens geïntroduceerd | In al het week 1- en week 2-materiaal eindigt geen enkele coderegel op `(`, `[` of `,` |

Punt 2 is het punt dat telt: dat is een **defect dat de vier meetronden niet vingen**. Alle vier
de programma's waren nagerekend over elke combinatie - 9, 9, 9 en 25, nul afwijkingen - en het
tweede programma is dan ook correct. Het is alleen niet wat de tekst erboven belooft, en juist
een student die de twee naast elkaar legt om zichzelf na te kijken loopt daarop vast. **Een
uitwerking die klopt kan nog steeds de verkeerde uitwerking zijn**, en dat verschil meet geen
test; daar is de lezer voor.

Vijf zou-punten zijn ook verwerkt; alles staat in `7f3eb50d`.

**Nagekomen, na lezing door de vakdeskundige.** Twee van de vier oordelen hierboven
moesten worden bijgesteld, en de tweede bijstelling is de leerzame.

*M4 klopte maar half.* `lectures/2a_var_con.ipynb` noemt `( )` als groepering in de
operatorentabel en zegt bij het `if`-statement dat haakjes om een conditie mogen maar niet
hoeven. De student kent haakjes dus wel; nieuw is alleen dat een regel doorloopt zolang er
een openstaat. De alinea sluit daar nu op aan in plaats van haakjes te introduceren.

*M1 betrof een erkende uitzondering.* De vakdeskundige: *"`from random import choice` is een
uitzondering, tijdens lessen zeg ik vaak neem dit aan voor nu."* Die vooruitverwijzing stond
nog nergens vast - de tabel *Vooruitverwijzingen om na te lopen* in `curriculum/leerlijn.md`
had `while` voor dit bestand al staan en `choice` niet - en staat er nu in.

*En mijn eerste herstel van M3 was zelf fout.* De tegenspraak was weggenomen door er een
regel voor in de plaats te zetten: *"kies de vorm die het kortst blijft bij het aantal
gevallen dat je hebt."* Die regel is onwaar, en dat was in het bestand zelf te meten: de
compacte vorm is bij drie wapens al de kortste (10 regels logica tegen 17 en 22), terwijl
diezelfde pagina zegt haar nog niet te schrijven. **Een tegenspraak wegschrijven met een
regel die je niet hebt nagemeten, levert een nieuwe tegenspraak op.** Er staat nu één
maatstaf - hoeveel benoemt de vorm hardop - met de gemeten getallen voor drie én vijf
wapens erbij. Dat staat in `7492f3e2`.

**Eén afwijking van de rolnorm**, door de lezer zelf gemeld: `beoordelaar-eerstejaars.md` zegt
*"Je kijkt niet in de uitwerking"*, en hier was de uitwerking juist het artefact. De rol is
gevraagd omdat de vraag "helpt dit een eerstejaars die zichzelf nakijkt" precies zijn vraag is.
Of die norm een uitzondering hoort te krijgen voor `solutions/`, is een besluit voor de
vakdeskundige en staat nog open.

### 9 september 2026, midden in de lus van #178

**Wat het was.** Eén zin in `conventies/begrippen.md`: de toetsbare zin bij de nummeringsregel
kreeg een clausule, zodat een genummerd label boven een codecel telt als tegenhanger van een
uitwerkingskop. Plus twee zinnen die vastleggen dat het om precies één bestand gaat.

**Waarom buiten de lus.** De auteur draaide zijn eigen toetsbare zin als controle en meldde het
counterexample in plaats van het weg te schrijven - `practicals/2_sequenties_en_data.ipynb` draagt
zijn tien taken als label en niet als kop. De vakdeskundige stelde daarop de zin woordelijk vast.
Daarmee zat er geen oordeel meer in, en de drie auteursrondes ervoor kostten 254.269, 298.059 en
331.037 tokens. **Een vierde ronde van die orde voor één vastgestelde zin is niet proportioneel.**

**Of er een beoordelaar overheen is gegaan.** Ja - alle vier, in de tweede beoordelaarsronde van
deze lus, met deze zin erin en met de aantekening erbij dat zij geen auteur had. Drie van de vier
legden de zin zelf langs alle negen uitwerkingsparen en vonden geen tegenvoorbeeld. Dat is de
eerste keer dat handwerk buiten de lus binnen dezelfde lus is nagelezen in plaats van achteraf of
niet; de eerste zeven ingrepen scoorden nul.

**Nagekomen correctie.** Deze alinea stond er eerst in de voltooid verleden tijd terwijl de
beoordelaars nog draaiden. De redacteur ving dat als puntje: *"stelt in de voltooid verleden tijd
vast dat de vier beoordelaars over de hele oplevering zijn gegaan; op het moment van schrijven was
dat nog niet zo."* Het klopte alsnog, maar dat is geluk en geen meting - **een bewering die vooruit
wordt opgeschreven is geen meting, ook niet als zij achteraf uitkomt.**
Daar is geen tokentelling van, en er is ook geen mechanisme dat het afdwingt - dit
kopje bestaat opdat een lege lijst zichtbaar maakt dat er niets is opgeschreven, in
plaats van dat het lijkt of er niets is gebeurd.

Noteer in elk geval: wat het was, waarom het buiten de lus bleef, en of er achteraf
een beoordelaar overheen is gegaan. Dat laatste is de regel *wie het zelf doet,
laat het lezen*, en of die wordt nageleefd is precies wat hier te zien hoort te
zijn.

### 29 augustus - 1 september 2026

Twee dagen handwerk, niet in tokens gemeten. Wat er is gedaan, en of het is
gelezen:

| Werk | Waarom buiten de lus | Achteraf gelezen? |
|---|---|---|
| Week 0: AI-uitleg bij het inrichten van de editor (#74) | Nieuwe tekst op een bestaande pagina, één dag voor de start van een groep | **nee** |
| Week 1: de NEWS-notatie en een variatieselector | Twee tekens en een zin | **nee** |
| Week 2: de omgeving, de bus, `adventure()`, `and`/`or` (#106) | Blokkades voor een groep die begon | **nee** |
| De onjuistheden in de colleges van week 2 (#111) | Zes feitelijke correcties | **nee** |
| Het logisimmateriaal weggehaald (25 MB) | Een gesloten besluit uitvoeren | **nee** |
| Achttien docstrings vertaald, `with open` in week 7 (#128) | Leek mechanisch | **nee**, wel door de orkestrator zelf nagelezen |
| `a.txt` teruggehaald (#113) | Eén ontbrekend bestand | **nee** |

### 1 september 2026, na het samenkomen met het werk van de tweede docent

| Werk | Waarom buiten de lus | Achteraf gelezen? |
|---|---|---|
| Vier issues bijgewerkt na PR #133/#135 | Vaststellen wat er achterhaald was | **nee** |
| README ingekort van 1039 naar 677 woorden | Redactie op een document buiten `source/` | **nee** |
| Het opbreken over drie niveaus vastgelegd (#138) | Een besluit van de vakdeskundige noteren | **nee** |
| De matrijsprocedure rechtgezet (#139) | Correctie op mijn eigen formulering | **nee** |
| A4 naar de PGM2-matrijs (#140) | Een voorstel uit de correctielijst uitvoeren | **nee** |
| Consistentiecontrole op issues en bord | Onderhoud, geen materiaal | **nee** |
| Werkitem #146 geschreven uit twee C6-oordelen | Bankwerk op andermans bevindingen, geen materiaal | n.v.t. — de bron *is* twee beoordelaars |
| Het leesvragenbesluit soortgebonden gemaakt (#150) | Een besluit van de vakdeskundige noteren | **nee** |
| Het poortbesluit van #146 vastgelegd (#152) | Vastlegplicht na C4 | **nee** |
| De body van #146 herschreven tot kaart | Leesbaarheid, geen materiaal | **nee** |
| De moet-lijst van C7 met de hand uitgevoerd | De auteur viel om op de maandlimiet | **nee** |
| #107 gesplitst in #167, #168 en #169 | Uitvoering van een triagebesluit | **nee** |
| Het poortbesluit van #167 vastgelegd | Vastlegplicht na C4 | **ja — stap 5b, BLOKKEER** |
| `uitgangspunten.md` opgeschoond van refactor-boekhouding | Verzoek van de vakdeskundige | **ja — stap 5b** |
| Het poortbesluit van #168 vastgelegd | Vastlegplicht na C4 | **ja — stap 5b** |
| Het leesvragenbesluit soortgebonden gemaakt (#150) | Een besluit van de vakdeskundige noteren | **nee** |
| Het poortbesluit vastgelegd in `curriculum/` en `conventies/` (#152) | Vastlegplicht na C4 | **nee** |
| De body van #146 herschreven tot kaart | Leesbaarheid, geen materiaal | **nee** |

**Zeventien ingrepen in totaal, nul beoordelaars.** Bij de eerste zeven leverden er
drie een reparatie op die een redacteur zou hebben gevangen (bevinding 4); bij deze
zes leverde de laatste er vier op, want de consistentiecontrole vond vier issues met
een achterhaalde bewering (bevinding 10).

**De laatste drie zijn wél gelezen**, en dat is het eerste gevolg van stap 5b uit
`/orc`: sinds die stap bestaat, gaat elke vastlegging in `curriculum/` of
`conventies/` langs een redacteur voordat de pull request wordt aangeboden. De
eerste keer leverde dat meteen `BLOKKEER` op met twee feitelijke fouten. Van
zeventien-op-nul naar drie-op-drie in één dag; of het houdt, is de volgende meting.

Dat de eerdere controle fouten vond is geen weerlegging van de regel maar de
bevestiging ervan: het gebeurde omdat er gekeken werd, en het was toeval dat er
gekeken werd. Dat is geen verwijt
achteraf maar de reden dat de regel er nu is - en deze tabel is de plek waar te
zien is of hij wordt nageleefd.

### 1 september 2026, rond werkitem #134

| Werk | Waarom buiten de lus | Achteraf gelezen? |
|---|---|---|
| PR #133: de mutatiegrens tussen PGM1 week 7 en PGM2 week 1 vastgelegd in `curriculum/` | Voorbereidend besluit van de vakdeskundige, vóór het werkitem bestond | **nee** |
| PR #135: `conventies/codeconventies.md` gelijkgetrokken met PR #133 | Gevonden tijdens de verkenning van #134, kleine correctie op een net genomen besluit | **nee** |
| PR #137: tuples van PGM2 week 1 naar PGM1 week 7 verplaatst in `curriculum/` | Besluit van de vakdeskundige, genomen bij de poort van #134 | **nee** |
| `curriculum/leerlijn.md` "Materiaal nu" voor PGM2 week 1 bijgewerkt (commit `6e953211`) | Gevonden door de redacteur-beoordelaar, per abuis niet in het eerste C7 opgenomen; zelf gerepareerd in plaats van terug de lus in gestuurd | **ja** — de tweede beoordelingsronde bevestigde de reparatie expliciet |

**Vier ingrepen, één gelezen.** De drie curriculum-PR's zijn besluiten van de
vakdeskundige die ík heb opgeschreven; niemand heeft ze nadien nog beoordeeld.
De vierde werd wél gelezen, maar alleen omdat de reparatie toevallig binnen de
looptijd van een beoordelingsronde viel die toch al liep - niet omdat er een
regel is die dat afdwingt voor werk buiten de lus. Zie bevinding 4.

### 1 september 2026, na afronding van #134 — issues #155 en #156

| Werk | Waarom buiten de lus | Achteraf gelezen? |
|---|---|---|
| `problems/6_basis.ipynb`: vooruitverwijzing naar dictionaries herformuleerd (PR #158) | XS-omvang, één zin in één bestand, per de proportionaliteitsregel geen werkitem voor de volle lus | **ja** — `rol-beoordelaar-redacteur` los ingezet, AKKOORD |
| `solutions/8_extra.ipynb` toegevoegd voor de sets-opgave (PR #159) | XS-omvang, één ontbrekende uitwerking naar bestaand patroon (`solutions/8_basis.ipynb`) | **ja** — `rol-beoordelaar-redacteur` los ingezet, AKKOORD; de rol had zelf geen shell, dus de poorten zijn door de orkestrator gedraaid vóór de PR openging |

Deze keer bewust wél gelezen, op verzoek gedaan in plaats van bij toeval - de
regel uit bevinding 4 toegepast in plaats van herhaald.

### 4 september 2026, week 2 op orde

| Werk | Waarom buiten de lus | Achteraf gelezen? |
|---|---|---|
| PR #176: spelling en aanhalingstekens in `solutions/2_rochambeau` en `2_basis` | XS-omvang, dertien regels redactie, per de proportionaliteitsregel geen werkitem | *nog niet* |
| PR #177: `2_sequenties_en_data` en `2_extra` omgezet van markdown-blok naar codecellen (#115) | Uitvoering van een doorlopend werkitem; mechanisch, geen ontwerp | **ja** — meegelezen in beide rondes hieronder |
| PR #177: `solutions/2_opstap.ipynb` geschreven, 1.789 woorden en 20 codecellen | Uitvoering van een gesloten besluit (`uitgangspunten.md` r764); nieuw materiaal, geen herziening | **ja** — twee rondes, en de tweede staat op BLOKKEER |

**Twee leesrondes over `2_opstap`, en beide keren convergentie.** De redacteur en de
eerstejaars zijn los van elkaar ingezet, zonder elkaars oordeel en zonder hun eigen
vorige oordeel.

| Ronde | Redacteur | Eerstejaars | Waarop zij samenkwamen |
|---|---|---|---|
| 1 | BLOKKEER | BLOKKEER | De tellingen in de inleiding en de slotalinea van *Debuggen* - drie luide fouten stonden er als twee, vijf punten als vier - en de omgekeerde bewering bij 3-G |
| 2, hertoets | AKKOORD MET PUNTJES | BLOKKEER | De debugsectie staat als markdown-blok terwijl `uitgangspunten.md` r774-776 een draaiende codecel voorschrijft |

**De hertoets vond wat de eerste ronde niet vond, en dat is het argument om er een te
draaien.** Ronde 1 ging over wat er stond, ronde 2 over de vorm waarin het stond.
Beide beoordelaars kwamen daar onafhankelijk op uit, met hetzelfde bewijs: de grond
"die code parseert niet" dekt drie van de zeven gevallen, want 3-B, 3-C, 3-E en 3-F
zijn geldige Python die uit zichzelf eindigt. `technische-conventies.md` r403-406 zegt
bovendien met zoveel woorden dat `skip-execution` niet in `solutions/` hoort, "want
daar is de uitvoering juist het bewijs dat de uitwerking werkt".

Dat de tweede ronde blokkeert op iets wat de eerste liet lopen, is geen strengheid die
oploopt. Het is een gevolg van het herstel zelf: ronde 1 repareerde tellingen met de
hand, en juist dat handwerk maakt zichtbaar dat niets in de repository die elf
getalsclaims narekent. Beide beoordelaars hebben ze opnieuw met de hand nagelopen en
ze kloppen alle vijf - maar dat handwerk is nog steeds de enige controle die er is.

**De blokkade is niet verwerkt maar doorgezet naar #169**, met beide zou-moeten-lijsten
erbij. Reden: de vormeis van r774-776 geldt voor alle 22 uitwerkingen en niet alleen
voor deze, en voor 3-A, 3-D en 3-G moet eerst gemeten worden of `raises-exception` een
`SyntaxError` bij het bouwen opvangt. Blijkt van niet, dan is dat volgens de
eerstejaars zelf een grond om het besluit voor te leggen, niet om er stil van af te
wijken. Wat hier zichtbaar hoort te blijven: **deze PR gaat dicht met een staande
blokkade**, en dat is een besluit van de vakdeskundige geweest, niet van de uitvoerder.

Twee dingen die de beoordelaars buiten deze oplevering vonden en die bij #169 horen:
`lectures/2b_strings_en_lists.ipynb` bevat 2-F t/m 2-I letterlijk, met `puntje` waar de
uitwerking `slice` schrijft en met precies de nummering 1, 2, 3, 6, 7, 4, 5 die in de
opgave nu is rechtgezet - de reparatie heeft die twee kopieën uit elkaar gedreven. En
de telling in `conventies/conventies.md` r73-75 ("11 van de 22 uitwerkingen staan als
markdown-blok") is niet hermeten terwijl er een uitwerking bij is gekomen.

**Wat het draaien opleverde dat lezen niet had opgeleverd.** De vier week
2-uitwerkingen zijn met de hand gedraaid omdat de build ze niet ziet. Dat leverde
vier zaken op in `2_rochambeau` die bij lezen niet opvallen: een zwevende string op
moduleniveau die zich voordoet als docstring, 74 seconden `time.sleep` verdeeld over
zeventien aanroepen, een hervraag die het tweede antwoord niet meer toetst, en
`# Uitbreiding Dummie proof` dat verwijst naar een uitbreiding die het practicum niet
kent - het practicum noemt RPS-5, RPS-25, RPS-101 en Blijven spelen. **Geen van deze
vier is gerepareerd**: ze raken de inhoud en horen bij #169. Wat wel is gerepareerd
zijn drie redactionele fouten die bij hetzelfde draaien opvielen (PR #176): een
spelfout, een paar scheve aanhalingstekens en `nested if`.

**Drie van mijn eigen metingen liepen eerst stuk, en alle drie op dezelfde manier:
een patroon dat nul gaf.** Losse codeblokken parsen meldde een `SyntaxError` die een
bewust fragment was; het blok zegt in zijn eigen commentaar dat het achter het vorige
hoort. Een zoektocht naar een puntje dat `'shoe'` oplevert gaf nul omdat ik alleen
positieve stapgroottes probeerde - met negatieve zijn er zestien. En een greep op
succescriteria in week 1 gaf nul terwijl ze er staan, in andere woorden. Alleen de
tweede is opgemerkt door te ijken; de andere twee doordat het antwoord ongeloofwaardig
was. Dat is de regel uit `CLAUDE.md` die zich drie keer op één dag bewees.

**Wat het schrijven van de uitwerking opleverde.** Alle antwoorden zijn gedraaid en
niet bedacht, en dat legde iets bloot dat de opgave zelf niet zegt: twee van de zeven
kapotte debugvoorbeelden (3-C en 3-F) geven bij de meegeleverde naam `"Hoebe"` het
júiste busnummer. Hun fout is bij die invoer onzichtbaar. De uitwerking noemt daarom
per geval een naam die de fout wél toont, en onderscheidt fouten die luid aflopen van
fouten die stil aflopen - hetzelfde onderscheid dat de ernstdrempel van de
beoordelaars gebruikt.

**Wat er niet is omgezet, en waarom dat geen omissie is.** `2_basis` en
`2_rochambeau` blijven markdown. Beide bestaan vrijwel geheel uit blokken met
`input()`; omgezet zouden die `skip-execution` dragen en levert de build nul
gecontroleerde cellen op. Bij `2_basis` komt daar een harde reden bij: het enige blok
zonder `input()` is de voortzetting van het eerste en leunt op `time` en `delay`
daaruit, dus overslaan van het eerste breekt het vijfde. Dat legt een blinde vlek van
`check-notebook-tags` bloot: de hook oordeelt per cel en kan niet zien dat een cel bij
een interactief programma hoort. **Elf van de achttien** blokken draaien nu mee: de
tien van `2_sequenties_en_data` en de ene van `2_extra`. De zeven die blijven liggen
zitten in `2_basis` (vijf) en `2_rochambeau` (twee).

### 10 september 2026, het visuele werk aan de interactieve cel

**Wat het was.** Zeven ingrepen aan `extensions/sphinx_interactive_code/` en één aan
`source/_static/custom.css`, na live gebruik door de vakdeskundige. Gemerged als
`d6baa34f` (PR #199).

**Waarom buiten de lus.** Dit is techniek en geen materiaal. De vakdeskundige heeft het
eerder zo afgebakend: *"mbt techniek (de integratie en flow/activeren op een pagina),
dat lijkt mij niet echt iets voor een lus maar wat jij en ik kunnen uitzoeken"*. Het
werd gestuurd door schermafbeeldingen: hij keek, meldde wat er niet klopte, ik mat waar
het vandaan kwam.

**Of er een beoordelaar overheen is gegaan.** Nee. Wel vier keer een visuele controle
door de vakdeskundige zelf, en één keer leidde die tot een terugdraaiing.

#### Wat het opleverde, en wat het leerde

Vier klachten, en **alle vier bleken hetzelfde patroon: wij tekenden iets wat het thema
al levert.**

| Klacht | Oorzaak | Ingreep |
|---|---|---|
| geflikker bij een tweede run | het uitvoervak werd vóór het draaien verborgen en daarna opnieuw gevuld | vorige uitvoer laten staan, alleen doven; regelhoogte reserveren |
| een streep onder de uitvoer | onze uitvoer stond *binnen* `div.cell_input`, dus hadden we een eigen kader nodig om het gebonden te laten lijken | uitvoer naar `div.cell_output` naast de invoer; eigen kader weg op notebookpagina's |
| een balk om de knop | een eigen achtergrond en `border-top`: een derde vlak in de cel | balk weg, knop los onder de code |
| wit blok in donkere modus | een eigen CodeMirror-thema dat wit schilderde, en acht hardgecodeerde kleuren | editor doorzichtig, kleuren uit CSS-variabelen die met het thema meedraaien |

**De reparatie was elke keer iets weghalen.** De CSS ging van 86 naar 104 regels, maar
het aantal kleuren dat wij zelf kiezen ging van acht naar één.

#### Twee dingen die alleen live te vinden waren

**De eerste poging om ons kader weg te halen mislukte**, en de melding was: *"de cel
staat nu los van de uitvoer."* Mijn analyse was dat de twee kaders hetzelfde deden en er
dus één weg kon. Fout: myst-nb's kader zegt *dit is een invoercel*, het onze bond editor,
knop en uitvoer tot één blok. Pas nadat de uitvoer naar `div.cell_output` was verhuisd -
waar het thema haar zelf aan de cel lijmt - kon dezelfde regel wél. **Dezelfde ingreep,
twee keer, met tegengesteld resultaat, en het verschil zat in de volgorde.**

**En de donkere modus legde een fout in het thema zelf bloot.** myst-nb rekent zijn
kleuren uit op `:root`, dus op `<html>`, met een schakelaar `:is(html, body)[data-theme]`.
Furo zet `data-theme` op `<body>`. Als die vlag omgaat is de kleur op `<html>` al
berekend, met alleen de `prefers-color-scheme`-stand. **Elke notebookcel op deze site
volgde dus het besturingssysteem in plaats van de knop in de zijbalk**, en niemand had
dat gemeld omdat het alleen opvalt als systeem en thema uit elkaar lopen. Gerepareerd in
`source/_static/custom.css`, voor alle cellen en niet alleen de onze.

#### Wat er onderweg is besloten

- **Geen forks.** Stock sphinx-thebe kan geen Pyodide - nagemeten in de bron: nul
  voorkomens van `lite`, `jupyterlite`, `pyodide` of `wasm`, en het laadt `thebe@0.8.2`
  voor een kernel via Binder. De enige route naar Pyodide is een fork van de TU Delft,
  van een git-URL, niet op PyPI. Onze eigen extensie is 691 regels en die houden we,
  **met een uitstapvoorwaarde: zodra stock sphinx-thebe lite-ondersteuning op PyPI heeft,
  opnieuw wegen.**
- **Wel leren van Thebe.** Zijn hele stylesheet telt drie regels voor de cel en tekent
  geen enkel kader; hij vervangt de inhoud ter plekke en laat het thema het uiterlijk
  dragen. Dat is de maatstaf waar deze ronde op uitkwam.
- **De CDN-versies staan vast.** De vijf CodeMirror-imports stonden op `@6`, wat bij elk
  paginabezoek opnieuw oplost naar de nieuwste 6.x. Een breaking change in een minor kon
  de editor bij een student breken **zonder dat er in de repo iets veranderde en zonder
  dat een build faalde om het te melden.** Nu vast tot op de patch, met de grond erbij.

### 11 september 2026, de vier registraties uit het C4 van #198

**Wat het was.** Vier besluiten van de poort vastgelegd in `curriculum/`: week 3 als
derde erkende afwijking op de bijeenkomstindeling, `zelfaanroep` uit de leerlijnkolom,
die kolom aangevuld met de vijftien begrippen die week 3 werkelijk introduceert, en het
gewicht van week 3 van 20% naar 30%.

**Waarom buiten de lus.** Het C2 belegde deze vier bij de auteur. De poort heeft ze
woordelijk vastgesteld, dus er zat geen oordeel meer in - het is registratie, en
`CLAUDE.md` zegt dat een besluit dat niet in `curriculum/` landt niet is genomen. De
auteursrondes van #178 kostten 254k, 298k, 331k en 374k; de weeklimiet stond op 88%.
**Vier vastleggingen laten wachten op een ronde die misschien halverwege afbreekt, is
het besluit zelf in gevaar brengen.** Dezelfde afweging als bij de clausule in
`begrippen.md` van 10 september.

**Of er een beoordelaar overheen is gegaan.** Nog niet. De auteur raakt `leerlijn.md`
en `uitgangspunten.md` in deze ronde niet meer, dus deze vier vallen buiten de diff die
de twee beoordelaars van #198 zien. **Ze horen apart gelezen te worden**, en dat staat
hier zodat het niet als gedekt telt.

**Wat de meting opleverde.** Eén van de vier was geen registratie maar een correctie:
`leerlijn.md` schreef *"P5 en A2, samen 20% van het tentamen"* terwijl de tabel drie
regels hoger P5, P6, P7 en A2 bij week 3 zet. P6 werd weggelaten. Nagemeten tegen
`leeruitkomsten.md`: 10 + 10 + 10 = 30%, met P7 zonder weging. **De dunste week van de
cursus draagt dus de helft meer dan het document over zichzelf zei.**

## Hoe je een meting noteert

Rol, ronde, tokens, duur, uitkomst in één regel. Bij een afgebroken run: wat er
bewaard is gebleven, want dat is het verschil tussen verlies en vertraging.

Zeg erbij wat de omvang was volgens triage, anders is een getal niet te
vergelijken met een volgende ronde.

## Werkitem #203 - procesaanpassing

Op 10 september 2026 zijn een gerichte analyse/ontwerp, één onafhankelijke
planbeoordeling (C3 AKKOORD) en een menselijk C4 AKKOORD uitgevoerd. De artefacten
staan op [#203](https://github.com/hanze-hbo-ict/programmeren/issues/203).
Codex toont hier geen tokenregistratie per rol; tokens en rolduur zijn niet
beschikbaar en worden niet geschat. De implementatie en onafhankelijke diffreview
worden bij oplevering hieronder aangevuld.

De gecontroleerde rijsommen, verschillen met historische samenvattingen en de
vooraf goedgekeurde proefafspraken staan in [203-proef.md](203-proef.md). De twee
praktijkproeven zijn nog niet gestart. Invoeringskosten horen apart van hun
kosten; afwezige meetgegevens betekenen geen besparing.

## #214 — Redactionele verantwoordelijkheid

Op 14 september 2026: kleine procesroute, uitvoering door Codex en onafhankelijke
redactionele beoordeling op GitHub. Geen boekbuild; toepasselijke pre-commit en
concrete scenario's in [214-redactie.md](214-redactie.md). Tokens en rolduur zijn
niet beschikbaar. Vermindering van menselijk redactiewerk is nog niet gemeten.

## Werkitem #237 — docentenhandleiding week 3

Volledige lus op een handleiding: ontwerper (met verkenning gecombineerd), poort, auteur, één
beoordelaar. Opgeleverd op 17 september 2026 in PR #245: `handleidingen/week_3.md` nieuw, 624
regels en 6.234 woorden, plus de `.docx`-regel in `curriculum/uitgangspunten.md`, twee verwijderde
`teacher_guides/`-bestanden, een bijgewerkte tally in de handleidingen van week 1 en 2 en één
kruisverwijzing in `source/lectures/3a_functies.ipynb`.

| Rol | Tokens | Duur | Uitkomst |
|---|---|---|---|
| curriculumontwerper, ronde 1 | 144.550 | 10 min 59 s | C2, zeven criteria, acht open vragen waarvan vier blokkerend |
| orkestrator, C1-correctie | niet beschikbaar | niet beschikbaar | drie eigen fouten hersteld vóór het ontwerpherstel |
| curriculumontwerper, ronde 2 | 172.449 | 4 min 30 s | drie blokschema's in plaats van de open vragen |
| auteur, ronde 1 | niet beschikbaar | niet beschikbaar | C5; geen meetregel in de kern op de PR |
| beoordelaar-onderwijskundige | 165.078 | 17 min 10 s | AKKOORD MET PUNTJES, 0 blokkades, 6 puntjes |
| orkestrator, vier puntjes | niet beschikbaar | niet beschikbaar | zelf hersteld, geen auteursronde |
| beoordelaar, naleesronde | 15.232 | 2 min 4 s | vier van vier akkoord |

**Eén ontwerpherstel gebruikt, van de één die is toegestaan, en het lag aan de orkestrator.** Het
C1 wees de ontwerper naar een deelkop in plaats van naar de moedersectie met de
bijeenkomstindeling, en noemde de sectie met open vragen het zwaarste deel van het werk. Het
ontwerp leverde daarop acht vragen waar voorstellen hoorden, waaronder één expliciete *"ik heb
hier geen voorstel"*. De correctie op C1 en het gerichte herstel kostten 172.449 tokens; dat is
de prijs van een onscherpe opdracht - meer dan het oorspronkelijke ontwerp kostte.

**Geen opleveringsherstel.** De beoordeling gaf nul blokkades. Vier van de zes puntjes waren
aanwijsbaar onjuist — twee onwaarheden in de tekst, één ontbrekende aantekening en een verouderde
telling in `curriculum/uitgangspunten.md` — en zijn door de orkestrator zelf rechtgezet in vier
zinnen in plaats van via een auteursronde. De beoordelaar las ze na (vier van vier akkoord,
15.232 tokens). Dat is de regel *wie het zelf doet, laat het lezen*, en hier kostte hij vijf
procent van een auteursronde.

**De rollen corrigeerden de orkestrator drie keer**, en alle drie de keren met een telling: 21
blokken in plaats van 24 (auteur én beoordelaar, onafhankelijk), twee uitwerkingen op 58
collegeopdrachten in plaats van één (auteur, nagemeten door de beoordelaar), en deelvraag **d**
in plaats van **c** bij Opdracht 2 van `3b` (auteur, stil rechtgezet). Zie de bevinding over het
criterium dat dwingt na te tellen.

**Wat er open bleef.** De bredere kruisverwijzingsregel uit het poortbesluit is nog nergens
vastgelegd en is dus niet genomen; de 33 collegeopdrachten zonder uitwerking staan bij #235 en
#95, net als de `.docx` van week 4 en de verwijzing daarnaar in `handleidingen/week_4.md`.

## Werkitem #256 — docentenhandleiding week 4 op de norm

De derde handleiding, en de eerste die een bestaande norm volgde in plaats van hem
uit te vinden. Opgeleverd op 21 september 2026 in PR #260: `handleidingen/week_4.md`
van 232 naar 684 regels, plus twee vastleggingen in `curriculum/uitgangspunten.md`
en drie rechtgezette verwijzingen in `handleidingen/week_3.md`.

| Rol | Tokens | Duur | Uitkomst |
|---|---|---|---|
| curriculumontwerper, ronde 1 | 164.519 | 15 min 10 s | C2; voorstel A over de bijeenkomstindeling, blokschema's met 22 blokrijen |
| curriculumontwerper, ronde 2 | 50.487 | 8 min 51 s | herstel na het poortbesluit; blokschema 2 en 3 opnieuw, 20 rijen, 0 B |
| auteur, ronde 1 | 280.463 | 18 min 11 s | C5; acht criteria zelf gemeten en gehaald |
| beoordelaar-onderwijskundige | 197.993 | 17 min 47 s | AKKOORD MET PUNTJES, 0 blokkades, 1 moet-punt, 4 puntjes |
| orkestrator, twee correctieronden | niet beschikbaar | niet beschikbaar | drie verouderde verwijzingen, daarna het moet-punt en drie puntjes |
| **totaal agents** | **693.462** | **circa 60 min** | |

Ter vergelijking: #237 (week 3) kwam op circa 497.000 met een auteur wiens tokens niet
beschikbaar waren. De twee zijn dus niet zuiver te vergelijken, maar de richting is
duidelijk: het volgen van een norm kostte hier **meer** dan het vaststellen ervan.
Dat is de aanleiding voor proef 1 van #203, vastgelegd in [203-proef.md](203-proef.md).

**Het poortbesluit veranderde het ontwerp, en dat was winst.** De ontwerper stelde voor
week 4 het patroon van week 3 te laten volgen: de oefenmidterm als werkcollege, CodingBat
in het practicum. Hij legde er eerlijk het tegensignaal bij — `practicals/4_python_bat.md`
noemt zichzelf een werkcollege — en redeneerde dat weg als een restant. De vakdeskundige
besliste andersom, op een grond die in geen enkel artefact stond: **de midterm wordt in
week 5 afgenomen, dus is het practicum van week 4 het oefenmoment.** Daarmee werd het
tegensignaal juist het bewijs, en verviel een van de twee open vragen.

**De nul die het vermelden waard is.** Onder die indeling hielden de vier overgeleverde
tijden uit `4_midterm.docx` geen stand: ze beschreven een klassikale cyclus met *geen
overleg*, en die past niet in een practicum. Week 4 is daarmee de eerste week met
**0 B en 20 R** - geen enkele tijd uit een bron. De beoordelaar heeft de drie `.docx`
zelf uit `3110b335^` gelezen en de afweging bevestigd, met één aanvulling die de
ontwerper zelf de zwakste bullet noemde: *"Start les (5 min)"* staat woordelijk boven
alle drie de documenten en is dus een huisvorm, geen meting van deze les.

**Wat de rollen aan de orkestrator corrigeerden.** De ontwerper: drie regelgetallen uit
C1 (620/625/232, niet 619/624/233). De auteur: twee fouten in het ontwerp - een uitwijk
die naar blok 7 wees terwijl het blok 6 is, en drie opdrachten die als `+=`, `-=` en `*=`
werden opgevoerd terwijl het alle drie `+=` is. De beoordelaar: dat de melding over
`week_3.md` onwaar was geworden door de reparatie zes regels verderop in dezelfde PR.

**Twee keer stond een agent in de verkeerde checkout.** De ontwerper ontdekte bij het
hervatten dat zijn shell in de hoofdcheckout stond, op een verlaten branch met drie
niet-vastgelegde bestanden. Hij heeft al zijn dragende metingen overgedaan tegen
`git show origin/master:<pad>` en kwam op dezelfde getallen uit, op één verfijning na.
Zie de bevinding daarover; bevinding 17 is hiermee voor de derde keer waargenomen.

## Werkitem #267 - compositie als begrip van PGM2 week 5

Kleine route zonder ontwerp: triage en C1 door de orkestrator, dan de mens (C4), de auteur en
één redacteur. Omvang S. Procesversie `e04d8dcf`. Dit is geen #203-proef, omdat er nog geen
proefissue gekozen was. Opgeleverd op 23 september 2026 in PR #278: `curriculum/leerlijn.md`,
`conventies/begrippen.md` en één rij in `curriculum/uitgangspunten.md`.

| Rol | Tokens | Duur | Uitkomst |
|---|---|---|---|
| auteur, oplevering | 92.213 | 3 min 11 s | C5; vier criteria, pre-commit groen |
| beoordelaar-redacteur | 43.248 | 1 min 55 s | AKKOORD MET PUNTJES, 0 blokkades, 3 puntjes |
| auteur, hervat voor de puntjes | 108.512 | 1 min 47 s | herstelbijlage; niet vastgesteld of dit getal de eerste run meetelt |
| beoordelaar-redacteur, vers, herstelmodus | 42.777 | 1 min 32 s | AKKOORD MET PUNTJES, 1 smaakpuntje |
| orkestrator | niet beschikbaar | niet beschikbaar | C1, C4, C4-aanvulling, correctie, PR |
| **totaal agents** | **286.750 of minder** | **circa 8 min** | herstelstand ontwerp 0, oplevering 0 |

Puntjes kostten geen ronde. De mens besliste twee keer: eerst over de drie open vragen uit
C0 en de reden, daarna over de registerrij (aard en status).

**Wat de beoordelaar aan de orkestrator corrigeerde.** De herstel-C6 liet zien dat de
onderbouwing in de C4-aanvulling ("zo gaat het ook bij de andere gesloten didactische
rijen") maar half klopte. Die zin had de orkestrator zelf geschreven. Zie de bevinding van
dezelfde datum.

## Werkitem #273 — college PGM2 week 1 gesplitst, met opdrachten

Route *overzichtelijke opgave of sectie*, omvang M, procescommit `e04d8dcf`, geen #203-proef.
Opgeleverd op 23 september 2026 in PR #279: `8a_datastructuren` ingekort en van drie opdrachten
voorzien, `8b_taalmodel` nieuw met vijf, `course/week_8.md` uitgeschreven, en twee regels in
`curriculum/` (leerlijn r165, uitgangspunten, statusregel weekpagina).

| Rol | Tokens | Duur | Uitkomst |
|---|---|---|---|
| curriculumontwerper (gecombineerd) | 113.950 | 8 min 26 s | C2, grens A aanbevolen, vier open vragen |
| orkestrator, C1, C4 en C4-aanvulling | niet beschikbaar | niet beschikbaar | mens koos grens B; C4 formuleerde de volgorde van 8b onnauwkeurig |
| auteur, oplevering | 179.339 | 11 min 12 s | C5, alle controles groen |
| auteur, volgorde 8b (hervat) | niet vastgesteld; harness meldt 220.224 | 4 min 58 s | volgorde E, D, F, G |
| beoordelaar-eerstejaars | 78.192 | 4 min 36 s | AKKOORD MET PUNTJES, 0 blokkades, 5 puntjes |
| beoordelaar-onderwijskundige | 80.715 | 4 min 42 s | AKKOORD MET PUNTJES, 0 blokkades, 3 puntjes |
| auteur, puntjes (hervat) | niet vastgesteld; harness meldt 244.873 | 4 min 38 s | 8 puntjes verwerkt |
| beoordelaar-onderwijskundige, naleesronde | 41.839 | 2 min 20 s | AKKOORD, 8/8 opgelost |
| **vastgesteld totaal agents** | **494.035** | | exclusief de twee hervatte auteursstappen |

Herstelstand bij afsluiting: ontwerp 0/1, oplevering 0/1. Zie de bevinding over hervatte agents
voor waarom de twee auteursgetallen niet zijn opgeteld.

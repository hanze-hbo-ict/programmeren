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

## Hoe je een meting noteert

Rol, ronde, tokens, duur, uitkomst in één regel. Bij een afgebroken run: wat er
bewaard is gebleven, want dat is het verschil tussen verlies en vertraging.

Zeg erbij wat de omvang was volgens triage, anders is een getal niet te
vergelijken met een volgende ronde.

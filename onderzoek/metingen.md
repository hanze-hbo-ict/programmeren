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

## Werk buiten de lus om

Hier hoort wat met de hand is gedaan omdat het te klein leek voor een werkitem.
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
| Het poortbesluit vastgelegd in `curriculum/` en `conventies/` (#152) | Vastlegplicht na C4 | **nee** |
| De body van #146 herschreven tot kaart | Leesbaarheid, geen materiaal | **nee** |

**Zeventien ingrepen in totaal, nul beoordelaars.** Bij de eerste zeven leverden er
drie een reparatie op die een redacteur zou hebben gevangen (bevinding 4); bij deze
zes leverde de laatste er vier op, want de consistentiecontrole vond vier issues met
een achterhaalde bewering (bevinding 10).

Dat de controle die fouten vond is geen weerlegging van de regel maar de
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

## Hoe je een meting noteert

Rol, ronde, tokens, duur, uitkomst in één regel. Bij een afgebroken run: wat er
bewaard is gebleven, want dat is het verschil tussen verlies en vertraging.

Zeg erbij wat de omvang was volgens triage, anders is een getal niet te
vergelijken met een volgende ronde.

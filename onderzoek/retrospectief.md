# Retrospectief: de rollenlus, augustus tot oktober 2026

*Geschreven door de onderzoekersrol op 20 oktober 2026, op verzoek van de vakdeskundige.
Dit is een verslag over de werkwijze, geen onderwijsmateriaal. Het hoort niet in `source/`,
niet in `_toc.yml` en niet in de Sphinx-build.*

## Samenvatting

Deze repository bevat het materiaal voor twee programmeervakken. Sinds augustus 2026 wordt
dat materiaal herzien met een **rollenlus**: taalmodellen die het werk niet alleen uitvoeren
maar ook onder elkaar verdelen, elk in een eigen context, met een mens bij de poort en bij de
merge. De vraag die eronder ligt staat in `onderzoek/README.md` §*De vraag*: levert verdelen
over rollen met een geïsoleerde context beter werk op dan één agent die alles doet, en tegen
welke prijs? Alles wat over die vraag is opgeschreven staat in `onderzoek/`: 6.178 regels in
vijf bestanden, met ruim vijftig bevindingen en zevenenveertig gemeten routes.

Wat eruit komt, is tweeledig. De lus vangt aantoonbaar fouten die geen enkele mechanische
poort vangt, en zij doet dat herhaalbaar: een verse lezer met een smalle opdracht vindt
werkelijke defecten in tekst die de poorten al groen had gekregen. Daar staat bewijs onder dat
telbaar is. Maar de hypothese zoals `README.md` haar stelt is met dit corpus **niet te
toetsen**: er is geen enkele route waarin één agent alles deed, dus er is niets om tegen te
vergelijken. En de kosten lopen zo uiteen (van 86.147 tot 2.972.571 tokens per route) en de
werkwijze is zo vaak bijgesteld (zestien verschillende procesversies over zeventien routes die
er een noemen) dat geen enkel gemiddelde iets betekent.

Het antwoord op de vraag die de vakdeskundige erachter stelde, of de administratie haar prijs
verdient, is **deels**. Er is genoeg vastgelegd om een retrospectief te dragen; dit document
is daarvan het bewijs, en het rust op metingen en niet op herinnering. Maar de administratie
is in haar huidige vorm te duur op de verkeerde plek. De leesronden op zes registraties
kostten samen ten minste 1.434.050 tokens, en de registratie van één werkitem (#377) kostte in
leesronden meer dan dat hele werkitem #386 aan agentwerk kostte. Die leesronden vonden
werkelijke fouten, maar vrijwel alle in de **verhalende** beweringen van de registratie, niet
in de meettabellen. En het opschrijven zelf borgt niets: twee van dertien roldefinities
verwijzen naar `onderzoek/`, twintig plaatsen in `bevindingen.md` zeggen dat er niets of
slechts deels iets veranderde, zeventien voorstellen wachten op een evaluatie van #203 die
niet is uitgevoerd, en drie bevindingen noemen een gevolg dat niet in de instructies staat.

De scherpste maat is de maat die het dossier zelf voorstelt: gebeurt het daarna nog een keer?
Voor de meetfout bij een hervatte agent is het antwoord vier keer ja, na drie bevindingen.
Voor de verouderde lokale `master` twee keer ja. Voor de gedeelde scratchpad drie keer ja. In
geen van die drie gevallen is de maatregel ooit in een instructie geland.

## Hoe dit stuk te lezen

Wie de werkwijze zelf wil begrijpen, leest eerst
[`rollen/rollen.md`](../rollen/rollen.md); dat herhaal ik hier niet. De paar alinea's
hieronder geven alleen wat je nodig hebt om de beoordeling te kunnen volgen.

Alle regelnummers verwijzen naar de werkboom op de branch `registratie-386`, kop `1f595e4b`.
Die branch is **nog niet gemerged**. Zij bevat de ingang van werkitem #386 in `metingen.md`
en drie bevindingen van 20 oktober 2026; waar ik die gebruik, staat het erbij.

Waar een bewering op één waarneming rust, staat dat erbij. Dat is de huisregel uit
`onderzoek/README.md`, en zij geldt ook voor dit document.

## 1. Wat de lus is

Een werkitem is een GitHub-issue (`CLAUDE.md` §*Wijzig materiaal niet uit de losse hand*).
Een mens schrijft dat issue; dat is het C0. Daarna loopt er een route langs genummerde
overdrachten, en tussen twee rollen gaat precies één artefact: C1 is het routebesluit, C1b een
meting, C2 een ontwerp, C3 de toets op dat ontwerp, C4 het besluit van de mens bij de poort,
C5 de oplevering van de auteur, C6 het oordeel van een onafhankelijke beoordelaar en C7 de
samenvoeging van meerdere oordelen. De contracten staan in
`.claude/agent-role-loop/core/contracts/`, de rollen in `core/roles/`, de gedeelde routenorm
in `core/loop.md`.

De rollen zijn aparte agents met een eigen, verse context. `loop.md` r98-103 eist dat
uitdrukkelijk: *"Iedere onafhankelijke beoordeling begint in een verse context. Geen
maaktranscript, geen afwegingen uit het uitgebreide C5 en bij de eerste beoordeling geen
andere oordelen."* Er zijn dertien roldefinities in `core/roles/`. Een daarvan, de
eerstejaars, mag de uitwerkingen van de opgaven niet zien, zodat hij vastloopt waar een
student vastloopt (`loop.md` r57-58).

Eén actor valt buiten die opzet: de **orkestrator**, die de route draait, de artefacten
doorgeeft, de besluiten van de mens vastlegt en de metingen bijhoudt. Hij heeft geen
roldefinitie in `core/roles/`; zijn instructie is het commando
`.claude/commands/orc.md`, 107 regels. Dat is geen detail, zoals §5 laat zien.

Niet elk werk gaat door de lus. `CLAUDE.md` §*Wijzig materiaal niet uit de losse hand* zegt
dat proportionaliteit vóór volledigheid gaat: een typefout zet je gewoon recht. Dat werk heet
in de administratie *Werk buiten de lus om*, en voor dat geval geldt de regel *wie het zelf
doet, laat het lezen*.

De werkwijze is sinds 10 september 2026 zelf onderwerp van een goedgekeurd
procesexperiment, #203, met als doel dertig procent minder tokens per route. De afspraken en de twee uitgevoerde
proeven staan in `onderzoek/203-proef.md`. Het afsluitende besluit van dat experiment is nog
niet genomen; `203-proef.md` r16-18 noemt de proeven en het evaluatiebesluit nog openstaand,
terwijl r93 en r154 van datzelfde bestand hun uitkomsten al dragen.

## 2. Wat dit corpus kan dragen en wat niet

`onderzoek/README.md` §*Wat dit geen experiment maakt in de strikte zin* zegt het zelf: *"Er
is geen controlegroep en er zijn geen herhalingen."* Dat is juist, en het is niet het enige.
Ik heb de vier grenzen uit mijn opdracht nagemeten en er drie aan toegevoegd.

### De noemer is nooit vastgelegd

`metingen.md` draagt **47** koppen `## Werkitem` (geteld met een patroon op `^## Werkitem`).
Op GitHub stonden op 20 oktober 2026 **129** gesloten werkitems en 30 open; dat getal is mij
door de orkestrator aangeleverd en ik kan het zonder shell niet zelf nameten. De meting die
daarvoor nodig is, is een telling van gesloten issues met het werkitemlabel op die datum.

Neem je die 129 aan, dan hebben ten minste 82 gesloten werkitems geen ingang, en dat is een
ondergrens: onder de 47 ingangen zitten ook #203 en #214, die procesaanpassingen zijn,
en #107, dat bij de triage is afgewezen. Welke werkitems een ingang kregen is nergens vooraf
vastgelegd. Daarmee kan dit corpus **geen enkele uitspraak van de vorm "x procent van de
routes doet y"** dragen. Wat het kan dragen is: dit is gebeurd, zo vaak, hier gemeten.

De selectie loopt bovendien aantoonbaar naar het interessante geval. `README.md` §*Hoe je
hieraan bijdraagt* zegt dat je een bevinding noteert *"zodra iets misgaat"*. Een route die
zonder incident afliep, levert dus een tabel op en geen tekst, en soms niets.

### De orkestratiekosten ontbreken, en dat is de grootste post

`metingen.md` r3-5 zegt het bij de opening: de getallen *"omvatten de rol zelf, niet het
orkestreren eromheen"*. Bij de twee duurste recente routes staat die regel ook letterlijk als
`niet beschikbaar`: #377 (`metingen.md` r3302 en r3322) en #386 (r3603). Over het hele bestand
staat **55** keer *niet beschikbaar*.

Dat is geen kleine marge. De orkestrator schrijft C1, zeven C4's, twee C7's, de pull request
en de rectificaties (#377, r3302), en hij is de actor aan wie de meeste bevindingen worden
toegeschreven. Van de kosten van die arbeid is niets bekend. Elke vergelijking in dit corpus
vergelijkt dus agentwerk met agentwerk en laat de duurste onbekende buiten beeld. Voor #203 is
dat expliciet geregeld (`203-proef.md` r208-213: orkestratie apart rapporteren, bij
vergelijking alleen meenemen als beide zijden haar bevatten), maar het blijft een gat in de
noemer en geen oplossing ervan.

### De procesversies maken stratificatie onmogelijk

Mijn opdracht vroeg de kosten te stratificeren naar procesversie, omdat elke ingang haar
startcommit noemt. Dat gaat niet. Ik heb de ingangen geteld die een procesversie noemen:
**zeventien**, en zij dragen **zestien verschillende** commits. Alleen `17e790e3` komt twee
keer voor (#377 op `metingen.md` r3291 en #382 op r3450). De overige vijftien stratums hebben
elk één route.

Dertig van de zevenenveertig ingangen noemen in het geheel geen procesversie. De oudste routes
(#103, #134, #146, #178) liggen vóór de invoering van die registratie; `loop.md` r13 eist haar
nu: *"Registreer bij iedere nieuwe C1 de gebruikte commit."*

Het gevolg is hard: er is geen enkel paar routes in dit corpus dat dezelfde soort werk onder
dezelfde procesversie deed. De twee #203-proeven zijn hier het eerlijkst over.
`203-proef.md` r86-89 zegt bij proef 1 dat zij twee werkitems vergelijkt en geen twee methoden,
en r149 zegt bij proef 2 dat de referentie #160 al onder de #203-lus draaide, dus dat de proef
een route met en zonder aparte verkenner vergelijkt en niet het oude proces met het nieuwe.

### Er is geen controlegroep, en de hypothese noemt er een

Dit is de scherpste grens, en `README.md` dekt hem niet af. De vraag in `README.md` r14-15
luidt of verdelen over rollen *"beter werk oplevert dan één agent die alles doet"*. In het hele
corpus staat **geen enkele route waarin één agent alles deed**. Er is dus geen enkele
waarneming aan de kant waartegen de hypothese zich afzet.

Wat er wel is, is een zwakkere maar toetsbare variant, en die draagt wel bewijs: *een verse
lezer met een smalle opdracht vindt werkelijke defecten in tekst die de poorten al groen
hadden*. Zie §5.

### Drie grenzen die ik eraan toevoeg

**De tellingen in het dossier zijn niet stabiel.** De vier getallen die mij voor dit stuk zijn
aangeleverd, wijken alle vier één of twee af van wat ik op de branchkop meet: 46 tegen mijn 47
ingangen `## Werkitem`, 52 tegen mijn 57 koppen in `bevindingen.md` (waarvan twee geen
bevinding zijn: *Open: welk model per rol* op r894, uitdrukkelijk *"Nog niet onderzocht"*, en
*Vervolg op de procesbevindingen: #203* op r922), 53 tegen mijn 55 keer *niet beschikbaar*, en
zes tegen mijn zeven regels met *"voor de derde keer"* of *"voor de vierde keer"*. Elk verschil
is precies de inhoud van de laatste commit op deze branch, `1f595e4b`, die de ingang van #386
en de drie bevindingen van 20 oktober toevoegde. De aangeleverde getallen zijn dus gemeten op
een stand die inmiddels één commit oud was. Dat is geen slordigheid van wie ze mat, het is de
bevinding *De orkestrator meet tegen een stilstaande lokale master*
(`bevindingen.md` r1680) in haar mildste vorm, en het is de reden dat elk getal in dit stuk
zijn commit draagt. Wat de telling zou sluiten: `git diff --stat 6c8ea078..1f595e4b --
onderzoek/`. Dat kan ik zonder shell niet draaien.

**Het dossier heeft geen eenduidige eenheid.** `bevindingen.md` nummert de eerste achttien
bevindingen en de rest niet. De nummers `## 9.` en `## 14.` staan elk twee keer, boven vier
verschillende bevindingen (r320 en r938; r550 en r600). Dat is op 1 oktober 2026 door de
vorige onderzoeksronde vastgesteld (`metingen.md` r2621-2622) en staat er negentien dagen
later nog. Sommige bevindingen dragen onder een `###` een tweede en derde voorval met een
eigen datum (bevinding 7 op r212 en r246, bevinding 17 op r827). Een eenduidig aantal
bevindingen bestaat dus niet; welk getal je noemt, hangt af van een telregel die het bestand
zelf niet geeft.

**De uitvoer van de vorige onderzoeksronde staat niet in `onderzoek/`.** En hier moet ik iets
rechtzetten dat in mijn eigen opdracht stond. Mij is meegedeeld dat deze rol nog nooit had
gedraaid. Dat is onjuist. `metingen.md` r2581-2587 registreert een onderzoeksronde van 1
oktober 2026, met de regel *"Eerste keer dat deze rol draaide"*: 183.955 tokens, 11 min 44 s,
tien bevindingen, drie aanbevelingen. Dit is dus de tweede ronde. Het rapport zelf staat
volgens die ingang op issue #203 en niet in `onderzoek/`, en zonder shell of GitHub kan ik het
niet lezen. Van de drie aanbevelingen van die ronde is er één in het dossier terug te vinden
(het dossier rechtzetten voordat er een nieuwe maatregel op wordt gebouwd, `metingen.md`
r746-748) en één in afwijkende vorm (het hernummeren als registratiewerk langs een rol,
r2628-2630). De derde heb ik niet kunnen vaststellen. Daarmee kan ik mijn kerntaak, *kwam het
daarna nog een keer voor*, voor de vorige ronde maar gedeeltelijk uitvoeren: ik ken haar
conclusies alleen uit de samenvatting die de orkestrator van haar maakte. Diezelfde meting
staat bovendien twee keer in `metingen.md`, op r765 en op r2585, met verschillende
omschrijvingen.

### Wat het corpus wel draagt

Gevalsbeschrijving, en goede. Van zevenenveertig routes staat per rol wat zij kostte, hoe lang
zij duurde en wat haar uitkomst was. Bij de meeste staat erbij wat de route openliet. De
bevindingen dragen hun bewijs, hun vindplaats en hun gevolg, en waar het gevolg uitbleef staat
dat er. Dat is zeldzaam genoeg om te benoemen: dit dossier schrijft zijn mislukkingen op, en
in meer dan één geval de mislukking van het opschrijven zelf (`bevindingen.md` r1262, *Een
bevinding opschrijven voorkomt haar niet*).

## 3. Welke bevindingen landden, en welke keerden terug

Dit is de kern van mijn opdracht. Een bevinding die is opgeschreven en niet uitgevoerd is
erger dan een die er niet staat, want zij wekt de indruk dat het is opgelost
(`core/roles/onderzoeker.md` r48-50). Ik heb per bevinding gezocht of het gevolg in de
instructies staat: `.claude/agent-role-loop/core/`, `.claude/commands/orc.md`, `CLAUDE.md`,
`curriculum/` en `conventies/`. Alles hieronder is gemeten op de branchkop `1f595e4b`.

### Wat werkelijk is geland

| Bevinding | Gevolg | Staat het er? |
|---|---|---|
| 1, ernstdrempel verhelderaar (r10) | drempel in rol en C3 | **ja**, `roles/verhelderaar.md` §*De ernstdrempel* r33 en r53, `contracts/C3-verhelderingsresultaat.md` r12 |
| 2, stille meetfouten (r44) | ijk elk patroon vóór je nul gelooft | **ja**, `loop.md` r137-138 en `CLAUDE.md` §*Meten* |
| 3, leesronde op ongelezen materiaal (r77) | leesronde als eigen modus | **ja**, `contracts/C6-beoordeling.md` r9 en §*Leesronde* r51 |
| 7, kennis buiten de repo (r195) | het besluit zelf vastleggen | **ja**, `curriculum/uitgangspunten.md` §*Leesvragen mogen fout aflopen* r954, met een registerrij op r376 |
| 13, besluit van gevallen naar soort (r501) | hetzelfde besluit soortgebonden | **ja**, zelfde vindplaats |
| 9 (tweede), titelhiërarchie buiten de build (r938) | controle van gerenderde TOC en koppen | **ja**, volgens de bevinding in de technische conventie en bij de eerstejaars |

De beste maat voor landing staat bij bevinding 14 op r659-664, en zij is niet "het staat
opgeschreven" maar "het bereikte de rol op het moment dat zij handelde". Het besluit
*Leesvragen mogen fout aflopen* werd van gevallen naar soort herschreven, in
`curriculum/uitgangspunten.md` gezet en in de opdracht van elke rol geplakt. Resultaat:
drie van de drie beoordelaars daarvóór meldden het als defect, nul van de vier daarna. Dat is
het enige geval in dit corpus waarin een maatregel een meetbaar, telbaar effect op het aantal
valse meldingen heeft gehad.

### Wat een gevolg noemt dat er niet staat

Dit is de ernstigste categorie, en zij is groter dan ik verwachtte.

**Bevinding 4** (r113) zegt onder *Wat het veranderde*: de regel *wie het zelf doet, laat het
lezen*, *"in `roles/triage.md` en in `/orc`"*. Die spreuk komt in de hele map `.claude/`
**nul** keer voor; ik heb erop gezocht met een patroon op `laat het lezen` en op `zelf doet`,
beide zonder treffer, en de ijking is de ene treffer in `CLAUDE.md`
§*Noteer wat de werkwijze leert*, die mijn patroon wel vindt. De plicht bestaat daar in andere
woorden: `loop.md` §*Buiten een werkitem* r166-167 eist bij een kleine correctie *"een
onafhankelijke lezer"*, en `loop.md` §*GitHub en registratie* r156-158 eist een onafhankelijke
redactionele beoordeling op besluittekst van de orkestrator. Bevinding 14 heeft dat op
r642-651 zelf vastgesteld en toegegeven. Maar de onjuiste vindplaats in bevinding 4 staat er
nog, zeven weken later, en de twee bevindingen spreken elkaar nu in hetzelfde bestand tegen.

**Bevinding 17** (r791) is het scherpste geval. Zij noemt onder *Wat het veranderde* twee
maatregelen: boomexclusiviteit voor een agent die in de werkboom schrijft, en *"een rol die
commit, controleert aan het eind zijn eigen diff tegen de basiscommit die hij bij de start
noteerde"*. Van de tweede schrijft de bevinding zelf: *"Dat is wat het hier ving, en het is de
enige controle die werkte."* Zij ving het vervolgens nog een keer, op 2 oktober bij #351
(r827-845). Geen van beide maatregelen staat in een instructie. Ik heb gezocht op
`basiscommit`, `eigen diff`, `worktree` en `scratchpad` in `.claude/`: nul treffers in enig
instructiebestand. De enige controle die in dit corpus twee keer aantoonbaar iets ving, staat
nergens waar een rol haar leest.

**Bevinding 1** is half geland. De ernstdrempel staat er (zie boven), maar de tweede helft,
dat `loop.md` het optimaliseer-tegen-de-criticus-patroon benoemt, staat er niet: nul treffers
op `optimaliseer` en op `criticus` in heel `core/`.

**Bevinding 2** is inhoudelijk geland maar haar vindplaats niet. Zij noemt een sectie
*Gereedschap: gebruik wat er is* in `loop.md`. Die sectie bestaat niet; de inhoud leeft voort
in één zin, `loop.md` r136-138.

**Stap 5b** is het bekendste geval en staat al twee keer in het dossier opgetekend
(`metingen.md` r1354-1355 en r2610-2611). De maatregel bij bevinding 14 was een genummerde
stap in `/orc`; bij de herschrijving van #203 is zij proza geworden. Ik heb het nagemeten: nul
treffers op `5b` in `orc.md`; wat er staat is r61-63, *"Een door jou geschreven besluitdiff
laat je onafhankelijk redactioneel toetsen tegen het C4 vóór de PR ter merge wordt
aangeboden."* Bevinding 14 noemt juist dat terugzetten naar proza haar zwakte, omdat *"een
losse stap wordt overgeslagen omdat het werk dan al af voelt"* (r666-671).

### Een tegenspraak tussen twee instructiebestanden

Bij diezelfde maatregel vond ik iets dat in geen enkele bevinding staat. De bevinding van
9 oktober (`bevindingen.md` r2051, *De orkestrator schreef in een C4 een clausule die de mens
niet had genomen*) stelt vast dat de toets tegen het C4 het verkeerde artefact toetst, omdat
de clausule in het C4 zelf stond, en stelt op r2094-2096 voor: toets tegen het menselijke
besluit **én** het C4.

Dat voorstel staat nu wel in `loop.md` r156-158 (*"onafhankelijke redactionele beoordeling op
de diff en het menselijke bronbesluit"*) en niet in `orc.md` r61-63, dat alleen het C4 noemt.
De twee bestanden geven de orkestrator dus verschillende opdrachten voor dezelfde handeling,
en `orc.md` is het bestand dat hij bij de start leest. Wanneer die zin in `loop.md` is gekomen
en of dat het gevolg van deze bevinding is, kan ik niet vaststellen; dat vraagt `git log -S`
op `loop.md`, en ik heb geen shell.

### Wat terugkeerde, met de maatregel al op papier

Dit is de toets die `core/roles/onderzoeker.md` r51-53 de scherpste noemt. Ik heb gezocht op
*"voor de derde keer"* en *"voor de vierde keer"* en vond **zeven** regels, niet zes:
r1550, r1803, r2132, r2159, r2180, r2181 en r2223. Drie daarvan (r2132, r2181, r2223) zijn
aanhalingen van één en dezelfde kop en geen eigen herhaling. De zeven regels dekken dus
**twee** families, niet zes losse gevallen. Dat onderscheid doet ertoe: het dossier lijkt bij
oppervlakkig lezen zes verschillende dingen te noemen die drie of vier keer misgingen, en het
zijn er twee die ver zijn doorgelopen.

| Patroon | Keren | Vindplaatsen | Maatregel in de instructies? |
|---|---:|---|---|
| Hervatte agent: telling van zijn tokens | 4 | r1193 (#273, 23 sep), r1464 (#326, 30 sep), r1803 (#335, 2 okt), r2159 (#382, 19 okt) | **nee** |
| De auteur schrijft een reden bij het besluit | 4 | r1397 (#271, twee keer), r1442 (#326), r1550 (#332) | **nee**, voorstel open in #331 |
| Blind zoekpatroon | 4 | r1348 (#270), r1502 (#328), r1765 (#102 en #351), r2004 (#377) | gedeeltelijk: de ijkregel staat er, de aanvullingen niet |
| Verouderde lokale `master` | 2 | r1680 (#102, #341), r1832 (#335) | **nee**, nul treffers op `fetch` in de instructies |
| Gedeelde scratchpad tussen rollen | 3 | r1725 (#102, twee rollen), r1757 (#381, 19 okt) | **nee** |
| Werk buiten de lus zonder lezer | doorlopend | r113, r320, `metingen.md` r1334 | regel in `CLAUDE.md`, niet in `.claude/` |

De hervatte agent is het zuiverste geval dat dit corpus bezit, en de moeite waard om uit te
schrijven. Op 23 september wordt vastgelegd dat de verbruiksmelding van een hervatte agent
vermoedelijk een lopend totaal is en dat optellen de eerste oplevering dubbel rekent (r1193).
Op 30 september gebeurt het opnieuw, en de bevinding daarover stelt vast dat de praktijk in
`metingen.md` al sinds #271 met het verschil rekent (r1464). Op 2 oktober gebeurt het voor de
derde keer, en nu met gevolg: de hoge lezing werd gebruikt als onderbouwing van de conclusie
dat hervatten duur is, en die conclusie was bijna als bevinding vastgelegd (r1803-1819). Op
19 oktober telt de orkestrator bij #382 opnieuw twee meldingen op en meldt 712.361 op een pull
request, vóór de merge (r2178-2184). Die bevinding zegt waar het aan ligt: *"Daar staat de
praktijk, en niet in `/orc`, waar de meetregel wordt geschreven."*

Ik heb dat nagemeten. `orc.md` §*Rondes, budget en metingen* r102-103 zegt: *"Sluit elk
gepubliceerd artefact af met rol, ronde, tokens, duur, omvang en uitkomst. Niet beschikbaar is
geen nul."* Over een hervatte agent staat er niets, en in `loop.md` r148-150 evenmin. Vier
keer dezelfde fout, drie bevindingen, één zin die nooit is geschreven.

### De maat die het dossier zelf aanlegt

Ik heb geteld hoe vaak een bevinding haar eigen gevolg als uitgebleven of onvolledig
beschrijft: **twintig** regels in `bevindingen.md` matchen op *"in de instructies is niets
veranderd"*, *"nog niet opgelost"*, *"deels opgelost"*, *"nog niets"* of *"nog niet bewezen"*.
En **zeventien** regels dragen een voorstelmarkering (*Voorstel voor*, *Voorstel, niet
beslist*, *voorstel naar de volgende procesronde*). Het werkelijke aantal voorstelpunten is
hoger, want sommige bevindingen voeren onder één inleidende regel twee voorstellen op
(r2232, r2188); een exact aantal vraagt een telregel die het bestand niet geeft.

De vorige onderzoeksronde kwam op 1 oktober uit op *"zestien voorstelpunten die wachten op de
evaluatie van #203 - en die evaluatie is zelf niet uitgevoerd"* (`metingen.md` r2605-2607).
Negentien dagen later is dat aantal gegroeid en is de evaluatie nog niet uitgevoerd.
`203-proef.md` r238 eist haar *"uiterlijk twee weken na de tweede proefoplevering"*; die
oplevering was 24 september 2026 (r154).

Hier zit het mechanisme dat dit alles bij elkaar houdt, en het is zelf gemeten. Bevinding 14
stelt op r653-657: van alle roldefinities verwijzen alleen `vakdeskundige.md` en
`onderzoeker.md` naar `onderzoek/`, dus *"voor een auteur of beoordelaar bestaat dit document
niet"*. Ik heb het hermeten op de branchkop: de map `core/roles/` bevat dertien definities en
precies die twee noemen `onderzoek/`. Een bevinding in dit dossier bereikt dus per constructie
geen enkele uitvoerende rol. Dat is geen falen van de rollen; het is de inrichting.

## 4. Wat een route kost, en wat de administratie kost

### De spreiding is te groot voor een gemiddelde

`onderzoek/metingen.md` geeft **34** regels met een totaal voor de agents. De uitersten liggen
ruim dertig keer uiteen: #294, drie zinnen over duck typing, kostte 86.147 (r2008); #178, één
stelsel voor de opgaveniveaus, kostte 2.972.571 (`203-proef.md` r263). Een greep uit de
tabellen, alle met hun vindplaats in `metingen.md`:

| Route | Soort werk | Agenttokens |
|---|---|---:|
| #294 (r2008) | drie zinnen | 86.147 |
| #328 (r2410) | comprehensions eruit, XS | 108.039 |
| #336 (r2441) | twee puntjes, XS | 127.359 |
| #386 (r3607, branch) | één `try` eruit, XS | 335.795 |
| #280 (r1823) | handleiding week 6, korte route | 470.035 |
| #256 (r1696) | handleiding week 4, met ontwerpstap | 693.462 |
| #102 (r2492) | ontbrekend werkcollege, M | 967.384 |
| #326 (r2240) | PGM2 week 2, comprehensions | 1.173.472 |
| #377 (r3320) | vooruitverwijzingen uit PGM1, M | 1.339.265 |
| #271 (r2050) | PGM2 week 7, L | 1.507.079 |
| #134 (r357) | PGM2 week 1, volledige lus | ongeveer 2.660.000 |
| #178 (`203-proef.md` r263) | één stelsel voor opgaveniveaus | 2.972.571 |

Wat uit die reeks wél valt af te lezen, en wat de bevindingen onderbouwen, is dat de prijs
niet door de omvang van het materiaal wordt bepaald maar door het **aantal ronden** en door de
**soort tekst** die wordt geraakt. Bevinding 1 (r20-21) meet 718k in ontwerpen en verhelderen
bij #103, meer dan de auteur, en wijt dat aan vier ronden en niet aan omvang. Bevinding 16
(r728) meet bij #178 dat het materiaal na ronde 2 klaar was: tien van de elf
acceptatiecriteria stonden vanaf commit `6913faae` op gehaald, en alles daarna ging over één
criterium dat niet over het materiaal ging maar over `conventies/begrippen.md`. Haar conclusie
is de scherpste kostenuitspraak in dit corpus: een criterium over een conventiedocument luidt
*"de vier plekken spreken elkaar niet tegen"*, en dat heeft geen eindpunt, want elke ronde die
een gat dicht schrijft nieuwe zinnen en elke nieuwe zin is nieuw oppervlak. De tegenhanger
staat op r1080: een criterium dat een getal eist, convergeert wel, en het controleert de keten
die het getal doorgaf.

### Wat de twee #203-proeven laten zien

Beide proeven zijn uitgevoerd en beide staan met hun afwijkingen opgeschreven, wat ze
bruikbaar maakt.

Proef 1 (`203-proef.md` r93-137) liet de ontwerpstap weg bij twee handleidingen.
Uitkomst: #276 kwam op 72,5 procent van de referentie #256 en haalde de dertig procent niet, met twee
terechte blokkades; #280 kwam op 67,8 procent en haalde het doel met nul blokkades. De
besparing komt uit het weglaten van de ontwerpstap (215.006 bij #256), maar de auteur werd
duurder: 343.145 bij #276 tegen 280.463 bij #256, een toename van 62.682 tokens, omdat hij een
deel van het ontwerpwerk zelf deed. Drie afwijkingen van de afspraken vooraf staan erbij, en
één daarvan telt: de budgetreactie is bij #276 niet uitgevoerd.

Proef 2 (r139-199) voegde verkenner en ontwerper samen bij een L-route. Uitkomst: dat
**bespaarde niets**. De gecombineerde stap kostte 200.332 tegen 176.129 voor de twee losse
stappen bij de referentie #160. Van de bekende fasen had alleen de herstelbeoordeling een
groot verschil, en de bevinding legt uit dat dat uit de uitkomst van de beoordeling kwam en
niet uit de route die werd getest. Het totaal eindigt op *niet vast te stellen*, omdat de
hervatte auteur op de sessielimiet stopte zonder verbruiksmelding (r168-170 en
`bevindingen.md` r1373).

Beide proeven wijzen dezelfde kant op: samenvoegen van rollen verplaatst kosten in plaats van
ze weg te nemen. Dat is dezelfde vorm als bevinding 4 (r113) over werk buiten de lus: *"het
verplaatst de kosten in plaats van ze te besparen"*. Twee proeven bewijzen geen gelijkblijvende
kwaliteit, zoals `203-proef.md` r246 zelf zegt.

### De duurste poort is de bouw, en hij ging vier keer

Het scherpste kostengetal in het hele corpus staat in de ingang van #386 (`metingen.md`
r3650-3655, op de branch): vier volledige Sphinx-bouwen in een XS-werkitem waarin één `try`
uit een bestand moest. Twee van de auteur, één van de beoordelaar en één van de orkestrator
als verificatie. `make clean && make html` voert alle 127 notebooks van `source/` uit; na het
herstel deed een incrementele `make html` hetzelfde werk in **4,27 s**, met nul
waarschuwingen.

De oorzaak is gemeten en is geen vergissing van een rol. De bevinding op `bevindingen.md`
r2198 (branch) stelt vast dat de orkestrator in C1 alle vier de acceptatiecriteria aan de
onderwijskundige toewees, inclusief *de toepasselijke controles schoon, inclusief een schone
build*, met de opdracht alles zelf na te meten. Twee vindplaatsen verbieden dat: `loop.md`
§*Verificatie en eindpunt* r133-137, waar mechanische controles vóór de beoordeling gaan en de
auteur pas C5 levert als de controles groen zijn, en de rolprompt van de beoordelaar, waarin
shell *"uitsluitend voor gerichte verificatie"* is. De rol kende die grens, want hij
verantwoordde zijn shellgebruik met *"geen installatie buiten `uv sync`"*: hij schreef zichzelf
de uitzondering op in plaats van haar te melden.

Dat is de duurste vorm van herhaald werk in dit corpus, en zij komt niet uit de contextisolatie
maar uit de criteriumtoewijzing. Een rol kan niet zien dat een poort al is gedraaid, want
niemand vertelt het haar.

### Wat de administratie zelf kost

Dit is de vraag die de vakdeskundige stelde, en het antwoord is te meten. Ik heb de leesronden
opgeteld die in `metingen.md` staan op registraties en bevindingen, dus op tekst die over het
proces gaat en niet over het materiaal:

| Wat werd gelezen | Ronden | Tokens | Vindplaats |
|---|---:|---:|---|
| PR #342 en #343, `.gitignore` en één bevinding | 3 van 4 gemeten | 183.342 | r826-831 |
| PR #354, het dossier rechtzetten (incl. de onderzoeksronde) | 2 | 290.942 | r765-766 |
| PR #367, één bevinding | 2 | 231.030 | r720-735 |
| PR #366, de ingang van #104 | 2 | 214.138 | r3048-3050 |
| PR #385, de ingang van #377 | 2 | 336.954 | r3430-3432 |
| PR #286 en #287, metingen en een correctie | 4 | 177.644 | `bevindingen.md` r1335-1337 |
| **som** | | **1.434.050** | |

Dat is een **ondergrens**, om drie redenen. De eerste ronde op #342/#343 staat als *niet
vastgesteld*: zij meldde 2.714.155 tokens in 7 min 8 s, en de vorige onderzoeksronde stelde
vast dat dat intern onmogelijk is, namelijk 380.489 per minuut waar de drie ronden erna op
gewogen 12.717 uitkomen (`metingen.md` r833-841). Het getal blijft met dat voorbehoud staan en
telt niet mee. Verder zit het schrijfwerk van de orkestrator er niet in, want dat is overal
*niet beschikbaar*. En er zijn ingangen die ik niet heb opgeteld.

Zet die 1.434.050 naast de routetotalen hierboven: zes registraties lezen kostte meer
dan #326, #102 of #377 aan agentwerk, en bijna zoveel als de duurste volledige weekherziening in
de nieuwe procesversie. De ingang van #377 alleen kostte in leesronden 336.954 tokens, tegen
335.795 voor alle drie de agentstappen van heel #386: een verschil van 1.159 tokens tussen het
beschrijven van een route en het uitvoeren van een andere (`metingen.md` r3669-3671, op de
branch).

**En de leesronden vonden iets.** Dat moet er onmiddellijk bij, want het is de kant van de
balans die de kosten rechtvaardigt. De twee ronden op de ingang van #377 vonden zes fouten:
een commit die als niet-bestaand werd opgevoerd terwijl hij bestaat, een onware bewering dat
PGM1 geen `try`/`except` meer kent, een dode verwijzing die wel bestaat, een niet-bestaande
processtap, een verkeerde sectienaam, en één rekenkundige onmogelijkheid, namelijk een wijde
afbakening die meer blokken opleverde dan PGM1 fences heeft (r3430-3441). De ronden op #367
vonden drie keer dezelfde ongetelde noemer, de laatste keer in de reparatie van de vorige
(r720-735). De ronde op #343 vond een commit-hash die in geen enkele repo bestaat, in de pull
request die de bevinding *noem de vindplaats* droeg (r794-799).

Maar let op **waar** die fouten zaten. Vrijwel alle zijn beweringen in lopende tekst: getallen,
noemers, hashes, sectienamen, processtappen. De hertelling op #377 bracht vier getallen terug
en *"liet de nullen en de ijking 40/74/32/16 ongemoeid; die waren door beide lezers
onafhankelijk gereproduceerd"* (r3440-3441). De meettabellen met hun afbakening hielden dus
stand; het verhaal eromheen niet. Dat is het aangrijpingspunt voor §6.

Er is nog een kostenpost die het dossier zelf benoemt, en die niet in tokens staat. De keten
eindigt nergens: *"een registratie van een lezing die zelf opnieuw gelezen moet worden, eindigt
nergens"* (r850-851). Bij #377, #343 en #104 staat met zoveel woorden dat de laatste alinea,
de hertelling of de samenvoeging door geen rol meer is gelezen (r3443-3445, r849-851, r3041).

## 5. Het bewijs voor en tegen de kernhypothese

`onderzoek/README.md` r24-27 stelt de hypothese zo: contextisolatie vangt de fouten die één
agent maakt, want *"wie meet weet niet wat de uitkomst zou moeten zijn, wie beoordeelt heeft de
worsteling van de schrijver niet gezien, en tussen twee rollen gaat precies één artefact"*.

### Wat ervoor pleit

**De naïeve rol vindt wat niemand anders vindt, en juist omdat zij minder weet.** De leesronde
op PGM1 week 1 en 2 kostte 248k en leverde twee werkitems vol aantoonbare defecten
(`metingen.md` r36-46). De eerstejaars vond daar dat het eerste practicum met Python opent met
een instructie om op een knop te klikken die niet bestaat, dat het taartavontuur een functie
geeft die nooit wordt aangeroepen, en dat twee van de zeven *foute* uitwerkingen in een
bugzoekopgave het juiste antwoord geven (`bevindingen.md` r85-89). Het scherpste geval is
19 oktober bij #382 (r2159): de auteur bewees een overnameinstructie door alle codecellen van
de uitwerking 300 keer uit te voeren, foutloos, terwijl de tekst `import random` niet noemde.
De eerstejaars, die de uitwerking niet mag zien, las de opsomming letterlijk en gaf BLOKKEER,
want wie haar volgt krijgt een `NameError`. De bevinding voegt eraan toe: *"Bij een route met
alleen de onderwijskundige was het waarschijnlijk doorgegaan; die meet tegen de uitwerking. Dat
is niet vastgesteld."* Dat voorbehoud is correct en het is precies de vorm van bewijs die dit
corpus kan leveren: één waarneming, met de tegenhypothese erbij.

**Een verse lezer vindt wat geen poort dekt.** Bij #178 vond de lus twintig `Opgave N` in
codecommentaar die de hook per constructie niet ziet, een toetsbare zin die voor vier van de
negen uitwerkingsbestanden onwaar was, en een rechtvaardiging die door de eigen ingreep van
ronde 1 onwaar was geworden (r763-767: *"Zonder de lus was geen daarvan gevonden."*). Bij #386
ving de beoordelaar dat `handleidingen/week_6.md` naar een verdwenen notebook verwees, en de
ingang zegt erbij waarom dat telt: `handleidingen/` zit niet in de Sphinx-build, dus geen poort
dekt het (`metingen.md` r3642-3644, branch).

**De verse lezer betrapt rekenkundig onmogelijke getallen.** Zie §4: 2.714.155 tokens in zeven
minuten, en bij #377 een afbakening die meer blokken gaf dan er fences zijn.

**Een rol corrigeert naar boven.** Bij #368 gaf de orkestrator een bewering uit een
beoordelingsoordeel door zonder haar te toetsen aan zijn eigen C1-aanvulling, waarin hij zelf
een derde splitsing had gemeten. De auteur ving het en nam het puntje in gecorrigeerde vorm
over (`bevindingen.md` r1909-1916). Het dossier noemt dat zelf *"het sterkste bewijs dat de
maatregel niet van de richting afhangt"*, en dat lijkt me juist.

**En de detectie is telbaar.** De vorige onderzoeksronde mat dat van de veertien bevindingen
tussen 24 september en 1 oktober er acht gaan over een bron die niet is geraadpleegd terwijl
hij bestond, en dat juist daar de verse lezer achteraf acht keer heeft geblokkeerd
(`metingen.md` r2592-2599). Haar herformulering is de scherpste samenvatting die dit dossier
van zichzelf heeft: *"de lus heeft in deze familie één controle die werkt, en dat is detectie
achteraf; preventie is nooit geprobeerd, omdat elk preventievoorstel geparkeerd staat."*

### Wat ertegen pleit, of het duur maakt

**Isolatie beschermt niet tegen een gedeelde blinde vlek.** Bevinding 7 (r212-235): twee
beoordelaars met verschillende opdrachten merkten los van elkaar op dat twee midtermvragen
geen juist antwoord hebben, en beide concludeerden verkeerd, want *"het programma werkt niet"*
is bij die vragen het antwoord. De bevinding zegt het zelf: *"contextisolatie helpt hier niet -
ze isoleert ze van elkaar, niet van een gedeelde blinde vlek."* En natrekken hielp evenmin,
want de meting was juist.

**Isolatie veroorzaakte de duurste herhaling in het corpus.** Bij #134 blokkeerden alle vier de
beoordelaars onafhankelijk, en drie noemden dezelfde zin, die een bewust bij de poort genomen
besluit volgde dat zij niet hadden gekregen. Kosten: een volledige tweede beoordelingsronde,
ongeveer 669.000 tokens, om te bevestigen wat bij de eerste ronde al waar was
(`bevindingen.md` r550-577). De bevinding noteert dat de isolatie met opzet zo is gebouwd en
dat er niets is veranderd.

**De actor buiten de isolatie produceert de meeste fouten.** Tien van de zevenenvijftig
`##`-koppen in `bevindingen.md` noemen de orkestrator in hun titel; in de hoofdtekst zijn het
meer, maar een exact aantal vraagt een toewijzingsregel die ik zou moeten verzinnen, en dat doe
ik niet. Bevinding 11 (r404-456) zegt waar dat op neerkomt, en ik kan het niet beter
formuleren: *"Contextisolatie beschermt rollen tegen elkaars redenering. Niets beschermt de
orkestrator tegen zijn eigen."* Diezelfde actor heeft als enige geen roldefinitie in
`core/roles/`, zoals ik in §1 heb gemeten.

**Twee orkestrators op één route is geen theoretisch risico.** Bij #377 draaiden twee sessies
dezelfde herstelronde (`bevindingen.md` r1942). De tweede auteur deed de hele ronde opnieuw:
137.861 tokens, 18 min 24 s, 51 gereedschapsaanroepen. Hij ving het zelf, doordat hij op de
boom keek en zag dat zijn opdracht van een achterhaalde stand uitging. Maar er landde ook een
commit in `conventies/` die in haar eigen ronde door geen enkele rol is gelezen, omdat de twee
herbeoordelingen al gepubliceerd waren toen hij kwam. De bevinding stelt vast dat niets in deze
repo een route aan een sessie toewijst.

**De isolatie hangt aan de discipline van de rollen, niet aan de inrichting.** Bij #102 kreeg
de onderwijskundige een scratchpad aangewezen die ook het volledige C2, het C5, het C4 en het
C6 van de andere beoordelaar bevatte. Hij meldde het zelf en schreef erbij dat hij de rest
uitdrukkelijk niet had geopend (`bevindingen.md` r1725-1743). De bevinding zegt het precies:
*"dat de isolatie standhield is hier vastgesteld voor één rol in één ronde, en het is geen
controle."* Het kwam in de ronde erna meteen terug, en bij #381 op 19 oktober werd het
schrijfinterferentie: een hulpscript van de auteur werd in die gedeelde map overschreven.

**Dezelfde meting wordt meerdere keren gedaan.** Bij #386 hebben auteur, orkestrator en
beoordelaar de nameting op `ast.Try` elk met een eigen script gedaan (`metingen.md` r3626-3631,
branch). Daar bevestigde het elkaar en ving het de valse nul van #377 aantoonbaar niet op
nieuw, dus die drievoud was hier waardevol. Maar het is drie keer hetzelfde werk in een
XS-route, en samen met de vier bouwen is dat waar de prijs van isolatie zichtbaar wordt.

### Weging

Het bewijs is niet eenduidig, en ik zou het zo samenvatten.

Er is **sterk, herhaald bewijs** voor één smalle stelling: een verse lezer met een smalle
opdracht en een eigen perspectief vindt werkelijke defecten die geen mechanische poort vangt,
en de naïeve rol vindt er die een beter geïnformeerde rol per constructie niet kan vinden. Dat
is zes tot acht keer onafhankelijk waargenomen, met vindplaats en gevolg, en één keer met een
telbaar effect (drie van drie meldingen vóór een maatregel, nul van vier erna).

Er is **geen bewijs** voor de hypothese zoals `README.md` haar stelt. Niet omdat het bewijs
tegenviel, maar omdat de vergelijking nooit is gemaakt: er is geen route met één agent. En er
is **bewijs tegen een deel ervan**: isolatie helpt niet tegen een gedeelde blinde vlek, zij
veroorzaakte de duurste herhaling in het corpus doordat één artefact het poortbesluit niet
meenam, en zij is op de plek waar zij het hardst nodig is (de orkestrator) helemaal niet
aanwezig.

De eerlijkste formulering die dit corpus draagt is dus niet *"isolatie vangt fouten"* maar:
**isolatie levert detectie achteraf, en preventie is nooit geprobeerd.** Die zin is niet van
mij; zij staat sinds 1 oktober in `metingen.md` r2597-2599, en negentien dagen later geldt zij
nog.

## 6. Wat eruit volgt

Dit zijn voorstellen, geen besluiten. Zij zijn invoer voor de evaluatie van #203, en die
evaluatie ligt bij de vakdeskundige (`203-proef.md` r244-248). Ik houd het op drie, om de reden
die in mijn eigen roldefinitie staat: een rapport dat tien dingen wil veranderen wordt
genegeerd.

### Voorstel 1: splits de registratie in een mechanisch deel en een verhalend deel

**Waarop het rust.** De leesronden op zes registraties kostten ten minste 1.434.050 tokens
(§4). De fouten die zij vonden zaten vrijwel alle in verhalende beweringen: getallen zonder
telling, noemers, commit-hashes, sectienamen, een niet-bestaande processtap. De meettabellen
met hun afbakening hielden bij #377 stand bij twee onafhankelijke lezers (`metingen.md`
r3440-3441).

**Wat het zou veranderen.** Een ingang in `metingen.md` bestaat uit twee delen. Deel één is
mechanisch: de route, de procesversie met hash, de tabel met rol, ronde, tokens, duur,
toolaanroepen en uitkomst, de herstelstand, en wat de route openliet als opsomming met
vindplaats. Dat deel gaat niet langs een leesronde; de orkestrator rekent het na tegen de
verbruiksmeldingen, zoals hij bij #386 al deed. Deel twee is de verhalende toelichting, en
alleen dat deel gaat langs een lezer. Wie geen tweede deel schrijft, hoeft geen ronde.

**Wat het kost.** Een wijziging in `orc.md` §*Rondes, budget en metingen* en in de
vormafspraak in `metingen.md` §*Hoe je een meting noteert* (r1562-1568). Risico: de fouten die
nu in het verhaal worden gevonden, kruipen in de tabel. Daarom hoort het narekenen van de
tabel tegen de meldingen een benoemde handeling te zijn en geen gewoonte.

**Waaraan je zou zien dat het werkt.** De leesronden op registraties worden kleiner dan de
130k tot 180k per ronde die zij nu kosten, en de blokkades verschuiven naar `bevindingen.md`.
Zie je het omgekeerde, een blokkade op een tabel, dan is het voorstel weerlegd.

### Voorstel 2: zet de drie vier-keer-terugkerende regels op de plek waar gehandeld wordt

**Waarop het rust.** Drie patronen keerden terug met de maatregel al op papier, en in alle
drie de gevallen staat de maatregel nergens in `.claude/` (§3, gemeten): de telling van een
hervatte agent (vier keer, drie bevindingen), de controle van de eigen diff tegen de
basiscommit (de enige controle die twee keer aantoonbaar iets ving), en een eigen pad per
overdracht in plaats van een gedeelde scratchpad (drie keer). Daar komt de verouderde lokale
`master` bij (twee keer, nul treffers op `fetch` in de instructies).

**Wat het zou veranderen.** Vier zinnen, elk op de plek waar de handeling valt en niet in
`onderzoek/`:

- in `orc.md` bij de meetregel: de verbruiksmelding van een hervatte agent is cumulatief, dus
  neem het verschil met de vorige melding van diezelfde agent, en noteer de hoge lezing
  ernaast;
- in `roles/auteur.md`: noteer bij de start je basiscommit en leg aan het eind je eigen diff
  daartegen;
- in `orc.md` §*Artefacten doorgeven*: een overdracht krijgt een eigen pad, dat niet ook de
  artefacten van andere rollen bevat;
- in `orc.md` §*Inname en route*: `git fetch origin` vóór het meten, en noem als meetbasis de
  korte hash van de commit van `origin/master` die je werkelijk hebt gelezen.

**Wat het kost.** Vier regels in twee bestanden, en één procesbesluit. Alle vier zijn al als
voorstel uitgeschreven in `bevindingen.md` (r2190-2193, r814-819, r1745-1748, r1718-1721); er
is geen nieuw ontwerpwerk nodig.

**Waaraan je zou zien dat het werkt.** De eerste drie zijn hard te toetsen: een vijfde
voorkomen van de opteltelling, een beoordelaar die opnieuw moet melden wat hij niet heeft
geopend, of een derde route die tegen een stilstaande `master` is gemeten. Komt dat niet voor
in de volgende tien routes, dan is de vorm (regel bij de handeling in plaats van regel in het
dossier) voor deze familie bevestigd. Dat is precies de toets die bevinding 9 (r320) voorstelt
en die hier voor het eerst op vier gevallen tegelijk kan worden gedraaid.

### Voorstel 3: geef de evaluatie van #203 een datum en een eindige lijst, en sluit de achterstand af

**Waarop het rust.** Zeventien voorstelmarkeringen in `bevindingen.md` en twintig plaatsen
waar een bevinding haar eigen gevolg als uitgebleven of deels beschrijft (§3). De evaluatie had
volgens `203-proef.md` r238 uiterlijk twee weken na de tweede proefoplevering van 24 september
moeten plaatsvinden. De vorige onderzoeksronde noemde dit op 1 oktober haar zwaarste vondst
(`metingen.md` r2605-2607), en negentien dagen later is er niets veranderd. Daar komen twee
dossierfouten bij die ik heb gemeten en die geen besluit vragen: de onjuiste vindplaats in
bevinding 4, die bevinding 14 al weerlegt, en de dubbele nummers `## 9.` en `## 14.`, sinds
1 oktober bekend.

**Wat het zou veranderen.** Het doel is niet dat alle zeventien voorstellen worden ingevoerd;
`203-proef.md` r244-246 vraagt juist om één afsluitend besluit met een **eindige**
wijzigingslijst. Het gaat erom dat de wachtrij ophoudt te groeien, want zolang zij groeit is
"voorstel voor de evaluatie van #203" de goedkoopste manier om een bevinding af te sluiten
zonder iets te veranderen, en dan is `bevindingen.md` een plek waar werk heen gaat om te
blijven liggen.

**Wat het kost.** Een leesronde van de vakdeskundige over zeventien voorstellen, met drie
uitkomsten per voorstel: invoeren, verwerpen met reden, of laten liggen met een vervaldatum.
Een verworpen voorstel met reden is voor dit onderzoek net zo waardevol als een ingevoerd
voorstel, en het haalt de wachtrij leeg.

**Waaraan je zou zien dat het werkt.** Elke bevinding die daarna wordt opgeschreven, draagt
onder *Wat het veranderde* een vindplaats in `.claude/`, `curriculum/` of `conventies/`, of de
mededeling dat het voorstel is verworpen en waarom. Het aantal regels met *"in de instructies
is niets veranderd"* groeit niet verder dan twintig.

## Wat ik heb nagegaan en niet gevonden, en wat ik niet kon vaststellen

Dit hoort erbij, want een ronde waarvan niet duidelijk is wat er is bekeken, is de volgende
keer niet te vergelijken (`core/roles/onderzoeker.md` r67-69).

**Nagegaan en niets gevonden.** Ik heb in `.claude/` gezocht op `laat het lezen`, `zelf doet`,
`basiscommit`, `eigen diff`, `worktree`, `scratchpad`, `fetch`, `origin/master`, `5b`,
`optimaliseer`, `criticus` en `Gereedschap` als sectienaam. Alle elf gaven nul treffers in een
instructiebestand; `fetch` komt alleen voor als toestemmingsregel in
`.claude/settings.local.json`. Elk van die patronen is geijkt op een bekende treffer elders:
`laat het lezen` vindt wel de regel in `CLAUDE.md`, `5b` vindt wel de twee plaatsen in
`metingen.md` waar staat dat de stap niet meer bestaat, en `Gereedschap` vindt wel vier
treffers in `core/` waarvan geen enkele een sectiekop is. Dat is de regel uit `CLAUDE.md`
§*Meten*: een stukgelopen patroon geeft altijd nul.

Ik heb verder gezocht naar een tweede bevinding over de dubbele nummering, naar een werkitem
dat het hernummeren uitvoert, en naar een vindplaats van het rapport van de onderzoeksronde van
1 oktober binnen `onderzoek/`. Geen van die drie bestaat in dit corpus.

**Niet vastgesteld.** Ik heb geen shell, dus geen enkele commit, hash, GitHub-draad of
tokenmelding in dit stuk is door mij geverifieerd; ik heb bestanden gelezen en patronen
gedraaid met `Grep`. In het bijzonder:

- de 129 gesloten en 30 open werkitems komen uit de opdracht en zijn niet door mij nagemeten;
- wanneer `loop.md` r156-158 het menselijke bronbesluit ging eisen, en of dat het gevolg van de
  bevinding van 9 oktober is (`git log -S` op `loop.md` zou het sluiten);
- of de aangeleverde corpusgetallen precies door `1f595e4b` verklaard worden
  (`git diff --stat 6c8ea078..1f595e4b -- onderzoek/`);
- het aantal bevindingen dat aan de orkestrator is toe te schrijven op grond van de hoofdtekst
  in plaats van de kop; dat vraagt een toewijzingsregel die het bestand niet geeft;
- het exacte aantal openstaande voorstelpunten, om dezelfde reden;
- de orkestratiekosten van elke route in dit corpus. Die zijn *niet beschikbaar*, en dat is
  geen nul;
- of de kwaliteit onder de kortere routes van #203 gelijk is gebleven. `203-proef.md` r192-197
  noteert voor proef 2 dat een waarneming in de les er nog niet is: *niet vastgesteld*. Dat is
  de ontbrekende kwaliteitstoets die r238-240 vraagt niet als nul fouten te lezen, en ik lees
  haar ook niet zo.

**Wat op één waarneming rust.** De vier bouwen in #386, de dubbele orkestratorsessie bij #377,
de eerstejaarsvondst bij #382, de schrijfinterferentie bij #381 en het narekenen naar boven
door de auteur bij #368. Elk van die vijf is één geval, met de meting erbij, en geen van de
vijf draagt op zichzelf een maatregel.

---

**Meetregel.** Rol: onderzoeker (buiten de lus). Ronde: 2 van deze rol; de eerste draaide op
1 oktober 2026 en staat in `metingen.md` r2581-2587. Tokens: 17.052 output tokens over
22 toolaanroepen in deze sessie, wandklok ongeveer 34 minuten. **Dat is een andere grootheid
dan de tabellen in `metingen.md`**, die de cumulatieve `subagent_tokens` uit de
verbruiksmelding gebruiken; die melding kan ik niet zien, en de orkestrator zet het
vergelijkbare getal erbij. De opgave is dus wat ik zelf kan lezen, zoals het voorstel in
`bevindingen.md` r2267-2270 (branch) vraagt, en niet het huisgetal. Duur: zie de wandklok, die
ook mijn wachttijd bevat en dus hoger ligt dan het agentverbruik. Omvang: ongeveer 6.200 regels
`onderzoek/` gelezen, plus `loop.md`, `orc.md`, dertien roldefinities steekproefsgewijs,
`C6-beoordeling.md`, `C3-verhelderingsresultaat.md` en gerichte metingen in `curriculum/` en
`.claude/`; zeventien patroonmetingen gedraaid, alle geijkt. Uitkomst: dit retrospectief, met
zeven grenzen van het corpus, zes geland en vijf niet of half geland verklaarde bevindingen,
zes terugkerende patronen met hun aantal, een administratiekost van ten minste 1.434.050
tokens, en drie voorstellen als invoer voor de evaluatie van #203. Niets gewijzigd, niets
besloten.

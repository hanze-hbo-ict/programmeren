# Bevindingen over de werkwijze

Genummerd, met de datum, het bewijs en wat het veranderde. Een bevinding zonder
gevolg is een anekdote; als er niets veranderde staat erbij waarom niet.

Waar een bevinding op één waarneming rust, staat dat erbij.

---

## 1. De verhelderaar had geen ernstdrempel, en de lus optimaliseerde tegen zijn eigen criticus

*29-30 augustus 2026. Werkitem #103.*

Het weekontwerp werd drie keer afgekeurd, en de bezwaren werden elke ronde kleiner:
ronde 1 structureel (een verificatiemodel dat bij de build niet kón draaien; een
besluit dat het ontwerp zelf nam terwijl het van de vakdeskundige was), ronde 2
tekstueel (een ambigue afsluiting), ronde 3 mechanisch (drie zoekpatronen die
stukliepen zodra je ze draaide).

Samen **718k tokens in ontwerpen en verhelderen** — meer dan de auteur — voor een
ontwerp dat na ronde 2 bruikbaar was.

De oorzaak was aanwijsbaar: het contract vroeg de verhelderaar "is dit
uitvoerbaar", en op die vraag is in elk ontwerp iets te vinden. Er was geen
onderscheid tussen wat de auteur ophoudt en wat hij zelf ziet.

**Er zit een tweede laag in.** Het C3 van ronde 3 eiste dat elk zoekpatroon
uitvoerbaar was. Ronde 4 antwoordde met een meetgereedschap van zes patronen, met
ijkgetallen en een shell-functie — elf procent van het document. Elke stap
verdedigbaar, samen uit verhouding. De lus optimaliseerde tegen zijn eigen criticus.

**Wat het veranderde.** Een ernstdrempel in `roles/verhelderaar.md` en het
C3-contract: blokkerend is wat de auteur ophoudt of wat hij verkeerd doet zonder
het te merken; de rest reist mee als verbeterpunt en kost geen ronde. De toets is
of de fout **luid of stil afloopt**. Verder: de tweede FAAL-ronde werd een
reparatie in plaats van een herontwerp, en `loop.md` benoemt het
optimaliseer-tegen-de-criticus-patroon.

**Getoetst.** Onder de drempel was ronde 3 geen FAAL geweest. De ronde erna gaf
AKKOORD met negen bevindingen, alle als verbeterpunt.

---

## 2. Fouten die stil aflopen zijn de duurste, en meten is waar ze zitten

*29 augustus – 1 september 2026. Zes keer waargenomen.*

Zes keer ging een meting mis zonder dat er iets fout ging:

1. `rg` is op deze machine geen ripgrep maar een shell-functie. Het meetgereedschap
   was op ripgrep-semantiek geschreven, inclusief `-U` voor multiline.
2. De patronen P4 en P6 stonden in een markdown-tabel en droegen daardoor `\|` in
   plaats van `|`. De alternatie viel weg en beide gaven **nul** treffers — terwijl
   nul juist het geslaagd-criterium was. Een stuk patroon slaagt altijd.
3. `\w+\[..\]\[..\]` matcht geen index van één teken en gaf nul treffers op een
   bestand waar `my_list[3][3]` twee keer in staat.
4. `ast.get_docstring` geeft een docstring genormaliseerd terug, zonder de
   inspringing die in de bron staat. Zoeken op wat de AST teruggeeft vindt in de
   bron niets.
5. In sommige notebookcellen is `source` één string in plaats van een regellijst.
   `for r in c["source"]` itereert dan over losse tekens en doet niets.
6. Twee keer een buildcontrole met `grep -i "warning|error"` die aansloeg op de
   configuratieregels van myst, waar `suppress_warnings` in staat.

Geen van de zes gaf een foutmelding. Ze gaven een antwoord.

**Wat het veranderde.** In `loop.md` een sectie *Gereedschap: gebruik wat er is* —
stel vast wat er op de machine staat in plaats van het aan te nemen, installeer
nooit iets, en **ijk elk patroon op een bekend getal voordat je een nul
vertrouwt**. Diezelfde regel staat in `CLAUDE.md`, zodat elke sessie hem laadt.

**Wat het niet oploste.** Nummer 4, 5 en 6 zijn ná die regel gebeurd, door de
orkestrator zelf, bij werk dat buiten de lus om werd gedaan. Zie bevinding 4.

---

## 3. Op ongelezen materiaal is lezen goedkoper en opbrengender dan ontwerpen

*30 augustus 2026. Twee weken, twee beoordelaars.*

Twee beoordelaars — een redacteur en een eerstejaars — op PGM1 week 1 en 2, die de
lus nooit hadden gezien: **248k tokens**, en het leverde twee werkitems op vol
aantoonbare defecten. Ter vergelijking: één week door de volle lus kostte 1,13M.

De eerstejaars vond dingen die geen andere rol zou vinden: dat het eerste practicum
met Python opent met een instructie om op een knop te klikken die niet bestaat, dat
het taartavontuur een functie geeft die nooit wordt aangeroepen, en dat twee van de
zeven "foute" uitwerkingen in een bugzoekopgave het juiste antwoord geven.

De redacteur vond wat alleen met tellen te zien is: dat alle 25 collegeopdrachten
woordelijk in de opstap terugkomen (aantoonbaar, want de kapotte nummering 1, 2, 3,
6, 7, 4, 5 komt in beide voor), en een verhouding van 94 voorspelvragen tegen 17
schrijfopdrachten.

De afbakening van de solutionplicht staat in het besluit in
[curriculum/uitgangspunten.md](../curriculum/uitgangspunten.md). Werkitem #253
legt daar vast dat college- en practicumopdrachten er niet automatisch onder
vallen; het ontbreken van een gelijknamige `solution` bij een collegeopdracht is
daarmee geen vastgesteld tekort.

**Wat het veranderde.** De leesronde is als eigen modus in het C6-contract
opgenomen: geen dekking van acceptatiecriteria maar van de normen die er wel zijn,
geen stop op een ontbrekende kern, en de plicht voor wie hem start om te zeggen dat
het er een is. In `loop.md` staat wanneer je hem inzet: **vóór** een ongelezen week
door de volle lus gaat, niet erna.

**Kanttekening.** Beide beoordelaars moesten hun eigen stopvoorwaarde negeren en
schreven een alinea over waarom ze niet stopten. Het werkte omdat de opdracht
expliciet zei dat er geen C5 was.

---

## 4. Werk dat buiten de lus om wordt gedaan, verplaatst de kosten in plaats van ze te besparen

*31 augustus – 1 september 2026.*

Werk dat te klein leek voor een werkitem is met de hand gedaan. Drie keer leverde
dat een reparatie op die een rol zou hebben gevangen:

- Een **half doorgevoerde vertaling** in `solutions/2_rochambeau`: één van drie
  regels werd Nederlands, met `"""Play a game of rock-paper-scissors in Dutch` boven
  `argumenten: geen (...)`. Half vertaald is slechter dan onvertaald. Een redacteur
  ziet dit.
- Een **kop die de conventie niet volgde** in `5_opstap`: twaalf keer "Opgave" waar
  `begrippen.md` "Opdracht" voorschrijft — in een week die net was herzien. De
  beoordeling van die week was overgeslagen.
- Een **diff van 370 regels voor 44 wijzigingen**, doordat notebookcellen in een
  ander formaat werden teruggeschreven dan ze hadden. Dat maakt een PR
  onbeoordeelbaar: de echte wijziging verdwijnt in de opmaak.

Alle drie uiteindelijk met de hand gevonden. Eén doordat een getal niet klopte met
wat er was gedaan; twee door de diff regel voor regel te lezen. Geen hook en geen
build had ze gezien.

**Wat het veranderde.** De regel *wie het zelf doet, laat het lezen*, in
`roles/triage.md` en in `/orc`: werk dat buiten de lus om wordt gedaan gaat daarna
alsnog langs minstens één beoordelaar. En, breder, bevinding 8.

---

## 5. Sommige gebreken zijn vanuit geen enkele week zichtbaar

*31 augustus 2026. Eerste veegronde van de eindredacteur.*

174k tokens over de hele cursus, en drie bevindingen die per week niet te zien zijn:

- **Dictionary-methoden komen in de hele cursus nul keer voor.** `.items()`,
  `.keys()`, `.values()` en `.get()` samen: vijf treffers, alle vijf in bestanden
  die aan geen week hangen. Dat raakt twee leeruitkomsten, samen 20% — en de
  codeconventie draagt de week-7-grens juist met het argument *"dictionaries zonder
  `.items()` wordt gekunsteld"*.
- **Het besluit "recursie naar PGM2" is in drie lagen uitgevoerd en in de vierde
  niet.** Materiaal, PGM1-tentamen en PGM2-tentamen volgen het; de toetsmatrijs
  niet. Gevolg: het PGM2-tentamen besteedt een derde van zijn punten aan een
  onderwerp waarvoor de PGM2-matrijs geen enkele uitkomst kent.
- **Over de hele cursus zit 51% van het opgavemateriaal in de optionele laag.** De
  leerlijn meet alleen PGM1 en concludeert daar dat de scheefheid kleiner wordt.

Daarnaast: de vier weken die in dezelfde ronde waren herzien **liepen uiteen** op
de opgavekop — week 5 koos "Opgave", de weken 3, 6 en 7 "Opdracht". De kloof in de
repository was gegroeid, niet gekrompen.

**Wat het veranderde.** De eindredacteur mocht niet over dekking en niveau
oordelen (*"je oordeelt niet over de inhoud van een week"*) terwijl hij de enige
was die het kon; de onderwijskundige moest het door een kijkgat, met alleen de kern
van één oplevering als invoer. Die grens is scherper gesteld in plaats van
weggehaald: *"opgave 6 is slecht gekozen"* is niet van hem, *"de toets weegt anders
dan de matrijs zegt"* wel.

---

## 6. Triage is de goedkoopste rol en neemt het duurste besluit

*29 augustus – 1 september 2026.*

Twee triageruns kostten samen **32k**, twee procent van de sessie. Ze bepaalden of
er een lus van 1,13M zou draaien.

En het routebesluit was alles of niets: `LICHT` sprong van de hele lus naar
"schrijf het maar", waarmee meten, ontwerpen, verhelderen, de poort én alle
beoordeling in één keer wegvielen. Er was geen manier om te zeggen: dit moet
gemeten worden maar niet ontworpen.

Daarbij werden twee dingen in één getal gepropt. **Omvang en verantwoordelijkheid
zijn niet hetzelfde.** "Vertaal achttien docstrings" is qua omvang S en raakt twee
rollen hard: meten (de omvang van het werk is zelf een bewering) en lezen (een
vertaling kan grammaticaal goed en toch inconsistent zijn).

**Wat het veranderde.** C1 noemt de rollen bij naam in plaats van een route, met
per rol de vraag die hem oproept, en `/orc` draait precies die. Omvang en
rollenlijst staan naast elkaar: de eerste zegt hoe diep, de tweede welke.

---

## 7. Een rol kan goed meten en verkeerd concluderen als de kennis buiten de repo ligt

*31 augustus 2026.*

De eindredacteur telde de punten in beide oefententamens, kwam op 90 uit tegen
matrijzen die op 100% sluiten, en concludeerde dat er geen omrekening bestond
tussen percentages en punten. Dat blokkeerde zijn hele toets op dekking en niveau.

De meting klopte. De conclusie niet: het cijfer is `9 × behaalde punten / totaal + 1`,
met een totaal van 90, en die +1 is de basis omdat een student minimaal een 1
haalt. Dat stond nergens in de repository.

**Wat het veranderde.** De formule staat nu in `curriculum/leeruitkomsten.md`, en
de eindredacteur weet het. Maar het wijst op iets breders: het werkitemsjabloon
heeft een veld *Wat de repo niet weet*, en dat is er juist voor. De eindredacteur
draait zonder werkitem en heeft dat veld dus niet. **Nog niet opgelost.**

### Tweede voorval, 1 september 2026

Bij de leesronde op week 4 merkten **beide** beoordelaars los van elkaar op dat
twee midtermvragen geen juist antwoord hebben: opgave 18 loopt op een
`ZeroDivisionError`, opgave 20 eindigt nooit. De redacteur voerde er nog een
bewijsstuk bij aan - de dode variabele `number = 48` - om te laten zien dat "het
programma werkt niet" niet de bedoeling was.

Beide metingen klopten. Ik heb ze zelf nagerekend en ze hielden stand. De conclusie
klopte niet: de vragen toetsen code lezen en begrijpen, en tot de uitkomsten die je
leert voorspellen horen de fouten. "Het programma werkt niet" *is* het antwoord, en
die optie staat bij elke vraag.

Twee dingen maken dit voorval erger dan het eerste. De kennis lag niet bij één rol
die pech had: twee rollen met verschillende opdrachten kwamen langs dezelfde plek
en beoordeelden hem allebei verkeerd, wat betekent dat contextisolatie hier niet
helpt - ze isoleert ze van elkaar, niet van een gedeelde blinde vlek. En het
nareken*en* hielp evenmin: de meting bevestigen bevestigde de verkeerde conclusie,
want er viel niets te weerleggen aan de waarneming.

Wat het wél had gevangen is dat het besluit ergens stond. Dat is precies wat
bevinding 7 al concludeerde, en de herhaling laat zien dat het veld *Wat de repo
niet weet* het probleem niet dekt: dit werkitem bestond nog niet toen de rollen
draaiden. Bij een leesronde is er geen C0 om zo'n veld in te vullen.

**Wat het veranderde.** Het besluit staat nu in `curriculum/uitgangspunten.md`
onder *Leesvragen mogen fout aflopen*, met een tabel die de twee vragen die goed
zijn scheidt van de twee die het niet zijn, en met een regel gericht aan wie het
materiaal later nakijkt: repareer deze niet. Dat is de goedkoopste borging, want
ze staat op de plek waar een rol toch al langskomt.

Wat er niet is veranderd: een leesronde begint nog steeds zonder een plek waar
staat wat er over dit materiaal al besloten is. **Deels opgelost.**

### Meting, 9 oktober 2026: de eerste veegronde mét werkitem (#375)

#375 gaf de eindredacteur voor het eerst een C0, met het veld *Wat de repo niet
weet*. Dat veld bevatte drie punten: deze bevinding, de kosten van de vorige
ronde, en dat de PGM2-bevindingen uit #124 geparkeerd waren voor overleg met de
PGM2-docent. Geen van de drie was kennis waarvan een conclusie in het rapport
afhing.

**Er volgde geen verkeerde conclusie.** De orkestrator heeft bij de bespreking
acht bevindingen nagemeten op `71f82f94`: A1a, A1c, A1d, A2, B1, B2, B3 en B4.
Ze hielden stand, op één ondertelling na: `wk10ex3.py` staat twee keer in het
practicum en niet één keer. B4 ving zelfs een verkeerde premisse in een eerdere
issue. #348 vroeg of `_` geldt in weken *"waar de student het nog niet kent"*,
terwijl de leerlijn het in PGM1 week 4 introduceert.

**Wat verkeerde conclusies voorkwam, was niet het veld.** Het rapport had een
sectie *Niet vastgesteld* met vier punten die het niet kon beslissen. Twee daarvan
bleken precies de kennis te vragen die buiten de repo lag:

- of `is True` in asserts bewust is (de vakdeskundige: nee, eruit; #377)
- of *werkcollege* en *practicum* hetzelfde bedoelen

Bij het tweede punt beschreef de repo zelf het verkeerde model. Volgens
`uitgangspunten.md` r58-67 is het werkcollege `practicals/` en het practicum
`problems/`. Volgens de vakdeskundige zijn er twee colleges en een practicum, en
zijn de opgaven huiswerk (#380). Een rol die de repo als waarheid had genomen,
had hier verkeerd geconcludeerd. De eindredacteur deed dat niet, omdat hij het
openliet. De roldefinitie vraagt die sectie niet: `grep -i "niet vastgesteld"`
op `.claude/agent-role-loop/core/roles/eindredacteur.md` geeft 0. De ijking van
dat patroon is het rapport zelf, dat de kop draagt.

**Wat alleen in de bespreking boven kwam.** Drie dingen stonden niet in het veld
en niet in de repo: de indeling van de week, dat het PGM1-oefententamen later
wordt rechtgetrokken, en dat de extra rond `minimax.md` later komt. Ze kwamen
pas boven toen de vakdeskundige per bevinding besliste. Het veld vangt wat de
schrijver van het werkitem vooraf weet. Wat een bevinding pas oproept, vangt het
niet.

**Wat het veranderde.** Nog niets aan de werkwijze. De meting wijst op een
goedkopere borging dan het veld: een verplichte sectie *Niet vastgesteld* in het
rapport van de eindredacteur, met per punt de vraag aan de vakdeskundige. Dat is
een procesbesluit voor de vakdeskundige en is hier niet ingevoerd. **Deels
opgelost**, met als nieuw gegeven dat het rapport zelf de kennisvraag kan
dragen, zonder een C0.

---

## 8. Het register hield de stand van de discussie bij, niet die van het materiaal

*31 augustus 2026.*

De veegronde vond 25 MB logisimmateriaal — een pagina in de inhoudsopgave, een
Java-applicatie van 22 MB, schakelbestanden en tien schermafbeeldingen — voor een
onderwerp dat volgens het besluitenregister al maanden was geschrapt. Hij zette het
in categorie *licht*.

Hij kende de huidige lijn wel; hij schreef er zelf bij dat schakelingen volgens het
register zijn geschrapt. Wat misging was de weging, en dat had een oorzaak: hij
vond het via zijn punt over **wezen**, een opruimcategorie. Maar de pagina was geen
wees — hij stond gewoon in de inhoudsopgave. De echte bevinding was een andere: *een
gesloten besluit is niet uitgevoerd.*

Dezelfde vorm als het recursiebesluit uit bevinding 5, en dát woog hij wél zwaar —
maar dat vond hij omdat de matrijs zichzelf tegensprak, niet omdat hij ernaar zocht.

**Wat het veranderde.** Het register legde uit wat *aard* betekent en nergens wat
*status* betekent, en de waarden beschreven de stand van de discussie. Nu staat
erbij of het materiaal al volgt: *uitgevoerd*, *deels uitgevoerd*, of *nog niet
uitgevoerd* — en **staat er niets, dan is het niet vastgesteld en niet: het is
gedaan**. De eindredacteur zoekt er nu naar. Het onderscheid waar dit om draait:
**werk in uitvoering tegenover afgerond werk**.

---

## 9. Een regel is geen borging

*1 september 2026.*

Bevinding 2 leverde een regel op: ijk elk patroon op een bekend getal voordat je
een nul vertrouwt. **Drie van de zes stille meetfouten gebeurden ná die regel.**

Dat is de scherpste toets die er is - gebeurt hetzelfde nog eens ná de maatregel,
dan raakt de maatregel de oorzaak niet - en de eerste keer dat we hem op onszelf
toepasten faalde onze eigen borging erop.

De oorzaak is niet dat de regel verkeerd is. Hij is juist. De oorzaak is dat een
regel in een document een **instructie** is, en dat instructies leken zodra het werk
onder tijdsdruk staat of buiten de lus om gaat. Alle drie de gevallen waren
handwerk.

**Wat het veranderde.** Waar het kon is de instructie vervangen door een handeling
die toch al gebeurt. De meting hoort nu in de reactie waarin het artefact wordt
geplaatst, niet in een losse stap erna: vergeten is dan geen stap overslaan maar een
onvolledig artefact plaatsen, en dat verbood het contract al.

**Wat het niet oploste.** Handwerk is niet af te dwingen. Daar is gekozen voor
zichtbaarheid in plaats van dwang: `metingen.md` heeft een kopje *Werk buiten de lus
om* met een kolom "achteraf gelezen?", zodat een lege lijst laat zien dat er niets
is opgeschreven in plaats van dat het lijkt of er niets is gebeurd. De eerste zeven
ingrepen staan er, en scoren zeven keer **nee**.

Of dat werkt is niet vastgesteld. Het is de tweede maatregel op dezelfde oorzaak, en
de toets is dezelfde: gebeurt het daarna nog een keer.

---

## 10. Een correctie in een reactie corrigeert het document niet

*1 september 2026.*

Bij een consistentiecontrole op de open werkitems bleken er vier een bewering te
dragen die al was weerlegd. In alle vier de gevallen **stond de correctie er wel,
maar als reactie eronder** terwijl de fout in de tekst zelf bleef staan:

- **#104** droeg de randvoorwaarde *"er gaat er geen weg, er komt er geen bij, en
  de formulering blijft; dat is extern vastgelegd"*, een dag nadat die formulering
  in `curriculum/uitgangspunten.md` was rechtgezet en er een correctie op de issue
  stond.
- **#136** noemde 71% waar de hermeting 60% gaf - een cijfer dat een uur eerder al
  was gecorrigeerd en dat ik daarna alsnog in een nieuw werkitem overnam.
- **#124** droeg datzelfde cijfer op meerdere plekken, en voerde bevinding A2 nog
  als open terwijl zij was uitgevoerd.
- **#126** verwees naar "bevinding A4", wat verwarrend werd zodra leeruitkomst A4
  van matrijs veranderde.

Wie zo'n issue van boven naar beneden leest, gelooft de tekst. De correctie
eronder wordt gevonden door wie hem toch al kent.

**Dit is de derde keer dat dezelfde vorm terugkomt.** Bevinding 8 ging over het
besluitenregister dat de stand van de discussie bijhield en niet die van het
materiaal. De veegronde vond 25 MB voor een geschrapt onderwerp omdat *gesloten*
niet *uitgevoerd* betekende. En nu: een issue die *gecorrigeerd* is zonder dat de
tekst het is.

Steeds hetzelfde: **de vastlegging en de werkelijkheid lopen uiteen, en er is niets
dat het verschil zichtbaar maakt.**

**Wat het veranderde.** De vier issues zijn in hun body gecorrigeerd, niet alleen
in een reactie, en #104 en #124 dragen bovenaan een regel die de lezer naar de
reacties stuurt. Dat is een reparatie en geen maatregel.

**Wat het niet oploste.** Er is geen regel die zegt waar een correctie hoort te
landen. Voor artefacten in de lus is dat geen probleem - die zijn onveranderlijk en
een nieuwe ronde levert een nieuw artefact op. Het probleem zit bij documenten die
blijven staan en meebewegen: een werkitem, het besluitenregister, een
conventietelling.

Een mogelijke regel, nog niet ingevoerd: *corrigeer waar de fout staat, en laat in
een reactie zien dat je het hebt gedaan* - de omgekeerde volgorde van wat er nu
gebeurt. Of, sterker: een issue waarvan de body is achterhaald krijgt bovenaan een
regel die dat zegt, zoals het besluitenregister sinds bevinding 8 achter de status
zet of het materiaal al volgt.

Of dat werkt is niet vastgesteld, en gezien bevinding 9 is een regel op zichzelf
geen borging. De toets is dezelfde: gebeurt het daarna nog een keer.

---

## 11. De orkestrator citeert zichzelf in plaats van de bron

*1 september 2026. Vijf waarnemingen.*

Vijf keer in één sessie moest de orkestrator een eigen uitspraak corrigeren, en
alle vijf hadden dezelfde vorm: **een bewering overgenomen uit wat hij zelf eerder
had gezegd, in plaats van uit de bron.**

| Wat er werd beweerd | Wat het was | Waar de bron stond |
|---|---|---|
| Week 5 is 71% extra | 60% | Zelf te meten; 71% kwam uit een meting van vóór de herziening |
| De tabel *Voorgestelde correcties* is nieuw | Bestond al sinds het curriculummodel | `git log -S` |
| De uitkomsten liggen extern vast, formulering blijft | Er is een procedure, geen slot | `leeruitkomsten.md`, twee secties |
| De toets besteedt 40 van de 90 punten aan ontwerpwerk | 15; opgave 7 schrijft de opdeling voor | De opgavetekst zelf |
| Triage adviseerde #115 langs de weken te splitsen | Adviseerde het grotendeels op te heffen | Het C1, drie regels verderop |

Geen van de vijf is gevonden door een controle. Vier ervan zijn gevonden doordat de
vakdeskundige ernaar vroeg; de vijfde doordat een getal niet klopte met wat er net
was gedaan.

**Waarom dit een eigen bevinding is en niet een geval van bevinding 2.** Die ging
over metingen die stil mislukken - een patroon dat nul teruggeeft, een AST die
anders normaliseert. Hier mislukt er niets. De meting was er, zij was juist, en zij
werd correct opgeschreven. Wat er misging is dat een latere samenvatting de bron
niet meer raadpleegde.

De repo heeft precies hiervoor een regel, in `CLAUDE.md` en in de verkennersrol:
*beweer niets over dit materiaal zonder het te meten, en meet het ding zelf, niet
iets ernaast.* Die wordt op het materiaal toegepast en niet op de eigen eerdere
uitspraken. Een gespreksgeschiedenis voelt als kennis en niet als een bron die
geraadpleegd moet worden - en dat is precies wat zij is, met dezelfde
houdbaarheidsdatum als een telling in `conventies.md`.

**Waar het zich concentreert.** Alle vijf komen voor in een samenvatting: een
werkitem schrijven op grond van een eerdere meting, een issue bijwerken na een
besluit, een adviesronde navertellen. Het maken van het artefact zelf ging goed;
het hergebruik ervan niet.

**Wat het veranderde.** Nog niets, en dat is met opzet. Gezien bevinding 9 is een
regel op zichzelf geen borging, en dit is bij uitstek een geval waar een regel niet
helpt: de orkestrator wist de regel al. Wat wel zou kunnen werken is een handeling
- teruglezen vóór samenvatten - maar die is niet af te dwingen en zou bij elke
samenvatting een leesronde toevoegen.

Wat de bevinding wel oplevert is een **plek om te tellen**. Als dit patroon in een
volgende reeks werkitems opnieuw vijf keer voorkomt, is dat een sterker argument
voor een maatregel dan wat hier nu staat. Als het één keer voorkomt, was deze
sessie een uitschieter - een lange sessie met veel besluiten die elkaar snel
opvolgden.

**Voor het onderzoek is dit het interessantste geval in dit document**, want het
raakt de aanname onder de hele lus. Contextisolatie beschermt rollen tegen elkaars
redenering. Niets beschermt de orkestrator tegen zijn eigen.

---

## 12. Een rol zonder shell beweert toch wat het gereedschap zou doen

*1 september 2026.*

De redacteur las week 4 in een leesronde. Hij had `Read`, `Glob` en `Grep`, geen
`Bash`, en hij wist dat: bij *Build schoon* schreef hij **niet gemeten**, met de
reden erbij. Twee alinea's verderop stelde hij dat `lectures/4a_lussen.ipynb` de
hook `check-code-blocks` breekt omdat cel 74 een `return` op moduleniveau heeft
zonder `<!-- codecontrole:skip -->`, en in zijn slotparagraaf dat het bestand
daarom "niet te committen" is — als één van de dingen die vóór publicatie moesten.

Gedraaid: de hook slaagt, op alle tien de bestanden van week 4, en
`check-notebook-tags` ook. `return` op moduleniveau is voor `ast.parse` geldige
syntaxis; de fout valt pas bij `compile`. De waarneming klopte — die `return`
staat er, zonder skip — maar het gevolg was afgeleid uit hoe de hook zou werken.

Dit is bevinding 7 met een verschil dat telt. Daar lag de ontbrekende kennis buiten
de repository en kon de rol er niet bij. Hier lag ze binnen handbereik: het is één
commando, de rol had het alleen niet. En de rol maakte zichtbaar dat hij het
onderscheid kende, want hij paste het één regel eerder correct toe.

De verleiding zit in de vorm van het oordeel. "Niet gemeten" invullen bij een
kolom kost niets; een aparte alinea openen met "dit heb ik niet kunnen nagaan"
verzwakt de bevinding waar je hem juist opschrijft.

**Wat het veranderde.** De bevinding is niet in werkitem #146 als eis beland maar
als weerlegging, onder *Wat de repo niet weet*, zodat de auteur er geen regel voor
schrijft die niets oplost. Structureel is er nog niets veranderd. Twee richtingen,
geen van beide genomen:

- De beoordelaars `Bash` geven. Dat maakt ze duurder en het haalt de scheiding weg
  die de leesronde goedkoop houdt.
- In het C6-contract eisen dat een bewering over gedrag van gereedschap het label
  *gelezen* of *gemeten* draagt, net als de kolom nu al doet — dan geldt de regel
  overal in het oordeel en niet alleen in de tabel.

De tweede is de goedkoopste, en hij sluit aan op wat de rol uit zichzelf al deed.
**Nog niet opgelost.**

---

## 13. Eén artefact per overdracht maakt het werkitem onleesbaar

*1 september 2026.*

Werkitem #146 stond bij de poort op **135.829 tekens** — ruwweg twintigduizend
woorden, verdeeld over een body en acht reacties. De vakdeskundige:

> "issue #146 is waanzinnig groot geworden, zo veel tekst dat ik de bomen door het
> bos niet meer zie."

Geen van die artefacten is te lang voor zichzelf. C1b is 34.000 tekens omdat de
verkenner negen bestanden heeft doorgemeten en dat ook laat zien; C2 is 36.000
tekens omdat het negen onderdelen met verificatiemodellen draagt. De regel *één
artefact in, één artefact uit* werkt precies zoals bedoeld. Het probleem is de
**optelsom**, en die heeft niemand als taak.

Dat is een ander soort gebrek dan de vorige twaalf. Hier gaat niets mis in een
rol; het gaat mis tussen de rollen, op de enige plek waar een mens moet beslissen.
De lus is gebouwd om context te isoleren zodat rollen elkaar niet besmetten — maar
de vakdeskundige heeft juist géén isolatie: hij krijgt bij de poort alles tegelijk.

Er speelt nog iets. Dezelfde bevinding kwam drie keer terug — de leesvragen die
fout aflopen, telkens met een nieuwe opgave erbij (18 en 20, daarna 14) — en elke
keer schreef ik hem opnieuw op en legde ik hem opnieuw voor. Dat is niet alleen
verspilling: het is ruis bovenop een issue die al te vol was, en het maakt het
besluit dat er wél ligt moeilijker vindbaar. De vakdeskundige moest dat twee keer
zeggen.

**Wat het veranderde.** Twee dingen, allebei uitgevoerd.

De **body van het werkitem is nu de kaart en niet het archief**: waar het over
gaat in vijf regels, wat er níét verandert, de zes besluiten die bij de poort
liggen met hun aanbeveling, en een tabel met links naar de artefacten en wat ze
kostten. De oorspronkelijke tekst staat eronder in een `<details>`. De artefacten
blijven staan waar ze staan — de traceerbaarheid is niet het probleem, de
vindbaarheid was het.

En het besluit *Leesvragen mogen fout aflopen* in `curriculum/uitgangspunten.md`
is **van gevallen naar soort** herschreven. Het somde opgave 18 en 20 op; nu zegt
het dat het voor de hele soort geldt, met "blijf hiervan af, meld het niet
opnieuw" erbij en met opgave 14 er expliciet bij omdat die het gevaarlijkst is.
Een besluit dat gevallen opsomt, nodigt uit tot het melden van het volgende geval.

Wat er niet is opgelost: er is nog steeds geen rol die de optelsom bewaakt, en
niets dwingt de volgende orkestrator om de body als kaart te onderhouden.
**Deels opgelost.**

---

## 14. Beoordelaars herhalen een besluit dat de poort al nam, omdat ze het besluit niet krijgen

*1 september 2026. Werkitem #134.*

Alle vier de beoordelaars gaven bij de eerste ronde onafhankelijk **BLOKKEER**,
en drie van de vier noemden dezelfde tekst als blokkerend: een zin in
`lectures/8a_datastructuren.ipynb` die verwijst naar een tuple "die je in PGM1
week 7 al bent tegengekomen." Die tuple stond op dat moment inderdaad nog
nergens in het PGM1-week-7-materiaal — maar dat was geen gat, het was een
bewust genomen besluit. Bij de poort van hetzelfde werkitem had de
vakdeskundige al vastgelegd dat tuples naar PGM1 week 7 verhuizen en dat de
volgorde waarin de twee werkitems (#134 en #102) worden uitgevoerd er niet toe
doet, juist met het argument dat de daadwerkelijke onderwijsvolgorde (PGM1 vóór
PGM2) los staat van welke pull request eerder landt.

De beoordelaars konden dat niet weten. Het contract schrijft voor dat elke
beoordelaar **alleen de kern van C5** krijgt, met opzet: "Geef geen enkele
beoordelaar het uitgebreide deel of het oordeel van een ander." Het C4-besluit
zelf — de reden waarom de tekst mag staan zoals hij staat — hoort bij geen van
beide. Het gevolg: vier onafhankelijke, correcte metingen ("dit klopt niet met
wat er nu in `source/` staat") die vier keer tot dezelfde onterechte conclusie
leidden ("dus is dit een fout"), omdat er niemand was die het antwoord op de
vraag "is dit besluit al genomen?" kon geven behalve de vakdeskundige zelf, pas
bij het lezen van het C7.

Dat kostte een volledige tweede beoordelingsronde: vier beoordelaars plus de
hoofdredacteur opnieuw, **ongeveer 669.000 tokens** om te bevestigen wat bij de
eerste ronde al waar was. Zie [metingen.md](metingen.md#werkitem-134--pgm2-week-1-van-list-comprehension-naar-datastructuren).

Dit is een ander soort gebrek dan bevinding 1, dat over een ontbrekende
ernstdrempel ging. Hier maten de rollen precies goed volgens hun eigen
contract; het gat zit tussen de rollen, in wat een latere rol niet krijgt van
een eerdere.

**Wat het veranderde.** Nog niets. De isolatie tussen ontwerp en beoordeling is
met opzet zo gebouwd (bevinding 11 laat zien wat er misgaat als een latere rol
wél toegang heeft tot eerdere redenering: hij citeert zichzelf in plaats van de
bron), en het is niet vanzelfsprekend dat het C4-besluit daar een uitzondering
op moet zijn. Een mogelijke maatregel — de C5-kern laten verwijzen naar de
specifieke C4-beslissingen die een bewering onderbouwen, zodat een beoordelaar
kan navragen zonder de hele geschiedenis te krijgen — is niet ingevoerd en niet
beproefd.

Wat de bevinding wel oplevert is dezelfde **plek om te tellen** als bevinding
11: komt dit patroon terug bij een volgend werkitem met een vergelijkbare
poortbeslissing, dan is dat een sterker argument dan deze ene, goed gemeten
maar op zichzelf staande waarneming.

---

## 14. Niets toetst wat de orkestrator schrijft

*2 september 2026.*

De lus laat elk artefact door een verse rol beoordelen. Het ontwerp gaat langs de
verhelderaar, de oplevering langs vier beoordelaars, en die vier langs de
hoofdredacteur. Eén artefact ontsnapt daaraan: **wat de orkestrator zelf naar
`curriculum/` en `conventies/` schrijft bij de vastlegplicht.**

Bij werkitem #146 gingen daar drie fouten doorheen.

| Fout | Gevonden door | Wanneer |
|---|---|---|
| `leerlijn.md`: "vijf vragen waarvan **de vijfde** het stopmoment is" - het is de vierde | drie van de vier beoordelaars van PR #153 | ná de merge |
| Een pad naar een C5 dat nooit is weggeschreven, meegegeven aan de hoofdredacteur | de hoofdredacteur zelf, die het meldde en doorging | tijdens |
| *begrensde herhaling* geschreven waar `leeruitkomsten.md` r83 *lusconstructies* zegt, en doorgevoerd tot in het college | de vakdeskundige | ná de merge |

De derde is de leerzaamste. De bindende laag zei al *lus*; ik schreef *herhaling*
en voerde dat consequent door, tot het materiaal zichzelf tegensprak - `4_opstap`
zei "begrensde `for`-lus", het college zei "begrensde herhaling". **Vier
beoordelaars verklaarden dat criterium gehaald**, want zij toetsten
`begrensd`/`onbegrensd` tegen r83 en vergeleken het zelfstandig naamwoord niet. Een
gemeten criterium, correct uitgevoerd, en het ding zelf niet nagekeken.

**Wat dit níét is.** Het is geen detectieprobleem: alle drie zijn gevangen, drie
van de drie. Het is een tijdigheidsprobleem - twee waren al gemerged, en een besluit
in `curriculum/` is precies het soort tekst waar volgende rollen op gaan staan.

**Waarom de bestaande regel niet volstaat.** *Wie het zelf doet, laat het lezen* staat als
spreuk alleen in `CLAUDE.md`, en is in de tabel van vijftien ingrepen onder *Werk buiten de
lus om* in `metingen.md` **elf van de vijftien keer niet nageleefd**. Dat is bevinding 9 nog
eens: een regel is geen borging.

Hier stonden eerder twee dingen die niet klopten, rechtgezet op 1 oktober 2026 bij de
onderzoeksronde. Er stond *"zeventien van de zeventien keer niet nageleefd"*, met de hele
sectie als bron; nageteld draagt die tabel achttien rijen waarvan drie paren hetzelfde werk
beschrijven, dus vijftien ingrepen, waarvan drie achteraf wél een lezer kregen en bij één de
vraag niet van toepassing is. Het getal staat nu bij de tabel waar het uit komt. Wat de héle
sectie zegt staat hier met opzet niet: dat is een tweede telling over een bron die blijft
groeien, en twee leesronden lang was juist die samenvatting de fout.

En er stond dat de regel *"al in `CLAUDE.md` en in `/orc`"* staat. De spreuk zelf komt in
`.claude/` nergens voor, geijkt op de ene treffer in `CLAUDE.md` - maar de plicht bestaat
daar wél in andere woorden: `.claude/commands/orc.md` laat een door de orkestrator
geschreven besluitdiff onafhankelijk redactioneel toetsen vóór de PR, `loop.md` eist in
§*Buiten een werkitem* een onafhankelijke lezer bij een kleine correctie, en §*GitHub en
registratie* eist een redactionele beoordeling op door de orkestrator geschreven
besluittekst. De scherpte van deze bevinding zit dus niet in een ontbrekende vindplaats, maar
in wat bevinding 9 al zei: die plicht staat er als regel en niet als handeling, en bij de
herschrijving van #203 is de stap die haar wél een handeling maakte teruggezet naar proza.
Rechtzetten zonder dat erbij te zeggen zou van een voorzichtige vaststelling een feit maken,
en daarover gaat een andere bevinding in dit bestand.

En een bevinding hier opschrijven verandert dat niet. Gemeten: van alle
roldefinities verwijzen alleen `vakdeskundige.md` en `onderzoeker.md` naar
`onderzoek/`. **Voor een auteur of beoordelaar bestaat dit document niet.** Wie hier
iets neerzet en denkt dat het daarmee is geborgd, heeft het opgeschreven en niet
geregeld.

**Wat wél werkte, in dezelfde sessie.** Het besluit *Leesvragen mogen fout aflopen*
werd van gevallen naar soort herschreven, landde in `curriculum/uitgangspunten.md`,
en werd in de opdracht van elke rol geplakt. Resultaat: drie van de drie
beoordelaars daarvóór meldden het als defect, nul van de vier daarna. Het verschil
zat niet in het opschrijven - dat stond er al - maar in dat het de rol bereikte op
het moment dat zij handelde.

**Wat het veranderde.** `/orc` heeft een stap **5b** gekregen: schrijft de
orkestrator zelf naar `curriculum/` of `conventies/`, dan gaat die diff langs
`rol-beoordelaar-redacteur` vóórdat de pull request ter merge wordt aangeboden. Als
stap en niet als regel, en met dezelfde motivering die `/orc` al bij de meetregel
gebruikt: *een losse stap wordt overgeslagen omdat het werk dan al af voelt.* De
pull request zonder dat oordeel is een onvolledig artefact.

Of dat werkt is de volgende meting. De meetregel zelf is deze sessie wél elke keer
nageleefd, en dat is de enige aanwijzing dat de vorm klopt. **Nog niet bewezen.**

---

## 15. De orkestrator typt artefacten over in plaats van ze door te geven

*3 september 2026.*

Bij de beoordelingsronde van #168 kreeg elke beoordelaar de kern van C5 doordat de
orkestrator hem **met de hand in vier prompts overtypte**. Daarbij viel het
verplichte veld *Wat dit raakt buiten deze week* weg — in alle vier.

De eerstejaars stopte daarop en gaf geen oordeel, precies zoals het C6-contract
voorschrijft. Zijn onderbouwing waarom dat geen formaliteit was, is het aardigste
deel: hij had tijdens het lezen gezien dat twee van de zes gewijzigde bestanden
geen week 1-materiaal zijn, en dat `projects/picobot.md` nog *toestand* schrijft.
Hij kón niet aannemen dat het veld leeg was, want hij zag bewijs dat het dat niet
was.

**Het veld dekte dat allemaal.** De auteur had `projects/picobot.md` erin staan
met 39 voorkomens, als bekende afwijking met een eigen werkitem. Het gat zat in de
overdracht en niet in de oplevering.

**Dit is het derde geval van dezelfde soort**, alle drie van de orkestrator en alle
drie in dezelfde sessie:

| Wat | Gevolg |
|---|---|
| Een pad naar een C5 dat nooit is weggeschreven (#146) | De hoofdredacteur werkte zonder de oplevering |
| IJkgetallen die practicum plus een buiten-scope bestand bleken (#168) | Een auteur zou 39 voorkomens zoeken in een bestand dat hij niet mag aanraken |
| De kern overgetypt en een verplicht veld afgeknipt (#168) | Vier beoordelaars kregen een onvolledig artefact; één stopte |

Het patroon is telkens hetzelfde: **de orkestrator geeft iets door zonder te
controleren dat het compleet is.** Bevinding 14 ging over wat hij naar
`curriculum/` schrijft; dit gaat over wat hij tússen rollen doorgeeft, en dat is een
groter oppervlak.

**Wat het veranderde.** Nog niets structureels, en dat is de eerlijke stand. De
eerstejaars doet zelf het voorstel dat me het beste lijkt, en het is goedkoper dan
een regel: **geef de kern letterlijk door in plaats van hem over te typen.** Een
artefact hoort naar een bestand te gaan dat de rol leest, niet door een prompt heen
gekopieerd te worden — dat kan `/orc` al ("in de prompt zelf, of in een bestand dat
hij mag lezen"), en het overtypen was de duurdere van de twee opties die de regel
toestaat.

Dat het één keer goed afliep is geen geruststelling maar het tegendeel: het liep
goed af omdat de rol zijn stopvoorwaarde naleefde. Drie andere beoordelaars kregen
hetzelfde onvolledige artefact en **stopten niet**. Zij hadden het veld ook nodig —
twee van hen kwamen in hun oordeel uit bij precies wat erin stond.

**Nog niet opgelost.**

---

## 16. Een werkitem dat conventies wijzigt vindt bij elke ronde een nieuw gat

Werkitem #178 kostte **2.972.571 tokens** over vier auteursrondes en twee volledige
beoordelaarsrondes, en werd afgesloten zonder eindoordeel omdat de vakdeskundige de
lus stopte: *"ik heb het idee dat we wat teveel in cirkeltjes ronddraaien en veel
tijd aan details wordt besteed."* Ter vergelijking: een volledige M kostte bij #182
935.978, en de twee zwaarste L's tot dan 1.204.000 en 2.660.000.

**Het materiaal was na ronde 2 klaar.** Van de elf acceptatiecriteria gingen er tien
over `source/`, en die stonden vanaf commit `6913faae` alle tien op *gehaald* en zijn
daarna niet meer veranderd. Alles daarna - twee auteursrondes, vier beoordelaars, een
hoofdredacteur, twee poortbesluiten van de vakdeskundige - ging over criterium 1, en
criterium 1 gaat niet over het materiaal maar over `conventies/begrippen.md`.

### Waarom dat niet convergeert

Een criterium over `source/` is af te meten: *nul genummerde `Opgave N` buiten de
tentamens* is een getal, en zodra het nul is blijft het nul. Een criterium over een
conventiedocument luidt *"de vier plekken spreken elkaar niet tegen"*, en dat is geen
telling maar een oordeel over een tekst die elke ronde langer wordt. Elke ronde die
een gat dicht, schrijft nieuwe zinnen; elke nieuwe zin is nieuw oppervlak voor de
volgende ronde. Zichtbaar in de opeenvolging:

| Ronde | Blokkade | Waar |
|---|---|---|
| 1 | `technische-conventies.md` schrijft `begrippen.md` een regel toe die daar niet staat | de tekst |
| 3 | `begrippen.md` belegt `Opgave` uitputtend en `Opdracht` in één van drie vormen | de tekst die ronde 3 schreef |
| 4 | *(niet meer beoordeeld)* de docstring van de hook herhaalt nu de regel in plaats van ernaar te verwijzen - dezelfde fout als ronde 1, op de derde plek | de tekst die ronde 4 schreef |

Die derde regel staat er niet omdat een beoordelaar hem vond, maar omdat **de auteur
hem zelf meldde onder *Niet gedane vervolgen***. Het patroon was op dat moment al
zichtbaar voor de rol die het veroorzaakte.

### Twee dingen die dit niet zijn

**Het is geen slecht werk.** Elke gevonden bevinding was juist, en drie ervan waren
scherp: de twintig `Opgave N` in codecommentaar die de hook per constructie niet ziet,
de toetsbare zin die voor vier van de negen uitwerkingsbestanden onwaar was, en de
rechtvaardiging in `technische-conventies.md` die door de eigen ronde-1-ingreep onwaar
was geworden. Zonder de lus was geen daarvan gevonden.

**Het is ook geen kwestie van te strenge beoordelaars.** De weging klopte: bij de
tweede ronde stond het drie keer AKKOORD MET PUNTJES tegen één BLOKKEER, en de
hoofdredacteur hief die tegenspraak op met de juiste grond. Het probleem zit een laag
eerder, in wat het criterium meet.

### Wat dit verandert

**Een acceptatiecriterium over een document in `conventies/` of `curriculum/` hoort
een telling te zijn of een sluitingsvoorwaarde met een eindpunt, niet een oordeel
over de tekst als geheel.** *"De vier plekken spreken elkaar niet tegen"* heeft geen
eindpunt: er is altijd een volgende zin die iets toeschrijft. *"`begrippen.md` noemt
elke in `source/` voorkomende vorm van `Opgave` en `Opdracht` bij naam, met
vindplaats en aantal"* heeft er wel een, want de vormen zijn te tellen.

**En de triage hoort te wegen of een werkitem het bindende document verandert of
alleen het materiaal.** #178 deed allebei, en de triage woog alleen de omvang van het
materiaal (84 koppen, 59 te wijzigen). De 84 koppen kostten één auteursronde. De vier
regels in `begrippen.md` kostten er drie, plus twee beoordelaarsrondes en twee
poortbesluiten.

*Bewijs: `onderzoek/metingen.md`, werkitem #178. Vastgesteld 9 september 2026.*

## 17. Twee agents in één werkboom eten elkaars commits op

Op 11 september 2026 draaide de auteur van #198 in de werkboom terwijl de
orkestrator daar het werk van #196 startte: een nieuwe branch, wijzigingen aan vier
bestanden, een commit en een push. **De eerste commit van de auteur landde daardoor
op de branch van de orkestrator**, met vier bestanden erin die niet van hem waren.

Geen van beiden merkte het op het moment zelf. De orkestrator zag een schone
`git status` en een geslaagde push; de auteur werkte door in een werkboom die onder
hem van branch was gewisseld. **Het kwam pas aan het licht doordat de auteur aan het
eind zijn eigen diff tegen de basiscommit legde** in plaats van te vertrouwen op waar
hij dacht te staan.

### Waarom dit niet opvalt

`git status` is schoon zolang er niets ongecommit is, en een `git checkout -b` van de
ene actor is voor de andere onzichtbaar: hij ziet geen fout, alleen andere bestanden.
De poorten draaien ook gewoon groen, want de inhoud klopt - alleen de *plaats* klopt
niet. **Er is geen enkele controle in deze repo die dit vangt.** De hooks kijken naar
bestanden, niet naar welke branch ze dragen.

### Wat het veranderde

- **Een agent die in de werkboom schrijft, heeft die werkboom exclusief.** Zolang een
  auteursronde draait, start de orkestrator daar geen tweede tak. Werk dat echt
  parallel moet, hoort in een aparte `git worktree`.
- **Een rol die commit, controleert aan het eind zijn eigen diff tegen de basiscommit
  die hij bij de start noteerde.** Dat is wat het hier ving, en het is de enige
  controle die werkte.
- De auteur van #198 heeft beide branches rechtgezet, de vreemde patch bewaard en
  **daarna alle poorten en metingen opnieuw gedraaid**. Dat laatste is het deel dat
  navolging verdient: een hersteloperatie maakt eerdere metingen ongeldig.

*Bewijs: #198, commit `d32a8373` tegenover `a711a28f`; de nameting staat als reactie
op dat issue. Vastgesteld 12 september 2026.*

### Tweede voorval, 2 oktober 2026 - met de regel al op papier

Het gebeurde opnieuw, en nu stond de maatregel hierboven al drie weken opgeschreven.
Tijdens de beoordeling van #351 zette de orkestrator de werkkopie op een andere branch
om de metingen vóór sessie-einde vast te leggen. Daardoor stond `curriculum/` bij de
beoordelaar twee regels korter dan in de commit die hij beoordeelde, en schoven alle
regelnummers onder r37 met twee.

**Wat het ving, is precies de tweede maatregel hierboven.** De redacteur merkte het
aan een regelnummer dat niet meer rijmde, pakte de hele boom van `8411c334` uit met
`git show`, controleerde de md5 tegen het object en draaide zijn volledige
meetbatterij opnieuw; de uitkomsten waren identiek. Hij ankerde dus op de commit in
plaats van op de werkkopie, en dat is wat bij #198 ook als enige werkte.

Het verschil met het eerste voorval is dat er toen geen regel was en nu wel. De eerste
maatregel - *een agent die in de werkboom schrijft, heeft die werkboom exclusief* - is
geschreven voor een auteur die commit, en de orkestrator heeft haar niet op zichzelf
toegepast terwijl een beoordelaar las. Een beoordelaar schrijft niet, maar hij leest
regelnummers, en die zijn even kwetsbaar.

**Wat het veranderde.** De leesronde op de registratie van #346 en #351 draaide in een
eigen `git worktree`, de maatregel die hierboven al stond. Dat werkte: die rol meldde
geen verschuiving. De bredere vraag of elke rol standaard een eigen worktree hoort te
krijgen in plaats van op afspraak, staat als voorstel bij de evaluatie van #203.

*Bewijs: de beoordeling van #351 op PR #357, sectie Afwijking; de registratie in
[metingen.md](metingen.md) bij werkitem #351. Gemeten 2 oktober 2026.*

## 18. Parallelle routes vragen een afhankelijkheids- en boardcontrole

Bij #163, #239 en #237 kwamen drie samenhangproblemen tegelijk aan het licht.

**Een werkitem kan niet alleen worden gelezen.** #239 maakte de week-4-
docentenhandleiding en liet de oude `teacher_guides/4_midterm.docx` staan als bron
voor werkvormen. #237 had een C4 om week-3-docx te verwijderen. Beide keuzes waren
binnen hun eigen route begrijpelijk, maar samen was niet vastgelegd of oude docx na
migratie moeten blijven of uniform verdwijnen. De parent #95 was de plek waar die
regel al hoorde te worden bewaakt. Een C1 moet daarom parent, siblings en relevante
eerder genomen besluiten expliciet meenemen vóór een verwijdering of verplaatsing.

**De Project-status is een procesartefact.** Bij #163 stond de issue nog op
*Triage* terwijl C1b al was gepubliceerd en de ontwerper klaarstond. De issue- en
PR-reacties waren inhoudelijk correct, maar het board gaf een onjuiste processtand.
Het publiceren van C1b, C2, C4, C5 en C6 moet daarom telkens ook de bijbehorende
statusovergang controleren.

**Zoeken op termen is geen volledige inhoudscontrole.** De verkenner vond nul
treffers op `verzamelvariabele`, waarna de beoordelaars nog een ontbrekende lokale
verwijzing bij `in_mset` en een inconsistente linkvorm vonden. Een C5/C6 moet naast
treffers ook een kleine steekproef op paden, links en de betekenis van termen
bevatten. In dezelfde ronde bleek een inventarispad in C1 (`4_python_bat.ipynb`)
niet overeen te komen met het bestaande `.md`-bestand; bronpaden moeten vóór
overdracht worden geverifieerd.

**Wat dit verandert.**

- C1 bevat een afhankelijkheidsoverzicht: parent, siblings, gedeelde bestanden en
  besluiten die de scope raken.
- Elke artefactpublicatie eindigt met een controle van de GitHub Project-status.
- C5/C6 bevatten naast mechanische zoekacties een beperkte inhoudelijke steekproef
  op links, paden en termgebruik.
- Een verwijdering van oud bronmateriaal blijft geblokkeerd totdat de uniforme
  parentbeslissing is vastgelegd.

*Bewijs: #163 (C1b, C2, C5 en C6), #239/#240, #237 en parent #95. Vastgesteld
17 september 2026.*

## Open: welk model per rol

*1 september 2026. Nog niet onderzocht.*

De lus is al een orchestrator-patroon — een coördinator die uitdeelt aan werkers
met een eigen context — maar alle werkers draaien op hetzelfde model. Er is een
derde as naast *welke rollen* en *hoe diep*: **met welk model**.

Een eerste lezing, uitdrukkelijk als hypothese en niet als besluit:

- De **verkenner** doet werk dat te controleren valt: tellen, grepen, vergelijken.
  Bevinding 2 laat zien dat het vaak misgaat, maar ook dat het te ijken is. Dat
  pleit niet tegen een goedkoper model, het pleit voor de ijkregel.
- De **eerstejaars** heeft geen intelligentie nodig maar **naïviteit**. Hij moet
  vastlopen waar een student vastloopt. Een sterker model is daar mogelijk juist
  slechter in.
- De **ontwerper** en de **verhelderaar** doen het tegenovergestelde: alternatieven
  wegen, beperkingen tegelijk vasthouden, zien dat een verificatiemodel niet kan
  draaien.
- **Triage** is één kort besluit dat alle andere kosten bepaalt: goedkoop uit te
  voeren, duur om fout te hebben.

Dit is niet doorgevoerd, en met opzet niet. Er is voor de meeste rollen één
waarneming, en de aanbevolen werkwijze is meten op de eigen taken, vergelijken op
de moeilijkste tien procent, en een schaduwtest draaien voordat je omzet. Wie dit
op redeneren alleen vastlegt in configuratie, heeft een gok die niet meer te
weerleggen is.

## Vervolg op de procesbevindingen: #203

Op 10 september 2026 is een gerichte proceswijziging goedgekeurd. De grond is de
combinatie van herhaalde ontwerprondes (#103), een niet overgedragen menselijk
besluit (#134), de unieke eerstejaarsbevinding (#146) en uitdijend normherstel
(#178). Dit is een vervolg op de bestaande bevindingen, geen nieuwe gemeten
kwaliteitswinst.

De maatregel: relevante besluiten en objectief bewijs in de beoordelingsinvoer,
criteria expliciet toewijzen, gericht herstel met rondelimiet en kleinere routes
waar verantwoordelijkheden gecombineerd kunnen worden. De eerstejaarsblik en
onafhankelijke controle van uitwerkingen blijven apart belegd. Wat wijzigt,
waarop dit rust en wanneer het wordt geëvalueerd staat in
[203-proef.md](203-proef.md). Minder rollen is voorlopig een hypothese; de twee
praktijkproeven moeten nog plaatsvinden.

## 9. De titelhiërarchie staat buiten de buildcontrole

*11 september 2026. Werkitem #205.*

De nieuwe pagina voor Picobot stond onder het hoofdstuk **Uitwerkingen**, maar
had zelf de kop **Uitwerkingen Picobot**. De build, linkcontrole en twee
inhoudelijke beoordelingen signaleerden dit niet. De student zag daardoor een
dubbele titel in de navigatie.

De oorzaak was dat het werkitem navigatie als bereikbaarheid definieerde, niet als
samenhang tussen TOC-kop, paginatitel en eerste kop. De technische controles
controleren verwijzingen en syntax, niet deze zichtbare hiërarchie.

**Wat het veranderde.** De technische conventie vraagt nu om controle van de
gerenderde TOC en paginakoppen. De eerstejaarsbeoordelaar heeft die controle als
expliciete stap gekregen. De concrete correctie in #205 was `Uitwerkingen Picobot`
naar `Picobot`.

## Redactionele selectie en herstel — 14 september 2026

De auteursrol verbood ongenoemd materiaal te laten verdwijnen; de redacteur mocht
alleen op verslechtering blokkeren. Daarmee kon verbeterde maar nog ontoereikende
tekst passeren. [#214](https://github.com/hanze-hbo-ict/programmeren/issues/214)
verduidelijkt selectie door ontwerper/auteur en beoordeling tegen de opdracht en
schrijfwijzer. Besluit, bronbeperking en scenario's: [214-redactie.md](214-redactie.md).

## Transitieve CDN-dependencies — 15 september 2026

De interactieve CodeMirror-editor importeert modules via esm.sh. Een directe
versiepin zet de transitieve graaf niet vast: caret-ranges kunnen verschillende
module-URL's voor `@codemirror/state` opleveren. De browser behandelt die als
verschillende modules, waardoor `instanceof`-controles falen. Werkitem [#221](https://github.com/hanze-hbo-ict/programmeren/issues/221)
zet de state-dependency daarom expliciet vast en controleert de gebouwde editor.

Deze reparatie raakt de CodeMirror-graaf, niet de Pyodide-runtime. De repo blijft
Pyodide `v314.0.7` gebruiken. Vendoring is een afzonderlijke vervolgbeslissing.

### Aanvulling, 16 september 2026: de pin was niet af, en de voor de hand liggende
### reparatie breekt hem opnieuw

De eerste reparatie (`67223e7b`, #222) pinde `@codemirror/state` en haalde de
gemelde fout weg. **Twee randen van de graaf bleven een bereik:** `lang-python`
haalde `@codemirror/language@^6.8.0`, en `commands` en `language` haalden
`@codemirror/view` via een bereik. Dezelfde klasse fout kon dus terugkomen zodra
bovenstrooms een `language`- of `view`-patch verscheen, alleen dan op `Language`
of `ViewPlugin` in plaats van op `State`. `bd59892f` (#226) sluit dat.

**Wat hier te leren valt, en het is niet wat je zou raden.** De voor de hand
liggende reparatie is: geef elke import dezelfde volledige `?deps=`-lijst. Dat
maakt het juist weer stuk. Gemeten op 16 september: met
`state@6.7.4?deps=…,view,language,highlight` serveert esm.sh
`/@codemirror/state@6.7.4/X-ZEB…/es2022/state.mjs`, terwijl `view` en `language`
intern `/@codemirror/state@6.7.4/es2022/state.mjs` importeren. Twee URL's, twee
module-instanties, en het probleem is terug in dezelfde vorm.

**De regel die eruit volgt: een pakket mag zichzelf niet in zijn eigen `deps`
noemen.** Een gedeeld pakket importeer je kaal, of met precies de deps die zijn
afnemers ook gebruiken; wie het anders doet, maakt een derde variant.

**En de controle die dit vaststelt.** Niet "staat de versie in de URL", maar:
haal de URL's uit het bestand zelf op, volg hun eigen imports, en tel de unieke
module-URL's per gedeeld pakket. Alles behalve 1 is fout. Op `bd59892f`:

    1 @codemirror/state     /@codemirror/state@6.7.4/es2022/state.mjs
    1 @codemirror/view      /@codemirror/view@6.43.11/X-ZEB<state>/es2022/view.mjs
    1 @codemirror/language  /@codemirror/language@6.12.4/X-ZEB<state,view,highlight>/es2022/language.mjs
    1 @lezer/highlight      /@lezer/highlight@1.2.3/es2022/highlight.mjs

**Wat het veranderde.** De editor laadt weer; de vakdeskundige heeft dat op
16 september in de browser vastgesteld. En de afweging over vendoren staat er
sterker voor: twee reparaties in twee dagen aan een graaf die wij niet beheren,
en de tweede was nodig omdat de eerste een rand miste die niemand had geteld.


## Een scopegrens hoort niet boven de proportionaliteitsregel te staan — 16 september 2026

**Wat er gebeurde.** Bij #231 droeg de opgave `problems/3_opstap.ipynb` een scheve deelvraag:
opdracht 3 heeft een a, b én c, maar deelvraag d zei *"om je antwoord op a en b te controleren"*.
Eén woord. C0 en het C1 legden de opgave **hard buiten scope**. De auteur hield zich daaraan en
meldde het als niet gedaan vervolg; de onderwijskundige beoordelaar deponeerde het opnieuw als
bevinding buiten het werkitem. De orkestrator schoof het twee keer door naar "een eigen
werkitem", tot de vakdeskundige ingreep: *"had dat niet door een van de rollen aangepakt moeten
worden? de auteur bijv.? ik vind dit slordig."*

**Waarom dit geen incident is.** `CLAUDE.md` draagt twee regels die elkaar hier raken:

- *"Proportionaliteit gaat vóór volledigheid. Een typefout, een dode link of een naam rechtzetten
  doe je gewoon, in een branch met een pull request."*
- en de praktijk dat een C1 de afbakening vastlegt, zodat een werkitem niet uitdijt.

**Drie rollen op rij hebben de tweede boven de eerste gezet**, en alle drie konden zich beroepen
op wat er in hun invoer stond. De auteur mocht de opgave niet aanraken. De beoordelaar had haar
buiten zijn reikwijdte. De orkestrator had de grens zelf geschreven. Niemand deed iets fout
binnen zijn eigen opdracht, en tóch bleef een aantoonbaar foute regel staan die met één woord te
repareren was — en er stond een werkitem klaar om ervoor opgetuigd te worden.

**Wat het veranderde.** Rechtgezet met `8b42a59d`, in dezelfde PR (#234). En de regel die eruit
volgt, voor wie een C1 schrijft:

> **Een scopegrens beschermt tegen uitdijen, niet tegen repareren.** Zij hoort te zeggen wat er
> niet *herzien* wordt, niet dat een aantoonbare fout blijft staan. Noem in de afbakening
> expliciet dat een typefout, een dode verwijzing of een kapotte deelvraag in een buiten-scope
> bestand gewoon wordt rechtgezet, met vermelding in C5 — anders leest de auteur de grens
> letterlijk, en dat is precies wat hij hoort te doen.

Dit hangt samen met wat de vakdeskundige eerder in dezelfde week vroeg: *"niet te veel blijven
hangen bij details en daar enorme issues voor optuigen."* Een werkitem openen voor één woord is
dezelfde fout van de andere kant.

## De beoordelaar krijgt geen C5-kern bij een route zonder ontwerp — 16 september 2026

**Wat er gebeurde.** Twee keer op één dag, in twee verschillende routes, meldde de beoordelaar
ongevraagd hetzelfde: hij had **geen C5-kern ontvangen**. Bij #230 de eerstejaars, bij #231 de
onderwijskundige. Beiden kregen C0, C1 en de repository, en beiden hebben alles zelf gemeten in
plaats van overgenomen.

**Waarom het gebeurt.** `loop.md` geeft de beoordelaar als invoer *"C1-toewijzing + C5-kern"*.
Bij de korte route — auteur en één beoordelaar, zonder verkenner, ontwerper of poort — is de
uitvoeropdracht C0 + C1, en de C5 bestaat pas nadat de auteur klaar is. De orkestrator schreef
de beoordelaarsopdracht op de branch en de criteria en gaf de kern niet door.

**Waarom het toch een gebrek is, in de woorden van de onderwijskundige:**

> *"Voor de volgende ronde hoort dit wel als bestand langs te komen, al was het maar om te kunnen
> zien of auteur en beoordelaar dezelfde getallen meten."*

Hij heeft gelijk, en het bewijs staat in ditzelfde werkitem: het C1 telde *acht* inhoudelijke
deelvragen waar het er zeven zijn. De auteur mat het na en meldde het; de beoordelaar mat het
onafhankelijk na en kwam op hetzelfde. **Twee onafhankelijke metingen van hetzelfde getal is
precies wat een overdracht van de kern zichtbaar maakt** — zonder die kern was het toeval geweest
dat beiden het opmerkten.

Merk ook op wat er níét gebeurde: geen van beide beoordelaars stopte, terwijl het C6-contract
voorschrijft te stoppen bij een ontbrekend verplicht veld. Beiden kozen bewust door te gaan en
meldden de afwijking. Dat is de juiste afweging geweest, maar het betekent dat de norm hier
stilzwijgend niet wordt gevolgd.

**Wat het veranderde.** Nog niets in de instructies; dit is de vastlegging. Voor wie het oplost:
de vraag is niet of de kern mee moet, maar wanneer hij bestaat. Bij een route zonder ontwerp
levert de auteur zijn C5 vóór de beoordeling, dus de kern kán mee — de orkestrator moet hem
alleen doorgeven in plaats van de beoordelaar rechtstreeks op de branch te zetten.

## Een criterium dat dwingt na te tellen, vangt de fout in de opdracht zelf — 17 september 2026

**Wat er gebeurde.** Het ontwerp van #237 leidde een zevende criterium af dat niet in het
werkitem stond: *elk tijdsblok draagt zijn herkomst* — **B** voor een tijd uit de bron van 2023,
**R** voor een richttijd zonder bron — en de verdeling in de verantwoording telt op tot het
aantal blokrijen. De meetregel onder dat ontwerp vatte de drie vastgestelde tabellen samen als
*"24 blokken, 6 om 18"*. Dat getal is overgenomen in het poortbesluit en in de auteursopdracht.

De tabellen bevatten 8 + 8 + 5 = **21** rijen, 6 met **B** en 15 met **R**. De auteur nam de
tabellen ongewijzigd over, telde de verdeling zelf en meldde de afwijking; de beoordelaar telde
onafhankelijk na en kwam op hetzelfde. De auteur ving bovendien een tweede telfout op: het ontwerp
schreef *"Vier uit de bron (45 min)"* waar die vier rijen 5 + 10 + 15 + 20 = 50 minuten zijn.

**Waarom het telt.** Het foute getal stond in drie opeenvolgende artefacten van dezelfde keten —
ontwerp, poort, opdracht. Geen van de drie overschrijvingen kon het vangen, want ze schreven het
getal over in plaats van de tabellen te tellen. Wat het wél ving was een criterium dat de auteur
verplichtte de bron zelf te tellen om eraan te voldoen. **Een criterium dat een getal eist,
controleert de keten die het getal doorgaf.**

**Wat het veranderde.** Dit criterium gaat mee naar de volgende handleidingen. Het is bovendien
de tegenhanger van bevinding 16: criteria over een `conventies/`-document convergeren niet omdat
ze geen eindvoorwaarde hebben; dit criterium convergeert juist omdat het een telling is.

## De reikwijdte uit C1 kan door het poortbesluit worden ingehaald — 17 september 2026

**Wat er gebeurde.** Het C1 van #237 stelde vast dat er geen Sphinx-build nodig was: een
handleiding staat in `handleidingen/` en niet in `source/`, dus de build raakt hem niet. Dat
klopte toen het werd geschreven. Het poortbesluit voegde daarna één opdracht toe die wél een
boekbestand raakte — een kruisverwijzing in `source/lectures/3a_functies.ipynb` — en daarmee
vraagt `CLAUDE.md` de build alsnog. Auteur en beoordelaar draaiden hem allebei uit zichzelf, en
hij was groen.

**Waarom het gebeurt.** De reikwijdte wordt vastgesteld vóór het menselijke besluit, en een
poortbesluit mag de afbakening veranderen. Dat is niet fout — het is waarvoor de poort bestaat —
maar het maakt de controles uit C1 een momentopname.

**Wat het veranderde.** Nog niets in de instructies. Voor wie het oplost: de goedkoopste vorm is
dat het C4 de reikwijdte opnieuw noemt zodra het de afbakening aanpast, in plaats van de
orkestrator te laten onthouden dat C1 is ingehaald.

## Een tekstvervanging die code in proza raakt, breekt de structuur van de pagina — 18 september 2026

**Wat er gebeurde.** In `source/problems/2_extra.ipynb` is `from math import *` vervangen door
`from math import sqrt, factorial` plus een toelichtende comment op een eigen regel. De
vervanging raakte drie plekken: de codecel, het `python`-blok in de markdown, en een **inline
code-span in lopende tekst**. Op de eerste twee hoort de comment thuis. Op de derde kwam er een
regeleinde in een code-span, en de tweede regel begint met `#` in kolom 0. Blokken worden vóór
inline-elementen geparseerd en een ATX-kop mag een alinea onderbreken, dus MyST maakte er een
kop van. De gebouwde pagina droeg twee `<h1>`: "Extra", en
``Vooruitwijzing: deze functies komen in week 3 aan bod` zorgt dat deze module beschikbaar is in de code``.

Het stond ruim een dag op de pagina van de lopende week en is door de vakdeskundige gezien, niet
door een controle.

**Waarom geen enkele poort het ving.** Een tweede `<h1>` is geldige HTML en geldige MyST; de
build waarschuwt niet. De hooks kijken naar celtags, kopwoorden en Python-syntaxis, niet naar
documentstructuur. En de menselijke controle keek of de code draaide — dat deed ze — niet of de
zin eromheen nog klopte. Vergelijk bevinding 9: de titelhiërarchie staat buiten de buildcontrole.

**Wat het veranderde.** Herstel in PR #249. De les is smal en bruikbaar: **code in lopende tekst
is een citaat, geen code.** Wie een codefragment repo-breed vervangt, controleert apart waar dat
fragment in proza voorkomt — daar mag er geen regeleinde bij, en een comment hoort er niet.

## Een melding over werk dat je in dezelfde PR uitvoert, veroudert binnen die PR — 23 september 2026

**Wat er gebeurde.** Bij #256 hernoemde de auteur een kop in `curriculum/uitgangspunten.md`
van *Drie* naar *Vier erkende afwijkingen*. Dat maakte een citaat in `handleidingen/week_3.md`
stil dood. Hij meldde dat netjes onder *Wat er nog loopt* in de handleiding die hij schreef,
met de reden dat het buiten de afbakening viel. De orkestrator vond de melding terecht maar
de conclusie niet, en repareerde het citaat alsnog in dezelfde PR - **zonder de melding weg
te halen**. De melding stond in `6a76797c` (`week_4.md`), de reparatie kwam in `a9b9954c`
(`week_3.md`); de opgeleverde tekst vertelde de volgende lezer dus dat er werk lag dat
een latere commit in dezelfde PR al had gedaan. De beoordelaar ving het als moet-punt.

**Waarom dit een patroon is en geen slordigheid.** Een handleiding draagt een subsectie
*Wat er nog loopt*: een momentopname van de repository, geschreven door de rol die het
eerst ziet. Wie daarna in dezelfde PR meer doet dan de afbakening voorzag - en dat is
precies wat de proportionaliteitsregel aanmoedigt - maakt die momentopname onwaar zonder
er langs te komen. Het is dezelfde soort fout als de dode kruisverwijzing uit #252, maar
met een kortere lus: de veroorzaker en de gedupeerde tekst zitten in één commit.

**Wat het veranderde.** Hersteld in `cb1d830f`. De regel die eruit volgt is smal en goed
te onthouden: **repareer je iets wat elders als openstaand gemeld staat, zoek die melding
dan op voordat je commit.** `grep` op het onderwerp van je reparatie is genoeg; in dit
geval gaf `grep -rn "Drie erkende afwijkingen"` precies één treffer, en dat was de melding.

## Een keuzeoptie van de orkestrator wordt de onderbouwing van de mens - 23 september 2026

**Wat er gebeurde.** Bij #267 legde de orkestrator de open vragen voor als meerkeuze-opties.
Onder elke optie stond een korte toelichting. De vakdeskundige koos een optie, en het C4
registreerde wat bij die optie stond. Twee keer was dat geen feit maar een onderbouwing
die de orkestrator had geschreven:
- De reden voor de term: "*compositie* is de gangbare term; ... aggregatie voegt in week 5
  niets toe". Die staat nu als reden van de vakdeskundige in `curriculum/leerlijn.md`.
- De status van de registerrij: "geen heropenvoorwaarde, net als bij de meeste didactische
  rijen". In de C4-aanvulling werd dat "zo gaat het ook bij de andere gesloten didactische
  rijen". De verse redacteur in herstelmodus toonde aan dat dit maar half klopt. Vier oudere
  gesloten didactische besluiten hebben wel een heropenvoorwaarde (`uitgangspunten.md` r272,
  r507, r720, r901).

**Waarom dit een patroon is.** Het C4-contract verbiedt "nieuwe inhoudelijke rechtvaardiging
namens hem". Een meerkeuzevraag omzeilt dat verbod zonder dat iemand het merkt. De mens
kiest, dus het klinkt als zijn besluit. Maar de woorden en de feitelijke claim erin komen
van de orkestrator, en niemand heeft die claim gemeten. De vraag was juist gesteld omdat
de orkestrator de reden niet zelf mocht invullen.

**Wat het veranderde.** Er staat een correctie op #267 ([reactie](https://github.com/hanze-hbo-ict/programmeren/issues/267#issuecomment-5802736725)).
De regel die eruit volgt, en die nog niet in `/orc` is vastgelegd: **een optie beschrijft
gevolgen, geen redenen; een feitelijke claim in een optie is gemeten, anders staat hij er
niet.** Vraag de reden open, of zet in het C4 dat de formulering van de orkestrator is en
door de mens is gekozen. Of dit in de instructies komt, is een procesbesluit voor de
vakdeskundige.

## Een hervatte agent meldt zijn tokens als lopend totaal — 23 september 2026

**Wat er gebeurde.** Bij #273 kreeg de auteur na zijn oplevering twee gerichte opdrachten in
dezelfde context: de volgorde van `8b` en daarna de puntjes. De harness meldde achtereenvolgens
179.339, 220.224 en 244.873 tokens. Het getal loopt op, ook na een stap met 13 toolaanroepen. Het
lijkt dus het lopende totaal van de agent te zijn en niet het verbruik van die ene stap. Uit de
melding zelf is dat niet vast te stellen.

**Waarom het ertoe doet.** De proef van #203 vergelijkt tokens per werkitem met een referentie.
Wie de drie getallen optelt, rekent de eerste oplevering drie keer mee. Wie alleen het laatste
neemt, gaat ervan uit dat het een totaal is, en dat is niet bewezen. Juist de goedkope route die
`loop.md` aanbeveelt, *dezelfde auteurscontext mag blijven*, maakt de meting dus dubbelzinnig.

**Wat het veranderde.** In [metingen.md](metingen.md) staan de hervatte stappen bij #273 als
*niet vastgesteld*, met het gemelde getal ernaast, en ze tellen niet mee in het totaal. Voor de
proeven van #203 moet de meetdefinitie vooraf zeggen of een hervatte agent als één run met zijn
laatste getal telt. Dat hoort de vakdeskundige vast te stellen bij de keuze van de referentie.

**Tweede waarneming, dezelfde route.** De mens koos in het poortbesluit het alternatief (grens B)
in plaats van de aanbeveling. De orkestrator schreef de gevolgen ervan zelf over in het C4 en
formuleerde er één onnauwkeurig: *E en F wisselen*. Dat gaf een volgorde die de sets tussen het
model en het genereren zette. De auteur meldde het als afwijking, en de correctie kostte een
hervatte auteursstap en een tweede menselijke vraag. Bij een gekozen alternatief is een
ontwerpherstel duurder, maar het overschrijven laat de ontwerpverantwoordelijkheid stil bij
de orkestrator. Leg in dat geval de concrete eindvolgorde zelf aan de mens voor, niet een
bewerking op een volgorde.

## Een herstelopdracht mag een gevonden defect niet uit de blokkades definiëren — 23 september 2026

**Wat er gebeurde.** In de herstelronde van #160 (PR #264) gaf de orkestrator beide verse
beoordelaars deze instructie mee: "Nieuwe echte defecten die de reparatie introduceert,
meld je als blokkade; overige nieuwe dingen zijn puntjes." De opdracht zelf staat niet op
GitHub; de aanhaling komt van de orkestrator die haar schreef. Beide beoordelaars vonden
vervolgens een echt defect dat al in de eerste oplevering zat. Basisstap 12 blijft eindeloos
lopen bij een deel van de correcte oplossingen: 7 van 16 varianten bij de eerstejaars, 1 van 4
bij de onderwijskundige. De student ziet dan niets.

Beide meldden het als puntje, maar met een verschillende reden. De eerstejaars noemde het een
"zwaarwegend puntje" en schreef erbij dat het naar de maatstaf van C6 een blokkade zou zijn.
Hij volgde de opdracht, legde het punt expliciet aan de mens voor en benoemde de spanning met
het contract. De onderwijskundige noemde de instructie niet en gaf een inhoudelijke reden:
"de hint van stap 10 stuurt naar `while self_copy.is_before(d2_copy)`". Alleen bij de eerstejaars is
de instructie dus aantoonbaar de reden voor de classificatie.

**Waarom het ertoe doet.** `loop.md` zegt: "Nieuwe echte defecten blijven zichtbaar; een
budget maakt ze niet groen." De instructie ging een stap verder dan herstelmodus vraagt.
Herstelmodus beperkt *wat opnieuw onderzocht wordt*, maar niet *hoe een gevonden defect wordt
geclassificeerd*. De orkestrator wist dat de ronde de laatste was, en de formulering maakte
een groen oordeel makkelijker dan de bevinding rechtvaardigde. De C7 heeft het rechtgezet: het
oordeel bleef AKKOORD MET PUNTJES, maar P1 werd apart van de overige puntjes als open defect
aan de mens voorgelegd.

**Waarom ronde 0 het niet zag.** De eerste blokkade (B1) ging erover dat de tekst één uitvoer
als feit stelde. Om te toetsen of de reparatie voor elke oplossing klopte, draaiden de
beoordelaars in de herstelronde veel meer studentvarianten: 16 en 4, tegen twee per
beoordelaar in ronde 0. Pas die bredere steekproef liet de varianten zien die niet eindigen.
De reparatie van de ene bevinding zocht dus de ruimte af waarin de volgende lag. Dat is geen
fout van ronde 0, maar het laat zien dat "eerder vastgesteld" voor naburige onderdelen minder
zegt dan het lijkt.

**Wat het veranderde.** De vakdeskundige besliste over P1: accepteren, vervolg in #265. Over
de herstelopdracht zelf is niets besloten. Wat eruit volgt, is een afleiding en geen bestaande
formulering. Herstelmodus in `loop.md` en in `C6-beoordeling.md` beperkt wat de beoordelaar
opnieuw toetst. `loop.md` zegt verderop dat nieuwe echte defecten zichtbaar blijven, en
C6 *Herstelmodus* dat een nieuwe echte blokkade zichtbaar blijft. Een
herstelopdracht die de classificatie van gevonden defecten zelf voorschrijft, gaat daartegenin.
`/orc` en `loop.md` zijn niet aangepast. Of de herstelopdracht in `/orc` een vaste formulering
krijgt, is een procesbesluit voor de vakdeskundige.

## Een bevinding opschrijven voorkomt haar niet — 24 september 2026

**Wat er gebeurde.** Op 23 september legde de orkestrator vast: *een melding over
werk dat je in dezelfde PR uitvoert, veroudert binnen die PR* (#256), met de
regel *zoek die melding op voordat je commit*. Op 23 september 's avonds, bij #280 (`8eedf9aa`), zette
dezelfde orkestrator de `.docx`-meldingen in week 3, 4 en 5 recht en liet in
`handleidingen/week_6.md` de zin staan dat ze níét waren rechtgezet. De
beoordelaar ving het. Bij het volgende herstel ging het bijna een derde keer mis (zie het commitbericht van `b0169ec8`);
toen was het de orkestrator zelf die er op het laatste moment aan dacht.

**Waarom dit een patroon is.** De bevinding stond in `onderzoek/`, dat de
orkestrator niet leest vóór een commit. Een regel die op het moment van handelen
niet voor ogen staat, werkt niet, ook niet bij wie hem schreef.

**En een tweede, in dezelfde ronde.** De vakdeskundige zei *"mogen weg"*; de
orkestrator schreef *"gaat weg"* en verklaarde een categorie materiaal al
afgeschreven, terwijl de poort had gezegd dat per map zou worden voorgelegd. De
hooks waren groen. Alleen een lezer die de tekst naast het besluit legde, zag het.
De orkestrator had de PR al ter merge aangeboden; de vakdeskundige vroeg
*"alles checks/rollen hebben het bekeken?"* (in het gesprek met de orkestrator,
niet op GitHub), en pas daarop kwam die lezer.

**Wat het veranderde.** Nog niets in de instructies; beide punten gaan als
voorstel naar de volgende procesronde (#203):
- **een vaste controle vóór elke commit van de orkestrator**: `grep` op het
  onderwerp van de reparatie, over `handleidingen/`, `curriculum/` en `conventies/`;
- **geen merge van een PR met orkestratorcommits die geen rol heeft gezien**,
  ook niet als de vakdeskundige erom vraagt - de vraag *"alles checks/rollen hebben
  het bekeken?"* hoort de orkestrator zelf te stellen, niet de vakdeskundige.

## Een getal dat de orkestrator opschrijft, heeft hij niet altijd geteld - 24 september 2026

**Wat er gebeurde.** Na #268 schreef de orkestrator twee korte vastleggingen. In beide stond een
getal dat hij niet had geteld. Een verse redacteur gaf daarop in beide gevallen BLOKKEER:
- **PR #286**, de metingen van #268. Er stond: *"De mens besliste na het C7 twee keer."* Het
  waren er vier, als je de merge meetelt: de plaats van opdracht 3, het verwerken van de puntjes,
  de bijzin en de merge. De bijzin stond in de lijdende vorm, alsof hij vanzelf kwam. Zie de
  [reviews op PR #286](https://github.com/hanze-hbo-ict/programmeren/pull/286).
- **PR #287**, de correctie van `make clean`. Volgens de tekst hoorden de 15 meldingen *Using
  cached notebook* per build bij *"ID 3 en 4"*. De logs tonen drie cacheposten: per build 12
  meldingen voor ID 4, 2 voor ID 3 en 1 voor ID 21. De orkestrator had de ID's overgenomen uit de eerste acht regels
  van `grep -B1 'Using cached notebook'`, zonder ze met `grep | sort | uniq -c` te tellen. Dat
  is zijn eigen verklaring; op GitHub staat alleen de latere telling in de herstelbijlage. Zie
  de [reviews op PR #287](https://github.com/hanze-hbo-ict/programmeren/pull/287).

In dezelfde sessie noemde de orkestrator in een taakprompt ook een basiscommit (*"4a…"*) die
niet bestond. De beoordelaar merkte het op; het oordeel veranderde er niet door.

En toen deze bevinding zelf de eerste keer werd beoordeeld, stonden er weer twee onjuiste
beweringen in. Er stond *"de 15 gedeelde cacheposten"*, maar het waren 15 meldingen en drie
cacheposten. En er stond dat de nalezing van #287 nog niet in de instructies stond. Zie de
[review op PR #288](https://github.com/hanze-hbo-ict/programmeren/pull/288).

**Waarom dit een patroon is.** `CLAUDE.md` zegt *meet het ding zelf*. De getallen hierboven zijn
geen beweringen over het materiaal. Ze staan in het verslag van de orkestrator zelf. Het
vermoeden is dat zulke getallen als samenvatting voelen en niet als meting, zodat ze uit een
uitsnede of uit het geheugen worden overgenomen. Dat vermoeden is niet gemeten. De fout hoort in
dezelfde rij als eerdere orkestratortekst die niet naast de bron werd gelegd:
- *"gaat weg"*, waar de vakdeskundige bij #280 *"mogen weg"* zei;
- *"E en F wisselen"* bij #273;
- de keuzeoptie bij #267.

Dat staat in de bevindingen over #267 en #273 (beide 23 september) en over #280 (24 september)
hierboven.

**Wat er gebeurde met de nalezing.** Beide PR's gingen naar een verse redacteur voordat ze ter
merge werden aangeboden. Voor #287 was dat geen keuze: `loop.md` (*Buiten een werkitem*) vraagt
bij een kleine correctie buiten de lus al om *"een onafhankelijke lezer"*. Die regel stond er
ook al toen de vorige bevinding haar tweede voorstel deed. Voor #286, de metingen van een
werkitem, staat er geen regel. `loop.md` (*GitHub en registratie*) en `orc.md` vragen alleen bij
een besluittekst om een onafhankelijke redactionele toets. Daar vroeg de orkestrator zelf om de nalezing, zonder verzoek van de
vakdeskundige.

De vier nalezingen kostten samen 109.744 tokens voor #286 (75.623 eerste beoordeling, 34.121
herstelbeoordeling) en 67.900 voor #287 (40.834 en 27.066). Daarin zitten niet de afgebroken
eerste run op #286, die door de sessielimiet stopte en geen telling heeft, en het herstelwerk van
de orkestrator. Dit rust op één sessie.

**Wat het veranderde.** De blokkades zijn hersteld in PR #286, #287 en #288. In de instructies is
niets veranderd. Er gaan twee voorstellen naar de volgende procesronde (#203):
- **Een getal in orkestratortekst komt met de opdracht die het opleverde**, in de herstelbijlage
  of in de PR-beschrijving. Een getal zonder die opdracht is niet gemeten.
- **Breid de lezerregel uit `loop.md` uit tot alle orkestratortekst**, dus ook tot de metingen en
  bevindingen van een werkitem. Nu geldt ze alleen buiten een werkitem en bij een besluitdiff.
  Dat past het tweede voorstel van de vorige bevinding aan, omdat een deel ervan al vastlag.

## Een zoekpatroon uit bekende formuleringen vindt alleen bekende formuleringen - 24 september 2026

**Wat er gebeurde.** Bij #270 vroeg de vakdeskundige de omschrijving van duck typing in
`conventies/begrippen.md` te laten aansluiten op het materiaal: "methoden en attributen" in plaats
van "de aangeroepen methoden". De orkestrator zocht de plekken met de formuleringen die hij al
kende en trok er zeven gelijk (commit `6b06cadb`). De verplichte redactionele lezing van die diff
vond een achtste: `source/course/week_13.md` r17-18, *"omdat het de methoden heeft die worden
aangeroepen"*. Dat is de weekpagina, de eerste plek waar de student het begrip leest. De redacteur
vond de zin niet met een patroon maar met een brede zoektocht op "duck", en schreef over zijn eigen
patroon: *"Mijn patroon vond in `669c1fe7` de 7 bekende gevallen en er blijven er nu 0 over, dus
het patroon ving alleen de formuleringen die ik al kende."*

**Waarom het ertoe doet.** De regel in `CLAUDE.md` luidt: *ijk elk patroon op een bekend getal
voordat je een nul vertrouwt*. Die ijking bewijst dat het patroon werkt. Ze bewijst niet dat het
patroon alles vangt. Een patroon dat uit de bekende gevallen is opgebouwd, haalt zijn ijking
altijd, en daarom is de nul erna geen bewijs van volledigheid. Bij het gelijktrekken van een term
draait het om volledigheid.

**Wat het veranderde.** De weekpagina is hersteld in `6a45a921`, en een verse redacteur heeft de
reparatie gelezen. De regel *wie het zelf doet, laat het lezen* ving hier een echt defect in
orkestratortekst, en dat was de reden om hem te volgen. In de instructies is niets veranderd.
Voorstel voor de volgende procesronde (#203): **zoek bij het gelijktrekken van een term op de term
zelf** (hier "duck"), en beoordeel elke treffer. Zoek niet alleen op de oude formulering. Een
patroon op de oude formulering meet hoeveel gevallen er over zijn, niet hoeveel er waren.

## Een agent die op de sessielimiet stopt, levert zijn verbruik niet af - 24 september 2026

**Wat er gebeurde.** Bij #270 leverde de hervatte auteur zijn herstel volledig af: een
herstelbijlage, de bijgewerkte C5-kern en commit `669c1fe7`. Daarna stopte hij op de sessielimiet
(HTTP 429). De taakmelding van de harness aan de orkestrator had de status *failed*, request-ID
`req_011CfNLibVDp2Xev4pRA5LjP`, en geen `subagent_tokens`. Van de agentstap die bij de L-proef het meest onzeker was, ontbreekt zo
het verbruik.

**Waarom het ertoe doet.** De budgetreactie uit [203-proef.md](203-proef.md) hangt af van een
cumulatieve stand na elke agentstap. Door deze ene ontbrekende melding kon de herziene grens van
1.250.000 niet worden getoetst. De proef eindigt daardoor op *niet vast te stellen* in plaats van
op een getal. Er speelde nog iets mee. De bevinding *Een hervatte agent meldt zijn tokens als lopend
totaal* (23 september) vroeg al om vooraf vast te leggen hoe een hervatte agent telt. Die afspraak is bij de start van #270 niet gemaakt.
Dat had hier niets uitgemaakt, want er kwam geen getal. Maar het is de tweede keer dat de
hervatte auteur de meting van een werkitem onzeker maakt. De eerste keer was #273, dat geen
proef was.

**Wat het veranderde.** In [metingen.md](metingen.md) staat de stap als *niet beschikbaar*, en in
de uitkomst van proef 2 staat het totaal als *1.119.651 plus het onbekende auteursherstel*. Er is
niet geschat. In de instructies is niets veranderd. Voorstel voor de evaluatie van #203: **leg de
telling van een hervatte agent vast bij de keuze van de referentie** (de bevinding over het
lopende totaal), en **noteer bij een melding zonder verbruik vóór de volgende agentstart dat de
budgetcontrole vervalt**, zodat de mens weet dat hij zonder stand beslist.

## De auteur schrijft een reden bij het besluit - 25 september 2026

**Wat er gebeurde.** Bij #271 legde de auteur de besluiten van de poort vast in `curriculum/`
(O7a), zoals het C4 vroeg. Twee keer schreef de auteur daarbij een reden die de vakdeskundige niet
had gegeven:
- In `curriculum/practicum-oop.md`, onder *"Bij de poort van #271 is besloten"*, bij VP5: *"dat
  spreekt elkaar niet tegen, want bij een lijst veranderen `+` en `-` niets en mag `+=` het object
  veranderen"*. Die reden was ook onjuist, want een lijst heeft geen `-`. De onderwijskundige
  blokkeerde de oplevering erop. Het was de enige blokkade.
- In `curriculum/leerlijn.md`, bij het besluit *"Ja, ook in de opstap"*, geschreven in de
  herstelronde: *"zodat de opstap de nieuwe syntaxis van de week draagt"*. Deze reden klopt wel,
  want ze volgt uit een bestaande regel. De onderwijskundige in herstelmodus noemde het een
  puntje, *"hetzelfde soort toevoeging als bij B1"*.

De tweede keer gebeurde het in dezelfde auteurscontext, nadat de herstelopdracht de eerste keer
letterlijk had benoemd.

**Waarom dit een patroon is.** De bevinding *Een keuzeoptie van de orkestrator wordt de
onderbouwing van de mens* (23 september) beschrijft hetzelfde bij de orkestrator, die een reden
in een optie zet. Hier doet de auteur het, bij het vastleggen. Het C4-contract verbiedt
"nieuwe inhoudelijke rechtvaardiging namens hem" voor wie het C4 schrijft. Voor wie het C4 later
in `curriculum/` uitschrijft, staat dat verbod nergens. Een besluittekst zonder reden leest
kaal, dus de schrijver vult er een aan. Het gevaar zit in de plek: een zin onder *"is besloten"*
leest als het woord van de vakdeskundige.

**Wat het veranderde.** Beide zinnen zijn in PR #304 aangepast. De eerste keer ving de
onderwijskundige het, omdat het C1 van #271 (*"de onderwijskundige dekt ook ... de besluitdiffs in
`curriculum/` en `conventies/`, getoetst tegen het C4"*) en het C4 die toets aan de beoordeling
toevoegden. Dat was een keuze voor dit werkitem, geen vaste regel: `loop.md` (*GitHub en
registratie*) schrijft de onafhankelijke redactionele toets alleen voor bij een besluittekst die
de orkestrator schrijft. Een besluittekst van de auteur valt daar niet onder. De opdracht aan de
auteur verbood het niet, en een benoeming in de herstelopdracht voorkwam de tweede keer niet.

Voorstel voor de instructies, een procesbesluit voor de vakdeskundige: **zet in de auteursrol bij
het vastleggen van een besluit dat alleen het letterlijke besluit en zijn datum worden
vastgelegd. Een reden alleen als de vakdeskundige die gaf, en dan als citaat.** Daarbij hoort
de vraag of de regel in `loop.md` over de redactionele toets van besluittekst ook moet gelden
voor besluittekst die de auteur schrijft. Nu noemt die regel alleen de orkestrator.

**Tweede waarneming, bij een bestaande bevinding.** *Een agent die op de sessielimiet stopt,
levert zijn verbruik niet af* (24 september) gebeurde opnieuw. De eerste auteursrun van #271
stopte op HTTP 429 zonder verbruiksmelding. Dit keer is de context hervat, en die meldde
daarna een getal. Of dat getal het afgebroken deel bevat, is uit de melding niet af te leiden.
Het staat in [metingen.md](metingen.md) met dat voorbehoud.

## De auteur maakt van een voorzichtige reden een feit - 30 september 2026

**Wat er gebeurde.** Bij #326 legde de auteur het poortbesluit over dubbele `for`-clausules vast in
`curriculum/leerlijn.md`: *"komen niet in de week, want die zijn altijd als geneste comprehension
te schrijven"*. De vakdeskundige had gezegd: *"Dubbele for hoeft niet (dat kan denk ik altijd
geschreven worden als een geneste lc)"*. De auteur maakte van dat *denk ik* een feit, en dat feit
is onjuist: `[x for r in m for x in r]` geeft een platte lijst, `[[x for x in r] for r in m]` een
lijst van lijsten. De onderwijskundige blokkeerde de oplevering erop (PR #330, B1). Het was de
enige blokkade, net als bij #271.

**Waarom dit de bevinding van 25 september bevestigt.** *De auteur schrijft een reden bij het
besluit* beschreef twee gevallen bij #271, waarvan één onjuist. Hier gebeurt het een derde keer,
in een variant: de reden kwam van de vakdeskundige, maar de voorzichtigheid verdween. Het C4 van
#326 citeerde het besluit letterlijk. Het zei er niet bij dat alleen het citaat mag worden
vastgelegd. Het voorstel van 25 september (in de auteursrol: alleen het letterlijke besluit met
datum, en een reden alleen als citaat) is nog niet in de instructies opgenomen.

**Wat het veranderde.** In het herstel (`62e597f`) staat nu het citaat met bron. Omdat het C2 (AC12)
en het C4 de toets tegen de besluiten aan de onderwijskundige gaven, werd het gevangen. Dat is opnieuw een
keuze per werkitem, geen vaste regel. Het voorstel van 25 september ligt er dus met drie gevallen
in plaats van twee. Het is een procesbesluit voor de vakdeskundige.

## De bestaande meetpraktijk voor een hervatte agent werd niet geraadpleegd - 30 september 2026

**Wat er gebeurde.** Bij #326 werden twee agents hervat: de ontwerper voor zijn herstel en de
auteur voor het zijne. De orkestrator noteerde op GitHub steeds twee lezingen: het gemelde getal
als verbruik van de stap, of het verschil met de vorige melding. Hij deed dat zonder te weten dat
de vraag al in [bevindingen.md](bevindingen.md) stond. *Een hervatte agent meldt zijn tokens als
lopend totaal* (23 september) beschrijft hetzelfde bij #273 en houdt het lopende totaal
voor aannemelijk (*"Het lijkt dus"*), maar *"uit de melding zelf ... niet vast te stellen"*. De meetdefinitie hoort de
vakdeskundige vast te stellen. [metingen.md](metingen.md) rekent sinds #271 met het verschil, met
dat voorbehoud erbij. Ook bij #326 liep het getal op na weinig toolaanroepen: 140.027 → 157.171
na 8 aanroepen, en 422.605 → 440.576 na 13. Dat steunt het vermoeden, maar bewijst het niet.

**Nog een keer hetzelfde, in de eerste versie van deze bevinding.** De orkestrator schreef eerst
dat de bevinding van 23 september dat lopende totaal al had vastgesteld (*"had dat al
vastgesteld"*), en liet de hoge lezing
in metingen.md *vervallen*. Daarmee maakte hij van een voorzichtige uitspraak een feit, en nam hij
een meetkeuze die bij de vakdeskundige ligt. Dat is het patroon van de bevinding hierboven, nu bij
de orkestrator zelf. Een redactionele lezing van de orkestratordiff, die de orkestrator liet uitvoeren volgens de
regel *wie het zelf doet, laat het lezen*, ving het (PR #330).

**Waarom het ertoe doet.** Dit volgt het patroon van *Een bevinding opschrijven voorkomt haar
niet* (24 september): de bevinding en de praktijk stonden er, maar de orkestrator raadpleegde ze
niet op het moment dat het ertoe deed. Er was geen budgetgrens, dus er is op de telling geen
besluit genomen. In een proef van #203 hangt de budgetreactie wel aan de telling, en dan beslist
de lezing welke stand de mens krijgt voorgelegd.

**Wat het veranderde.** In [metingen.md](metingen.md) telt #326 zoals #271: het verschil tussen
twee meldingen, met het voorbehoud, en met de hoge lezing ernaast. In de instructies is niets
veranderd. Het voorstel van 23 en 24 september staat nog open: leg de telling van een hervatte
agent vast in de meetdefinitie. Aanvullend voorstel voor de evaluatie van #203: laat `/orc` bij
de start de bevindingen over het meten raadplegen.

**Twee kleinere waarnemingen uit hetzelfde werkitem.**
- *De orkestrator vroeg rollen zonder schrijfgereedschap om een bestand te schrijven.* De
  verhelderaar en de beoordelaars hebben alleen lees- en zoekgereedschap. Het eerste C3 kwam
  daarom als tekst terug, met de melding dat het pad niet te schrijven was. De orkestrator zette
  het letterlijk neer. Latere opdrachten vroegen om tekst. Dat kost niets, maar een opdracht die
  niet uitvoerbaar is, zet een rol aan het improviseren.
- *Een zoekpatroon met een uitgesloten tekenklasse miste een treffer.* Voor #328 zocht de
  orkestrator comprehensions met `[^\[\]{}()]` tussen haakje en `for`. De list comprehension
  `[pixel[:] for pixel in brede_regel]` in `solutions/6_extra.ipynb` r80 viel daardoor weg,
  terwijl de ijking op een eenvoudige comprehension slaagde. De AST-scan van de auteur vond hem wel.
  Dit is een variant van *Een zoekpatroon uit bekende formuleringen vindt alleen bekende
  formuleringen* (24 september): de ijking bewijst dat het patroon werkt, niet dat het alles
  vangt. De issue #328 is aangevuld.

## Een besluit naar de letter uitgevoerd - 30 september 2026

**Wat er gebeurde.**
- Bij #332 was werkcollege stap 3 (`has_extension`) inhoudelijk opgave 1 van het oefententamen.
  De onderwijskundige zag dat bij het lezen (C6, puntje 1). De vakdeskundige besliste: *"Stap 3
  een andere functie geven."*
- De auteur schreef `same_extension`. Dat is een andere functie met een andere naam en andere
  argumenten, maar in hetzelfde domein, met dezelfde `.exe`-context en drie van de vier takken
  gelijk.
- De verse beoordelaar in herstelmodus vergeleek beide functies op 40 invoeren. Ze vielen op 39
  samen. De beoordelaar noemde dat een puntje voor de vakdeskundige: *"Aan de letter van het besluit is
  voldaan. Of het ook aan de bedoeling voldoet, is een oordeel van de vakdeskundige, en ik heb de afweging niet opnieuw
  gemaakt."*
- De vakdeskundige besliste: *"Nee, verder weg van het tentamen."*

**Waarom het ertoe doet.**
- Het is één geval. Een kort besluit liet hier ruimte, en de uitvoering bleef dicht bij het
  bestaande.
- Het lijkt op *De auteur maakt van een voorzichtige reden een feit* (30 september). Daar werd de
  reden van een besluit te stellig; hier werd het besluit smal uitgevoerd.
- De beoordelaar legde een getal naast de eigen lezing: het aantal invoeren waarop de twee functies
  samenvallen. Of dat getal het besluit van de vakdeskundige droeg, staat nergens.

**Wat het veranderde.**
- De vervolgopdracht gaf het besluit een meetbare vorm: stap 3 buiten het domein van extensies,
  met een gemeten vergelijking met `check_extension` in de C5.
- De nieuwe `safe_name` valt bij een echte extensie op hoogstens 14 van de 40 invoeren samen. Een
  tussenversie die op 37/40 uitkwam, verwierp de auteur zelf.
- Wat de vervolgronde kostte, staat in [metingen.md](metingen.md) onder *Werkitem #332*, met het
  voorbehoud over de telling van een hervatte agent.
- In de instructies is niets veranderd. **Voorstel** voor de evaluatie van #203: geef een
  besluit dat een verschil vraagt ("anders dan", "verder weg van") in de opdracht aan de auteur
  een meetbare eindvoorwaarde mee. Laat de auteur die eindvoorwaarde zelf meten, en de
  beoordelaar natrekken.

## Drie bekende patronen keerden terug bij #332 - 30 september 2026

Drie bestaande bevindingen gebeurden bij #332 opnieuw. De bevindingen stonden er al; ze hebben
de herhaling niet voorkomen.

**1. *De auteur schrijft een reden bij het besluit* (25 september), voor de vierde keer.**
- `conventies/begrippen.md` kreeg bij het termbesluit: *"De vakdeskundige koos het Nederlandse
  woord, dat voor een beginner doorzichtiger is."*
- Het C4 van #332 noemt geen reden. De bijzin kwam uit de aanbeveling van de ontwerper bij VP2
  (*"Onzeker: basisgeval is voor een beginner doorzichtiger"*). Een overweging uit het ontwerp
  werd zo een motief van de vakdeskundige.
- De onderwijskundige ving het als puntje, omdat haar toewijzing voor de beoordeling ook de
  besluitdiff tegen het C4 omvatte. Het is geschrapt in `6cc6afa`.
- Het voorstel van 25 september staat nog open in #331.

**2. *Een zoekpatroon uit bekende formuleringen vindt alleen bekende formuleringen* (24 september).**
- De auteur toetste AC4 met `lambda|key\s*=` (geijkt op `9_extra`) en een AST-scan op
  `ast.Lambda` (zonder vermelde ijking).
- Beide beoordelaars vonden onafhankelijk een functie als waarde:
  `for f in [positives_loop, ...]:`. Het patroon zocht naar de bekende vormen van *functie als
  argument*, niet naar het begrip.
- Het was de enige blokkade van de oplevering. Hersteld in `73962fb`, en de herstelbeoordeling
  zocht met een ruimere AST-scan.

**3. *De bestaande meetpraktijk voor een hervatte agent werd niet geraadpleegd* (30 september).**
- De orkestrator gaf na het herstel van de auteur eerst op GitHub en aan de vakdeskundige twee
  totalen (*"999.009 of 1.399.676"*). Pas daarna las hij de melding als lopend totaal. Hij
  raadpleegde [metingen.md](metingen.md) pas bij het afsluiten, en daar rekent men al sinds #271
  met het verschil.
- De uitkomst is dezelfde, maar de volgorde is de verkeerde. Het is precies de herhaling die deze
  bevinding al beschreef, op de dag dat ze werd opgeschreven.
- Er was geen budgetgrens, dus er is geen besluit op de telling genomen.

**Wat het veranderde.** In dit werkitem alleen de herstellingen bij punt 1 en 2; bij punt 3 bleef
de uitkomst dezelfde. Wel bevestigt
het de lijn van *Een bevinding opschrijven voorkomt haar niet* (24 september). Voor alle drie
ligt een voorstel klaar dat de instructies zou veranderen: #331 (*Leg vast hoe de auteur
besluiten vastlegt en hoe een hervatte agent telt*) voor de eerste en de derde, en het
voorstel van 24 september voor de tweede. Geen van de drie is opgenomen. Dat is een procesbesluit
voor de vakdeskundige, niet voor de orkestrator.

## Een tegensprekend antwoord van de mens niet als tegenspraak herkend - 30 september 2026

**Wat er gebeurde.**
- Bij de poort van #332 legde de orkestrator VP1 voor als meerkeuzevraag, over het oefenbestand
  `extra/practice/1_recursie.ipynb` en de voorbeeldpagina.
- Drie opties:
  - *"Opgaan en verwijderen"*, de aanbeveling;
  - *"Laten staan, opstap nieuw"*;
  - *"Opgaan, voorbeeldpagina blijft"*.
- De vakdeskundige koos de derde. Het label noemde het opgaan van het oefenbestand, maar niet dat
  het daarna zou verdwijnen. Dat stond alleen in de toelichting eronder: *"Het oefenbestand gaat
  op in de opstap en verdwijnt"*. Het label van de eerste optie noemde het verwijderen wel.
- Het C4 registreerde *"wordt daarna verwijderd"*, en de auteur verwijderde het bestand in
  `a78cf1c`.
- Na de eerste beoordeling vroeg de orkestrator iets over de voorbeeldpagina. Het antwoord van de
  vakdeskundige luidde: *"Dat klopt niet; de opgaven in extra moeten wel blijven, maar de
  voorbeelden in extra mogen hergebruikt worden in de lopende tekst van de week (graag zelfs)"*.
- De orkestrator betrok die zin alleen op de voorbeeldpagina, en legde hem niet naast het C4.
  Een andere lezing lag voor de hand: de zin onderscheidt *opgaven* van *voorbeelden*, en het
  oefenbestand bevatte de opgaven. Die lezing wordt gesteund door wat de vakdeskundige na de merge
  van PR #334 zei: *"Je hebt de extra oefeningen voor recursie gewist."* Het terugzetten staat nu
  in #338.

**Waarom het ertoe doet.**
- Het nieuwe patroon: een later antwoord sprak een eerder besluit tegen, en die tegenspraak is
  niet als zodanig behandeld. De orkestrator las het antwoord binnen de vraag die
  hij had gesteld, en niet tegen de besluiten die al genomen waren.
- De lezing van de orkestratordiff van #332 had het verwijderen van `1_recursie` en het volledige
  antwoord allebei in handen. Ze verbond de twee niet. Geen van de beoordelingen en lezingen noemde
  de tegenspraak; het verwijderen was conform het C4.
- De vakdeskundige meldde het na de merge.
- Mogelijk speelde ook de optie mee, met het verschil tussen de labels dat hierboven onder *Wat er
  gebeurde* staat. Dat de vakdeskundige de toelichting miste, is een
  vermoeden. Het wordt gesteund door de latere uitspraak, maar de bron zegt het niet. Het is
  verwant aan *Een keuzeoptie van de orkestrator wordt de onderbouwing van de mens*
  (23 september): ook daar registreerde het C4 wat in de toelichting van een optie stond. Het
  onderscheid tussen label en toelichting is nieuw.

**Wat het veranderde.** De besluiten over het terugzetten staan in #338. In de instructies is
niets veranderd. **Voorstel** voor de evaluatie van #203, een procesbesluit voor de
vakdeskundige:
- leg een antwoord van de mens dat een genomen besluit kan raken, naast het C4. Vraag dan
  expliciet of het besluit verandert, voordat de volgende agentstap begint;
- zet in een optielabel elk gevolg dat iets verwijdert of verplaatst.

## De orkestrator meet een gat en behandelt het als nieuw - 30 september 2026

**Wat er gebeurde.** Drie keer in drie dagen legde de orkestrator iets aan de vakdeskundige voor,
of schreef het in een opdracht aan een rol als open vraag, terwijl het al besloten was en ergens
vastlag. De eerste twee op 28 september, het derde op 30 september.

- **Recursie in de midterm.** De opdracht aan de toetsontwikkelaar noemde als derde
  voorlegging: *"De elf itemplaatsen met recursie [...] toetsen dus stof die niet meer wordt
  onderwezen."* De verplaatsing van de recursie-uitkomst naar PGM2 staat in
  `curriculum/uitgangspunten.md`, én in de manifesten `data/pgm1/2021-*/toets.md` - die staan
  in de ANS-repo en zijn hier dus niet te vinden - die de orkestrator de dag ervoor zelf had
  geschreven: *"bewaard als referentie, niet als voorbeeld"*. De vakdeskundige: *"daar hebben
  we het over gehad verdorie"*.
- **De overlap met de oefenmidterm.** Aan de toetsontwikkelaar doorgegeven als risico dat
  voorgelegd moest worden. Het wás de werkwijze van de vakdeskundige, die een dag eerder had
  gezegd dat de toets de oefening qua opzet moest weerspiegelen. De meting die de orkestrator
  als bewijs meestuurde - achttien van de twintig concepten vallen samen - was de bevestiging
  dat die werkwijze werkte, niet een probleem.
- **Het ontbrekende werkcollege van week 7.** Opgeschreven in #341 als een afwijking die de
  auteur meet en de vakdeskundige vaststelt, zoals bij week 1 tot en met 5. Het was een gat dat
  commit `92df099e` had achtergelaten. En bij het heropenen van #102 noemde de orkestrator de
  vastgelegde lijn - de mutatiegrens, de verhuizing van objectmethoden naar PGM2 week 1 - met
  geen woord, terwijl die in `curriculum/uitgangspunten.md` §*Mutabiliteit: een grens die we
  bewaken* over 75 regels is onderbouwd.

**Waarom dit een patroon is.** Steeds dezelfde volgorde: de orkestrator meet de huidige staat,
vindt een gat, en behandelt het gat als nieuw. De stap die ontbreekt is zoeken of het gat het
gevolg van een besluit is. `CLAUDE.md` legt de ene helft van die regel vast - *"een besluit dat
niet in `curriculum/` of `conventies/` landt, is niet genomen"* - maar de keerzijde staat er
niet: wat er wél in staat, ís genomen, en dat geldt ook voor wat de orkestrator zelf heeft
opgeschreven.

Het kost meer dan een verkeerde vraag. Een voorlegging die niet nodig is kost een wachtmoment in
een lus die op menselijke poorten draait, en bij de midterm was dat tien dagen voor een afname.
Erger is dat het zich voortplant: de toetsontwikkelaar behandelde recursie als open vraag omdat
de opdracht dat zei, tot de orkestrator hem tijdens de rit corrigeerde. Een rol kan een besluit
niet terugvinden dat de orkestrator hem niet noemt.

**Wat het veranderde.** Bij #102 staat de vastgelegde lijn nu als aparte reactie, met per
besluit de vindplaats en een lijst van wat een herontwerp niet mag doen. Bij #341 is het
criterium over de afwijking ingetrokken.

Voorstel voor de instructies, een procesbesluit voor de vakdeskundige: **`CLAUDE.md` draagt de
ene helft van deze regel; laat het ook de keerzijde dragen. Zoek, vóór je iets als gat of als
open vraag opschrijft, in `curriculum/`, `conventies/` en de gesloten werkitems of het al
beslist is, en noem in de opdracht aan een rol de vindplaats en niet alleen de conclusie.**
Zolang die regel alleen hier staat, hangt hij aan wie deze bevinding toevallig leest, en dat is
precies de afhankelijkheid die de bevinding beschrijft.

## De orkestrator meet tegen een stilstaande lokale master - 1 oktober 2026

**Wat er gebeurde.** Drie artefacten van 30 september zijn gemeten tegen een tak die 43
commits achterliep. De lokale `master` stond op `79ddba40` van 26 september 22:46;
`origin/master` stond op dat moment al op `a83bd990` van 30 september 17:33. Het C1 bij #102
noemt `79ddba40` bovendien *"`origin/master`"*, en dat was het niet.

- **Werkitem #341** noemt in zijn aanleiding *"`handleidingen/` telt zes bestanden"* en vraagt om
  *"`handleidingen/week_7.md`, nieuw"*. Dat bestand bestond al: 341 regels, commit
  `1f207a89`, gemerged als PR #320 op 26 september 23:36, vier dagen vóór het werkitem werd
  geschreven. `79ddba40` is precies de commit vóór die merge.
- **De heropening van #102** en **het C1 daaronder** zijn tegen dezelfde boom gemeten. Hun
  twee dragende gaten hielden bij hermeting wel stand - week 7 is nog steeds de enige week
  van veertien zonder bestand in `source/practicals/`, en `source/solutions/7_opstap.ipynb`
  ontbrak werkelijk - maar dat is geluk en geen methode.

**Waarom dit een patroon is.** Het is niet de eerste keer, en het verschil met de vorige keer
is het punt. De registratie van #336 in [metingen.md](metingen.md) noteert onder *Omgeving*
dat de lokale `master` 86 commits achterliep en dat daardoor het werkcollege lokaal ontbrak -
en erachter staat *"Bijgewerkt met fast-forward vóór C1"*. Daar is de verouderde tak dus
gezien en rechtgezet voordat er gemeten werd. Bij #102 is hij niet gezien. Dezelfde
omgevingsfout, de ene keer gevangen en de andere keer niet, en geen van beide keren een regel
geworden - bij #336 stond het er als omgevingsfeit, en bij #102 pas hier als bevinding. In deze
repo wordt via
pull requests op GitHub gemerged en volgt de lokale tak niet mee; een meting tegen de
werkkopie meet dan de stand van de laatste keer dat iemand `git pull` deed.

Het verschil met een gewone meetfout is dat deze fout **werk uitvindt dat al gedaan is**. Een
gat dat je op een oude boom meet, is soms geen gat. Dat is de keerzijde van de bevinding
*De orkestrator meet een gat en behandelt het als nieuw* (30 september): daar was het gat het
gevolg van een besluit, hier van een merge die de meter niet had gezien.

**Wat het veranderde.** Bij #102 staat de meetbasis rechtgezet als aparte reactie, met de
twee gaten hermeten op `95b3743a` en alle vindplaatsen uit het C1 opnieuw nagelopen; één
regelnummer was verschoven. Bij #341 is gemeten dat het bestand bestaat en is het werkitem
voorgelegd aan de vakdeskundige, omdat de aanleiding niet klopt en het daarmee een besluit
vraagt en niet alleen het opheffen van een blokkade.

**Voorstel voor de instructies, een procesbesluit voor de vakdeskundige: meet nooit tegen
`master` of tegen de werkkopie zonder eerst `git fetch origin`, en noem als meetbasis de
korte hash van de commit van `origin/master` die je werkelijk hebt gelezen.** Een C1 of
werkitem dat *"origin/master"* zegt zonder hash is niet te controleren, en daardoor waren deze
drie artefacten pas een dag later vindbaar fout. Dit voorstel staat als invoer voor de evaluatie
op #203; de twee rechtzettingen die het al opleverde staan op #102 en #341.

## Rollen in één route delen de scratchpad van de orkestrator - 1 oktober 2026

**Wat er gebeurde.** Bij de beoordeling van #102 stelde de onderwijskundige vast dat de
scratchpad die hij voor de buildlogs kreeg aangewezen dezelfde map is waarin de orkestrator de
artefacten van alle andere rollen van die route had neergezet: het volledige C2, het C5, het
C4 en de C6 van de andere beoordelaar. Hij meldde het zelf, en schreef erbij dat hij er
uitsluitend de twee buildlogs en het poortverslag had gelezen en de rest uitdrukkelijk niet
had geopend, om zijn blinde beoordeling niet te breken.

**Waarom het ertoe doet.** `loop.md` eist dat iedere onafhankelijke beoordeling in een verse
context begint: geen maaktranscript, geen afwegingen uit het uitgebreide C5, en bij de eerste
beoordeling geen andere oordelen. Die eis werd hier gedragen door de discipline van de rol en
niet door de inrichting. Een beoordelaar die de buildlogs *moet* lezen om criterium 7 te
toetsen, krijgt de rest in dezelfde map mee; dat de isolatie standhield is hier vastgesteld
voor één rol in één ronde, en het is geen controle.

**Wat het veranderde.** Nog niets. Het is hier opgeschreven omdat de rol het vond en omdat
het zonder vastlegging onzichtbaar blijft: in de artefacten staat alleen dat de isolatie
standhield, niet dat zij van goede wil afhing.

**Voorstel voor de instructies, een procesbesluit voor de vakdeskundige: geef een rol alleen
de bestanden die hij nodig heeft, op een pad dat niet ook de artefacten van andere rollen
bevat.** Een aparte map per overdracht is genoeg; waaraan je zou zien dat het werkt is dat
een beoordelaar geen afweging meer hoeft te melden over wat hij niet heeft geopend. Dit voorstel
staat als invoer voor de evaluatie op #203.

**Het kwam in de ronde erna meteen terug.** De redacteur die deze registratie las, kreeg
dezelfde map aangewezen en vond daar de artefacten van alle rollen van deze route, inclusief
de twee C7's die hij als bron moest gebruiken. Hij meldde dat bij één patroonzoektocht twee
van die bestanden hebben meegedraaid. Twee rollen, twee rondes, dezelfde toestand, allebei
door de rol zelf gemeld en niet door de inrichting gevangen.

## Een regelafbreking maakt een zoekpatroon blind - 1 oktober 2026

**Wat er gebeurde.** Vier keer op één dag gaf een zoekpatroon nul omdat de gezochte zin over
twee regels liep, in bestanden die rond 92 tekens afbreken.

- De onderwijskundige zocht bij #102 vijf gewijzigde passages terug in de gerenderde HTML en
  kreeg drie valse nullen voordat hij de regelafbreking doorhad. Hij loste het op door de
  HTML plat te slaan vóór het zoeken, en noteerde het in zijn C6.
- De orkestrator zocht in `curriculum/uitgangspunten.md` naar *"dunste week van de cursus"* en
  kreeg nul, terwijl de zin er staat: *"Het is de dunste"* eindigt de ene regel en *"week van
  de cursus"* begint de volgende. Met de regels plat geslagen is de treffer er wel.

**Waarom dit geen variant is van een bekende bevinding.** *Een zoekpatroon uit bekende
formuleringen vindt alleen bekende formuleringen* (24 september) gaat over een patroon dat te
nauw is geformuleerd. Hier is het patroon juist exact goed en is het **bestand** anders
opgemaakt dan de zoeker aanneemt. De ijkregel uit `CLAUDE.md` vangt het alleen als je ijkt op
een vindplaats die zelf over twee regels loopt, en dat is precies wat niemand doet: je ijkt op
iets korts dat je zeker weet, en dat staat op één regel.

**Wat het veranderde.** De vindplaats in `uitgangspunten.md` is met een geijkt patroon
bevestigd en is #351 geworden; zonder die tweede poging was dat werkitem er niet.

**Voorstel voor de instructies, een procesbesluit voor de vakdeskundige: zoek een zin van meer
dan een paar woorden nooit regelgewijs.** Sla de regels plat vóór het zoeken, of zoek op een
fragment dat zeker binnen één regel valt. En ijk een nul op een vindplaats die net zo lang is
als wat je zoekt, niet op een kort woord dat overal past. Dit voorstel staat als invoer voor de
evaluatie op #203.

## De meetpraktijk voor een hervatte agent werd voor de derde keer niet geraadpleegd - 2 oktober 2026

**Wat er gebeurde.** Bij #335 werden twee agents hervat: de ontwerper voor zijn herstel en de
auteur voor de puntjesreparatie. De orkestrator noteerde op GitHub steeds het gemelde getal als
verbruik van die stap. Bij de auteur ging hij verder: aan de vakdeskundige meldde hij dat de
reparatie, met 423.033 tokens, *"meer dan de hele oorspronkelijke oplevering"* kostte. Hij
kondigde ook aan dat als bevinding vast te leggen, als bewijs dat hervatten duur is. De
praktijk in [metingen.md](metingen.md) rekent sinds #271 met het verschil tussen twee meldingen
van dezelfde agent. Volgens die praktijk was de reparatie 42.625 tokens. De orkestrator zag de
fout pas bij het schrijven van de metingen, toen hij de tabel van #332 opende. De correctie
staat op #335 en PR #360.

**Waarom dit een patroon is.** Het is dezelfde fout als bij #273 (23 september) en #326
(30 september), en de bevinding van 30 september beschrijft precies dit. Nieuw is de richting.
De vorige keren stonden er twee lezingen naast elkaar. Nu werd de hoge lezing gebruikt als
onderbouwing van een tegengestelde conclusie, en die was bijna als bevinding vastgelegd. Een
bevinding die op een verkeerde telling rust, stuurt de werkwijze de verkeerde kant op. Ook hier
bleken de toolaanroepen de aanwijzing: 7 aanroepen voor +46.044, en 27 voor +42.625.

**Wat het veranderde.** De tellingen op GitHub zijn gecorrigeerd, met beide lezingen. In
[metingen.md](metingen.md) telt #335 met het verschil, en de hoge lezing staat ernaast. In de
instructies is niets veranderd.

Voorstel, een procesbesluit voor de vakdeskundige. Het voorstel van 23, 24 en 30 september staat
nog open: leg de telling van een hervatte agent vast in de meetdefinitie in `/orc`, op de plek
waar de orkestrator de meetregel schrijft, en niet alleen hier. Drie keer dezelfde fout na twee
bevindingen laat zien dat een bevinding die de orkestrator niet op het moment zelf leest, hem
niet bereikt.

**Bij hetzelfde werkitem: opnieuw een stilstaande lokale master.** De route van #335 is gemeten
tegen de lokale `master` op `d7202964`. `origin/master` was intussen al verder met #102, #344,
#352, #354 en #355. Dat is het patroon van *De orkestrator meet tegen een stilstaande lokale
master* (1 oktober), een dag na die bevinding. Bij de inname stond de bevinding wel in
`origin/master`, maar niet in de lokale werkkopie die de orkestrator las. De fout kwam pas aan
het licht door de samenvoegconflicten bij de merge van PR #360. De gevolgen bleven beperkt tot
twee tellingen die #102 al had veranderd:
- de niveautelling: C1b, C2 en C5 gingen uit van 41, 36 en 5, terwijl `origin/master` op 41,
  37 en 4 stond (geijkt met hetzelfde script); na samenvoegen is het 43, 42 en 1;
- het aantal `## Opdrachten`-vindplaatsen in `begrippen.md`: dertig, niet negenentwintig.

Beide zijn bij het oplossen van de conflicten hermeten en rechtgezet. Een `git fetch` met een
vergelijking tegen `origin/master` bij de inname had dit voorkomen. Dat onderstreept het
voorstel van 1 oktober.

## Een getal uit een oordeel is ook een overgenomen getal - 5 oktober 2026

**Wat er gebeurde.** Bij de registratie van #104 in PR #366 las een redacteur de ingang en gaf
**BLOKKEER** op drie moetpunten. Een ervan was dat de slotalinea beweerde dat een registratie
vóór de beoordeling hoort te vallen, terwijl de ingang zich zelf weerlegt. Zijn bewijs luidde:
*"Drie van de vijf tabelrijen en vier van de zes vetgeleide alinea's bestaan pas ná de
beoordeling."* De orkestrator nam dat bewijs over in zijn herstel - *"drie van haar vijf
tabelrijen en vier van haar alinea's"* - en telde het niet na.

Geen van beide noemers klopt. Nageteld op `f01798ef`: de tabel heeft **zes** rijen onder de
scheidingsregel, en vijf klopt alleen als je de orkestratorrij weglaat, de enige zonder
tokengetal - een criterium dat er niet bij stond. De sectie heeft **acht** vetgeleide alinea's,
niet zes: dertien blokken, waarvan één kop en één tabel, dus elf alinea's. Een verse redacteur
ving het eerste getal in de herstelbeoordeling en schreef erbij dat het ongewijzigd uit zijn
eigen vorige oordeel kwam; het tweede is pas bij de lezing van déze bevinding geteld, omdat het
hier als citaat werd doorgegeven zonder dat iemand het had nageteld.

De telling stond bovendien in dezelfde sectie als de alinea die in datzelfde herstel was
rechtgezet omdat zij een rangtelwoord zonder telling gebruikte: in `9f9b8e1e` eindigt die alinea
op r2935 en staat de telling 32 regels lager, op r2967. Hoe groot die afstand was, is bij het
opschrijven van deze bevinding opnieuw uit het vorige oordeel overgenomen in plaats van gemeten -
*"negen regels"* - en daarmee ook de richting, want de telling stond eronder en niet erboven. Dezelfde fout dus, bij het opschrijven van de bevinding erover,
en opnieuw gevonden door de lezing en niet door de schrijver.

**Waarom dit een patroon is.** De bevinding van 24 september, *Een getal dat de orkestrator
opschrijft, heeft hij niet altijd geteld*, vermoedt dat zulke getallen als samenvatting voelen en
niet als meting, en noemt dat vermoeden ongemeten. Dit geval voegt er een bron aan toe die het
niet dekt: niet een uitsnede of het geheugen, maar een artefact dat de orkestrator net volledig
had gelezen, van een rol die het getal zelf had opgeschreven als bewijs. Dat is de vorm waarin
een getal geen meting meer lijkt te vragen - het staat in een oordeel, het ondersteunt een
blokkade die juist is, en het overnemen voelt als trouw aan de bron in plaats van als een nieuwe
bewering. De rol die het opschreef had het zelf ook niet geteld, en de rol die hém naschreef
evenmin.

`CLAUDE.md` §*Meten* zegt *"meet het ding zelf, niet iets ernaast"*. Wat dit geval toevoegt is dat
een oordeel van een rol ook *iets ernaast* is zodra je er een getal uit overneemt, hoe zorgvuldig
het ook is opgeschreven en hoe volledig je het ook hebt gelezen.

De lezing van deze bevinding gaf zelf **BLOKKEER**, twee ronden achter elkaar; zie de
[reacties op PR #367](https://github.com/hanze-hbo-ict/programmeren/pull/367). Wat die ronden
kostten en wat zij vingen, staat bij de ingang onder *Werk buiten de lus om* in `metingen.md`.

**Wat het veranderde.** Het getal is nageteld en rechtgezet in `7450b6a3`, met de alineatelling
eruit; de ingang staat zo in `695d5cb0`. De tweede noemer van het citaat is hier nageteld. Twee
punten gaan naar de evaluatie van #203, bovenop de twee voorstellen van 24 september; geen van
beide is hier beslist.

- **Voorstel: wie een getal uit een artefact overneemt, telt het na of schrijft erbij dat hij het
  niet heeft geteld.** Het eerste voorstel van 24 september vraagt dat een getal met de opdracht
  komt die het opleverde. Bij een getal uit een oordeel is die opdracht *lees dit artefact*, en
  dan is de vraag of de telling erachter ooit is gedaan niet te beantwoorden. Het gaat dus om de
  telling, niet om de opdracht. **Aanvulling van 6 oktober:** een regelnummer in een ander
  document valt hieronder, en bovendien veroudert het; verwijs naar de sectie waar de verwijzing
  een merge kan overleven.
**Nog drie gevallen, bij #368 op 6 oktober 2026, en één ervan is van de andere kant gevonden.**

1. **Een regelnummer is ook een getal.** De orkestrator schreef in de C0 en de C1 van #368 dat
   besluit VP7 is vastgelegd in `conventies/codeconventies.md` r89. Die regel is
   `| `L` | lijst |`; de `_`-rij staat op r95 zonder besluitnummer, en het besluit zelf staat in
   `curriculum/leerlijn.md` r676. Hij had de vindplaats uit #348 overgenomen in plaats van haar te
   openen. De ontwerper ving het bij zijn hermeting, en de orkestrator zette het recht in een
   C1-aanvulling op de issue.
2. **De auteur corrigeerde de orkestrator.** Bij de puntjesronde gaf de orkestrator een bewering
   uit het tweede beoordelingsoordeel door: dat van de splitsing 51/83 alleen de C0 (59/74) en de
   eerste auteursmeting (52/82) afweken. Hij toetste die niet aan zijn **eigen** C1-aanvulling,
   waarin hij zelf een derde splitsing had gemeten: 43/91. De auteur ving het, nam het puntje in
   gecorrigeerde vorm over en claimde de meetpijplijn die hij niet had gezien niet. Tot nu stond
   dit patroon in het dossier als iets wat de orkestrator doet en een beoordelaar vangt; dat een
   rol het naar bóven toe rechtzet is nieuw, en het is het sterkste bewijs dat de maatregel niet
   van de richting afhangt.
3. **Eén variant die hier niet thuishoort maar wel op hetzelfde lijkt.** In de registratie van
   #368 typte de orkestrator twee getallen verkeerd over die hij net had gelezen: 94.161 voor
   94.165 en 507.200 voor 507.204. Hij ving het zelf vóór de commit. Dat is overtypen en geen
   overnemen - de telling was gedaan - en het hoort hier alleen bij omdat het symptoom gelijk is
   en de remedie niet: tegen overtypen helpt natellen van de som, tegen overnemen helpt de
   telling zelf doen.

**Een verwijzing veroudert bij de eerste merge die haar raakt.** Geval 1 heeft een staartje dat
het patroon uitbreidt. De registratie van #368 schreef dat het naslepen van `ix` al belegd lag in
`codeconventies.md` r140-143 - juist op het moment van schrijven, want zo stond het in het C2 en
het C4, die de uitgangsversie citeerden. Dezelfde route voegde daarna 121 regels aan dat bestand
toe, en sindsdien leest r140-143 de alinea over `first` en `rest` terwijl de bedoelde passage op
r265-268 staat. Een regelnummer dat naar een ander document wijst is dus niet alleen een getal
dat geteld moet worden, het is er ook een dat verschuift. Wie naar een passage verwijst die hij
niet in dezelfde commit vastzet, noemt de sectie en niet de regel.

- **Voor de evaluatie: de lezerregel heeft hier meer gevangen dan de registratie zelf.** Het
  tweede voorstel van 24 september was die regel uit te breiden tot alle orkestratortekst, dus
  ook tot de metingen van een werkitem. Bij #366 is dat gedaan terwijl de norm iets smallers
  vraagt: `loop.md` noemt een *besluittekst*, `orc.md` een *besluitdiff* getoetst tegen het C4, en
  dit is een registratie met een voorstel erin. Dat onderscheid is vastgesteld in puntje 4 van de
  [herstelbeoordeling op PR #366](https://github.com/hanze-hbo-ict/programmeren/pull/366). Die
  twee ronden kostten 129.104 en 85.034 tokens en leverden drie blokkades plus de herhaling
  hierboven op.

## Twee orkestratorsessies draaiden één werkitem - 9 oktober 2026

**Wat er gebeurde.** (Alle tijden hieronder lokaal, +02:00.) Aan #377 werkten twee
orkestratorsessies tegelijk, met twee GitHub-identiteiten: `ralfvandenbroek` schreef C1, de eerste C4's, de C5-kern en de
beoordelingen van ronde 1 en de herstelronde; `misja` nam de route vanaf diezelfde
herstelronde over zonder te weten dat zij liep. De tweede sessie fetchte om 10:33, zag de
branchkop `441028b1` van 10:27 en de aankondiging *"herstelronde 1 gestart"* van 10:38,
concludeerde *aangekondigd maar niet uitgevoerd*, en startte om ongeveer 10:49 een tweede
auteur op dezelfde ronde. De auteur van de eerste sessie had op dat moment al gepusht -
`8c49d8fe`, 10:43 - en de twee herbeoordelingen stonden om 10:50 op de PR.

De tweede auteur draaide dus de hele ronde opnieuw: 137.861 tokens, 18 min 24 s, 51
gereedschapsaanroepen. **Hij ving het zelf.** Zijn C5 opent met een afwijking vooraf: *"De
opdracht noemt `441028b1` als laatste commit. Dat is niet de stand. Op de branch stond bij
mijn start al `8c49d8fe`."* Niet de orkestrator die hem startte, maar de rol die op de boom
keek, zag dat de opdracht van een achterhaalde stand uitging.

Gratis was die dubbele ronde niet. Omdat hij de stand zag, schreef hij geen tweede versie van
het werk, maar hij zette er wél additief één commit op: `995234fb`, 11:04:11, dertien regels
in `conventies/codeconventies.md`, die de scopevraag over `5b` en `7b` in de conventietekst
openliet. **In haar eigen ronde heeft geen enkele rol die commit gelezen**: de twee
herbeoordelingen waren al gepubliceerd toen hij landde, en het C7 van die ronde noteert hem
daarom als *niet beoordeeld*. Pas in de vervolgronde namen beide beoordelaars hem in de diff
mee, en toen was hij door `bdf63511` al geheel vervangen. Een tweede orkestrator op dezelfde
ronde levert dus niet alleen dubbel werk op, maar ook een wijziging in `conventies/` die
buiten de beoordeling van haar eigen ronde valt en die niemand had gemist als zij was
weggebleven.

**Waarom dit geen variant is van de twee bestaande bevindingen.** Bevinding 17 gaat over twee
agents in één werkboom, en de maatregel daar is boomexclusiviteit. Bevinding 18 gaat over
parallelle routes op het bord, en de maatregel daar is een afhankelijkheidscontrole tussen
werkitems. Met `995234fb` erbij is de afstand tot 17 kleiner dan zij lijkt - er landde
inderdaad een commit van de ene actor op de branch waar de andere aan werkte - maar de
maatregel van 17 dekt het niet: de twee auteurs zaten niet in één werkboom, ze werkten vanuit
twee sessies op dezelfde branch, met ieder een eigen boom. Dit is één route met twéé
orkestrators, en daarvoor staat nergens iets. Niets in
deze repo wijst een route aan een sessie toe: de Status op het bord is één veld dat iedereen
kan zetten, een issue heeft geen eigenaar, en de branch draagt geen spoor van wie haar
bestuurt. De enige signalen waren GitHub-tijdstempels, en die stonden in drie verschillende
reacties.

En de fout die eruit volgde is niet *te weinig gelezen* maar *het verkeerde gelezen*. De
branchkop is een stand van gepusht werk, en een lopende agent heeft nog niets gepusht. Een
kop die ouder is dan de aankondiging betekent daarom precies het omgekeerde van wat de tweede
sessie eruit las: niet dat de ronde niet liep, maar dat zij nog niet klaar was.

**Wat het veranderde.** De tweede sessie plaatste een rectificatie op PR #385 - de bewering
*"aangekondigd maar niet uitgevoerd"* was onjuist - hield de rondeteller op **1/1** in plaats
van een tweede ronde te claimen, en gebruikte het dubbele werk als onafhankelijke verificatie
van `8c49d8fe`: twee auteurs kwamen op dezelfde omzetting uit. De eerste sessie meldde zich af
op de PR, startte geen agents meer en droeg bord, metingen en deze bevinding over aan de
andere. Haar meetregels staan in die afmelding, zodat de registratie van #377 in
[metingen.md](metingen.md) beide sessies dekt.

- **Voorstel voor de instructies, een procesbesluit voor de vakdeskundige: een route heeft
  één orkestrator.** Wie een werkitem hervat, zegt dat eerst op de issue en kijkt of daar al
  zo'n claim staat; staat er een aankondiging die jonger is dan de branchkop, dan loopt die
  stap en vraag je de mens. En fetch opnieuw vlak vóór elke agentstart, niet alleen bij de
  inname: de fetch van 10:33 was juist en bij het handelen om 10:49 achterhaald. Dit voorstel
  staat als invoer voor de evaluatie van #203.

## Een meting over notebooks las alleen de codecellen - 9 oktober 2026

**Wat er gebeurde.** De orkestrator mat bij #377 hoeveel kale booleanasserts er nog in PGM1
stonden en gaf het antwoord aan de vakdeskundige door: **50 in drie bestanden**. Het waren
**82 in vier**. Zijn AST-scan liep over de codecellen van de notebooks, en
`source/practicals/5b_boter_kaas_eieren.ipynb` zet zijn code in ` ```python `-fences **in
markdowncellen**: 32 asserts, 17 met `assert not` en 15 kaal, die het patroon geen van alle
zag. Voor dat bestand gaf de scan nul.

Dat is precies het geval waartegen `CLAUDE.md` waarschuwt - *een stukgelopen patroon geeft
altijd nul* - en de ijking ving het niet, want geijkt was er wél: PGM2 gaf ruime treffers. De
ijking stond alleen op de verkeerde as. Het patroon werkte; het **corpus** was te klein, en
een ijking op een ander deel van hetzelfde corpus zegt daar niets over.

De auteur had het goed. De tabel die hij in `conventies/codeconventies.md` schreef gaf de
juiste getallen, en de orkestrator heeft alle acht cellen nagemeten (17/15, 25/17, 3/1, 3/1).
De fout zat dus niet in het materiaal en niet in het artefact, maar in het getal dat de
orkestrator náást het artefact aan de mens doorgaf.

**Waarom dit geen variant is van de bestaande bevindingen over blinde patronen.** *Een
zoekpatroon uit bekende formuleringen vindt alleen bekende formuleringen* (24 september) gaat
over een te nauw patroon, en *Een regelafbreking maakt een zoekpatroon blind* (1 oktober) over
een bestand dat anders is opgemaakt dan de zoeker aanneemt. Hier is het patroon goed en de
opmaak bekend: notebooks hebben code- en markdowncellen, en dat weet iedereen. Wat eraan
ontbrak is de reden om in de markdowncellen te kijken, en die is didactisch: een practicum
zet code in proza zodat de student haar **overtypt** in plaats van uitvoert. Wie uitwerkingen
meet, mist precies de bestanden waar de vorm het meest zichtbaar is voor de student.

**Wat het veranderde.** De meting is overgedaan met de fences erbij, de correctie staat op
PR #385, en het besluit dat eruit volgde - alle resterende asserts omzetten - werd op het
juiste getal genomen. De nameting in de registratie van #377 in
[metingen.md](metingen.md) leest codecellen, `python`-fences in markdowncellen en
`.md`-fences, en loopt de blokken die niet parseren apart met grep na in plaats van ze te
laten vallen - onder twee afbakeningen, zodat het getal zelf navolgbaar is. Een nul die naast
een ijking én een nagelopen rest staat, is pas een nul.

**Tweede geval, dezelfde dag, in een werkvoorraad.** De registratie van #377 stuurde een
puntje naar de veegronde dat eveneens uit een ongeijkte nul kwam: dat `uitgangspunten.md`
verwijst naar een kruisverwijzingsregel die `conventies/schrijfwijzer.md` niet heeft. De
auteursrol die dat opschreef beriep zich op `grep -rn 'kruisverwijzing' conventies/` - nul
treffers - en de regel staat er wél, in §*Samenhang bewaken*, beginnend met een hoofdletter:
**"Kruisverwijzingen moeten altijd kloppen."** Met `-i` is er één treffer. Niemand ving het bij
de bronronde; de lezer van de registratie ving het, en op dat moment lag er al een
veegrondepuntje dat iemand had laten repareren wat klopt. Een stukgelopen patroon levert dus
niet alleen een verkeerd besluit op, maar ook werk dat niet bestaat - en dat is duurder,
omdat het pas opvalt als iemand het oppakt.

## De orkestrator schreef in een C4 een clausule die de mens niet had genomen - 9 oktober 2026

**Wat er gebeurde.** De vakdeskundige besloot dat de versmalling van de bevriezing alleen het
oefententamen van PGM1 geldt. De orkestrator legde dat vast in een C4 en schreef er een
clausule bij die niet in het besluit zat: dat `source/extra/practice/pgm1_examen.ipynb` bij de
andere oefententamens hoort en zijn vormbevriezing houdt *"voor zover het de vorm van de toets
zelf betreft"*. Die woorden waren van de orkestrator. De auteur voerde ze uit, want ze stonden
in zijn opdracht, en de redacteur gaf **BLOKKEER** op AC7: de tekst vrijwaart de vorm van een
toets die het besluit juist bevroren houdt. De orkestrator trok de clausule daarop in met een
gecorrigeerd C4 (*"Die woorden zijn van de orkestrator"*), de vakdeskundige besliste dat toets
én uitwerking beide onder de versmalling vallen, en een verse redacteur stelde in herstelmodus
vast dat B4 met haar premisse vervalt - en dat de reparatie die zij vroeg **uitdrukkelijk niet
moet worden uitgevoerd**. Zonder die herbeoordeling had de auteur een tekst geschreven die het
besluit tegenspreekt.

**Waarom dit een patroon is, en waar de bestaande maatregel precies faalt.** Dit is de
tegenhanger van *Een keuzeoptie van de orkestrator wordt de onderbouwing van de mens* (23
september). Daar schreef de orkestrator de **reden** bij een keuze, hier de **reikwijdte**.
Het C4-contract verbiedt nieuwe inhoudelijke rechtvaardiging namens de mens, maar niets toetst
het C4 zelf: de mens leest zijn eigen besluit terug in woorden die hij niet koos, en voor de
auteur is het C4 de bron.

Bevinding 14 - *Niets toetst wat de orkestrator schrijft* - is geantwoord met de maatregel
die nu als slotalinea van `orc.md` §*Ontwerpen en besluiten* staat: schrijft de orkestrator
naar `curriculum/` of `conventies/`, dan gaat die diff langs een onafhankelijke redactionele
toets vóór de merge. En die alinea zegt: getoetst **tegen het C4**. Dat is waarom de maatregel
dit niet had hoeven vangen - de diff klopte met het C4, want de clausule stond er zelf in. De
redacteur ving het doordat hij verder keek dan de norm vraagt en de diff ook tegen het
*menselijke* besluit legde. De maatregel werkte hier dus beter dan hij is opgeschreven.

Twee dingen horen hierbij. De maatregel was in `/orc` eerst een genummerde **stap 5b**, en is
bij de herschrijving van #203 proza geworden; `metingen.md` noteert die overgang zelf twee
keer, en bevinding 14 noemt juist dat terugzetten naar proza haar zwakte. Deze bevinding
voegt er een tweede zwakte aan toe die niets met de vorm te maken heeft: ook als handeling
zou zij tegen het verkeerde artefact toetsen. En de orkestrator citeerde bij het opschrijven
van deze bevinding eerst *stap 5b* als bestaande stap, in een dossier dat op twee plaatsen
vastlegt dat zij dat niet meer is - gevonden door de lezer van deze registratie.

**Wat het kostte.** De stap die alleen door de clausule bestaat is de herbeoordeling: 46.797
tokens en 2 min 49 s. De blokkade zelf kostte geen ronde, want de automatische herstelronde
was al verbruikt; wat zij kostte is een gang terug naar de vakdeskundige met een vraag die
zijn besluit niet had opgeroepen.

- **Voorstel voor de instructies, een procesbesluit voor de vakdeskundige: de redactionele
  toets van een besluitdiff gaat tegen het menselijke besluit én het C4, niet tegen het C4
  alleen.** En: wat in een C4 niet letterlijk van de mens komt, staat er als zodanig bij - de
  regel die bij de bevinding van 23 september al is voorgesteld, nu met een tweede geval en
  een aanwijsbare blokkade erachter. Dit voorstel staat als invoer voor de evaluatie van het
  procesexperiment #203.

## *Niet beschikbaar* stond in de eigen sessie - 9 oktober 2026

**Wat er gebeurde.** De orkestrator publiceerde bij #377 acht meetregels van rollen met
*tokens: niet beschikbaar*, één ervan met de uitleg *"niet beschikbaar in deze sessie; de
orkestrator leest ze van de agentstart"*. Ze waren wél beschikbaar. Elke agent die klaar is,
levert een verbruiksmelding met `subagent_tokens`, `tool_uses` en `duration_ms` af in de
sessie, en die meldingen
staan in het sessielog van de orkestrator op het tijdstip dat hij het artefact
plaatste: de melding van de vervolgronde kwam om 14:17:55 binnen met 185.013 tokens, en de C5
met *niet beschikbaar* ging om 14:19:22 online (tijden lokaal, +02:00). Achteraf uit het log
gehaald: negen ronden, **931.369 tokens**, elk met duur en aantal gereedschapsaanroepen. Ze
staan in de registratie
van #377 in [metingen.md](metingen.md).

Er zit een tweede helft in: waar de duur ontbrak, kwam er een schatting in plaats van de
melding, en geen van de drie schattingen klopte. De vervolgronde werd uit de mtimes van
scratchpadbestanden geschat op *"18 min 40 s"* en meet 23 min 34 s - vijf minuten te laag,
omdat die bestanden het begin en het einde van het werk niet afbakenen. De twee andere gaan de
andere kant op en veel verder: de begrenzingsronde stond gepubliceerd als *"circa 35 minuten
tot commit"* en meet **5 min 46 s**, en de herbeoordeling van de onderwijskundige als *"ca. 20
min, waarvan ca. 10 min `make clean && make html`"* en meet **13 min 56 s**. Een wandklok
tussen twee momenten in de sessie meet ook alles wat ernaast gebeurde, inclusief wachten op de
mens; de melding meet de agent. Dat zijn twee verschillende grootheden, en de gepubliceerde
getallen zeiden niet welke van de twee ze waren.

**Waarom dit een patroon is.** `loop.md` zegt: *"Ontbrekende meetgegevens heten niet
beschikbaar, nooit nul."* Die regel beschermt tegen een verzonnen nul en zegt niets over de
vraag of het getal werkelijk ontbreekt. Daardoor werd *niet beschikbaar* het antwoord op *ik
heb het nu niet bij de hand*, en dat is dezelfde fout als een nul vertrouwen die uit een
stukgelopen patroon komt: een lege uitkomst die niet is geijkt. Zij staat in de drukste
familie van dit bestand - *Een hervatte agent meldt zijn tokens als lopend totaal* (23
september), *Een agent die op de sessielimiet stopt, levert zijn verbruik niet af* (24
september), *De meetpraktijk voor een hervatte agent* (30 september en 2 oktober) en *Een
getal uit een oordeel is ook een overgenomen getal* (5 oktober) - en voegt eraan toe wat die
alle niet beschrijven: niet een getal dat verkeerd is doorgegeven, maar een getal dat is
weggelaten terwijl het er lag. De rij *aanvulling na C4* in de registratie is tegelijk een
geval van de eerste: op GitHub staat zij als *"niet beschikbaar (de agent werd hervat)"*, in
de tabel als 3.773 in 28 s, uit het verschil van twee cumulatieve meldingen.

Het bijzondere is dat de bron hier niet moeilijk te vinden was. Hij stond in de eigen
sessie, en `metingen.md` opent
met de zin dat de getallen uit *"de tokentelling die de orkestrator per subagent terugkrijgt"*
komen en *"verder alleen in de sessiecontext"* bestaan.

**Wat het veranderde.** De negen getallen zijn achteraf uit het log gehaald en staan in
die registratie, met de schatting die te laag was erbij. De negende ronde - de dubbele
auteur uit de eerste bevinding - kreeg helemaal geen eigen meetregel; haar getal staat nu ook
in de registratie. De acht meetregels op PR #385 blijven staan zoals ze zijn gepubliceerd; de
registratie is de plaats waar het wordt rechtgezet, en dat is hier niet voor het eerst - de
bevinding van 5 oktober noteert ook een getal dat pas bij het opschrijven is nageteld.

- **Voorstel voor de instructies, een procesbesluit voor de vakdeskundige: de meetregel wordt
  geschreven bij de verbruiksmelding, niet bij het artefact.** De orkestrator leest de melding
  zodra een rol klaar is en zet rol, tokens, duur en aantal aanroepen in de reactie waarin
  hij het artefact plaatst. *Niet beschikbaar* staat er pas nadat hij gekeken heeft, en met
  waar hij keek. Een schatting draagt haar methode én de reden dat de melding ontbreekt, en
  zegt welke grootheid zij schat: de agent of de wandklok. Dit voorstel staat als invoer voor
  de evaluatie van #203.

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

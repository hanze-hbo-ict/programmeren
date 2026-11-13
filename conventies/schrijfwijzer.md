# Schrijfwijzer

Deze schrijfwijzer legt vast hoe we schrijven voor de studenten van
Programmeren 1 en 2: register, aanspreekvorm, terminologie en de opbouw van een
tekst. Wie materiaal schrijft of laat schrijven, houdt zich eraan. Wie
materiaal beoordeelt, toetst eraan.

Dit document gaat over de tekst. De technische opmaak staat in
[technische-conventies.md](technische-conventies.md).

Dit document is voor auteurs, niet voor studenten. Het staat bewust buiten
`source/` en maakt geen deel uit van het boek.

## Doelgroep

Eerstejaars HBO-ICT die leren programmeren, veelal zonder voorkennis. Dat
bepaalt vrijwel alles hieronder: wie voor het eerst programmeert, heeft geen
kapstok om nieuwe begrippen aan op te hangen en raakt sneller de draad kwijt bij
een zin die twee dingen tegelijk doet.

## Register

Het materiaal is een bewerking van CS5 van Harvey Mudd College en heeft daaruit
een eigen stem geërfd: **eenvoudig, vriendelijk en uitnodigend**. Die stem
houden we aan. Het is een keuze, geen erfenis die we gedogen.

Wat dat betekent:

- Korte zinnen. Eén gedachte per zin.
- Leg uit voordat je een term gebruikt, niet erna.
- Aanmoedigen mag. Een opgave mag afsluiten met "Succes!" en een lastig
  onderdeel mag benoemen dat het lastig is.
- Humor mag, mits ze de uitleg niet in de weg zit en zonder toelichting te
  volgen is voor iemand die de context niet deelt.

Wat we niet doen:

- Neerbuigend zijn. "Dit is natuurlijk heel eenvoudig" maakt een student die het
  níet eenvoudig vindt niet wijzer.
- Ironie of understatement waarop de uitleg leunt. Een beginner heeft geen
  referentiekader om die te herkennen.
- Vulwoorden die niets dragen. "Gewoon" en "even" suggereren dat iets triviaal
  is; laat ze weg tenzij ze echt iets afbakenen.

## Emoji

Emoji mogen, sober en gepast. Ze staan al jaren in het materiaal en dragen bij
aan de toon.

De regel bewaakt het niveau, niet het bestaan. Het risico is wildgroei bij
AI-ondersteund schrijven: taalmodellen strooien met emoji en tillen een tekst
met drie emoji ongemerkt naar dertig. Voeg er dus geen toe zonder reden, en
haal ze weg waar ze zich hebben opgehoopt.

## Geen chatbot-tekst

Veel van dit materiaal wordt met AI-ondersteuning geschreven of herzien. Dat is
prima. Het resultaat mag alleen niet te lezen zijn als modeluitvoer.

Dit is de scherpste regel in dit document, omdat de fout aantoonbaar al is
gemaakt. In `source/extra/examples/minimax.md` staan twee zinnen die nooit
lesmateriaal hadden mogen worden en nu live op de site staan:

> Wil je dat ik nog dieper inga op bepaalde aspecten van het algoritme of heb je
> interesse in hoe dit zou werken voor andere spellen?
>
> Zou je geïnteresseerd zijn in meer details over een specifiek aspect van dit
> proces?

Een tekst richt zich tot de student, niet tot een gesprekspartner. Let daarnaast
op deze terugkerende patronen:

- De tegenstellingsconstructie "het gaat niet om X, maar om Y", gebruikt als
  ritme in plaats van als echte tegenstelling.
- Drieslagen: "helder, consistent en professioneel".
- Bezwerende slotzinnen die niets toevoegen.
- Overmatig "juist", "immers" en "simpelweg".

Dit is een richtlijn, geen mechanische toets. De vraag per geval: draagt deze
zin een echte wending in de redenering, of vult ze het ritme op? Vult ze op, dan
gaat ze weg.

## Vaktermen: Nederlands of Engels

Het proza is Nederlands. Voor vaktermen geldt:

- Gebruik de Engelse term waar die in het vakgebied gangbaarder is. Forceer geen
  Nederlandse vertaling voor `string`, `debuggen` of `commit`.
- Introduceer een Engelse term bij eerste gebruik kort in het Nederlands, en
  gebruik daarna alleen de Engelse. Voor beginners is die eerste toelichting
  wél nodig, anders dan bij ouderejaars.
- Vervoeg Engelse termen niet tot hybriden. Niet "je cloneert de repository",
  wel "clone de repository".
- Eén begrip, één term. Wissel niet ongemerkt tussen synoniemen.
- Gebruik **lijst**, behalve als het specifiek over het Python-type `list` gaat.
  Schrijf ook **lijsten** en **lijst van lijsten**. Het besluit met de menselijke
  reden staat in [begrippen.md](begrippen.md#lijst-en-list).

De taal van de **code zelf** (namen, commentaar, docstrings) is een aparte
kwestie, met een eigen afspraak per studiejaar. Die hoort in de codeconventies;
dat document is nog niet geschreven.

### Wel en niet

| Niet | Wel | Reden |
|---|---|---|
| cloneert, clonen | clone de repository | geen vernederlandst Engels werkwoord |
| mergen, merget | merge de branch | idem |
| een scriptje, een testje | een script, een test | geen verkleinwoorden voor vakinhoud |
| gewoon, even (als vulwoord) | weglaten | suggereert dat iets triviaal is |
| overkill | te zwaar, buitensporig | Nederlands volstaat |

Vul deze tabel aan zodra er een geval bij komt. Wat hier staat, is de afspraak.

## Aanspreekvorm

- De student is **je**. Consequent, ook in kaders en opdrachten.
- Instructies staan in de gebiedende wijs: "Schrijf een functie", "Voer de code
  uit", "Controleer of ...".
- De auteur is **we** waar dat natuurlijk valt ("we komen hier later op terug"),
  niet "ik" en niet "de docent".

## Opbouw van een tekst

Een beginner moet altijd weten of hij uitleg leest of iets moet doen.

- **Scheid tekstsoorten zichtbaar.** Uitleg, opdracht en controle staan niet
  door elkaar in één alinea.
- **Werk stap voor stap.** Een opdracht met meerdere handelingen wordt een
  genummerde reeks, geen doorlopende alinea.
- **Maak het eindresultaat expliciet.** Bij elke opdracht hoort waaraan de
  student ziet dat het gelukt is: een verwachte uitvoer, een assertion die
  slaagt, een afbeelding die verschijnt.
- **Een kop benoemt de inhoud.** Toets een kop op de plek waar hij zonder
  context verschijnt, zoals de zijbalk: daar moet hij zichzelf dragen.
- **Leerdoelen** formuleer je als wat de student kan, niet als wat is
  opgeleverd.

### De vorm van een opgave

Beknopt betekent niet dat er minder op de pagina staat, maar dat de student
minder hoeft te lezen om te weten wat hij moet doen. Gebruik daarvoor structuur
én selectie: schrap herhaling en zinnen zonder functie. Bewaar de uitleg,
voorbeelden en hints die de student nodig heeft. Uitleg voor een latere stap
krijgt daar een plek, binnen de afgesproken opbouw.

De vaste vorm, uitgewerkt in [`problems/3_basis`](../source/problems/3_basis.ipynb):

1. **Het probleem en zijn context.** Waar dit over gaat en waarom iemand het zou
   willen. Een alinea, geen bladzijde.
2. **De regel of het gegeven**, één keer en volledig, met een uitgewerkt
   voorbeeld. Een tabel is hier vrijwel altijd beter dan proza.
3. **Een overzicht van de stappen.** Wat de student gaat maken, in één tabel of
   lijst, zodat de vorm van het geheel zichtbaar is voordat hij begint.
4. **Genummerde stappen.** `## Stap 1`, `## Stap 2`, enzovoort, elk met een
   koptekst die de functie of handeling noemt. Per stap: één zin specificatie,
   voorbeelden als tabel, eventueel een hint, dan een lege cel en een testcel.
5. **Een afsluiting** die het resultaat plaatst, en waar mogelijk vooruitwijst
   naar wat de student hierna nodig heeft.

Twee dingen daarbij:

**Nummer de stappen ook echt.** Een reeks kopjes zonder nummers laat de student
niet zien waar hij is. Gebruik *stap* voor de delen van één samenhangende opgave
en *opdracht* voor losse oefeningen die niet op elkaar voortbouwen. Welk woord
waar hoort, en hoe je nummert, staat in [begrippen.md](begrippen.md), *Opgave,
opdracht, stap*; dat document bindt hier.

**Klap een hint niet weg.** Een hint achter een dropdown lijkt de pagina rustiger
te maken, maar hij verstopt precies de hulp waarvoor hij bedoeld is. Wie hem niet
nodig heeft, leest eroverheen.

## Leesbaarheid

Behoud noodzakelijke vaktermen en leg ze uit passend bij de plaats in de
leerlijn. Een vaste term ontslaat je niet van uitleg. Vereenvoudig gewone,
onnodig moeilijke formuleringen met behoud van redenering, precieze instructies
en programmeerinhoud.

Gebruik de ruwe LiNT-II-prozascore als redactioneel signaal. De streefgrenzen zijn:

| Tekstfunctie | Profiel | Centrale grens (afgeronde weergave) |
|---|---|---|
| College-uitleg | `introduces` | 45,0 |
| Opgaven en practica | `practises` | 50,1 |
| Naslag en extra | `reference` | 58,0 |

Vergelijk de ruwe score met de ongeronde centrale waarden:
44,961681620883596, 50,11724442358537 en 57,978536074574286.
De jargon-geneutraliseerde analyse helpt bij het kiezen van zinnen, maar verlaagt
het scoredoel niet. De toolstatus `over` begint pas boven de intervalbovengrens
(circa 47,78, 53,34 en 60,50). `borderline` betekent dus niet dat de centrale
streefgrens is gehaald: 46,0 bij `introduces` vraagt nog werk of menselijke afweging.

Stop scoregericht herschrijven zodra de score op of onder de centrale grens ligt
én de tekst inhoudelijk en redactioneel goed is. Onduidelijke uitleg moet ook bij
een lage score worden verbeterd. Na maximaal drie herschrijfronden boven de grens
beslist een mens over het vervolg, waaronder eventueel gemotiveerd behoud.
Zinnen opknippen tot losse labels, fragmenten of lijstjes die alleen de score
verlagen telt niet als verbetering. Bij minder dan 150 gescoorde woorden of een
versnipperingswaarschuwing is passagebeoordeling nodig; de score volstaat dan niet
als stopbewijs.

Een voldoende score bewijst geen taalniveau 3F en is geen gelijkstelling met B1
of B2. [#479](https://github.com/hanze-hbo-ict/programmeren/issues/479) beheert het
inhoudelijke 3F-beoordelingskader en de kleine proef, met woordkeuze, zinsbouw,
structuur, verwijzingen, instructies en voorkennis. Deze scorehulp vervangt dat
menselijke oordeel niet. Ook uitgesloten tekst, zoals code, tabellen en inline
code, moet de auteur lezen. Varianten- en scoresignalen vragen passagebeoordeling;
tellingen leveren vindplaatsen, geen automatische defecten of schrapopdrachten.

De vakdeskundige gaf op 13 november 2026 letterlijk “akkoord” op
[D3: leesbaarheidsnorm](https://github.com/hanze-hbo-ict/programmeren/issues/492#issuecomment-6862594544).
De meetinstructie staat in [technische-conventies.md](technische-conventies.md),
*Leesbaarheid meten*.

## Expressiemiddelen

Materiaal hoeft niet uit lopende tekst te bestaan. De leidende regel: een middel
wordt ingezet waar het het begrip dient, niet als versiering.

- **Kaders** voor een terzijde, een valkuil of een waarschuwing die de hoofdlijn
  niet moet onderbreken. Niet voor tekst die ook een gewone alinea kan zijn.
- **Diagrammen** voor processen en structuren die zich slecht in proza laten
  vangen. Een diagram in Mermaid heeft de voorkeur boven een afbeelding: het is
  eigen werk, versievast en aanpasbaar.
- **Afbeeldingen** waar een visueel voorbeeld iets toont wat tekst niet
  efficiënt kan, zoals een screenshot van een interface. Gebruik alleen eigen
  werk, publiek domein of materiaal met een verenigbare licentie, met
  bronvermelding.
- **Tabellen** voor vergelijkingen met een tweedimensionale structuur. Niet voor
  wat een opsomming ook aankan.
- **Codeblokken** met de juiste taalaanduiding, zodat onderscheid zichtbaar is
  tussen code die de student leest en uitvoer die hij verwacht.

Welke opmaak deze middelen precies vragen, staat in
[technische-conventies.md](technische-conventies.md).

## Samenhang bewaken

Materiaal groeit, en met elke toevoeging ontstaan afhankelijkheden tussen
plekken. Dit materiaal draagt daar de littekens van: dezelfde opgave in meerdere
varianten, verwijzingen naar bestanden die niet meer bestaan, en uitleg die op
twee plekken half hetzelfde beweert.

- **Eén bron van waarheid.** Een feit staat op één plek; andere plekken
  verwijzen ernaar en herhalen het niet.
- **Codeer geen afleidbare staat hard.** Schrijf niet in proza op welke weken
  al een practicum hebben; laat de structuur dat dragen.
- **Hef een afhankelijkheid liever op dan haar te onthouden.** Dwingt een
  wijziging hier een wijziging daar af, maak die band dan overbodig. Kan dat
  niet, leg dan vast waar de andere plek zit.
- **Kruisverwijzingen moeten altijd kloppen.** Een zin die zegt waar iets anders
  staat - "dat heb je in week 2 gezien", "in het practicum schrijf je die
  functie zelf" - is een bewering over ander materiaal, en die veroudert zodra
  dat materiaal schuift. Verplaats je een onderdeel naar een andere week of een
  andere bijeenkomst, of verwijder je het na goedkeuring door de vakdeskundige,
  zoek dan de zinnen op die ernaar wijzen en werk ze in dezelfde wijziging bij.
  Een dode link vangt de build; een verwijzing die nog werkt maar niet meer waar is, vangt
  niemand. **Loopt stil af**, en dat maakt hem duur: de student leest een
  aanwijzing die hem naar de verkeerde plek stuurt.

Deze controle bij verwijderen verduidelijkt de bestaande regel
*Wat er niet meer toe doet, mag weg* in
[`curriculum/uitgangspunten.md`](../curriculum/uitgangspunten.md).
De vakdeskundige beslist nog steeds per directory wat weg mag.
Vastgesteld op 28 oktober 2026, [C4 van #445](https://github.com/hanze-hbo-ict/programmeren/issues/445#issuecomment-6466878171), punt 11.

## Opmaak en interpunctie

- Nederlandse interpunctie.
- Gebruik voor een gedachtestreep spatie-koppelteken-spatie ( - ). **Geen
  em-dash en geen en-dash.** Het materiaal voldoet hier nu al aan; deze regel
  legt dat vast. De em-dash is de meest herkenbare tell van modeltekst, en
  daarmee de enige harde, toetsbare uitwerking van de regel hierboven.
  Het verbod op de em-dash en de en-dash geldt voor wat gepubliceerd wordt: het
  boek, dus `source/` (zie *Reikwijdte* in [conventies.md](conventies.md)). In
  interne documenten buiten het boek, zoals die in `curriculum/`, `conventies/`
  en `onderzoek/`, en ook in `README.md`, mogen ze wel. Vastgesteld door de
  vakdeskundige op 24 september 2026, naar aanleiding van de beoordeling van
  PR #291.
- Spaarzaam met vetgedrukte tekst en opsommingen; alleen waar ze de structuur
  echt verhelderen.
- Verwijs naar bestanden en directories als inline code.

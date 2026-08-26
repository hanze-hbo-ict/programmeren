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
  Nederlandse vertaling voor `string`, `list`, `debuggen` of `commit`.
- Introduceer een Engelse term bij eerste gebruik kort in het Nederlands, en
  gebruik daarna alleen de Engelse. Voor beginners is die eerste toelichting
  wél nodig, anders dan bij ouderejaars.
- Vervoeg Engelse termen niet tot hybriden. Niet "je cloneert de repository",
  wel "clone de repository".
- Eén begrip, één term. Wissel niet ongemerkt tussen synoniemen.

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
minder hoeft te lezen om te weten wat hij moet doen. Structuur doet dat werk,
niet weglaten.

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
en *opdracht* voor losse oefeningen die niet op elkaar voortbouwen.

**Klap een hint niet weg.** Een hint achter een dropdown lijkt de pagina rustiger
te maken, maar hij verstopt precies de hulp waarvoor hij bedoeld is. Wie hem niet
nodig heeft, leest eroverheen.

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

## Opmaak en interpunctie

- Nederlandse interpunctie.
- Gebruik voor een gedachtestreep spatie-koppelteken-spatie ( - ). **Geen
  em-dash en geen en-dash.** Het materiaal voldoet hier nu al aan; deze regel
  legt dat vast. De em-dash is de meest herkenbare tell van modeltekst, en
  daarmee de enige harde, toetsbare uitwerking van de regel hierboven.
- Spaarzaam met vetgedrukte tekst en opsommingen; alleen waar ze de structuur
  echt verhelderen.
- Verwijs naar bestanden en directories als inline code.

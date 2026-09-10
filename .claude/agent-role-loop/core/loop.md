# De rollenlus

Dit is de gedeelde routenorm voor Claude en Codex. Contracten staan in
[contracts/](contracts/), verantwoordelijkheden in [roles/](roles/) en de
principes in [principles.md](principles.md). De uitleg voor mensen staat in
[rollen/rollen.md](../../../rollen/rollen.md).

## Invoering

De werkwijze van #203 geldt voor nieuw gestarte routes na goedkeuring van de
instructie-PR. Een lopende route blijft bij zijn vastgelegde C1 en procesversie;
raadpleeg daarvoor de versie van deze bestanden bij de startcommit. Zet haar niet
halverwege om. Registreer bij iedere nieuwe C1 de gebruikte commit.
De proef en het evaluatiemoment staan in
[onderzoek/203-proef.md](../../../onderzoek/203-proef.md).

## Route kiezen

De orkestrator schrijft C1 zelf, op basis van C0. Een aparte triage-agent is
beschikbaar op verzoek, geen standaardstap. C1 noemt omvang, verantwoordelijkheden,
uitvoerende agents, criteriumtoewijzing en de reden voor extra rollen.
`DOORLOPEND` blijft open als verzamelplek; `AFWIJZEN` geeft gericht advies.

Voor `LUS` gelden deze uitgangspunten:

| Werk | Route |
|---|---|
| Kleine, eenduidige correctie | auteur, onafhankelijke beoordelaar; uitvoeropdracht is C0 + C1 |
| Overzichtelijke opgave of sectie | gecombineerde verkenner/ontwerper, mens, auteur, onafhankelijke beoordelaar |
| Ingrijpende weekherziening | verkenner, ontwerper, verhelderaar, mens, auteur, twee onafhankelijke beoordelaars |

Een verantwoordelijkheid hoeft geen eigen agent te zijn. De gecombineerde rol
wordt uitgevoerd door `rol-curriculumontwerper` en levert C2 met meetbasis.
Geen lege C1b, C2, C3 of C4 maken voor een stap die niet nodig is.

Voeg gericht toe:

- **Aparte verkenner:** omstreden dragende feiten of een inventarisatie die meerdere
  ontwerpkeuzes moet dragen. Levert C1b, zonder voorstellen.
- **Verhelderaar:** onderling afhankelijke onderdelen of onzekerheid over de
  uitvoerbaarheid van het verificatieplan. Toetst C2; niet automatisch na elk C2.
- **Mens:** altijd vóór uitvoering van een ontwerp, en ook zonder ontwerp bij
  verwijderen van materiaal, verplaatsen tussen vakken of een nieuw inhoudelijk
  besluit. C4 kan dan naar de concrete uitvoeropdracht in C0 + C1 verwijzen.
  Een wijziging aan curriculum of conventies vraagt de mens, niet automatisch
  alle agents. Een al gegeven expliciet besluit vastleggen, niet opnieuw vragen.

De omvang bepaalt de diepte: XS/S/M meet en ontwerpt alleen wat de taak nodig
heeft; L/XL neemt de omgeving mee waar afhankelijkheden dat vragen. Een vak
herindelen eerst opsplitsen. Bij twijfel benoemt C1 de concrete onzekerheid en
kiest de verantwoordelijkheid die haar kan oplossen.

## Beoordeling toewijzen

Bij studentmateriaal is de **eerstejaars** de eerste beoordelaar. Hij krijgt geen
uitwerkingen te zien. Bij verandering van didactische opzet komt de
**onderwijskundige** erbij; bij een weekherziening is dit standaard de tweede.
Bij omvangrijke redactionele wijzigingen komt de **redacteur** erbij, of vervangt
hij de onderwijskundige als de didactiek gelijk blijft. Bij uitsluitend proces-
of normtekst is de redacteur de eerste beoordelaar.

C1 wijst ieder acceptatiecriterium toe aan minstens één passende beoordelaar.
C2 kan criteria toevoegen; werk die toewijzing dan vóór beoordeling bij.
Criteria over uitwerkingen gaan naar een beoordelaar die ze mag lezen en
verifiëren: de onderwijskundige, of bij uitsluitend redactioneel werk de redacteur.
Voeg die rol toe als hij ontbreekt. Een klein aantal agents mag geen gat in de
controle veroorzaken. Iedere beoordelaar toetst zijn criteria, de relevante
conventies en objectief verificatiebewijs naast zijn eigen perspectief.

De **pragmaticus** is beschikbaar op verzoek. Proportionaliteit en het onderscheid
tussen blokkades en puntjes gelden voor elke rol en vragen geen vaste extra agent.
De **hoofdredacteur** draait alleen bij onopgeloste tegenspraak tussen oordelen.
Bij één beoordelaar volstaat C6. Bij meer beoordelaars zonder tegenspraak publiceert
de orkestrator C7 als mechanische samenvatting met bronverwijzingen, zonder eigen
bevindingen: een onopgeloste blokkade blijft BLOKKEER. Een inhoudelijk verschil van
duiding dat bronnen niet beslechten gaat naar de mens. De mens beslist over merge.

## Invoer en context

| Stap | Invoer | Uitvoer |
|---|---|---|
| triage door orkestrator | C0, relevante staande zaken | C1 |
| aparte verkenner indien gekozen | C0 + C1 | C1b |
| ontwerper, eventueel gecombineerd | C0 + C1, C1b indien aanwezig | C2 met meetbasis |
| verhelderaar indien gekozen | C0 + C1 + C2 | C3 |
| mens indien verplicht | C2 + eventueel C3, of concrete C0 + C1 | C4 |
| auteur | C1, C2 + C4 of C0 + C1; toepasselijk C4 en C3-verbeterpunten | C5 |
| gekozen beoordelaars | C1-toewijzing + C5-kern | C6 per beoordelaar |
| samenvoeging of arbitrage indien nodig | alle gekozen C6; volledige C5 bij arbitrage | C7 |

Geef de artefacten letterlijk mee of via leesbare bestanden, inclusief relevante
vastgestelde besluiten met exacte bronnen. Geef gerichte vindplaatsen van normen,
geen nieuwe kopie van alle conventies. Een rol mag de oorspronkelijke bron lezen
waar nodig; een verwijzing naar een onbereikbaar issue is geen overdracht.

Iedere onafhankelijke beoordeling begint in een verse context. Geen
maaktranscript, geen afwegingen uit het uitgebreide C5 en bij de eerste
beoordeling geen andere oordelen. Objectief verificatiebewijs en geldende
besluiten staan juist wél in C5-kern. De auteur mag zijn context behouden bij een
gerichte reparatie. Schrijven gebeurt achter elkaar, onafhankelijke beoordelaars
kunnen parallel draaien.

## Herstellen en stoppen

Na C3 FAAL repareert de ontwerper het bestaande C2 op de genoemde blokkades;
geen automatische volledige herschrijving. Na C6/C7 BLOKKEER repareert de auteur
de genoemde blokkades. Geef steeds artefact, criterium-ID's, bevindingen en
relevante besluiten mee. Een gewijzigde scope of nieuw inhoudelijk besluit vraagt
eerst de mens. Een HERZIEN van de mens is geen automatische reparatieronde.

Per ontwerp en per oplevering is maximaal **één automatische herstelronde**
toegestaan, inclusief herbeoordeling. De orkestrator telt dit op GitHub; een nieuwe
agent, context of sessie zet de teller niet terug. Blijft daarna een blokkade,
leg dan gericht doorgaan, opsplitsen of stoppen voor. Hervatten kan alleen met
expliciet besluit en een nieuwe begrensde opdracht. Puntjes kosten geen ronde.

Herbeoordeling heeft expliciet **herstelmodus**. De verse beoordelaar krijgt de
bijgewerkte C5-kern, reparatiediff, eerdere blokkerende bevindingen met criterium-ID
en eerdere dekking van niet-geraakte criteria. Dit is geen nieuwe blinde
beoordeling. Hij toetst de reparatie en de daardoor geraakte criteria; overgenomen
dekking heet *eerder vastgesteld*, niet *opnieuw onderzocht*. Gebruik dezelfde
werkwijze bij C3-herbeoordeling van het gewijzigde ontwerp.

Een volledige herbeoordeling volgt alleen bij gewijzigde scope, gedeelde
afhankelijkheden die eerder bewijs ongeldig maken of een onbetrouwbare basis.
Leg reden, nieuwe toewijzing en kostenafweging vast. Dit omzeilt de rondelimiet
niet. Nieuwe echte defecten blijven zichtbaar; een budget maakt ze niet groen.

## Verificatie en eindpunt

Mechanische controles gaan vóór beoordeling. Draai pre-commit op geraakte
bestanden; bij boek-, buildconfiguratie- of dependencywijzigingen ook een schone
Sphinx-build met nul waarschuwingen en fouten. Bij uitsluitend procesdocumentatie
is die build niet nodig: noteer reikwijdte en toepasselijke controles. Installeer
geen nieuw gereedschap; stel vast wat beschikbaar is. Meet het ding zelf:
uitvoer uitvoeren, een pagina bekijken, een zoekpatroon ijken vóór je nul gelooft.

Elk criterium heeft een concrete eindvoorwaarde. Voor proces- of normtekst is dat
een eindige wijzigingslijst of scenario met verwachte uitkomst; geen onbegrensd
"alles is consistent". De auteur levert pas C5 wanneer de relevante controles
groen zijn. Een niet uitgevoerde controle staat als niet vastgesteld, niet als groen.

## GitHub en registratie

C0 is een GitHub-issue, overdrachten zijn reacties op issue of PR. Iedere reactie
bevat contract-ID en meetregel: rol, ronde, tokens, duur, omvang en uitkomst.
Ontbrekende meetgegevens heten **niet beschikbaar**, nooit nul. Bij een afgebroken
run noteer je wat bewaard bleef. Tokenregistratie is geen factuurbedrag.

Noteer ook de kosten van orkestratie indien beschikbaar. Neem de meetregels over
in `onderzoek/metingen.md` bij afsluiting of vóór sessie-einde. Structurele
bevindingen krijgen bewijs en gevolg in `onderzoek/bevindingen.md`.
Procesbesluiten landen in `onderzoek/`; inhoudelijke besluiten in `curriculum/`
of `conventies/`. Een door de orkestrator geschreven besluittekst krijgt
onafhankelijke redactionele beoordeling op de diff en het menselijke bronbesluit;
dit mag onderdeel zijn van de al gekozen beoordeling.

De budgetreactie tijdens de #203-proef staat in
[onderzoek/203-proef.md](../../../onderzoek/203-proef.md). Geen automatische
extra agentstart nadat de daar afgesproken grens is overschreden.

## Buiten een werkitem

Een kleine correctie mag zonder aparte issue, in een branch met PR en een
onafhankelijke lezer volgens dezelfde criteriumtoewijzing. Noteer dit onder
*Werk buiten de lus om* in `onderzoek/metingen.md`.

Een leesronde op bestaand materiaal is beschikbaar volgens C6, niet verplicht
vóór ieder ontwerp. De **eindredacteur** bewaakt periodiek samenhang over weken;
de **onderzoeker** onderzoekt periodiek de werkwijze. Beiden blijven buiten de lus.

# De rollenlus als experiment

> **Gesloten op 20 oktober 2026.** Deze map is een archief en wordt niet meer
> bijgehouden: er komen geen metingen, bevindingen of procesbesluiten meer bij, en
> wat er staat blijft staan zoals het is opgeschreven - ook waar het in de
> tegenwoordige tijd spreekt over een werkwijze die sindsdien is veranderd. De
> ingang is [`retrospectief.md`](retrospectief.md), de laatste oplevering van de
> onderzoekersrol; die rol is met de track vervallen. De lus zelf blijft en staat
> beschreven in [`../rollen/rollen.md`](../rollen/rollen.md).

Dit is de onderzoekskant van deze repository. Hier staat wat we over de
**werkwijze** leren, gescheiden van het werk aan het materiaal zelf.

De scheiding is met opzet. Wie het cursusmateriaal onderhoudt heeft niets aan een
tokentelling; wie de werkwijze wil begrijpen of overnemen heeft niets aan de vraag
of week 5 een raster doorloopt. En een observatie die alleen in een commitbericht
staat, is over een half jaar niet terug te vinden.

## De vraag

Kun je cursusmateriaal onderhouden met taalmodellen die het werk niet alleen
uitvoeren maar ook verdelen - en levert het verdelen over rollen met een eigen,
geïsoleerde context beter werk op dan één agent die alles doet?

Concreet: agents meten wat er staat, ontwerpen de herziening, schrijven het
materiaal en beoordelen elkaars werk. Een mens schrijft het werkitem, beslist bij de
poort halverwege, en merget. De vraag is of die verdeling de fouten vangt die één
agent maakt, en tegen welke prijs.

De aanleiding is een concrete: deze repository is niet stukgegaan aan één slechte
wijziging, maar aan veel wijzigingen die ieder op zich verdedigbaar waren en samen
de samenhang hebben opgegeten. Een betere reviewer lost dat niet op. De hypothese
is dat contextisolatie het wel doet: wie meet weet niet wat de uitkomst zou moeten
zijn, wie beoordeelt heeft de worsteling van de schrijver niet gezien, en tussen
twee rollen gaat precies één artefact.

## Wat dit geen experiment maakt in de strikte zin

Er is geen controlegroep en er zijn geen herhalingen. Wat er wel is: een
werkelijke repository met werkelijke gebreken, een reeks ingrepen waarvan de kosten
en de uitkomsten zijn opgeschreven, en een werkwijze die onderweg is bijgesteld op
grond van wat er misging. De waarde zit in de gevalsbeschrijving, niet in de
statistiek.

Waar een bevinding op één waarneming rust, staat dat erbij.

## Wat hier staat

| | |
|---|---|
| [`retrospectief.md`](retrospectief.md) | Wat de hele reeks heeft opgeleverd; de ingang tot dit archief |
| [`metingen.md`](metingen.md) | Wat een ronde kost, per rol, per keer |
| [`bevindingen.md`](bevindingen.md) | Wat we over de werkwijze hebben geleerd, met het bewijs en wat het veranderde |

De werkwijze zelf staat in [`../rollen/rollen.md`](../rollen/rollen.md) (voor
mensen) en in `../.claude/agent-role-loop/core/` (de definities die de agents
lezen). Dit document beschrijft niet hoe de lus werkt; het beschrijft wat we ervan
leren.

## Hoe dit is bijgehouden

Een meting werd genoteerd zodra een rol klaar was, want de gegevens bestonden verder
alleen in de sessiecontext; dat was een verplichting van de orkestrator, omdat alleen
die de tokentelling te zien kreeg. Een bevinding werd genoteerd zodra iets misging op
een manier die niet aan dat ene geval lag, met erbij wat het veranderde - een
bevinding zonder gevolg is een anekdote.

Wie de bevinding opschreef, was degene die de fout voelde. Dat was met opzet zo: de
bruikbaarste bevindingen kwamen voort uit het merken dat een getal niet klopte met
wat er net was gedaan, niet uit het achteraf lezen van een transcript.

Periodiek las de **onderzoeker** dit alles en vroeg wat eruit volgde: wat keerde
terug, was een bevinding werkelijk geland, en gebeurde het daarna nog een keer. Die
rol stond buiten de lus, naast de eindredacteur, en draaide zelden. Haar laatste
oplevering is het retrospectief dat deze track heeft afgesloten.

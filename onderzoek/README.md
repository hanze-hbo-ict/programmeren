# De rollenlus als experiment

Dit is de onderzoekskant van deze repository. Hier staat wat we over de
**werkwijze** leren, gescheiden van het werk aan het materiaal zelf.

De scheiding is met opzet. Wie het cursusmateriaal onderhoudt heeft niets aan een
tokentelling; wie de werkwijze wil begrijpen of overnemen heeft niets aan de vraag
of week 5 een raster doorloopt. En een observatie die alleen in een commitbericht
staat, is over een half jaar niet terug te vinden.

## De vraag

Kun je het onderhoud van cursusmateriaal beter doen door het werk te verdelen over
rollen met een eigen, geïsoleerde context, dan door één assistent alles te laten
doen?

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
| [`metingen.md`](metingen.md) | Wat een ronde kost, per rol, per keer |
| [`bevindingen.md`](bevindingen.md) | Wat we over de werkwijze hebben geleerd, met het bewijs en wat het veranderde |

De werkwijze zelf staat in [`../rollen/rollen.md`](../rollen/rollen.md) (voor
mensen) en in `../.claude/agent-role-loop/core/` (de definities die de agents
lezen). Dit document beschrijft niet hoe de lus werkt; het beschrijft wat we ervan
leren.

## Hoe je hieraan bijdraagt

Noteer een meting zodra een rol klaar is, want de gegevens bestaan verder alleen in
de sessiecontext. Dat is een verplichting van de orkestrator: alleen die krijgt de
tokentelling te zien. Noteer een bevinding zodra iets misgaat op een manier die niet
aan dat ene geval ligt - en schrijf erbij wat het veranderde, want een bevinding
zonder gevolg is een anekdote.

Wie de bevinding opschrijft, is degene die de fout voelde. Dat is met opzet zo: de
bruikbaarste bevindingen van deze week kwamen voort uit het merken dat een getal
niet klopte met wat er net was gedaan, niet uit het achteraf lezen van een
transcript.

Periodiek leest de **onderzoeker** dit alles en vraagt wat eruit volgt: wat keert
terug, is een bevinding werkelijk geland, en gebeurde het daarna nog een keer. Die
rol staat buiten de lus, naast de eindredacteur, en draait zelden - na één ronde is
er geen patroon.

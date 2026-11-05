# Rubric PGM2-oefententamen

Deze docentrubric hoort bij de zes herziene opgaven in
`source/extra/practice/PGM2_examen.md` en de bijbehorende uitwerking in
`source/solutions/PGM2_examen.ipynb`. Totaal: 100 punten. Zij doet geen uitspraak
over het echte tentamen of haalbare studenttijd.

Besluit: [C4 #470](https://github.com/hanze-hbo-ict/programmeren/issues/470#issuecomment-6662338378),
5 november 2026. Gehele deelpunten volgens
[C2-addendum](https://github.com/hanze-hbo-ict/programmeren/issues/470#issuecomment-6662364884).
De bewijsgrenzen en eenmalige weektoerekening in `curriculum/leeruitkomsten.md`
blijven gelden. Toetscontext of paradigma levert geen extra weekbudget op.

## Beoordeling per prestatie

Ken per onderstaande deelprestatie uitsluitend de genoemde punten toe wanneer
de prestatie aan het opdrachtcontract voldoet; anders nul. Splits een genoemde
prestatie niet verder op met ongeschreven deelpunten. Bij 1 omvat elke regel
alle drie functies, respectievelijk de hele keten of wijzigingsonderbouwing.
Geldige afwijkende implementaties krijgen dezelfde punten. Een fout kost alleen
de betrokken prestatiepunten; werkende code, tests en vorm krijgen geen tweede
algemene beloning. Ontwerp- of analysepunten worden bij ontbreken niet als
L2/L3-toepassing herboekt.

| Opgave | LU | Waarneembare prestatie | Punten |
|---|---|---|---:|
| 1 | L5 | Verantwoordelijkheid, invoer en resultaat van elk van de drie functies verklaren. | 5 |
| 1 | L5 | Gegevens- en aanroepafhankelijkheden in de keten verklaren met `spel.exe` en beide suffixen. | 5 |
| 1 | L5 | Geschikte wijzigingsplaats voor hoofdletterongevoeligheid onderbouwen en gevolgen voor functies en aanroepen verklaren. | 5 |
| 2 | L2 | Comprehension met juiste even-selectieconditie. | 2 |
| 2 | L2 | Comprehension bouwt juiste resultaatlijst in invoervolgorde, inclusief duplicaten. | 3 |
| 2 | L2 | Recursief basisgeval voor lege lijst. | 1 |
| 2 | L2 | Recursieve aanroep met kleinere invoer die termineert. | 2 |
| 2 | L2 | Correcte recursieve selectie en combinatie. | 2 |
| 2 | L2 | Meegegeven predicaat daadwerkelijk aanroepen voor elk getal. | 2 |
| 2 | L2 | Resultaat van predicaat verwerken tot juiste selectie. | 3 |
| 3 | L1 | Dictionary met studentnummer als sleutel maken; laatste registratie vervangt eerdere volledig. | 3 |
| 3 | L1 | Cijfer en huiswerk gericht opzoeken en eenmaal bonus toevoegen aan definitieve registratie. | 3 |
| 3 | L1 | Dictionary verwerken tot gesorteerd overzicht met juiste cijfers. | 3 |
| 3 | L1 | Set unieke definitieve huiswerkmakers maken. | 3 |
| 3 | L1 | Lidmaatschap controleren en setverschil met alle deelnemers voor ontbrekende groep gebruiken. | 3 |
| 4 | L3 | Staat, legale zet en eindcontrole implementeren, ook bij minder dan drie lucifers. | 7 |
| 4 | L3 | Nim en spelers via interface laten samenwerken; beurtwisseling, stop en winnaar volgens contract. | 7 |
| 4 | L3 | StrategicPlayer erft over, overschrijft zetkeuze en wordt verwisselbaar gebruikt zonder typetest. | 6 |
| 4 | L3 | Posities met `__eq__` vergelijken volgens contract, zonder mutatie. | 5 |
| 4 | L4 | Ongeldige zet rechtstreeks in zetmethode vóór mutatie met `ValueError` signaleren. | 5 |
| 4 | L4 | Specifiek `ValueError` afvangen, melden en dezelfde beurt vervolgen met ongewijzigde spelstaat. | 5 |
| 5 | L2 | Correcte recursieve functie voor niet-lege kleineletterwoorden, Nederlandse docstring en minstens drie betekenisvolle assertions samen; alles of niets. | 5 |
| 6 | L6 | Zelf gekozen, niet voorgeschreven strategie kort onderbouwen. | 5 |
| 6 | L6 | Zelf gekozen structuur/taakverdeling kort onderbouwen. | 5 |
| 6 | L6 | Correcte implementatie van die keuze met functionele of OO-constructies en het scorecontract. | 5 |

Bij Nim beloont L3 de geldige toestandsverandering; de afzonderlijke L4-regel
beloont het foutpad vóór mutatie. Alleen invoercontrole of een brede `except`
levert de L4-punten niet op. Bij 5 blijft het nieuwe blok ondeelbaar. Andere
vormvereisten zonder eigen rubricpunten zijn checklistvoorwaarden en geven geen
ongeschreven puntenaftrek. Bij 6 is één zelf ontworpen functie met comprehension
of recursie geldig; een `def` rond geheel imperatieve code bewijst de vereiste
functionele keuze niet. Een contractconforme OO-keuze is even geldig.

## Alle oude punten afgehandeld

De oude punten verdwijnen waar zij vervangen of vervallen zijn. Oude en nieuwe
punten worden niet opgeteld. De twee behouden deelvragen blijven elk 5 punten.

| Oude eenheid | Oud | Bestemming |
|---|---:|---|
| 1 Extensies | 10 | Vervangen door 15 L5-punten; gegeven recursie is onbeloonde analyse-invoer. |
| 2a lus | 5 | Vervallen als toetscriterium; bruikbare PGM1-voorkennis. |
| 2b comprehension | 5 | Behouden als 5 L2-punten met expliciete rubric. |
| 2c recursie | 5 | Behouden als 5 L2-punten met expliciete rubric. |
| 3 Bonus | 10 | Vervangen door 15 L1-punten. |
| 4.1 player_takes | 5 | Vervangen binnen nieuw L3-contractblok van 25 punten. |
| 4.2 AI_turn | 5 | Vervangen binnen spelers-/polymorfismecontract van datzelfde blok. |
| 4.3 game_over | 5 | Vervangen binnen datzelfde L3-contractblok. |
| 4.4 computerbeurt | 5 | Vervangen door samenwerking in datzelfde blok en apart L4-foutpad van 10 punten. |
| 5 Alfabetisch incl. docstring/assertions | 15 | Hele ongesplitste blok vervangen door nieuw ongesplitst blok van 5 L2-punten; geen historische deelrubric. |
| 6 Moeilijke woorden | 20 | Vervangen door 15 L6-punten met vrije strategie en structuur. |

Oud: 10+5+5+5+10+5+5+5+5+15+20 = 90. De toegevoegde
predicaatprestatie bij 2 krijgt 5 punten. Nieuw: 15+15+15+35+5+15 = 100.
L1–L6: 15/20/25/10/15/15; niveaus: toepassen 70, analyseren 15, creëren 15.
Het cijfer is `1 + 9 * behaalde punten / 100`; de basis 1 krijgt geen puntenbudget.

## Contractcontroles

De uitwerking controleert lege/gelijke suffixen, te lange suffixen, selectie en
volgorde; lege en negatieve/even/oneven getallen en twee predicaten; dubbele
studentregistraties en ontbrekende huiswerkmakers; geldige en ongeldige Nim-zetten,
kleine restposities, overerving, verwisselbare aanroepen en vergelijking zonder
mutatie; één/gelijke/stijgende/dalende letters; de vier scorevoorbeelden en de
grenzen 10/11 tekens en 15/16 woorden. De interactieve Nim-besturing wordt
bovendien met vaste invoer gecontroleerd. Assertions zijn bewijs voor de code;
de analyse en de onderbouwingen worden inhoudelijk beoordeeld.

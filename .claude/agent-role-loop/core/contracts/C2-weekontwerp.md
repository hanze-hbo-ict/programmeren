# C2 - Weekontwerp

## Doel

Wat de curriculumontwerper oplevert en waar de auteur zich uitsluitend op baseert:
een uitvoerbaar ontwerp, gegrond in de bevindingen van de verkenner en in
`curriculum/`. Een goed ontwerp laat de auteur werken zonder eisen te verzinnen,
en laat de verhelderaar en de vakdeskundige oordelen zonder het onderzoek over te
doen. Hier wordt ook per onderdeel gekozen hoe wordt vastgesteld dat het klopt.

## Schema

Secties, in deze volgorde:

- **Samenvatting** - één alinea.
- **Doelen** - genummerd.
- **Niet-doelen** - wat uitdrukkelijk buiten dit werk valt.
- **Huidige staat** - de feiten zoals ze nu zijn, uit de bevindingen. Markeer
  wat niet is vastgesteld als aanname.
- **Voorgestelde opzet** - de vorm van de oplossing en de dragende keuzes, met
  hun grond.
- **Acceptatiecriteria** - genummerd en toetsbaar; overgenomen uit C0 of afgeleid
  (en dan als afgeleid gemarkeerd).
- **Wat dit raakt buiten deze week** - andere weken, `curriculum/`, `conventies/`,
  of `<geen>`. Een gevolg dat elders neerslaat hoort hier, niet in iemands hoofd.
- **Onderdelen** - één blok per apart beoordeelbaar onderdeel (zie hieronder).
- **Risico's** - of `<geen>`.
- **Aannames** - of `<geen>`.
- **Open vragen** - of `<geen>`. Vragen voor de vakdeskundige horen hier.

Per onderdeel:

- **Doel** - één zin.
- **Niet-doelen** - of `<geen>`.
- **Bestanden** - wat wordt aangeraakt; markeer gissingen als aanname.
- **Checklist** - geordende vinkjes.
- **Verificatieplan** - een van:
  - `assertions-draaien` - de uitwerking draait bij de build en de assertions
    slagen. Het uitgangspunt voor alles met code.
  - `uitvoer-nagerekend` - verwachte uitvoer is berekend tegen de echte
    databestanden. **Motivering verplicht** als niet voor het eerste is gekozen.
  - `handmatig-met-verwachte-uitkomst` - concrete stappen, elk met het resultaat
    dat als geslaagd telt. Voor materiaal zonder code. **Motivering verplicht.**
- **Klaar wanneer** - de objectieve voorwaarde, met verwijzing naar de
  acceptatiecriteria.

## Waar je tegenaan ontwerpt

De toetsmatrijs ligt vast. De doelgroep is gemengd. Wat deze week gebruikt moet
eerder zijn geïntroduceerd, en wat volgende week veronderstelt moet hier zijn
geleverd. Een opgave lost bij voorkeur een probleem op in plaats van een
constructie te oefenen. Zie [`rollen/curriculumontwerper.md`](../../../../rollen/curriculumontwerper.md).

## Voorbeeld

Verkort tot één onderdeel.

```md
## Samenvatting
Week 7 draagt mutabiliteit en dictionaries, en die vechten om dezelfde ruimte:
twaalf koppen tegen twee. Beide moeten blijven, dus de week wordt herverdeeld in
plaats van dat er iets uit gaat.

## Doelen
1. Dictionaries krijgen de behandeling die PGM2 week 1 veronderstelt.
2. Mutatie wordt benoemd als grens in plaats van als techniek.

## Niet-doelen
- Het werkcollege wijzigen; Markov blijft zoals het is.

## Huidige staat
Geen opstap. Basis is 453 woorden en een getallenpuzzel. Van de 29 koppen in
het college gaan er 2 over dictionaries.

## Voorgestelde opzet
Tekstanalyse als basis, teruggehaald uit `v1.0.0`, waar het college
`Woorden tellen` en `Unieke woorden` had die geen van beide zijn overgeleverd.
Dezelfde structuur als het werkcollege: woord naar aantal in plaats van woord
naar opvolgers.

## Acceptatiecriteria
1. Basis opent met een concreet probleem.
2. De week heeft een opstap die dekt wat de basis vraagt.
3. Voldoet aan de conventies in `conventies/conventies.md`, en de build is schoon.

## Wat dit raakt buiten deze week
- `conventies/codeconventies.md`: de methodegrens verschuift naar week 7.
- #96: de opgaven van deze week hebben nul uitvoerbare cellen.

### Onderdeel 1: basisopgave tekstanalyse

**Doel:** een opgave waarin de student woordfrequentie berekent uit een bestand.

**Niet-doelen:** <geen>

**Bestanden:** `problems/7_basis.ipynb`, `solutions/7_basis.ipynb`,
`problems/assets/teksten/` (nieuw)

**Checklist:**
- [ ] Twee tekstbestanden, waarvan één met de hand na te rekenen
- [ ] Zes stappen, elk met testcel
- [ ] Uitwerking met docstrings en toelichting per functie

**Verificatieplan:** `assertions-draaien`
- De uitwerking draait bij de build; elke assertion is eerst tegen de echte
  bestanden berekend.

**Klaar wanneer:** AC1 en AC2 gehaald, en de build toont de uitvoer van `report`.

## Risico's
- Twee nieuwe onderdelen in de laatste week van een periode.

## Aannames
- De student heeft in week 6 leren lezen uit een bestand.

## Open vragen
1. P4 vraagt letterlijk om "de bijbehorende methodes" terwijl de conventie ze
   verbiedt. Voorstel: de methodegrens valt samen met de mutatiegrens in week 7.
```

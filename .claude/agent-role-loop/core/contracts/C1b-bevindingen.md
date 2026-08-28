# C1b - Bevindingen

## Doel

Wat de verkenner oplevert: de feitelijke staat van het materiaal, met de meting
erbij, zodat de curriculumontwerper erop kan ontwerpen zonder zelf te gaan
graven. Dit contract bestaat omdat meten hier een eigen rol is; in het bronmodel
verkent de planner zelf en is er geen apart artefact.

**Feiten, geen oordeel.** Een bevinding die de volgende rol niet kan narekenen,
is een mening.

## Schema

- **Wat er staat** - per bestand: soort, omvang, structuur. Per niveau het
  totaal. Noem ontbrekende niveaus en gaten in de nummering.
- **Tegenover de conventies** - overtredingen, geteld, met vindplaats.
- **Tegenover de leerlijn** - welke leeruitkomsten hier landen, met weging en
  niveau, naast wat het materiaal daadwerkelijk aanbiedt.
- **Wat er ooit stond** - wat `v1.0.0` op deze plek had en wat daarvan over is.
- **Vooruitverwijzingen** - begrippen die eerder opduiken dan de leerlijn ze
  plaatst, met vindplaats en verschil in weken.
- **Ontbrekende bestanden** - alles waarnaar wordt verwezen en dat er niet is.
- **Niet vastgesteld** - of `<geen>`. Wat je niet kon meten zonder een vervanger
  te meten. Dit veld is verplicht aanwezig; leeg laten mag, weglaten niet.

Elk onderdeel draagt de meting: het commando, het getal, of de manier waarop het
is vastgesteld.

## Voorbeeld

```md
## Wat er staat
| Bestand | Woorden | Cellen |
|---|---|---|
| lectures/7a_lists_advanced.ipynb | 1001 | 118 (59 markdown, 59 code) |
| problems/7_basis.ipynb | 453 | 18, alle markdown |

Er is geen opstap. Week 7 is de enige week van PGM1 zonder.

## Tegenover de conventies
Het college heeft 59 codecellen en nul met `skip-execution`, dus alle 59 draaien
bij de build. Onder `## Quiz` staan drie vragen van de vorm "wat wordt geprint?",
elk gevolgd door een cel die het antwoord afdrukt.

Gemeten met: telling van `metadata.tags` over alle codecellen.

## Niet vastgesteld
Of het practicum in drie bijeenkomsten past. Dat is niet uit de repo te meten.
```

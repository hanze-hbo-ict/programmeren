# C6 - Beoordeling

## Doel

Het onafhankelijke oordeel van één beoordelaar over de **kern** van de oplevering
(C5). Vier beoordelaars leveren er elk één, geïsoleerd: geen van hen ziet het
oordeel van een ander voordat het eigen oordeel af is. De beoordeling scheidt wat
moet veranderen van wat kan veranderen, en herleidt elk acceptatiecriterium tot
bewijs.

## Schema

Verplichte velden:

- **Oordeel** - `BLOKKEER` / `AKKOORD` / `AKKOORD MET PUNTJES`.
- **Dekking van de acceptatiecriteria** - per criterium: `gehaald` of `niet
  gehaald`, plus het bewijs waarop je je baseert.
- **Afwijking van wat is opgegeven** - waar de oplevering iets raakt dat niet
  onder "wat dit raakt buiten deze week" staat; of `<geen>`.

Optionele velden (laat leeg met `<geen>`):

- **Moet veranderen** - blokkerende bevindingen; `BLOKKEER` vraagt er minstens één.
- **Zou moeten veranderen** - waardevol maar niet blokkerend.
- **Puntjes** - goedkope verbeteringen en smaak.

## Regels voor elke beoordelaar

- Beoordeel alleen het geleverde werk en zijn acceptatiecriteria.
- Herontwerp de week niet. Vind je dat er iets anders had moeten staan, dan is dat
  een bevinding voor de vakdeskundige, geen oordeel over deze oplevering.
- Wees concreet over bewijs: noem het criterium, de plek, en wat je overtuigde of
  juist niet.
- Ontbreekt een verplicht veld in de kern, stop dan en zeg precies wat er mist in
  plaats van een oordeel te geven.

## De weegdrempel

Een beoordeling die alles opsomt wat beter kan, is niet strenger maar onbruikbaar:
wie hem leest weet niet meer waar hij moet beginnen. Weeg daarom, en houd je aan de
verhouding.

- **Moet veranderen** is voor wat de lezer of de student ophoudt, of wat aantoonbaar
  niet klopt. Reken op een handvol, niet op twintig. Kom je hoger uit, dan weeg je
  waarschijnlijk niet maar tel je.
- **Zou moeten veranderen** is voor wat het werk echt beter maakt en wat de
  volgende ronde haalt.
- **Puntjes** zijn goedkoop en verzamel je; ze mogen samen in één opsomming.

De toets is dezelfde als bij de verhelderaar: **loopt de fout luid of stil af?** Wat
de lezer meteen ziet en zelf herstelt, is geen blokkade. Wat er goed uitziet en het
niet is, wel.

Noem tot slot wat expliciet goed is en waarom. Dat is geen beleefdheid: wie herziet
moet weten wat hij niet mag weggooien.

## Voorbeeld

```md
Oordeel: AKKOORD MET PUNTJES

Moet veranderen: <geen>

Zou moeten veranderen:
- Stap 4 kent een gelijkspel in de korte tekst, en de opgave zegt dat wel maar
  de uitwerking legt niet uit dat `>` en `>=` een ander antwoord geven.

Puntjes:
- "Wat een tekst over zichzelf zegt" is een mooie kop maar staat niet in de
  inhoudsopgave; daar staat alleen "Basis".

Dekking van de acceptatiecriteria:
- AC1: gehaald - de opening beschrijft auteurschapsherkenning en verwijst naar
  een echt geval.
- AC2: gehaald - opdracht 10 van de opstap is letterlijk het patroon van stap 3.
- AC3: gehaald - hooks en build gemeld als groen.

Afwijking van wat is opgegeven: <geen>
```

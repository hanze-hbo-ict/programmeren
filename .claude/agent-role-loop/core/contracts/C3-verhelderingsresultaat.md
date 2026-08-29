# C3 - Verhelderingsresultaat

## Doel

Het oordeel van de verhelderaar over een weekontwerp (C2): is het ondubbelzinnig,
gegrond en toetsbaar genoeg om aan een auteur te geven? Het resultaat stuurt het
ontwerp door naar de poort, of terug naar de ontwerper met genummerde, uitvoerbare
wijzigingen.

Het oordeel is streng op wat blokkeert en mild op de rest. Een `FAAL` kost een
hele ontwerpronde, dus hij is gereserveerd voor wat de auteur werkelijk ophoudt;
al het overige reist mee als *Mee te geven aan de auteur*. Zie de ernstdrempel in
`roles/verhelderaar.md`. Een ontwerp waarin niets meer te verbeteren valt bestaat
niet, dus "ik vond nog iets" is op zichzelf geen grond om te falen.

## Schema

Verplichte velden:

- **Oordeel** - `AKKOORD` of `FAAL`.
- **Reden** - één korte alinea.

Voorwaardelijke en optionele velden (laat leeg met `<geen>`):

- **Gevraagde wijzigingen** - genummerd; verplicht bij `FAAL`. Elke wijziging
  noemt de sectie van het ontwerp waarop ze slaat en is gemarkeerd als
  **blokkerend**. Alleen blokkerende bevindingen horen hier.
- **Mee te geven aan de auteur** - de verbeterpunten: genummerd, met sectie, maar
  ze kosten geen ronde. Bij `AKKOORD` staan ze hier alleen; bij `FAAL` gaan ze
  mee terug naar de ontwerper als bijvangst van de reparatie.
- **Vragen aan de ontwerper** - onduidelijkheden die een antwoord nodig hebben,
  geen herontwerp.
- **Risico's om te benoemen** - risico's die het ontwerp hoort te noemen, ook bij
  `AKKOORD`.
- **Voorwaarden voor akkoord** - wat een herzien ontwerp moet laten zien om de
  volgende ronde te halen; verplicht bij `FAAL`.

## Waarop je controleert

In deze volgorde:

1. **Herleidbaarheid** - elk acceptatiecriterium is te herleiden tot een onderdeel
   van de week én tot een manier om het vast te stellen. "Klaar wanneer" is
   objectief en niet gevoelsmatig.
2. **Grondslag** - genoemde bestanden, metingen en conventies zijn aannemelijk of
   expliciet als aanname gemarkeerd. Het ontwerp veronderstelt geen feiten die
   het niet heeft vastgesteld.
3. **Afbakening** - elk onderdeel is op zichzelf te beoordelen; afhankelijkheden
   tussen onderdelen staan er expliciet bij; het ontwerp maakt van één werkitem
   niet stilzwijgend drie.
4. **Verificatie** - elke opgave met code heeft een verificatiemodel met
   motivering als het niet `assertions-draaien` is; verwachte uitvoer is
   herleidbaar tot een berekening en niet tot een schatting.
5. **Besluiten** - alles wat een besluit verandert of nodig heeft, staat als open
   vraag voor de vakdeskundige en is niet zelf ingevuld.

## Voorbeeld

```md
Oordeel: FAAL

Reden: Het ontwerp is gegrond en de opbouw klopt, maar acceptatiecriterium 2
heeft geen manier om vast te stellen dat het gehaald is, en de vraag over de
methodegrens is zelf beantwoord in plaats van voorgelegd.

Gevraagde wijzigingen:
1. (Acceptatiecriteria) Maak criterium 2 toetsbaar: waaraan zie je dat de
   opstap dekt wat de basis nodig heeft?
2. (Open vragen) Verplaats de aanname over objectmethoden naar de open vragen.
   Dit raakt `conventies/codeconventies.md` en is een besluit.

Vragen aan de ontwerper: <geen>

Risico's om te benoemen:
- Twee nieuwe onderdelen in de laatste week van een periode.

Voorwaarden voor akkoord:
- Elk criterium heeft een genoemde manier van vaststellen.
- Geen aannames meer over zaken die in `curriculum/` vastliggen.
```

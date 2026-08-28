# C4 - Poortbesluit

## Doel

Het menselijk oordeel tussen ontwerpen en schrijven. De poort bestaat om te
voorkomen dat zelfverzekerde automatisering langs een afweging heen loopt, en het
is het enige contract in de lus dat **door een mens moet worden ingevuld**. Het
besluit geeft de auteur groen licht, stuurt het ontwerp terug, of stopt het werk,
en het legt de genomen beslissingen vast zodat latere rollen erop kunnen bouwen
zonder ze opnieuw te voeren.

## Schema

Verplichte velden:

- **Besluit** - `AKKOORD` / `HERZIEN` / `STOP`.
- **Reden** - één korte alinea.

Voorwaardelijke en optionele velden (laat leeg met `<geen>`):

- **Vereiste wijzigingen vooraf** - verplicht bij `HERZIEN`; genummerd, gericht
  aan de curriculumontwerper.
- **Genomen beslissingen** - antwoorden op de open vragen, en de keuzes over
  afbakening of risico die bij de poort zijn gemaakt.
- **Uitgestelde vragen** - vragen waarvan is vastgesteld dat uitstel veilig is,
  zodat het uitstel zichtbaar is in plaats van stil.
- **Waar dit is vastgelegd** - de verwijzing naar `curriculum/` of `conventies/`.
  **Een besluit dat daar niet landt, is niet genomen.**

## De checklist

1. Is het doel nog het goede doel?
2. Is de afbakening aanvaardbaar? Zijn de niet-doelen dat?
3. Zijn de acceptatiecriteria toetsbaar?
4. Is het verificatieplan geloofwaardig, en waar het niet `assertions-draaien` is,
   is de motivering eerlijk?
5. Is wat onomkeerbaar is, ook zo bedoeld? Materiaal weggooien is onomkeerbaar in
   de praktijk, ook al staat het in de geschiedenis.
6. Zijn de open vragen beantwoord, of expliciet veilig om uit te stellen?
7. Kan de auteur dit uitvoeren zonder eisen te verzinnen?

## Voorbeeld

```md
Besluit: AKKOORD

Reden: Het ontwerp klopt en de vragen zijn beantwoord. De methodegrens naar week
7 is een besluit dat ik neem; het is niet anders op te lossen zonder P4 te laten
vallen.

Vereiste wijzigingen vooraf: <geen>

Genomen beslissingen:
- Objectmethoden mogen vanaf week 7, samen met mutatie. Eén grens, geen twee.
- De Rij van Conway vervalt; niet verplaatsen.

Uitgestelde vragen:
- Of de week in drie bijeenkomsten past. Dat weet ik pas bij het geven.
- Waar Game of Life thuishoort qua technieken.

Waar dit is vastgelegd:
- `conventies/codeconventies.md`, sectie "Objectmethoden pas vanaf week 7"
- `curriculum/uitgangspunten.md`, besluitenregister
- `curriculum/leerlijn.md`, week 7
```

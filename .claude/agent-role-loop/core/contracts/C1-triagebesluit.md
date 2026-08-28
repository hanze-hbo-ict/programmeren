# C1 - Triagebesluit

## Doel

Het proportionaliteitsoordeel over een werkitem (C0): verdient dit de volledige
lus, een licht pad, een doorlopende plek, of geen lus? Het besluit is met opzet
kort. De waarde zit in het routeren, niet in de analyse; analyse hoort bij de
curriculumontwerper.

## Schema

Verplichte velden:

- **Besluit** - een van:
  - `VOLLEDIG` - de hele lus, vanaf de verkenner.
  - `LICHT` - geen verkenning en geen beoordeling; rechtstreeks naar de auteur met
    een minimaal ontwerp. Voor klein, omkeerbaar werk dat geen besluit raakt.
  - `DOORLOPEND` - een staande zorg die overal speelt en nooit af is. Blijft open
    als verzamelplek; het werk gaat mee met de sectie die toch herzien wordt.
  - `AFWIJZEN` - de lus is het verkeerde gereedschap. Te klein voor enig proces,
    of te groot en eerst op te splitsen.
- **Reden** - hooguit drie zinnen.
- **Omvangoordeel** - `XS` / `S` / `M` / `L` / `XL`, bevestigt of overrulet de
  schatting van de indiener.

Voorwaardelijk veld:

- **Advies** - verplicht bij `AFWIJZEN`: wat de indiener in plaats daarvan moet
  doen (zelf uitvoeren, of langs welke naden opsplitsen). Anders `<geen>`.

## Waar je op let

**Hoe moeilijk is het terug te draaien?** Dit weegt zwaarder dan omvang.
Materiaal weggooien, een opgave naar een ander vak verplaatsen of een
leeruitkomst aanraken verdient de volledige lus, ook als de wijziging klein oogt.

**Raakt het `curriculum/`?** Dan volledig. Alles wat een besluit verandert of er
een nodig heeft, gaat langs de vakdeskundige.

## Voorbeeld

```md
Besluit: VOLLEDIG

Reden: Een hele week herzien, met een leeruitkomst die opnieuw gedekt moet
worden en materiaal dat verdwijnt. Groot genoeg voor een ontwerp, en niet
terug te draaien met één commit.

Omvangoordeel: L (bevestigt de schatting)

Advies: <geen>
```

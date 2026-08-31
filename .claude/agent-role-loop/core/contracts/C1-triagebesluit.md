# C1 - Triagebesluit

## Doel

Het proportionaliteitsoordeel over een werkitem (C0). Twee vragen, en ze staan
los van elkaar: **welke verantwoordelijkheden dit werk nodig heeft**, en **hoe diep
elk van die verantwoordelijkheden moet gaan**. Het besluit is met opzet kort. De
waarde zit in het routeren, niet in de analyse; analyse hoort bij de
curriculumontwerper.

## Schema

Verplichte velden:

- **Besluit** - een van:
  - `LUS` - het werk gaat langs de rollen die je in het veld hieronder noemt.
  - `DOORLOPEND` - een staande zorg die overal speelt en nooit af is. Blijft open
    als verzamelplek; het werk gaat mee met de sectie die toch herzien wordt.
  - `AFWIJZEN` - de lus is het verkeerde gereedschap. Te klein voor enig proces,
    of te groot en eerst op te splitsen.
- **Rollen** - verplicht bij `LUS`: de verantwoordelijkheden die dit werk nodig
  heeft, als opsomming, in lusvolgorde. Bijvoorbeeld
  `verkenner, auteur, beoordelaar-redacteur`. Noem per rol in één regel waarom hij
  meedoet; wie je weglaat hoef je niet te verantwoorden, dat doet de reden al.
  De lijst en de vragen die haar bepalen staan in `roles/triage.md`.
- **Reden** - hooguit drie zinnen.
- **Omvangoordeel** - `XS` / `S` / `M` / `L` / `XL`, bevestigt of overrulet de
  schatting van de indiener.

Voorwaardelijk veld:

- **Advies** - verplicht bij `AFWIJZEN`: wat de indiener in plaats daarvan moet
  doen (zelf uitvoeren, of langs welke naden opsplitsen). Anders `<geen>`.

## Omvang en rollen zijn twee dingen

Dit is het onderscheid dat eerder ontbrak, en waardoor werk werd overgeslagen dat
achteraf toch moest gebeuren.

De **rollen** zeggen *welke* verantwoordelijkheden meedoen. De **omvang** zegt *hoe
diep* elk van die rollen gaat - zie de tabel onder Proportionaliteit in `loop.md`.

Ze lopen niet gelijk op. "Vertaal achttien docstrings naar het Nederlands" is qua
omvang S, maar raakt twee verantwoordelijkheden hard: **meten**, want de omvang van
het werk is zelf een bewering die kan kloppen of niet, en **lezen**, want een
vertaling kan grammaticaal goed en toch inconsistent zijn. Een klein werkitem met
twee rollen is geen tegenspraak.

## Waar je op let

**Hoe moeilijk is het terug te draaien?** Dit weegt zwaarder dan omvang.
Materiaal weggooien, een opgave naar een ander vak verplaatsen of een
leeruitkomst aanraken verdient de volledige lus, ook als de wijziging klein oogt.

**Raakt het `curriculum/`?** Dan volledig. Alles wat een besluit verandert of er
een nodig heeft, gaat langs de vakdeskundige.

## Voorbeeld

```md
Besluit: LUS

Rollen:
- verkenner - de opgave rust op een telling die niemand heeft nagemeten
- curriculumontwerper - er is een keuze tussen repareren en vervangen
- verhelderaar - volgt op het ontwerp
- vakdeskundige - het raakt het besluitenregister
- auteur
- beoordelaar-eerstejaars - de student leest de herschreven opgave
- beoordelaar-redacteur - er verandert veel proza
- hoofdredacteur - twee beoordelaars, dus één oordeel nodig

Reden: Een hele week herzien, met een leeruitkomst die opnieuw gedekt moet
worden en materiaal dat verdwijnt. Niet terug te draaien met één commit.

Omvangoordeel: L (bevestigt de schatting)

Advies: <geen>
```

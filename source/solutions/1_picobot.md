---
title: "Picobot"
---

# Uitwerkingen Picobot

Deze uitwerkingen zijn modeloplossingen voor de vier Picobot-opdrachten uit
week 1. Een state is hier geen positie in de kamer, maar een fase in de
strategie. De regel kiest op basis van de huidige state en de vier zichtbare
richtingen een beweging en eventueel een nieuwe fase. Een `X` betekent: blijf
staan en verander alleen van state.

## Opdracht 1 — De lege kamer

```text
0 *x** -> E 0
0 *E** -> x 1
1 x*** -> N 1
1 N*** -> x 2
2 ***x -> S 2
2 ***S -> W 1
```

De strategie is een zigzag over alle kolommen. State 0 gaat naar het oosten
tot de oostmuur. Daarna wisselt Picobot naar state 1 en gaat naar het noorden
tot de noordmuur. State 2 laat hem vervolgens naar het zuiden gaan. Aan de
zuidmuur gaat hij één vak naar het westen en begint de volgende kolom.

| State | Gedrag | Overgang |
|---|---|---|
| 0 | Naar het oosten zolang dat kan | oostmuur → 1 |
| 1 | Naar het noorden zolang dat kan | noordmuur → 2 |
| 2 | Naar het zuiden zolang dat kan | zuidmuur → west, 1 |

De wildcard maakt de regels onafhankelijk van muren aan de andere drie kanten.

## Opdracht 2 — Het doolhof

```text
0 **x* -> W 1
0 **W* -> x 3
1 ***x -> S 2
1 ***S -> x 0
2 *x** -> E 3
2 *E** -> x 1
3 x*** -> N 0
3 N*** -> x 2
```

Deze oplossing volgt systematisch de gangen. De vier states staan voor de
voorkeursrichting van de volgende rechte beweging: west, zuid, oost en noord.
Zolang die richting open is, blijft Picobot bewegen. Bij een muur verandert hij
van fase en probeert hij de volgende richting. Daardoor loopt hij de verbonden
gangen door zonder dat een aparte state voor elke positie nodig is.

| State | Voorkeursrichting | Bij blokkade |
|---|---|---|
| 0 | west | state 3 |
| 1 | zuid | state 0 |
| 2 | oost | state 1 |
| 3 | noord | state 2 |

De `X`-regels zijn overgangsregels: Picobot blijft op het kruispunt staan,
maar begint daarna met de volgende richtingsfase.

## Opdracht 3 — De ruit

```text
0 *x** -> E 0
0 xE*S -> N 0
0 NE*x -> S 0
0 NE*S -> W 1
1 x*** -> N 1
1 N*** -> S 2
2 ***x -> S 2
2 **WS -> N 3
2 **xS -> W 1
3 **** -> W 1
```

De oplossing gebruikt afwisselende verticale en horizontale bewegingen langs
de schuine randen van de ruit. State 0 handelt de oostelijke rand af: eerst
naar het oosten, en bij de verschillende hoekpatronen omhoog, omlaag of naar
het westen. State 1 is de noordwaartse sweep. State 2 is de zuidwaartse sweep
en kiest onderaan tussen nog verder zuid, omhoog langs de rand of één stap naar
het westen. State 3 voert die weststap uit en brengt Picobot terug naar state 1.

De specifieke patronen (`xE*S`, `NE*x`, `NE*S` en `**WS`) herkennen de hoeken
van de ruit. Zo worden gewone randcellen en hoekcellen verschillend behandeld.

## Opdracht 4 — De grot

```text
0 *E** -> W 1
0 *x** -> E 0
1 **W* -> x 5
1 **x* -> W 1
2 **x* -> W 3
2 **W* -> E 0
3 ***x -> S 4
3 ***S -> x 2
4 *x** -> E 5
4 *E** -> x 3
5 x*** -> N 2
5 N*** -> x 4
```

Hier wordt de grot in banen doorlopen. States 0 en 1 vormen een oost-west-
beweging: state 0 gaat oostwaarts en keert bij de oostmuur om; state 1 gaat
westwaarts en schakelt bij de westmuur naar de volgende fase. States 2 en 3
doen hetzelfde voor een volgende baan, met een overgang via het zuiden.
States 4 en 5 verbinden de banen aan de andere kant via oost en noord.

| State | Hoofdbeweging | Functie van de overgang |
|---|---|---|
| 0 | oost | oostmuur → westwaartse fase 1 |
| 1 | west | westmuur → verbindingsfase 5 |
| 2 | west | westmuur → oostwaartse fase 0 |
| 3 | zuid | zuidmuur → fase 2 |
| 4 | oost | oostmuur → fase 3 |
| 5 | noord | noordmuur → fase 4 |

De zes states coderen dus de richting én aan welke kant van de grot de
volgende baan moet worden aangesloten. De regels met `X` verplaatsen niet,
maar markeren alleen zo'n overgang.

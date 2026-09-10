---
title: "Picobot"
---

# Uitwerkingen Picobot

Deze uitwerkingen zijn modeloplossingen voor de vier Picobot-opdrachten uit
week 1. Een staat is hier geen positie in de kamer, maar een fase in de
strategie. De regel kiest op basis van de huidige staat en de vier zichtbare
richtingen een beweging en eventueel een nieuwe staat. Een `X` betekent: blijf
staan en verander alleen van staat. Bekijk ook het [practicum Picobot](/practicals/1_picobot.md)
en de [weekindex](/course/solutions_1.md).

## Opdracht 1 — De lege kamer

Deze uitwerking hoort bij [Opdracht 1 in het practicum](/practicals/1_picobot.md#opdracht-1-de-lege-kamer).

```text
0 *x** -> E 0
0 *E** -> x 1
1 x*** -> N 1
1 N*** -> x 2
2 ***x -> S 2
2 ***S -> W 1
```

De strategie is een zigzag over alle kolommen. Staat 0 gaat naar het oosten
tot de oostmuur. Daarna wisselt Picobot naar staat 1 en gaat naar het noorden
tot de noordmuur. Staat 2 laat hem vervolgens naar het zuiden gaan. Aan de
zuidmuur gaat hij één vak naar het westen en begint de volgende kolom.

| Staat | Gedrag | Overgang |
|---|---|---|
| 0 | Naar het oosten zolang dat kan | oostmuur → 1 |
| 1 | Naar het noorden zolang dat kan | noordmuur → 2 |
| 2 | Naar het zuiden zolang dat kan | zuidmuur → west, 1 |

De wildcard maakt de regels onafhankelijk van muren aan de andere drie kanten.
Controleer de uitwerking vanaf drie startposities: bij een muur, in een hoek en
midden in de kamer. De hele kamer kleurt grijs en Picobot stopt vanzelf.

## Opdracht 2 — Het doolhof

Deze uitwerking hoort bij [Opdracht 2 in het practicum](/practicals/1_picobot.md#opdracht-2-het-doolhof).
Lees voor de strategie ook het [doolhofcollege](/lectures/1b_picobot.md#de-right-hand-rule).

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

Deze oplossing volgt de right-hand rule: houd steeds dezelfde wand aan je
rechterhand. In een gang gaat Picobot rechtdoor. Op een splitsing kiest hij de
volgende richting waarmee hij de rechterwand blijft volgen. Bij een doodlopend
punt blijft hij met `X` staan en gaat hij verder met de volgende richting. De
vier staten bewaren de richting waarin hij daarna kijkt: west, zuid, oost en
noord. Zo doorloopt hij alle verbonden gangen zonder voor elke positie een
aparte staat nodig te hebben.

| Staat | Voorkeursrichting | Bij blokkade |
|---|---|---|
| 0 | west | staat 3 |
| 1 | zuid | staat 0 |
| 2 | oost | staat 1 |
| 3 | noord | staat 2 |

De `X`-regels zijn overgangsregels: Picobot blijft op het doodlopende punt
staan, maar begint daarna met de volgende richtingsfase. Controleer de
uitwerking vanaf drie startposities. Het hele doolhof kleurt grijs en Picobot
stopt vanzelf.

## Opdracht 3 — De ruit

Deze uitwerking hoort bij [Opdracht 3 in het practicum](/practicals/1_picobot.md#opdracht-3-de-ruit).

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
de schuine randen van de ruit. Staat 0 handelt de oostelijke rand af: eerst
naar het oosten, en bij de verschillende hoekpatronen omhoog, omlaag of naar
het westen. Staat 1 is de noordwaartse sweep. Staat 2 is de zuidwaartse sweep
en kiest onderaan tussen nog verder zuid, omhoog langs de rand of één stap naar
het westen. Staat 3 voert die weststap uit en brengt Picobot terug naar staat 1.

De specifieke patronen (`xE*S`, `NE*x`, `NE*S` en `**WS`) herkennen de hoeken
van de ruit. Zo worden gewone randcellen en hoekcellen verschillend behandeld.
Controleer de uitwerking vanaf drie startposities. De hele ruit kleurt grijs en
Picobot stopt vanzelf.

## Opdracht 4 — De grot

Deze uitwerking hoort bij [Opdracht 4 in het practicum](/practicals/1_picobot.md#opdracht-4-de-grot).

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

Hier wordt de grot in banen doorlopen. Staten 0 en 1 vormen een oost-west-
beweging: staat 0 gaat oostwaarts en keert bij de oostmuur om; staat 1 gaat
westwaarts en schakelt bij de westmuur naar de volgende fase. Staten 2 en 3
doen hetzelfde voor een volgende baan, met een overgang via het zuiden.
Staten 4 en 5 verbinden de banen aan de andere kant via oost en noord.

| Staat | Hoofdbeweging | Functie van de overgang |
|---|---|---|
| 0 | oost | oostmuur → westwaartse fase 1 |
| 1 | west | westmuur → verbindingsfase 5 |
| 2 | west | westmuur → oostwaartse fase 0 |
| 3 | zuid | zuidmuur → fase 2 |
| 4 | oost | oostmuur → fase 3 |
| 5 | noord | noordmuur → fase 4 |

De zes staten coderen dus de richting én aan welke kant van de grot de
volgende baan moet worden aangesloten. De regels met `X` verplaatsen niet,
maar markeren alleen zo'n overgang.
Controleer de uitwerking vanaf drie startposities. De hele grot kleurt grijs en
Picobot stopt vanzelf.

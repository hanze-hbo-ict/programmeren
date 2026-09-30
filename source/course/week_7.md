# Mutabiliteit en algoritmeontwerp

![Schotel](/images/saucer.png)

In week 5 maakte je al 2D-lijsten en liep je door een raster. Deze week leer je
een lijst op een vaste plek veranderen, eerst bewust en daarna met aandacht voor
verwijzingen en kopiëren. Je oefent ook hoe je een groter probleem in deelproblemen
verdeelt en functies samenstelt.

De kern is verplicht: de **opstap**, het **werkcollege** en de **basis**. In het
werkcollege bouw je met de klas het algoritme voor vallende korrels op, van
deelproblemen naar code. De extra is een zelfstandige uitdaging met Game of Life.
Als je weinig tijd hebt, stop je na één werkende basisgeneratie; de extra mag de
kern nooit verdringen.

## Route

1. Lees het college over mutabiliteit, functiecompositie, deelproblemen en tuples.
2. Maak de opstap: één rastercel wijzigen, herkennen dat twee namen naar dezelfde
   lijst verwijzen en een klein
   tuplepaar uitpakken.
3. Doe het [werkcollege](/practicals/7b_vallende_korrels) mee: knip het probleem
   van vallende korrels in deelproblemen en bouw het algoritme gezamenlijk op.
4. Maak de basis: ontwerp de buurttelling, de regel voor één cel en de
   samengestelde functie voor één volledige generatie.
5. Kies daarna de extra: Game of Life met dezelfde rasterafspraken.

## Tijdpad en uitvalpad

| Bijeenkomst | Richttijd | Product |
|---|---:|---|
| 1 | 90 minuten | College, directe mutatie, verwijzingen, kopiëren en tuple/unpacking in de opstap |
| 2 | 90 minuten | Werkcollege: vallende korrels opgeknipt in deelproblemen, met één werkende tijdstap |
| 3 | 90 minuten | Basis: `count_neighbors`, `next_cell` en één geteste generatie; daarna facultatief de Game-of-Life-extra |

Loop je uit, rond dan eerst de opstap en één volledige basisgeneratie af. Laat
visualisatie, meerdere generaties en de extra vallen; die zijn geen onderdeel van
de minimale kern. Loopt bijeenkomst 2 uit, dan valt stap 3 van het werkcollege:
één werkende tijdstap is het product van die bijeenkomst, en `settle` kun je
daarna zelf afmaken.

In [week 5](/course/week_5) oefende je het doorlopen van rasters. In
[PGM2 week 1](/course/week_8) komen dictionaries, methoden en Markov aan bod.
Die onderwerpen horen niet bij deze week.

```{tableofcontents}
```

# Onderwerpen

![Schotel](/images/saucer.png)

## Comprehensions

Deze week leer je een lus die een nieuwe lijst opbouwt korter op te schrijven,
als **list comprehension**: `[len(word) for word in words]` is in één regel wat
een lus met `append` in vier regels doet. Met accolades bouw je op dezelfde
manier een set of een dictionary op, als **set comprehension** of **dict
comprehension**. Daarbij leer je drie hulpmiddelen: `enumerate` geeft je bij
elk element ook zijn positie, `zip` loopt twee lijsten naast elkaar langs, en
de conditionele expressie `a if c else b` kiest per element een waarde.

Het eerste college behandelt de list comprehension, met `range`, `enumerate`,
`zip` en de conditionele expressie. Dat heb je nodig voor het eerste deel van de
opstap. Het tweede college behandelt dict en set comprehensions, een lijst van
lijsten, ook met een geneste comprehension, en wanneer je beter een lus houdt.
Dat heb je nodig voor het tweede deel van de opstap, voor de basis en voor de
extra. In het werkcollege maak je met deze vormen een register bij een tekst.

Aan het eind van de week kun je een lus die een lijst, set of dictionary
opbouwt herschrijven als comprehension, en een comprehension terugschrijven als
lus. En je kunt uitleggen wanneer een lus de betere keuze blijft.

### Waar je vandaan komt

In [week 4 van Programmeren 1](/course/week_4) leerde je het
[lusrecept](/lectures/4a_lussen.ipynb#het-lusrecept): wat verzamel je, wat loop
je langs, wat gebeurt er per stap? Een comprehension is dat recept in één
uitdrukking, voor het geval dat je een nieuwe verzameling opbouwt. In
[week 1 van Programmeren 2](/course/week_8) leerde je dictionaries, sets en
`.items()`, en telde je de woorden van een tekst. Deze week bouw je daarop voort,
met dezelfde teksten.

```{tableofcontents}
```

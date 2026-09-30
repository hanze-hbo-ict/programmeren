# Onderwerpen

![Schotel](/images/saucer.png)

## Recursie

Deze week leer je **recursie**: een functie die zichzelf aanroept, voor een
kleiner deel van hetzelfde probleem. Dat is de natuurlijke aanpak voor een
probleem waarvan je de diepte niet van tevoren weet, zoals een directory met
subdirectories die zelf weer subdirectories hebben. Elke recursieve functie heeft
een **basisgeval**, waarin ze zichzelf niet aanroept, en een **recursief geval**,
met de **recursieve aanroep**.

Het eerste college laat zien hoe een recursieve functie werkt: hoe ze zichzelf
aanroept, waarom ze een basisgeval nodig heeft, en hoe elke aanroep zijn eigen
frame op de stack krijgt. Dat heb je nodig voor het eerste deel van de opstap,
waarin je recursieve functies leest en naspeelt. Het tweede college laat zien hoe
je zelf een recursieve functie ontwerpt, met drie vragen: wat is het basisgeval,
wat is het kleinere probleem, en hoe combineer je? Dat heb je nodig voor het
tweede deel van de opstap, voor de basis en voor de extra. In het werkcollege
doorzoek je een directory met subdirectories.

Aan het eind van de week kun je een recursieve functie lezen en aanroep voor
aanroep naspelen, en kun je zelf een recursieve functie ontwerpen die een getal,
een string, een lijst of een boolean teruggeeft.

### Waar je vandaan komt

In [week 3 van Programmeren 1](/course/week_3) zag je dat Python bij elke
aanroep van een functie een frame op de stack zet, met de variabelen van die
aanroep. Bij recursie staan er zo meer frames van dezelfde functie tegelijk op de
stack. In [week 1 van Programmeren 2](/course/week_8) leerde je dictionaries,
en in [week 2](/course/week_9) `sum([...])` met een list comprehension. Het
werkcollege gebruikt die twee om een directory te doorzoeken die als dictionary
is opgeschreven.

```{tableofcontents}
```

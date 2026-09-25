# Onderwerpen

![Schotel](/images/saucer.png)

## Operator overloading en exceptions

Deze week laat je je eigen klassen meedoen met de operatoren van Python. Python
vertaalt `a == b` naar de aanroep `a.__eq__(b)`, en `a < b` naar `a.__lt__(b)`.
Zo'n methode, die Python zelf aanroept, heet een **magische methode**. Schrijf je
er een in je klasse, dan bepaal jij wat de operator bij jouw objecten doet. Dat
heet **operator overloading**.

Daarna leer je een fout melden. Met `raise` **gooi** je een **exception**: de
methode stopt meteen, en de fout valt op waar hij ontstaat, in plaats van dat het
programma stilletjes doorgaat met iets wat niet klopt. Met `try` en `except`
**vang** je zo'n exception **af**, en **handel** je de fout **af**: het programma
doet iets zinnigs in plaats van te stoppen.

Aan het eind van de week kun je een klasse schrijven die werkt met `==`, `<` en
`sorted`, en code schrijven die een fout meldt met `raise` en haar afhandelt met
`try` en `except`.

Deze week staat ook het [oefententamen](/course/pgm2_tentamen) van Programmeren 2.

### Waar je vandaan komt

In [week 6 van Programmeren 2](/course/week_13) bouwde je subklassen op klassen die
er al waren, en code die met al die klassen werkt zonder te vragen welke het is.
Op een paar plekken viel die code nog stilletjes terug: bij foute invoer in een
constructor, en bij een subklasse die een methode vergeet. Deze week komen daar
exceptions voor in de plaats. En `Date` uit week 5 vergeleek je met `equals`;
deze week wordt dat `==`.

```{tableofcontents}
```

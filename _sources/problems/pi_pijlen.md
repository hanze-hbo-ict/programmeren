# Pi met pijltjes

```{include} ../class/problems/pi_pijlen.md
```

![Dartboard](images/pi_pijlen/500px-Dartboard.png)

Het is misschien verbazingwekkend dat het mogelijk is om de wiskundige constante π te berekenen zonder dat je andere operaties nodig hebt dan tellen, optellen en vermenigvuldigen. In deze opgave ga je twee functies schrijven om pi (`3.14159...`) te benaderen door *het gooien van pijltjes*.

Zie ook [Calculating Pi with Darts](https://www.youtube.com/watch?v=M34TO71SKGk) hoe je dit zou kunnen simuleren met échte pijltjes!

## Pi met pijltjes berekenen: achtergrond

Stel je een cirkel voor die ingeschreven is in een vierkant die het gebied met `-1 ≤ x ≤ 1` en `-1 ≤ y ≤ -1` beslaat. De oppervlakte van de ingeschreven cirkel, waarvan de straal `1.0` is, moet dan π zijn: de oppervlaktre van een cirkel is immers gelijk aan π*r*<sup>2</sup>, en de straal *r* is hier `1.0`.

:::{admonition,notice} Ingeschreven cirkel
Een *ingeschreven* cirkel raakt de randen van het omliggende vierkant precies; als het vierkant dus zijden van lengte 2 heeft, is de diameter van de cirkel ook 2.
:::

Als je pijltjes gooit op willekeurige punten in het vierkant zullen maar een deel daarvan de ingeschreven cirkel raken. De verhouding

```
oppervlakte van de cirkel / oppervlakte van het vierkant
```

kan benaderd worden door de verhouding

```
aantal pijltjes dat de cirkel raakt / totaal aantal geworpen pijltjes
```

Als je meer en meer pijltjes gooit benadert de tweede verhouding hierboven steeds dichter de eerste verhouding. Aangezien drie van de vier waardes hierboven bekend zijn kunnen we ze gebruiken om de oppervlakte van de cirkel te benaderen. Dit kan weer gebruikt worden om π te benaderen.

### Pijltjes gooien ontwerpen...

Om een pijltje te gooien, moet je willekeurige x- en y-coördinaten genereren tussen `-1.0` en `1.0`. Zorg dat je de regel

```python
import random
```

bovenaan je bestand toevoegt. Als je dit doet, heb je nu de beschikking tot de functie

```python
random.uniform(-1.0, 1.0)
```

Deze regel geeft een floating-pointwaarde in het bereik van `-1.0` tot en met `1.0`. Je kan bijvoorbeeld schrijven:

```python
x = random.uniform(-1.0, 1.0)
```

## De functie `throw_dart`

Met dit in het achterhoofd is het handig om een hulpfunctie `throw_dart()` te schrijven die

* Eén "pijlte" gooit in het vierkant door een willekeurige `x`- en een willekeurige `y`-coördinaat te genereren tussen -1 en 1
* Bepaalt of dat pijltje in de cirkel met straal 1 rond de oorsprong valt; je kan hier de functie `math.sqrt` gebruiken om dit te controleren, maar dat is niet strikt noodzakelijk!
* `True` teruggeeft als het pijltje de cirkel raakt en `False` teruggeeft als het pijlte de cirkel mist
* Onthoud dat het pijltje altijd het vierkant raakt, door de manier waarop de worp ontworpen is...

:::{admonition,tip} Valt het pijltje binnen de cirkel?"
Het pijltje valt binnen de cirkel als de afstand tot het middenpunt, in dit geval (0, 0), kleiner is dan of gelijk is aan de straal. Je kan de afstand berekenen met de stelling van Pythagoras: de afstand van een punt (*x*, *y*) tot het punt (0, 0) is gelijk aan de wortel van *x*<sup>2</sup> + *y*<sup>2</sup>
:::

Deze hulpfunctie kan je gebruiken voor de beide hoofdfuncties van deze opgave: `for_pi` en `while_pi`.

Hoe je je Monte-Carlosimulatie ook ontwerpt moet je onthouden dat je als altijd een docstring opneemt in beide functies die uitlegt hoe de functie werkt!

## De functie `for_pi`

De functie `for_pi(n)` moet een positieve integer `n` als parameter meekrijgen.

Ze moet `n` pijltjes in het vierkant "gooien".

Na elk pijltje dat gegooid is moet de functie het volgende afdrukken:

* Het aantal pijltjes dat tot nu toe gegooid is.
* Het aantal pijtljes dat tot nu toe de cirkel ***geraakt*** heeft.
* De hieruit volgende schatting voor π.

**Returnwaarde**; *vergeet deze niet!*

De functie `for_pi` moet de *uiteindelijke schatting voor π* na `n` worpen teruggeven.

Hier is een voorbeelduitvoer om te laten zien hoe `for_pi` moet werken:

* Je eigen uitvoer zal variëren vanwege de willekeurigheid...
* Het moet echter de echte waarde van π benaderen als het aantal gegooide pijltjes `n` groter wordt

```ipython
In [1]: for_pi(10)
1 raak van 1 worpen dus pi is 4.0
2 raak van 2 worpen dus pi is 4.0
3 raak van 3 worpen dus pi is 4.0
4 raak van 4 worpen dus pi is 4.0
4 raak van 5 worpen dus pi is 3.2
5 raak van 6 worpen dus pi is 3.33333333333
6 raak van 7 worpen dus pi is 3.42857142857
6 raak van 8 worpen dus pi is 3.0
7 raak van 9 worpen dus pi is 3.11111111111
8 raak van 10 worpen dus pi is 3.2

Out[1]: 3.2
```

## De functie `while_pi(error)`

De functie `while_pi(error)` moet een positieve floating-pointwaarde `error` als parameter meekrijgen.

Ze moet dan pijltjes naar het vierkant gooien totdat het *absolute verschil* tussen de schatting die de functie voor π maakt en de echte waarde van π minder is dan `error`.

Je functie `while_pi` heeft de echte, bekende waarde van π nodig om te bepalen of de schatting binnen de foutmarge ligt! Dit zou niet kunnen als de constante die we benaderen echt onbekend is, maar in dit geval kan je de regel

```python
import math
```

toevoegen aan je code en de waarde `math.pi` gebruiken als de echte waarde voor π.

Net als de functie `for_pi` moet je functie `while_pi` na elke worp het volgende afdrukken:

* Het aantal pijltjes dat tot nu toe gegooid is.
* Het aantal pijtljes dat tot nu toe de cirkel ***geraakt*** heeft.
* De hieruit volgende schatting voor π.

**Returnwaarde**; *vergeet deze niet!*

De functie `while_pi` moet *het aantal gegooide pijltjes* teruggeven dat nodig was om de gevraagde
nauwkeurigheid te bereiken.

Hier is een voorbeelduitvoer om te laten zien hoe `while_pi` werkt:

```ipython
In [7]: while_pi(0.1)
1 raak van 1 worpen dus pi is 4.0
2 raak van 2 worpen dus pi is 4.0
3 raak van 3 worpen dus pi is 4.0
4 raak van 4 worpen dus pi is 4.0
5 raak van 5 worpen dus pi is 4.0
5 raak van 6 worpen dus pi is 3.33333333333
6 raak van 7 worpen dus pi is 3.42857142857
7 raak van 8 worpen dus pi is 3.5
7 raak van 9 worpen dus pi is 3.11111111111

Out[7]: 9
```

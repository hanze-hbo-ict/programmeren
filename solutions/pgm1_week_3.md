# PGM1 Week 3

## Basis

### [Functies](/problems/basis/3_functies)

Dit is het begin van het Python bestand waar we eventueel te gebruiken modules importeren, bijvoorbeeld de functie `choice` uit de module `random`. Het kan zijn dat je geen modules gebruikt? Dan kun je dit weg laten.

```python
import time
from random import choice, randint
```

#### Opdracht 1b

Schrijf de functie `tpl(x)` die een getal als argument accepteert en drie keer de waarde van dat argument teruggeeft.

```python
def tpl(x):
    """Geeft driemaal het argument terug

    :param x: De waarde om te verdrievoudigen
    :type x: int, float of string
    :rtype: int, float of string
    """
    return 3 * x
```

We hebben besloten de *docstring* van meer informatie te voorzien voor nog meer duidelijkheid.

Aangezien het een simpele taak is die de functie moet doen, kan de berekening gelijk in de return gezet worden.

#### Opdracht 2a

Schrijf de functie `min_two(a, b)` die twee getallen als argument accepteert en de kleinste waarde teruggeeft.

```python
def min_two(a, b):
    """ Geeft de laagste van de twee parameters terug

    :param a, b: de twee waarden waarvan de laagste terug moet worden gegeven
    :type a, b: int
    :rtype: int
    """
    if a < b:
        return a
    elif b < a:
        return b
    else:
        return "Beide getallen zijn even groot!"
```

In de opdracht werd niet gezegd dat we er van uit mogen gaan dat de twee getallen niet hetzelfde kunnen zijn.

Daarom controleert de functie zowel of a kleiner is en of b kleiner is.
Als geen van beide kleiner zijn dan zullen de argumenten even groot zijn.

#### Opdracht 2b

Schrijf de functie `min_three(a, b, c)` die drie getallen als argument accepteert en de kleinste waarde teruggeeft.

```python
def min_three(a, b, c):
    """ Geeft de laagste van de drie parameters terug

    :param a, b, c: de twee waarden waarvan de laagste terug moet worden gegeven
    :type a, b, c: int
    :rtype: int
    """
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c
    else:
        return "Er zijn getallen die even groot zijn!"
```

In de opdracht werd niet gezegd dat we er van uit mogen gaan dat de twee getallen niet hetzelfde kunnen zijn.

Daarom controleert de functie zowel of elke variable kleiner is dan de andere twee met de 'and' in de if statements.

Als geen van de drie argumenten kleiner zijn dan de andere dan zullen er twee hetzelfde zijn of alle zelfs alle drie.

#### Opdracht 3

Schrijf de functie absolute(x,y) dat twee getallen accepteert en de afstand berekent tussen de twee getallen.

```python
def absolute(x, y):
    """ Geeft de afstand tussen de twee parameters terug

    :param x, y: de twee waarden waarvan de afstand terug moet worden gegeven
    :type a, b, c: int
    :rtype: int
    """
    if x >= 0 and y >= 0:
        if x > y:
            # Bij twee positieve getallen dan krijg je de afstand
            # door het kleinste getal van de grote te trekken.
            return x - y
        else: # y is groter
            return y - x
    elif x < 0 and y >= 0:
        # y is groter dan de negatieve x.
        # Omdat x negatief is, is de afstand y plus de positieve versie van x.
        return y + (x * -1)
    elif x >= 0 and y < 0:
        # Nu is y negatief
        return x + (y * -1)
    else:
        # Beide getallen zijn negatief.
        # Vindt het kleinste getal.
        if x < y:
            # De afstand is altijd positief.
            # We corrigeren door het kleinste getal positief te maken
            # en het kleinste getal negatief te houden.
            return (x * -1) + y # Plus een negatief getal wordt een aftrek som
        else:
            return (y * -1) + x
```

Als beide getallen positief zijn dan hoeft alleen de laagste van de hoogste af getrokken te worden.

Als een van beide getallen negatief is dan is het andere getal automatisch het grotere getal. Om dan de juiste waarde te krijgen moet de positieve versie van het negatieve getal opgeteld worden bij het al positieve getal.

Als beide getallen negatief zijn dan kunnen we de positieve versie van het kleinste getal nemen en het andere getal daarvan aftrekken.

We maken hiervoor gebruik van het feit dat in Python wanneer je een negatief getal ergens bij optelt het een aftrek operatie wordt.

#### Opdracht 4

Schrijf de functie `trap(x)` die een getal accepteert en een omgekeerde `#` trap tekent. Maak gebruik van recursie.

```python
def trap(x):
    """ Print een onderste boven trap naar het scherm

    :param x: het aantal traptreden
    :type x: int
    :rtype: geen return waarde
    """
    if x > 0:
        print(x * "#")
        trap(x - 1)
    else:
        return
```

Aangezien de bovenste tree de breedste is, kan het programma beginnen bij `x` en vanaf daar aftellen naar 0.

Is `x` groter dan nul ( `x > 0` ) dan zijn er nog treden om te plaatsen. Plaats de trede, corrigeer x voor de geplaatste trede en roep de functie nog een keer aan.

Is `x` gelijk aan nul ( `x == 0` ) dan zijn er geen treden meer om te plaatsen en kan de functie stoppen.


#### Opdracht 5a

Schrijf de functie `lines(x, space)` die twee `#`-lijnen tekent van `x` regels hoog en `space` geeft aan hoeveel spaties tussen de lijnen liggen.

```python
def lines(x, space):
    """ Tekent twee lijnen met # voor <x> aantal regels met <space>
    aantal spaties tussen de twee lijnen

    :param x: geeft aan hoeveel regels
    :param space: geeft aantal spaties tussen de twee lijnen
    :type x, space: int
    :rtype: geen return waarde
    """
    if x > 0:
        print("#" + space*" " + "#")
        lines(x - 1, space)
    else:
        return
```

Hier geldt hetzelfde als voor de onderste boven trap.

Zodra `x` gelijk is aan nul mag het programma stoppen, alle regels zijn naar het scherm geprint.

Als `x` nog geen nul is dan moet er nog een regel naar het scherm geprint worden.

```{note}
We veranderen hier alleen `x` en niet `space`, want de afstand tussen de lijnen is niet afhankelijk van hoeveel regels er al geprint zijn.
```

#### Opdracht 5b

Schrijf een functie `print_square(x)` die een getal accepteert en een `#` vierkant van grootte `x` print. Maak gebruik van de functie `lines`.

```python
def print_square(x):
    """ Tekent een vierkant van # met grootte x

    :param x: geeft aan hoe groot het vierkant moet zijn
    :type x: int
    :rtype: geen return waarde
    """
    print(x * "#")
    lines(x - 2, x - 2)
    print(x * "#")
    return
```

Het verschil tussen `lines()` en `print_square()` is dat `print_square()` begint en eindigt met een volle regel met `x * "#"`.

Deze kunnen direct naar het scherm geprint worden. Dit betekent dat `lines()` alleen de regels tussen de eerste en de twee hoeft te vullen.

We gebruiken `x - 2` voor de `x` van lines omdat er al twee regels geprint worden door `print_square()` zelf.

We gebruiken `x - 2` voor space omdat er voor en na de space een `#` geprint wordt. Als we hier geen rekening mee houden dan worden de `lines()` regels te breed.

#### Run en check de functies

In de `main()` kunnen de functies nu aangeroepen worden voor gebruik.

Met de *assert statements* in `testing()` testen we of alle functies doen wat ze moeten doen.

Zijn er assert die we vergeten zijn?

```python
def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """

    rand_var1 = random.randint(3, 9)
    rand_var2 = random.randint(3, 9)
    rand_var3 = random.randint(-9,-3)
    rand_var4 = random.randint(-9,-3)

    print("Random variable 1 = ", rand_var1)
    print("Random variable 2 = ", rand_var2)
    print("Random variable 3 = ", rand_var3)
    print("Random variable 4 = ", rand_var4)

    print("De tpl functie met random variable 1:", tpl(rand_var1))
    print("De min_two functie met random variable 1 en 2:", min_two(rand_var1, rand_var2))
    print("De min_three functie met random variable 1, 3 en 2:", min_three(rand_var1, rand_var3, rand_var2))
    print("De absolute functie met random variable 3 en 1:", absolute(rand_var3, rand_var1))
    print("De absolute functie met random variable 3 en 4:", absolute(rand_var3, rand_var4))
    print("De trap functie met random variable 2:")
    trap(rand_var2)
    print("De lines functie met random variable 1 en 2:")
    lines(rand_var1, rand_var2)
    print("De lines functie met random variable 2 en 1:")
    lines(rand_var2, rand_var1)
    print("De print_square functie met random variable 1:")
    print_square(rand_var1)
    print("De print_square functie met random variable 2:")
    print_square(rand_var2)


def testing():
    """
    Test functie. Hier staan alle assertions om de functies te testen.
    """
    assert tpl(4) == 12, "tpl() geeft geen waarde terug die drie keer het argument is"
    assert tpl("hoi") == "hoihoihoi", "tpl() geeft geen waarde terug die drie keer het argument is"

    assert min_two(7, 9) == 7, "min_two() geeft niet het kleinste getal terug bij twee positieve getallen"
    assert min_two(7, 3) == 3, "min_two() geeft niet het kleinste getal terug bij twee positieve getallen"
    assert min_two(7, -9) == -9, "min_two() geeft niet het kleinste getal terug bij een positief en een negatief getal"
    assert min_two(-7, 3) == -7, "min_two() geeft niet het kleinste getal terug bij een positief en een negatief getal"
    assert min_two(-7, -9) == -9, "min_two() geeft niet het kleinste getal terug bij twee positieve getallen"
    assert min_two(-7, -3) == -7, "min_two() geeft niet het kleinste getal terug bij twee negatieve getallen"
    assert min_two(4,4) == "Beide getallen zijn even groot!", "Beide getallen zijn even groot maar dit wordt niet gevonden"
    assert min_two(-4,-4) == "Beide getallen zijn even groot!", "Beide getallen zijn even groot maar dit wordt niet gevonden"

    assert min_three(7, 9, 3) == 3, "min_three() geeft niet het kleinste getal terug bij drie positieve getallen"
    assert min_three(7, 3, 9) == 3, "min_three() geeft niet het kleinste getal terug bij drie positieve getallen"
    assert min_three(7, -9, 3) == -9, "min_three() geeft niet het kleinste getal terug bij een negatief getal"
    assert min_three(-7, 3, 9) == -7, "min_three() geeft niet het kleinste getal terug bij een negatief getal"
    assert min_three(-7, -9, -3) == -9, "min_three() geeft niet het kleinste getal terug bij drie positieve getallen"
    assert min_three(-9, -7, -3) == -9, "min_three() geeft niet het kleinste getal terug bij drie negatieve getallen"
    assert min_three(4,4,4) == "Er zijn getallen die even groot zijn!", "Er zijn getallen die even groot zijn maar die worden niet gevonden"
    assert min_three(-4,-4,-4) == "Er zijn getallen die even groot zijn!", "Er zijn getallen die even groot zijn maar die worden niet gevonden"

    assert absolute(3, 12) == 9, "absolute() met twee postieve getallen berekent de afstand niet goed"
    assert absolute(12, 3) == 9, "absolute() met twee positieve getallen berekent de afstand niet goed"
    assert absolute(-3, -12) == 9, "absolute() met twee negatieve getallen berekent de afstand niet goed"
    assert absolute(-12, -3) == 9, "absolute() met twee negatieve getallen berekent de afstand niet goed"
    assert absolute(3, -12) == 15, "absolute() met een negatief getal en een positief getal berekent de afstand niet goed"
    assert absolute(-3, 12) == 15, "absolute() met een negatief getal en een positief getal berekent de afstand niet goed"

main()
testing()
```

### [Turtle](/problems/basis/3_turtle)

Deze opgave gaat over het tekenen met een turtle.


#### Opdracht 1a

Maak de functie `sq()` af zodat het een vierkant tekent met zijdes met 25 pixels. Maak gebruik van recursie om de herhaling van code te voorkomen.

```python
import time
from turtle import *
from random import *

def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """
    speed(10) # set the drawing speed to 10
    sq(4)
    done() # tell turtle the drawing is done.

def testing():
    """
    Test functie. Hier staan alle assertions om de functies te testen.
    """

def sq(n):
    """Draws 25-pixel sides of a square.
    """
    if n == 0:
        return
    else:
        forward(25)
        right(90)
        sq(n - 1)

main()
testing()
```


#### Opdracht 1b

Schrijf de functie `sqLine(x)`. De parameter `x` geeft een hoeveel vierkantjes op een rij moeten komen. Maak gebruik van de `sq` functie.

```python
def sqLine(x):
    """ Tekent x vierkanten op een rij.
    """
    if x == 0:
        return
    else:
        sq()
        forward(25)
        sqLine(x - 1)
```

Als de forward niet wordt uitgevoerd dan maakt de turtle elk vierkantje op dezelfde locatie. Omdat de turtle naar rechts kijkt na het maken van het eerste vierkantje wordt het volgende vierkantje rechts van de eerste gemaakt. De derde komt rechts van de tweede enzovoorts.


#### Opdracht 1c

Schrijf de functie `sqSpiral(n)`. De paramater `n` geeft aan met hoeveel vierkantjes de eerste zijde van de spiraal moet hebben.

```python
def sqSpiral(n):
    """ Tekent een spiraal van vierkanten.
    n geeft aan hoeveel vierkanten de eerste zijde moet hebben.
    """
    if n == 0:
        return
    else:
        sqLine(n)
        right(90)
        sqSpiral(n - 1)
```

Het eerste vierkantje van de tweede lijn in de spiraal valt op het laatste vierkantje van de eerste lijn. Anders wordt de tweede lijn te lang. Daarom hoeft alleen de kijkrichting van de turtle aangepast te worden.


#### Opdracht 2a

Schrijf de functie `sqLength(lengte, x=4)`. Deze functie tekent een vierkant van aangegeven grootte. `sqLength(50)` tekent een vierkant met zijdes van 50 pixels lang.

```python
def sqLength(lengte, x = 4):
    """ Tekent een vierkant met grootte 'lengte'
    """
    if x == 0:
        return
    else:
        forward(lengte)
        right(90)
        sqLength(lengte, x - 1)
```


#### Opdracht 2b

Schrijf de functie `sqRec(start, step)`. De parameter start geeft de grootte van het eerste vierkant aan en de step geeft aan hoeveel kleiner het volgende vierkant is. Maak gebruik van de `sqLength` functie.

```python
def sqRec(start, step):
    """ Tekent vierkanten step kleiner dan het start vierkant in het start vierkant.
    """
    if start <= 0:
        return
    else:
        sqLength(start)
        sqRec(start - step, step)
```


#### Opdracht 2c

Schrijf een functie `sqMiddle(start, step)` De parameter start geeft de grootte van het eerste vierkant aan en de step geeft aan hoeveel kleiner het volgende vierkant is. Maak gebruik van de `sqLength` functie. Dit keer worden de vierkantjes in het midden getekend. Met de `up()` functie stopt de turtle met tekenen. Met de functie `down()` start de turtle weer met tekenen.

```python
def sqMiddle(start, step):
    """ Tekent vierkanten step kleiner dan het start vierkant in het midden van het start vierkant.
    """

    if start <= 0:
        return
    else:
        sqLength(start)
        up()
        forward(step / 2)
        right(90)
        forward(step / 2)
        left(90)
        down()
        sqMiddle(start - step, step)
```

Omdat het volgende vierkant precies in het midden van het vorige vierkant moet zitten, moet er rekening gehouden worden dat de afstand tussen de twee bij alle zijden even groot is. Dit bereiken we door `step / 2` naar rechts en naar beneden als afstand te nemen voor het begin punt van het volgende vierkant. Met `left(90)` zetten we de turtle weer terug naar zijn beginrichting.


#### Opdracht 3a

Schrijf de functie `lijn(x)` die een lijn tekent. De `x` geeft een hoe lang de lijn moet zijn. Aan het einde van de functie staat de turtle weer waar het was begonnen.

```python
def lijn(x):
    """ Tekent een lijn en zet de turtle weer terug op begin punt.
    """
    forward(x)
    up()
    right(180)
    forward(x)
    right(180)
    down()
```

De lijn hoeft maar een keer getekend te worden en net als met de vorige opdracht moet niet vergeten worden de kijkrichting van de turtle weer op de orginele positie te zetten. Dit kan met right(180) om zo een volledige cirkel te maken of met `left(180)` om de half cirkel ongedaan te maken.


#### Opdracht 3b

Schrijf de functie `simpleFlake(n, angle, length)`. De `n` geeft aan hoeveel lijnen er getekend moet worden. `angle` geeft aan hoeveel graden er na elke lijn gedraaid wordt. De parameter `length` geeft aan hoe lang elke lijn moet zijn.

```python
def simpleFlake(n, angle, length):
    """ Tekent een simpele sneeuwvlok.
    """
    if n == 0:
        return
    else:
        lijn(lengte)
        right(angle)
        simpleFlake(n - 1, angle, length)
```
# PGM1 Week 4

## Basis

### [Turtle](/problems/basis/4_turtle)


#### Opdracht 1a

Kopieer onderstaande code over naar een bestand genaamd `wk4ba1.py`. Probeer te voorspellen wat het programma zal tekenen.

```python
import time
from turtle import *
from random import *

def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """
    speed(10)
    drawStar(3, 150)
    done() # tell turtle the drawing is done.

def testing():
    """
    Test functie. Hier staan alle assertions om de functies te testen.
    """

def drawStar(n, distance):
    forward(distance)
    back(distance)
    right(72)

    forward(distance)
    back(distance)
    right(72)

    forward(distance)
    back(distance)
    right(72)

    forward(distance)
    back(distance)
    right(72)

    forward(distance)
    back(distance)
    right(72)

main()
testing()
```

In de main functie wordt de `drawStar` functie aangeroepen met de waarde 3 voor parameter n en waarde 150 voor waarde distance. Deze functie tekent eerst een horizontale lijn naar rechts, de start kijkrichting van turtle, met de lengte van parameter `distance`.

Vervolgens wordt turtle naar achteren geschoven zonder de kijkrichting te veranderen. Als turtle weer op zijn startpunt staat dan wordt zijn kijkrichting met 72 graden naar rechts gedraaid. Dit doet de functie in totaal vijf keer. Dus uiteindelijk zullen er vijf lijnen met een lengte 150 pixels op het scherm getekend worden en de hoek tussen elke lijn is 72 graden.

#### Opdracht 1b
<!---- Er staat een typo in de tekst van de opdracht drawStaw ipv drawStar ---->
Pas de functie drawStar aan. Aan elke punt van de ster wordt er een nieuwe ster getekend dat 3 keer zo klein is als de vorige ster.

```python
def drawStar(n, distance):
    if n == 0:
        return # Er hoeft niet nog een ster getekend te worden
    else:
        forward(distance) # Er moet op het einde van de lijn een nieuwe ster getekend worden
        drawStar(n-1, distance/3)
        back(distance) # Dus we gaan pas terug naar het begin punt als de ster op het einde getekend is
        right(72)

        forward(distance)
        drawStar(n-1, distance/3)
        back(distance)
        right(72)

        forward(distance)
        drawStar(n-1, distance/3)
        back(distance)
        right(72)

        forward(distance)
        drawStar(n-1, distance/3)
        back(distance)
        right(72)

        forward(distance)
        drawStar(n-1, distance/3)
        back(distance)
        right(72)
```

Parameter `n` geeft aan hoe veel niveaus sterren er zijn. Is `n` gelijk aan twee dan tekent het programma een hoofdster met op elke punt van de hoofdster een andere ster, drie keer zo klein. Wat gebeurt er als we `drawStar(0, 150)` aanroepen?

Omdat er op de punt van de ster een nieuwe ster getekend moet worden, roepen we de functie recursief aan voor turtle terug naar zijn beginpunt geschoven wordt. We gebruiken `n-1` omdat we het volgende niveau in gaan. Als we `n` gebruiken dan gaat turtle oneindig door omdat de base case niet gehaald wordt. Omdat de volgende ster drie keer zo klein moet zijn als de huidige ster doen we `distance/3`. Bij `drawStar(3, 300)` betekent dit dat de eerste ster lijnen van 300 pixels heeft, de sterren op de punten van de eerste sterren hebben lijnen van 100 pixels en de sterren op de punten van de tweede sterren hebben lijnen van 33 pixels.


#### Opdracht 2

Schrijf de functie `squares(n, distance, steps=0)`: te schrijven dat onderstaande vierkante fractal maakt. `n` geeft aan hoe diep de fractal moet gaan. `distance` geeft de grootte van het middelste vierkant. `steps` houdt bij hoe vaak de functie al is aangeroepen.

```python
def squares(n, distance, steps=0):
    #als n gelijk is aan 0 dan
    if n == 0:
        # als steps even is, dan moet er 90 graden naar links gedraaid worden
        if steps % 2 == 0: # Een even getal is altijd door twee te delen zonder rest getal
            left(90)
        # als steps oneven is, dan moet er 90 graden naar rechts gedraaid worden.
        else:
            right(90)
        # stop met tekenen
        return

    # ga vooruit
    forward(distance)
    # roep de functie opnieuw op met aangepaste variabelen
    squares(n-1, distance/2, steps+1)
    # ga vooruit
    forward(distance)
    # roep de functie opnieuw op met aangepaste variabelen
    squares(n-1, distance/2, steps+1)
    # ga vooruit
    forward(distance)
    # roep de functie opnieuw op met aangepaste variabelen
    squares(n-1, distance/2, steps+1)
    # ga vooruit
    forward(distance)

#Daan's plan vertaalt tot een werkende functie.
```

Op de eerste drie hoeken van elk vierkant, behalve de vierkanten van het laatste niveau, moet een kleinere vierkant getekend worden. Daarom wordt de functie `squares` drie keer recursief aangeroepen, een keer voor elke hoek van het vierkant behalve dus de vierde hoek. Als `n` gelijk is aan nul dan zijn alle niveaus getekend en stopt de recursie.

De functie wordt recursief aangeroepen met `n-1` om zo de verschillende niveaus van het fractal bij te houden. De `distance` wordt gedeeld door twee zodat het volgende vierkant twee keer zo klein is als het huidige niveau. Met `steps+1` wordt bijgehouden welke kant turtle moet kijken zodra `n` gelijk is aan nul zodat de nieuwe vierkanten in de juiste richting getekend worden.

### [Midterm](/problems/basis/4_midterm)

#### Opdracht 1

Het juiste antwoord is: **d**

Toelichting: op het moment dat variable `x` zijn waarde krijgt toegekend is de waarde van score 30.

#### Opdracht 2

Het juiste antwoord is: **c**

Toelichting: als het programma de `if`-constructie in gaat, is `x` groter dan twee. Dit activeert het `if`-statement en de andere elementen van de `if`-constructie worden niet uitgevoerd worden.

#### Opdracht 3

Het juiste antwoord is: **b**

Toelichting: omdat de start waarde van `x` acht is, wordt de eerste `if`-statement`True`. De waarde van`x` is nu 4. Nu volgt de volgende `if`-constructie. De `if` wordt geactiveerd want er wordt gevraagd of`x` kleiner dan of gelijk is aan vier, wat`True` is. Er wordt 3 opgeteld bij`x` en de `if`-constructie wordt verlaten.

#### Opdracht 4

Het juiste antwoord is: **b**

Toelichting: bij string vergelijkingen wordt naar de eerste letters gekeken. Zijn beide hetzelfde dan wordt naar de volgende letter gekeken. De `if`-constructie begint met een `if`-statement met een "E". Omdat de string ook begint met een "E" wordt naar de tweede letter gekeken, maar die is er niet in de tweede string dus is`x` groter dan "E" en wordt de `if`-statement`False`. Het programma gaat nu naar de if else met de vraag`x` kleiner dan "M". De letter E komt voor M in het alfabet dus deze vergelijking wordt`True`. De print statement bij deze `elif`-statement wordt uitgevoerd en de `if`-constructie wordt verlaten.

#### Opdracht 5

Het juiste antwoord is: **c**

Toelichting: om toegang te krijgen tot de letters van een string kan er gebruik gemaakt worden van index. De -1 in `woord[-1]` is een negatieve index, wat betekend dat in plaats van beginnen bij het eerste element/letter, er begonnen moet worden met het laatste element/letter. De -1 geeft toegang tot het laatste element van het woord.

#### Opdracht 6

Het juiste antwoord is: **c**

Toelichting: de index van een string begint met nul. Het eerste getal is het startpunt. Het getal na de dubbele punt is waar het stopt en dit element wordt niet meegenomen. Dus met `woord[3:6]` wordt het vierde, vijfde en zesde element opgevraagd.

#### Opdracht 7

Het juiste antwoord is: **a**

Toelichting: `string[start:stop:step]`, dus `woord[-1:1:-2]` zegt: begin bij het laatste element, maken stappen van twee naar links (het begin) en stop als het eerste element bereikt wordt.

#### Opdracht 8

Het juiste antwoord is: **d**

Toelichting: de functie wordt aangeroepen voordat hij gedefinieerd is. Hij bestaat dus nog niet op het moment dat de print statement het aanroept.

#### Opdracht 9

Het juiste antwoord is: **b**

Toelichting: `x`, het eerste argument, is kleiner dan y, het tweede argument dus de `if`-statement in de functie is `False` en de functie geeft daarom `y` terug.

#### Opdracht 10

Het juiste antwoord is: **c**

Toelichting:`x` is groter dan `y` dus de `if`-statement wordt`False` en de functie wordt verlaten zonder een fatsoenlijke return. Een return zonder waarde geeft een None terug. Dit wordt opgeslagen in `temp` en `temp` wordt naar het scherm geprint.

#### Opdracht 11

Het juiste antwoord is: **c**

Toelichting: met de gegeven argumenten voor `function1` wordt het `if`-statement in deze functie `False`. De functie geeft daarom de waarde die `function2` met als argument de waarde van `y`, welke 5 is, terug geeft.

#### Opdracht 12

Het juiste antwoord is: **a**

Toelichting: het return statement staat niet in de *scope* van het `if`-statement. Dus zodra het eerste `if`-statement klaar, stopt de functie met `return x`. Omdat het `if`-statement met de gegeven argumenten `False` wordt geeft de functie de originele waarde van`x` terug.

#### Opdracht 13

Het juiste antwoord is: **c**

Toelichting: omdat de print statement voor de base case en de recursie aanroep staat, wordt "hoi" elke keer dat de functie wordt aangeroepen naar het scherm geprint. Dus ook met `function(0)`, de vijfde aanroep van de functie.

#### Opdracht 14

Het juiste antwoord is: **b**

Toelichting: gebruik Pythontutor en volg het verloop van het programma.

#### Opdracht 16

Het juiste antwoord is: **d**

Toelichting: gebruik Pythontutor en volg het verloop van het programma.

#### Opdracht 16

Het juiste antwoord is: **a**

Toelichting: gebruik Pythontutor en volg het verloop van het programma.

#### Opdracht 17

Het juiste antwoord is: **a**

Toelichting: gebruik Pythontutor en volg het verloop van het programma.

#### Opdracht 18

Het juiste antwoord is: **b**

Toelichting: gebruik Pythontutor en volg het verloop van het programma.

#### Opdracht 19

Het juiste antwoord is: **c**

Toelichting: gebruik Pythontutor en volg het verloop van het programma.


## Context

### [Functies](/problems/context/4_functies)

#### Opdracht 1a

Schrijf een functie `max(l)` die een lijst `l` met getallen accepteert en het grootste getal teruggeeft.

```python
def max(l):
    """ Geeft het grootste getal uit een lijst integers.
    """
    if l == []:
        return

    M = max(l[1:])  # De max van de REST van l

    if M == None:
        return l[0]

    if l[0] > M:
        return l[0]
    else:
        return M
```

Als de lijst leeg is dan zijn er geen elementen meer om te vergelijken. Als er nog maar één element is en `max(l[1:])` wordt aangeroepen dan gaat de lijst out of bounds wat de waarde `None` geeft. Door gebruik te maken van een check of de lijst leeg is en of het recursief aanroepen een `None` teruggeeft, kunnen we voorkomen dat het programma stopt met een out of bounds foutmelding.


#### Opdracht 1b

Schrijf een functie `size(l)` die een lijst `l` accepteert en teruggeeft hoeveel objecten er in `l` zitten.

```python
def size(l):
    """ Geeft het aantal elementen in een lijst terug.
    """
    if l == []:
        return 0
    return 1 + size(l[1:])
```

Zolang de lijst niet leeg is, kunnen we het programma recursief aanroepen elke keer met één element minder. Voor elk element wordt 1 + recursieve aanroep terug gegeven. Zodra de lijst leeg is, wordt de recursie gestopt en een 0 terug gegeven.


#### Opdracht 1c

Schrijf een functie `add_up(l)` die een lijst `l` met getallen accepteert, alle getallen bij elkaar optelt en het resultaat teruggeeft.

```python
def add_up(l):
    """ Geeft de som van alle elementen in een lijst terug.
    """
    if l == []:
        return 0
    return l[0] + add_up(l[1:])
```

We kunnen hier hetzelfde doen als bij de `size` functie, maar in plaats van 1 + recursieve aanroep terug te geven, geven we de waarde van het element terug + recursieve aanroep.


#### Opdracht 2a

Schrijf een functie `present(l, c)` die een lijst `l` en variabele `c` accepteert en`True` teruggeeft of `c` in `l` zit en anders `False` teruggeeft.

```python
def present(l, c):
    """ Geeft een`True` terug als variable c in lijst l terug te vinden is anders geeft het een`False` terug.
    """
    if l == []:
        return False

    if l[0] == c:
        return True

    return present(l[1:], c)
```

De functie gaat recursief door de lijst tot de variable gevonden is en `True` teruggegeven kan worden of de lijst leeg is en `False` teruggegeven wordt.

#### Opdracht 2b

Schrijf een functie `count(l, c)` die een lijst `l` en variabele `c` accepteert en teruggeeft hoe vaak `c` in `l` zit.

```python
def count(l, c):
    """ Geeft terug hoe vaak variable c in lijst l zit.
    """
    if l == []:
        return 0

    if l[0] == c:
        return 1 + count(l[1:], c)
    return 0 + count(l[1:], c)
```

Deze keer moet de functie door blijven gaan zodra de variable de eerste keer is gevonden, in het geval deze meerdere keren in de lijst voorkomt. Daarom blijft de functie recursief aangeroepen worden maar met een + 0 als c niet op de gecontroleerde plek staat en een + 1 als het gecontroleerde element gelijk is aan de variable.


#### Opdracht 2c

Schrijf een functie `find(l, c)` die een lijst `l` en variabele `c` accepteert en de eerste index teruggeeft waar `c` staat. Zit `c` niet in `l` dan geeft de functie -1 terug.

```python
def find(l, c):
    """ Geeft de eerste index terug waar variable c in lijst l terug te vinden is.
    Als c niet terug te vinden is dan geeft het programma -1 terug.
    """
    if l == []:
        return -1

    if l[0] == c:
        return 0

    x = find(l[1:], c)

    if x == -1:
        return -1
    return 1 + x
```


#### Assert statements om de functies te controleren

Hier is een lijst en assert statements om je functies te controleren.

```python
lijst = [5, 1, 1, 1, 1, 3, 4, 1, 2, 1, 5]

assert max(lijst) == 5, "Max van lijst moet 5 zijn, check max()."
assert size(lijst) == 11, "Er horen 11 elementen in de lijst te zitten, check size()."
assert add_up(lijst) == 25, "De som van de lijst moet 25 zijn, check add_up()."
assert present(lijst, 9) == False, "9 staat niet in de lijst en present() moet dan een`False` geven, check present()."
assert present(lijst, 4) == True, "4 staat in de lijst en present() zou een`True` moeten terug geven, check present()."
assert count(lijst, 1) == 6, "Er staan 6 1-en in de lijst maar de count functie geeft wat anders, check count()."
assert count(lijst, 9) == 0, "Er staat geen 9 in de lijst maar de count functie geeft wat anders, check count()."
assert find(lijst, 5) == 0, "De eerste 5 staat op index 0, check find()."
assert find(lijst, 9) == -1, "Er staat geen 9 in de lijst dus de functie moet een -1 terug geven, check find()."
assert find(lijst, 4) == 6, "De eerste 4 is het zevende element en moet dus index 6 hebben, check find()."
assert find(lijst, 1) == 1, "De eerste 1 is het tweede element en moet dus index 1 hebben, check find()."
```


### [Recursieve turtles](/problems/context/4_turtle)

#### Opdracht

Definieer `flakeside` om de gegeven code te laten werken en implementeer de functie`flakeside(sidelength, levels)`, die één zijkant van de Koch-kromme tekent.

```python
import time
from turtle import *
from random import *

def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """
    # flakeside(300, 0)
    # flakeside(300, 1)
    # flakeside(300, 2)
    # flakeside(300, 3)

    # snowflake(300, 0)
    # snowflake(300, 1)
    # snowflake(300, 2)
    snowflake(300, 3)
    done() # tell turtle the drawing is done.

def testing():
    """
    Test functie. Hier staan alle assertions om de functies te testen.
    """

def flakeside(sidelength, levels):
    if levels < 1:
        forward(sidelength)
    else:
        flakeside(sidelength/3, levels-1)
        right(60)
        flakeside(sidelength/3, levels-1)
        left(120)
        flakeside(sidelength/3, levels-1)
        right(60)
        flakeside(sidelength/3, levels-1)

def snowflake(sidelength, levels):
    """Fractal snowflake function, complete.
       sidelength: pixels in the largest-scale triangle side
       levels: the number of recursive levels in each side
    """
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)

main()
testing()
```



---
title: Functies
description: Functies schrijven en testen
---

# Functies

Deze opgave bestaat uit het maken van verschillende functies. Vergeet niet elke functie te testen met assertions en vergeet de docstrings niet.

## Opdracht 1

a. Kopieer onderstaande code over naar een bestand genaamd `wk3ba2.py`.

```python
import time
from random import *

def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """

def testing():
    """
    Test functie. Hier staan alle assertions om de functies te testen.
    """

main()
testing()
```

b. Schrijf de functie `tpl(x)` die een getal als argument accepteert en drie keer de waarde van dat argument teruggeeft.

```ipython
In : tpl(4)
Out: 64

In: tpl("hoi")
Out: "hoihoihoi"
```

## Opdracht 2
a. Schrijf de functie `min_two(a, b)` dat twee getallen als argument accepteert en de kleinste waarde teruggeeft.

b. Schrijf de functie `min_three(a, b, c)` dat drie getallen als argument accepteert en de kleinste waarde teruggeeft.

## Opdracht 3

Schrijf de functie `absolute(x,y)` dat twee getallen accepteert en de afstand berekent tussen de twee getallen.

```ipython
In : absolute(3, 10)
Out: 7

In: absolute(-3, 10)
Out: 13
```

Denk aan Probeer, Plan, Programmeer!  Bedenk hoe je dit probleem oplost op papier voordat je gaat programmeren.

## Opdracht 4

Schrijf de functie `trap(x)` dat een getal accepteert en een omgekeerde # trap tekent. Maak gebruik van recursie

```ipython
In : trap(3)
Out:
###
##
#

In: trap(5)
Out:
#####
####
###
##
#
```

Hint: `3 * '#' = '###'`

## Opdracht 5

a. Schrijf de functie `lines(x, space)` dat twee #-lijnen tekent van x regels hoog en space geeft aan hoeveel spaties tussen de lijnen liggen.

```ipython
In : lines(3, 3)
Out:
#   #
#   #
#   #

In: lines(2, 5)
Out:
#     #
#     #
```

b. Schrijf een functie `print_square(x)` dat een getal accepteert en een # vierkant van grootte x print. Maak gebruik van de functie `lines`.


```ipython
In : printSquare(3, 3)
Out:
###
# #
###

In: lines(5)
Out:
#####
#   #
#   #
#   #
#####
```

Probeer, Plan, Programmeer!
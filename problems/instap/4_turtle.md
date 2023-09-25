---
title: Turtle
file: wk4in3.txt
---

# Turtle

Onderstaande opdrachten gaan allemaal over het tekenen met turtle.

## Opdracht 1

```python
def blaat(distance):

    left(90)
    forward(distance/2)
    right(90)
    forward(distance/2)

    right(180)
    forward(distance)

    right(180)
    forward(distance/2)
    right(90)
    forward(distance)

    left(90)
    forward(distance/2)

    right(180)
    forward(distance)

    right(180)
    forward(distance/2)
    left(90)
    forward(distance/2)
    right(90)
```

Wat wordt er getekend met de aanroep `blaat(50)` ?

## Opdracht 2

```python
def blaat(n, distance):

    if n == 0:
        return

    left(90)
    forward(distance/2)
    right(90)
    forward(distance/2)
    blaat(n-1, distance/2)
    right(180)
    forward(distance)
    blaat(n-1, distance/2)
    right(180)
    forward(distance/2)
    right(90)
    forward(distance)

    left(90)
    forward(distance/2)
    blaat(n-1, distance/2)
    right(180)
    forward(distance)
    blaat(n-1, distance/2)
    right(180)
    forward(distance/2)
    left(90)
    forward(distance/2)
    right(90)
```

Wat wordt er getekend met de aanroep `blaat(2, 100)`

---
title: Outputs
description: Lezen van functies
---

# Recursie

Bepaal de outputs van onderstaande programma's zonder het gebruik van een interperter.

## Opdracht 1



```python
def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """
    x = blaat(10)

def testing():
    """
    Test functie. Hier staan alle assertions om de functies te testen.
    """

def blaat(x):
    print(x)
    if x == 0:
        return
    blaat(x-1)

main()
testing()

```

a. Wat doet de functie blaat?  
b. Wat is de ouput van dit programma?  
c. Gebruik de [Python Tutor](http://www.pythontutor.com/visualize.html)  om je antwoord van a en b te controleren.  


## Opdracht 2

```python
def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """
    x = blaat(10, 2)

def testing():
    """
    Test functie. Hier staan alle assertions om de functies te testen.
    """

def blaat(x, y):
    print(x)
    if x == 0:
        return
    blaat(x-y, y)

main()
testing()

```

a. Wat doet de functie blaat?  
b. Wat is de ouput van dit programma?  
c. Wat is de ouput als `blaat(10, 2)` wordt vervangen met `blaat(5,0)`  
d. Gebruik de [Python Tutor](http://www.pythontutor.com/visualize.html)  om je antwoord van a, b en c te controleren.  


## Opdracht 3

```python
def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """
    x = blaat(10, 6)

def testing():
    """
    Test functie. Hier staan alle assertions om de functies te testen.
    """

def blaat(x, y):
    print(x)
    if x >= 20:
        return
    blaat(x+y, y)

main()
testing()
```


a. Wat doet de functie blaat?  
b. Wat is de ouput van dit programma?  
c. Gebruik de [Python Tutor](http://www.pythontutor.com/visualize.html)  om je antwoord van a en b te controleren.  

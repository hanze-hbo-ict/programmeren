---
title: Outputs
description: Lezen van functies
---

# Outputs

Bepaal de outputs van onderstaande programma's zonder het gebruik van een interperter.

## Opdracht 1



```python
def main():
    """
    Main functie. Roept de andere functies aan om hun werk te doen.
    """
    x = blaat(4) + blaat(6)
    print(x)

def testing():
    """
    Test functie. Hier staan alle assertions om de functies te testen.
    """

def blaat(x):
    l = list(range(x))
    return sum(l)

main()
testing()

```

a. Wat doet de functie blaat?  
b. Wat is de output van dit programma?  
c. Gebruik de [Python Tutor](http://www.pythontutor.com/visualize.html)  om je antwoord van a en b te controleren.  


## Opdracht 2
```python
def main():
    """
    Main functie. Roept de andere functies aan om hun werk te doen.
    """
    x = blaat("lol")
    y = blaat("xo")
    print(x + y)

def testing():
    """
    Test functie. Hier staan alle assertions om de functies te testen.
    """

def blaat(x):
    s = x[::-1] + x
    return s

main()
testing()

```

a. Wat doet de functie blaat?  
b. Wat is de output van dit programma?  
c. Gebruik de [Python Tutor](http://www.pythontutor.com/visualize.html)  om je antwoord van a en b te controleren.  


## Opdracht 3


```python
def main():
    """
    Main functie. Roept de andere functies aan om hun werk te doen.
    """
    l = blaat1(5)
    x = blaat2(l)
    print(x)

def testing():
    """
    Test functie. Hier staan alle assertions om de functies te testen.
    """

def blaat1(x):
    l = list(range(x))
    return l[::-1]

def blaat2(l):
    x = sum(l)
    y = len(l)
    return x / y

main()
testing()
```

a. Wat doet de functie blaat1?  
b. Wat doet de functie blaat2?  
c. Wat is de output van dit programma?  
d. Gebruik de [Python Tutor](http://www.pythontutor.com/visualize.html)  om je antwoord van a, b en c te controleren.  

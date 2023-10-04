---
title: Lezen van functies
file: wk5in1.txt
---

# Functies lezen

Maak onderstaande opdrachten zonder het gebruik van een interpreter.

## Opdracht 1

```python
def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """
    x = blaat("Test")

def testing():
    """
    Test functie. Hier staan alle assertions om de functies te testen.
    """

def blaat(x):
    print(x)
    if len(x) == 0:
        return
    blaat(x[:-1])

main()
testing()
```

a. Wat is de ouput van dit programma?

b. Gebruik de [Python Tutor](http://www.pythontutor.com/visualize.html) om je antwoord van a te controleren.


## Opdracht 2

```python
def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """
    x = blaat("Test", "e")
    print(x)

def testing():
    """
    Test functie. Hier staan alle assertions om de functies te testen.
    """

def blaat(x, y):
    if len(x) == 0:
        return True
    if x[0] == y:
        return False
    return blaat(x[1:], y)

main()
testing()
```

a. Wat is de ouput van dit programma?

b. Gebruik de [Python Tutor](http://www.pythontutor.com/visualize.html)  om je antwoord van a te controleren.

## Opdracht 3

```python
def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """
    print(blaat(10, 9))
    print(blaat(7, 6))
    print(blaat(13, 12))
    print(blaat(18, 17))

def testing():
    """
    Test functie. Hier staan alle assertions om de functies te testen.
    """

def blaat(x, y):
    if y == 1:
        return True
    if x % y == 0:
        return False
    return blaat(x, y-1)

main()
testing()
```

a. Wat is de ouput van dit programma?

b. Gebruik de [Python Tutor](http://www.pythontutor.com/visualize.html)  om je antwoord van a te controleren.

b. Wat is het doel van de functie `blaat()` ? Probeer verschillende inputs om tot een oplossing te komen.


## Opdracht 4

Schrijf een functie `order(L)` dat een lijst accepteert en een boolean teruggeeft om aan te geven of de lijst in de juiste volgorde staat.

Voorbeelden

```python
order("test") == False
order("abcde") == True
order(1,3, 6, 7, 9, 12) == True
order(1,5,8, 10, 5, 13, 18) == False
```

Kevin heeft geprobeerd deze opdracht te maken, maar er staan fouten in zijn code. Kan je ze allemaal vinden?

```python
def order(L):
    if len(L) == 0:
        return True
    if L[0] > L[1]:
        return False
    return order(L[:1])
```

## Opdracht 5

Elk bestand in de computer eindigt met een bestand extensie. Dit geeft aan wat voor bestand het is. Bijvoorbeeld .py laat de computer bijvoorbeeld weten dat het om een python bestand gaat. In een email is het vaak niet toegestaan om een bijlage mee te sturen dat eindigt op .exe Dit zou namelijk malware kunnen zijn dat schadelijk is voor de computer.

Schrijf een functie extensie_check(s, e) dat een string `s` en string `e` accepteert en aangeeft via een boolean of 's' eindigt met 'e'.

Voorbeelden:

```python
extensie_check("tentamen.docx", ".exe") ==  False
exentsie_check("program.exe", ".exe" == True
extensie_check("wk8ex1.py", ".py") == True
```

Kim heeft het volgende plan bedacht:

We kunnen via recursie bepalen of een string s eindigt met een string e:

*   Als string `e` leeg is, geef True terug,  `s` eindigt altijd met een lege string.
* 	Als string `s` leeg is, geef False terug. `e` kan namelijk niet aan einde van een lege string zitten.
*	Als de laatste letter van `e` niet gelijk is aan de laatste letter van `s`, geef False terug. In dit geval eindigt `s` dus niet met `e`.
*	Anders zijn de laatste letters wel gelijk en roep je de functie opnieuw op, maar dan zonder de laatste letters van beide strings en geeft het resultaat daarvan terug.


Schrijf een functie extensie_check(s, e) die gebruikt maakt van bovenstaande recursieve algoritme. Je mag geen gebruik maken van list comprehensions of lusconstructies.

## Opdracht 6

Schrijf een functie `maxDis(L)` dat een lijst met integers accepteert en het getal teruggeeft dat het verste van de nul afligt.

Mark heeft het volgende idee bedacht.

* Gebruik de functie `abs()` om van een negatief getal een positief getal te maken. Een positief getal blijft positief.
* Als er maar 1 element in `L  zit, geef dan dit element terug. De functie stopt hier.
* Pak de eerste element van de lijst en bewaar deze.
* Stuur de rest van de lijst door en wacht op antwoord.
* Vergelijk het eerste element van de lijst met het teruggekomen antwoord. Als het eerste element groter is, dan geeft de functie deze terug en anders het andere getal.

Schrijf een functie extensie_check(s, e) die gebruikt maakt van bovenstaande recursieve algoritme. Je mag geen gebruik maken van list comprehensions of lusconstructies.

# Een lusje om Python

| Naam         | Beschrijving                                                   |
|--------------|----------------------------------------------------------------|
| Onderwerp    | Lussen in Python                                               |
| Bestandsnaam | `wk7ex5.py`                                                    |
| Inleveren    | Lever jouw bestand met de juiste bestandsnaam in op GradeScope |

Bij de laatste opgave van deze week vragen we je drie Python-programma's die **lussen** gebruiken te lezen en te wijzigen.

Lussen zijn een krachtige controlestructuur voor *iteratie*, het herhaaldelijke uitvoeren van dezelfde actie.

Assembleertaal implementeert lussen met het commando `jump`; in deze opgave ga je aan de slag met de manier waarop Python dit doet: `for` en `while`

## Looping `for` a `while`...

Iets heel vaak herhalen is waar computers op hun best zijn; en mensen in het algemeen duidelijk niet van gediend zijn!

Plak, om een beeld te krijgen van het gebruik van *lussen*, deze functie met commentaar in een nieuw bestand `wk7ex5.py`. Dit is een functie die de faculteit berekent door middel van de `for`-lus van Python.

```python
#
# wk7ex5.py - Aan de slag met lussen!
#
# Naam:
#

def fac(n):
    """Loop-based factorial function

    Argument: a nonnegative integer, n
    Return value: the factorial of n
    """
    result = 1                 # beginwaarde; lijkt op een basisgeval
    for x in range(1, n + 1):  # herhaal van 1 tot en met n
        result = result * x    # pas het resultaat aan door keer x te doen
    return result              # merk op dat dit NA de lus is!

#
# Tests voor de lus-versie van de faculteit
#
assert fac(0) == 1
assert fac(5) == 120
```

## Lusfunctie 1: `power(b, p)`

Begin met het lezen en uitvoeren van bovenstaand bestand. Je zult zien dat de tests slagen.

Maak daarna een nieuwe functie `power(b, p)`, door de bovenstaande functie te kopiëren en aan te passen, of door de fuctie zelf te schrijven op dezelfde manier. Deze functie

-   Accepteert een numerieke waarde `b`, het grondtal
-   Accepteert een niet-negatieve integer `p`, de macht (`p` kan 0 zijn)
-   Geeft de waarde van `b ** p` terug
-   De functie moet een `for`-lus gebruiken! Je mag niet gewoon `b ** p` gebruiken...
-   In dit geval doen we alsof `power(0, 0)` gelijk is aan `1.0`, ook als dat wiskundig niet helemaal juist is.

Hier zijn een paar tests die je kan omzetten naar asserts:

```python
#
# Tests voor de lus-versie van machtsverheffen
#
print("power(2, 5): is 32 ==", power(2, 5))
print("power(5, 2): is 25 ==", power(5, 2))
print("power(42, 0): is 1 ==", power(42, 0))
print("power(0, 42): is 0 ==", power(0, 42))
print("power(0, 0): is 1 ==", power(0, 0))
```

::: {admonition} Overeenkomst met de faculteitsfunctie
:class: tip

De parameter `n` uit de faculteitsversie heeft dezelfde functie als de parameter `p` in deze functie. Het grondtal `b` wordt alleen gebruikt om mee te vermenigvuldigen.
:::

## Lusfunctie 2: `summed_odds(L)`

De functie `summed` hieronder bespreken we in het college. Kopieer de functie naar je bestand en probeer hem uit.

```python
def summed(L):
    """Loop-based function to return a numeric list.
       ("sum" is built-in, so we're using a different name.)

    Argument: L, a list of integers.
    Result: the sum of the list L.
    """
    result = 0
    for e in L:
        result = result + e    # of result += e
    return result

# tests!
assert summed([4, 5, 6]) == 15
assert summed(range(3, 10)) == 42
```

Maak nu zelf een functie `summed_odds(L)` door deze functie als voorbeeld te gebruiken, die

-   Een lijst integers `L` accepteert.
-   Je mag ervan uitgaan dat de lijst alleen integers bevat.
-   De functie moet de som teruggeven van alle **oneven** getallen in `L`.
-   Maak gebruik van een lus!

Vergeet niet de functie voldoende te testen!

```python
# tests!
assert summed_odds([4, 5, 6]) == 5
assert summed_odds(range(3, 10)) == 24
```

!!! tip "Een `if`-statement"
    Maak *binnen* de lus gebruik van een `if`-statement, zodat je de waarde alleen aan het resultaat toevoegd onder de juiste omstandigheden.

## Lusfunctie 3: `until_a_repeat(high)`

Bij deze functie kijken we naar wat ook wel de *verjaardagenparadox* wordt genoemd.

-   Zelfs in een vrij kleine groep mensen (al vanaf 23!) is de kans dat twee van die mensen dezelfde verjaardag hebben groter dan 50%.
-   [Wikipedia](https://nl.wikipedia.org/wiki/Verjaardagenparadox) heeft hier ook een pagina over met wat meer details.

Kopieer eerst deze functie om getallen te raden met een `while`-lus in je bestand.

```python
import random

def count_guesses(hidden):
    """Uses a while loop to guess "hidden", from 0 to 99.

    Argument: hidden, a "hidden" integer from 0 to 99.
    Result: the number of guesses needed to guess hidden.
    """
    guess = random.choice(range(0, 100))     # 0 tot en met 99
    num_guesses = 1                          # we hebben nu 1 keer geraden
    while guess != hidden:
        guess = random.choice(range(0, 100)) # opnieuw raden!
        num_guesses += 1                     # 1 toevoegen aan het aantal pogingen
    return num_guesses
```

Gebruik `count_guesses` als voorveeld om een variant te schrijven die we `until_a_repeat(high)` gaan noemen.

-   Deze functie houdt een lijst `L` bij van alle getallen die geraden zijn. Begin met `L = []`!
-   We blijven getallen raden zolang alle elementen van `L` uniek zijn (dus zolang er geen herhalingen zijn).
    -   Gebruik een `while`-lus!
    -   Gebruik de functie `unique(L)` hieronder die een boolean teruggeeft.
-   Binnen de `while`-lus doet de funtie het volgende:
    -   Gok een getal van 0 tot high met behulp van `range(0, high)`
    -   Houd het aantal geraden getallen bij (bijvoorbeeld met een telvariabele)
    -   Voeg het getal toe aan de lijst `L`
-   Als de `while`-lus klaar is moet de functie het aantal geraden getallen teruggeven dat nodig was om een dubbel getal te krijgen.

::: {admonition} Tellen
:class: tip

-   Onthoud dat je 1 aan een variabele kan toevoegen met `count += 1`
-   Op dezelfde manier kan je een element, bijvoorbeeld `42` aan het einde van een lijst toevoegen met `L = L + [42]`.

    Het element moet wel tussen blokhaken staan, omdat alleen lijsten mogen worden opgeteld bij een lijst.
:::

### Hulpfunctie: `unique(L)`

Hier is de hulpfunctie `unique` die je al eerder hebt gezien.

```python
def unique(L):
    """Returns whether all elements in L are unique.

    Argument: L, a list of any elements.
    Return value: True, if all elements in L are unique,
            or False, if there is any repeated element
    """
    if len(L) == 0:
        return True
    elif L[0] in L[1:]:
        return False
    else:
        return unique(L[1:])  # in deze functie mag je WEL recursie gebruiken!
```

Nadat je `until_a_repeat` hebt geschreven, kan je controleren dat `until_a_repeat(365)` inderdaad verrassend kleine getallen oplevert! Bijvoorbeeld,

```ipython
In [1]: until_a_repeat(365)
Out[1]: 25

In [2]: until_a_repeat(365)
Out[2]: 8

In [3]: until_a_repeat(365)
Out[3]: 23

In [4]: until_a_repeat(365)
Out[4]: 33
```

Probeer het daarna eens 10.000 keer met een list comprehension:

```python
L = [until_a_repeat(365) for i in range(10000)]
```

Je kan dan het gemiddelde, minimum en maximum van deze lijst `L` vinden:

```ipython
In [1]: sum(L) / len(L)

In [2]: max(L)

In [3]: min(L)

In [4]: 42 in L
```

Je hoeft deze resultaten niet in te leveren, maar kijk eens of de resultaten zijn zoals je verwacht zou hebben.

Soms is het lastig om te weten of de fout zit in je programma of in je verwachtingen!

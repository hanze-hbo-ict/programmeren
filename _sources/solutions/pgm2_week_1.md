# PGM2 week 1

## Basis

### [List comprehension](/problems/basis/8_list_comprehension)

#### Opdracht mult_of_five

```python
def mult_of_five(n):
    """Return a list containing the first n multiples of 5
    """
    return [x * 5 for x in range(1, n + 1)]

assert mult_of_five(0) == []
assert mult_of_five(1) == [5]
assert mult_of_five(2) == [5, 10]
assert mult_of_five(3) == [5, 10, 15]
```

Hier maken we gebruik van range() om het juiste aantal elementen te krijgen. Een [range(1,1)] geeft een lege lijst omdat deze range niks terug geeft. We doen x*5 om de veelvouden van 5 te krijgen.


#### Opdracht divisible_by

```python
def divisible_by(n, L):
    """Return a list with values in L divisible by n
    """
    return [x for x in L if x % n == 0]

assert divisible_by(5, [15, 0, 23, 4]) == [15, 0]
assert divisible_by(3, [2, 4, 8, 10]) == []
assert divisible_by(2, []) == []
```

Met de %-operator en de if-statement kunnen we testen welke waarden in de lijst L deelbaar zijn door n. Wordt de if-statement True dan wordt het betreffende element toegevoegd aan de lijst.


#### Opdracht starts_with

```python
def starts_with(s, L):
    """Return all strings in L which start with s
    """
    return [x for x in L if x[0:len(s)] == s]

assert starts_with("a", []) == []
assert starts_with("a", ["bbc", "brits", "omroep"]) == []
assert starts_with("a", ["abc", "cde", "aha", "abba"]) == ["abc", "aha", "abba"]
assert starts_with("ab", ["abc", "cde", "aha", "abba"]) == ["abc", "abba"]
assert starts_with("abc", ["abc", "cde", "aha", "abba"]) == ["abc"]
assert starts_with("abcd", ["abc", "cde", "aha", "abba"]) == []
```

We maken hier gebruik van len(s) om rekening te houden met lengte van s en zo dus het juiste deel van x te gebruiken in de if-statement.


#### Opdracht double_letters

```python
def double_letters(L):
    """Double all letters in L
    """
    return [x*2 for x in L]

assert double_letters(["a"]) == ["aa"]
assert double_letters(["a", "1", "23"]) == ["aa", "11", "2323"]
```

In plaats van x keer twee te doen, zou je ook x+x kunnen doen?


#### Opdracht num_as

```python
def num_as(L):
    """Count the number of a's in L
    """
    return sum([1 for x in L if x == 'a'])

assert num_as(["a", "b", "c", "a", "d"]) == 2
assert num_as(["y", "b", "c", "x", "d"]) == 0
```

Je hoeft niet x terug te geven, een constante kan ook zoals we hier gedaan hebben.


#### Opdracht vwl

```python
def vwl(s):
    ''' Return the number of vowels in a string
    '''
    return sum([1 for x in s if x in 'aeiou'])

assert vwl("appel") == 2
assert vwl("bbc") == 0
assert vwl("oma") == 2
```


#### Opdracht add_tax

```python
def add_tax(t, L):
    """Increment each item in L with t percent tax
    """
    return [(x + (x/100)*t) for x in L]

assert add_tax(7, [10, 100, 30, 40]) == [10.7, 107.0, 32.1, 42.8]
assert add_tax(7, [0, 16, 8]) == [0.0, 17.12, 8.56]
```

Zoals eerder gezien kun je berekeningen uitvoeren op x en het resultaat komt in de nieuwe lijst. Dit geldt ook voor complexe berekeningen. Met behulp van haakjes weten we zeker dat de berekeningen in de juiste volgorde gemaakt worden.


#### Opdracht above_below_freeze

```python
# Met hulp functie
# Hulp functie
def is_freeze(x):
    """ Return a string indicating if integer x is above, equal or below zero.
    """
    if x == 0:
        return "gelijk"
    if x > 0:
        return "boven"
    else:
        return "onder"

def above_below_freeze(L):
    """Return whether each item in L is below, above or
    equals freezing temperature as a string representation
    """
    return [is_freeze(x) for x in L ]

# Zonder hulp functie
# def above_below_freeze(L):
#     """Return whether each item in L is below, above or
#     equals freezing temperature as a string representation
#     """
#     return ["gelijk" if x == 0 else "boven" if x > 0 else "onder" for x in L ]
# # Dit is gelijk aan de volgende if structure:
# # if x == 0:
# #   print("gelijk")
# # else:
# #     if x > 0:
# #         print("boven")
# #     else:
# #         print("onder")

assert above_below_freeze([-1, 0, 10]) == ["onder", "gelijk", "boven"]
assert above_below_freeze([21, -21, 0]) == ["boven", "onder", "gelijk"]
```

De andere functie kan aangeroepen worden in de list comprehension met x als argument. Als de functie een waarde returned dan wordt deze toegevoegd aan de nieuwe list.

De functie kan ook uitgevoerd worden zonder hulp functie met een if else combinatie. elif kan niet in list comprehensions, maar we kunnen dat dus opvangen met een nested if statement. Als er alleen met een if statement gewerkt wordt dan kunnen we de volgorde uit de voorbeelden aanhouden, maar met meerdere condities en dus meerdere outputs wordt alles naar voren geschoven.


#### Opdracht zipper

```python
def zipper(L1, L2):
    """Pairwise combine lists L1 and L2
    """
    return [[L1[x], L2[x]] for x in range(0,len(L2))]

assert zipper([1, 3, 5], [2, 4, 6]) == [[1, 2], [3, 4], [5, 6]]
assert zipper([10, 9, 12], ["jan", "feb", "mar"]) == [[10, "jan"], [9, "feb"], [12, "mar"]]
```

In de asserts kunnen we zien dat de items van de eerste list ook als eerste in de output staan. Daarom houden we deze volgorde ook aan in de list comprehension. Omdat we op dezelfde plek de data uit beide lijsten moeten halen, is een enkele variable die de index representateert voldoende. We hoeven in dit geval range niet te corrigeren aangezien list index ook bij nul begint.


#### Opdracht only_evens

```python
def is_even(x):
    """Return True if x is even, False otherwise
    """
    return x % 2 == 0

def only_evens(L):
    """Returns a list containing the even numbers in L
    """
    return [x for x in L if is_even(x) == True]

assert only_evens([1, 1, 1]) == []
assert only_evens([2, 2, 2]) == [2, 2, 2]
assert only_evens([0, 1, 2, 3]) == [0, 2]
```

In de hulp functie maken we net als eerder gebruik van een if statement en de %-operator en de regels met betrekking tot integer devision.


## Context

### [Numerieke integratie](/problems/context/8_list_comprehension)

```python
# hiermee krijgen we functies als sin en cos...
from math import *

def main():
    """Main functie"""

def testing():
    """test functie"""
    assert lc_mult(4) == [0, 2, 4, 6]
    assert lc_idiv(4) == [0, 0, 1, 1]
    assert lc_fdiv(4) == [0.0, 0.5, 1.0, 1.5]
    assert unitfracs(2) == [0.0, 0.5]
    assert unitfracs(5) == [0.0, 0.2, 0.4, 0.6, 0.8]
    assert unitfracs(10) == [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    assert scaledfracs(10, 30, 5) == [10.0, 14.0, 18.0, 22.0, 26.0]
    assert scaledfracs(41, 43, 8) == [41.0, 41.25, 41.5, 41.75, 42.0, 42.25, 42.5, 42.75]
    assert scaledfracs(0, 10, 4) == [0.0, 2.5, 5.0, 7.5]
    assert sqfracs(10, 20, 2) == [100.0, 225.0]
    assert sqfracs(5, 10, 5) == [25.0, 36.0, 49.0, 64.0, 81.0]
    assert sqfracs(4, 5, 4) == [16.0, 18.0625, 20.25, 22.5625]
    assert f_of_fracs(dbl, 10, 20, 5) == [20.0, 24.0, 28.0, 32.0, 36.0]
    assert f_of_fracs(sq, 4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
    assert f_of_fracs(sin, 0, pi, 2) == [0.0, 1.0]
    assert f_of_fracs(sqrt, 1, 17, 2) == [1.0, 3.0]

    assert integrate(dbl, 0, 10, 4) == 75
    assert integrate(sq, 0, 10, 4) == 2.5 * sum([0, 2.5*2.5, 5*5, 7.5*7.5])

# twee extra functies (die niet in de module math hierboven zitten)

def dbl(x):
    """Doubler!  argument: x, a number"""
    return 2 * x

def sq(x):
    """Squarer!  argument: x, a number"""
    return x ** 2

# voorbeelden om aan list comprehensions te wennen...

def lc_mult(n):
    """This example accepts an integer n
       and returns a list of integers
       from 0 to n-1, **each multiplied by 2**
    """
    return [2 * x for x in range(n)]

def lc_idiv(n):
    """This example accepts an integer n
       and returns a list of integers
       from 0 to n-1, **each divided by 2**
       WARNING: this is INTEGER division...!
    """
    return [float(x // 2) for x in range(n)]

def lc_fdiv(n):
    """This example accepts an integer n
       and returns a list of integers
       from 0 to n-1, **each divided by 2**
       NOTE: this is floating-point division...!
    """
    return [x / 2 for x in range(n)]

# Hier begin je met de functies voor deze opgave:

# Stap 1, deel 1
def unitfracs(n):
    """Geeft een lijst van linkergrenzen (en dit zijn breuken, of fracties)
    op gelijke afstand van elkaar en met elk een waarde tussen 0 en 1 terug
    """
    #pass  # vervang deze regel (pass is een Python-statement dat niets doet)
    return[ x / n for x in range(n)]

def scaledfracs(low, hi, n):
    """Geeft een lijst met n linkergrenzen terug die evenredig verdeeld
    zijn over een interval dat van low tot hi loopt
    """
    diff = hi - low
    return [low + x * diff for x in unitfracs(n)]

def sqfracs(low, hi, n):
    """Geeft een lijst met n linkergrenzen terug die evenredig verdeeld
    zijn over een interval dat van low tot hi loopt en gekwadrateerd zijn
    """
    return [sq(x) for x in scaledfracs(low, hi, n)]

def f_of_fracs(f, low, hi, n):
    """ Geeft de fracties van low, hi en n en past de functie f toe op de fracties
    """
    return [f(x) for x in scaledfracs(low, hi, n)]

def integrate(f, low, hi, n):
    """Integrate returns an estimate of the definite integral
       of the function f (the first argument)
       with lower limit low (the second argument)
       and upper limit hi (the third argument)
       where n steps are taken (the fourth argument)

       integrate simply returns the sum of the areas of rectangles
       under f, drawn at the left endpoints of n uniform steps
       from low to hi
    """
    xDiff = (hi - low) / n
    y = f_of_fracs(f, low, hi, n)
    opps = sum(y) * xDiff
    return opps

def c(x):
    """c is a semicircular function of radius two"""
    return (4 - x ** 2) ** 0.5

print(integrate(c, 0, 2, 2))
print(integrate(c, 0, 2, 20))

testing()
```
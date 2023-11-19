# Lang leve lusjes

## Opdracht 1

Wat is de output van onderstaande programma's?

a.
```python
def fun1B():
    for i in range(1, 6):
        if i % 2 == 0:
            print("i is", i)
            return
fun1B()
```

b.
```python
def fun2B():
    for i in range(1, 6):
        if i % 2 == 0:
            print("i is", i)
        return
fun2B()
```

c.
```python
 def fun3B():
    for i in range(1,6):
        if i % 2 == 0:
            print("i is", i)
    return
fun3B()
```

d.
```python
def fun4B():
    for i in range(1,6):
        if i % 2 == 0:
            print("i is", i)
return
fun4B()
```

## Opdracht 2
Iets heel vaak herhalen is waar computers op hun best zijn; en mensen in het algemeen duidelijk niet van gediend zijn!

**a.**  Plak, om een beeld te krijgen van het gebruik van *lussen*, deze functie met commentaar in een nieuw bestand `wk9wc2.py`. Dit is een functie die de faculteit berekent door middel van de `for`-lus van Python.

```python
#
# wk9wc2.py - Aan de slag met lussen!
#
# Naam:
#
def main():
    """main functie"""

def testing():
    """test functie"""
    assert fac(0) == 1
    assert fac(5) == 120

def fac(n):
    """Loop-based factorial function

    Argument: a nonnegative integer, n
    Return value: the factorial of n
    """
    result = 1                 # beginwaarde; lijkt op een basisgeval
    for x in range(1, n + 1):  # herhaal van 1 tot en met n
        result = result * x    # pas het resultaat aan door keer x te doen
    return result              # merk op dat dit NA de lus is!

testing()
main()

```

**b** Lusfunctie 1: `power(b, p)`

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


## Opdracht 3

**a** Wat is de output van onderstaande programma?

```python
def function(L):
    result = 0
    for e in L:
        result = result + e    # of result += e
    return result

print(function([4, 5, 6]))
```

**b** Lusfunctie 2: `summed_odds(L)`

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



## opracht 4

**a** Wat is de output van onderstaande programma?

```python
def function(L):
    result = []
    for e in L:
        if e < 5:
            result +=  [e]
    return result

print(function([1, 2, 3, 4, 5, 6]))
```

**b** Lusfunctie 3: 'factors(n)'

Maak nu zelf een functie 'factors(n)' die:

- een integer 'n' ontvangt
- een lijst teruggeeft met alle factoren van 'n'

Vergeet niet de functie voldoende te testen
```python
assert factors(12) == [1, 2, 3, 4, 6, 12]
assert factors(15) == [1, 3, 5, 15]
```


## Opdracht 5

**a** Wat is de output van onderstaande programma?

```python
def function(s):
    result = ''
    for c in s:
        result = c + result
    return result

print(function("Hanze"))
```

**b** Lusfunctie 4: 'count_vowels(s)'

Maak zelf een functie 'count_vowels(s) die:
- Een string 's' accepteert
- de functie telt alle klinkers in de string en geeft dat terug als integer.

Maak zelf een aantal assertions om je functie te testen.
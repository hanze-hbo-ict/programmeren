# Iteraties

In de volgende opgaven ga je herhalingen schrijven met behulp van `for`- en `while`-lussen, list comprehension en recursie.

## Opgave 1

Gegeven is de volgende recursieve oplossing voor het tellen hoe vaak het getal 42 in een lijst `L` voorkomt

```python
def count_42(L):
    if len(L) == 0:
        return 0

    if L[0] == 42:
        return 1 + count_42(L[1:])
    else:
        return count_42(L[1:])

assert count_42([0, 42, 1, 42, 3]) == 2
```

Maak de volgende code af om het aantal keer 42 in een lijst met een `for`-lus te tellen

```python
def count_42(L):
    total = 0

    L = [0, 42, 1, 42, 3]

    for ... in ...:
        ...

    return total

assert count_42([0, 42, 1, 42, 3]) == 2
```

Maak de volgende code af om het aantal keer 42 in een lijst met een `while`-lus te tellen

```python
def count_42(L):
    total = 0

    while ...:
        ...

    return total
```

Maak de volgende code af om het aantal keer 42 in een lijst met een list comprehension te tellen

```python
def count_42(L):
    M = [... for ... in ... if ...]

    total = sum(M)

    return total

assert count_42([0, 42, 1, 42, 3]) == 2
```

## Opgave 2

**a.** Schrijf een programma dat een `for`-lus gebruikt om de getallen 1 tot en met 10 te printen. Je hoeft hier alleen maar de lus te schrijven, een functie is niet nodig.

**b.** Schrijf een programma dat een `while`-lus gebruikt om de getallen 1 tot en met 10 te printen. Ook hier hoef je geen functie te schrijven.

**c.** Schrijf een programma dat recursief de getallen 1 tot en met 10 print.


## Opgave 3

Schrijf een programma dat met een `while`-lus een voor een de even getallen tussen 20 en 40 print.

Tip: gebruik een variabele om het getal bij te houden, in de lus verminder je elke keer dit getal met 1 zolang het nog niet gelijk is aan 20.

## Opgave 4

Gegeven de volgende twee lijsten

```python
L = ["Mi", "na", "i", "Marj"]
M = ["jn", "am", "s", "olein"]
```

Maak met een list comprehension een nieuwe list `K` die paarsgewijs de elementen uit `L` en `M` samenvoegt, dus `L[0]` met `M[0]`, `L[1]` met `M[1]` enzovoort.

## Opgave 5

Gegeven de volgende lijst, maak met behulp van list comprehension een nieuwe lijst aan waar de lege waarden zijn verwijderd

```python
L = ["Tom", "", "Marie", "Isis", "", "Klaas"]
```


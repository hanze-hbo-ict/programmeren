---
title: "Voorbeelden van recursie"
description: "Voorbeelden van recursie"
---

# Voorbeelden van recursie

## `power(b, p)`

```python
def power(b, p):
    """power calculates b**p via recursion
       Argument: b, a number
       Argument: p, an integer
    """
    if p == 0:
        return 1
    elif p < 0:    # dit is optioneel
        return 1.0 / power(b, -p)
    else:
        return b * power(b, p - 1)
```

## `add(m, n)`

```python
def add(m, n):
    """add calculates m + n via recursion and adding 1
       Argument: m, a number
       Argument: n, an integer
    """
    if n == 0:
        return m
    else:
        return add(m, n - 1) + 1
```

## `leng(s)`

```python
def leng(s):
    """leng returns the length of s
        Yes, it's already built in as len(s), but...
        Argument: s, which can be a string or list
    """
    if s == '' or s == []:   # als lege string of lege lijst
        return 0
    else:
        return 1 + leng(s[1:])
```

## `vwl(s)`

```python
def vwl(s):
    """vwl returns the number of vowels in s
       Argument: s, which will be a string
    """
    if s == '':
        return 0   # geen klinkers in de lege string
    elif s[0] in 'aeiouy':
        return 1 + vwl(s[1:])
    else:
        return 0 + vwl(s[1:])   # De 0 + is niet nodig maar ziet er mooier uit
```

## `mymax(L)`

```python
def mymax(L):
    """mymax returns the largest element in L
       (this is also built-in, as max)
       Argument: L, a _nonempty_ list
    """
    if len(L) == 1:
        return L[0]
    elif L[0] < L[1]:
        return mymax(L[1:])           # de eerste vervalt
    else:
        return mymax(L[0:1] + L[2:])  # de tweede vervalt
```

## `zeroest(L)`

```python
def zeroest(L):
    """zeroest returns the element closest to 0 in L
       Argument: L, a _nonempty_ list
    """
    if len(L) == 1:
        return L[0]

    z = zeroest(L[1:])      # welke is het dichtst bij nul in de rest van L?

    if abs(L[0]) < abs(z):
        return L[0]         # L[0] was dichter bij nul!
    else:
        return z            # z was dichter bij nul!
```

## `reverse(s)`

```python
def reverse(s):
    """Return s in reversed order
       Argument: s, which will be a string
    """
    if len(s) == 1:         # basisgeval
        return s
    else:                   # recursief geval
        return reverse(s[1:]) + s[0]
```
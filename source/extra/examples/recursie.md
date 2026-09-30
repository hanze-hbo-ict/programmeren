---
title: "Voorbeelden van recursie"
description: "Voorbeelden van recursie"
---

# Voorbeelden van recursie

## `power(b, p)`

```python
def power(b, p):
    """Geeft b tot de macht p, voor een geheel getal p."""
    if p == 0:  # basisgeval
        return 1
    elif p < 0:  # dit is optioneel
        return 1.0 / power(b, -p)
    else:  # recursief geval
        return b * power(b, p - 1)
```

## `add(m, n)`

```python
def add(m, n):
    """Geeft m + n door n keer 1 op te tellen; n is 0 of groter."""
    if n == 0:  # basisgeval
        return m
    else:  # recursief geval
        return add(m, n - 1) + 1
```

## `leng(s)`

```python
def leng(s):
    """Geeft de lengte van de string of lijst s, net als de ingebouwde len(s)."""
    if s == "" or s == []:  # basisgeval: een lege string of een lege lijst
        return 0
    else:  # recursief geval
        return 1 + leng(s[1:])
```

## `vwl(s)`

```python
def vwl(s):
    """Geeft het aantal klinkers in de string s; hier telt de y mee."""
    if s == "":  # basisgeval
        return 0  # geen klinkers in de lege string
    elif s[0] in "aeiouy":  # recursief geval
        return 1 + vwl(s[1:])
    else:  # recursief geval
        return 0 + vwl(s[1:])  # De 0 + is niet nodig maar ziet er mooier uit
```

## `mymax(L)`

```python
def mymax(L):
    """Geeft het grootste element van L, net als de ingebouwde max; L is niet leeg."""
    if len(L) == 1:  # basisgeval
        return L[0]
    elif L[0] < L[1]:  # recursief geval
        return mymax(L[1:])  # de eerste vervalt
    else:  # recursief geval
        return mymax(L[0:1] + L[2:])  # de tweede vervalt
```

## `zeroest(L)`

```python
def zeroest(L):
    """Geeft het element van L dat het dichtst bij 0 ligt; L is niet leeg."""
    if len(L) == 1:  # basisgeval
        return L[0]

    z = zeroest(L[1:])  # welke is het dichtst bij nul in de rest van L?

    if abs(L[0]) < abs(z):
        return L[0]  # L[0] was dichter bij nul!
    else:
        return z  # z was dichter bij nul!
```

## `reverse(s)`

```python
def reverse(s):
    """Geeft de string s achterstevoren; s is niet leeg."""
    if len(s) == 1:  # basisgeval
        return s
    else:  # recursief geval
        return reverse(s[1:]) + s[0]
```

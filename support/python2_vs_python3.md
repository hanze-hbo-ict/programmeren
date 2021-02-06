---
title: "Python 2 en Python 3"
description: "Een korte uitleg over verschillen tussen Python 2 en Python 3"
---

# Python 2 en Python 3

Python 3 is de nieuwste versie (maar bestaat al sinds 2008!) en Python 2 wordt sinds 1 januari 2020 niet meer verder ontwikkeld of ondersteund.

Als je al eerder in Python 2 geprogrammeerd hebt dan is de overstap naar Python 3 niet *heel* groot, maar er zijn een aantal belangrijke verschillen. **Deze lijst is in volgorde van meest naar minder voorkomend.**

:::{admonition} In detail
:class: info

Zie voor een meer compleet overzicht [The key differences between Python 2.7.x and Python 3.x with examples](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html).
:::

## De functie `print`

In Python 3 is `print` een *functie* en niet een *statement*, je moet dus haakjes om het argument zetten. De functie `print()` werkte overigens ook al in Python 2, maar het gebruik van het statement `print` zal in Python 3 een fout geven. Dit is een klein maar belangrijk verschil.

In Python 2:

```ipython
In [1]: print "Hallo wereld!"
'Hallo wereld!'
```

In Python 3:

```ipython
In [1]: print("Hallo wereld!")
'Hallo wereld!'
```

## Integerdeling

Python 3 voert nu een *floating-point*deling uit als een enkele slash (`/`) wordt gebruikt, in Python 2 was dit een *integer*deling. In Python 3 moet nu een dubbele slash (`//`) worden gebruikt voor een integer deling.

In Python 2:

```ipython
In [1]: 3 / 2
Out[1]: 1
```

In Python 3:

```ipython
In [1]: 3 / 2
Out[1]: 1.5

In [2]: 3 // 2
Out[2]: 1
```

## `execfile()`

`execfile()` bestaat niet meer in Python 3, in plaats hiervan gebruiken we het `run`-commando in IPython.

## `raw_input()`

`raw_input()` is nu `input()` en Python 3 schoont de invoer die met `input` gelezen wordt automatisch op (dat wil zeggen, het leest de invoer altijd als een *string*). Om het oude gedrag van Python 2
te krijgen, moet `eval(input())` worden gebruikt, maar dit is niet aan te raden.

In Python 2:

```ipython
In [1]: foo = input()
1 + 2

In [2]: type(foo)
Out[2]: int

In [3]: foo
Out[3]: 3
```

In Python 3:

```ipython
In [1]: foo = input()
1 + 2

In [2]: type(foo)
Out[2]: str

In [3]: foo
Out[3]: '1 + 2'
```

## Geen long of short integers

Er zijn geen long of short integers meer in Python 3. Alle `int`s in Python 3 werken als `long`s in Python 2, alleen staat er geen `L` meer
achter het resultaat van `repr`.

## Vergelijken van types

Het vergelijken van variabelen van verschillende types werkt niet meer. In Python 2 kon bijvoorbeeld `'spam' > 42` worden vergeleken en gaf het als resultaat `True`. Dit werkt niet meer in Python 3 en in plaats daarvan krijg zal een `TypeError` foutmelding volgen. Dit betekent ook dat lijsten met verschillende types niet meer kunnen worden gesorteerd.

## `range()` als generator

In Python 3 geeft `range()` een *generator* terug in plaats van een lijst. In Python 3 werkt `range()` op dezelfde manier als `xrange()` in Python 2, en is `xrange()` verwijderd. Om het gedrag van Python 2 na te bootsen kan je `list(range())` gebruiken.

In Python 2:

```ipython
In [1]: L = range(2)

In [2]: L
Out[2]: [0, 1]
```

In Python 3:

```ipython
In [1]: L = range(2)

In [2]: L
Out[2]: range(2)

In [3]: L = list(range(2))

In [4]: L
Out[4]: [0, 1]
```

## `reduce()`, `file()` en `reload()`

`reduce()`, `file()` en `reload()` zijn niet meer ingebouwd in Python 3

- `reduce()` moet nu worden geïmporteerd uit `functools`.
- `file()` moet nu worden geïmporteerd uit `io`.
- `reload()` moet nu worden geïmporteerd uit `importlib`.

## Verwijderd of hernoemd

Belangrijke modules die niet meer werken (of hernoemd zijn) in Python 3:

- `visual`: VPython in Python 3 is behoorlijk veranderd ten opzichte van VPython in Python 2.
- `imp`: gebruik in plaats hiervan `importlib`, deze lijken erg op elkaar

## Bytes, encoding en `chr()`

`chr()` zal niet meer een `ValueError` genereren als de karaktercodes groter zijn dan 256 omdat UTF-8 nu de standaard tekstcodering is. Dit kan ook andere zaken als het lezen van bestanden als bytes beïnvloeden.

## `dict.keys()` en `dict.values()`

`dict.keys()` en `dict.values` geven nu een object in plaats van een lijst terug.

Verder zijn een aantal van de aanroepen in `dict` zijn veranderd, zie het eerder genoemde artikel voor meer details.

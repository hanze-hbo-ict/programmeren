---
title: "Picobot: Rondjes rennen"
description: "Kennismaken met Picobot"
csa-chapter: 1
csa-level: Beginner
file: wk2in2.txt
---

# Busreis

## Opdracht uit de herkansing van 2022-2023

Tijdens een busreis worden studenten verdeelt over verschillende bussen aan de hand van hun achternaam.

|Bus	|Eerste letter achternaam|
|1|	A t/m E|
|2|	F t/m J|
|3|	K t/m O|
|4|	Q t/m U|
|5|	V t/m Z|

Student met de achternaam Niël komt in bus 3
Student met de achternaam Hoebe komt in bus 2

Gegeven is een variabele naam die staat voor de achternaam ( zonder voorvoegsels en met hoofdletter) van een student, deze toekenning hoef je niet te schrijven. Schrijf een conditionele statement (geen functie) om de juiste bus nummer af te drukken. Je hoeft de bus nummer dus niet een variabele op te slaan.

## Opgave

Deze opdracht is op veel manieren op te lossen. Hieronder staan een aantal oplossingen, maar er zit telkens een fout in. Welke fout is er gemaakt waardoor de code niet klopt? Maak geen gebruik van een interpeter.

a.

```python
if naam[0] <= 'E':
    print(1)
if naam[0] <= 'J':
    print(2)
if naam[0] <= 'O':
    print(3)
if naam[0] <= 'U':
    print(4)
else
    print(5)

```

b.

```python
if naam[0] >= 'E':
    print(1)
elif naam[0] >= 'J':
    print(2)
elif naam[0] >= 'O':
    print(3)
elif naam[0] >= 'U':
    print(4)
else:
    print(5)

```
c.

```python
if naam[0] <= 'E':
    print(1)
else:
    if naam[0] <= 'J':
        print(2)
    elif naam[0] <= 'O':
        print(3)
        if naam[0] <= 'U':
            print(4)
        else:
            print(5)

```
d.
```python
if naam[0] <= 'E':
    print(1)
elif naam[0] <= 'J':
    print(2)
    elif naam[0] <= 'O':
        print(3)
    elif naam[0] <= 'U':
        print(4)
    else:
        print(5)

```

e.
```python
if naam[0] <= 'Z':
    print(5)
elif naam[0] <= 'U':
    print(4)
elif naam[0] <= 'O':
    print(3)
elif naam[0] <= 'J':
    print(2)
else:
    print(1)

```


f.

```python
if naam <= 'E':
    print(1)
elif naam <= 'J':
    print(2)
elif naam <= 'O':
    print(3)
elif naam <= 'U':
    print(4)
else:
    print(5)

```

g.

```python
if naam < 'F'
    print(1)
elif naam < 'K'
    print(2)
elif naam < 'P'
    print(3)
elif naam < 'V'
    print(4)
else:
    print(5)
```


h.

```python
if naam[0] >= 'A' or naam[0] <= 'E':
    print(1)
elif naam[0] >= 'F' or naam[0] <= 'J':
    print(2)
elif naam[0] >= 'K' or naam[0] <= 'O':
    print(3)
elif naam[0] >= 'Q' or naam[0] <= 'U':
    print(4)
else:
    print(5)

```

i.
Geef een juiste oplossing voor dit probleem.


# Opstap

## Syntax van conditionele statements
 Leerdoel: Lezen van conditionele statements in python

### Opdracht
In deze opdracht is het vooral de bedoeling om te bepalen wat de output is van de code. Test je antwoorden met behulp van de [python tutor](https://pythontutor.com/visualize.html#mode=edit). 

Wat is de output?

a.

```python
x = 8
if x > 5 :
    print("if statement is True")
print("staat buiten de if statement")

```

b.

```python
x = 8
if x < 5 :
    print("if statement is True")
print("staat buiten de if statement")

```

c.

```python
x = 8
if x < 5 :
    print("if statement is True")
else:
    print("if statement is false")
print("staat buiten de if-else statement")

```

d.

```python
x = 5
if x < 5 :
    print("if statement is True")
elif x > 5:
    print("elif statement is True")
else:
    print("zowel de if en elif statements zijn false")
```

e.

```python
temp = 23.0

if temp > 35.0:
    print("Heet!")
elif temp > 20.0:
    print("Warm")
elif temp > 10.0:
    print("Koel")
else:
    print("Brrr!")
```

f.

```python
temp = 15.0

if temp > 35.0:
    print("Heet!")
else:
    if temp > 20.0:
        print("Warm")
    else:
        if temp > 10.0:
            print("Koel")
        else:
            print("Brrr!")
```


g.

```python
x = 5
if x < 5 :
    x = x + 3
elif x > 5:
    x = x - 3
print(x)
```

h.

```python
x = 4
if x < 5 :
    x = x + 3
elif x > 5:
    x = x - 3
else:
    x = x * 2
print(x)
```

i.

```python
naam = "Suzan"
if naam <= 'E':
    print("groep 1")
elif naam <= 'J':
    print("groep 2")
elif naam <= 'O':
    print("groep 3")
elif naam <= 'U':
    print("groep 4")
else:
    print("groep 5")
```

j.

```python
naam = "Emily"
if naam  <= 'E':
    print("groep 1")
elif naam  <= 'J':
    print("groep 2")
elif naam  <= 'O':
    print("groep 3")
elif naam <= 'U':
    print("groep 4")
else:
    print("groep 5")
```



## Syntax van strings
 Leerdoel: Syntax omrent het gebruik van strings en lijsten in Python

### Opdracht 1

Wat is de output ?

a.

```python
a = "123"
print(2 * a)
```

b.

```python
a = "hanze"
b = "Hogeschool"
print(2 * a + b)
```

c.

```python
a = 123
b = "456"
print(a, b)
```
d.  
```python
p = [3,1,4,1,5]
c = [2,9,9,7,9,2,4,5,8]
answer0 = p[0:3]
answer1 = c[5]
print(answer0 * answer1)
```

e.  

```python
c = "computer"
s = "science"

answer0 = s[2:0:-1]
answer1 = c[5]
print(s[2:0:-1] + c[5] + s[2::-2] + s[0] + c[4:2:-1]  + c[6:])
```

### Opdracht 2

```python
pi = [3, 1, 4, 1, 5, 9]

L = ['pi', "isn't", [4,2]]
```

1. Wat is `len(pi)`?
2. Wat is `len(L)`?
3. Wat is `len(L[1])`?
4. Wat is `pi[2:4]`?
5. Welk puntje ("slice") `pi` is gelijk aan `[3,1,4]`? (hint, neem het aantal elementen als stop waarde)
6. Welk puntje `pi` is `[3,4,5]`?

### Opdracht 3

```python
L = ['pi', "isn't", [4,2]]

M = 'You need parentheses for chemistry !'
#    0   4   8   12  16  20  24  28  32
```

1. Wat is `L[0]`?
2. Wat is `L[0][1]`?
3. Wat is `L[0:1]`?
6. Wat is `M[9:15]`?
7. Wat is `M[::5]`?
4. Welk puntje M is `'try'`?
5. Welk puntje M is `'shoe'`?

## Opdracht 4

```python
pi = [3, 1, 4, 1, 5, 9]
```

1. Wat is `pi[0] * (pi[1] + pi[2])`?
2. Wat is `pi[0] * (pi[1:2] + pi[2:3])`?
3. Hoe krijg je `[3,4,5,3,4,5,3,4,5]`?

## Opdracht 5
True or false?

```python
a. [4,2] > [42]
b. "hoi" > "doei"
c. "eten" > "werken"
d. "Haard" < "Huis"
e. "F" < "Fiets"
f. [4, "m&m's"] < [1, "koffie"]
```


## Debugging

Leerdoel: Vinden van bugs in conditionele statements

**Opdracht uit de herkansing van 2022-2023**

Tijdens een busreis worden studenten verdeelt over verschillende bussen aan de hand van hun achternaam.

| Bus | Eerste letter achternaam |
| --- | ------------------------ |
| 1   | A t/m E                  |
| 2   | F t/m J                  |
| 3   | K t/m O                  |
| 4   | Q t/m U                  |
| 5   | V t/m Z                  |

Student met de achternaam Niël komt in bus 3
Student met de achternaam Hoebe komt in bus 2

Gegeven is een variabele naam die staat voor de achternaam ( zonder voorvoegsels en met hoofdletter) van een student, deze toekenning hoef je niet te schrijven. Schrijf een conditionele statement (geen functie) om de juiste bus nummer af te drukken. Je hoeft de bus nummer dus niet een variabele op te slaan.

### Opgave

Deze opdracht is op veel manieren op te lossen. Hieronder staan een aantal oplossingen, maar er zit telkens een fout in. Welke fout is er gemaakt waardoor de code niet klopt? Test je antwoord met behulp van de python tutor. 

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


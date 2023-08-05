---
title: "Picobot: Rondjes rennen"
description: "Kennismaken met Picobot"
csa-chapter: 1
csa-level: Beginner
---

| Naam         | Beschrijving                                                   |
|--------------|----------------------------------------------------------------|
| Onderwerp    | Outputs                                                        |
| Leerdoel     | Lezen van code                                                 |
| Bestandsnaam | `wk2in1.txt`                                                   |
| Inleveren    | Lever jouw bestand met de juiste bestandsnaam in op GradeScope |


Bepaal de outputs van onderstaande programma's zonder het gebruik van een interperter. 

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

k. 

```python
p = [3,1,4,1,5]
c = [2,9,9,7,9,2,4,5,8]
answer0 = p[0:3]
answer1 = c[5]
print(answer0 * answer1)
```

l. 

```python
c = "computer"
s = "science"

answer0 = s[2:0:-1]
answer1 = c[5]
print(s[2:0:-1] + c[5] + s[2::-2] + s[0] + c[4:2:-1]  + c[6:])
```
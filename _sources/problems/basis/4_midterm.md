---
title: Midterm
file: wk4ba2.txt
---

# Midterm


## 1. Welke waarde heeft x aan het einde van dit programma?

```python
max_punten = 100
score = 30
x = score/max_punten * 9 + 1
score = 50

```

 -  **a** 50
 -  **b** 2.7
 -  **c** 5.5
 -  **d** 3.7


## 2. Welke waarde heeft x aan het einde van dit programma?

```python
x = 4
if x > 2 :
    x = x / 4
elif x < 2 :
    x = x + 3
else :
    x = x * 3
```

 -  **a** 4
 -  **b** 12
 -  **c** 1
 -  **d** 7


## 3. Welke waarde heeft x aan het einde van dit programma?

```python
x = 8
if x > 5 :
    x = x - 4
if x <= 4 :
    x = x + 3
elif x == 7 or x == 4 :
    x = x * 2
```

 -  **a** 14
 -  **b** 7
 -  **c** 4
 -  **d** 8


## 4. Wat print dit programma?

```python
x = "Emily"

if x < "E":
    print ("groep 1")
elif x < "M":
    print ("groep 2")
elif x < "Z":
    print ("groep 3")
else:
    print ("groep 4")

```

 -  **a** ‘groep 1’
 -  **b** ‘groep 2’
 -  **c** ‘groep 3’
 -  **d** ‘groep 4’


## 5. Wat print dit programma?

```python
woord = "Hanzehogeschool"
print(woord[-1])
```

 -  **a** ‘H’
 -  **b** ‘a’
 -  **c** ‘l’
 -  **d** ‘o’


## 6. Wat print dit programma?

```python
woord = "Hanzehogeschool"
print(woord[3:6])
```

 -  **a** ‘’nze’
 -  **b** ‘nzeh’
 -  **c** ‘zeh’
 -  **d** ‘zeho’


## 7. Wat print dit programma?

```python
woord = "Hanzehogeschool"
print(woord[-1:1:-2])
```


 -  **a** ‘loceoen’
 -  **b** ‘azhgsho’
 -  **c** ‘Hneoecol’
 -  **d** ‘’


## 8. Wat print dit programma?

```python
print(function(5, 10))

def function(x, y):
    if x <= y:
        return x
```

 -  **a** 5
 -  **b** 10
 -  **c** None
 -  **d** programma werkt niet


## 9. Wat print dit programma?

```python
def function(x, y):
    if x > y:
        return x
    return y

print(function(5, 10))
```

 -  **a** 5
 -  **b** 10
 -  **c** None
 -  **d** programma werkt niet


## 10. Wat print dit programma?

```python
def main():
    temp = function(10, 5)
    print(temp)


def function(x, y):
    if x < y:
        return x

main()
```

 -  **a** 5
 -  **b** 10
 -  **c** None
 -  **d** programma werkt niet


## 11. Wat print dit programma?

```python
def main():
    temp = function1(10, 5)
    print(temp)


def function1(x, y):
    if x < y:
        return function2(x)
    return function2(y)

def function2(x):
    return x * x

main()
```

 -  **a** 5
 -  **b** 10
 -  **c** 25
 -  **d** 100
 -  **e** None
 -  **f** programma werkt niet


## 12. Wat print dit programma?

```python
def main():
    temp = function1(5, 12)
    print(temp)


def function1(x, y):
    if x % 2 == 0:
        x = x/2
    return x
    if x < y:
        return x
    return y

main()
```

 -  **a** 5
 -  **b** 12
 -  **c** None
 -  **d** Programma werkt niet


## 13. Hoe vaak print dit programma “hoi”  ?

```python
def function(y):

    print("hoi")

    if y == 0:
        return

    function(y-1)

function(4)
```

 -  **a** 3
 -  **b** 4
 -  **c** 5
 -  **d** Programma werkt niet


## 14. Wat print dit programma?

```python
def function(x):

    if x == 0:
        return x
    print(function(x-1))
    return x

function(5)
```

 -  **a** 1,2,3,4,5
 -  **b** 0,1,2,3,4
 -  **c** 5,4,3,2,1
 -  **d** 4,3,2,1,0

## 15. Wat print dit programma?

```python
def function(x, y):

    print(x[y])

    if y == 0:
        return

    function(x, y-1)
    print(y)


function("Hanze", 4)
```

 -  **a** H, 0, a, 1, n, 2, z, 3, e, 4
 -  **b** H, a, n, z, e, 0, 1, 2, 3, 4,
 -  **c** e, z, n, a, H, 4, 3, 2, 1, 0
 -  **d** e, z, n, a, H, 1, 2, 3, 4
 -  **e** H, a, n, z, e, 4, 3, 2, 1
 -  **f** e, 4, z, 3, n, 2, a, 1, H

## 16. Wat print dit programma?

```python

def function(x):
    if len(x) == 0:
        return
    function(x[:-1])
    print(x[-1])

function("Hanze")
```


 -  **a** H, a, n, z, e
 -  **b** e, z, n, a, H
 -  **c** H, H, H, H, H
 -  **d** H, a, n, z

## 17. Welke error geeft dit programma?


```python
def function(x):

    print(x[0])

    if len(x) == 0:
        return

    function(x[:-1])

function("Hanze")
```

 -  **a** IndexError
 -  **b** RecursionError
 -  **c** TypeError
 -  **d** SyntaxError


## 18. Gegeven de volgende regels aan code.

```{code-block} python
---
linenos: True
---
function([1,2,3,4,5], 4)
def function(x,y):
    function(x[:-1], y-1)
    if y == 0:
    print(x[0:y])
        return
```

In welke volgorde moeten deze regels staan om de volgende output te krijgen:
[1, 2, 3, 4]
[1, 2, 3]
[1, 2]
[1]


 -  **a** 1, 2, 5, 4, 6, 3
 -  **b** 2, 4, 6, 5, 3, 1
 -  **c** 1, 2, 4, 6, 5, 3
 -  **d** 2, 5, 4, 6, 3, 1


## 19. Gegeven de volgende regels aan code.

```{code-block} python
---
linenos: True
---
def function(x,y,z):
    if y == z:
        return

    function(x, y+1, z)

function("x", 2, 5)
```

Welke printstatement moet er op regel 4 komen om de volgende output te generen ?

```text
   xxxx
  xxxxxx
 xxxxxxxx
```

```python
 -  a print(y*' ' + x*y)
 -  b print(y*' ' + x*y*2)
 -  c print((z-y)*' ' + x*y*2)
 -  d print((z-y)*' ' + x*y)
```

# Reading code

## Opdracht 1

Welke error geeft onderstaande code?

```python
def function(x):

    print(x[0])

    if len(x) == 0:
        return

    function(x[:-1])

function("Hanze")
```

## Opdracht 2

Wat is de output van onderstaande programma?

```python
def function(x):
    if len(x) == 0:
        return
    function(x[:-1])
    print(x[-1])

function("Hanze")
```

## Opdracht 3

Gegeven de volgende regels aan code

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

Welke print statement moet er op regel 4 komen om de volgende output te generen?

```ipython
  xxxx
 xxxxxx
xxxxxxxx
```

## Opdracht 4

Wat is de output van onderstaande programma?

```python
def main():
    x = [1,7,3,8,9,5]
    function(x)
    print(x)

def function(x):
    if len(x) <= 1:
        return
    x[0] = function2(x[0], x[1])
    function(x[1:])

def function2(x, y):
    if x < y:
        return x
    return y

main()
```

# Reading code

Onderstaande opdrachten gaan over het lezen van recursieve functies. Als het programma werkt, wat is dan de output? Als de functie niet werkt, geef dan aan waarom het niet werkt. Gebruik **geen** interpreter!

## Opdracht 1

```python
def blaat(x):
    if len(x) == 0:
        return
    print(x[0])
    blaat(x[1:])

blaat("Hanze")
```

## Opdracht 2

```python
def blaat(x):
    if len(x) == 0:
        return
    print(x[0])
    return 1 + blaat(x[1:])

blaat("Hanze")
```

## Opdracht 3

```python
def blaat(x):
    if x == 0:
        return 0
    return 1 * blaat(x-1)

assert blaat(3) == 6
assert blaat(5) == 120
```

## Opdracht 4

```python
def main():
    numbers = [1,2,3,4,5,6,7,8,9,0]
    l = blaat(numbers)
    print(l)

def blaat(l):
    if len(l) == 0:
        return 0
    if l[0] % 2 == 0:
        return l[0] + blaat(l[1:])
    else:
        return blaat(l[1:])

main()
```

## Opdracht 5

```python
def main():
    numbers = [1,2,3,4,5,6,7,8,9,0]
    l = blaat(numbers)
    print(l)

def blaat(l):
    if len(l) == 0:
        return 0
    if l[0] % 2 == 0:
        return [l[0]] + blaat(l[1:])

    return blaat(l[1:])

main()
```

## Opdracht 6

```python
def main():
    r = blaat(8)
    print(r)

def blaat(l):
    if l == 0:
        return [0]
    return [l * 5] + blaat(l-1)

main()
```

## Opdracht 7

```python
from random import *

def main():
    guess(44)


def guess(hidden):
    """De computer raadt een geheim getal
    """
    comp_guess = choice(list(range(10)))

    if comp_guess == hidden:
        print("Gevonden!")
    else:
        guess(hidden)

main()
```

## Opdracht 8

```python
def main():
    print(blaat("test"))


def test():
    assert blaat("test") == False
    assert blaat("racecar") == True

def blaat(l):
    if len(l) == 0:
        return True
    if l[0] != l[-1]:
        return False
    else:
        blaat(l[1:len(l)])

main()
```

## Opdracht 9


```python
def main():
    print(blaat("test"))

def blaat(s):
    if len(s) <= 1:
        return s
    else:
        return s[0] * len(s) + blaat(s[1:])
main()
```

## Opdracht 10

```python
def main():
    numbers = [1,2,3,4,5,6,7,8,9,0]
    print(blaat(2, numbers))

def blaat(n, L):
    if len(L) == 0:
        return []
    elif L[0] % n == 0:
        return [L[0]] + blaat(n-1, L)
    else:
        return blaat(n-1, L)
main()
```

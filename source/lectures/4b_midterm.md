# Oefenmidterm

Twintig leesopdrachten om je voor te bereiden op de midterm. Bij elke opdracht lees je een programma en kies je wat eruit komt.

Maak ze eerst zelf. De antwoorden met uitleg staan bij de [uitwerkingen](/solutions/4_midterm).

## Opdracht 1

```python
max_points = 100
score = 30
grade = score / max_points * 9 + 1
score = 50
```

Welke waarde heeft `grade` aan het einde van dit programma?

- **a.** 50
- **b.** 2.7
- **c.** 5.5
- **d.** 3.6999999999999997

## Opdracht 2

```python
x = 4
if x > 2:
    x = x / 4
elif x < 2:
    x = x + 3
else:
    x = x * 3
```

Welke waarde heeft `x` aan het einde van dit programma?

- **a.** 4
- **b.** 12
- **c.** 1.0
- **d.** 7

## Opdracht 3

```python
x = 8
if x > 5:
    x = x - 4
if x <= 4:
    x = x + 3
elif x == 7 or x == 4:
    x = x * 2
```

Welke waarde heeft `x` aan het einde van dit programma?

- **a.** 14
- **b.** 7
- **c.** 4
- **d.** 8

## Opdracht 4

```python
x = "Emily"

if x < "E":
    print("groep 1")
elif x < "M":
    print("groep 2")
elif x < "Z":
    print("groep 3")
else:
    print("groep 4")
```

Wat drukt dit programma af?

- **a.** "groep 1"
- **b.** "groep 2"
- **c.** "groep 3"
- **d.** "groep 4"

## Opdracht 5

```python
woord = "Hanzehogeschool"
print(woord[-1])
```

Wat drukt dit programma af?

- **a.** "H"
- **b.** "a"
- **c.** "l"
- **d.** "o"

## Opdracht 6

```python
woord = "Hanzehogeschool"
print(woord[3:6])
```

Wat drukt dit programma af?

- **a.** "nze"
- **b.** "nzeh"
- **c.** "zeh"
- **d.** "zeho"

## Opdracht 7

```python
woord = "Hanzehogeschool"
print(woord[-1:1:-2])
```

Wat drukt dit programma af?

- **a.** "loceoen"
- **b.** "azhgsho"
- **c.** "Hneoecol"
- **d.** ""

## Opdracht 8

```python
print(function(5, 10))


def function(x, y):
    if x <= y:
        return x
```

Wat drukt dit programma af?

- **a.** 5
- **b.** 10
- **c.** `None`
- **d.** Het programma werkt niet

## Opdracht 9

```python
def function(x, y):
    if x > y:
        return x
    return y


print(function(5, 10))
```

Wat drukt dit programma af?

- **a.** 5
- **b.** 10
- **c.** `None`
- **d.** Het programma werkt niet

## Opdracht 10

```python
def main():
    temp = function(10, 5)
    print(temp)


def function(x, y):
    if x < y:
        return x


main()
```

Wat drukt dit programma af?

- **a.** 5
- **b.** 10
- **c.** `None`
- **d.** Het programma werkt niet

## Opdracht 11

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

Wat drukt dit programma af?

- **a.** 5
- **b.** 10
- **c.** 25
- **d.** 100
- **e.** `None`
- **f.** Het programma werkt niet

## Opdracht 12

```python
def main():
    temp = function1(5, 12)
    print(temp)


def function1(x, y):
    if x % 2 == 0:
        x = x / 2
    return x
    if x < y:
        return x
    return y


main()
```

Wat drukt dit programma af?

- **a.** 5
- **b.** 6
- **c.** 12
- **d.** `None`
- **e.** Het programma werkt niet

## Opdracht 13

```python
def function(y):
    while y >= 0:
        print("hoi")
        y = y - 1


function(4)
```

Hoe vaak drukt dit programma `hoi` af?

- **a.** 0
- **b.** 3
- **c.** 4
- **d.** 5
- **e.** Het programma werkt niet

## Opdracht 14

<!-- codecontrole:skip -->

```python
x = 8
while x < 100:
x = x * 2

print(x)
```

Wat drukt dit programma af?

- **a.** 8
- **b.** 64
- **c.** 100
- **d.** 128
- **e.** Het programma werkt niet

## Opdracht 15

```python
x = 5
n = 2
while x < 100:
    x = x * n
    n += 1
print(x)
```

Wat drukt dit programma af?

- **a.** 60
- **b.** 80
- **c.** 120
- **d.** 160
- **e.** Het programma werkt niet

## Opdracht 16

```python
x = 100
n = 1
for i in range(0, 5):
    x = x - n
    n = n * i + 1
print(x)
```

Wat drukt dit programma af?

- **a.** 96
- **b.** 91
- **c.** 75
- **d.** 10
- **e.** Het programma werkt niet

## Opdracht 17

```python
x = 100
while x > 10:
    if x % 2 == 0:
        x = x / 2
    else:
        x = x + 1
print(x)
```

Wat drukt dit programma af?

- **a.** 1
- **b.** 6
- **c.** 7.0
- **d.** 13
- **e.** Het programma werkt niet

## Opdracht 18

```python
lis = []
number = 48
for x in range(0, 48):
    if 48 % x == 0:
        lis = lis + [x]
print(lis)
```

Wat drukt dit programma af?

- **a.** `[1, 2, 3, 4, 6, 8, 12, 16, 24, 48]`
- **b.** `[0, 1, 2, 3, 4, 6, 8, 12, 16, 24]`
- **c.** `[1, 2, 4, 6, 8, 12, 16, 24, 48]`
- **d.** `[0, 1, 2, 4, 6, 8, 12, 16, 24]`
- **e.** Het programma werkt niet

## Opdracht 19

```python
my_list = [1, 2, 3, 4, 5, 6]
result = []
for ix in range(0, 6):
    if not my_list[ix] % 2 == 0:
        result = result + [my_list[ix] * 2]
    else:
        result = result + [my_list[ix]]
print(result)
```

Wat drukt dit programma af?

- **a.** `[2, 2, 6, 4, 10, 6]`
- **b.** `[0, 2, 4, 6, 8, 10]`
- **c.** `[2, 4, 6, 8, 10, 12]`
- **d.** `[1, 2, 3, 4, 5, 6]`
- **e.** Het programma werkt niet

## Opdracht 20

```python
lis = []
x = 1
while x < 5:
    if not x % 2 == 0:
        lis = lis + [2 * x]
        x = x * 3 + 1
    else:
        lis = lis + [x]
        x = x / 2
print(lis)
```

Wat drukt dit programma af?

- **a.** `[1, 4, 2, 1, 4]`
- **b.** `[1, 2, 3, 4, 5]`
- **c.** `[1, 4, 13]`
- **d.** `[2, 4, 2, 2, 4]`
- **e.** Het programma werkt niet

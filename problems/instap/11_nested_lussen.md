# Geneste lussen

Wat is de output van de onderstaande programma's?

## opgave 1
```python
name = "harry"
for x in range(3):
    for x in range(3):
        print(name)
```

## opgave 2
```python
lijst = [1, 2, 3]
for i in range(3):
    for j in lijst:
        print(j)

```

## opgave 3
```python
lol = [[1, 2, 3],[ 9, 8, 7]]
for i in lol:
    for j in i:
        print(j)
```

## opgave 4
```python
lol = [[1, 2, 3][9, 8, 7]]
for y in range(len(lol)):
    for x in range(len(lol[y]))
        print(lol[y][x])
```

## opgave 5
```python
lol = [[4, 5], [8, 9], [1, 2]]
k = 1
for i in range(2):
    k = k * 10
    for j in range(2):
        lol[i][j] *= k
print(lol)
```

## opgave 6
```python
for i in range(5):
    for j in range(i):
        print(i * j)
```

## opgave 7
```python
n = 5
for i in range(n):
    for j in range(i):
        print('*', end="")
    print('')
```

## opgave 8
```python
n = 5
for i in range(n):
    for j in range(i):
        print('*', end="")
    print('')
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end="")
    print('')
```


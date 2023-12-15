# List comprehension

Wat is de inhoud van lijst `L` met de onderstaande list comprehensions?

## opgave 1
```python
L = [x for x in range(10)]
```

## opgave 2
```python
L = [x for x in range(5,10)]
```

## opgave 3
```python
L = [x for x in range(10) if x != 5]
```

## opgave 4
```python
L = [x for x in range(10) if x % 3 == 0]
```

## opgave 5
```python
L = [x for x in range(10) if x % 3 == 0]
```

## opgave 6
```python
fruits = ["appel", "banaan", "kiwi", "citroen", "mango" ]
L = [x for x in fruits if "a" in x]
```

## opgave 7
```python
fruits = ["appel", "banaan", "kiwi", "citroen", "mango" ]
L = [fruits[x] for x in range(len(fruits)) if fruits[x] <= "c"]
```

## opgave 8
```python
fruits = ["appel", "banaan", "kiwi", "citroen", "mango" ]
L = [x for x in range(len(fruits)) if fruits[x] <= "c" and x % 2 == 0]
```

## opgave 9
```python
fruits = ["appel", "banaan", "kiwi", "citroen", "mango" ]
L = [x for x in fruits if len(x) > 5]
```

## opgave 10
```python
fruits = ["appel", "banaan", "kiwi", "citroen", "mango" ]
L = [len(x) for x in fruits]
```
# For lusjes

Wat is de output van onderstaande programma's?

## opgave 1
```python
for i in range(5):
    print(i)
```

## opgave 2
```python
L = [2, 4, 6, 8]
for x in L:
    print(x)
```

## opgave 3
```python
L = [9, 7, 5, 3, 1]
for i in range(len(L)):
    print(L[i])
```

## opgave 4
```python
L = [5, 3, 1]
result = 0
for i in range(len(L)):
    result = result + L[1]
print(result)
```

## opgave 5
```python
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
result = 0
for i in range(len(L)):
    if L[i] % 2 == 0:
        result += L[i]
print(result)
```

## opgave 6
```python
s = "Hanze"
result = 0
for _ in s:
    result += 1
print(result)
```

## opgave 7
```python
s = "Dit is een string"
result = ""
for x in s:
    if x in "eauoi":
        result += x
print(result)
```

## opgave 8
```python
s = "Dit is een string"
result = ""
for i in range(len(s)):
    if s[i- 1] == " ":
        result += s[i]
print(result)
```

## opgave 9
```python
lijst = []
for i in range(10):
    if i < 2:
        lijst += [1]
    else:
        lijst += [lijst[i-1] + lijst[i-2]]
print(lijst)
```

## opgave 10
```python
lijst = []
temp = 1
for i in range(5):
		if(temp % 2 != 0):
			lijst += [2 * temp]
			temp =  temp + 5
		else:
			lijst += [temp]
			temp = temp / 2
print(lijst)
print(temp)
```
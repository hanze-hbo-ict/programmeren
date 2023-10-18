# For lusjes

Wat is de output van onderstaande programma's?

## opgave 1
```python
n = 0
while n < 5:
    print(n)
    n += 1

```

## opgave 2
```python
l = [1,2,3,4,5]
while len(l) > 0:
    print(l)
    l = l[1:]
```

## opgave 3
```python
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
```

## opgave 4
```python
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
```

## opgave 5
```python
number = 4
faculty = 1
while number  > 0:
    faculty = faculty * number
    number -= 1
print(faculty)
```

## opgave 6
```python
num1 = 5
num2 = 8
while num2 > 0:
    num1 = num1 + num1
    num2 -= 1
print(num1)

```

## opgave 7
```python
s = "Dit is een test"
while s[0] != "e":
    s = s[1:]
print(s)
```

## opgave 8
```python
total = 0
number = int(input('Enter a number: '))

while number != 0:
    total += number
    number = int(input('Enter a number: '))

print('total =', total)
```

## opgave 9
```python
l = [1,2,3,4,5]
index = 0
while l[index] != 3 :
    index += 1
print(index)
```

## opgave 10
```python
lijst = []
temp = 1
while len(lijst) < 10:
		if(temp % 2 != 0):
			lijst += [2 * temp]
			temp =  temp + 5
		else:
			temp = temp / 2
print(lijst)
```
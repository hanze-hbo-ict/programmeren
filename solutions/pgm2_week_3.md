# PGM2 week 3

## Basis

### [Iteraties](/problems/instap/10_iteraties)

#### Opgave 1

Schrijf een functie die het aantal keer 42 in een lijst telt met een for-lus, een met een while-lus en een die list comprehension gebruikt.

```python
def count_42(L):
    total = 0

    for x in L:
        if x == 42:
            total += 1

    return total

def count_42(L):
    total = 0
    i = 0

    while i < len(L):
        if L[i] == 42:
            total += 1
        i += 1

    return total

def count_42(L):
    M = [1 for x in L if x == 42]

    total = sum(M)
    return total # Of return sum(M)

# assert count_42([0, 42, 1, 42, 3]) == 2
```

De variablen die in de lussen nodig zijn of geupdate worden, moeten aangemaakt worden voor de lus gestart wordt.
Als je dit verkeerd doet, kun je een infinite loop maken of wordt de variable niet goed aangepast/bijgehouden.


#### Opgave 2

Drie manieren om de getallen 1 tot en met 10 naar het scherm te printen.

```python
for x in range(1,11):
    print(x)

print()

counter = 1
while counter < 11:
    print(counter)
    counter +=1

print()

def NumbertoScreen(n=1):
    """ Print 1 tot en met n naar het scherm, recursief.
    """

    if n == 11:
        return
    else:
        print(n)
        return NumbertoScreen(n+1)

NumbertoScreen()
```

Zoals jullie kunnen zien, is de for-lus in dit geval de meest korte optie en vereisen de andere twee iets meer code. We hebben de twee lussen hier zo kort mogelijk gemaakt door de variable die de lus voorwaarde regelt ook gelijk de variable is die naar het scherm geprint wordt. Dit is niet altijd handig en dan kun je beter twee aparte variablen gebruiken.


#### Opgave 3

Schrijf een programma dat met een while-lus een voor een de even getallen tussen 20 en 40 print.

```python
# aparte nummer en counter
number = 20
counter = 40
while counter > 20:
    if number % 2 == 0:
        print(number)
    number +=1
    counter -= 1

# nummer en counter in een
number = 20
while number < 40:
    if number % 2 == 0:
        print(number)
    number +=1
```

Hier zijn twee mogelijke oplossingen. Ook hier zou je aan een enkele variable genoeg kunnen hebben.


#### Opgave 4

Maak een list comprehension die paarsgewijs elementen uit twee andere lijsten samenvoegt.

```python
L = ["Mi", "na", "i", "Marj"]
M = ["jn", "am", "s", "olein"]

K = [L[x] + M[x] for x in range(0,len(L))]
print(K)
```


#### Opgave 5

Maak met behulp van list comprehension een nieuwe lijst aan waar de lege waarden uit een andere lijst worden verwijderd.

```python
L = ["Tom", "", "Marie", "Isis", "", "Klaas"]
M = [x for x in L if x != '']
print(M)
```

Zo lang x niet gelijk is (!=) aan een lege string, geven we hem aan de nieuwe list.

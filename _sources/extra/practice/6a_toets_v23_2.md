---
version: 2023
lang: nl
papersize: a4
geometry: margin=2.5cm
toc: false
mainfont: Arial
---

# Proeftoets

## Opgave 1 (10pt)

Gegeven is een lijst `L` waar elk element een lijst is met studentnummer, het cijfer dat is behaald voor een tentamen en of het huiswerk wel of niet is gemaakt. Studenten die het huiswerk hebben gemaakt krijgen een 0.5 bonus op hun tentamencijfer.

Voorbeeld:

```python
L = [
    ["0308230", 7.6, True],
    ["8273927", 5.1, False],
    ["8234987", 6.4, False],
    ["2368612", 5.9, True],
    ["9731827", 3.2, False]
]
```
levert:

```python
HW = [
    [ "0308230", 8.1],
    ["2368612", 6.4]

]
```

### Opgave 1a (5pt)

Schrijf een list comprehension (*geen* functie of lus) die een lijst maakt van alle studenten die het huiswerk hebben gemaakt en het aangepaste cijfer voor het tentamen. Noem deze lijst `HW`.

### Opgave 1b (5pt)

Schrijf een lusconstructie (*geen* functie of list comprehension) die een lijst maakt van alle studenten die het huiswerk hebben gemaakt en het aangepaste cijfer voor het tentamen. Noem deze lijst `HW`.

## Opgave 2 (10pt)
Gegeven een lijst van getallen. We willen graag weten of de getallen bij elkaar opgeteld meer dan 100 zijn. Een student komt met de volgende oplossing:

```python
def over_hundred(L):
    result = 0
    for i in L:
        result += result + L[i]
        if result > 100:
            return True
        return False

lc = [x for x in range(12, 15)]
print(over_hundred(lc))

```
Helaas werkt de functie niet naar behoren. Pas de functie zo aan zodat het werkt. Vergeet de docstring niet en test de functie met drie assertions. 

## Opgave 3 (10pt)
Schrijf een while loop (geen functie) dat voor integers vraagt van de gebruiker. De while loop stopt zodra de gebruiker een negatief getal invoert. Uiteindelijk wordt er geprint hoeveel positieve getallen er zijn ingevoerd en ook de som van al deze positieve getallen wordt geprint. 

Vragen voor input: 
```python
inp = int(input("Geef positief getal: "))
```

Voorbeeld van het programma:
```python
Geef positief getal: 1
Geef positief getal: 3
Geef positief getal: 2
Geef positief getal: 5
Geef positief getal: 4
Geef positief getal: -1
Getallen gegeven: 5
Getallen opgeteld: 15
```

## Opgave 4 (15pt)
Schrijf de functie number_stairs(size) dat de integer size ontvangt en een ladder uitprint van nummers. Gebruik een lusconstructie. 

Voorbeeld: 
```python
number_stairs(5)
```
output:
```python
1
12
123
1234
12345
```
```python
number_stairs(3)
```
output: 
```python
1
12
123
```


## Opgave 5 (25pt)
De grootste gemene deler (ggd) tussen twee getallen is de grootste deler die beide getallen gemeenschappelijk hebben. Een deler kan gevonden worden met behulp van modulo: $$12\%4 = 0$$ 4 is dus een deler van 12 gezien er geen rest overblijft.  

ggd van 12 en 18 is 6.  
ggd van 24 en 36 is 12.  
ggd van 33 en 48 is 1.  

In deze opdracht gaan we een programma schrijven dat de ggd tussen twee getallen kan berekenen.

### Opgave 5a
Schrijf de functie `intersect(l1, l2)` met docstring. Deze functie krijgt twee lijsten binnen. Beide lijsten bevatten alleen unieke getallen. `intersect(l1, l2)` bepaald welke getallen in beide lijsten aanwezig zijn, plaats deze in een lijst en geeft het eindresultaat terug. Je mag geen gebruik maken van recursie. (10)

### Opgave 5b
Beschrijf hoe je een functie `ggd(g1, g2)` kan maken dat de ggd van twee getallen (g1 en g2) kan bepalen met behulp van list comprehensions en de functie `intersect(l1, l2)`. Licht de stappen toe die je nodig hebt om tot het goede resultaat te komen.  (5)

### Opgave 5c
Schijf de functie `ggd(g1, g2)` aan de hand van het plan dat je bij opgave 5b hebt ontworpen. Maak gebruik van list comprehensions en functie `intersect(l1, l2)`. Je mag in de functie `ggd(g1, g2)` geen gebruik maken van recursie of lusconstructie. Vergeet geen docstring toe te voegen en test de functie met drie assertions. (10)

Mocht het niet gelukt zijn bij 5a om de functie intersect(l1, l2) te schrijven mag je onderstaande functie gebruiken als vervanging.

```python
def intersect(l1, l2):
    if len(l1) == 0:
        return []
    elif l1[0] in l2:
        return [l1[0]] + intersect(l1[1:], l2)
    else:
        return intersect(l1[1:], l2)

```

## Opgave 6 (20pt)
Nim is een spel voor twee spelers. Er liggen 16 lucifers op tafel. Om de beurt pakt een speler 1, 2 of 3 lucifers. Degene die de laatste lucifer van tafel pakt heeft gewonnen. De speler is altijd als eerste aan de beurt en de AI is tweede. Zodra het de beurt is van de AI pakt hij net zoveel stokjes totdat er weer een meervoud van 4 op tafel ligt. Als er bijvoorbeeld 13 stokjes op tafel ligt dan zou de AI er 1 pakken zodat er 12 op tafel blijven liggen. Met deze strategie wint de AI altijd.

```python
import random

class Nim:
    def __init__(self, number_of_sticks):
        self.sticks = number_of_sticks

    # hier komt de functie player_takes() 

    def AI_turn(self):
          
    def game_over(self):
        
game = Nim(16)
while(True):
     print("stokjes op tafel: ", game.sticks)
     player_turn = int(input("hoeveel stokjes? "))
     if player_turn not in [1, 2, 3]:
          print("illigal move")
          continue
     game.player_takes(player_turn)
     if game.game_over():
          print("You win")
          break

     # computer beurt

```
### Opgave 6a
Schrijf de functie `player_takes` binnen de class Nim. Deze functie krijgt o.a. mee hoeveel stokjes een speler van tafel pakt en update de variable `sticks`. (5)

### opgave 6b
Maak de functie `AI_turn` af. Het geeft het aantal stokjes wat de AI wilt oppakken terug. De AI wil altijd een meervoud van vier maken, als dat niet mogelijk is kiest hij een willekeurige hoeveelheid stokjes. Gebruik `random.randint(1, 4)` om een random aantal stokjes te kiezen. (5)

### Opgave 6c
Maak de functie `game_over` af. Deze functie controleert of het spel voorbij is door te checken of er nog stokjes op tafel liggen. Als er geen stokjes liggen geeft het true terug en anders geeft het false terug. (5)

### opgave 6d
De while loop is niet helemaal compleet. De beurt van de PC mist. Maak de while loop af door de beurt van de computer toe te voegen onder de comment `#computer beurt`. (5)
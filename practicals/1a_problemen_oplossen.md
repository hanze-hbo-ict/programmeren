# Problemen oplossen

## Doel

Hoe los je een probleem op? Dat is het doel van dit werkcollege; werken aan probleemoplossend vermogen. Dit is een belangrijke vaardigheid in programmeren. Er is eerst een oplossing nodig, een idee, voordat dit geprogrammeerd kan worden.

Het probleem oplossen is de eerste stap van de 3 p's:

- **Probeer**: Probeer het probleem op te lossen op papier.
- **Plan**: Noteer de stappen die zijn gebruikt om het probleem op te lossen.
- **Programmeer**: Vertaal de stappen naar een programmeertaal.

## Strategieën

De strategie die gebruikt kan worden om een oplossing te vinden verschilt per probleem. De ene strategie past beter dan de ander, wat wel handig is om pen en papier te gebruiken. Hier zijn er een aantal:

-   *Teken het probleem op papier*. Dit werkt vooral als je met ruimtelijke vragen bezig bent.
-   *Maak het probleem kleiner*. Bijvoorbeeld wordt er gevraagd om een methode te verzinnen om getallen te sorteren. In plaats van het probleem op te lossen met 100 getallen, doe het eerst met twee getallen, daarna met drie, enz.
-   *Probeer alle opties uit*. Deze leent zich vooral als er niet teveel verschillende input is, zoals bij een logische schakeling.


### Opdracht: Nim

```{figure} images/1/NimGame.png
Lucifers opgesteld in rijen voor een spelletje Nim.
```

Nim is een spel voor twee spelers. Er liggen 16 lucifers op tafel. Om de beurt pakt een speler 1, 2 of 3 lucifers. Degene die de laatste lucifer van tafel pakt heeft gewonnen. Als de speler die als tweede begint de juiste strategie gebruikt kan hij/zij altijd winnen. De opdracht is om in tweetallen uit te vinden wat deze winnende strategie is. Bedenk ook samen welke oplosstrategie hier handig kan zijn.

### Opdracht+: SOS

Mocht je de oplossing van Nim gevonden hebben, dan kan je jezelf uitdagen met deze opdracht. SOS is ook een spel voor twee spelers. Het speelveld is een rij van 100 vakjes. Om de beurt zet een speler een letter 'S' of 'O' in een vakje. Het spel is voorbij zodra er 'SOS' gespeld is op het bord, de kleur van de letters maakt niet uit. Wie de laatste letter heeft neergezet wint. Ook hier geldt dat als de speler die als tweede begint de juiste strategie gebruikt hij/zij altijd kan winnen.

## Logica puzzles

Logische schakelingen werken met drie poorten: `and`, `or` en `not` en het resultaat is een 0 of een 1. Ook bij Boolaanse logica maak je ook gebruik van 3 operatoren genaamd `and`, `or` en `not` en zijn er maar twee resulaten mogelijk namelijk `True` of `False`. Dit wordt gebruikt binnen het programmeren om aan de computer uit te leggen welke instructies wel of niet uitgevoerd moeten worden. Het is dus handig om er mee te oefenen en dat gaan we doen aan de hand van zogenaamde *Truth and Lies* puzzles. Deze puzzels trainen ook nog eens het probleemoplossend vermogen.

Bekijk nog eens de volgende waarheidstabellen.

### `AND`

|       | input | output        |
|-------|-------|---------------|
| **x** | **y** | **AND(x, y)** |
|  `0`  |  `0`  |      `0`      |
|  `0`  |  `1`  |      `0`      |
|  `1`  |  `0`  |      `0`      |
|  `1`  |  `1`  |      `1`      |

De output van `AND` is 1 (`True`) als ALLE inputs gelijk aan zijn aan 1 (`True`).

### ``OR``

|       | input | output       |
|-------|-------|--------------|
| **x** | **y** | **OR(x, y)** |
|  `0`  |  `0`  |      `0`     |
|  `0`  |  `1`  |      `1`     |
|  `1`  |  `0`  |      `1`     |
|  `1`  |  `1`  |      `1`     |

De output van `OR` is 1 (`True`) als MINSTENS één input gelijk is aan 1 (`True`).

### `NOT`

| input | output     |
|-------|------------|
| **x** | **NOT(x)** |
|  `0`  |     `1`    |
|  `1`  |     `0`    |

De output van `NOT` is de omkering van de input.

### Opdracht 1

Alice, Bob en Chris komen van een eiland waar sommige mensen altijd de waarheid spreken en en de rest altijd liegt.

- Alice zegt: "Bob liegt of Alice spreekt de waarheid".
- Alice zegt: "Chris spreekt de waarheid".
- Bob zegt: "Chris spreekt de waarheid".

Wie spreken altijd de waarheid en wie liegen er altijd?


Dit soort raadsels lenen zich ervoor om verschillende inputs te gebruiken.

### Opdracht 2

Alice, Bob, Chris en Dave komen van een eiland waar sommige mensen altijd de waarheid spreken en en de rest altijd liegt.

- Bob zegt: "Alice liegt en Chris en Dave spreken de waarheid"
- Bob zegt: "Dave liegt of Chris spreekt de waarheid"
- Bob zegt: "Chris liegt en Alice spreekt de waarheid."


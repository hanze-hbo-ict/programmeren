# Strings

Tekstuele data en collecties

## Getallen

Zijn getallen voldoende om alles te kunnen representeren? Ja en nee!

We lopen nu vooruit op wat verder komen gaat, maar met getallen kunnen we heel veel representeren, in ieder geval in de computer! Maar voor ons is dit niet voldoende, bijvoorbeeld tekst of collecties (verzamelingen) van data.

## Sequenties

- lijsten met getallen
- *strings*, lijsten met karakters

Beide zijn *sequenties* in Python, verzamelingen van *opeenvolgende* elementen.

Verzamelingen van data zijn heel natuurlijk, denk bijvoorbeeld aan een reeksen van dagelijkse temperaturen (het werk van het [KNMI](https://knmi.nl/)) of verkoopcijfers van een winkel om bijvoorbeeld de maand- of jaaromzet te kunnen berekenen. De volgorde maakt in al deze gevallen uit: het heeft *betekenis*.

![character string](images/3/letter_beads.jpg)

Tekst (wat je nu leest) is een opeenvolging van karakters en het datatype om tekstuele data te representeren is een *string*. Vergelijk het met een draad waar je individuele karakters aan vast rijgt.

## `str`ings: tekstuele data

|                  | Voorbeeld                             |
|------------------|---------------------------------------|
| strings          | `s = 'hanze'`<br/> `c = 'hogeschool'` |
| type             | `type(s)`                             |
| lengte           | `len(s)`                              |
| optellen         | `s + c`                               |
| vermenigvuldigen | `2*s + 3*c`                           |


type('hanzehogeschool')

Je zult zien dat je bijzonder veel met strings kan doen, van bij elkaar optellen tot vermenigvuldigen!

Gegeven de volgende twee *strings*

```python
s1 = 'ha'
s2 = 'k'
```

- wat is `s1 + s2`?
- en wat is `2*s1 + s2 + 2*(s1 + s2)`

Syntax check! Tekst schrijf je tussen aanhalingstekens en Python begrijpt dat je hiermee een string bedoelt. Je mag zowel enkele als dubbele aanhalingstekens gebruiken, zolang je maar consequent bent, bijvoorbeeld `"hoi'` zal een syntaxfout geven!

Strings optellen ...

s1 = "ha"
s2 = "k"

print(s1 + s2)

Strings vermenigvuldigen ...

s1 = "ha"
s2 = "k"

print(2*s1 + s2 + 2*(s1 + s2))

## Lists

Verzamelingen van alle mogelijke data.

```python
M = [4, 7, 100, 42, 5, 47]
```

Net als bij strings (draden?) gebruiken we ook hier de Engelse term *lists* (en niet lijsten). Je ziet hier een lijst met 6 elementen die aan de variabele M wordt toegekend. Met de vierkante haken geef je Python aan dat je hier een list bedoelt, elementen in de lijst scheid je met komma's.

### Lengte

De lengte van een lijst

M = [4, 7, 100, 42, 5, 47]

len(M)

Een list is een sequentie en net als bij een string kan je de lengte (het aantal elementen) opvragen met `len(x)`. 

### Index

De elementen in de lijst zijn geïndexeerd, ze hebben een vaste positie.

|     |   0  |   1  |    2   |   3   |   4  |   5  |     |
|:---:|:----:|:----:|:------:|:-----:|:----:|:----:|:---:|
| `[` | `4`, | `7`, | `100`, | `42`, | `5`, | `47` | `]` |


In een sequentie staat elk element op een vaste positie en we beginnen altijd te tellen vanaf 0.

### Positie

Het element op index positie 0 opvragen

M = [4, 7, 100, 42, 5, 47]

M[0]

De syntax lijkt wat eigenaardig omdat je hier wéér vierkante haken moet gebruiken, deze keer achter de varabele naam om het karakter op deze positie op te vragen.

### Slicing

Een opeenvolgende selectie van elementen opvragen

M = [4, 7, 100, 42, 5, 47]

M[0:3]

Slicing, alsof je een puntje uit een taart snijdt! De eerste positie is de *start* index (0), de tweede de *stop* index (3). Stop is **tot** de index (en niet *tot en met*). Slicing geeft als resultaat altijd hetzelfde type terug (een list in dit geval). We zullen straks zien dat je ook strings kan slicen en dan zal het een substring teruggeven.

### Alle data

Een list kan alle datatypen bevatten

```python
L = [3.14, [2, 40], 'derde', 42]
```

Let hier even op, je ziet hier een een *lijst* als element op index positie 1 en een string op positie 2. Een lijst in een lijst, wat zal `len(x)` nu tellen?

L = [3.14, [2, 40], 'derde', 42]

len(L)

Alleen de elementen van de lijst zelf worden geteld!

## Strings en indexering

String indexering met `[]`


| 0     | 1     | 2     | 3     | 4     |
|-------|-------|-------|-------|-------|
| **h** | **a** | **n** | **z** | **e** |


Goed nieuws! Net als lists zijn strings geïndexeerd en ook hier begint tellen bij 0!

### Positie

Het karakter op index positie 0 opvragen

s = 'hanze'

s[0]

Exact detzelfde syntax en werking als bij lists!

### Negatieve indices

Negatieve indicess tellen van achteren naar voren!


| 0     | 1     | 2     | 3     | 4     |
|-------|-------|-------|-------|-------|
| **h** | **a** | **n** | **z** | **e** |
| -5    | -4    | -3    | -2    | -1    |


s = 'hanze'

s[-5]

Negatieve indices introduceren we nu voor strings, maar je kan misschien al raden dat dit op dezelfde manier ook bij lists werkt!

### Slicing

Een substring opvragen:

s = "hanzehogeschool"

s[0:5]

s = "hanzehogeschool"

s[5:]

Het is je misschien opgevallen dat je de "stop" positie leeg kan laten, Python neemt dan aan dat je tot en met het einde van de sequentie (de string in dit geval) bedoelt. Wat zou gebeuren als we de "start" positie ook leeg laten?

s = "hanzehogeschool"

s[:]

De substring is in dit geval de hele string! Python vult voor jou het begin en einde in op bais van de lengte van de string. Bedenk dat dit een *kopie* van de string is, denk hier terug aan geheugenadressen: de waarden zijn hetzelfde, maar de identiteit is anders. Probeer dit zelf en vergelijk `id(s)` met `id(s[:])`. 

### Stappen

Met hoeveel stappen door de sequentie lopen (*skip-slicing*)

```text
[start:stop:step]
```

Standaard is de stap 1, dat wil zeggen, neem steeds 1 stap voor het volgend element dat we in de selectie zouden willen hebben. 

s = 'hanzehogeschool'

s[::1]

Twee stappen per keer:

s = 'hanzehogeschool'

s[::2]

### Achteruit lopen

Stappen kunnen ook negatief zijn!

s = 'hanzehogeschool'

s[::-1]

Als je goed oplet zie je dat we met een negatieve stap de string hebben omgedraaid! Python gebruikers willen graag opscheppen met deze "truc" om een string om te draaien en misschien hebben ze wel gelijk!

#### Opgelet

Let op: bij een negatieve staprichting moet de start- en stopindex omgekeerd zijn!

s = 'hanzehogeschool'

s[14:8:-1]

Omdat de staprichting wijzigt, wijzigt ook op welke index moet worden begonnen en tot welke index moet worden gelopen.

## Quiz

### Vraag 1

```python
pi = [3, 1, 4, 1, 5, 9]

L = ['pi', "isn't", [4,2]]
```

1. Wat is `len(pi)?`
2. Wat is `len(L)`?
3. Wat is `len(L[1])`
4. Wat is `pi[2:4]`
5. Welk puntje ("slice") `pi` is gelijk aan `[3,1,4]`? (hint, neem het aantal elementen als stop waarde `[0,3]`)
6. Welk puntje `pi` is `[3,4,5]`?

#### Antwoord

1. 6
2. 3
3. 5
4. `[4, 1]`
5. `pi[:3]`
6. `pi[::2]`

### Vraag 2

```python
L = ['pi', "isn't", [4,2]]

M = 'You need parentheses for chemistry !'
#    0   4   8   12  16  20  24  28  32
```

1. Wat is `L[0]`?
2. Wat is `L[0][1]`
3. Wat is `L[0:1]`
4. Welk puntje M is `'try'`?
5. Welk puntje M is `'shoe'`?
6. Wat is `What is M[9:15]`?
7. Wat is `M[::5]`

#### Antwoord

1. `'pi'`
2. `'i'`
3. `['pi']`
4. `M[31:34]` of `M[-5:-2]`
5. `M[30:17:-4]`
6. `'parent'`
7. `Yeah cs!'`

### Vraag 3

```python
pi = [3, 1, 4, 1, 5, 9]
```

1. Wat is `pi[0] * (pi[1] + pi[2])`?
2. Wat is `pi[0] * (pi[1:2] + pi[2:3])`?

#### Antwoord

1. In stappen:
    1. `3 * (1 + 4)`
    2. 15
2. In stappen:
    1. `3 * ([1] + [4])`
    2. `3 * [1, 4]`
    3. `[1, 4, 1, 4, 1, 4]`
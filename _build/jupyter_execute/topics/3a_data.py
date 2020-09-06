# Data

Data en handelingen op data

## Informatica

een taal leren $\sim$ **syntax** (noodzakelijk, maar niet het punt)

... informatica studeren $\sim$ **semantiek** (leren hoe machines denken!)


Een programmeertaal als Python leren heeft alles te maken met syntax waarmee je handelingen kan schrijven die een machine moet uitvoeren. Maar hiervoor heb je eerst andere kennis nodig, kennis die alles te maken heeft met wat de machine (bijvoorbeeld, jouw laptop) doet.

![Achter de schermen](images/3/rob-laughter-WW1jsInXgwM-unsplash.jpg)

We gaan stap voor stap ontdekken wat er zich in de machine afspeelt en gaan we kijken naar data en handelingen op (of de verwerking van) data.

## Handelingen en data

x = 41
y = x + 1

Laten we om te beginnen de volgende twee variabelen `x` en `y` ieder een waarde toekennen. Deze waarden (`41` en `42`) worden in het geheugen opgeslagen.

## Achter het doek

![box_metafoor](images/3/box.png)

Stel je een variabele voor als een doos: de inhoud van de doos is de waarde (bijvoorbeeld `41` of `42` in ons geval) met extra informatie over het *type* van de waarde (een `int` wat staat voor *integer*, een geheel getal) en een geheugenlocatie (LOC).

### Geheugen

![box_locatie](images/3/box_2.png)

Geheugen is een hele lange lijst van dit soort dozen, elk met een naam, waarde, type en geheugenlocatie.

![RAM 8Gb](images/3/1136px-Samsung-1GB-DDR2-Laptop-RAM.jpg)

Random Access Memory ([RAM](https://nl.wikipedia.org/wiki/Dynamic_random-access_memory)) is waar variabelen worden opgeslagen, een kaart zoals je deze hier ziet zit ook in jouw laptop! Als je het zwarte materiaal voorzichtig zou weghalen dan zal een (microscopisch klein) raster zichtbaar worden.

![RAM Grid](images/3/ramgrid.png)

Horizontaal zie je de *bitlijnen*, of adresregels (de geheugenlokatie) en verticaal de *woordlijnen* (of dataregels). Elk kruispunt is een [condensator](https://nl.wikipedia.org/wiki/Condensator) die elektrisch geladen of ongeladen kan zijn.

### Bits

![RAM Grid Bit](images/3/ramgrid_bit.png)

Zo'n punt dat geladen (1 of `True`) of ongeladen (0 of `False`) kan zijn wordt een *bit* genoemd. Dit is de kleinst mogelijk informatie-eenheid!

### Bytes

![RAM Grid Byte](images/3/ramgrid_byte.png)

Een *byte* is een verzameling van 8 aaneengesloten bits op een adresregel.

### Woord?

![Windows 64bit](images/3/windows_64bit.png)

*Woord* in woordregel is niet een woord als in een zin (taal) maar een term die staat voor de [natuurlijke eenheid](https://en.wikipedia.org/wiki/Word_(computer_architecture)) van informatie voor een bepaalde computerarchitectuur. Tegenwoordig is deze voor de meeste systemen 64-bit, dit wordt ook wel de *adresruimte* van een architectuur genoemd.

Deze eenheid is van belang want het bepaalt bijvoorbeeld het grootste gehele getal dat kan worden opgeslagen. Maar hoe komen we van bits naar bytes en vervolgens tot getallen en andere data zul je je afvragen? Maak je geen zorgen, daar komen we later uitgebreid op terug, eerst gaan we kijken naar datatypes!

## Datatypes

*Alle* talen hebben datatypes!

| Type    | Voorbeeld         | Wat is het?                                                                      |
|---------|-------------------|----------------------------------------------------------------------------------|
| `float` | `3.14` of `3.0`   | decimale getallen                                                                |
| `int`   | `42` of `10**100` | gehele getallen                                                                  |
| `bool`  | `True` of `False` | het resultaat van een test of vergelijking met: `==`, `!=`, `<`, `>`, `<=`, `>=` |


type(42.0)

Dit zijn de eerste datatypes waar we kennis mee gaan maken en ze komen aardig overeen met wat wij (mensen!) kunnen onderscheiden, bijvoorbeeld gehele- of decimale getallen. 

Ook een `bool`(ean) is uiteindelijk een getal: als we `False` typen zal Python dit lezen als 0. `True` en `False`is *syntax* (!) om het voor ons makkelijker te maken, maar *semantisch* staat het voor 1 en 0 (in ieder geval voor Python!).

Met de de *functie* `type(x)` kan je opvragen welk type Python denkt dat de waarde heeft.

## Operatoren

Speciale tekens die alles te maken hebben met handelingen op data.

### Python operatoren

| Betekenis                         |                                 |
|-----------------------------------|---------------------------------|
| groepering                        | `(` `)`                         |
| machtsverheffing                  | `**`                            |
| vermenigvuldiging, modulo, deling | `*` `%` `/` `//`                |
| optelling, aftrekking             | `+` `-`                         |
| vergelijking                      | `==` `!=`, `<`, `>`, `<=`, `>=` |
| toekenning                        | `=`                             |


Net als bij rekenen moet je hier rekening houden met de bewerkingsvolgorde, hier zijn ze van meest naar minst belangrijk weergegeven. Het is *niet* nodig deze volgorde te onthouden, onze tip is waarden te groepereren in plaats van je zorgen te maken over de bewerkingsvolgorde.

Bij twee operatoren moeten we even stilstaan omdat niet direct duidelijk is wat ze doen, de modulo operator `%` en de *integer* deling `//` (in tegenstelling tot de gewone deling `/`).

### Modulo operator `%`

- `7 % 3`
- `9 % 3`

`x % y` is het **restant** wanneer `x` door `y` wordt gedeeld

11 % 3

Syntax check! Het maakt niet uit of je `x%2` of `x % 2` schrijft (met spaties), Python weet wat je bedoelt :)

#### Voorbeelden

|   | Test          | Mogelijke waarden van `x` |                                              |
|---|---------------|---------------------------|----------------------------------------------|
| A | `x % 2 == 0`  |                           |                                              |
| B | `x % 2 == 1`  |                           |                                              |
| C | `x % 4 == 0`  |                           | Wat gebeurt hier als `x` een jaartal is?     |
| D | `x % 24 == 0` |                           | Wat gebeurt hier als `x` een aantal uren is? |


3 % 2 == 0

A en B hebben alles te maken met even en oneven getallen, voorbeeld C met schrikkeljaren en voorbeeld D misschien met het digitaal display van jouw wekker?

### Integer deling

- `7 // 3`
- `9 // 3`
- `9 // 3`

`x // y` is als `x / y` maar dan **afgerond** tot een geheel getal

30 // 7

De `//` operator rondt af naar beneden, maar dan ook volledig naar beneden! In het Engels staat de  `//` operator naast "integer division" ook bekend als "floor division": floor als in vloer (het laagste) in tegenstelling tot ceiling (plafond, hoogste). Maar er is meer aan de hand, want je zult zien dat `//` veel lijkt op de `%` operator!

De verdeling van 30 in veelheden van 7:

```python
30 == (4) * 7 + (2)
```

Zouden we dit kunnen generaliseren tot een algemene regel met behulp van de operatoren `//` en `%` die we nu hebben leren kennen?

De verdeling van `x` in veelheden van `y`:

```python
x == (x // y) * y + (x % y)
```

En daar is de `%` operator weer :) Je zult later zien dat het gebruik van `%` en `//` bijzonder handig zal zijn als we gaan rekenen met ... bits!

Kort samengevat: de `//` operator rondt volledig naar beneden af (door alles achter de komma weg te laten).

### Wat is gelijk?

| Een waarde TOEKENNEN | IS NIET gelijk aan | een waarde TESTEN |
|----------------------|--------------------|-------------------|
| `=`                  | `!=`               | `==`              |


De enkele `=` ken je van wiskunde waar je $a = 1$ zal uitspreken als "a is gelijk aan 1". Bij programmeertalen is dit anders en wordt "ken aan a de waarde 1 toe" bedoeld. Om te testen of de waarde gelijk is aan een andere waarde wordt `==` gebruikt (en `!=` voor is *niet* gelijk aan).

### Identiteit

Is `==` een test op *waarde* of *identiteit* (geheugenlokatie)?

Sommige talen hebben `===`!

Er is een verschil tussen testen op *waarde* en testen op *identiteit* (of het hetzelfde "doos" is, de geheugenlokatie). Python heeft geen `===` (zoals Javascript, een programeertal gebruikt in browsers) maar heeft speciaal voor dit geval `is`, bijvoorbeeld `a is b` om te vergelijken op basis van identiteit.

Vergelijken op waarde of identiteit met `==` kan erg verschillen per taal. Voor Java (een veel gebruikte programmeertaal) betekent `==` een test op *identiteit*. Python heeft gekozen om `==` een test op gelijkheid van *waarde* te laten zijn. Dit ligt misschien het dichtst bij hoe mensen denken, zeker als het gaat om vergelijken van bijvoorbeeld getallen of tekst.

Een voorbeeld om het verschil duidelijk te maken:

a = 3141592
b = 3141592

a == b

a is b

print(id(a))
print(id(b))

`id(x)` geeft de adreslokatie van een waarde terug. Je kan zien dat `a` en `b` anders zijn, hoewel ze tóch dezelfe waarde hebben!

## Quiz

Voer de volgende regels uit:

```python
x = 41
y = x + 1
z = x + y
```

Welke waarden hebben `x`, `y` en `z`?

x = 41
y = x + 1
z = x + y

print(x, y, z)

Voer vervolgens de volgende regel uit:

```python
x = x + y
```

Welke waarden hebben `x`, `y` en `z` nu?

x = x + y

print(x, y, z)

### Achter de schermen

```python
x = 41
y = x + 1
z = x + y
```

In het geheugen:

![box_voor_x](images/3/box_3a.png)

De drie variabelen `x`, `y` en `z` zijn nu in het geheugen bewaard op drie verschillende lokaties.

Laatste stap:

```python
x = x + y
```

In het geheugen:

![box_na_x](images/3/box_3b.png)

Met de laatste stap wijzigen we de waarde van `x` en dit betekent dat de oorspronkelijke lokatie wordt gewist en de nieuwe waarde in het geheugen wordt gezet, op een nieuwe lokatie!

Je kan de identiteit (de geheugenlokatie) in Python opvragen met `id(x)`. Probeer dit eens met `x` voor en na de laatste operatie en je zal zien dat ze verschillend zijn. Het wissen of verwijderen van een waarde kan je doen met `del x` (dus zonder de haakjes `()`).

### Extra

```python
a = 11 // 2
b = a % 3
c = b ** a+b * a
```

Welke waarden hebben `a`, `b` en `c`?

a = 11 // 2
b = a % 3
c = b ** a+b * a

print(a, b, c)

## Cultuur

![42](images/3/wikipedia_42.png)

Het boek [The Hitchhiker's Guide to the Galaxy](https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy) van [Douglas Adams](https://en.wikipedia.org/wiki/Douglas_Adams) heeft sporen nagelaten in onder andere informatica: de kans is groot dat je in voorbeelden of uitwerkingen het getal 42 tegenkomt. Maar ook in het gewone leven als je op [25 mei](https://en.wikipedia.org/wiki/Towel_Day) mensen met een handdoek ziet lopen ...
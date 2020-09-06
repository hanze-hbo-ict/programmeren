# Condities

![Keuzes maken](images/1/AB-Vzw.png)

Een van de eerste concepten die we nodig hebben bij het programmeren is het **conditioneel statement**, dat ons in staat stelt om onze computer te vertellen dat hij een set instructies moet volgen als aan een bepaalde voorwaarde is voldaan. Elke keer dat we controleren of aan een voorwaarde wordt voldaan wordt dit een **test** genoemd. Deze tests slagen als aan de voorwaarde wordt voldaan (waar, of `True` zijn), en falen als de uitkomst van de test `False` is.

Een keus maken in Python kan heel eenvoudig zijn...

```python
if [conditie]:
    [doe iets]
```

## Drie mogelijkheden

- `if`
- `elif`
- `else`

Er zijn drie manieren om een conditionele statement te schrijven. `if` is verplicht en kan gecombineerd worden met `elif` en/of `else`. We lopen ze kort even langs.

### `if`

```python
if cijfer > 5.5:
    print("Voldoende")
```

Als aan de conditie is voldaan dan worden de instructies uitgevoerd die ingesprongen onder `if` staan. `if` is natuurlijk Engels voor "als", en zo zal je meer termen in het Engels gaan tegenkomen. En let op, het gebruik van `if` is verplicht, een `elif` of `else` zonder `if` is niet geldig!

### `elif`

```python
if cijfer > 7.5:
    print("Goed")
elif cijfer > 5.5:
    print("Voldoende")
```

`elif` is een afkorting van "else if", of "anders als". Dit geeft aan dat in het geval de test boven deze faalt (de `if`, in dit geval), een nieuwe conditie zal moeten worden gecontroleerd op dezelfde manier als het `if` statement. Als aan de voorwaarde erboven (`if`) al is voldaan, dan zal de `elif` niet worden uitgevoerd.

### `else`

```python
if cijfer > 7.5:
    print("Goed")
elif cijfer > 5.5:
    print("Voldoende")
else:
    print("Onvoldoende")
```

`else` is de laatste optie: als alle voorgaande tests mislukken, voer dan de volgende instructie(s) uit.

Let op: Python is zeer gevoelig voor de manier waarop je jouw code schrijft, zowel de *syntaxis* (hoe je de woorden van de taal samenvoegt tot samenhangende instructies) als de inspringing (hoe ver de tekst van de linkerkant van het scherm af staat) zijn belangrijk.

Voor conditionele statements moet je ervoor zorgen dat de instructies die bij elke test horen, daar direct onder staan en vier spaties onder het `if`, `elif` of `anders` statement ingesprongen staan.

We zullen het nu hebben over waarom je misschien conditionele statements wilt gebruiken, en je zult zien hoe je ze schrijft. Vervolgens nemen we enkele voorbeelden door en leggen we uit waarom ze werken. Na deze lezing zal je voorbereid zijn om het steen, papier en schaar lezing te volgen en aan het huiswerk te beginnen.

## Waar of niet waar

`True` of `False`

Een conditioneel statement maakt het mogelijk dat onze code verschillende dingen kan doen, afhankelijk van de vraag of een conditie waar of niet waar was.

Dit is waarschijnlijk de meest nuttige uitdrukking die we kunnen schrijven. Als we geen condities hadden dan zou onze code elke keer weer hetzelfde doen. Dat zou een niet heel erg nuttig programma zijn.

Stel je voor dat jouw e-mailprovider je altijd laat inloggen, ongeacht het wachtwoord dat je gebruikt? Conditionele statements stellen ons programma in staat om het juiste antwoord te geven, zelfs als de invoer verandert.

In dit geval is het conditionele statement: is het ingevoerde wachtwoord gelijk aan het eerder bewaarde wachtwoord van een gebruiker? 

temp = 22.0

if temp > 35.0:
    print("Heet!")

Conditionele statements stellen ons programma in staat om het juiste antwoord te geven, zelfs als de invoer verandert.

Stel je bijvoorbeeld voor dat we proberen te bepalen of het buiten heet is. Als het warmer is dan 35 graden Celsius, zullen we zeggen dat het heet is.

Een `if`-statement is de juiste keuze voor deze code omdat we alleen willen zeggen dat het heet is als de temperatuur hoger is dan 35 graden Celsius. Op dit moment hebben we de temperatuur gedefinieerd op 22. We weten dat 22 niet groter is dan 35, dus deze test zal mislukken. Wanneer een test faalt, dan zal zijn *body* niet worden uitgevoerd.

Dus deze code zal *niets* afdrukken. Onthoud, dat is wat we willen!

Merk op dat de body altijd één niveau dieper ingesprongen is dan de test en dat er een dubbele punt is geschreven na de test.

temp = 36.0

if temp > 35.0:
    print("Heet!")

Als we de temperatuur veranderen naar 36 en dan de code uitvoeren, dan wordt er 'Heet!' geprint.

Wat als we ook andere temperaturen willen classificeren? Om dit te doen, moeten we twee nieuwe conditionele statements introduceren, `elif` en `else`. Laten we beginnen met `elif`.

temp = 36.0

if temp > 35.0:
    print("Heet!")
elif temp > 20.0:
    print("Warm")

`elif` is een combinatie van de woorden "else" en "if". Het betekent dat als de vorige test is mislukt, doe dan deze test. Om te zien hoe het werkt, laten we een voorbeeld proberen.

Hier is de temperatuur nog steeds 36. Net als eerder, de eerste `if` slaagt, dus de body wordt uitgevoerd en het programma drukt 'Heet!' af.

Wordt het *tweede* blok uitgevoerd? Bedenk, `elif` betekent als de eerste test mislukt, voer deze test uit. Sinds de eerste test is geslaagd, voeren we de `elif` niet meer uit, en er wordt niets meer geprint.

temp = 23.0

if temp > 35.0:
    print("Heet!")
elif temp > 20.0:
    print("Warm")

Wat gebeurt er als we de temperatuur op 23 zetten? Dan faalt de eerste test, zodat de body niet wordt uitgevoerd.

Sinds de eerste test faalde, doen we vervolgens de `elif` test. We zien dat deze test slaagt, dus deze body wordt uitgevoerd en het programma drukt 'Warm' af.

temp = 23.0

if temp > 35.0:
    print("Heet!")
elif temp > 20.0:
    print("Warm")
elif temp > 10.0:
    print("Koel")
else:
    print("Brrr!")

Laten we dit programma nu voltooien met een volledig temperatuurbereik. We hebben een classificatie van 'Koel' toegevoegd voor temperaturen tussen 10 graden en 20 graden. We hebben ook een nieuwe conditie toegevoegd, het `else`-statement. Het `else`-statement betekent dat als geen van de `if`'s of `elif`'s geslaagd is, de code in het `else`-statement wordt uitgevoerd.

Hier betekent dat als de temperatuur niet hoger was dan 35, 20 of 10, we 'Brrr!' afdrukken. 
Bijvoorbeeld, de temperatuur is nu 23. Dus wat drukt onze code af? De eerste test faalt, maar we slagen voor de tweede test. Dat betekent dat de body van de tweede test wordt uitgevoerd, maar geen van de andere `elif`'s  of het `else`-statement.

Onze code drukt 'Warm' af, dat is wat we wilden.

temp = 0.0

if temp > 35.0:
    print("Heet!")
elif temp > 20.0:
    print("Warm")
elif temp > 10.0:
    print("Koel")
else:
    print("Brrr!")

Wat gebeurt er als de temperatuur 0 is? Dan slagen we niet voor alle `if`- en `elif`-statements, dus geen van de bodies zal worden uitgevoerd. Aangezien alle tests mislukt zijn, wordt het `else`-statement uitgevoerd. Het heeft geen test en in plaats daarvan drukt het 'Brrr' af.

## Mogelijke fouten

- volgorde
- uitsluiting

We laten nu een paar dingen zien die fout kunnen gaan bij het schrijven van het temperatuurprogramma.

### Volgorde

temp = -10.0

if temp > 0.0:
    print("Brrr!")
elif temp > 10.0:
    print("Koel")
elif temp > 20.0:
    print("Warm")
else:
    print("Heet!")

De code die je hier ziet is een soortgelijk programma dat we eerder hebben geschreven. Maar wat gebeurt er als je de temperatuur op negatief 10 zet? Het eerder geschreven programma zal 'Brrr!' afdrukken. Echter, het programma dat je hier ziet zal 'Heet!' afdrukken!

Merk op dat het niet werkt voor negatieve getallen. Maar ook een temperatuur van bijvoorbeeld 15 zal niet het gewenste resultaat geven, en zal 'Brrr!' afdrukken ...

### Uitsluiting

temp = 40.0

if temp > 35.0:
    print("Heet!")

if temp > 20.0:
    print("Warm")

if temp > 10.0:
    print("Koel")

Laten we eens kijken naar een andere manier om dit programma te schrijven die misschien ook niet werkt zoals we zouden willen.

In plaats van een heleboel `elif`-statements te schrijven, hadden we drie `if`-statements kunnen schrijven. Maar wat gebeurt er als de temperatuur 40 graden is?

In dit geval zullen alle drie de tests slagen en drie verschillende statements over de temperatuur afdrukken. Dat gebeurt omdat de `if`-statements elkaar niet uitsluiten. Als één slaagt, dan wordt de rest nog steeds getest.

Dat was veel informatie, dus laten we de belangrijke concepten even kort samenvatten.

## Conditionele statements

- één of meerdere blokken
- alleen de geslaagde test wordt uitgevoerd

### Blokken

```python
if temp > 35.0:
    print("Heet!")
elif temp > 20.0:
    print("Warm")
elif temp > 10.0:
    print("Koel")
else:
    print("Brrr!")
```

Een `if`-statement laat een programma verschillende code uitvoeren, afhankelijk van het feit of een test slaagt of niet. Het typische `if`-statement heeft één of meer blokken, en elke `if` of `elif` heeft een test. Hier tel je 4 blokken (één `if`, twee `elif`'s en een `else`)

### Handelen

```python
temp = -10.0

if temp > 35.0:
    print("Heet!")
elif temp > 20.0:
    print("Warm")
elif temp > 10.0:
    print("Koel")
else:
    print("Brrr!")
```

Tests worden achtereenvolgens uitgevoerd totdat één slaagt. De code die bij deze test hoort wordt uitgevoerd, en er worden verder *geen* andere tests meer uitgevoerd.

Als geen enkele test slaagt, dan wordt de optionele `else` uitgevoerd.

Vergeet niet dat `if` tests altijd worden uitgevoerd, terwijl `elif` en `else` tests alleen worden uitgevoerd als de vorige tests zijn mislukt.

## Geneste blokken

![Matroesjka](images/1/matroesjka.png)

Blokken kunnen worden genest en we gaan een klein experiment doen om dit te laten zien: is `elif` echt nodig?

### Is `elif` nodig?

temp = -10.0

if temp > 35.0:
    print("Heet!")
elif temp > 20.0:
    print("Warm")
elif temp > 10.0:
    print("Koel")
else:
    print("Brrr!")

Dit is het voorbeeld dat we al eerder hebben gezien. Wat nu als `elif` niet zou bestaan, kunnen we dit ook met alleen `if` en `else` schrijven? Laten we beginnen met de eerste conditie!

temp = -10.0

if temp > 35.0:
    print("Heet!")
else:
    if temp > 20.0:
        print("Warm")
    elif temp > 10.0:
        print("Koel")
    else:
        print("Brrr!")

Als de eerste conditie (`temp > 35.0`) faalt, doe dan het volgende (`else`). Dit principe gaan we herhalen voor de volgende condities, tot er geen `elif` meer over is. En hier zie je ook een eerste genest blok!

temp = 15.0

if temp > 35.0:
    print("Heet!")
else:
    if temp > 20.0:
        print("Warm")
    else:
        if temp > 10.0:
            print("Koel")
        else:
            print("Brrr!")

Het blijkt dat we heel goed zonder `elif` kunnen! En je ziet ook dat we langzaam de diepte ingaan, een vorm die je misschien herkent als een beslissingsboom.

![Beslisboom](images/1/decision_tree.png)

Waarom tóch `elif` gebruiken? `elif` is een syntactisch hulpmiddel dat het voor ons gemakkelijker maakt: met heel veel keuzes zou onze code door alle inspringen van de pagina gaan lopen!

## Steen, papier en schaar

![RPS](images/1/RPS-3_NL.png)

Een voorbeeld waar geneste conditionele statements kunnen worden gebruikt is bij het steen, papier en schaar spel (RPS, of *rock, paper and scissors*).

```python
comp = "steen"
user = "papier"

if comp == "papier" and user == "papier":
    print("Gelijkspel. Nog een keer?")
elif comp == "steen":
    if user == "schaar":
        print("Ik win! *_*")
    else:
        print("Jij wint. Aargh!")
```

We gaan dit spel tegen de computer spelen, waar de variabele `user` jouw keus is en de variabele `comp` de keus van de computer. De vraag is nu of dit programma correct is...

1. zal dit programma de juiste uitkomst printen?
2. zal het **altijd** de juiste uitkomst printen, ook als `user` en `comp` andere waarden krijgen?

Let op, je ziet hier een voorbeeld hoe je meerdere condities kan combineren door middel van `and`: de test slaagt alleen als zowel de eerste (`comp == "papier"`) als de tweede test (`user == "papier"`) correct is!

## Quiz

### Vraag 1

```python
comp = "steen"
user = "steen"

if comp == "steen":
    if user == "papier":
        print("Ik win *_*!")
    elif user == "schaar":
        print("Jij wint.")
else:
    print("Gelijkspel.")
```

- wat zal dit programma printen?
- wat zal dit programma printen als het `else` blok inspringt zodat het onderdeel wordt van de geneste `if`-`elif`?

### Vraag 2

```python
comp = "steen"
user = "steen"

if comp == "steen":
    print("Ik win *_*!")

if user == "papier":
    print("Jij wint.")
else:
    print("Gelijkspel.")
```

- zoals dit programma nu is geschreven, wat zal het printen?
- welke waarden moeten `comp` en `user` hebben om een juist antwoord te printen?
- hoeveel van de mogelijke 9 combinaties wordt door dit programma correct afgehandeld?


|            | **steen** | **papier** | **schaar** |
|------------|-----------|------------|------------|
| **steen**  |           |            |            |
| **papier** |           |            |            |
| **schaar** |           |            |            |

Tip, gebruik een waarheidstabel om de combinaties te noteren die dit programma correct afhandelt waar de kolommen voor de keus van de computer staan en de rijen voor de keus van de gebruiker.

Je zult merken dat voor het oplossen van het steen, papier en schaar spel (en zeker als je een variant met meer dan drie opties uitwerkt!) je een `if` ... `elif` ... `else` combinatie nodig hebt. Je zal jezelf ook kunnen gaan afvragen wat de meest *efficënte* oplossing is. Zou de oplossing nog steeds even efficiënt zijn bij een spel met 15 of 25 varianten of zal je daar andere oplossingen moeten vinden?

### Vraag 3

Gegeven de volgende twee programma's

**Programma A**

```python
perc = 0.70

if perc > 0.90:
    print("Uitmuntend")
elif perc > 0.70:
    print("Goed")
elif perc > 0.60:
    print("Voldoende")
else:
    print("Aargh!")
```

**Programma B**

```python
perc = 0.70

if perc > 0.00:
    print("Aargh!")
elif perc > 0.60:
    print("Voldoende")
elif perc > 0.75:
    print("Goed")
else:
    print("Uitmuntend")
```

Wat zal programma **A** printen?

- Uitmuntend
- Goed
- Voldoende
- Aargh!

Wat zal programma **B** printen?

- Uitmuntend
- Goed
- Voldoende
- Aargh!

Wat is een mogelijke waarde van `perc` zodat programma **A** "Goed" zal printen?
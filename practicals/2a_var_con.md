# Maximum

Het probleem: Gegeven twee getallen, welke van de twee getallen is de grootste?

De 3 p's:

- **Probeer**: Probeer het probleem op te lossen op papier.
- **Plan**: Noteer de stappen die zijn gebruikt om het probleem op te lossen.
- **Programmeer**: Vertaal de stappen naar een programmeer taal.

**Stap 1: probeer**:
In dit voorbeeld is de probeer fase niet erg indrukwekkend. Gegeven twee getallen kunnen wij als mens al heel snel zien welke van de twee groter is.

**Stap 2: Plan**:
1. Neem twee getallen a en b
2. als a > b dan is a de grooste anders is b het grootste getal.

**Stap 3: Programmeer**:
Nu het plan omzetten in code. Deze cursus gebruikt hiervoor python. De leerdoelen van deze werkcollege zijn:
* Input en output
* Variabelen
* If-then-else

Dit is de kennis dat nodig is om het gemaakte plan om te zetten tot programmeer code.

## Input en output

De computer moet worden verteld welke twee getallen we met elkaar willen vergelijken. Dit kan gedaan worden met behulp van een Input functie. Een functie en is een opdracht dat een computer kan uitvoeren.

```python
input()
```

De functie heeft als naam 'input'. Door het gebruik van haakjes weet de computer dat het hier gaat om een functie en dat er dus een opdracht uitgevoerd moet worden. In dit geval weet de computer dat er gevraagd moet worden voor input. Om te vertellen aan de gebruiker van het programma wat voor input er verwacht wordt kunnen we een string toevoegen aan de functie. Een string wordt aangegven met dubbele quotes, zo weet de computer dat het om een zin/woord gaat.

```python
input("Geef getal a")
input("Geef getal b")
```

De functie krijgt nu als parameter een string mee. De computer geeft deze zin als output voordat hij vraagt om input. Zo kan een gebruiker lezen welke input er gevraagd wordt. Om de computer enkel ouput te laten zien wordt de print functie gebruikt.

```python
print("Hello world")
```

De computer print nu hello world als dit programma wordt gedraaid. "Hello world" worden vaak gebruikt als eerste kennis making met code. Voor python is deze ene zin genoeg. Er is een hele wikipage met 'hello world' programma's in allerlei verschillende programmeer talen. https://en.wikipedia.org/wiki/%22Hello,_World!%22_program

## Variabelen

De computer wordt nu verteld om om input te vragen, maar is nog niet verteld wat er met deze input moet gebeuren. Data kan bewaard worden in een variabele. Zie een variabele als een doos met daarop een naam, een adres en een type. In de doos wordt de data bewaard.
* De naam bepalen we zelf als programmeur. Advies is om herkanbare namen te gebruiken voor variabelen. Dit maakt code leesbaarder. Werken met namen is voor ons als mensen makkelijker dan werken met geheugen adressen.
* Het adres wordt door de computer bepaald. Zo weet de computer waar in het geheugen de data staat.
* Het type verteld de computer wat voor soort data het is. Er zijn verschillende soorten datatypes.

```python
getal_A = input("Geef getal a")
getal_B = input("Geef getal b")
```

De computer zal nu de data opslaan in de variabelen getal_A en getal_B

Variabelen mogen geen spaties bevatten en moeten beginnen met een kleine letter. Er zijn twee verschillende manieren in omgang om variabelen op te schrijven. snake_case gebruikt de underscore als vervanging van de spatie. camelCase gebruikt hoofdletters voor elke nieuw woord. Welke van de twee gebruikt wordt maakt niet uit, maar wees consequent ter bevoordering van de leesbaarheid van je code.

## Datatypes
Er zijn verschillende soorten datatypes:
- **int** Een geheel getal van 32 of 64 bits groot.
- **float** Een komma getal
- **Bool** Is afgeleid van boolean en heeft enkel de waarde True of False
- **String** Een reeks van characters, zoals woorden en zinnen. Deze wordt aangegeven met de dubbele haakjes
- **Array** Een lijst van objecten.

Er zijn ook andere datatypes, maar voor nu is dit alles wat we gaan gebruiken. Zodra een variabelen wordt gemaakt probeert Python in te schatten welke datatype er wordt bedoelt. Dit gaat niet altijd goed. In andere talen, zoals java, moet de programmeer aangeven welke datatype de variabele heeft.

```python
getal_A = input("Geef getal a")
```

Om ervoor te zorgen dat de input echt een getal is en geen woord kan de functie int() gebruikt worden.

```python
getal_A = int(input("Geef getal a"))
```

De input dat gegeven wordt, wordt nu omgezet naar een int.

## Python operatoren

Python kent verschillende operatoren om mee te rekenen en om variabelen te vergelijken.

| Betekenis                         |                                 |
|-----------------------------------|---------------------------------|
| groepering                        | `(` `)`                         |
| machtsverheffing                  | `**`                            |
| vermenigvuldiging, modulo, deling | `*` `%` `/` `//`                |
| optelling, aftrekking             | `+` `-`                         |
| vergelijking                      | `==` `!=`, `<`, `>`, `<=`, `>=` |
| toekenning                        | `=`                             |


**Opdracht 1.**

Gegeven een stukje code, welke ouput verwacht je?

a.


```python
a = 5
b = 2
print(a * b)
```

b.


```python
a = "5"
b = 2
print(a * b)
```

c.


```python
a = 5
b = 2
print(a < b)
```

d.


```python
a = "5"
b = "2"
print(a + b)
```

e. % staat voor modulo rekenen


```python
a = 5
b = 2
print(a % b)
```

f.


```python
a = 5
b = a
a = 2
print(a)
print(b)
```

g. Er zijn twee manieren gegeven voor een deling, namelijk / en //. Zoek uit wat het verschil is om te bepalen wat de ouput is van onderstaand programma.

```python
a = 5
b = 2
print(a / b)
print(a // b)
```

**Opdracht 2**

Waar kan dit programma gebruikt voor worden?


```python
getal = int(input("geef een geheel getal"))
print(getal * getal)
```

## If then else


Stap 1 van het plan was:  Neem twee getallen a en b. Via de input functie kan er gevraagd worden voor twee getallen en deze worden opgeslagen in variabelen.


```python
getal_A = int(input("Geef een geheel getal a: "))
getal_B = int(input("Geef een geheel getal b: "))
```

Nu stap 2 nog: de twee getallen met elkaar vergeleken worden om te bepalen welke van de twee getallen de grooste is.

**opdracht 3**

Wat is het nadeel van onderstaande code?


```python
getal_A = int(input("Geef een geheel getal a: "))
getal_B = int(input("Geef een geheel getal b: "))
print(getal_A > getal_B)
```

### Het if statement

Met behulp van een if-statement kan een computer verteld worden of een stuk code wel of niet uitgevoerd hoeft te worden. Als de if statement true is wordt de code binnen de if statement uitgevoerd. ALs de if statement false is slaat de computer de code over

if *conditie* :
&emsp;   Do this
&emsp;    Do this
&emsp;    Do this

### syntax
Let op de dubbele punt na de conditie, deze is verplicht. Ook heel belangrijk binnen python is het gebruik van tabs. De code dat uitgevoerd moet worden als de if statement true is hebben een tab, een zogenaamde indentation. Dit is gevoelig. Als de code ook maar een spatie uit lood ligt werkt de code niet of geeft het een andere uitkomst dan gewenst.

Binnen python hoeven er geen haakjes om de conditie. Ook hier geldt dat je consequent moet zijn. Dus overal haakjes in de if-statement of nergens.

Dit alles valt onder syntax. Als er een fout wordt gemaakt in de syntax geeft de compiler een `syntax error`. Vaak geeft het ook een regelnummer waar hij het probleem is tegengekomen. Vaak mist er dan dubbele puntjes. Een andere error wat je tegen kan komen is `indentation error`. Dan is er een probleem met het gebruik indentations, met andere worden, de tabs.

**Opdracht 4:**   Wat is de output?

a.


```python
a = 5
b = 2
if a < b:
    print(a)
print(b)
```

b.


```python
a = 5
b = 2
if a > b:
    print(a)
print(b)
```

c.


```python
a = 5
b = 2
if a == b:
    print(a)
    print(b)
```

d.


```python
a = 5
b = 2
if a == b:
    print(a)
   print(b)
```

### Het if-else statement

Soms is het nodig om een computer te laten kiezen tussen twee opties. Als a waar is voer opdracht a uit en anders voer opdracht b uit.

if *conditie* :
&emsp;   Do this
&emsp;    Do this
&emsp;    Do this
else :
&emsp;    Do that
&emsp;    Do that

Ook hier is het weer belangrijk om aan de tabs te denken en aan de dubbele punten!

**Opdracht 5** Wat is de output?

a.

```python
a = 5
b = 2
if a < b:
    print(a)
else:
    print(b)
```

b.

```python
a = 5
b = 2
if a > b:
    print(a)
else:
    print(b)
```

c.

```python
a = 5
b = 2
if a > b:
    print(a - b)
else:
    print(b - a)
print(a + b)
```

### De if-then-else boom

Het is ook mogelijk om de computer te laten kiezen tussen verschillende opties, Dit kan gedaan worden door een else if te gebruiken, in python aangegen met elif. Als a waar is voer opdracht a uit anders als b waar is voer opdracht b uit anders voer opdracht c uit.

if *conditie* :
&emsp;   Do this
&emsp;    Do this
&emsp;    Do this
elif *conditie* :
&emsp;    Do this
&emsp;    Do this
else:
&emsp;    Do this
&emsp;    Do this

Er kan een onbeperkte hoeveelheid else if condities toegevoegd worden en er hoeft niet altijd geëindigd te worden met else. De else statement wordt enkel uitgevoerd als alle bovenstaande statements false zijn. Zodra een true statement wordt gevonden zullen de andere statement binnen de boom niet meer gecontroleerd worden.

```python
if cijfer > 7.5:
    print("Goed")
elif cijfer > 5.5:
    print("Voldoende")
else:
    print("Onvoldoende")
```

Als het behaalde cijfer een 8 is print dit programma 'goed'. Het ligt namelijk hoger dan een 7.5, dus de eerste statement is true en is de statement dat wordt uitgevoerd. De andere statements worden niet meer gecontroleerd. Dus ondanks dat een 8 ook hoger is dan een 5,5 wordt het woord 'voldoende' niet geprint.

Als het behaalde cijfer een 6 is print het programma 'voldoende'. De eerste statement is false, gezien 6 lager is dan een 7,5. De tweede statement is true en dus wordt het woord 'voldoende' geprint.

Als het behaalde cijfer een 4 is print het programma onvoldoende gezien de eerste twee statements false zijn wordt automatisch de else statement uitgevoerd.

**Opdracht 6** Wat is de output?

a.

```python
getal = 6.8
if getal > 7.5:
    print("hello")
elif getal > 5.5:
    print("bonjour")
else:
    print("hoi")
```

b.

```python
getal = 8.2
if getal < 5.5:
    print("bonjour")
elif getal < 7.6:
    print("hoi")
else:
    print("hello")
```

c.

```python
getal = 7.5
if getal >= 5.5 and getal < 7.5:
    print("hoi")
elif getal > 7.5:
    print("hello")
else:
    print("bonjour")

```

d.

```python
getal = 6.8
if getal < 5.5:
    print("hoi")
else:
    if getal < 7.6:
        print("hello")
    else:
        print("bonjour")

```

**Opdracht 7** Wat is de output?

a.

```python
x = 42
if x > 5 and x < 10:
    x = x * 2
elif x < 20:
    x = x / 2
print(x)
```

b.

```python
x = 2
if x < 5:
    x = x * 2
elif x < 10:
    x = x / 2
print(x)
```

c.

```python
x = 6
if x < 10:
    x = x * 2
if x < 20:
    x = x / 2
print(x)
```

d.

```python
x = 42
if x > 5 and x < 10:
    x = x * 2
elif x < 5 or x > 10:
    x = x / 2
else:
    x = x + 2
print(x)
```

e.

```python
x = 10
if x > 5 and x < 10:
    x = x * 2
elif x < 5 or x > 10:
    x = x / 2
else:
    x = x + 2
print(x)
```

## Maximum probleem

Met behulp van een if-else statement kan het programma afgerond worden. Het plan was:

1. Neem twee getallen a en b
2. als a > b dan is a de grooste anders is b het grootste getal.

Met behulp van inputs en variabelen was stap 1 opgelost.

```python
getal_A = int(input("Geef een geheel getal a: "))
getal_B = int(input("Geef een geheel getal b: "))
```

Met behulp van if-else statements kunnen we stap twee oplossen door de twee getallen met elkaar te vergelijken en het grooste getal te printen.

```python
getal_A = int(input("Geef een geheel getal a: "))
getal_B = int(input("Geef een geheel getal b: "))

if getal_A > getal_B:
    print(getal_A)
else:
    print(getal_B)
```

**Opdracht 8**
rock-paper-scissors.

Rock-paper-scissors is een bekend spel dat gespeeld wordt door twee spelers. Beide spelers kunnen kiezen tussen een steen, papier of een schaar. Steen wint van de schaar, schaar wint van papier en papier wint van de steen. Als beide spelers dezelfde kiezen is het gelijkspel.

a. Een student heeft een poging gedaan om een stukje programma te schrijven dat een winaar kan aanwijzen. Het werkt alleen nog niet zo goed. Welke fouten zijn er gemaakt?


```python
speler1 = (input("rock, paper of scissor "))
speler2 = (input("rock, paper of scissor "))

if speler1 == "rock" and speler2 =="rock" :
    print("Tie")
    if speler1 == "scissor" and speler2 =="scissor" :
        print("Tie")
        if speler1 == "paper" and speler2 =="paper" :
            print("tie")

if speler1 == "rock":
    if speler2 =="scissor":
        print("speler 1 wins")
        if speler2 == "paper":
            print("speler 2 wins")


if  speler1 == "scissors":
    if speler2 =="paper":
        print("speler 1 wins")
    else:
        print("speler 2 wins")
```

b. Herschrijf de code tot een werkende versie.

c. (uitdaging). Herschrijf de code met zo min mogelijk regels code. Het probleem kan opgelost worden in 8 regels. Dit is mogelijk daar handig gebruik te maken van and en or (boolean logica).
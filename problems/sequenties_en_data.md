# Sequenties en data

```{include} ../class/problems/sequenties_en_data.md
```

Je gaat in deze opdracht het volgende oefenen:

- in het eerste gedeelte ga je oefenen met splitsen en gebruiken van Python data
- in het tweede gedeelte ga je aantal *functies* schrijven, de fundamentele bouwstenen van software

## IPython

We gaan eerst bekend raken met de omgeving waar je de meeste tijd in zal doorbrengen, de interactieve Python *interpreter* (of *shell*) IPython.

Voor dit gedeelte hoef je *niet* met een bestand te werken, start IPython door `ipython` op de command line te typen. Je zal aan de prompt `In [n]` zien of je in ipython bent (`n` zal een getal zijn), of zoals je dit zal zien als regel op de command line:

```ipython
In [1]:
```

### Genummerde prompts

De genummerde prompts zijn handig omdat je alle invoer (bijvoorbeeld strings) en uitvoer (welk type dan ook) kan ophalen via hun nummer. Probeer de onderstaande voorbeelden om te zien hoe dit werkt:

```ipython
In [1]: 6*7
Out[1]: 42

In [2]: Out[1]*2
Out[2]: 84

In [3]: In[1]*2
Out[3]: '6*76*7'
```

Heel fijn! De Python `eval` functie voert strings uit alsof het Python commando's zijn. Probeer `eval(Out[3])` eens in het bovenstaande voorbeeld uit te voeren!

:::{admonition} Nummering van de prompt
:class: notice

Het kan heel goed zijn dat de opgaven *niet* dezelfde nummering hebben als jouw prompt, maak je geen zorgen als deze afwijkt!
:::

### Bewerkingen met Python

Probeer om te beginnen een paar bewerkingen met getallen, lists (lijsten), strings en booleans, bijvoorbeeld:

```ipython
In [1]: 40 + 2
Out[1]: 42

In [2]: 40 ** 2
Out[2]: 1600

In [3]: 40 % 7  # 40 "mod" 7: de rest van 40 gedeeld door 7
Out[3]: 5

In [3]: 40 // 11  # integerdeling: de rest wordt genegeerd
Out[3]: 3

In [4]: 'hi there!'  # (zie hoe beleefd Python is!)
Out[4]: 'hi there!'

In [5]: 'who are you?'  # (maar is soms wat gevoelig.)
Out[5]: 'who are you?'

In [6]: L = [0, 1, 2, 3]  # Je kan gegevens (in dit geval een list) een naam geven (in dit geval de naam L)
# (Python geeft hier geen antwoord)

In [7]: L
Out[7]: [0, 1, 2, 3]  # Je kan de gegevens zien, in dit geval een list die bij de naam L hoort

In [8]: L[1:]  # Je kan lijsten slicen (in dit geval de list met naam L)
Out[8]: [1, 2, 3]

In [9]: L[::-1]  # Je kan lijsten omdraaien (ook strings!) door middel van "stap" slicing met -1 als de stapgrootte.
Out[9]: [3, 2, 1, 0]

In [10]: [6, 7, 8, 9][1:]  # Je kan lijsten slicen met de lijst zelf in plaats van een naam (Dat is in dit geval niet heel handig, inderdaad!)
Out[10]: [7, 8, 9]

In [11]: 100*L + [42]*100
Out[11]: (een lijst met 500 elementen ...)

In [12]: L = 42  # Je kan een andere waarde toekennen aan de naam L, zelfs van een ander type. Nu wijst L naar de integer 42, in plaats van de list waar het eerder naar verwees
# (Python geeft hier geen antwoord)

In [13]: L == 42  # Eén of twee gelijktekens maakt uit! Dit _vergelijkt_ de twee waarden.
Out[13]: True

In [14]: L != 42  # Dit test op "ongelijkheid"
Out[14]: False
```

### Fouten

Fouten zijn onvermijdelijk! Deze fouten worden in Python ook wel *exceptions* genoemd en één van de belangrijkste gewoontes die je hopelijk tijdens het maken van de oefeningen zult ontwikkelen is dat wanneer een fout optreedt *je dit beschouwt als een kans, en niet als een probleem*!

Wat we hiermee bedoelen is dat een fout de perfecte gelegenheid is om:

1. jouw beeld van hoe een computer werkt te helpen verbeteren (de "gedachtegang van de computer")
2. de code (software) die je schrijft (of jouw begrip daarvan) te helpen verbeteren
3. jouw *debugging* vaardigheden te verbeteren (foutmeldingen begrijpen en fouten kunnen opsporen)

Laten we nu fouten gaan maken, oftewel *exceptions*. Neem hier *een paar minuten* de tijd voor en probeer in deze tijd zoveel mogelijk van de onderstaande *exceptions* te veroorzaken!

`NameError`
: Een onbekende variabele!

`TypeError`
: Probeer bijvoorbeeld een integer te *slicen*, of een integer bij een string op te tellen!

`ZeroDivisionError`
: De naam geeft het misschien al aan, iets delen door 0?

`SyntaxError`
: Fouten die katten veroorzaken als ze over een toetsenbord lopen...

`IndexError`
: Probeer een index die buiten de grenzen van een sequentie valt (bijvoorbeeld van een list of string)

`OverflowError`
: Bedenk dat integers niet kunnen *overflowen*, als ze te groot worden voor het geheugen dan zal Python crashen (ook een leuk experiment!). Om een `OverflowError` te kunnen genereren zal je *floating point* getallen zoals bijvoorbeeld `42.0` in een berekening moeten gebruiken. Pas bijvoorbeeld de machtsverheffingsoperator `**` toe om snel tot heel grote getallen te komen!

Probeer deze fouten te veroorzaken in IPython. Bijvoorbeeld, stond in het volgende voorbeeld nu een kat op het toetsenbord?!?:

```ipython
In [15]: 2 + 2qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
  File "<ipython-input-13-29796e3163e7>", line 1
    2 + 2qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
                                              ^
SyntaxError: invalid syntax
```

## Opgave

In deze opgave ga je oefenenen met *slicen* en *indexeren* van lijsten (lists).

Maak eerst een nieuw tekstbestand aan, kopieer vervolgens het volgende in het bestand en sla het op als `wk2ex1.py`:

```python
# Voorbeeldopgave lists, resultaat: [2, 7, 5, 9]

e = [2, 7, 1]
pi = [3, 1, 4, 1, 5, 9]

answer0 = e[0:2] + pi[-2:]
print(answer0)
```

:::{admonition} Opmerkingen bij deze code
:class: notice

- let op dat je het bestand opslaat als platte tekst met een `.py` bestandsextensie (zie werken met [platte tekst](../support/platte_tekst.md))
- in de code worden *twee* lists gedefiniëerd, één met de naam `e` en een ander met de naam `pi`
- wanneer je de code uitvoert zal de regel `answer0 = e[0:2] + pi[-2:]` de waarde van de variabele `answer0` definiëren. Met andere woorden, vanaf deze regel is in het programma de naam `answer0` bekend die verwijst naar het resultaat van de expressie `e[0:2] + pi[-2:]`!
- vervolgens drukt de code de waarde van de variabele `answer0` af.
:::

### Code uitvoeren

Let op het volgende om jouw bestand in IPython te kunnen uitvoeren:

* zorg dat je op de command line in de directory bent waar `wk2ex1.py` is opgeslagen. Dit kan bijvoorbeeld het Bureaublad zijn of een andere directory (gebruik `pwd` om te zien waar je bent!)
* typ `ipython` om IPython te starten
* voer in IPython vervolgens `run wk2ex1.py` uit

:::{admonition} Liever lui dan moe
:class: tip

Een geschiedenis wordt bijgehouden van alles wat je al eerder op de command line hebt getypt en zo kan je eerdere commandos terughalen met pijltje omhoog.

Een ander hulpmiddel dat je op de command line kan gebruiken is *Tab completion*, dat wil zeggen, laat de shell voorzover mogelijk het commando aanvullen zolang het uniek is. Bijvoorbeeld, je wilt jouw bestand `mijn_bestand.py` laten uitvoeren in IPython, dan zal je waarschijnlijk aan `run mijn<Tab>` genoeg hebben om het door de shell te laten aanvullen tot `run mijn_bestand.py` (`<Tab>` is natuurlijk de tab-toets op jouw toetsenbord!).
:::

### Lijsten maken en bewerken

In deze opgave ga je een aantal lijsten maken met *alleen* maar de getallen in de lijsten `pi` en `e` met behulp van de volgende bewerkingen:

-   lijsten indexeren, bijvoorbeeld `pi[0]`
-   lijsten slicen, bijvoorbeel `e[:1]`
-   stapsgewijs slicen, bijvoorbeeld `pi[0:6:2]`
-   lijsten samenvoegen met `+`, bijvoorbeeld `e[0:2] + pi[-2:]`

    (voor deze opgaven vragen we jou `+` *niet* te gebruiken voor het optellen van getallen)

:::{admonition} Lege regels en experimenteren
:class: info

Gebruik *één of meer lege regels* tussen jouw antwoorden (zodat het zowel voor jou als voor ons goed leesbaar blijft!).

Nadat je het bestand een eerste keer hebt uitgevoerd met `run` kan je experimenteren op de IPython command line, probeer bijvoorbeeld `e[0:1] + pi[0:1]` te typen.

*Als je het leuk vindt* kan je proberen zo min mogelijk bewerkingen te gebruiken om tot eenvoudige, elegante en efficiënte oplossingen te komen.
:::

De opgaven zijn als volgt:

0.  Gebruik `pi` en `e` (of maar één!) om de lijst `[2, 7, 5, 9]` te maken. Dit is het voorbeeld dat je hierboven ziet, deze lijst bewaar je in de variabele met naam `answer0`.

1.  Gebruik `pi` en `e` (of maar één, je mag voor alle verdere problemen ook maar één lijst gebruiken) om de lijst `[7, 1]` te maken.

    Bewaar de lijst, net als hierboven, in de variabele `answer1`. Hier is een klein begin wat je kan kopiëren en plakken:

    ```python
    # Opgave 1: [7, 1] maken

    answer1 = e[1:2]  # niet het juiste antwoord, maar een begin...
    print(answer1)
    ```

2.  Gebruik `pi` en `e` om de lijst `[1, 1, 2]` te maken. Bewaar deze lijst in de variabele `answer2`.

3.  Gebruik `pi` en `e` om de lijst `[1, 4, 1, 5, 9]` te maken. Bewaar deze lijst in de variabele `answer3`.

4.  Gebruik `pi` en `e` om de lijst `[1, 2, 3, 4, 5]` te maken. Bewaar deze lijst in de variabele `answer4`.

### Strings slicen en indexeren

Deze opgave is in dezelfde stijl als de vorige, maar gebruikt strings in plaats van lijsten. Kopieer eerst de volgende regels naar jouw bestand onder de laatste opgave die je hebt gemaakt (gebruik lege regels om ze duidelijk van elkaar te scheiden!):

```python
# Oefeningen met strings

h = "hanze"
s = "hogeschool"
g = "groningen"
```

Je mag elke combinatie van de onderstaande vier bewerkingen gebruiken:

-   strings indexeren, bijvoorbeeld `h[0]`
-   strings slicen, bijvoorbeeld `s[1:]`
-   strings samenvoegen met `+`, bijvoorbeeld `h + s`
-   herhalingen met `*`, bijvoorbeeld `42*g`

De opgaven zijn als volgt (de eerste kijg je van ons):

5.  Gebruik `h`, `s` of `g` (je mag voor elke volgende opgave één of meerdere gebruiken) om de string `hoi` te maken.

    Bewaar de string in de variabele met naam `answer5`. De oplossing zie je hieronder, kopiëer en plak deze in jouw bestand:

    ```python
    # Opgave 5:  'hoi' maken

    answer5 = s[0:2] + g[4]
    print(answer5)
    ```

    In totaal zijn 3 bewerkingen nodig, het ophalen van `ho` met `s[0:2]` (slicen), het ophalen van `i` met `g[4]` (indexeren) en vervolgens deze twee waarden samenvoegen met `+` zodat we tot `hoi` komen als nieuwe waarde.

    :::{admonition} Meer of minder bewerkingen
    :class: warning

    Bij elk van de volgende opgaven zullen we steeds aangeven wat het minimaal aantal bewerkingen is dat wij hebben kunnen vinden. Het maakt niet uit als jij meer bewerkingen nodig hebt, zolang je maar tot een *juiste oplossing* komt!
    :::

6.  Gebruik `h`, `s` of `g` om de string `schoenen` te maken en bewaar deze string in de variabele `answer6`. (Ons record: 4 bewerkingen)

7.  Gebruik `h`, `s` of `g` om de string `anzeogeschool` te maken en bewaar deze string in de variabele `answer7`. (Ons record: 3 bewerkingen)

8.  Gebruik `h`, `s` of `g` om de string `gnagnahahahahaha` te maken en bewaar deze string in de variabele `answer7`. (Ons record: 7 bewerkingen)

9.  Gebruik `h`, `s` of `g` om de string `legonoego` te maken en bewaar deze string in de variabele `answer7`. (Ons record: 7 bewerkingen)

10. Gebruik `h`, `s` of `g` om de string `leggings` en bewaar deze string in de variabele `answer7`. (Ons record: 7 bewerkingen)

Als je hier bent aangekomen, heb je de eerste helft van dit practicum voltooid! Je kan je bestand
`wk2ex1.py` in GradeScope inleveren.

Uitstekend! Nu door naar het volgende deel van het practicum

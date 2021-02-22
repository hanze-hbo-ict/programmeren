# De slaapwandelende student

```{include} ../class/problems/slaapwandelende_student.md
```

In deze opgave ga je functies schrijven om het gedrag van een slaapwandelende student te bestuderen, dit noemen we ook wel een "toevalsbeweging" of "random walk". De student loopt door een lange gang, maar omdat de student slaapt is elke stap in een willekeurige richting (links of rechts). Blijft de student eeuwig vastzitten in de gang? Of bereikt de student uiteindelijk de practicumruimte (of een bed)?

## Deel 1: `rs()`

Maak een nieuw bestand `wk3ex2.py` aan en begin met de volgende header en functie `rs()`:

```python
# Programmeren I, week 3 opgave 2
# Bestandsnaam: wk3ex2.py
# Naam:
# Probleemomschrijving: Slaapwandelende student

import random


def rs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
       arguments: none at all!
    """
    return random.choice([-1, 1])
```

Je kan de functie `rs()` aanroepen elke keer dat je een nieuwe, willekeurige stap wilt zetten, de returnwaarde zal `1` of `-1` zijn.

Een voordeel om dit in als functie te hebben is dat het hierdoor makkelijk wordt later aan te passen wat een "willekeurige stap" betekent, zonder andere code te hoeven aanpassen!

:::{admonition} Header
:class: question

Met *header* wordt bedoeld alles wat algemeen is en bovenin jouw bestand wordt beschreven, bijvoorbeeld een commentaar of eventuele import statements van Python modules die jouw functies gaan gebruiken. Vergelijk dit verder met de kop-lijf-staart structuur van een tekst (hoewel Python bestanden geen staart hebben!).
:::

### Modules importeren

Je ziet dat de Python module `random` wordt geïmporteerd. Laten we even stilstaan bij het verschil tussen `import` zoals wij het hier gebruiken en de variant `from ... import *`

Als je het `import`-statement als volgt gebruikt

```python
import random
```

kan je de module `random` gebruiken, maar je moet in dat geval elke aanroep vooraf laten gaan door de *naam* van de module:

```python
random.choice([-1, 1])
```

Een andere manier om modules te gebruiken is met:

```python
from random import *
```

In dit geval worden *alle* functies en constanten uit de module `random` geïmporteerd en kan je gewoon `choice([-1, 1])` gebruiken, wat korter is. Je zou een probleem kunnen hebben als je nog een *andere* functie met de naam `choice` hebt maar op dit moment hoef je hier geen rekening mee te houden.

## Strings: een opfrisser

In deze opgave is *stringvermenigvuldiging* heel handig. Hier is een opfrisser:

```ipython
In [1]: print('spam' * 3)
Out[1]: 'spamspamspam'

In [2]: print('begin|' + '_'*10 + '|einde')
Out[2]: 'begin|__________|einde'
```

In het tweede voorbeeld geeft `'_'*10` aan hoeveel ruimte er moet zijn tussen `'begin|'` en `'|einde'`. Het is mooi om underscores (liggende streep) of een andere "ondergrond" te gebruiken waar de slaapwandelaar over kan rondlopen!

## Deel 2: `rwpos(start, nsteps)`

Schrijf nu een functie met de naam `rwpos(start, nsteps)` die twee argumenten accepteert:

- Een integer `start`, die de beginpositie van de slaapwandelaar voorstelt
- Een (niet negatieve) integer `nsteps` die het aantal willekeurige stappen voorstelt dat moet worden gezet vanaf de startpositie.

De naam `rwpos` bevat de aanwijzing dat deze functie de `r`andom-`w`alker-`pos`itie teruggeeft.

Schrijf `rwpos` zodat het de *positie* van de slaapwandelaar na `nsteps` willekeurige stappen teruggeeft, waarbij elke stap de functie `rs()` gebruikt om de positie aan te passen; in dit geval betekent het dat de positie altijd plus `1` of min `1` is ten opzichte van de vorige positie.

### Zo maar een voorbeeld

Bekijk het *raad het getal* voorbeeld in het [random voorbeeld](/support/random), je kan dit gebruiken als een begin.

### Debuggen

Je kan als onderdeel van de functie `rwpos` een regel toevoegen die de waarde van `start` afdrukt elke keer dat de functie wordt aangeroepen. Dit is een hulpmiddel om jouw code te kunnen zien wat jouw code doet en eventuele problemen te kunnen *debuggen*. Je kan net als hieronder de string `start is` daar aan toevoegen, bijvoorbeeld `print("start is", start)`.

Vergeet niet dat omdat elke stap willekeurig is de precieze waarden die je functie teruggeeft vrijwel altijd anders zal zijn dan je in dit voorbeeld ziet, maar het algemene beeld moet ongeveer hetzelfde zijn:

```ipython
In [1]: rwpos(40, 4)  # elke keer anders...
start is 40
start is 41
start is 42
start is 41
start is 42
Out[1]: 42

In [2]: rwpos(40, 4)  # elke keer anders...
start is 40
start is 39
start is 38
start is 37
start is 36
Out[2]: 36
```

### Moet je 4 of 5 regels afdrukken?

Je kan vier regels uitvoer hebben in plaats van vijf; dit is waarschijnlijk afhankelijk van of je wel of niet de positie afdrukt in het basisgeval. Beide aantallen zijn helemaal goed voor deze opgave.
### Geen lussen

Ook als je al eerder `while`- of `for`-lussen hebt gebruikt, moet je in deze opgave *recursie* gebruiken! Deze opdrachten zijn in de eerste plaats gericht op het ontwikkelen van ontwerpvaardigheden, en meer specifiek *recursief* ontwerp. Maak je geen zorgen, lussen komen later nog uitgebreid aan bod.

## Deel 3: `rwsteps(start, low, hi)`

Schrijf nu een functie `rwsteps(start, low, hi)` die drie argumenten accepteert:

- Een integer `start` die de beginpositie van de slaapwandelaar voorstelt,
- Een (niet negatieve) integer `low` die de kleinste waarde voorstelt waar de slaapwandelaar heen mag lopen, en
- Een integer `hi` die de hoogste waarde voorstelt waar de slaapwandelaar heen mag lopen.

Je mag ervan uitgaan dat `hi >= start >= low`.

### Handelingen

Wat moet `rwsteps` doen? Het moet een toevalsbeweging simuleren, waarbij elke stap wordt afgedrukt (zie hieronder). Bovendien moet de functie stoppen als de slaapwandelaar *op of buiten* de grenzen `low` en `hi` komt. Als het stopt, moet `rwsteps` het *aantal stappen* teruggeven die de slaapwandelaar genomen heeft om de grens te bereiken.

### Debuggen

Voeg een regel debugcode toe aan `rwsteps` die een visuele weergave geeft van de positie van de slaapwandelaar terwijl deze rondloopt! Je mag best creatiever zijn dan een simpel karakter `'S'`. Je kan bijvoorbeeld `0->-<` of 😴 overwegen (een echte slaapwandelaar!).

Als (leuke) bonusopgave kan je een uitgebreidere simulatie van een slaapwandelaar maken die de weergave laat afhangen van de richting waarop de slaapwandelaar loopt (ogen die naar links of rechts kijken?). De slaapwandelaar zou ook kunnen reageren op andere voorwerpen, personen of dingen in het pad, zie de bonusopgave onderaan.

Hier zijn twee voorbeelden van een simpele slaapwandeling, één die gebruik maakt van spaties en één die underscores gebruikt (waardoor het makkelijker te zien is wat er gebeurt dan met spaties!). Eén van de twee heeft muren aan de zijkanten en de andere niet. Je bent vrij in het maken van keuzes hierin, wees creatief! Ter herinnering, je kan een string van 10 underscores maken met `10*'_'`, stringvermenigvuldiging komt hier goed van pas!

```ipython
In [1]: rwsteps(10, 5, 15)
     |_____S_____|
     |____S______|
     |___S_______|
     |__S________|
     |___S_______|
     |____S______|
     |___S_______|
     |__S________|
     |_S_________|
     |S__________|
Out[1]: 9                     # hier is de returnwaarde!

In [2]: rwsteps(10, 7, 20)
           S
            S
             S
            S
           S
          S
           S
          S
           S
          S
         S
        S
Out[2]: 11
```

### Geen lussen

Ook hier gebruik je recursie om `rwsteps` voor dit probleem te implementeren.

:::{admonition} Recursie toepassen
:class: tip

Dit probleem kan lastig zijn omdat je *zowel* een willekeurige stap moet zetten *als* het totaal aantal stappen moet bijhouden!

Eén manier om dit te doen is om de regel `rest_of_steps = rwsteps(newstart, low, hi)` te gebruiken voor de recursieve aanroep, waarbij `newstart` een geschikte waarde toegekend heeft gekregen op de regel erboven, en `rest_of_steps` op een geschikte manier gebruikt wordt in de returnwaarde eronder...
:::

### Grenzen aan recursie

De standaard recursielimiet van Python is 1000, wat betekent dat Python niet toestaat dat een functie zichzelf meer dan 1000 keer aanroept. Gebeurt dit wel dan stopt Python de uitvoering met de fout `RecursionError: maximum recursion depth exceeded`

Als je deze foutmelding krijgt, kan je de recursiegrens verhogen door de volgende regels toe te voegen bovenaan jouw bestand:

```python
import sys

sys.setrecursionlimit(50000)
```

Door deze aanpassing bevat de recursiestack ruimte voor 50000 functieaanroepen in plaats van de standaard 1000.

### Handelingen vertragen

Wil je de slaapwandelaar vertragen? Je kan de simulatie vertragen door om te beginnen de volgende regels bovenaan jouw bestand toe te voegen:

```python
import sys
import time
```

Vervolgens kan je de onderstaande regels toevoegen aan de functies `rwsteps` en `rwpos`:

```python
sys.stdout.flush()  # forceert Python om alles _nu_ af te drukken
time.sleep(0.1)     # en wacht daarna 0.1 seconde
```

Pas dit verder naar eigen inzicht aan!

## Deel 4: Simulaties van toevalsbewegingen maken en analyseren

Om *random walks* zoals die van onze slaapwandelaar te kunnen analyseren hebben we twee begrippen nodig:

1.  De **totale afwijking** is het aantal stappen *vanaf het beginpunt* tot waar de slaapwandelaar is geëindigd. Dit kan zowel positief als negatief zijn, afwijkingen naar rechts worden als positief beschouwd en afwijkingen naar links als negatief.

    De meest logische manier om de totale afwijking te vinden is om twee getallen van elkaar af te trekken, de eindpositie van de wandelaar minus de beginpositie. Om dit te doen heb je een variant van `rwpos` nodig (en niet `rwsteps`).

2.  De **gekwadrateerde afwijking** is het *kwadraat* van het aantal stappen vanaf het beginpunt waar de wandelaar is geëindigd. Dat wil zeggen, het is het kwadraat van de totale afwijking.

Onderzoek met deze twee begrippen in het achterhoofd de volgende twee vragen:

-   Wat is de gemiddelde *totale afwijking* voor een wandelaar na het zetten van `100` willekeurige stappen? En wat is het gemiddelde na `n` willekeurige stappen? Zoals hierboven beschreven is de totale afwijking het resultaat van `rwpos` minus de beginpositite `start`. Maak hier *geen* gebruik van de ingebouwde Python functie `abs`.

-   Wat is de gemiddelde *gekwadrateerde afwijking* voor een wandelaar na het zetten van `100` willekeurige stappen? En wat is het gemiddelde na `n` willekeurige stappen, kan je dit uitdrukken in termen van `n`? Controleer dat je de totale afwijkingen kwadrateert *voordat* je ze optelt om het gemiddelde te berekenen!

Je zult jouw random walk functies moeten aanpassen om de bovenstaande vragen te kunnen beantwoorden. Heel specifiek zal je volgende stappen moeten zetten:

1.  Schrijf een versie van `rwpos` die *geen* debuginformatie of uitleg afdrukt. Ze moet alleen de uiteindelijke   positie teruggeven. Noem deze nieuwe versie `rwpos_plain`.

    Let op, de recursieve aanroep(en) moeten aangepast worden zodat `rwpos_plain` wordt aanroepen, en niet `rwpos`!

2.  Bedenk een plan hoe je deze vragen gaat beantwoorden en in ieder geval een *list comprehension* bevat die vergelijkbaar is met:

    ```python
    lc = [rwpos_plain(0, 100) for x in range(142)]
    ```

    Het zal je niet verassen dat de waarde `142` in jouw oplossing door een variabele zal moeten worden vervangen. Om het *gemiddelde* van de waarden die je gevonden hebt te berekenen heb je `sum(lc)` in combinatie met `len(lc)` nodig...

3.  Om met list comprehensions vertrouwd raken is het handig om het bovenstaande op de Python prompt uit te voeren:

    ```ipython
    In[42]: lc = [rwpos_plain(0, 100) for x in range(142)]
    ```

    Kijk naar de waarde die in `lc` terecht is gekomen (deze zal 142 elementen bevatten). Bepaal ook het gemiddelde van `lc`. Gebruik hier geen rekenmachine voor, bedenk hoe je dit in Python kan doen!

4.  Schrijft twee extra functies:
    -   de functie `ave_signed_displacement(numtrials)`, die `rwpos_plain(0, 100)`  `numtrials` keer moet uitvoeren en het gemiddelde van het resultaat moet teruggeven. Gebruik de bovenstaande list comprehension als de eerste regel van je functie! (en vervang 142 door een variabele...)

    -   de functie `ave_squared_displacement(numtrials)`, die `rwpos_plain(0, 100)` `numtrials` keer moet uitvoeren en het gemiddelde van de *kwadraten* van het resultaat moet teruggeven! Eén manier om dit te doen is door de list comprehension een beetje aan te passen. Bedenk dat `x**2` de manier is waarop je in Python `x` kwadrateert.

Roep de functies vervolgens aan en bestudeer de resultaten die deze tests opleveren. Neem jouw antwoorden op in het bestand, dit kan door ze in commentaar te zetten (met het `#` teken) of *eenvoudiger* door ze in een triple-quoted string op te nemen die je kent van docstrings (omdat daar regelafbrekingen in mogen voorkomen). Bijvoorbeeld,

```python
"""
    Om de gemiddelde totale afwijking voor een
    toevalsbeweging met 100 willekeurige stappen
    te berekenen, heb ik ...
        (leg kort je methode en het resultaat uit)

    Zorg dat je ave_signed_displacement en
    ave_squared_displacement beide ten minste één
    keer uitvoert en de gegevens en het gemiddelde
    hierin kopieert.
"""
```

Jouw bestand moet dus voor deel 4 de volgende onderdelen bevatten:

1. de antwoorden op de twee bovenstaande vragen en je aanpak hiervan
2. de bovenstaande Python-functies, inclusief `ave_signed_displacement(numtrials)` en `ave_squared_displacement(numtrials)`.

Vergeet niet om docstrings met commentaar en uitleg aan elke functie die je schrijft toe te voegen! Vermeld verder als het kan eventuele bronnen die je hebt gebruikt, bijvoorbeeld informatie over random walks die je online hebt gevonden. Voel je niet verplicht dit te doen, de vraag of jouw antwoorden en analyses juist zijn hebben verder *geen effect* op de beoordeling van deel 4 van deze opdracht! Jouw werk zal eerder worden beoordeeld op de vraag of de functies werken zoals ze zouden moeten werken, of ze nuttig zijn voor het beantwoorden van de vragen, en of je in heldere bewoordingen een beschrijving hebt kunnen geven.

## Bonusopgave

Voor maximaal 5 bonuspunten kan je aanpassingen doen aan de ASCII-weergave van je slaapwandelaar(s):

* Bijvoorbeeld, een bijzonder creatieve [ASCII emoji](https://en.wikipedia.org/wiki/List_of_emoticons) of grens
* Een karakter dat verandert afhankelijk van of het naar links of naar rechts beweegt
- Een aparte `rwsteps` functie die meer dan één wandelaar heeft (die misschien op elkaar reageren)
- Het combineren van al deze dingen of iets volledig anders implementeren (een wandeling in een tweedimensionale ruimte?)

Vergeet niet duidelijk commentaar toe te voegen waarin je jouw extra werk aanprijst, anders kunnen ze door ons over het hoofd worden gezien!

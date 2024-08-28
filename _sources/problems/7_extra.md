# Extra

## John Conway's Game of Life

Game of Life is een *cellulaire automaat* uitgevonden door de in 2020 overleden wiskundige John Conway. Game of Life is niet zozeer een "spel" in de traditionele betekenis, maar een proces dat over tijd veranderd aan de hand van een paar simpele regels. Het proces wordt opgezet als een raster cellen, die ieder "levend" of "dood" kunnen zijn op een gegeven tijdstip. Op elk tijdstip overleven of sterven cellen aan de hand van de volgende regels:

1. Een cel met minder dan twee levende buren sterft (vanwege isolatie)
2. Een cel met meer dan 3 levende buren sterft (vanwege overbevolking)
3. Een dode cel met precies 3 levende buren komt weer tot leven
4. Alle andere cellen blijven in dezelfde toestand

Alhoewel deze regels simpel lijken leiden ze tot complexe en interessante patronen. Meer informatie en een aantal interessante patronen kan je vinden op [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

In dit practicum ga je een Pythonprogramma implementeren om Game of Life te spelen.

### Nadenken over het leven

Zoals altijd is het belangrijk om het probleem in kleine onderdelen op te delen en het programma in stappen te ontwikkelen zodat anderen de code kunnen begrijpen en je kan garanderen dat elk onderdeel correct is voordat je er op doorontwikkelt. We zullen het probleem in de volgende stappen onderverdelen:

* Een tweedimensionale array van cellen maken
* Het bord weergeven (in verschillende kleuren) en het bijwerken met nieuwe gegevens
* De gebruiker toestaan de toestand van de cellen aan te passen
* De regels van "Game of Life" implementeren
* (Optioneel) De simulatie starten en stoppen

Voordat je begint moet je een schema ontwerpen om je gegevens bij te houden. In beginsel zijn de gegevens die je moet bijhouden de toestand van alle cellen op het bord. Om dit te doen, kan je de gegevens in een tweedimensionale array met integerwaardes bijhouden, waar `0` een lege cel (uit) voorstelt en `1` een levende cel (aan) voorstelt.

### Begincode

Begin ermee het zip-bestand op onderstaande link te downloaden:

[wk9ex1.zip](https://github.com/hanze-hbo-ict/programmeren/raw/master/problems/assets/wk9ex1.zip)

Het is het makkelijkst om dit zip-bestand op het bureaublad uit te pakken. Het bevat wat ondersteunende code om je levensgeneraties grafisch weer te geven, maar dat is het laatste deel van het practicum. Eerst ga je de basisfunctionaliteit implementeren om tweedimensionale arrays te maken, te wijzigen en te laten evolueren volgens de regels van Life.

## Stap 1: Een tweedimensionaal "bord" met cellen maken: `create_one_row` en `create_board`

In het bestand `wk9ex1.py` zie je deze voorbeeldfunctie:

```python
def create_one_row(width):
    """Returns one row of zeros of width "width".
       You might use this in your create_board(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row
```

Deze functie biedt een startpunt om *ééndimensionale* lijsten te maken; maar je kan hetzelfde idee gebruiken om onbeperkt diepe geneste lijststructuren te bouwen.

### De functie `create_board`

Bouw op dit voorbeeld voort en schrijf een functie genaamd `create_board(width, height)` die een nieuwe tweedimensionale lijst met `height` rijen en `width` kolommen maakt en teruggeeft, waarin alle gegevenselementen `0` zijn (dit hoeft niet grafisch weergegeven te worden, alleen maar als Pythonlijst!).

Zorg dat je de functie `create_one_row` **niet opnieuw** implementeert!

**Gebruik** in plaats daarvan `create_one_row` in je functie `create_board` op een zelfde manier waarop `0` gebruikt wordt om individuele elementen toe te voegen in `create_one_row`. Hier zie je een sjabloon; je kan dit kopiëren en plakken en dan de delen die nodig zijn om het te voltooien invullen:

```python
def create_board(width, height):
    """Returns a 2D array with "height" rows and "width" columns."""
    a = []
    for row in range(height):
        a += [...]        # gebruik de bovenstaande functie zodat ... één rij is!!
    return a
```

Dat is alles wat je nodig hebt! Het idee is dus om het voorbeeld van `create_one_row` te gebruiken; maar in plaats van dat je elke keer een `0` toevoegt, voegt de functie elke keer een hele rije met `0`'en toe, namelijk het resultaat van `create_one_row`!

Probeer je functie `create_board` uit!

```ipython
In [1]: a = create_board(5, 3)
In [2]: a
Out[2]: [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
```

## Stap 2: Je tweedimensionale bord met cellen afdrukken

### De functie `print_board`

Je hebt ongetwijfeld gemerkt dat als Python een tweedimensionale lijst afdrukt, het de tweedimensionale structuur compleet negeert en alles platslaat naar een enkele regel (misschien met regelafbreking, als dat nodig is). Om je bord tweedimensionaal af te drukken met ASCII-tekens (we zullen het grafisch weergeven als het helemaal werkt) kan je deze functie kopiëren naar je bestand.

**Let op: er mist één regel!** Misschien zie je het al...

```python
def print_board(a):
    """This function prints the 2D list-of-lists a."""
    for row in a:               # row is de hele rij
        for col in row:         # col is het individuele element
            print(col, end='')  # druk dat element af
```

Probeer `print_board` vervolgens uit. Op dit moment, klopt het *niet helemaal*:

```
In [1]: a = create_board(5, 3)
In [2]: print_board(a)
000000000000000
```

**Voeg één regel toe* zodat `print_board` onze *tweedimensionale* array tweedimensionaal weergeeft!

:::{admonition} `print()`
:class: tip
De betreffende regel is `print()`; een leeg print-statement. *Waar moet deze regel staan?!*
:::

Vergeet niet je verbeterde `print_board` te testen:

```ipython
In [1]: a = create_board(5, 3)
In [2]: print_board(a)
00000
00000
00000
```

## Stap 3: Patronen toevoegen aan tweedimensionale arrays

### De functie `diagonalize`

Om te oefenen met het lussen over tweedimensionale arrays, kan je deze functie genaamd `diagonalize(width, height)` naar je bestand kopiëren:

```python
def diagonalize(width, height):
    """Creates an empty board and then modifies it
       so that it has a diagonal strip of "on" cells.
       But do that only in the *interior* of the 2D array.
    """
    a = create_board(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if row == col:
                a[row][col] = 1
            else:
                a[row][col] = 0

    return a
```

Deze functie, `diagonalize`, krijgt de gewenste breedte en hoogte mee. Ze maakt dan een array `a` en stelt de elementen in `a` zo in dat alle elementen `0` zijn *behalve de **binnenkant** van de diagonaal* waar geldt dat `row == col`.

Probeer de resultaten weer te geven met deze commandos:

```ipython
In [1]: a = diagonalize(7, 6)

In [2]: a
Out[2]:
[[0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]

In [3]: print_board(a)
0000000
0100000
0010000
0001000
0000100
0000000
```

Bekijk even goed in welke richting de diagonaal loopt; dat geeft aan op welke manier de *rijen* van het bord weergegeven worden: van boven naar beneden, in dit geval.

:::{admonition} De randen blijven 0!
:class: notice

Merk op dat de code `range(1, height - 1)` en `range(1, width - 1)` gebruikt om te voorkomen dat de randen aangepast worden.

We zullen dit patroon blijven gebruiken tijdens dit practicum, aangezien Game of Life niet kan werken met randcellen (ze hebben minder dan 8 buren).
:::

Je kan in dit voorbeeld ook zien dat `height` en `width` niet hetzelfde hoeven te zijn; het is echter geen probleem als dat wel zo is.

### De functie `inner_cells`

Schrijf aan de hand van het voorbeeld van `diagonalize` een variatie met de naam `inner_cells(w, h)` die een tweedimensionale array teruggeeft met *alleen maar* levende cellen, met een waarde `1`, ***behalve*** een rand van één cel breedt die leeg blijft (met een waarde `0`) langs de buitenrand van de tweedimensionale array.

Je kan bijvoorbeeld dit proberen:

```ipython
In [1]: a = inner_cells(5, 5)

In [2]: print_board(a)            # je kan hiervoor pijltje omhoog gebruiken!
00000
01110
01110
01110
00000
```

Dit is maar een kleine aanpassing op `diagonalize`!

### De functie `random_cells`

Maak nu een functie genaamd `random_cells(w, h)`, die een array met willekeurig toegekende `1`'en en `0`'en teruggeeft, *behalve* de buitenrand, die moet nog steeds helemaal leeg zijn (allemaal `0`'en), net zoals bij `inner_cells`.

Hier is een voorbeelduitvoer:

```ipython
In [1]: a = random_cells(10, 10)

In [2]: print_board(a)  # pijltje omhoog!
0000000000
0100000110
0001111100
0101011110
0000111000
0010101010
0010111010
0011010110
0110001000
0000000000
```

Je herinnert je misschien dat `random.choice([0, 1])` een `0` of een `1` teruggeeft. Je hebt `import random` nodig om dit te kunnen gebruiken!

## De functie `copy`

Elk van de functies tot nu toe die een array bijwerken maken een nieuwe verzameling cellen zonder rekening te houden met een oude "generatie" waar ze van af zouden kunnen hangen. Game of Life van Conway, daarentegen, volgt een verzameling cellen door de ene generatie te *veranderen* in de volgende.

Om te zien waarom `copy(a)` een essentiële hulpfunctie is voor dit proces, kan je de volgende commando's proberen:

```ipython
In [1]: a = inner_cells(5, 5)  # maak een bord van 5 bij 5 met inner_cells

In [2]: print_board(a)         # pijltje omhoog
00000
01110
01110
01110
00000

In [3]: new_a = a              # maakt een oneigenlijke ("shallow" of "ondiepe") kopie

In [4]: print_board(new_a)     # pijlte omhoog en aanpassen... ZIET er hetzelfde uit...!
00000
01110
01110
01110
00000

In [5]: a[2][2] = 5            # zet het midden van de oude a op 5

In [6]: print_board(a)         # er is een 5 in het midden...
00000
01110
01510
01110
00000

In [7]: print_board(new_a)     # merk op dat new_a ook veranderd is; aargh!
00000
01110
01510
01110
00000
```

Hier hebben we een ondiepe "kopie" (of *shallow copy*) van `a` gemaakt, en die shallow copy `new_a` genoemd.

`new_a` is echter alleen maar een kopie van de *verwijzing* naar de originele elementen van `a`!

Het gevolg hiervan is dat als de elementen van `a` veranderen, de elementen van `new_a` ook veranderen, ondanks dat we die nooit rechtstreeks hebben aangepast!

Het voorbeeld hierboven laat ***shallow*** copying zien: het kopiëren van een *verwijzing* naar de elementen, niet het maken van een volledige *kopie* van alle elementen.

Een volledige kopie van alle elementen maken heet **diep** kopiëren of *deep copying*.

## `copy(a)`, een "deep" copier, schrijven...

Begin met deze code:

```python
def copy(a):
    """Returns a DEEP copy of the 2D array a."""
    height = len(a)
    width = len(a[0])
    new_a = create_board(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            # welke enkele regel moet hier staan om elk element van a
            # naar het corresponderende element van new_a te kopiëren?
            ...

    return new_a
```

en maak de implementatie af om een functie genaamd `copy(a)` te maken, die een **deep** copy van de tweedimensionale array `a` maakt.

Je hoeft je zoals gebruikelijk geen zorgen te maken over de buitenrand: die blijft altijd `0`. De lussen lopen alleen over de cellen die niet op de rand liggen.

`copy` krijgt dus een tweedimensionale array `a` als invoer. En `copy` geeft een helemaal nieuwe tweedimensionale array terug waarvan de elementen hetzelfde patroon vormen als in de originele array.

Je kan controleren dat je functie `copy` goed werkt met dit voorbeeld:

```ipython
In [1]: a = inner_cells(5, 5)  # maak een bord van 5 bij 5 met inner_cells bord

In [2]: print_board(a)         # pijltje omhoog
00000
01110
01110
01110
00000

In [3]: new_a = copy(a)

In [4]: print_board(new_a)
00000
01110
01110
01110
00000

In [5]: a[2][2] = 5

In [6]: print_board(a)     # deze is veranderd!
00000
01110
01510
01110
00000

In [7]: print_board(new_a)  # NIET veranderd!
00000
01110
01110
01110
00000
```

Deze keer wordt `new_a` ***niet*** veranderd ondanks dat `a` wel veranderd is: het is een echte, "diepe" kopie.

:::{admonition} de ingebouwde `deepcopy` van Python
:class: notice

Je functie `copy` geeft een deep copy terug van haar invoer. Dit is handig genoeg om ingebouwd te zijn in Python. Om deze ingebouwde functie te gebruiken, kan je dit uitvoeren:

```python
from copy import deepcopy

new_a = deepcopy(a)
```

Nu heb je gezien hoe dit geïmplementeerd wordt: elementsgewijs! Voel je vrij om te kiezen welke
van de twee je wilt gebruiken.
:::

### De functie `inner_reverse`

Kopiëren is een simpele manier om een nieuwe "generatie" array-elementen te maken die kan afhangen van een vorige generatie.

Nu ga je een functie schrijven die een generatie cellen *verandert* in een nieuwe generatie.

Om dit te doen, schrijf je een functie `inner_reverse(a)` die een oude tweedimensionale array `a` (een oude "generatie") meekrijgt en dan een nieuwe generatie `new_a` met dezelfde afmetingen maakt, met behulp van `create_board` of `copy`.

Bij `inner_reverse` moet de nieuwe generatie echter overal het "tegenovergesteld" van de cellen van `a` zijn, behalve aan de buitenrand.

Net zoals bij `inner_cells` moet je ervoor zorgen dat de cellen in de buitenrand van de nieuwe generatie altijd allemaal `0` zijn.

Voor cellen aan de binnenkant; dus niet op de rand; waar `a[row][col]` een `1` is, moet de waarde in de nieuwe array een `0` zijn en omgekeerd.

:::{admonition} Maak gebruik van `copy`
:class: tip

Je kan de functie `copy(a)` kopiëren en plakken, en dan een toepasselijke `if/else` toevoegen.
:::

Probeer je functie `inner_reverse` door een voorbeeld te laten zien. Dit voorbeeld gebruikt `random_cells`:

```ipython
In [1]: a = random_cells(8, 8)

In [2]: print_board(a)
00000000
01011010
00110010
00000010
01111110
00101010
01111010
00000000

In [3]: a2 = inner_reverse(a)

In [4]: print_board(a2)
00000000
00100100
01001100
01111100
00000000
01010100
00000100
00000000
```

:::{admonition} Terzijde
:class: notice

Je zou kunnen beargumenteren dat het mogelijk is om gewoon het oude argument `a` aan te passen, in plaats van het aanmaken en teruggeven van een nieuwe array; dit is wel waar voor het omdraaien van een patroon met array-elementen, maar het is *niet* waar als we de regels voor Game of Life van Conway gaan implementeren. In dat geval zou het aanpassen van cellen zonder te kopiëren het aantal buren van andere cellen veranderen!
:::

## Stap 4: Game of Life van John Conway

In deze stap maak je twee functies:

* `count_neighbours(row, col, a)` en
* `next_life_generation(a)`

### De functie `count_neighbours`

Het is handig om een hulpfunctie `count_neighbours(row, col, a)` te schrijven, die *het aantal levende buren* van een cel in het bord `a` op een gegeven `row` en `col` teruggeeft.

Er zijn twee mogelijke oplossingsrichtingen voor `count_neighbours`:

1. Schrijf *kleine* for-lussen die de negen cells gecentreerd **op `a[row][col]`** bekijken. Je zal dan het centrum toevoegen. Dit is geen probleem, mits je het weer van het resultaat *aftrekt* voordat je dat teruggeeft!
2. **OF** schrijf acht `if`-statements om alle acht mogelijke buren te bekijken... Merk hierbij op dat je ze ALLE acht wilt uitvoeren; gebruik dus `if` voor ze allemaal; gebruik geen `elif`: die is te "exclusief" 🙂

Definieer of plak deze 5-bij-5-array `a` en controleer daarna de aantallen
buren van een paar cellen, om te testen of `count_neighbours` werkt:

```ipython
In [1]: run wk9ex1

In [2]: a = [[0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0]]

In [3]: print_board(a)
00000
00100
00100
00100
00000

In [4]: count_neighbours(2, 1, a)
Out[4]: 3                # Klopt! Er zijn hier 3 levende buren

In [5]: count_neighbours(2, 2, a)
Out[5]: 2                # Vergeet niet de cel zelf niet te tellen!

In [6]: count_neighbours(0, 1, a)
Out[6]: 1
```

### De functie `next_life_generation(a)`

Je schrijft ten slotte `next_life_generation`, die de regels van Game of Life implementeert.

:::{admonition} `inner_reverse`
:class: tip

Deze functie zal het meeste lijken op `inner_reverse`, dus die kan je als sjabloon gebruiken.
:::

Hier is een beginsignature voor `next_life_generation`:

```python
def next_life_generation(a):
    """Makes a copy of a and then advances one
       generation of Conway's Game of Life within
       the *inner cells* of that copy.
       The outer edge always stays at 0.
    """
```

Deze functie `next_life_generation` moet een tweedimensionale array `a` meekrijgen, die de "oude" generatie cellen voorstelt, en moet een *nieuwe generatie* cellen teruggeven, die ieder `0` of `1` zijn, gebaseerd op de regels voor *Game of Life* van John Conway:

1. Vergeet niet de nieuwe generatie `new_a` te maken met dezelfde afmetingen als de oude generatie `a`.
2. Alle randcelen blijven nul (`0`), zoals gebruikelijk (maar zie de extra uitdagingen, hieronder).
3. Een cel met minder dan twee levende buren sterft (vanwege eenzaamheid).
4. Een cel met meer dan 3 levende buren sterft (vanwege overbevolking).
5. Een cel die dood is en precies 3 levende buren heeft wordt weer levend.
6. Alle andere cellen behouden hun huidige staat (en krijgen dus de waarde van de bijbehorende oude cel).

Om dit iets concreter te maken noemen we de nieuwe generatie cellen die je teruggeeft `new_a` om deze te onderscheiden van `a`.

:::{admonition} De buitenrand moet `0` blijven
:class: notice

Zoals benoemd bij `inner_reverse` moet je alle cellen in de buitenrand altijd leeg houden!** Dit is simpelweg een kwestie van het beperken van je lussen tot een geschikt bereik. Dit maakt echter de bijwerkingsregels hierboven een stuk makkelijker, omdat het betekent dat je altijd alleen de cellen aan de binnenkant bewerkt, die allemaal ***een volledige verzameling van acht buren hebben zonder dat je de grenzen overschrijdt.***
:::

:::{admonition} Waarschuwingen/tips
:class: tip

Er zijn een paar zaken die je in je achterhoofd moet houden:

* Tel alleen buren in de oude generatie `a`. Verander alleen de nieuwe generatie, `new_a`.
* Onthoud dat je *elke* waarde in `new_a` (de nieuwe elementen) moet instellen, ook als deze hetzelfde is als in `a`.
* Een cel is **GEEN** buur van zichzelf.
* Een vierkant van 2 bij 2 cellen is stabiel en zal niet veranderen (als dit geïsoleerd is); je kan dit op een klein raster proberen om het te testen.
* Een lijn van 3 bij 1 cellen zal afwisselend horizontaal en verticaal zijn (als deze geisoleerd is); dit is ook een goed patroon om te testen.
:::

Hier is een aantal tests die je kan proberen gebaseerd op de laatste suggestie in de bovenstaande lijst:

```ipython
In [1]: a = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]  # vertical bar

In [2]: print_board(a)
00000
00100
00100
00100
00000

In [3]: a2 = next_life_generation(a)

In [4]: print_board(a2)
00000
00000
01110
00000
00000

In [5]: a3 = next_life_generation(a2)

In [6]: print_board(a3)
00000
00100
00100
00100
00000
```

enzovoorts.

Als je Game of Life werkt, kan je wat andere gangbare patronen vinden, dat wil zeggen, andere onveranderlijke stabiele vormen ("stenen"), herhalende patronen ("planten"), maar ook andere patronen die over het scherm bewegen, ook wel bekend als gliders ("dieren" of "vogels").

## Stap 5: Grafisch leven!

Als je code voor `next_life_generation` werkt, kan je het bestand `wk9ex1_graphics.py` uitvoeren; daarvoor kan je deze code gebruiken:

```text
run wk9ex1_graphics.py
```

:::{admonition} Waarschuwing
:class: warning

Als dit niet werkt, moet je `ipython` opnieuw opstarten. Dit lost het probleem meestal op. Het bestand `wk9ex1_graphics.py` probeert je functie `next_life_generation` te laden; soms werkt de interactie tussen deze twee bestanden niet helemaal.
:::

Dit bestand doet een paar aannemes:

* Het bestand `wk9ex1.py` bevindt zich in dezelfde directory
* Je hebt `next_life_generation` correct geschreven in dat bestand (met de naam `wk9ex1.py`)

Soms moet je `start()` twee keer aanroepen, als het een foutmelding geeft:

```python
start()
```

Nadat je het gestart hebt, zou je een venster met een Game-of-Life-omgeving van 20 bij 20 willekeurige cellen moeten zien. Het zou ook zijn opties moeten afdrukken:

```
    PAUZE: 'p'
 DOORGAAN: 'Return'/'Enter'
   WISSEN: 'Spatie'
  SLUITEN: 'Esc'
```

Vergeet niet op het venster te klikken zodat het de focus krijgt.

Als je op Enter drukt, zal het programma je functie `next_life_generation` herhaaldelijk aanroepen om naar de volgende generatie te gaan.

Om de simulatie te pauseren, klik je op het venster en druk je op de `P`-toets.

Als de simulatie gepauseerd is, kan je de toestand van cellen veranderen door er in te klikken...

Om de simulatie verder te laten gaan, druk je op de `Enter`-toets (met de focus in het venster).

Je kan het venster sluiten op de gebruikelijke manier, door op het kruisje in de hoek te klikken, of door op de Escape-toets (Esc) te drukken met de focus in het Life-venster.

### Kleurrijk leven!

Je kan de kleuren die gebruikt worden om `0` en `1` weer te geven veranderen door middel van de gegeven functie `set_color`. Je kan bijvoorbeeld deze code gebruiken vanaf de prompt die je krijgt na het laden van het bestand `wk9ex1_graphics.py`:

```
In [1]: set_color(0, "white")

In [2]: set_color(1, "orange")

In [3]: start()
```

om het kleurschema van de Hanzehogeschool te gebruiken. De [lijst met kleuren](https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm) is erg uitgebreid, laat je creativiteit de vrije loop!

### Maximaal leven...

Vereist meer dan alleen programmeren, helaas! (Alhoewel Python vond dat `werken` maximaal leven was!)

Als je Game of Life vrolijk "leeft", dan heb je het practicum voltooid. We hopen dat je het
leven nu in een ander licht ziet, of dat het in ieder geval levendig geweest is... Vergeet niet je
bestand `wk9ex1.py` in te leveren in Gradescope!

## Optionele variaties op Game of Life

Dat gezegd hebbende, er is altijd meer!

Als je wilt, kan je proberen een variatie op Game of Life te implementeren:

### De donut

Voor deze variatie moet je de lege rand cellen om het bord weghalen. In dit geval moet het bord de vorm van een donut hebben: de linker- en rechterranden van het bord worden buren, en de boven- en onderranden ook. Dit maakt het tellen van het aantal buren en het bewaken van de grenswaardes lastiger. Met één enkele functie om de "echte" locatie op het bord van een gegeven `row` en `col` op te zoeken valt het wel mee...

### Buitenaards leven

Game of Life wordt gezien als een cellulaire automaat van het type 23/3, omdat cellen overleven met 2 of 3 buren (de cijfers voor de streep) en geboren worden met 3 buren (het cijfer na de streep). Veel van de (misschien zelfs alle) andere overlevings/geboortemogelijkheden zijn ook bestudeerd. Sommige hebben zelfs namen: 1358/357 heet bijvoorbeeld "Amoeba" en 1/1 heet "Gnarl". Kies voor deze variatie op het spel andere regels voor overleven en geboren worden, misschien uit [deze lijst van varianten](http://en.wikipedia.org/wiki/Life-like_cellular_automaton) en implementeer een toets die tussen Game of Life van John Conway en je eigen gekozen regels wisselt (en een andere toets om terug te gaan...)


### Meer soorten cellen

Je kan ook regels bedenken die meer dan twee soorten cellen toestaan. Je kan ook kleuren instellen voor maximaal 8 soorten cellen, genummerd van 0 tot en met 7.

---
title: Fijne functies
csa-level: 2
---

# Fijne functies

```{include} ../class/problems/fijne_functies.md
```

In deze opgave ga je oefenen met het schrijven van functies (de fundamentele bouwstenen van software) en het toepassen van onder andere string- en lijstbewerkingen.

## Ingebouwde functies

Je gaat eerst een aantal van de vele *ingebouwde* Python functies proberen.

### `range`

`range` geeft een *iterator* met integers terug. Het maakt niet uit als je niet precies weet wat een iterator is, het belangrijkst is dat je ziet dat `list` de iterator omzet naar een *lijst* met integers:

```ipython
In [1]: list(range(0, 100))
Out[1]: [0, 1, 2, ..., 99]
```

:::{admonition} Tot het eind!
:class: info

Let op dat `range`, zoals bij vrijwel alles in Python, *tot* het eindpunt telt (en niet tot *en met*)!
:::

### `sum`

`sum` telt een lijst van getallen op, en `range` maakt een lijst met integers (of eigenlijk een iterator met integers, maar daar kan `sum` ook mee overweg):

```ipython
In [2]: sum(range(3, 11))
Out[2]: 52
```

Een omslachtige manier om `40 + 2` uit te rekenen:

```ipython
In [3]: sum([40, 2])
Out[3]: 42
```

### `help`

`help` is handig, gebruik het als je vastzit!

```ipython
In [4]: help(sum)
# (een uitleg van sum)
```

Afhankelijk van jouw besturingssyteem zal je misschien op **`q`** moeten drukken om *help* te verlaten.

```ipython
In [5]: import math
```

Je zal `math` eerst moeten `import`eren, anders krijg je een fout!

```ipython
In [6]: dir(math)
# (Alle functies in de module math...)

In [7]: dir(__builtins__)
# (een grote lijst van alle ingebouwde functies)
```

De functie `dir` is vaak handig, het laat alles zien wat zich in een specifieke Python *module* bevindt. Zo bevat de speciale module `__builtins__` alle *ingebouwde* functies.

:::{admonition} Dubbele underscores
:class: info

Let op dat je twee *underscores* typt bij `__builitins__`, zowel voor als na de kleine letters, de underscore `_` is Shift-minteken op de meeste toetsenborden.
:::

Als je goed kijkt naar de grote lijst die `dir(__builtins__)` teruggeeft zul je de functie `sum` vinden die je net hebt gebruikt. Je zal echter ook een aantal andere belangrijke functies *niet* tegenkomen, bijvoorbeeld `sin` of `cos` of `sqrt`. Deze functies (en vele anderen) kan je vinden in de module `math`. Er zijn in Python veel modules met functies beschikbaar die je direct kan gebruiken, en nog veel meer die je kan downloaden.

## Meer importeren

Om functies te gebruiken die niet standaard ingebouwd zijn moet je de module waar ze in voorkomen importeren. Probeer de volgende voorbeelden om kennis te maken met hoe je de vele Python modules kan gebruiken:

1.  Je kan een module importeren, en dan alle functies gebruiken via de modulenaam:

    ```ipython
    In [1]: import math
    # (Python geeft hier geen antwoord)

    In [2]: math.sqrt(9)
    Out[2]: 3.0
    ```

    Merk op dat `sqrt` een `float` teruggeeft zelfs als het argument een `int` is.

    ```ipython
    In [3]: math.cos(3.14159)
    Out[3]: -0.999...
    ```

    Merk op dat het argument dat `cos` en vrienden als argument accepteert in radialen is. Bovendien is 3.14159 iets minder dan de constante `math.pi`.

2. Als je niet overal `math.` voor wilt typen dan kan je dit voorkomen met:

    ```ipython
    In [1]: from math import *
    # (Python geeft hier geen antwoord)
    ```

    Sterretje `*` betekent hier "alles" en importeert alle functies en constanten uit de module `math` zodat ze in de huidige omgeving kunnen worden gebruikt, je hoeft er nu geen `math.` meer voor te zetten!

    ```ipython
    In [2]: cos(pi)
    Out[2]: -1.0
    ```

    Zonder `from math import *` zou je in dit geval `math.cos(math.pi)` moeten hebben geschreven.

    :::{admonition} import *
    :class: warning

    Het is niet *altijd* een goed idee om dit te doen, zeker niet als je veel modules gebruikt. Sommige modules kunnen dezelfde functienaam gebruiken en in dat geval zal de ene import de andere vervangen ...
    :::

## Een nieuw bestand

Functies zijn de fundamentele bouwstenen van programmeren. Wat Python onderscheidt van andere programmeertalen is het gemak waarmee je eigen functies kan maken!

Kopieer het volgende commentaar en de definitie van een functie met de naam `dbl` naar jouw bestand:

```python
def dbl(x):
    """Returns twice the argument

    Spam is great, and dbl("spam") is better!

    :param x: The value to double
    :type x: int, float or string
    :rtype: int, float or string
    """
    return 2 * x
```

### Uitvoeren

Als je dit bestand op de gebruikelijke manier uitvoert zie je dat niets gebreurt!:

```ipython
In[1]: run wk2ex2.py
```

De net gemaakte functie `dbl` is nu echter wel beschikbaar, probeer deze nu te *gebruiken*:

```ipython
In [2]: dbl(21)
Out[2]: 42

In [3]: dbl('wauw! ')
Out[3]: 'wauw! wauw! '
```

## Signature en docstring

De eerste regel van een functie wordt de *signature* genoemd. De signature van een functie bevat het keyword `def` (een afkorting van "define"), de naam van de functie, en een lijst met argumenten voor de functie tussen haakjes. Let op de *dubbele punt* waar de signature mee wordt afgesloten.

Direct onder de signature staat een string tussen drie dubbele aanhalingstekens `"""`, dit heet een *docstring* (een afkorting van "documentation string"). We verwachten dat je in al je functies een docstring schrijft, zelfs in eenvoudige functies zoals `dbl` zodat dit een gewoonte voor jou wordt.

Een docstring moet de argumenten van de functie en het resultaat (de returnwaarde) beschrijven. Zoals je hierboven ziet kan je ook andere belangrijke informatie toevoegen. Docstring zijn de manier waarop *jouw* functies onderdeel worden van het ingebouwde hulpsysteem van Python.

Om dit te zien, kan je dit typen:

```ipython
In [2]: help(dbl)
```

Je zal zien dat Python de docstring als hulp teruggeeft! Het hulpsysteem van de taal is gebouwd op docstrings! Deze manier van zelfdocumentatie in Python is belangrijk om jouw functies inzichtelijk te maken, zowel voor anderen als voor jezelf.

:::{admonition} Inspringen (indentatie)
:class: warning

De eerste driedubbele aanhalingstekens *moeten* ingesprongen worden direct onder de signatuur. De afsluitende driedubbele aanhalingstekens van de docstring springen op hetzelfde niveau en an alle volgende code binnen de functie (de functie "body").
:::

## Voorbeeldopgave

Laten we beginnen met functies schrijven! Vergeet niet voor elk van deze functies een docstring toe te voegen die beschrijft wat je functie *doet* en wat de *argumenten* zijn. Zie het voorbeeld `tpl` hieronder voor hoe je dit kan doen, deze lijkt heel erg op `dbl` die je al eerder hebt gezien:

Schrijf de functie `tpl(x)` die een getal als argument accepteert en drie keer de waarde van dat argument teruggeeft.

### Uitwerking

Kopieer de volgende oplossing (nadat je een paar regels nieuwe regels hebt toegevoegd om de leesbaarheid te verbeteren) naar jouw bestand:

```python
def tpl(x):
    """Returns thrice the argument

    :param x: The value to triple
    :type x: int, float or string
    :rtype: int, float or string
    """
    return 3 * x
```

## Opgaven

Als in de opgaven wordt gesproken over een *getal*, neem dan aan dat dit een integer of een float mag zijn, in alle andere gevallen zal duidelijk worden worden gezegd welk type moet worden gebruikt.

### `sq(x)`

Schrijf de functie `sq(x)` die een getal `x` als argument accepteert en het *kwadraat* van het argument als resultaat teruggeeft. (Het kwadraat van `x` is `x` keer zichzelf...)

### `interp(low, hi, fraction)`

Schrijf de functie `interp(low, hi, fraction)` die de getallen `low`, `hi` en `fraction` als argumenten accepteert en een floating point getal teruggeeft.

`fraction` staat voor een *fractie*, een deel van een geheel dat van een laagste waarde `low` naar een hoogste waarde `hi` loopt. Bijvoorbeeld, in het geval van een taart zou dit van waarde 0 (geen taart) naar 2 (twee, hmmm!) kunnen lopen, waar fractie 0.75 gelijk staat aan 1.5 (anderhalve taart, ook fijn).

Wat hier uit volgt is dat als `fraction` 0 is `low` moet worden teruggegeven. Als `fraction` 1 is zal `hi` moeten worden teruggegeven. Waarden voor `fraction` tussen `0` en `1` geven resultaten tussen `low` en `hi`.

Sterker nog, `fraction` kan een waarde onder 0 krijgen en het resultaat zal dan kleiner zijn dan `low`. Ook kan `fraction` een waarde boven `1` krijgen, en het resultaat zal dan groter zijn dan `hi` (puristen zouden dit waarschijnlijk `extrap`olatie in plaats van `interp`olatie, noemen).

Nu het probleem bekend is zal je misschien geneigd zijn de functie op te delen in een aantal condities en `if`, `elif` en dergelijke proberen te gebruiken. Je kan deze functie echter schrijven *zonder* conditionele statements (`if`, `elif`, `else`)! Probeer de functie te schrijven *zonder* `if` te gebruiken!

Hier zijn een paar voorbeelden om te verduidelijken hoe `interp` zal moeten werken:

```ipython
In [1]: interp(1.0, 9.0, 0.25)  # Een kwart (.25) op weg van 1.0 naar 9.0
Out[1]: 3.0

In [2]: interp(1.0, 3.0, 0.25)  # Een kwart op weg van 1.0 naar 3.0
Out[2]: 1.5

In [3]: interp(2, 12, 0.22)     # 22% op weg van 2 naar 12
Out[3]: 4.2
```

:::{admonition} Tip
:class: tip


Als je niet zeker weet hoe je moet beginnen, kan je naar het eerste voorbeeld hierboven kijken. Hierbij geldt dat

```text
low is 1.0
hi is 9.0
fraction is 0.25
```

Kijk of je kan bepalen hoe je deze drie waarden moet combineren om tot de correcte returnwaarde 3.0 te komen. Je zou kunnen beginnen met `(hi - low)` ...
:::

Hier zijn nog twee andere voorbeelden die je kan proberen:

```ipython
In [1]: interp(24, 42, 0)       # 0% op weg van 24 naar 42
Out[1]: 24.0

In [2]: interp(102, 117, -4.0)  # -400% op weg van 102 naar 117 (vreemd!)
Out[2]: 42.0
```

In de volgende functies ga je strings gebruiken, reeksen van karakters. Schrijf ze allemaal in jouw bestand. Test elke functie die je hebt geschreven *voordat* je doorgaat naar de volgende. Zorg er ook voor dat je voor elke functie een docstring toevoegt die (heel kort) vertelt wat deze doet.

### `checkend(s)`

Schrijf een functie `checkend(s)` die als parameter een string `s` accepteert en `True` teruggeeft als het eerste karakter van `s` gelijk is aan het laatste karakter van `s`. Anders zal het `False` teruggeven. De functie `checkends` hoeft niet te werken met een lege string `s` (een string met waarde `""`).

:::{admonition} boolean waarden
:class: warning

De functie moet *geen* strings teruggeven! In plaats daarvan moet het een *boolean* teruggeven, dus `True` of `False`, zonder aanhalingstekens.

In de editor zul je zien dat booleans een andere kleur krijgen (in het standaardkleurenschema van VSCode worden ze blauw) om aan te geven dat Python ze herkent als waarden van het type `bool`. Als je er per ongeluk strings van hebt gemaakt (`"True"` in plaats van `True`) dan worden ze oranje in VSCode.

Voor alle duidelijkheid, booleans en strings zijn twee heel     verschillende dingen! Voor `True` en `False` heb je vrijwel altijd de booleans, dus zonder aanhalingstekens, nodig.
:::

We geven straks een aantal tips, maar bekijk eerst de volgende voorbeelden. Deze voorbeelden leggen uit hoe `checkends` werkt en vergeet niet ze te proberen als je een eerste versie van de functie geschreven hebt. Merk op dat het laatste, vierde voorbeeld hieronder de
string met *een enkele spatie* is, dat is niet hetzelfde als de lege string, die bevat geen karakters:

```ipython
In [1]: checkends('niet gelijk')
Out[1]: False

In [2]: checkends('kijk! wel gelijk')
Out[2]: True

In [3]: checkends('q')
Out[3]: True

In [4]: checkends(' ')
Out[4]: True
```

Zorg dat het laatste voorbeeld (de string met een enkele spatie) ook werkt in jouw functie. Zoals eerder gezegd, een lege string hoeft *niet* te werken.

:::{admonition} Vergelijken
:class: tip

Je kan in deze functie gebruikmaken van een `if`-`else`-constructie, hier is een begin:

```python
if s[0] == ...:
    return True
else:
    return False
```

Misschien kan je een oplossing vinden die helemaal geen `if` en `else` gebruikt, dit is ook goed!

De vergelijking `x == 42` is een expressie waar `True` of `False` uitkomt.
:::

### `flipside(s)`

Schrijf een functie `flipside(s)` die als arument een string `s` accepteert en een string teruggeeft waarvan de eerste helft de
tweede helft van `s` is en de tweede helft de eerste helft van `s`. De functie zal argument `s` dus *gespiegeld* teruggeven.

Als `len(s)` (de lengte van `s`) oneven is, dan geldt dat *eerste helft* van `s` één karakter korter is dan de tweede helft. De tweede helft van de string die teruggegeven wordt zal in dit geval één karakter korter zijn dan de eerste helft. Na de onderstaande voorbeelden kan je ook een tip vinden.

:::{admonition} Lengte bepalen
:class: info

Het kan hier handig zijn de ingebouwde functie `len(s)` te gebruiken, die de lengte van het argument, een string `s`, teruggeeft. De functie `len` kan je ook gebruiken voor andere typen, bijvoorbeeld lijsten (lists).
:::

Voorbeelden:

```ipython
In [1]: flipside('huiswerk')
Out[1]: werkhuis

In [2]: flipside('zijkant')
Out[2]: kantzij
```

:::{admonition} Integerdeling
:class: tip

Deze functie is eenvoudiger als je op de eerste regel een variabele maakt die gelijk is aan `len(s) // 2`, bijvoorbeeld,

```python
def flipside(s):
    """Put your docstring here
    """
    x = len(s) // 2

    return ...
```

`//` staat voor een *integer deling*, zie hoe dit anders is dan een gewone `/` deling:

```ipython
In [1]: 3 / 2
Out[1]: 1.5

In [2]: 3 // 2
Out[2]: 1
```

De oplossing en het return statement moet je natuurlijk verder aanvullen. Je zal de variabele `x` *twee keer* gaan gebruiken, daarom is het handig is om deze waarde een naam te geven, in plaats van het twee keer `len(s) // 2` te typen.

Terzijde, de naam `x` is hier slecht gekozen, `l` (voor "lengte") zou beter zijn geweest. We hebben echter `l` niet gebruikt omdat het te veel lijkt op het nummer `1`. Welke naam zou beter kunnen zijn dan `x`? Bedenk dat Python namen met meerdere letters ondersteunt, en dat de naam `len` al in gebruik is!
:::

### `convert_from_seconds(s)`

Schrijf een functie `convert_from_seconds(s)` die als argumment een (niet negatieve) integer `s` accepteert en een lijst met *vier* (niet negatieve) integers teruggeeft die het aantal seconden in een meer gebruikelijke vorm beschrijft, zodat:

- het eerste element het *aantal dagen* bevat
- het tweede element het *aantal uren* bevat
- het derde element het *aantal minuten* bevat
- het laatste element het *aantal seconden* bevat

Je zal op het volgende moeten letten:

- 0 ≤ seconden < 60
- 0 ≤ minuten < 60
- 0 ≤ uren < 24

Er is geen limiet op het aantal dagen. Een paar voorbeelden:

```ipython
In [1]: convert_from_seconds(610)
Out[1]: [0, 0, 10, 10]

In [2]: convert_from_seconds(100000)
Out[2]: [1, 3, 46, 40]
```

Hoe te beginnen? Je kan de volgende code (die *vier* variabelen telt) als begin gebruiken:

```python
def convert_from_seconds(s):
    """Put your docstring here
    """
    days = s // (24 * 60 * 60)  # Het aantal dagen
    s = s % (24 * 60 * 60)  # Het restant
    hours = ...
    minutes = ...
    seconds = ...
    return [days, hours, minutes, seconds]
```

De gedachte hier is dat wanneer je de vier variabelen (`days`, `hours`, `minutes` en `seconds`) klaarzet ze in één keer als lijst kunnnen worden teruggeven, wat in de laatste regel gebeurt:

```python
return [days, hours, minutes, seconds]
```

De regel die het aantal dagen berekent is:

```python
days = s // (24 * 60 * 60)
```

Het is nu aan jou om te bedenken wat de regels voor `hours`, `minutes` en `seconds` moeten zijn!

Je ziet in de bovenstaande code dat `s` op een gegeven moment een andere waarde aanneemt (het resultaat van een modulo `%` berekening). Het is mogelijk dit probleem op te lossen zonder de variabele `s` te veranderen, maar het al gaande wijzigen van `s` is een elegante en handige oplossingsstrategie om stap voor stap tot de waarde van de vier variabelen te komen. Probeer deze strategie in de bovenstaande code verder toe te passen.

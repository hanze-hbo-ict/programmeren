# List Comprehensions


## Voorbereiding

Download [Python sounds](https://github.com/hanze-hbo-ict/programmeren/raw/master/problems/assets/wk4ex1.zip).

Dit bestand moet ergens uitgepakt worden. Het bevat een aantal bestanden die allemaal in **dezelfde map** moeten staan:

- `wk4ex1.py`  (het bestand dat je gaat uitvoeren!)
- `swfaith.wav`
- `swnotry.wav`
- `spam.wav`
- `audio.py`

### Werk vanuit deze directory!

Je moet deze week vanuit de directory `wk4ex1` werken, je zal hiervoor moeten `cd`'en naar de map `wk4ex1`. Houd alle bestanden in `wk4ex1` bij elkaar, als je het bestand `wk4ex1.py` verplaatst zonder de andere bestanden werkt het **niet**!

## Opdracht 1

Je gaat een aantal functies schrijven met behulp van list comprehensions. List comprehensions zijn een flexibele manier om een functie (of handeling, bijvoorbeeld een berekening) uit te voeren (te "mappen") op alle elementen van een lijst.

**a.** Bekijk de functie `three_ize` vrijwel aan het begin van `wk4ex1.py`:

```python
def three_ize(L):
    """three_ize is a function that accepts a list and
       returns a list of elements each three times as large.
    """
    # lc, een voorbeeld van een list comprehension
    lc = [3 * x for x in L]
    return lc
```

Deze functie voert de berekening `3 * x` uit op de waarden `x` in de lijst `L`. Probeer het uit met dit voorbeeld:

```ipython
In [1]: three_ize([13, 14, 15])
Out[1]: [39, 42, 45]
```



**b.** Gebruik de bovenstaande functie `three_ize` als voorbeeld om de functie `scale` te schrijven met onderstaande *signature*:

```python
def scale(L, scale_factor):
    ...
```

Deze functie geeft een lijst terug die vergelijkbaar is met `L`, behalve dat elk element is vermenigvuldigd met `scale_factor`. Maak gebruik van list comprehensions! Een voorbeeld:

```ipython
In [1]: scale([70, 80, 420], 0.1)
Out[1]: [7.0, 8.0, 42.0]
```

## Opdracht 2

De volgende stap is het schrijven van een functie `three_ize_by_index` met list comprehensions waar je gebruik gaat maken van de *index* (of positie) van elementen in een lijst.

**a** Controleer dat de onderstaande functie `three_ize_by_index` in jouw bestand `wk4ex1.py` aanwezig is.

```python
def three_ize_by_index(L):
    """three_ize_by_index has the same behavior as three_ize
       but it uses the INDEX of each element, instead of
       using the elements themselves -- this is much more flexible!
    """
    # nog een voorbeeld van een list comprehension
    n = len(L)
    lc = [3 * L[i] for i in range(n)]
    return lc
```

Deze functie doet *exact hetzelfde* als `three_ize`, maar gebruikt nu de *index* van elk element. Dat wil zeggen, nu is het de **locatie** van elk element in een lijst, we noemen deze hier `i`, die steeds verandert.

Het gebruik van een index maakt list comprehensions nog flexibeler dan wanneer we de elementen rechtstreeks gebruiken, zoals we gaan zien in de volgende opdrachten.

**b** : `add_2`

Gebruik de bovenstaande functie gebaseerd op *index* als richtlijn om de functie `add_2(L, m)` te schrijven met onderstaande signature:

```python
def add_2(L, m):
    ...
```

Deze functie krijgt twee lijsten `L` en `m` mee en geeft een enkele lijst terug die de elementen van de twee lijsten elementsgewijs bij elkaar optelt. Als de twee lijsten een andere lengte hebben, moet `add_2` een lijst teruggeven die even lang is als de *kortste* van de twee. Je kan de extra elementen van de langere lijst negeren.

Je kan dit bijvoorbeeld doen door `min`, `len(L)` en `len(m)` te combineren. Als voorbeeld zal de regel

```python
n = min(len(L), len(m))
```

de kleinste van de lengtes van `L` en `m` aan `n` toekennen.

Het is handig om hier een aanpak gebaseerd op *index* te gebruiken. Je kan de functie `three_ize_by_index` als voorbeeld gebruiken. Bekijk ook hoe je de onderstaande list comprehension hiervoor zou kunnen gebruiken:

```python
lc = [L[i] + m[i] for ...]
```

Hieronder zie je twee voorbeelden van het gebruik van `add_2`:

```ipython
In [1]: add_2([10, 11, 12], [20, 25, 30])
Out[1]: [30, 36, 42]

In [2]: add_2([10, 11], [20, 25, 30])
Out[2]: [30, 36]
```

**c** : `add_3`

Schrijf nu een vergelijkbare functie `add_3` met drie argumenten volgens de onderstaande signature:

```python
def add_3(L, m, p):
    ...
```

waar `L`, `m` en `p` lijsten zijn en `add_3` de som van de drie lijsten teruggeeft, maar met evenveel elementen als de *kortste* van de drie. De aanpak zal erg lijken op die voor `add_2`.

## Opdracht 3

Schrijf nu een functie `add_scale_2` met de onderstaande signature:

```python
def add_scale_2(L, m, L_scale, m_scale):
    ...
```

Deze functie krijgt twee lijsten `L` en `m` mee en twee floating-point getallen `L_scale` en `m_scale`. Deze staan respectievelijk voor *schaalfactor voor `L`* en *schaalfactor voor `m`*.

De functie `add_scale_2` moet een enkele lijst teruggeven die een elementsgewijze optelling is van de twee lijsten, maar *ieder vermenigvuldigd met zijn respectievelijke floating-point getallen*. Als de lijsten niet dezelfde lengte hebben, moet de functie een lijst met de lengte van de *kortste* lijst teruggeven. Je kan extra elementen negeren.

Hier zie je twee voorbeelden:

```ipython
In [1]: add_scale_2([10, 20, 30], [7, 8, 9], 0.1, 10)
Out[1]: [71.0, 82.0, 93.0]

In [2]: add_scale_2([10, 20, 30], [7, 8], 0.1, 10)
Out[2]: [71.0, 82.0]
```

Dit zal nogal lijken op de vorige opdrachten!

## Opdracht 4

**a** Bekijk deze hulpfunctie in het bestand `wk4ex1.py`:

```python
def randomize(x, chance_of_replacing):
    """randomize accepts an original value, x
       and a fraction named chance_of_replacing.

       With the "chance_of_replacing" chance, it
       should return a random float from -32767 to 32767.

       Otherwise, it should return x (not replacing it).
    """
    r = random.uniform(0, 1)
    if r < chance_of_replacing:
        return random.uniform(-32768, 32767)
    else:
        return x
```

Lees de docstring en probeer de functie uit.

Het enige dat we hier van jou vragen is om te *begrijpen* wat deze functie doet: hoe vaak wordt de *oorspronkelijke* waarde teruggegeven en hoe vaak een *willekeurige* waarde. Deze willekeurige waarde valt binnen het bereik van de drukgolven van een geluid.

De functie geeft een willekeurige waarde terug, maar hier is een voorbeeld van een aantal keer dat de functie wordt uitgevoerd:

```ipython
In [1]: randomize(42, .5)
Out[1]: 42

In [2]: randomize(42, .5)
Out[2]: 42

In [3]: randomize(42, .5)
Out[3]: 29209.30669767395

In [4]: randomize(42, .5)
Out[4]: 42

In [5]: randomize(42, .5)
Out[5]: 17751.221299744262
```


**b** Schrijf nu een functie `replace_some` met de volgende signature:

```python
def replace_some(L, chance_of_replacing):
    ...
```

De functie krijgt een lijst `L` en een floating-point getal `chance_of_replacing` mee. `replace_some` moet onafhankelijk van elkaar elk element in L vervangen (of niet vervangen) door gebruik te maken van de hulpfunctie `randomize`.

:::{admonition} Gebruik `randomize`
:class: tip

Gebruik `randomize` in een list comprehension, meer hoef je niet te doen! Bedenk hoe je onderstaand statement kan aanvullen (en vergeet niet om `lc` terug te geven):

```python
lc = [randomize(..., ...) for x in L]
```
:::

Aangezien de functie willekeurig is, zal de uitvoer op jouw systeem niet gelijk zijn, maar probeer of het ongeveer als volgt werkt:

```ipython
In [1]: replace_some(range(40, 50), .5)  # vervang ongeveer de helft (hopelijk blijft de 42 staan!)
Out[1]: [40, 41, 42, -17461.09350529409, 44, -13989.513742241645, 46, -26247.774200304026, 48, 49]

In [2]: replace_some(range(20, 30), .1)  # vervang ongeveer een tiende (maar het is wel willekeurig: hier zijn er twee vervangen)
Out[2]: [20, 21, 16774.26240973895, 23, 24, 25, -18184.919872079583, 27, 28, 29]
```

Om je te helpen met testen zijn hier een paar `assert` statements om in je code over te nemen. Merk op dat de tweede assertion stelt dat het resultaat *ongelijk* is aan 42!

```python
assert replace_some(range(40, 50), 0) == list(range(40, 50))
assert replace_some([42], 1.0) != [42]
```

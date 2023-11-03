# Week 5

## Basis

### [Recursieve functies](/problems/basis/5_recursieve_functies)

#### Opdracht 1

Schrijf een functie `no_doubles(l)` die een lijst `l` accepteert, alle dubbele waarden verwijdert uit `l` en deze nieuwe lijst teruggeeft.

```python
def no_doubles(l):
    """ Haalt alle dubbele elementen uit lijst `l` en geeft de nieuwe lijst terug.
    """
    # Base case, de list is leeg.
    if len(l) == 0:
        return l

    if l[0] in l[1:]: # Het element is dubbel, ga door zonder dit element
        return no_doubles(l[1:])

    if type(l) == str:
        return l[0] + no_doubles(l[1:])
    else:
        return [l[0]] + no_doubles(l[1:])
        # Gebruik voor de list [l[0]] om de l[0] als list mee te geven. Doe je dit niet zo dan krijg je een som of foutmelding terug.

assert no_doubles("test") == "est", "De no_doubles() werkt niet goed met tekst."
assert no_doubles([1, 2, 3, 3, 4, 5]) == [1, 2, 3, 4, 5], "De no_doubles() werkt niet goed met een lijst van integers."
```

Omdat een string net wat anders werkt dan een lijst wordt met een `if`-statement gekeken of `l` een string is of een list voordat de functie recursief wordt aangeroepen met het niet dubbele element toe gevoegd aan de uiteindelijk return. Om dezelfde reden geeft het programma bij de base case `l` terug in plaats van een legen lijst of string. Door `l` terug te geven, wordt direct het juiste variable type terug gegeven. Verder maakt deze functie gebruik van principes die al eerder zijn langs gekomen.


#### Opdracht 2a

Schrijf een functie `intersect_sets(a, b)` die twee lijsten `a` en `b` binnen krijgt als parameters. De functie geeft een lijst terug met elementen die zowel in lijst `a` als in lijst `b` voorkomt.

```python
def intersect_sets(a, b):
    """ Geeft terug welke elementen in zowel lijst a als lijst b voorkomen.
    """
    # Base case
    if len(a) == 0:
        return []

    if a[0] in b: # Als a[0] voorkomt in b dan moeten we hem bewaren/meenemen.
        return [a[0]] + intersect_sets(a[1:], b)
    else: # Anders slaan we hem over.
        return intersect_sets(a[1:], b)

assert intersect_sets([1,2,3], [3,4,5]) == [3], "De intersect_sets() geeft een incorrecte lijst terug."
assert intersect_sets([1,2,3,4], [1,3,4,5]) == [1,3,4], "De intersect_sets() geeft een incorrecte lijst terug."
```

Hier werken we weer met lists dus kan de base case een lege list terug geven. Met de in statement in de `if`-statement wordt gekeken of een variable in een list zit. Is dit element in de list dan wordt de in een `True` en wordt de `if` geactiveerd. Omdat we alle elementen die in beide lijsten willen, wordt het element als list mee gegeven aan de recursieve return statement. Zit het element niet in de lijst dan roepen we de functie recursief aan zonder het element toe te voegen.


#### Opdracht 2b

Schrijf een functie `except_sets(a, b)` dat twee lijsten `a` en `b` binnen krijgt als parameters De functie geeft een lijst terug met alle elementen van `a` die niet in `b` voorkomen.

```python
def except_sets(a, b):
    """ Geeft een lijst terug met alle elementen van lijst a die niet in lijst b voorkomen.
    """
    # Base case
    if len(a) == 0:
        return []

    if a[0] not in b: # Als a[0] niet in b zit dan moeten we hem bewaren/meenemen.
        return [a[0]] + except_sets(a[1:], b)
    else: # Anders slaan we hem over.
        return except_sets(a[1:], b)

assert except_sets([1,2,3], [3,4,5]) == [1,2], "De except_sets() geeft een incorrecte lijst terug."
assert except_sets([1,2,3,4,6], [1,3,4,5]) == [2,6], "De except_sets() geeft een incorrecte lijst terug."
```

Omdat het programma nu juist alle elementen die niet in beide lijsten voorkomt moet bijhouden, wordt gebruik gemaakt van de not in statement om te kijken of het element niet in de lijst zit. Deze kun je vergelijken met de `!=` die je al eerder hebt gezien in `if`-statements. Verder werkt deze functie net zo als de `intersect_sets` functie.


#### Opdracht 2c

Schrijf een functie `union_sets(a, b)` die twee lijsten `a` en `b` binnen krijgt als parameters. De functie geeft de union terug van deze twee lijsten.

```python
def union_sets(a, b):
    """ Geeft de union terug van lijsten a en b.
    """
    temp = a + b
    return no_doubles(temp)
    # return no_doubles(a+b) zou ook nog kunnen

assert union_sets([1,2,3], [3,4,5]) == [1,2,3,4,5], "De union_sets() geeft een incorrecte lijst terug."
assert union_sets([1,2,3,4,6], [1,3,4,5]) == [2,6,1,3,4,5], "De union_sets() geeft een incorrecte lijst terug."
```

De vraag zegt niet dat deze functie recursief moet zijn. De union van de twee lijsten is de twee lijsten samengevoegd en de dubbele waarden verwijderd. Opdracht 1 was het schrijven van een functie die dubbele waarden verwijderd uit een lijst, `no_doubles(variable)`. Hier kunnen we handig gebruik van maken, nadat we de twee lijsten hebben samengevoegd. Roep de no_doubles() aan met de twee lijsten samengevoegd en geef terug wat uit deze functie komt.


#### Opdracht 3a

Schrijf de functie `fact(number, counter=1)` dat twee integers number en counter accepteert. De functie verzamelt alle delers van het gegeven number en geeft deze allemaal terug in een lijst. De counter start automatisch op 1 en kan gebruikt worden om de delers van number te vinden.

```python
def fact(number, counter=1):
    """ Geeft alle delers van number in lijst vorm terug.
    """
    # Base case
    if counter == number+1: # Als we hier niet +1 doen dan testen we niet of het getal deelbaar is door zichzelf!
        return []

    if number % counter == 0: # Het getal is deelbaar door counter zonder rest.
        return [counter] + fact(number, counter+1)
    else:
        return fact(number, counter+1)

assert fact(24) == [1,2,3,4,6,8,12,24], "De fact() geeft een incorrecte lijst terug."
assert fact(15) == [1,3,5,15], "De fact() geeft een incorrecte lijst terug."
```

Als het nummer zonder rest gedeeld kan worden door de counter dan is de counter een getal dat aan de delers lijst moet worden toegevoegd. Als het geen deler dan kan de functie zonder dit getal recursief aan geroepen worden. De base case vergelijkt counter met number+1 omdat er ook gekeken moet worden of een getal deelbaar is door zichzelf.


#### Opdracht 3b

Schrijf de functie `ggd(a, b)` die twee integers `a` en `b` accepteert en de ggd teruggeeft.

```python
def ggd(a, b):
    """ Geeft de ggd van twee integers a en b terug.
    """
    # Gebruik fact() om van beide getallen de delers te vinden.
    fa = fact(a)
    fb = fact(b)

    # Gebruik intersect_sets() om alle gemeenschappelijke delers te vinden.
    gd = intersect_sets(fa, fb)

    # Geef de hoogste waarde in de gd terug.
    return gd[-1]

assert ggd(24, 15) == 3, "De ggd() geeft een verkeerde ggd terug."
assert ggd(11, 43) == 1, "De ggd() geeft een verkeerde ggd terug."
assert ggd(60, 90) == 30, "De ggd() geeft een verkeerde ggd terug."
assert ggd(60, 120) == 60, "De ggd() geeft een verkeerde ggd terug."
```

De stappen zijn al in de opdracht meegegeven. Het programma kan `gd[-1]` teruggeven omdat de `fact` functie de getallen in de orde klein naar groot terug geeft. De `intersect_sets` functie behoudt deze volgorde. Het grootste getal staat dus altijd achteraan in de lijst.


#### Opdracht 3c

Een andere aanpak voor het vinden van de ggd is de het euclides algoritme. Schrijf de functie `euclides(a, b)` die twee integers `a` en `b` accepteert en via het euclides algoritme de ggd berekent en teruggeeft.

```python
def euclides(a, b):
    """ Geeft de ggd van twee integers volgens het euclides algoritme.
    """
    # Noem het grootste getal m
    if a > b:
        m = a
        n = b
    else:
        m = b
        n = a

    # r = m % n
    r = m % n

    # r == 0? Ja, geef n terug, nee roep de funcie nog een keer aan met n en er
    if r == 0:
        return n

    return euclides(n, r)

assert euclides(24, 15) == 3, "De euclides() geeft een verkeerde ggd terug."
assert euclides(11, 43) == 1, "De euclides() geeft een verkeerde ggd terug."
assert euclides(60, 90) == 30, "De euclides() geeft een verkeerde ggd terug."
assert euclides(60, 120) == 60, "De euclides() geeft een verkeerde ggd terug."
assert euclides(900, 1140) == 60, "De euclides() geeft een verkeerde ggd terug."
```

Ook hier kun je de stappen in de opdracht volgen.


#### Opdracht 3d

Welke van de twee is beter is vooral van toepassing op grotere getallen. Als je de ggd van 900 en 1140 wilt dan heb je de euclides nodig, omdat de ggd functie te vaak recursief wordt aangeroepen bij deze getallen en een `RecursionError` geeft.


## Context

### [Recursieve functies](/problems/context/5_recursieve_functies)

#### Opdracht 1 Bubblesort

```python
# Bubblesort

def bubble_sort_once(l):
    """ Sorteert lijst `l` volgens bubblesort algoritme, van klein naar groot, een keer.
    """
    # Base case. Om out of bounds te voor komen
    if len(l) == 1:
        return l

    # Er zijn nog maar twee elementen
    if len(l) == 2:
        if l[0] <= l[1]: # Het linker element is al kleiner of ze zijn even groot
            return l
        return [l[1]] + [l[0]] # De linker is groter, dus de twee getallen wisselen van plek

    if l[0] <= l[1]:
        return [l[0]] + bubble_sort_once(l[1:]) # We kunnen de huidige volgorde aanhouden
    else:
        return [l[1]] + bubble_sort_once([l[0]] + l[2:]) # We moeten de volgorde aanpassen

def check_order(l):
    """ Controleert of een list op volgorde is.
    """
    # Base case
    if len(l) == 2:
        if l[0] <= l[1]:
            return True
        else:
            return False

    if l[0] > l[1]: # Het eerste element is groter dan de volgende dus de lijst is niet op volgorde
        return False
    else: # Volgorde is goed dus we kunnen een element opschuiven om de rest van de lijst te checken
        return check_order(l[1:])

def bubblesort(l):
    """ Geeft de lijst `l` met bubble sort gesorteerd van klein naar groot terug.
    """
    if check_order(l) == True:
        return l
    else:
        `l` = bubble_sort_once(l)
        return bubblesort(l)
```


#### Opdracht 2 Mergesort

```python
def merge_sort(l):
    if len(l) > 1:
        half = len(l)//2
        return merge(merge_sort(l[:half]),  merge_sort(l[half:]))
    return l


def merge(l1, l2):
    if len(l1) == 0:
        return l2

    if len(l2) == 0:
        return l1

    if l1[0] <= l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    return [l2[0]] + merge(l1, l2[1:])
```

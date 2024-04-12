# PGM1 Week 6

## Basis

### [Wisselende stelsels](/problems/basis/6_wisselende_stelsels)

#### Opdracht 1

Schrijf een Python functie `num_to_base_b(n, b)`, die een (niet negatieve) integer n en een grondtal b (van 2 tot en met 10) accepteert en een string teruggeeft die het getal n in grondtal b voorstelt.

```python
def num_to_base_b(n, b):
    """ Geeft terug het integer n in grondgetal b
    """
    if n == 0:
        return ""
    return num_to_base_b(n//b, b) + str(n % b)

assert num_to_base_b(3116, 9) == '4242'
assert num_to_base_b(141474, 8) == '424242'
assert num_to_base_b(42, 8) == '52'
assert num_to_base_b(42, 5) == '132'
assert num_to_base_b(42, 10) == '42'
assert num_to_base_b(42, 2) == '101010'
assert num_to_base_b(4, 2) == '100'
assert num_to_base_b(4, 3) == '11'
assert num_to_base_b(4, 4) == '10'
assert num_to_base_b(0, 4) == '' # merk op dat als n 0 is we een lege string willen!!
assert num_to_base_b(0, 2) == '' # merk op dat als n 0 is we een lege string willen!!
```

Bij integerdeling kan er een rest getal overblijven. Dit getal moet ook meegenomen worden om het nieuwe getal in het gevraagde grondgetal te berekenen.


#### Opdracht 2

Schrijf een Python functie `base_b_to_num(s, b)` die een string s en een grondtal b accepteert, waarbij s een getal in grondtal b voorstelt en b een getal van 2 tot en met 10 is. De functie base_b_to_num moet een integer in grondtal 10 teruggeven die hetzelfde getal voorstelt als s.

```python
def base_b_to_num(s, b):
    """ Geeft het integer in grondgetal 10 terug van string s in grondgetal b
    """
    if s == "":
        return 0
    return base_b_to_num(s[:-1], b) * b + int(s[-1])

assert base_b_to_num("5733", 9) == 4242
assert base_b_to_num("1474462", 8) == 424242
assert base_b_to_num("222", 4) == 42
assert base_b_to_num("101010", 2) == 42
assert base_b_to_num("101010", 3) == 273
assert base_b_to_num("101010", 10) == 101010
assert base_b_to_num("11", 2) == 3
assert base_b_to_num("11", 3) == 4
assert base_b_to_num("11", 10) == 11
assert base_b_to_num("", 10) == 0 # de lege string moet 0 opleveren
```

Net als bij eerdere recursieve functies maken we gebruik van string slicing. De base case is een lege string.


#### Opdracht 3

Nu kunnen we wat we geschreven hebben samenvoegen tot een functie `base_to_base(b1, b2, s_in_b1)` die drie argumenten accepteert, een grondtal b1, een grondtal b2 (beide met een waarde tussen 2 tot en met 10) en s_in_b1, wat een string is die een getal in grondtal b1 voorstelt.

```python
def base_to_base(b1, b2, s_in_b1):
    """ Geeft terug de waarde van s_in_b1 in grond getal b2 ipv b1
    """
    n1 = base_b_to_num(s_in_b1, b1) # Zet het getal eerst om naar getal in grondgetal 10
    return num_to_base_b(n1, b2) # En nu zetten we dat getal om naar een getal in grondgetal b2

assert base_to_base(2, 10, "11") == '3'   # 11 in grondtal 2 is 3 in grondtal 10...
assert base_to_base(10, 2, "3") == '11'   # 3 in grondtal 10 is 11 in grondtal 2...
assert base_to_base(3, 5, "11") == '4'    # 11 in grondtal 3 is 4 in grondtal 5...
assert base_to_base(2, 3, "101010") == '1120'
assert base_to_base(2, 4, "101010") == '222'
assert base_to_base(2, 10, "101010") == '42'
assert base_to_base(5, 2, "4321") == '1001001010'
assert base_to_base(2, 5, "1001001010") == '4321'
```


#### Opdracht 4

Schrijf een functie `add(s, t)` die twee binaire strings s en t accepteert en hun som als resultaat teruggeeft terugstuurt, ook als binaire string.

```python
def add(s, t):
    """ Geeft de som van de twee binaire strings s en t terug als binaire string
    """
    decNrS = base_b_to_num(s, 2) # Zet ze eerst om naar grondgetal 10
    decNrT = base_b_to_num(t, 2)
    return num_to_base_b(decNrS + decNrT, 2) # Tel de twee integers bij elkaar op en zet om naar binaire string

assert add("11", "1") == '100'
assert add("11", "100") == '111'
assert add("110", "11") == '1001'
assert add("11100", "11110") == '111010'
assert add("10101", "10101") == '101010'
```


#### Opdracht 5

Schrijf voor dit probleem een Python functie `add_b(s, t)` die twee strings als argument accepteert. Deze strings stellen binaire getallen voor.

```python
def add_b(s, t):
    """ Geeft de som van de twee binaire strings s en t terug als binaire string, maar op de 'basisschool' methode voor optellen
    """
    # basisgevallen!
    if len(s) == 0 and len(t) == 0:
        return ""
    elif len(s) == 0:
        return t
    elif len(t) == 0:
        return s

    # Er zullen vier recursieve gevallen zijn; dit is de eerste:
    if s[-1] == '0' and t[-1] == '0':
        return add_b(s[:-1], t[:-1]) + '0'   # 0 + 0 == 0
    elif s[-1] == '1' and t[-1] == '0':
        return add_b(s[:-1], t[:-1]) + '1'  # 1 + 0 == 1
    elif s[-1] == '0' and t[-1] == '1':
        return add_b(s[:-1], t[:-1]) + '1'  # 0 + 1 == 1
    elif s[-1] == '1' and t[-1] == '1':
        return add_b(s[:-1], add_b("1", t[:-1])) + '0' # 1 + 1 == 10

assert add_b("11", "100") == "111"
assert add_b("11100", "11110") == "111010"
assert add_b("110", "11") == "1001"
assert add_b("110101010", "11111111") == "1010101001"
assert add_b("1", "1") == "10"
```

Met de basis gevallen wordt in de gaten gehouden of de strings leeg zijn of dat een van beide langer is dan de andere. Net als bij eerdere recursieve functies maken we weer gebruik van string slicing.


### [Sorteren](/problems/basis/6_sorting)

#### Opdracht 1

Schrijf een functie `blsort(L)` die als argument een lijst L accepteert en een lijst teruggeeft met dezelfde elementen als L, maar in oplopende volgorde. Een functie die sommigen handig vinden is `count(e, L)`, een hulpfunctie die je eerder al hebt gezien.

```python
def count(e, L):
    """ Telt hoe vaak e in lijst L zit
    """
    if len(L) == 0:
        return 0
    elif L[0] == e:
        return 1 + count(e, L[1:])
    else:
        return 0 + count(e, L[1:])

def blsort(L):
    count1 = count(1, L)
    lc = (len(L) - count1) * [0] + count1 * [1]
    return lc

assert blsort([1, 0, 1]) == [0, 1, 1]
L = [1, 0, 1, 0, 1, 0, 1]
assert blsort(L) == [0, 0, 0, 1, 1, 1, 1]
```


#### Opdracht 2

Schrijf de funtie `rem_one(L, e)` die een lijst L accepteer en element e en vervolgens èèn keer e verwijdert uit L en deze nieuwe lijst teruggeeft. Gebruik recursie om een algemene sorteerfunctie selection_sort(L) te schrijven die een lijst L accepteert en een lijst teruggeeft met dezelfde elementen als L, maar in oplopende volgorde. Je kan hiervoor de ingebouwde Python functie max (of min, als je deze liever hebt) gebruiken, en de functie rem_one.

```python
def rem_one(L, e):
    """ Verwijdert e een keer uit de lijst L
    """
    if len(L) == 0:
        return L
    elif L[0] == e: # Verwijder de eerste e die wordt tegengekomen en stop de recursie
        return L[1:]
    else:
        return [L[0]] + rem_one(L[1:], e) # Blijf de functie recursief aanroepen tot e gevonden is of de lijst leeg is

def selectionSort(L):
    """ Geeft lijst L gesorteerd van laag naar hoog terug
    """
    if len(L) == 0:
        return L
    # Je kunt er voor kiezen om van laag naar hoog te werken of van hoog naar laag
    # Hier gaan we van hoog naar laag
    maxL = max(L)
    newL = rem_one(L, maxL) # Verwijder de hoogste uit de lijst
    return selectionSort(newL)  + [maxL]

assert selectionSort([42, 1, 3.14]) == [1, 3.14, 42]
L = [7, 9, 4, 3, 0, 5, 2, 6, 1, 8]
assert selectionSort(L) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L = [1, 7, 9, 4, 3, 8, 0, 5, 2, 6, 1, 8, 4]
assert selectionSort(L) == [0, 1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9]
```


## Context

### [Compressie](/problems/context/6_compressie)

#### Opdracht 1

Schrijf een functie `compress(s)`, waarvan het argument een binaire string s is met een lengte van minder dan of gelijk aan 64 en dat als resultaat een andere binaire string teruggeeft. De resulterende binaire string zou een run-length codering van het origineel moeten zijn, zoals hierboven beschreven.

```python
def num_to_base_b(n, b):
    """ Geeft het integer n in grondgetal b terug
    """
    if n == 0:
        return ""
    return num_to_base_b(n//b, b) + str(n % b)

def countFront(c, s):
    if len(s) == 0:
        return 0

    if s[0] != c :
        return 0

    if s[0] == c:
        return 1 + countFront(c,s[1:])

def removeFront(c, s):
    if len(s) == 0:
        return ""

    if s[0] != c :
        return s

    if s[0] == c:
        return removeFront(c, s[1:])

def compress(s):
    """ Compress een string
    """
    if s == '' :
        return ""

    if s[0] == '1':
        count = countFront('1', s)
        countb = num_to_base_b(count, 2)
        return '1' + '0' * (7 - len(countb)) + countb + compress(removeFront('1', s))
    else:
        count = countFront('0', s)
        countb = num_to_base_b(count, 2)
        return '0' + '0' * (7 - len(countb)) + countb + compress(removeFront('0', s))
```


#### Opdracht 2

Schrijf vervolgens een functie `uncompress(c)` die het comprimeren van de functie compress “omkeert” of “ongedaan maakt”.

```python
def base_b_to_num(s, b):
    """ Geeft het integer in grondgetal 10 terug van string s in grondgetal b
    """
    if s == "":
        return 0
    return base_b_to_num(s[:-1], b) * b + int(s[-1])

def uncompress(s):
    """ Uncompress een string
    """
    if len(s) == 0:
        return ""

    first8 = s[:8]
    sign = first8[0]
    repeat = base_b_to_num(first8[1:], 2)
    return sign * repeat + uncompress(s[8:])
```

Hier zijn een aantal assert statements om de compress en uncompress functies te testen.

```python
assert compress(64 * "0") == '01000000'
assert uncompress("10000101") == '11111'  # 5 1'en
assert compress("11111") == '10000101'
assert uncompress(compress(64 * "0")) == 64 * "0"
stripes = "0" * 16 + "1" * 16 + "0" * 16 + "1" * 16
assert compress(stripes) == '00010000100100000001000010010000'
assert uncompress("00010000100100000001000010010000") == '0000000000000000111111111111111100000000000000001111111111111111'
assert uncompress("00010000100100000001000010010000") == stripes
```


### [Wisselende stelsels](/problems/context/6_lingo)

Schrijf een functie `lingo(s, t)` die twee strings s en t accepteert en een integer teruggeeft, de zogenaamde “Lingo-telling, of -score, waar s wordt vergeleken met t.

```python
def rem_first(L, c):
    """ Verwijder de eerste variable c die in lijst L te vinden is
    """
    if len(L) == 0:
        return L
    elif L[0] == c:
        return L[1:]
    else:
        return L[0] + rem_first(L[1:], c)

def lingo(s, t):
    """ Geeft de Lingo-score van de strings s en t terug als integer
    """
    if len(s) == 0 or len(t) == 0:
        return 0

    if s[0] in t:
        return 1 + lingo(s[1:], rem_first(t, s[0]))
    else:
        return lingo(s[1:], t)

assert lingo('diner', 'proza') == 1  # alleen de 'r'
assert lingo('beeft', 'euvel') == 2  # twee 'e's zijn gedeeld
assert lingo('gattaca', 'aggtccaggcgc') == 5 # 2 'a's, 1 't', 1 'c', 1 'g'
assert lingo('gattaca', '') == 0 # geef 0 terug bij een lege string
```



# Wisselende stelsels

| Naam         | Beschrijving                                                   |
|--------------|----------------------------------------------------------------|
| Onderwerp    | Getallen omzetten naar verschillende grondtallen               |
| Bestandsnaam | `wk6ba1.py`                                                    |
| Inleveren    | Lever jouw bestand met de juiste bestandsnaam in op GradeScope |

De volgende problemen hebben allemaal te maken met de weergave van grondtallen en het converteren of het berekenen ervan.

Om te beginnen zal je worden gevraagd om van grondtal 10 naar andere grondtallen te converteren en omgekeerd. Omdat bij grondtallen groter dan grondtal 10 nieuwe "cijfers" nodig zijn, beperken we ons tussen grondtallen van 2 tot en met 10.

## Opdracht 1: `num_to_base_b(n, b)`

Schrijf een Python functie `num_to_base_b(n, b)`, die een (niet negatieve) integer `n` en een grondtal `b` (van 2 tot en met 10) accepteert en een string teruggeeft die het getal `n` in grondtal `b` voorstelt.

Je hoeft niet te controleren of `b` tussen 2 en 10 ligt, we zullen ervoor zorgen dat dit de enige waarden zijn die we testen.

Vergeet ook niet dat hier *integerdeling* (zonder cijfers achter de komma) nodig is. In Python wordt bij integerdeling altijd naar beneden afgerond en daar gebruik je `//` voor, bijvoorbeeld,

```python
18 // 7 == 2
```

Hier zie je een aantal voorbeelden:

```ipython
In [1]: num_to_base_b(3116, 9)
Out[1]: '4242'

In [2]: num_to_base_b(141474, 8)
Out[2]: '424242'

In [3]: num_to_base_b(42, 8)
Out[3]: '52'

In [4]: num_to_base_b(42, 5)
Out[4]: '132'

In [5]: num_to_base_b(42, 10)
Out[5]: '42'

In [6]: num_to_base_b(42, 2)
Out[6]: '101010'

In [7]: num_to_base_b(4, 2)
Out[7]: '100'

In [8]: num_to_base_b(4, 3)
Out[8]: '11'

In [9]: num_to_base_b(4, 4)
Out[9]: '10'

In [10]: num_to_base_b(0, 4)
Out[10]: ''                   # merk op dat als n 0 is we een lege string willen!!

In [11]: num_to_base_b(0, 2)
Out[11]: ''                   # merk op dat als n 0 is we een lege string willen!!
```

:::{admonition} Opmerkingen
:class: notice

Vergeet niet dat jouw functie een string en *niet* een getal moet teruggeven! Verder,

<!-- TODO verwijzing naar num_to_bin in college -->

-   De functie `num_to_binary` die je eerder hebt geschreven is een goed begin...
-   Vraag jezelf af, wat moet er veranderen om waarden in grondtal `b` terug te geven in plaats van grondtal 2?
:::

Hier zie je een aantal tests die je kan gebruiken:

```python
assert num_to_base_b(0, 4) == ''
assert num_to_base_b(42, 5) == '132'
```

Je kan er natuurlijk meer bedenken!

:::{admonition} Tips
:class: tip

Jouw code moet een lege string teruggeven wanneer de waarde van `n` 0 is (dit voorkomt voorloopnullen!)

Gebruik de volgende twee Python functies voor het heen en weer schakelen tussen strings en getallen. Deze zijn het meest nuttig als je daar enkele tekens of getallen gebruikt:

-   `str(x)` geeft het getal (de integer) `x` terug als string
-   `int(x)` geeft de integerwaarde van de string `s` terug, Python zal een `ValueError` geven als `s` geen integer voorstelt
:::

## Opdracht 2: `base_b_to_num(s, b)`

We willen natuurlijk de omgekeerde conversie ook kunnen doen!

Daarom ga je een Python functie `base_b_to_num(s, b)` schrijven die een string `s` en een grondtal `b` accepteert, waarbij `s` een getal in grondtal `b` voorstelt en `b` een getal van 2 tot en met 10 is. De functie `base_b_to_num` moet een integer in grondtal 10 teruggeven die hetzelfde getal voorstelt als `s`.

Je hoeft niet te controleren of `b` tussen 2 en 10 ligt, we zullen ervoor zorgen dat dit de enige waarden zijn die we testen.

Hier zie je een aantal voorbeelden, controleer dat de eerste twee werken (het zijn de grootste voorbeelden die we zullen gebruiken):

```ipython
In [1]: base_b_to_num("5733", 9)
Out[1]: 4242

In [2]: base_b_to_num("1474462", 8)
Out[2]: 424242

In [3]: base_b_to_num("222", 4)
Out[3]: 42

In [4]: base_b_to_num("101010", 2)
Out[4]: 42

In [5]: base_b_to_num("101010", 3)
Out[5]: 273

In [6]: base_b_to_num("101010", 10)
Out[6]: 101010

In [7]: base_b_to_num("11", 2)
Out[7]: 3

In [8]: base_b_to_num("11", 3)
Out[8]: 4

In [9]: base_b_to_num("11", 10)
Out[9]: 11

In [10]: base_b_to_num("", 10)
Out[10]: 0                         # de lege string moet 0 opleveren
```

:::{admonition} Opmerkingen
:class: notice

Vergeet niet dat jouw functie een getal teruggeeft, en een string als argument `s` accepteert! Verder,

-   Het `bin_to_num` voorbeeld die je eerder hebt gezien is een goed begin...

-   Vraag jezelf weer af, wat moet er veranderen om waarden in grondtal 2 terug te geven in plaats van grondtal `b`?
:::

Gebruik de bovenstaande voorbeelden in jouw tests!

:::{admonition} Tips
:class: tip

Jouw functie `base_b_to_num` moet `0` teruggeven als `s` een lege string is. Verder,

-   Zoals gewoonlijk zal het meest rechtse karakter van de string de "een"'en kolom zijn," het minst significante getal in grondtal `b`.

-   ... maar dat betekent dat de waarde van het meest rechtse teken gewoon `int(s[-1])` is!

Nogmaals, hier zijn de Python functies om strings en getallen in elkaar om te zetten:

-   `str(x)` geeft het getal (de integer) `x` terug als string
-   `int(x)` geeft de integerwaarde van de string `s` terug, Python zal een `ValueError` geven als `s` geen integer voorstelt
:::

## Opdracht 3: `base_to_base(b1, b2, s_in_b1)`

Nu kunnen we wat we geschreven hebben samenvoegen tot een functie `base_to_base(b1, b2, s_in_b1)` die drie argumenten accepteert, een grondtal `b1`, een grondtal `b2` (beide met een waarde tussen 2 tot en met 10) en `s_in_b1`, wat een string is die een getal in grondtal `b1` voorstelt.

De functie `base_to_base` moet een string teruggeven die dezelfde waarde in grondtal `b2` vertegenwoordigt.

Hier zijn een aantal voorbeelden:

```ipython
In [1]: base_to_base(2, 10, "11")   # 11 in grondtal 2 is 3 in grondtal 10...
Out[1]: '3'

In [2]: base_to_base(10, 2, "3")    # 3 in grondtal 10 is 11 in grondtal 2...
Out[2]: '11'

In [3]: base_to_base(3, 5, "11")    # 11 in grondtal 3 is 4 in grondtal 5...
Out[3]: '4'

In [4]: base_to_base(2, 3, "101010")
Out[4]: '1120'

In [5]: base_b_to_num("1120", 3)
Out[5]: 42

In [6]: base_to_base(2, 4, "101010")
Out[6]: '222'

In [7]: base_to_base(2, 10, "101010")
Out[7]: '42'

In [8]: base_to_base(5, 2, "4321")
Out[8]: '1001001010'

In [9]: base_to_base(2, 5, "1001001010")
Out[9]: '4321'
```

:::{admonition} Opmerkingen
:class: notice

Ga geen conversie functies herschrijven! Converteer in plaats daarvan het getal naar decimaal en dan terug naar de gewenste grondtal!
:::

Hier zijn een paar tests:

```python
assert base_to_base(2, 4, "101010") == "222"
assert base_to_base(2, 5, "1001001010") == "4321"
```

:::{admonition} Tips
:class: tip

-   Gebruik eerst `base_b_to_num` om een gewoon, decimaal getal voor `s_in_b1` te krijgen. Geef het een naam.

-   Gebruik dan de functie `num_to_base_b` om die waarde om te zetten naar het juiste grondtal!
:::

## Opdracht 4: `add(s, t)`

Dit is een korte opgave om de functies die je hebt geschreven te gebruiken!

Schrijf een functie `add(s, t)` die twee binaire strings `s` en `t` accepteert en hun som als resultaat teruggeeft terugstuurt, ook als binaire string.

We raden je aan dit te doen door de twee binaire strings om te zetten in twee getallen in grondtal 10, de twee getallen bij elkaar op te tellen en de resulterende som vervolgens weer om te zetten naar grondtal 2!

Hier zijn een aantal voorbeelden:

```ipython
In [1]: add("11", "1")
Out[1]: '100'

In [2]: add("11", "100")
Out[2]: '111'

In [3]: add("110", "11")
Out[3]: '1001'

In [4]: add("11100", "11110")
Out[4]: '111010'

In [5]: add("10101", "10101")
Out[5]: '101010'
```

## Opdracht 5: `add_b(s, t)`

Hierboven zag je een manier om twee binaire getallen op te tellen: zet ze eerst om naar grondtal 10, tel deze getallen op en zet vervolgens de uitkomst weer om naar een binaire string.


Bij deze opgave zal je echter een andere, meer directe, methode implementeren voor het optellen van twee binaire getallen, met behulp van de "basisschool" methode die eerder is besproken:

```text
  101110
  100111
--------
```

Dit ziet er na optelling als volgt uit:

```text hl_lines="1"
   111
  101110
  100111
--------
 1010101
```

Je ziet hier de "carry" bits op de eerste regel.

Schrijf voor dit probleem een Python functie `add_b(s, t)` die twee strings als argument accepteert. Deze strings stellen binaire getallen voor.

De functie `add_b` moet een nieuwe string teruggeven die de som van de twee argumenten voorstelt.

De som moet berekend worden met het "basisschool" binaire optelalgoritme, zoals hierboven is besproken, en niet met basisconversies (door grondtallen om te zetten). Dat wil zeggen dat de optelling puur *syntactisch* zal moeten zijn: je gebruikt de opteloperator `+` voor getallen van Python *niet*.

:::{admonition} Tips
:class: tip

-   Je hebt op zijn minst *twee* base cases nodig. Eén base case om te overwegen is wat als `s` geen karakters meer heeft, maar `t` nog wel: wat zou de juiste string zijn om terug te geven?

-   De "carry" case (als je een bit moet "onthouden") is een ander lastig onderdeel van dit probleem.

-   Wanneer je een bit moet meenemen, zal je **drie** strings toe moeten voegen: (1) de rest van `s` (`s[:-1]`), (2) de rest van `t`, en de extra carry string, die gewoon `'1'` is.

-   De oplossing is om twee keer `add_b` te gebruiken: één keer om de carry string bij een van de twee "rest" strings toe te voegen, en een tweede keer om het eerste resultaat toe te voegen aan de andere van de twee "restanten"!
:::

Hier is een begin:

```python
def add_b(s, t):
    """ docstring: deze moet je nog invullen
    """
    # basisgevallen!

    # Er zullen vier recursieve gevallen zijn; dit is de eerste:
    if s[-1] == '0' and t[-1] == '0':
        return add_b(s[:-1], t[:-1]) + '0'   # 0 + 0 == 0

    # je moet nog drie recursieve gevallen benoemen...
```

Hier zijn een paar voorbeelden:

```ipython
In [1]: add_b("11100", "11110")
Out[1]: '111010'

In [2]: add_b("10101", "10101")
Out[2]: '101010'

In [3]: add_b("11", "1")
Out[3]: '100'

In [4]: add_b("11", "100")
Out[4]: '111'
```

En hier een aantal tests:

```python
assert add_b("11", "100") == "111"
assert add_b("11100", "11110") == "111010"
assert add_b("110", "11") == "1001"
assert add_b("110101010", "11111111") == "1010101001"
assert add_b("1", "1") == "10"
```
---
title: Boter, kaas en eieren en N op een rij
description: Boter, kaas en eieren en N (vier?) een rij
file: wk9ex2.py
points: 35
---

# Boter, kaas en eieren en N op een rij

In deze opgave moet je acht kleine functies, die allemaal erg op elkaar lijken, schrijven die tweedimensionale gegevens in Python verwerken, dat wil zeggen, lijsten-van-lijsten verwerken.

De applicatie die we in gedachten hebben is een *spelbord* waarvan je programma gaat bepalen:

* Of er drie op een rij is voor een bepaald karakter (vier functies), en
* Of er `n` op een rij is voor een bepaald karakter (vier functies die op de vorige vier lijken)

## Om te beginnen...

Begin door deze bestandsheader en de twee functies eronder te kopiëren naar een nieuw bestand `wk9ex2.py`:

```python
#
# wk9ex2.py
#
# Naam:
#


# dit is een functie om tweedimensionale arrays
#  (lijsten van lijsten) af te drukken
def print_2d(a):
    """print_2d prints a 2D array, a
       as rows and columns
       Argument: a, a 2D list of lists
       Result: None (no return value)
    """
    rows = len(a)
    cols = len(a[0])

    for r in range(rows):      # rows == aantal rijen
        for c in range(cols):  # cols == aantal kolommen
            print(a[r][c], end=' ')
        print()

    return None  # dit is impliciet aanwezig
    # als er geen return-statement aanwezig is


# een paar tests voor print_2d
a = [["X", " ", "O"], ["O", "X", "O"]]
print("2-row, 3-col a is")
print_2d(a)

a = [["X", "O"], [" ", "X"], ["O", "O"], ["O", "X"]]
print("4-row, 2-col a is")
print_2d(a)


# maak een tweedimensionale array van een ééndimensionale string
def create_a(rows, cols, s):
    """Returns a 2D array with
       rows rows and
       cols cols
       using the data from s: across the
       first row, then the second, etc.
       We'll only test it with enough data!
    """
    a = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row += [s[0]]  # voeg dat karakter toe
            s = s[1:]          # verwijder het eerste karakter
        a += [new_row]
    return a


# een paar tests voor create_a:
a = [["X", " ", "O"], ["O", "X", "O"]]
new_a = create_a(2, 3, "X OOXO")
assert new_a == a
print("Is new_a == a? moet True zijn:", new_a == a)

a = [["X", "O"], [" ", "X"], ["O", "O"], ["O", "X"]]
new_a = create_a(4, 2, "XO XOOOX")
assert new_a == a
```

Probeer het bestand uit door het op de command line van ipython uit te voeren.

:::{admonition} Gegevensformaat
:class: notice

Merk op dat alle tweedimensionele data in deze opgave lijsten van lijsten van losse karakters zijn:

-   De algehele structuur, meestal `a` genoemd, is een lijst van rijen
-   Elke rij is een lijst gegevenselementen
-   Elk gegevenselement is een string met een enkel karakter
-   Sterker nog, we beperken ons tot slechts drie strings:
    *   `'X'`, een hoofdletter X,
    *   `'O'`, een hoofdletter O,
    *   en `' '`, het spatieteken (dit is *niet* de lege string!).
:::

## Drie op een rij

De eerste vier functies die je gaat schrijven controleren of er drie op een rij is

* in een specifieke richting (opgenomen in de functienaam),
* voor een specifiek karakter `ch`,
* op een specifieke startrij- en kolom: `r_start` en `c_start`, en
* in een gegeven tweedimensionale array `a`.

Elk van de functies moet `False` teruggeven

* als er **GEEN RUIMTE** is voor drie op een rij vanaf de startpositie gegeven door `r_start` en `c_start` (controleer dit eerst!), of
* als `r_start` of `c_start` buiten de grenzen van `a` valt, of
* (zelfs als er ruimte binnen de grenzen is), als er GEEN drie-op-een-rij-patroon binnen `a` is die helemaal bestaat uit het karakter `ch` in de specifieke richting beginnend bij de locatie gegeven door `r_start` en `c_start`.

Elke functie moet daarentegen `True` teruggeven

* alleen maar als er een drie-op-een-rij-patroon in `a` is die helemaal bestaat uit het element `ch` in de specifieke richting beginnend bij de locatie van `r_start` en `c_start`.

### Voorbeeld

Bekijk het volgende patroon, ontworpen voor de richting "oost"

Hier zie je een paar grenscontroles en een voorbeeld van een `for`-lus:

```python
# voor de functie voor drie op een rij naar het oosten:

rows = len(a)      # aantal rijen is len(a)
cols = len(a[0])   # aantal kolommen is len(a[0])

if r_start >= rows:
    return False  # buiten de grenzen van de rijen

# andere grenscontroles...
if c_start > cols - 3:
    return False  # buiten de grenzen van de kolommen

# zijn alle gegevenselementen correct?
for i in range(3):                   # lusindex is i
    if a[r_start][c_start+i] != ch:  # controleer op fouten
        return False                 # fout gevonden; geef False terug

return True                          # geen fouten gevonden in de lus; geef True terug
```

Merk op dat voor andere richtingen

* Je andere controles nodig hebt (om te kijken of je niet uit de grenzen loopt).
* Ook moet je de lus aanpassen voor andere richtingen
* Het voorbeeld hierboven kijkt alleen naar drie op een rij in oostelijke richting.

### Vier functies

Hier zijn de signatures van de vier functies die je moet schrijven:

1. `def in_a_row_3_east(ch, r_start, c_start, a):`

   Deze moet bij `r_start` en `c_start` beginnen, kijken of er een drie op een rij van karakter `ch` is in **oostelijke richting** en een toepasselijke `True` of `False` teruggeven.
2. `def in_a_row_3_south(ch, r_start, c_start, a):`

   Deze moet bij `r_start` en `c_start` beginnen, kijken of er een drie op een rij van karakter `ch` is in **zuidelijke richting** en een toepasselijke `True` of `False` teruggeven.
3. `def in_a_row_3_southeast(ch, r_start, c_start, a):`

   Deze moet bij `r_start` en `c_start` beginnen, kijken of er een drie op een rij van karakter `ch` is in **zuidoostelijke richting** en een toepasselijke `True` of `False` teruggeven.
4. `def in_a_row_3_northeast(ch, r_start, c_start, a):`

   Deze moet bij `r_start` en `c_start` beginnen, kijken of er een drie op een rij van karakter `ch` is in **noordoostelijke richting** en een toepasselijke `True` of `False` teruggeven.

Deze functies kunnen gecombineerd worden om elke drie op een rij op een spelbord te herkennen, bijvoorbeeld voor Boter, Kaas en Eieren. Je gaat hierna meer algemene versies hiervan maken...

Hier zijn vier tests voor elke functie; plak deze in je bestand en controleer dat ze werken!

```python
# tests voor in_a_row_3_east
a = create_a(3, 4, "XXOXXXOOOOOO")
assert not in_a_row_3_east("X", 0, 0, a)
assert in_a_row_3_east("O", 2, 1, a)
assert not in_a_row_3_east("X", 2, 1, a)
assert not in_a_row_3_east("O", 2, 2, a)

# tests voor in_a_row_3_south
a = create_a(4, 4, "XXOXXXOXXOO OOOX")
assert in_a_row_3_south("X", 0, 0, a)
assert not in_a_row_3_south("O", 2, 2, a)
assert not in_a_row_3_south("X", 1, 3, a)
assert not in_a_row_3_south("O", 42, 42, a)

# tests voor in_a_row_3_southeast
a = create_a(4, 4, "XOOXXXOXX XOOOOX")
assert in_a_row_3_southeast("X", 1, 1, a)
assert not in_a_row_3_southeast("X", 1, 0, a)
assert in_a_row_3_southeast("O", 0, 1, a)
assert not in_a_row_3_southeast("X", 2, 2, a)

# tests voor in_a_row_3_northeast
a = create_a(4, 4, "XOXXXXOXXOXOOOOX")
assert in_a_row_3_northeast("X", 2, 0, a)
assert in_a_row_3_northeast("O", 3, 0, a)
assert not in_a_row_3_northeast("O", 3, 1, a)
assert not in_a_row_3_northeast("X", 3, 3, a)
```

## Van 3 naar N: N op een rij

Boter, Kaas en Eieren is al lang opgelost! Laten we onbeperkt grote spelborden bekijken...

Om dit te doen, ga je je drie-op-een-rij-functies uitbreiden naar N-op-een-rij-functies.

Elke functie krijgt een extra argument aan het einde, een integer `n`, die het aantal identieke elementen (gelijk aan `ch`) voorstelt die gevonden moeten worden om `True` terug te geven.

* Als de positie buiten de grenzen valt; of binnen de grenzen, maar alsnog buiten de grenzen valt door de waarde van `n`, moet je functie `False` teruggeven.
* Je functie moet natuurlijk ook `False` teruggeven als de rij wel binnen de grenzen valt, maar er geen N op een rij is!

Hier zijn de signatures van de vier N-op-een-rij-functies die je moet schrijven:

1. `def in_a_row_n_east(ch, r_start, c_start, a, n):`

   Deze moet bij `r_start` en `c_start` beginnen, kijken of er een N op een rij van karakter `ch` is in **oostelijke richting** en een toepasselijke `True` of `False` teruggeven.
2. `def in_a_row_n_south(ch, r_start, c_start, a, n):`

   Deze moet bij `r_start` en `c_start` beginnen, kijken of er een N op een rij van karakter `ch` is in **zuidelijke richting** en een toepasselijke `True` of `False` teruggeven.
3. `def in_a_row_n_southeast(ch, r_start, c_start, a, n):`

   Deze moet bij `r_start` en `c_start` beginnen, kijken of er een N op een rij van karakter `ch` is in **zuidoostelijke richting** en een toepasselijke `True` of `False` teruggeven.
4. `def in_a_row_n_northeast(ch, r_start, c_start, a, n):`

   Deze moet bij `r_start` en `c_start` beginnen, kijken of er een N op een rij van karakter `ch` is in **noordoostelijke richting** en een toepasselijke `True` of `False` teruggeven.

Ook hier zijn vier tests voor elke functie; plak deze in je bestand en controleer dat ze werken!

```python
# tests voor in_a_row_n_east
a = create_a(5, 5, 'XXOXXXOOOOOOXXXX XXXOOOOO')
assert in_a_row_n_east('O', 1, 1, a, 4)
assert in_a_row_n_east('O', 1, 3, a, 2)
assert not in_a_row_n_east('X', 3, 2, a, 4)
assert in_a_row_n_east('O', 4, 0, a, 5)


# tests voor in_a_row_n_south
a = create_a(5, 5, 'XXOXXXOOOOOOXXXXOXXXOOOXO')
assert not in_a_row_n_south('X', 0, 0, a, 5)
assert in_a_row_n_south('O', 1, 1, a, 4)
assert not in_a_row_n_south('O', 0, 1, a, 6)
assert in_a_row_n_south('X', 4, 3, a, 1)


# tests voor in_a_row_n_southeast
a = create_a(5, 5, 'XOO XXXOXOOOXXXXOXXXOOOXX')
assert in_a_row_n_southeast('X', 1, 1, a, 4)
assert not in_a_row_n_southeast('O', 0, 1, a, 3)
assert in_a_row_n_southeast('O', 0, 1, a, 2)
assert not in_a_row_n_southeast('X', 3, 0, a, 2)


# tests voor in_a_row_n_northeast
a = create_a(5, 5, 'XOO XXXOXOOOXOXXXOXXXOOXX')
assert in_a_row_n_northeast('X', 4, 0, a, 5)
assert in_a_row_n_northeast('O', 4, 1, a, 4)
assert not in_a_row_n_northeast('O', 2, 0, a, 2)
assert not in_a_row_n_northeast('X', 0, 3, a, 1)
```

Je gaat deze `in_a_row`-functies in de komende weken gebruiken om een versie van *Vier op een rij* te implementeren!

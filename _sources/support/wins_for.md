# Tips voor de in-een-rij-strategie voor `wins_for`

Als je je `in_a_row`-functies wilt gebruiken om `wins_for` te implementeren (of die van ons; zie hieronder voor de oplossingen), dan moet je je vier functies

* `in_a_row_n_east`
* `in_a_row_n_south`
* `in_a_row_n_northeast`
* `in_a_row_n_southeast`

boven (niet in) de klasse `Board` plakken, en ze dan in `wins_for` gebruiken, zoals hier:

```python
# BOVEN de klasse Board:
def in_a_row_n_east(ch, r_start, c_start, a, n):
    """Docstring"""


def in_a_row_n_south(ch, r_start, c_start, a, n):
    """Docstring"""


def in_a_row_n_northeast(ch, r_start, c_start, a, n):
    """Docstring"""


def in_a_row_n_southeast(ch, r_start, c_start, a, n):
    """Docstring"""


# de klasse Board zelf
class Board:
    """Docstring"""

    def wins_for(self, row, col, ox):
        """ wins_for code """
        # dit is pseudocode
        for row in ...:
            for col in ...:
                # controleer of je in één van de vier richtingen wint
```

Merk op dat je moet controleren of je in elk van de vier richtingen wint voor elke plaats op het bord; we doen dit extra grondig 🙂

## Oplossingen voor de `in_a_row`-functies...

Als je de `in_a_row`-functies niet opgelost hebt, kan je onze oplossingen gebruiken. Succes!

```python
def in_a_row_n_east(ch, r_start, c_start, a, n):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists a (array),
       returns True if there are n ch's in a row
       heading east and returns False otherwise.
    """
    h = len(a)
    w = len(a[0])
    if r_start < 0 or r_start > h - 1:
        return False  # rij buiten de grenzen
    if c_start < 0 or c_start + (n-1) > w - 1:
        return False  # kolom buiten de grenzen
    # lus over elke _offset_ i van de locatie
    for i in range(n):
        if a[r_start][c_start+i] != ch:  # klopt niet!
            return False
    return True  # alle offsets kloppen, dus we geven True terug


def in_a_row_n_south(ch, r_start, c_start, a, n):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists a (array),
       returns True if there are n ch's in a row
       heading south and returns False otherwise.
    """
    h = len(a)
    w = len(a[0])
    if r_start < 0 or r_start + (n-1) > h - 1:
        return False  # rij buiten de grenzen
    if c_start < 0 or c_start > w - 1:
        return False  # kolom buiten de grenzen
    # lus over elke _offset_ i van de locatie
    for i in range(n):
        if a[r_start+i][c_start] != ch:  # klopt niet!
            return False
    return True  # alle offsets kloppen, dus we geven True terug


def in_a_row_n_northeast(ch, r_start, c_start, a, n):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists a (array),
       returns True if there are n ch's in a row
       heading northeast and returns False otherwise.
    """
    h = len(a)
    w = len(a[0])
    if r_start - (n-1) < 0 or r_start > h - 1:
        return False  # rij buiten de grenzen
    if c_start < 0 or c_start + (n-1) > w - 1:
        return False  # kolom buiten de grenzen
    # lus over elke _offset_ i van de locatie
    for i in range(n):
        if a[r_start-i][c_start+i] != ch:  # klopt niet!
            return False
    return True  # alle offsets kloppen, dus we geven True terug


def in_a_row_n_southeast(ch, r_start, c_start, a, n):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists a (array),
       returns True if there are n ch's in a row
       heading southeast and returns False otherwise.
    """
    h = len(a)
    w = len(a[0])
    if r_start < 0 or r_start + (n-1) > h - 1:
        return False  # rij buiten de grenzen
    if c_start < 0 or c_start + (n-1) > w - 1:
        return False  # kolom buiten de grenzen
    # lus over elke _offset_ i van de locatie
    for i in range(n):
        if a[r_start+i][c_start+i] != ch:  # klopt niet!
            return False
    return True  # alle offsets kloppen, dus we geven True terug
```
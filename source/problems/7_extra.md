# Extra: Game of Life

Game of Life is een facultatieve uitdaging. Je kunt deze opgave zelfstandig
starten: alle benodigde afspraken en functies staan hier. De minimale kern van
de week blijft de opstap en basis.

## Raster en rand

Een bord is een rechthoekige lijst van lijsten. \`0\` betekent een dode cel en \`1\`
een levende cel. \`board[row][col]\` is de cel op rij \`row\` en kolom \`col\`.
Coördinaten buiten het bord tellen als dode cellen; buiten het bord wordt nooit
geschreven.

De regels zijn: een levende cel met minder dan twee of meer dan drie buren sterft;
met twee of drie buren blijft zij leven; een dode cel met precies drie buren wordt
levend. In alle andere gevallen blijft de cel dood.

## Startbord en functies

Begin met deze verticale 5x5-blinker:

```python
bord = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]


def copy_board(board):
    result = []
    for row in board:
        result = result + [row[:]]
    return result
```

`copy_board` is gegeven. Gebruik haar om de volgende generatie onafhankelijk op
te bouwen. Ontwerp zelf de drie andere functies. Dit skelet staat volledig in
deze extra, zodat je geen andere opgave hoeft te kopiëren:

```python
def count_neighbors(board, row, col):
    # loop over de acht relatieve buurposities
    # tel buiten het bord als 0
    pass


def next_cell(board, row, col):
    # gebruik count_neighbors en de regels hierboven
    pass


def next_generation(board):
    result = copy_board(board)
    # bereken elke cel uit board en schrijf alleen naar result
    pass
```

## Test je tussenstappen

Test een hoek, rand en binnen-cel met dit bord:

```python
voorbeeld = [
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
assert count_neighbors(voorbeeld, 0, 0) == 1  # hoek
assert count_neighbors(voorbeeld, 0, 2) == 2  # rand
assert count_neighbors(voorbeeld, 2, 2) == 2  # binnenkant
```

De eerste generatie van de blinker is:

```text
00000       00000
00100       00000
00100  ->   01110
00100       00000
00000       00000
```

Leg deze verwachte waarde vast met een assertion. Controleer ook dat het
invoerbord na \`next_generation\` onveranderd is:

```python
origineel = copy_board(bord)
assert next_generation(bord) == [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
assert bord == origineel
```

Breid alleen daarna uit met twee of meer generaties en eventueel een
afdrukfunctie. Visualisatie en extra patronen zijn facultatief. Als je tijd
krap is, stop je na de gegeven generatie en assertions; de extra mag de
verplichte kern niet verdringen.

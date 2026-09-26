# Extra: Game of Life

Deze extra gebruikt hetzelfde raster als de basis: een rechthoekige lijst van
lijsten met `0` voor dood en `1` voor levend. De kern is klaar vóór je hier
begint. Je mag `copy_board` gebruiken; ontwerp die niet opnieuw.

## Regels en rand

Coördinaten buiten het bord tellen als een dode cel en worden nooit geschreven.
De vier regels zijn: minder dan twee buren sterft; twee of drie blijft leven;
precies drie maakt een dode cel levend; anders blijft de cel dood.

Begin met dit 5x5-blinkerbord en controleer de gegeven generatie.

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

Gebruik het skelet uit de basis voor `count_neighbors`, `next_cell` en
`next_generation`. Voeg minstens deze assertions toe:

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

Breid daarna uit met twee of meer generaties en een afdrukfunctie. Visualisatie is
optioneel. Stop zodra de basisgeneratie en randgevallen werken; extra patronen
mogen geen voorwaarde voor de kern worden.

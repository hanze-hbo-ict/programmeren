# Extra

## Vier op een rij: min-max

Week 6 eindigde met een val. Speel je als X kolom `2`, `3` en `4`, dan verliest
`SimpleAIPlayer`: hij kijkt maar één zet vooruit, en ziet niet dat twee
dreigingen tegelijk niet allebei te blokkeren zijn. Een speler die verder
vooruitkijkt, ziet dat aankomen.

In deze opgave schrijf je zo'n speler: `MinimaxPlayer`, een subklasse van
`Player`. Hij probeert elke zet, bekijkt hoe de tegenstander daarop het best kan
antwoorden, en hoe hij zelf daar weer op kan antwoorden, een aantal zetten diep.
`host_game` verandert er niet voor: een nieuwe soort speler is één subklasse meer.

Je werkt verder in je bestand `vier_op_een_rij.py` van week 6.

### Min-max

Elk bord krijgt een waarde:

| Bord | Waarde |
|---|---|
| X heeft gewonnen | `-100` |
| niemand heeft gewonnen | `0` |
| O heeft gewonnen | `100` |

X wil een zo laag mogelijke waarde, O een zo hoog mogelijke. Om een zet te
waarderen, kijk je wat de tegenstander erna het best kan doen. De tegenstander
kiest de zet die voor hem het best is. Daarvoor kijkt hij weer naar wat jij
daarna kunt doen, enzovoort. Hoeveel zetten diep een speler zo kijkt, heet zijn
**ply**. Op de diepste laag kijkt hij niet verder, en telt de waarde van het bord
zoals het dan is.

Een voorbeeld met ply 2. X is aan zet en twijfelt tussen kolom `2` en kolom `3`:

```{mermaid}
graph TD
    A["X aan zet: kiest het minimum, 0"] -->|"X speelt 2"| B["O aan zet: kiest het maximum, 100"]
    A -->|"X speelt 3"| C["O aan zet: kiest het maximum, 0"]
    B -->|"O speelt 0"| D["100: O wint"]
    B -->|"O speelt 1"| E["0"]
    C -->|"O speelt 0"| F["0"]
    C -->|"O speelt 1"| G["0"]
```

Speelt X kolom `2`, dan kan O daarna winnen. O kiest het maximum, dus die zet is
voor X `100` waard. Speelt X kolom `3`, dan is het beste wat O kan doen een bord van
`0`. X kiest het minimum, en speelt dus kolom `3`. Omdat X het minimum kiest en O
het maximum, heet dit **min-max**.

### Het plan

| Onderdeel | Doet |
|---|---|
| `Board.score()` | een nieuwe methode: de waarde van het bord, `-100`, `0` of `100` |
| `ScoredMove` | een zet met zijn waarde; met `<` en `==` vergelijk je twee zetten |
| `MinimaxPlayer` | een subklasse van `Player`, die met min-max een zet kiest |

Een `MinimaxPlayer` heeft naast `ox` twee attributen:

| Attribuut | Wat het is |
|---|---|
| `tbt` | de keuzestrategie (*tiebreaking type*) als er meer even goede zetten zijn: `"LEFT"`, `"RIGHT"` of `"RANDOM"` |
| `ply` | het aantal zetten dat de speler vooruitkijkt, een integer van `0` of meer |

Van `Board` gebruikt de speler alleen methoden en properties, zoals `allows_move`,
`add_move`, `del_move`, `is_full`, `width` en de nieuwe `score`. Aan `_data` komt
hij niet.

### Wat je gaat maken

| Stap | Wat | Doet |
|---|---|---|
| 1 | `Board.score()` | de waarde van een bord |
| 2 | `ScoredMove` | een zet met een waarde, die zich laat vergelijken |
| 3 | `MinimaxPlayer` | de constructor, en `best`: de beste zet voor X of voor O |
| 4 | `tiebreak_move` | kiezen tussen even goede zetten |
| 5 | `scored_moves` | een zet met waarde voor elke kolom; krijg je cadeau |
| 6 | `scores_for` | het hart: recursief vooruitkijken |
| 7 | `next_move` | de beste zet kiezen |
| 8 | spelen | de val van week 6, en een heel spel |

Zet `import random` bovenaan in `vier_op_een_rij.py`, en de assertions onderaan,
onder de klassen.

## Stap 1: `score(self)`

Een nieuwe methode van `Board`. Ze geeft `-100` als X gewonnen heeft, `100` als O
gewonnen heeft, en anders `0`. Gebruik `wins_for`.

```python
b = Board(7, 6)
b.set_board("01020305")
assert b.score() == -100
b = Board(7, 6)
b.set_board("01010161")
assert b.score() == 100
assert Board(7, 6).score() == 0
```

Op het eerste bord heeft X vier stenen boven elkaar in kolom `0`, op het tweede
heeft O er vier in kolom `1`.

## Stap 2: de klasse `ScoredMove`

Een `ScoredMove` is een zet met zijn waarde: de kolom, en de waarde van het bord na
die zet. Schrijf de klasse buiten `Board` en `Player`:

| Methode | Doet |
|---|---|
| `__init__(self, col, score)` | slaat de kolom op in `self.col` en de waarde in `self.score` |
| `__repr__(self)` | geeft een string als `"ScoredMove(3, 100)"` |
| `__eq__(self, other)` | `True` als `other` een `ScoredMove` is met dezelfde waarde; is `other` iets anders, dan `False` |
| `__lt__(self, other)` | `True` als deze zet een lagere waarde heeft dan `other`; is `other` geen `ScoredMove`, dan een `TypeError` |

`__eq__` kijkt alleen naar de waarde, niet naar de kolom. Twee zetten zijn gelijk
als ze even goed zijn.

Hier zit de operator overloading van deze week. Twee zetten vergelijken is twee
bordtoestanden vergelijken: het bord na de ene zet tegen het bord na de andere.
Met `__lt__` werken `min` en `max` op een lijst zetten. `max` vraagt of de ene zet
groter is dan de andere; een methode voor `>` heeft `ScoredMove` niet, en dan
draait Python de vergelijking om naar `<`. Bij even goede zetten geven `min` en
`max` de eerste in de lijst.

```python
a = ScoredMove(2, 0)
b = ScoredMove(4, 0)
c = ScoredMove(5, 100)
assert a.col == 2
assert a.score == 0
assert repr(c) == "ScoredMove(5, 100)"
assert a == b
assert a is not b
assert not a == c
assert not a == 0
assert a < c
assert not a < b
assert c > a
assert min([c, a, b]).col == 2
assert max([a, c, b]).col == 5
```

## Stap 3: de klasse `MinimaxPlayer`

Schrijf `MinimaxPlayer` als subklasse van `Player`:

| Methode | Doet |
|---|---|
| `__init__(self, ox, tbt, ply)` | laat de constructor van `Player` `ox` opslaan, en slaat `tbt` en `ply` op |
| `best(self, moves)` | geeft uit de lijst `ScoredMove`s `moves` de beste zet voor deze speler: voor X die met de laagste waarde, voor O die met de hoogste |

`MinimaxPlayer` erft `opponent` van `Player`, en in stap 7 overschrijft hij
`next_move`.

:::{admonition} Hint
:class: tip

Voor X is de beste zet `min(moves)`, voor O `max(moves)`.
:::

```python
p = MinimaxPlayer("X", "LEFT", 2)
assert p.ox == "X"
assert p.tbt == "LEFT"
assert p.ply == 2
assert p.opponent() == "O"
moves = [ScoredMove(0, 100), ScoredMove(1, -100), ScoredMove(2, 0)]
assert p.best(moves).col == 1
assert MinimaxPlayer("O", "LEFT", 2).best(moves).col == 0
```

In week 6 vroeg je je af of de meest linkse kolom wel een goede standaardzet is
voor `Player`. In het practicum van deze week dwingt `Creature` met een
`NotImplementedError` af dat elke subklasse `special_move` overschrijft. Bij
`Player` doe je dat niet: `SimpleAIPlayer` valt met `super().next_move(board)`
terug op de standaardzet, en dat kan alleen als die een kolom teruggeeft.

## Stap 4: `tiebreak_move(self, moves)`

Vaak zijn meer zetten even goed. `tiebreak_move` krijgt een niet-lege lijst even
goede `ScoredMove`s, van links naar rechts, en geeft de kolom terug van de zet die
de speler kiest:

| `self.tbt` | Kiest |
|---|---|
| `"LEFT"` | de meest linkse zet |
| `"RIGHT"` | de meest rechtse zet |
| `"RANDOM"` | een willekeurige zet uit de lijst |

`tiebreak_move` geeft de kolom terug, niet de `ScoredMove`.

:::{admonition} Hint
:class: tip

`random.choice(L)` geeft een willekeurig element van de lijst `L`.
:::

```python
moves = [ScoredMove(2, 0), ScoredMove(4, 0), ScoredMove(5, 0)]
assert MinimaxPlayer("X", "LEFT", 1).tiebreak_move(moves) == 2
assert MinimaxPlayer("X", "RIGHT", 1).tiebreak_move(moves) == 5
assert MinimaxPlayer("O", "RANDOM", 1).tiebreak_move([ScoredMove(3, 0)]) == 3
```

Probeer `"RANDOM"` ook een paar keer met de lijst `moves`: de kolom is dan elke keer
`2`, `4` of `5`.

## Stap 5: `scored_moves(self, board)`

Deze methode krijg je cadeau. Ze maakt een `ScoredMove` voor elke kolom waarin een
zet mag. De waarden komen uit `scores_for`, die je in stap 6 schrijft. Die geeft
voor elke kolom een waarde, en `None` voor een kolom waarin geen zet meer mag.

```python
    def scored_moves(self, board):
        """Geeft een ScoredMove voor elke kolom waarin een zet mag."""
        scores = self.scores_for(board)
        moves = []
        for col in range(board.width):
            if scores[col] is not None:
                moves.append(ScoredMove(col, scores[col]))
        return moves
```

Neem haar over in `MinimaxPlayer`. Testen kan pas na stap 6.

## Stap 6: `scores_for(self, board)`

Dit is het hart van de speler. `scores_for` geeft een lijst met één element per
kolom van `board`: de waarde van het bord als de speler in die kolom speelt, gezien
`self.ply` zetten vooruit.

Loop over de kolommen, en geef elke kolom zo een waarde:

1. **Mag er geen zet in de kolom**, dan is haar element `None`.
2. **Heeft iemand al gewonnen, of is `self.ply` gelijk aan `0`**, dan kijkt de
   speler niet verder: de waarde is `board.score()`.
3. **Anders** zet de speler een steen `self.ox` in de kolom, en kijkt:
   - Is het spel daarna voorbij, doordat iemand wint of doordat het bord vol is,
     dan is de waarde `board.score()`.
   - Is het spel niet voorbij, dan is de tegenstander aan zet. Maak een
     tegenstander: een `MinimaxPlayer` met de andere steen, dezelfde `tbt` en één
     ply minder. De waarde van de kolom is de waarde van de beste zet van die
     tegenstander: `opponent.best(opponent.scored_moves(board)).score`.

   Haal daarna de steen weer weg met `del_move`. Na afloop is het bord precies
   zoals ervoor, net als bij `cols_to_win`.

De recursie zit in de laatste stap: `opponent.scored_moves` roept
`opponent.scores_for` aan, met één ply minder. Na `self.ply` lagen is de ply `0`,
en daar stopt het.

:::{admonition} Waarom één ply minder?
:class: tip

Kijk jij vier zetten vooruit en is de eerste zet de jouwe, dan blijven er voor de
tegenstander nog drie over. Zo werkt de recursie naar het geval waarin niemand
meer vooruitkijkt: ply `0`.
:::

Test `scores_for` op dit bord, met `set_board("1211244445")`:

```text
| | | | | | | |
| | | | | | | |
| | | | |X| | |
| |O| | |O| | |
| |X|X| |X| | |
| |X|O| |O|O| |
---------------
 0 1 2 3 4 5 6
```

```python
b = Board(7, 6)
b.set_board("1211244445")
before = repr(b)
assert MinimaxPlayer("X", "LEFT", 0).scores_for(b) == [0, 0, 0, 0, 0, 0, 0]
assert MinimaxPlayer("O", "LEFT", 1).scores_for(b) == [0, 0, 0, 100, 0, 0, 0]
assert MinimaxPlayer("X", "LEFT", 2).scores_for(b) == [100, 100, 100, 0, 100, 100, 100]
assert MinimaxPlayer("X", "LEFT", 3).scores_for(b) == [
    100,
    100,
    100,
    -100,
    100,
    100,
    100,
]
assert MinimaxPlayer("O", "LEFT", 3).scores_for(b) == [0, 0, 0, 100, 0, 0, 0]
assert MinimaxPlayer("O", "LEFT", 4).scores_for(b) == [
    -100,
    -100,
    -100,
    100,
    -100,
    -100,
    -100,
]
assert repr(b) == before

b = Board(7, 6)
b.set_board("000000")
assert MinimaxPlayer("X", "LEFT", 1).scores_for(b) == [None, 0, 0, 0, 0, 0, 0]
```

Wat de speler ziet, per regel:

| Speler | Ply | Ziet |
|---|---|---|
| X | 0 | niets: hij kijkt niet vooruit, en elk bord is `0` |
| O | 1 | als O aan zet was: winst in kolom `3` |
| X | 2 | elke zet behalve kolom `3` laat O daarna winnen |
| X | 3 | met kolom `3` wint X zelf, twee zetten later |
| O | 3 | nog geen gevaar buiten kolom `3` |
| O | 4 | elke zet behalve kolom `3` verliest |

De test met ply 4 kan een paar seconden duren.

## Stap 7: `next_move(self, board)`

`MinimaxPlayer` overschrijft `next_move`:

1. Maak met `scored_moves` de lijst zetten.
2. Bepaal met `best` de beste zet.
3. Maak een lijst van de zetten die even goed zijn als de beste: de zetten
   waarvoor `move == best` geldt.
4. Geef de kolom terug die `tiebreak_move` uit die lijst kiest.

In stap 3 werkt `==` via je `__eq__`. Dat vergelijkt de waarde: zo vind je alle
even goede zetten, en niet alleen de ene die `best` teruggaf.

```python
b = Board(7, 6)
b.set_board("1211244445")
assert MinimaxPlayer("X", "LEFT", 1).next_move(b) == 0
assert MinimaxPlayer("X", "RIGHT", 1).next_move(b) == 6
assert MinimaxPlayer("X", "LEFT", 2).next_move(b) == 3
assert MinimaxPlayer("X", "RIGHT", 2).next_move(b) == 3
assert MinimaxPlayer("X", "RANDOM", 2).next_move(b) == 3
```

Met ply 1 ziet X geen verschil tussen de kolommen, en beslist `tbt`. Met ply 2 is
er maar één goede zet, en maakt `tbt` niet uit.

## Stap 8: spelen

Eerst de val van week 6. X heeft kolom `2` en `3` gespeeld, O kolom `0`:

```text
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
|O| |X|X| | | |
---------------
 0 1 2 3 4 5 6
```

Blokkeert O nu niet, dan speelt X kolom `1` of `4`, en heeft hij drie op een rij met
aan beide kanten een lege plek: twee dreigingen tegelijk. `SimpleAIPlayer` ziet
niets en valt terug op kolom `0`. Een `MinimaxPlayer` met ply 3 ook nog: de
winst van X komt pas bij de vierde zet vanaf nu. Met ply 4 ziet O het wel, en
blokkeert in kolom `1`. Speelt X daarna kolom `4`, dan blokkeert O in kolom `5`, en
kan X niet meer met één zet winnen.

```python
b = Board(7, 6)
b.set_board("203")
assert SimpleAIPlayer("O").next_move(b) == 0
assert MinimaxPlayer("O", "LEFT", 3).next_move(b) == 0
assert MinimaxPlayer("O", "LEFT", 4).next_move(b) == 1

b = Board(7, 6)
b.set_board("20314")
assert MinimaxPlayer("O", "LEFT", 4).next_move(b) == 5
b.add_move(5, "O")
assert b.cols_to_win("X") == []
```

Laat daarna een `MinimaxPlayer` een heel spel spelen tegen de eenvoudige speler:

```python
b = Board(7, 6)
b.host_game(SimpleAIPlayer("X"), MinimaxPlayer("O", "LEFT", 3))
assert b.wins_for("O")
```

Kijk naar de eerste zetten. Zolang niemand binnen drie zetten kan winnen, zijn alle
kolommen voor O `0` waard, en kiest `tbt` de meest linkse. Daarin speelt min-max
precies zoals de standaardzet van `Player`.

Speel daarna zelf tegen de computer:

```text
In [1]: b = Board(7, 6)

In [2]: b.host_game(HumanPlayer("X"), MinimaxPlayer("O", "LEFT", 4))
```

Probeer de val van week 6 opnieuw.

## Tot slot

`host_game` is sinds week 6 niet veranderd, en toch speelt het nu tegen een
speler die vier zetten vooruitkijkt. Een nieuwe soort speler was één subklasse
meer. Van het bord gebruikt die speler alleen de methoden, en zetten vergelijkt hij
met `<` en `==`, via je eigen `ScoredMove`.

Verder kijken wordt snel duur. Elke ply erbij probeert voor elke zet weer zeven
antwoorden, dus het werk wordt telkens ongeveer zeven keer zo groot. Op een leeg
bord kost één zet met ply 4 al een paar seconden, en met ply 5 ongeveer zeven keer
zo lang. En zolang niemand binnen de ply kan winnen, is elke zet `0` waard, en speelt
de speler niet beter dan de meest linkse kolom. Een betere waarde voor een bord
waarop nog niemand gewonnen heeft, zou helpen: tel bijvoorbeeld hoeveel rijen van
drie een speler heeft met een lege plek erbij. Dan kiest de speler ook zinnig
voordat er iets te winnen valt.

# Extra

## Vier op een rij: spelers

In week 5 schreef je de klasse `Board`, met `host_game` om twee mensen tegen
elkaar te laten spelen. Nu wil je ook tegen de computer kunnen spelen, of de
computer tegen zichzelf laten spelen.

Daar zit `host_game` in de weg. Die methode doet twee dingen tegelijk: ze houdt
het spel bij, met de beurten en de uitslag, en ze vraagt met `input` om een zet.
Een computerspeler typt niets in. Je zou in `host_game` kunnen controleren wie er
aan de beurt is, een mens of de computer, en voor elk een eigen stuk code
schrijven. Maar dan moet `host_game` veranderen bij elke nieuwe soort speler.

In deze opgave haal je die twee dingen uit elkaar. Het bord houdt het spel bij. Een
**speler** kiest een zet. `host_game` vraagt de speler die aan de beurt is om een
zet, en hoeft niet te weten of dat een mens is of een computer. Dat is
polymorfisme, net als `special_move` in het practicum.

Je werkt verder in je bestand `vier_op_een_rij.py` van week 5.

### Het plan

| Onderdeel | Doet |
|---|---|
| `Board.cols_to_win(ox)` | een nieuwe methode: in welke kolommen wint `ox` met één zet? |
| `Player` | een speler: de steen die hij speelt, en een eenvoudige zet |
| `HumanPlayer` | een subklasse van `Player`: een mens, die zijn zet intypt |
| `SimpleAIPlayer` | een subklasse van `Player`: een computerspeler die één zet vooruitkijkt |
| `ScriptedPlayer` | een speler die een vaste lijst zetten afwerkt, zonder subklasse van `Player` te zijn |
| `Board.host_game(px, po)` | het spel, met twee spelers |

Elke speler heeft hetzelfde attribuut en dezelfde methode:

| Van een speler | Wat het is |
|---|---|
| `ox` | het attribuut met zijn steen: `"X"` of `"O"` |
| `next_move(board)` | de methode die een kolom teruggeeft waarin een zet mag |

Meer gebruikt `host_game` niet van een speler. Een speler kijkt naar het bord via
de methoden en properties van `Board`, zoals `allows_move` en `width`, en komt
nooit aan `_data`.

**Let op: `host_game` verandert.** In week 5 was het `host_game(self)`. In deze
opgave wordt het `host_game(self, px, po)`, met twee spelers als argument. De
andere methoden van `Board` blijven zoals ze zijn.

### Wat je gaat maken

| Stap | Wat | Doet |
|---|---|---|
| 1 | `cols_to_win` | de kolommen waarin een speler met één zet wint |
| 2 | `Player` | een speler met een standaardzet |
| 3 | `HumanPlayer` | een mens die zijn zet intypt |
| 4 | `host_game(px, po)` | het spel met twee spelers |
| 5 | `SimpleAIPlayer` | winnen als het kan, blokkeren als het moet |
| 6 | `ScriptedPlayer` | een speler die een vaste lijst zetten afwerkt |
| 7 | spelen | de computer tegen zichzelf, en jij tegen de computer |

Zet de assertions onderaan in `vier_op_een_rij.py`, onder de klassen.

## Stap 1: `cols_to_win(self, ox)`

Een nieuwe methode van `Board`. Ze geeft een lijst van de kolommen waarin `ox` met
één zet vier op een rij krijgt, van links naar rechts. Kan `ox` met één zet niet
winnen, dan is de lijst leeg.

```text
| | | | | | | |
| | | | | | | |
| | | | | | | |
|O| | | | |X| |
|O| | |O| |X| |
|O| | |X|X|X| |
---------------
 0 1 2 3 4 5 6
```

Op dit bord, `set_board("334050505")`, wint X in kolom `2` en `6` met vier op de
onderste rij, en in kolom `5` met vier boven elkaar. O wint in kolom `0`.

Probeer elke kolom één voor één:

1. Kijk met `allows_move` of een zet in de kolom mag.
2. Zet een steen `ox` in de kolom, met `add_move`.
3. Kijk met `wins_for` of `ox` nu gewonnen heeft. Zo ja, zet de kolom in de lijst.
4. Haal de steen weer weg met `del_move`, voordat je de volgende kolom probeert.

Na afloop is het bord dus precies zoals ervoor.

```python
b = Board(7, 6)
b.set_board("334050505")
before = repr(b)
assert b.cols_to_win("X") == [2, 5, 6]
assert b.cols_to_win("O") == [0]
assert repr(b) == before
assert Board(7, 6).cols_to_win("X") == []
```

## Stap 2: de klasse `Player`

Schrijf een klasse `Player`, buiten de klasse `Board`:

| Methode | Doet |
|---|---|
| `__init__(self, ox)` | slaat de steen op in het attribuut `self.ox` |
| `opponent(self)` | geeft de steen van de tegenstander: `"O"` als `self.ox` `"X"` is, en anders `"X"` |
| `next_move(self, board)` | geeft de meest linkse kolom van `board` waarin een zet mag |

`next_move` loopt dus over de kolommen van het bord, van `0` tot `board.width`,
en geeft de eerste kolom terug waarvoor `board.allows_move(col)` waar is. Op een
vol bord wordt `next_move` niet aangeroepen, want dan is het spel al afgelopen.

```python
b = Board(7, 6)
p = Player("X")
assert p.ox == "X"
assert p.opponent() == "O"
assert Player("O").opponent() == "X"
assert p.next_move(b) == 0
b.set_board("000000")
assert p.next_move(b) == 1
```

De meest linkse kolom is geen goede zet. Het is een standaard: een subklasse die
niets beters weet, valt erop terug. Of een standaardzet die niet goed is wel een
goede standaard is, is een vraag die terugkomt. In week 7 leer je hoe een
superklasse kan afdwingen dat een subklasse een methode overschrijft.

## Stap 3: `HumanPlayer`

Een mens is een speler. Schrijf `HumanPlayer` als subklasse van `Player`. Hij erft
de constructor en `opponent`, en overschrijft alleen `next_move`: die vraagt om
een kolom, net zo lang tot er een zet komt die mag. Dat is de kleine lus uit
`host_game` van week 5, die nu in de speler staat:

```python
        col = -1
        while not board.allows_move(col):
            col = int(input(f"Keuze van {self.ox}: "))
        return col
```

Voer `next_move` een keer uit in de terminal, en typ eerst een kolom die niet
bestaat:

```ipython
In [1]: b = Board(7, 6)

In [2]: HumanPlayer("X").next_move(b)
Keuze van X: 9
Keuze van X: 3
Out[2]: 3
```

`next_move` zet zelf geen steen. Ze kiest alleen een kolom: het zetten doet
`host_game`.

## Stap 4: `host_game(self, px, po)`

Schrijf `host_game` opnieuw, zodat ze twee spelers meekrijgt. `px` speelt met
`"X"` en begint, `po` speelt met `"O"`. Elke beurt gaat zo:

1. Vraag de speler die aan de beurt is om een kolom: `col = player.next_move(self)`.
2. Zet zijn steen met `self.add_move(col, player.ox)`.
3. Druk het bord af.
4. Kijk of deze speler gewonnen heeft, en daarna of het bord vol is. In beide
   gevallen meld je de uitslag en stop je met `break`.
5. Anders is de andere speler aan de beurt.

Druk net als in week 5 aan het begin een welkom af en het lege bord. De uitslag
is `"X wint -- Gefeliciteerd!"`, `"O wint -- Gefeliciteerd!"` of
`"Gelijkspel!"`.

:::{admonition} Hint
:class: tip

Houd de speler die aan de beurt is bij in een variabele `player`, die begint als
`px`. Of het de beurt van `px` was, vraag je met `player is px`: is het hetzelfde
object?
:::

In `host_game` staat nu geen `input` meer, en ook geen `"X"` of `"O"` om te kijken
wie er aan de beurt is. `host_game` weet alleen dat een speler een `ox` heeft en
een `next_move`. Welke `next_move` er draait, hangt af van de speler.

Speel het spel zoals in week 5, met twee mensen:

```text
In [1]: b = Board(7, 6)

In [2]: b.host_game(HumanPlayer("X"), HumanPlayer("O"))
```

Speel de zetten van het voorbeeld van
[week 5](/problems/12_extra.md#stap-10-host_gameself): X kiest `3`, `2`, `1` en
`0`, en O kiest `4`, `4` en `2`. Je ziet dezelfde vragen en dezelfde borden, en
aan het eind `X wint -- Gefeliciteerd!`.

## Stap 5: `SimpleAIPlayer`

Een computerspeler is ook een speler. Schrijf `SimpleAIPlayer` als subklasse van
`Player`. Hij overschrijft `next_move`, en kiest zo:

1. Kan hij zelf met één zet winnen, dan speelt hij de eerste kolom uit
   `board.cols_to_win(self.ox)`.
2. Anders: kan de tegenstander met één zet winnen, dan blokkeert hij de eerste
   kolom uit `board.cols_to_win(self.opponent())`.
3. Anders valt hij terug op de standaardzet van zijn superklasse:
   `super().next_move(board)`.

Hij kijkt dus maar één zet vooruit.

```text
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | |X| | |
| | |O| |X| | |
| | |O| |X| | |
---------------
 0 1 2 3 4 5 6
```

Op dit bord, `set_board("42424")`, wint X in kolom `4`. Voor X is dat dus de
winnende zet, en voor O de zet die blokkeert.

```python
b = Board(7, 6)
b.set_board("42424")
assert SimpleAIPlayer("X").next_move(b) == 4
assert SimpleAIPlayer("O").next_move(b) == 4

b = Board(7, 6)
b.set_board("334050505")
assert SimpleAIPlayer("X").next_move(b) == 2
assert SimpleAIPlayer("O").next_move(b) == 0

b = Board(7, 6)
assert SimpleAIPlayer("X").next_move(b) == 0
```

Op het tweede bord kan O zelf winnen in kolom `0`, en dat gaat vóór het
blokkeren van X.

## Stap 6: `ScriptedPlayer`

Een `ScriptedPlayer` speelt een lijst kolommen af die hij vooraf meekrijgt, één
per beurt. Hij is **geen** subklasse van `Player`, maar hij heeft wel een attribuut
`ox` en een methode `next_move(board)`. Meer heeft `host_game` niet nodig: dat is
duck typing.

| Methode | Doet |
|---|---|
| `__init__(self, ox, moves)` | slaat `ox` op in `self.ox`, en een kopie van de lijst `moves` |
| `next_move(self, board)` | geeft de volgende kolom uit de lijst: bij de eerste aanroep de eerste, bij de tweede de tweede, enzovoort |

:::{admonition} Hint
:class: tip

Houd in een attribuut bij hoeveel zetten de speler al heeft gedaan. Dat getal is
ook de index van de volgende kolom in de lijst.
:::

Met twee `ScriptedPlayer`s speel je een heel spel zonder iets in te typen. Zo kun
je `host_game` testen met een assertion. Dit is het spel uit week 5:

```python
b = Board(7, 6)
b.host_game(ScriptedPlayer("X", [3, 2, 1, 0]), ScriptedPlayer("O", [4, 4, 2]))
assert b.wins_for("X")
assert not b.wins_for("O")
```

`ScriptedPlayer` controleert niet of een zet mag. De lijst moet dus kloppen.

## Stap 7: spelen

Laat de computer tegen zichzelf spelen:

```python
b = Board(7, 6)
b.host_game(SimpleAIPlayer("X"), SimpleAIPlayer("O"))
assert b.wins_for("O")
```

Er zit geen toeval in deze spelers, dus dit spel loopt elke keer hetzelfde. Kijk
naar de eerste zetten. Beide spelers vallen terug op de meest linkse kolom, tot X
drie stenen op de onderste rij heeft, in kolom `0`, `1` en `2`. Dan blokkeert O in
kolom `3`. Aan het eind wint O.

Speel daarna zelf tegen de computer:

```text
In [1]: b = Board(7, 6)

In [2]: b.host_game(HumanPlayer("X"), SimpleAIPlayer("O"))
```

Probeer dit: speel als X kolom `2`, `3` en `4`. Welke zet doet O daarna? En
waarom kun je dan toch winnen? Een speler die maar één zet vooruitkijkt, ziet niet
dat twee dreigingen tegelijk niet allebei te blokkeren zijn.

## Tot slot

`host_game` speelt nu met elke speler die een `ox` heeft en een `next_move`: een
mens, een computer of een lijst zetten. Het bord houdt het spel bij, en een
speler kiest een zet. Een nieuwe soort speler is een nieuwe klasse, en `host_game`
verandert er niet voor. In week 7 schrijf je een speler die verder vooruitkijkt
dan één zet: dat is één subklasse meer.

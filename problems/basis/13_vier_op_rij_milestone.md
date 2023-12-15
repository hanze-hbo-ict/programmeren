# Vier op een rij: Milestone

Dit is een vervolg van de basis opdracht van week 12. [begin van vier op een rij](12_vier_op_rij_begin.md)

## De methode `tiebreak_move`

De methode `tiebreak_move(self, scores)` krijgt `scores` mee, een niet-lege lijst met floating-pointgetallen. **Als er maar één score de hoogste is** in die lijst `scores`, dan moet deze methode het bijbehorende **kolomnummer** teruggeven, niet de score zelf! Merk op dat het kolomnummer gelijk is aan de index in de lijst `scores`. Als er *meer dan één* score de hoogste is, omdat er een paar gelijk zijn, dan moet deze methode het **kolomnummer** van de hoogste score teruggeven, gekozen aan de hand van de keuzestrategie van de speler.

Dus, als de keuzestrategie `'LEFT'` is, moet `tiebreak_move` de **kolom** van de meest linkse hoogste score teruggeven (niet de score zelf). Als de keuzestrategie `'RIGHT'` is, moet `tiebreak_move` de **kolom** van de meest rechtse hoogste score teruggeven (niet de score zelf). En als de keuzestrategie `'RANDOM'` is, dan moet `tiebreak_move` de **kolom** van een willekeurige gekozen hoogste score teruggeven (ook hier niet de score zelf).

Een mogelijke aanpak om deze methode te schrijven is door *eerst een lijst met **indexen** te maken waarvan de waarde in `scores` gelijk is aan het maximum. Als `scores` bijvoorbeeld de lijst `[50, 50, 50, 50, 50, 50, 50]` bevat moet `max_indices` gelijk zijn aan `[0, 1, 2, 3, 4, 5, 6]`. Als aan de andere kant `scores` de lijst `[50, 100, 100, 50, 50, 100, 50]` bevat moet `max_indices` gelijk zijn aan `[1, 2, 5]`...

Het is slim om tests te schrijven voor alle drie keuzestrategieën. Hier zijn er vast twee:

```python
scores = [0, 0, 50, 0, 50, 50, 0]
p = Player('X', 'LEFT', 1)
p2 = Player('X', 'RIGHT', 1)
assert p.tiebreak_move(scores) == 2
assert p2.tiebreak_move(scores) == 5
```

:::{admonition} Tip
:class: tip

Het is handig om eerst het maximum van de lijst te zoeken (met de ingebouwde Python-functie `max`) en daarna de kolom te zoeken waar de waarde maximaal is. *Kies hier een slimme startpositie*; de waarde van `self.tbt` kan helpen om een geschikte startpositie te kiezen van waar je kan zoeken.
:::

## De methode `scores_for`

De methode `scores_for(self, b)` is het hart van de klasse `Player`! Ze moet een lijst scores teruggeven, waarbij de score op index `c` aangeeft hoe "goed" het bord is *nadat de speler een zet in kolom `c` doet*. "Goedheid" wordt gemeten door wat er in het spel zal gebeuren na `self.ply` zetten.

Dit is een complexe, recursieve functie! Hier is een overzicht van hoe deze functie kan werken:

Eerst maakt deze methode een lijst (bijvoorbeeld met de naam `scores`) waarvan de lengte gelijk is aan het aantal kolommen in het bord `b`, waarbij elk element de waarde 50 heeft. Bedenk dat je hier lijstvermenigvuldiging kan gebruiken: `[50.0] * b.width`

Deze methode lust daarna over alle kolommen.

**Basisgeval:** Als een bepaalde kolom vol is, geeft de methode deze kolom de waarde `-1.0`.

**Nog een basisgeval:** Als `self` het spel *nu al* heeft gewonnen, dan hoeven er geen extra zetten gedaan te worden (dat mag niet eens!); gebruik simpelweg de geschikte score (`100.0`) voor de kolom die nu bekeken wordt.

**Nog weer een basisgeval:** Op dezelfde manier geldt dat als `self.opp_ch()` het spel *nu al* heeft gewonnen, het ook niet nodig is om nog meer zetten te doen; gebruik simpelweg de geschikte score (`0.0`) voor de kolom die nu bekeken wordt.

:::{admonition} Belangrijk
:class: notice

Het is belangrijk dat de controle of de speler wint gebeurt *voor de controle* dat de tegenstander wint, omdat er borden zijn waar beide waar zijn, maar `self` is nu aan de beurt, dus die zou dan winnen!
:::

**Nog een ander basisgeval:** Nu komen we bij het *echte* basisgeval: als de `ply` van het object 0 is, wordt er geen zet gedaaan. Bovendien zijn de situaties waar de kolom vol is of het spel afgelopen is al afgehandeld, dus er is maar één score die je hoeft te geven aan een kolom als de lookahead 0-ply is: **welke score is dat?** Dit is wat je verwacht als de speler helemaal *niet* in de toekomst kijkt.

**Recursief geval:** Als de ply van de speler wel groter is dan 0 en het spel nog niet over is, ***moet de code een zet doen in de kolom die nu bekeken wordt***. Hiervoor gebruik je een aantal methodes uit `Board`. Het is bovendien handig om te kijken of het bij het nieuwe bord het spel nu wel beëindigd is... Als dat zo is, geef dan de kolom de juiste score.

Als deze zet gedaan is, en het spel *niet* voorbij is, is de belangrijkste taak om te bepalen **welke scores de tegenstander aan het nieuwe bord zou geven**. Dit betekent dat je een tegenstander moet maken (van de klasse `Player`!) en kijkt welke scores de tegenstander aan het bord zou geven. Je kan hiervoor recursie gebruiken om te bepalen wat de zeven scores zijn die de tegenstander zou geven aan zijn volgende zet.

:::{admonition} Hoe maak je een tegenstander
:class: tip

Je maakt gewoon een nieuw object **van het type `Player`**! Bijvoorbeeld met `op = Player(self.opp_ch(), ..., ...)`. Het is veilig om deze nieuwe tegenstander dezelfde keuzestrategie te laten volgen als de speler zelf; dus gelijk aan de waarde van `self.tbt`.
:::

:::{admonition} Wat is het juiste aantal ply dat je moet gebruiken?
:class: tip

Als je zelf bijvoorbeeld vijf zetten vooruitkijkt, hoeveel zetten kijkt je tegenstander dan nog vooruit? We willen toewerken naar het basisgeval waar **niet**, oftewel nul zetten, vooruitgekeken wordt!
:::

De scores die de tegenstander bepaald heeft zijn NIET de scores die `self` moet gebruiken! De tegenstander heeft immers een ander doel dan `self`! Je moet in plaats daarvan uitzoeken welke van de zeven scores de tegenstander, `op`, zou kiezen. Bereken dan de score die jij (`self`) dan zou krijgen: dit is honderd min de beste score van de tegenstander! Gebruik ten slotte deze berekende score als de waarde van een zet in de huidige kolom.

Vergeet niet de steen die je hebt gezet om deze kolom te evalueren weer te ***verwijderen***!

Als alle mogelijke zetten bekeken zijn moet de methode `scores_for` de volledige lijst met scores teruggeven, één per kolom. In een bord met zeven kolommen zijn er dus zeven getallen in de lijst die teruggegeven wordt.

Je kan deze functie testen met onderstaande Python-code; doe dit ook echt, dit is een belangrijke en complexe functie!

```python
b = Board(7, 6)
b.set_board('1211244445')
print(b)

# 0-ply lookahead ziet geen bedreigingen
assert Player('X', 'LEFT', 0).scores_for(b) == [50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]

# 1-play lookahead ziet een manier om te winnen
# (als het de beurt van 'O' was!)
assert Player('O', 'LEFT', 1).scores_for(b) == [50.0, 50.0, 50.0, 100.0, 50.0, 50.0, 50.0]

# 2-ply lookahead ziet manieren om te verliezen
# ('X' kan maar beter in kolom 3 spelen...)
assert Player('X', 'LEFT', 2).scores_for(b) == [0.0, 0.0, 0.0, 50.0, 0.0, 0.0, 0.0]

# 3-ply lookahead ziet indirecte overwinningen
# ('X' ziet dat kolom 3 een overwinning oplevert!)
assert Player('X', 'LEFT', 3).scores_for(b) == [0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0]

# Bij 3-ply ziet 'O' nog geen gevaar
# als hij in een andere kolom speelt
assert Player('O', 'LEFT', 3).scores_for(b) == [50.0, 50.0, 50.0, 100.0, 50.0, 50.0, 50.0]

# Maar bij 4-ply ziet 'O' wel het gevaar!
# weer jammer dat het niet de beurt van 'O' is...
assert Player('O', 'LEFT', 4).scores_for(b) == [0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0]
```

De uitvoer van het `print`-statement is:

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

De laatste test kan een aantal seconden duren, zelfs op een snelle computer...



## Milestone

De milestone, `milestone.py`, moet aan de volgende eisen voldoen:

* Het bevat een klasse `Board` met zoals beschrijven in het practicum van week 12. 
* Het bevat een klasse `Player` met een werkende constructor en `__repr__`
* Deze klasse bevat drie werkende methodes `opp_ch`, `score_board`, `tiebreak_move`
* Deze klasse bevat het hart van het N-ply-lookahead-algoritme, de werkende methode `scores_for`

# Vier op een rij: Eind

Dit is een vervolg van de basis opdracht van week 13. [milestone van vier op een rij](13_vier_op_rij_milestone.md)

## Opdracht 1:  De methode `next_move`

De methode `next_move(self, b)` krijgt een argument `b`, een object van het type `Board`, mee en geeft een integer terug; namelijk het kolomnummer dat het aanroepende object (van klasse `Player`) gaat spelen. Dit is de belangrijkste methode van de klasse `Player` die we zullen gebruiken, maar het is niets meer dan een "wrapper" voor het zware werk dat de andere methodes doen, met name `scores_for`. `next_move` maakt dus gebruik van `scores_for` en `tiebreak_move` om de zet terug te geven.

Om `next_move` te testen kan je code gebruiken die lijkt op het vorige voorbeeld.

```python
b = Board(7, 6)
b.set_board('1211244445')
print(b)

assert Player('X', 'LEFT', 1).next_move(b) == 0
assert Player('X', 'RIGHT', 1).next_move(b) == 6
assert Player('X', 'LEFT', 2).next_move(b) == 3

# de keuzestrategie maakt niet uit
# als er maar één beste zet is...
assert Player('X', 'RIGHT', 2).next_move(b) == 3

# nogmaals, de keuzestrategie maakt niet uit
# als er maar één beste zet is...
assert Player('X', 'RANDOM', 2).next_move(b) == 3
```

## Een spel tegen de AI spelen

Om Vier op een rij tegen de AI te spelen gaan we een methode toevoegen aan de klasse `Board`.

## Opdracht 2: De methode `play_game`

Je kan je implementatie testen door de methode `play_game(self, px, po)` aan de klasse `Board` toe te voegen. `play_game` doet precies wat het zegt: het roept steeds `next_move` aan op twee objecten van het type
`Player` om het spel te spelen. Deze objecten heten `px` en `po`.

Er is nog één extra detail in `play_game`: je moet je code om Vier op een rij te spelen zowel tegen zichzelf
kunnen laten spelen, maar ook tegen een mens. Dat wil zeggen dat als `px` of `po` de string `'human'` bevat in plaats van een object van het type `Player`, `play_game` moet wachten en de gebruiker moet vragen in welke kolom deze wil spelen, met foutcontroles net zoals in `host_game`.

:::{admonition} Zelf schrijven?
:class: notice

Je mag natuurlijk `play_game` zelf schrijven, als je dat een leuke uitdaging vindt. Anders kan je deze methode vinden in de [begincode voor de klasse `Board`](../assets/board.py).
:::

Probeer de voorbeelden hieronder; deze zijn niet afhankelijk van een willekeurige waarde, dus je kan ze goed gebruiken om `play_game` en je AI voor Vier op een rij te testen!

```ipython
In [1]: px = Player('X', 'LEFT', 0)

In [2]: po = Player('O', 'LEFT', 0)

In [3]: b = Board(7, 6)

In [4]: b.play_game(px, po)

# Veel borden overgeslagen...

|O|O|O| | | | |
|X|X|X| | | | |
|O|O|O| | | | |
|X|X|X| | | | |
|O|O|O| | | | |
|X|X|X|X| | | |
---------------
 0 1 2 3 4 5 6

X wint!
```

Voorbeeld 2 (merk op dat dit spel eerder afgelopen is!):

```ipython
In [5]: px = Player('X', 'LEFT', 1)

In [6]: po = Player('O', 'LEFT', 1)

In [7]: b = Board(7, 6)

In [8]: b.play_game(px, po)

# Veel borden overgeslagen...

|O|O| | | | | |
|X|X| | | | | |
|O|O| | | | | |
|X|X| | | | | |
|O|O|O| | | | |
|X|X|X|X| | | |
---------------
 0 1 2 3 4 5 6

X wint!
```

Voorbeeld 3 (de speler met hogere ply wint niet altijd!):

```ipython
In [1]: px = Player('X', 'LEFT', 3)

In [2]: po = Player('O', 'LEFT', 2)

In [3]: b = Board(7, 6)

In [4]: b.play_game(px, po)

# Veel borden overgeslagen...

|O|O|X|X|O|O| |
|X|X|O|O|X|X| |
|O|O|X|X|O|O| |
|X|X|O|O|X|X| |
|O|O|X|O|O|O|O|
|X|X|X|O|X|X|X|
---------------
 0 1 2 3 4 5 6

O wint!
```

## Opdracht 3:  Uitbreidingen

Je hebt nu een AI voor Vier op een rij geschreven! Om je project af te ronden, moet je nog één, of meer, als je dat leuk vindt, van de volgende uitbreidingen maken.

### Een variatie op Vier op een rij!

Voor deze optie ga je *de regels van Vier op een rij aanpassen*. We raden je aan een variant te maken in plaats van een compleet ander spel.

Pas de klassen `Board` en `Player` aan om je alternatieve spel te implementeren! Je hoeft dit niet in een andere klasse `Player` of `Board` te doen: je mag gewoon een nieuwe methode `play_game` maken, eventueel met een andere toepasselijke naam!

Als je deze optie kiest raden we aan de regels van Vier op een rij te *veranderen*; in ieder geval in het begin. Je kan bijvoorbeeld variaties uit deze lijst kiezen:

* Voeg een kans toe (bijvoorbeeld 10%) dat het spel de zet die je kiest totaal negeert en een willekeurige andere zet kiest...
* Verwissel om de zoveel tijd willekeurig een `X` en een `O`!
* Laat de speler het bord "omdraaien", alsof deze 180 graden gedraaid wordt (de stenen vallen niet uit het bord!)
* Laat een rij stenen verdwijnen als deze helemaal vol is (net zoals bij Tetris; dit leidt tot interessante strategieën!)
* Laat de zwaartekracht "diagonaal" werken, of een andere richting, of zelfs continu veranderen!
* Je mag ook andere varianten bedenken!


### Statische bordevaluatie in je AI

Aangezien n-ply-lookahead altijd hetzelfde werkt verschillen AI's niet op de manier waarop ze zoeken, maar op de manier waarop ze borden *evalueren* aan het eind van de zoektocht; als het spel dus geen winst of verlies is.

In het overzicht hierboven stellen we voor deze borden een waarde van 50 (op een schaal van 0 tot en met 100) te geven, maar dit kan veel uitgebreider. Een functie die deze borden waar niet gewonnen of verloren is een nauwkeurigere waarde geeft wordt soms een "statische-bordevaluatiefunctie" genoemd, omdat het alleen kijkt naar de *huidige* toestand van het bord. Deze statische evaluatie maakt het verschil in de vaardigheden van twee verschillende spel-AI's. Statische bordevaluatie probeert menselijke "intuïtie" over het spel vast te leggen, en wordt door veel computerspelers gebruikt in een grote verscheidenheid aan spellen, bijvoorbeeld [Hydra, een hele goede schaakcomputer](https://nl.wikipedia.org/wiki/Hydra_(schaakcomputer)) en [programma's die Go spelen](https://deepmind.com/research/alphago/). Programma's zoals [pokerprogramma's](https://webdocs.cs.ualberta.ca/~games/poker/man-machine/) doen dit ook, maar ze modelleren meer dan alleen de toestand van het spel. De kans op toekomstige toestanden en de gewoontes van andere spelers worden ook gemodelleerd.

Voor deze optie moet je de gebruiker de mogelijkheid geven op twee verschillende manieren te spelen:

* Simpele evaluatie: 0-50-100 OF
* Simme evaluatie

Implementeer nu een statische-bordevaluatiefunctie die geavanceerder is dan de 0-50-100-versie. Gebruik hiervoor een nieuwe methode `score_board_for_tourney`; bewaar je oude functies wel, voor als er iets mis gaat!

Deze nieuwe methode moet een ***nauwkeurigere evaluatie*** teruggeven van hoe goed of slecht een bord `b` is voor
`self.ox`; nauwkeuriger dan de simpele 0-50-100-score die de normale `Player` gebruikt.

De methode `score_board_for_tourney` mag **niet** in de toekomst kijken naar mogelijke zetten; in plaats daarvan kan ze eigenschappen gebruiken zoals:

* Hoe centraal staan mijn stenen ten opzichte van die van mijn tegenstander?
* Heb ik (niet geblokkeerde) rijen van 2 stenen? Heeft mijn tegenstander die?
* Hetzelfde voor (niet geblokkeerde) rijen van 3 stenen.
* En andere eigenschappen over het **huidige** board die je wilt berekenen.

De enige randvoorwaarde voor de functie `score_board_for_tourney(self, b)` is dat het een getal (een `float`) moet teruggeven voor elk bord dat meegegeven wordt, waarbij een hoger getal betekent dat het een beter bord is (voor `self.ox`). Aangezien de methode een *bord* en geen *kolom* evalueert, mag je negatieve getallen gebruiken voor *heel* slechte borden... Maar misschien vind je het makkelijker om de scores tussen de 0 en de 100 te laten vallen (0 = verloren, 100 = gewonnen). Je mag er ook vanuit gaan dat het bord 7 kolommen en 6 rijen heeft, zoals in de standaardversie van het spel.

Je mag aspecten van de functie `score_board_for_tourney(self, b)` willekeurig maken, als je dat wilt.

Om je functie `score_board_for_tourney` te testen kan je je methode `scores_for` kopiëren en plakken en de kopie `scores_for_tourney` noemen. Vervang dan de oude code

```python
elif self.ply == 0:
    scores[col] = 50.0
```

door de nieuwe versie

```python
elif self.ply == 0:
    scores[col] = self.score_board_for_tourney(b)
```

Je kan deze methode dan gebruiken om zelf tegen de computer spelen of deze laten spelen tegen andere spelers die je gemaakt hebt met de klasse `Player`.

Vergeet niet de scores die je berekent af te drukken, zodat je kan zien of ze overeenkomen met je intuïtie!








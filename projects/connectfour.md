# Vier op een rij

In dit project ga je Python gebruiken om een kunstmatige intelligentie (AI) te maken voor het spel Vier op een rij. Hij kan een aantal zetten (*"ply's"*) in het spel vooruitkijken, een optimale zet kiezen *voor die ply*, en (heel misschien) zijn maker verslaan met Vier op een rij!

:::{admonition} Ply's
:class: notice

Hogere ply's kosten meer tijd. Het aantal ply's boven de 5 of 6 zetten kost waarschijnlijk te veel tijd om uit te voeren, dus je zult beperkt zijn bij het kiezen hiervan.
:::

## Achtergrond

Kunstmatige intelligentie heeft een lange geschiedenis; het is zelfs zo dat het vakgebied van kunstmatige intelligentie (ten dele) voortkomt uit het geloof dat door programma's te schrijven die goed zijn in het spelen van strategische spellen we ook intelligentie op het niveau van de mens zouden kunnen programmeren.

Het is gebleken dat dat geloof niet waar was: menselijke intelligentie gaat fundamenteel over iets anders dan het strategisch nadenken over op regels gebaseerde contexten zoals spellen.

De toepassingen van spel-AI zijn echter breder dan alleen spellen. Technieken die de beste uitkomst vinden door *te zoeken door mogelijke situaties* (zoals zetten in een spel) behoren tot de kern van AI en kunnen toegepast worden in veel soorten beslissingsproblemen:

* Robots die moeten bepalen welke actie of beweging ze zullen doen.
* Beslissingssytemen die complexe interacties tussen kunstmatige systemen (en, soms, mensen...) modelleren of simuleren.
* Adaptieve systemen die zich aanpassen aan de handelingen van de gebruiker, bijvoorbeeld om vaardigheden op een nieuw gebied te oefenen (onderwijs en training).

## Het project

Bij dit project ga je een klasse `Player` maken die zetten kan kiezen om een zo sterk mogelijk speler in Vier op een rij te zijn!

Eerst ga je dit bouwen zodat je het in ASCII (tekst) kan spelen.

Nadat je de AI gebouwd hebt moet je deze op minstens één van deze manieren uitbreiden:
1. Door het maken van een grafische interface (2D of 3D) voor het spel die je AI laat zien!
2. Door het maken van een beter bordevaluatie-algoritme dan de 0-50-100-scores (die hieronder worden uitgelegd).
3. Door een bordklasse (die op `Board` lijkt) en een AI (die op `Player` lijkt) voor een **ander** spel van je eigen keuze (of ontwerp!) te maken.

## De klasse `Board`

Je kan de klasse `Board` uit je uitwerking van [opgave 2 van week 10](../week10/wk10ex2.md). Als je deze niet hebt gemaakt kan je ook [onze uitwerking](https://github.com/hanze-hbo-ict/programmeren/raw/master/problems/assets/board.py) gebruiken.

:::{admonition} Bordgrootte
:class: notice

Je mag je klasse `Player` zo schrijven dat deze elk aantal rijen en kolommen ondersteunt, en dat moedigen we ook zeker aan, maar wij zullen hem alleen testen met borden met zeven kolommen en zes rijen. Je mag dit ook best als standaardformaat gebruiken als je wilt!
:::

## De klasse `Player`

In dit project moet je een klasse `Player` schrijven die bordposities van Vier op een rij evalueert en bepaalt waar de volgende zet gedaan moet worden. Je kan voor deze klasse onderstaande begincode gebruiken, maar dit hoeft niet.

```python
class Player:
    """An AI player for Connect Four."""

    def __init__(self, ox, tbt, ply):
        """Construct a player for a given checker, tie-breaking type,
           and ply."""
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__(self):
        """Create a string represenation of the player."""
        s = "Player: ox = " + self.ox + ", "
        s += "tbt = " + self.tbt + ", "
        s += "ply = " + str(self.ply)
        return s
```

### Ontwerp

De aanpak is ongeveer als volgt. Eerst bekijk je elke kolom op het bord, en geef je die kolom een numerieke score:

* `-1.0` als de kolom vol is, en er dus geen zetten in gedaan kunnen worden.
* `0.0` als een zet in deze kolom ervoor zorgt dat de speler **verliest**.
* `50.0` als een zet in deze kolom niet tot winst of verlies leidt voor de speler (in ieder geval niet in de nabije toekomst).
* `100.0` als een zet in deze kolom ervoor zorgt dat de speler **wint**.

Nadat de lijst scores zoals hierboven genoemd is bepaald is, één score per kolom, kiest de computerspeler een zet door de kolom met de hoogste score te vinden en daar te spelen. Als er meerdere kolommen met de hoogste score zijn (en dat gaat ongetwijfeld gebeuren) wordt één van deze keuzestrategieën gebruikt:

* `'LEFT'` kiest, als er meerdere kolommen met de hoogste score zijn, de meest linkse van die kolommen.
* `'RIGHT'` kiest in dat geval de meest rechtse van die kolommen.
* `'RANDOM'` kiest in dat geval willekeurig één van die kolommen.

De meer gedetaillerde beschrijvingen hieronder geven een raamwerk en een aantal tips voor het ontwerp van je
klasse `Player` en hoe je die kan testen.

De klasse `Player` heeft een aantal instantievariabelen en methodes nodig, die we hieronder toelichten. Zorg dat je de tips bekijkt over hoe je de methodes kan testen nadat je ze geschreven hebt!

### Instantievariabelen

De klasse `Player` heeft ten minste drie instantievariabelen nodig:

* Een string van één karakter met de stenen, te weten `'X'` (hoofdletter x) of `'O'` (hoofdletter o), die door deze `Player` gebruikt worden. In de begincode hierboven heet deze variabele `self.ox`.
* Een string met de waarde `'LEFT'`, `'RIGHT'` of `'RANDOM'`, die de *keuzestrategie* voor de speler bepaalt. Dit is de naam van één van de die strategieën die hierboven uitgelegd zijn. In de begincode hierboven heet deze variabele `self.tbt` (voor *tiebreaking type*, de manier waarop gelijke scores beslecht worden).
* Een niet-negatieve integer die het aantal zetten dat de speler in de toekomst zal kijken om mogelijke zetten te evalueren bevat. In de begincode hierboven heet deze variabele `self.ply` omdat een beurt in een spel een *ply* genoemd wordt.

Het staat je natuurlijk vrij om er meer toe te voegen.

### De constructor `__init__`

De constructor `__init__(self, ox, tbt, ply)` voor `Player`-objecten krijgt drie argumenten mee. `self` verwijst naar het object dat aangemaakt wordt en wordt dus automatisch meegegeven aan de constructor. De constructor krijgt ten eerste een string `ox` van één karakter mee; dit zal een `'X'` of een `'O'` zijn. Ten tweede krijgt hij `tbt` mee, de string die de keuzestrategie van de speler bepaalt. Dit is `'LEFT'`, `'RIGHT'` of `'RANDOM'`. Het derde argument, `ply`, is een niet-negatieve integer met het aantal zetten dat de speler in de toekomst kijkt als hij bepaalt waar de volgende zet gedaan moet worden.

In de constructor moet je de instantievariabelen van het object instellen. Er is niet veel meer om te doen. De voorbeeldcode hierboven heeft al een werkende versie van deze constructor.

### De methode `__repr__`

De methode `__repr__(self)` geeft een string terug met een representatie van het aanroepende `Player`-object. Dit moet simpelweg de drie belangrijke eigenschappen van het object afdrukken: welke stenen het gebruikt, de keuzestrategie, en de ply. Ook hiervan is hierboven al een voorbeeldimplementatie gegeven.

Je kan `__init__` en `__repr__` samen bijvoorbeeld zo testen:

```python
p = Player('X', 'LEFT', 2)
assert repr(p) == 'Player: ox = X, tbt = LEFT, ply = 2'
p = Player('O', 'RANDOM', 0)
assert repr(p) == 'Player: ox = O, tbt = RANDOM, ply = 0'
```

Toegegeven, op dit moment is het testen vooral om een idee te krijgen van hoe objecten van het type `Player` werken.

### De methode `opp_ch`

De methode `opp_ch(self)` moet de **andere** steen teruggeven, dat wil zeggen, welke stenen gebruikt worden door de tegenstander van `self`. Specifiek betekent dit dat als `self` met `'X'` speelt, deze methode `'O'` moet teruggeven en omgekeerd. Vergeet niet de hoofdletter o te gebruiken! Deze methode is makkelijk te testen:

```python
p = Player('X', 'LEFT', 3)
assert p.opp_ch() == 'O'
assert Player('O', 'LEFT', 0).opp_ch() == 'X'
```

### De methode `score_board`

De methode `score_board(self, b)` moet een *enkele* `float`-waarde teruggeven die de score van de invoer `b` bepaalt; je mag ervan uitgaan dat `b` een object van het type `Board` is. Ze moet `100.0` teruggeven als het bord `b` gewonnen is door `self`. Ze moet `50.0` teruggeven als `self` niet gewonnen of verloren heeft, en het moet `0.0` teruggeven als `self` verloren heeft (dat wil zeggen als de tegenstander gewonnen heeft).

Het is slim om alle drie mogelijke uitvoerwaardes te testen; hier is een voorbeeld van hoe je dat kan doen:

```python
b = Board(7, 6)
b.set_board('01020305')
print(b)
p = Player('X', 'LEFT', 0)
assert p.score_board(b) == 100.0
assert Player('O', 'LEFT', 0).score_board(b) == 0.0
assert Player('O', 'LEFT', 0).score_board(Board(7, 6)) == 50.0
```

De uitvoer van het `print`-statement ziet er als volgt uit; verder zou je geen uitvoer moeten krijgen:

```text
| | | | | | | |
| | | | | | | |
|X| | | | | | |
|X| | | | | | |
|X| | | | | | |
|X|O|O|O| |O| |
---------------
 0 1 2 3 4 5 6
```

In de laatste twee asserts zie je dat er objecten gebruikt zijn die geen variabelenaam gekregen hebben; dit is geen probleem, Python zal ze vanzelf in de variabele `self` zetten bij de aanroep.

Merk op dat de keuzestrategie geen invloed heeft op deze methode. Je kan `score_board` sneller implementeren door
deze methode gebruik te laten maken van de methode `wins_for`. Bedenk wel dat deze methode een onderdeel is van de
klasse `Board`. Waarschijnlijk zal de methode `opp_ch` hier van pas komen!

### De methode `tiebreak_move`

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

### De methode `scores_for`

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

### De methode `next_move`

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

### De methode `play_game`

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

## Uitbreidingen

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

Vergeet niet een opmerking met een uitleg van je spel en hoe je het moet spelen toe te voegen aan de uitleg in het bestand `oplevering.txt`.

Als je deze uitbreiding kiest kan je natuurlijk meerdere methodes (of zelfs klassen) toe voegen aan `oplevering.py`!

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

### Graphics!

Ten slotte de derde optie... Deze optie is vermoedelijk het lastigste om te implementeren... Gebruik voor deze uitbreiding turtle graphics of de 3D-graphics van VPython, samen met je AI, om een speelbare versie van
Vier op een rij te maken.

:::{admonition} Opmerking
:class: warning

Het is vaak vrij uitdagend om een werkende Vier op een rij in ASCII te integreren met een grafische interface. Het kan zeker gedaan worden, maar het is niet zo simpel als het misschien lijkt...
:::

Het ontwerp is aan jou, maar je resultaat moet:

* De gebruiker de keuze geven om als 'X' of 'O' te spelen (hoe ze er ook uitzien).
* De gebruiker een moeilijkheidsniveau laten kiezen (het `ply`-niveau van de AI-speler).
* De gebruiker de mogelijkheid geven de computer tegen zichzelf te laten spelen (op twee verschillende niveaus, als dat gewenst is.)
* En tegen de gebruiker spelen en herkennen dat het spel geëndigd is in winst, verlies of gelijkspel.

Je mag de details zelf invullen; we zien je creatieve implementaties van Vier op een rij graag tegemoet (of ze nou wel of niet van ons winnen!)

Vergeet niet een beschrijving bij te voegen met daarin informatie over hoe we je spel moeten gebruiken!

## Inleveren

Je moet dit project in drie stappen inleveren: het begin in week 11, de milestone in week 12 en ten slotte de oplevering.

(connectfour-start)=
### Begin

Het begin, `begin.py`, moet aan de volgende eisen voldoen:

* Het bevat een klasse `Player` met een werkende constructor en `__repr__`
* Deze klasse bevat twee werkende methodes `opp_ch` en `score_board`

(connectfour-milestone)=
### Milestone

De milestone, `milestone.py`, moet aan de volgende eisen voldoen:

* Het bevat een klasse `Player` met een werkende constructor en `__repr__`
* Deze klasse bevat drie werkende methodes `opp_ch`, `score_board`, `tiebreak_move`
* Deze klasse bevat het hart van het N-ply-lookahead-algoritme, de werkende methode `scores_for`

### Oplevering

Voor de oplevering, het laatste inlevermoment voor dit project, moet je je implementatie van de kunstmatige intelligentie afmaken. Je moet hierbij minimaal één van de hierboven genoemde uitbreidingen maken. We zullen je programma testen met de hierboven beschreven functie `play_game`.

De oplevering, `oplevering.py`, moet een complete uitwerking van het project bevatten. In de uitleg moet je beschrijven hoe we je spel moeten gebruiken! Als je ervoor gekozen hebt om een ander spel of een statische evaluatiefunctie te maken, beschrijf dan ook de regels van dat spel, of de keuzes die je gemaakt hebt in je evaluatiefunctie.

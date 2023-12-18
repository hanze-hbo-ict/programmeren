# Vier op een rij: Begin

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




## De klasse `Board`

Je kan de klasse `Board` van het practicum gebruiken en samenvoegen met de klasse Player. 

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

Nadat je de AI gebouwd hebt kan je deze verbeteren door gebruik te maken van een beter bordevaluatie-algoritme dan de 0-50-100-scores (die wordt later uitgelegd).

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

## Opdracht 1: Het begin
a. Creeer een file genaamd begin.py.   
b. Import de python file waar de board klasse instaat. 
```python 
from board.py import *
```
c. Kopieer de klasse Player zoals hierboven staat en voeg toe aan begin.py.  
d. Test of alles werkt.    

Je kan `__init__` en `__repr__` samen bijvoorbeeld zo testen:

```python
p = Player('X', 'LEFT', 2)
assert repr(p) == 'Player: ox = X, tbt = LEFT, ply = 2'
p = Player('O', 'RANDOM', 0)
assert repr(p) == 'Player: ox = O, tbt = RANDOM, ply = 0'
```

Toegegeven, op dit moment is het testen vooral om een idee te krijgen van hoe objecten van het type `Player` werken.

## Opdracht 2:  De methode `opp_ch`

De methode `opp_ch(self)` moet de **andere** steen teruggeven, dat wil zeggen, welke stenen gebruikt worden door de tegenstander van `self`. Specifiek betekent dit dat als `self` met `'X'` speelt, deze methode `'O'` moet teruggeven en omgekeerd. Vergeet niet de hoofdletter o te gebruiken! Deze methode is makkelijk te testen:

```python
p = Player('X', 'LEFT', 3)
assert p.opp_ch() == 'O'
assert Player('O', 'LEFT', 0).opp_ch() == 'X'
```

## Opdracht 3: De methode `score_board`

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


Het begin, `begin.py`, moet aan de volgende eisen voldoen:

* Het bevat een klasse `Board` met zoals beschrijven in het practicum van week 12. 
* Het bevat een klasse `Player` met een werkende constructor en `__repr__`
* Deze klasse bevat twee werkende methodes `opp_ch` en `score_board`


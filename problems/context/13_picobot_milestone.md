# De evolutie van Picobot

Dit is een vervolg van de context opdracht van week 12. [De evolutie van Picobot](12_picobot_begin.md)

## De klasse `World`

Het andere fundamentele onderdeel van je programma is een klasse `World` die een complete Picobot-wereld kan representeren (en ook de positie van Picobot en zijn acties in de wereld). Voor dit project hoeft je klasse `World` alleen een lege ruimte van 25 bij 25 te bevatten en te simuleren.

Picobot, de "robot" die in één cel in de ruimte staat, hoeft geen eigen klasse te hebben: hij kan gewoon gesimuleerd worden vanuit de klasse `World`!

De klasse `World` heeft een aantal gegevens nodig om de toestand van de wereld bij te houden en Picobot daarin te simuleren:

* `self.prow`, de huidige rij waarin Picobot zich bevindt (dit zal veranderen).
* `self.pcol`, de huidige kolom waarin Picobot zich bevindt (dit zal veranderen).
* `self.state`, de huidige toestand van Picobot (dit zal veranderen).
* `self.room`, een lijst-van-lijsten die de tweedimensionale ruimte bevat waarin Picobot zich bevindt (dit lijkt heel erg op `self.data` in `Board` uit Vier op een rij).
* `self.prog`, een object van het type `Program` die de simulatie van Picobot bestuurt.

Als je nog andere instantievariabelen wilt gebruiken kan dat natuurlijk.

Dit is hoe de klasse begint:

```python
class World:
    def __init__(self, initial_row, initial_col, program):
        self.prow = initial_row
        self.pcol = initial_col
        self.state = 0
        self.prog = program
        self.room = [[' '] * WIDTH for row in range(HEIGHT)]
```

:::{admonition} `self.room`
:class: notice

Die lege list is niet de uiteindelijke waarde voor `self.room`! Deze verandert nog!
:::

Je kan terugkijken naar de implementatie van de klasse `Board` uit Vier op een rij als een voorbeeld van hoe je een ruimte in Picobot wilt opslaan; het beginpunt hierboven lijkt daar op! Merk op dat, net als `self.data` bij Vier op een rij, het een redelijke aanpak voor het maken van `self.room` is om een lijst van rijen te maken, die ieder een rij van kolommen is, die ieder een string van één karakter is.

Je moet bovendien zorgen dat de ***buitenrand*** van `self.room` muren bevat, misschien met het karakter `'W'`, of
wat je maar wilt. Als je je ASCII-weergave extra mooi wilt maken kan je `'-'` voor horizontale muren, `'|'` voor verticale muren en `+` voor kruisingen gebruiken!

:::{admonition} Tip
:class: tip

Als je een eenvoudigere aanpak kiest, waarin alle muren een `'+'` zijn, dan wordt alles veel makkelijker door **de plustekens in de ruimte zelf te zetten** met code als deze in je constructor `__init__`, *nadat* je de ruimte met lege spaties gemaakt hebt:

```python
for col in range(WIDTH):
    self.room[0][col] = '+'
```

Merk op dat dit alleen de bovenmuur maakt. Je moet ook de andere drie muren maken, en de `'P'` voor Picobot!

Deze aanpak om de hele inhoud van de ruimte bij te houdn in `self.room` maakt het schrijven van de methode `__repr__` veel makkelijker!
:::

In essentie slaat een object van type `World` een kaart van de ruimte `self.room`, het programma `self.prog` waarmee de ruimte verkend zal worden, en de huidige toestand, rij en kolom van Picobot `self.state`, `self.prow` en `self.pcol` op. Andere informatie opslaan is ook goed.

Daarnaast heeft de klasse `World` natuurlijk een aantal methodes nodig; je mag deze in beginsel zelf kiezen, maar een aantal methodes heb je sowieso nodig.

### De methode `__repr__`

De methode `__repr__(self)` geeft een string terug die de ruimte toont met een spatie voor lege cellen die nog niet bezocht zijn, de muren met welk teken je ook gekozen hebt, de positie van Picobot in de ruimte met een hoofdletter "P" en het karakter `o` (de kleine letter o) voor lege maar eerder bezochte posities in de ruimte. Deze methode is cruciaal voor het debuggen van je Picobot-simulator.

### De methode `get_current_surroundings`

De methode `get_current_surroundings(self)` geeft een omgevingsstring zoals `"xExx"` terug voor de huidige positie van Picobot die in de variabelen `self.prow` en `self.pcol` staat.

### De methode `step`

De methode `step(self)` verplaatst Picobot één stap. Hierbij werk je `self.room`, de toestand, de rij en de kolom van Picobot bij, allemaal aan de hand van het programma `self.prog`. Deze methode geeft niets terug! In plaats daarvan gebruikt ze de waardes `self.prow` en `self.pcol` van Picobot om de huidige omgeving te bepalen (aan de hand van `get_current_surroundings`). Ze gebruikt dan die omgeving en `self.state` om het programma, `self.prog` te vragen de verplaatsing en nieuwe toestand te bepalen. Dit kan gedaan worden via de methode `get_move` van het programma, zoals hierboven beschreven is in de klasse `Program`

Ten slotte moet de methode `step` de positie en toestand van Picobot bijwerken, en ook de ruimte bijwerken (door bijvoorbeeld een cel als leeg maar bezocht te markeren en een andere te markeren als de huidige positie van de `P` van Picobot).

### De methode `run`

Maak ook een methode `run(self, steps)` die het aantal stappen (`steps`) meekrijgt die uitgevoerd moeten worden. De methode `run` moet simpelweg dat aantal stappen uitvoeren met behulp van de method `run`. Dit is een Picobot-simulator!

### De methode `fraction_visited_cells`

Je hebt een methode `fraction_visited_cells(self)` nodig die een floating-pointgetal teruggeeft met het percentage (als kommagetal van `0.0` tot `1.0`) van de cellen in `self.room` die gemarkeerd zijn als *bezocht* (inclusief de huidige positie van Picobot). Dit is niet het aantal stappen, omdat cellen vaker bezocht kunnen worden. In plaats daarvan is dit het aantal unieke posities in de ruimte van Picobot waar hij tijdens het uitvoeren geweest is. Dit is de **fitness-score** voor een Picobot-programma!


## De Opdracht

 `world.py`, moet aan de volgende eisen voldoen:

* Het bevat een klasse `World` met een werkende constructor en `__repr__`
* Deze klasse bevat twee werkende methodes `step`, `run` en ``fraction_visited_cells`

Dit betekent dat je een Picobot-simulator gebouwd hebt; in ieder geval in ASCII.

### Hulp bij het debuggen...
Maak een main.py bestand aan en import zowel `program.py` en `world.py`

Vanuit main.py kan je beide klasse aanspreken.  

Dit is een methode `working` voor de klasse `Program` die lijkt op `randomize`. Het verschil is dat
`working` de regels instelt op een bekend, werkend programma dat de hele lege ruimte bedekt. Deze methode is
handig om te zorgen dat `step`, `run` en `evaluate_fitness` allemaal werken...

```python
def working(self):
    """
    This method will set the current program (self) to a working
    room-clearing program. This is super-useful to make sure that
    methods such as step, run, and evaluate_fitness are working!
    """
    possible_surroundings = ['NExx', 'NxWx', 'Nxxx', 'xExS',
                             'xExx', 'xxWS', 'xxWx', 'xxxS', 'xxxx']
    possible_moves = ['N', 'E', 'W', 'S']
    possible_states = [0, 1, 2, 3, 4]
    for st in possible_states:
        for surr in possible_surroundings:
            if st == 0 and ('N' not in surr):
                val = ('N', 0)
            elif st == 0 and ('W' in surr):
                val = ('E', 2)
            elif st == 0:
                val = ('W', 1)
            elif st == 1 and ('S' not in surr):
                val = ('S', 1)
            elif st == 1 and ('W' in surr):
                val = ('E', 2)
            elif st == 1:
                val = ('W', 0)
            elif st == 2 and ('E' not in surr):
                val = ('E', 2)
            elif st == 2 and ('N' in surr):
                val = ('S', 1)
            elif st == 2:
                val = ('N', 0)
            else:
                stepdir = surr[0]
                while stepdir in surr:
                    stepdir = random.choice(possible_moves)
                val = (stepdir, st)  # blijft in dezelfde toestand
            self.rules[(st, surr)] = val
```
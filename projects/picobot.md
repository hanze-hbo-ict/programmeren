# De evolutie van Picobot

In de eerste week van Programmeren I hebben we Picobot, een virtuele robot, geprogrammeerd. In dit project ga je een Python-programma schrijven die zelf Picobot-programma's **schrijft**!

Sterker nog, je Python-software zal automatisch steeds betere Picobot-programma's laten "evolueren" aan de hand van een opp de natuur geïnspireerde technologie die we een "genetisch algoritme" noemen. Je gebruikt technieken die we bij de colleges over object-georiënteerd programmeren in Python hebben behandeld. Hierdoor zal het eindresultaat relatief kort en elegant zijn!

## Genetische algoritmes

Het belangrijkste idee achter een genetisch algoritme is om te beginnen met een ***populatie*** van *willekeurige* Picobot-programma's.

* Je code bepaalt dan de *"fitness"* ("geschiktheid") van elk van de Picobot-programma's door het een aantal stappen uit te laten voeren en dan te bepalen welk percentage van de ruimte het opvult; dit leidt tot een kommagetal tussen 0.0 en 1.0.
* Je programma selecteert aan de hand hiervan een aantal programma's met de ***hoogste fitness***.
* Uit die verzameling selecteert je programma willekeurige paren programma's om te "paren". Dit paarproces maakt een nieuw Picobot-programma, een "kind", met eigenschappen van de beide Picobot-programma's die zijn "ouders" zijn.
* Bovendien moet je software een klein aantal willekeurige mutaties introduceren bij sommige programma's. Zulke willekeurige mutaties helpen om de diversiteit in de populatie te bewaken, wat belangrijk is voor de fitness van de populatie als geheel.
* Op deze manier heb je een volgende generatie van programma's gemaakt. De volgende generatie is even groot als de vorige generatie, maar heeft hopelijk een hogere fitness.
* Je zal dit proces een aantal keer herhalen; als laatste kies je het programma met de hoogste fitness uit de laatste generatie en *dat* is je volledig geëvolueerde Picobot-programma!

## Picobot

Kijk nog even terug naar de opgaven in week 1 van Programmeren I om je geheugen op te frissen wat betreft de logica van Picobot, en de syntax van de regels.

Je kan ook meteen naar de [Picobot-simulator](https://www.cs.hmc.edu/picobot/) gaan.

## Het project

De code die je schrijft komt in een bestand met de naam `begin.py`, `milestone.py` of `oplevering.py`, afhankelijk van de fase van je project. Vergeet niet bovenaan het bestand de volgende zaken te vermelden:

* Een korte beschrijving van het project
* De datum

Zorg ook dat je de modules die je nodig hebt importeerd, bijvoorbeeld,

* `import random`
* ... en misschien nog andere modules.

Gebruik ten slotte een aantal globale variabelen om *"magische constanten"* in je code te vermijden.

"Magische cinstanten" zijn simpelweg constanten in een programma die "magisch" lijken omdat hun betekenis niet uitgelegd wordt. Het is een slecht idee om ze te gebruiken omdat als je (of iemand anders) later je code opnieuw wilt lezen, het erg lastig is om te begrijpen wat deze getallen doen!

De lege ruimte van Picobot is bijvoorbeeld 25 bij 25 groot (inclusief muren). In plaats van overal in je code het getal `25` neer te zetten, kan je beter een paar global constanten bovenaan je bestand zetten:

```python
HEIGHT = 25
WIDTH = 25
NUM_STATES = 5
```

Die laatste is een limiet op het aantal toestanden in je Picobot-programma's; meer hierover later. Je mag ook andere globale constanten gebruiken; het is gebruikelijk om deze namen te geven die uit alleen maar hoofdletters bestaan (bovendien veranderen ze niet tijdens het uitvoeren van het programma).

Een ander **groot** voordeel van deze globale constanten is dat je ze kan wijzigen, en omdat je ze door de hele code gebruikt, zal die enkele aanpassing overal doorwerken (als je elke individuele `25` moet aanpassen zou dat foutgevoelig zijn; je kan er één missen; en bovendien veel tijd kosten!)

### De klasses `Program` en `World`

Je programma heeft twee basiscomponenten nodig:

* De eerste is een Picobot-programma (of verzameling regels) en
* De tweede is een Picobot-wereld.

Je moet voor elk van deze twee een klasse schrijven:

* `class Program` bevat een Picobot-programma.
* `class World` bevat een Picobot-wereld.

Je hoeft geen aparte klasse voor Picobot zelf te hebben; die zal simpelweg een onderdeel worden van `World` van hierboven.

Je mag ook andere klassen die je zelf ontworpen hebt toevoegen, zeker als je andere functionaliteiten toevoegt, maar deze twee zijn het fundament.

## De klasse `Program`

Je klasse `Program` begint als volgt:

```python
class Program:
    def __init__(self):
        self.rules = {}
```

Wat is die `self.rules`? Het is een dictionary waar de details van het programma in worden opgeslagen! Een Picobot-regel ziet er immers uit als:

```
toestand omgeving -> verplaatsing nieuweToestand
```

Een regel kan er bijvoorbeeld zo uitzien:

```
0 xExx -> N 1
```

Deze regel betekent: "Als ik in toestand 0 ben en de omgeving is `xExx` dan moet ik naar het noorden bewegen en naar toestand 1 gaan".

Dit kan (en doe dit vooral!) in de dictionary opgeslagen worden door de tuple `(0, "xExx")` als sleutel te gebruiken waarbij de bijbehorende waarde de tuple `("N", 1)`.

Een `Program`-object slaat deze regel op in de dictionary `self.rules` zodat de sleutel `(0, "xExx")` de bijbehorende waarde `("N", 1)` krijgt. Of in code:

```python
self.rules[(0, "xExx")] = ("N", 1)
```

Dit is natuurlijk maar een voorbeeld van een Picobot-regel; deze specifieke regel zit misschien niet eens in het programma.

### Lege ruimte (om mee te beginnen)

Begin voor dit project met de lege Picobot-ruimte. (Programma's evalueren om het doolhof op te lossen is moeilijker; die en andere Picobot-werelden zijn een optioneel bonusgedeelte van het project.)

### Begin met maar 5 toestanden

Het is slim om het aantal toestanden die je Picobot-programma's (objecten van de klasse `Program`) gebruiken te beperken.

De ervaring leert dat 5 toestanden een goede waarde is om mee te beginnen. Voor moeilijkere omgevingen kunnen meer toestanden handig zijn. Maar voor eenvoudigere omgevingen vergroten meer toestanden alleen maar de zoekruimte (de verzameling mogelijke Picobot-programma's) en kost het alleen maar meer tijd om programma's te evolueren zonder dat ze betere resultaten geven.

### Geen wildcards!

Gebruik in ieder geval om te beginnen het wildcardkarakter `*` niet in je Picobot-regels.

De wildcard maakt zowel je Picobot-simulator als het evolueren van programma's een stuk moeilijker, omdat hij veel regels vertegenwoordigd met een enkele regel. In plaats daar van moeten al je Picobot-programma's volledig gespecificeerde omgevingen bevatten.

Gelukkig is dit haalbaar, omdat er maar 9 mogelijke omgevingen zijn in de lege ruimte.

### Mogelijke *omgevingen*

Picobot hoeft in de lege ruimte alleen deze 9 omgevingen te overwegen (waarom?):

```text
xxxx
Nxxx
NExx
NxWx
xxxS
xExS
xxWS
xExx
xxWx
```

Daarnaast beperken we Picobot-programma's tot het gebruik van exact 5 toestanden: 0, 1, 2, 3 en 4. (In ieder geval om mee te beginnen.)

Dat is wat de globale constante `NUM_STATES` aan het begin van het programma betekent.

Een volledig gespecificeerd Picobot-programma heeft dus precies 5 * 9 = 45 regels, één voor elke combinatie van toestand en omgeving. Voor elke combinatie hebben we een sleutel `(toestand, omgeving)` en een bijbehorende waarde `(verplaatsing, nieuweToestand)`.

### De constructor `__init__`

De klasse `Program` heeft natuurlijk een constructor `__init__(self)` nodig; deze kent gewoon de lege dictionary toe aan `self.rules`, zoals je hierboven kan zien.

### De methode `__repr__`

Daarnaast heeft de klasse een methode `__repr__(self)` nodig die de stringrepresentatie van het programma **teruggeeft**; Python verwacht dat deze methode een string teruggeeft! Als je een nieuwe regel wilt beginnen in een string, kan je `\n` gebruiken.

:::{admonition} Belangrijk!
:class: notice

Vergeet niet dat `__repr__` een string moet **teruggeven** in plaats van de string af te drukken!
:::

Zorg er in het bijzonder voor dat je methode `__repr__` een string maakt die alle regels in `self.rules` **gesorteerd** bevat, gesorteerd op de sleutels van de dictionary. Dit is handig omdat het betekent dat de programma's makkelijker met elkaar te vergelijken zijn; ze staan immers dan altijd in dezelfde volgorde.

Maar *hoe* kan je de regels gesorteerd afdrukken? Bedenk dat `self.rules` een dictionary is. Als je dus

```python
keys = list(self.rules.keys())
```

gebruikt wordt `keys` een lijst van alle *sleutels* in de dictionary. `keys` is dus een lijst van de vorm
`[(toestand, omgeving), (toestand, omgeving), ...]`. Je kan dan de ingebouwde functie `sorted` als volgt gebruiken:

```python
sorted_keys = sorted(keys)
```

Dit maakt een **gesorteerde** lijst met sleutels, met de naam `sorted_keys`. Top!

:::{admonition} Net zo belangrijk!
:class: danger

Je methode `__repr__` moet het hele Picobot-programma zo teruggeven ***dat je deze direct kan kopiëren en plakken*** in de [Picobot-simulator](https://www.cs.hmc.edu/picobot/). Elke regel moet dus als volgt geformatteerd worden:

```
2 Nxxx -> W 3
```

Hier vind je [voorbeeld-uitvoer](/support/picobot_example) die je als sjabloon kan gebruiken.
:::

### De methode `randomize`

De klasse moet een methode `randomize(self)` bevatten, die een willekeurige volledige set regels genereert voor de dictionary `self.rules` van het programma. Onthoud dat de dictionary leeg begint. Deze methode maakt willekeurige regels, één voor elke combinatie van de `NUM_STATES` mogelijke toestanden; in het begin zijn dit er 5; en de 9 mogelijke omgevingen. Merk op dat er voor 5 toestanden en 9 omgevingen 45 willekeurig gegenereerde regels zijn.

:::{admonition} Sleutels van `rules`
:class: tip

De sleutels (begintoestand, omgeving) van de dictionary zijn ***niet*** willekeurig! Je kan gewoon door alle mogelijke toestanden en alle mogelijke omgevingen lussen. Voor elke combinatie moet je *wel* een willekeurige nieuwe toestand en een willekeurige verplaatsing genereren. Een uitdaging is dat de verplaatsing *geldig moet zijn, dus **niet** tegen een muur aan*!
:::

:::{admonition} Geldige verplaatsingen
:class: tip

Om ervoor te zorgen dat je alleen een geldige verplaatsing kiest voor een gegeven omgeving `pattern` kan je een while-lus die op deze lijkt gebruiken:

```python
movedir = random.choice(POSSIBLE_MOVES)
while movedir in pattern:
    movedir = random.choice(POSSIBLE_MOVES)
```

Hierbij is het wel van belang dat je mogelijke verplaatsingen en je omgevingen allemaal hoofdletters gebruiken voor de mogelijke waarden, maar dat zou geen probleem moeten zijn. Deze `while`-lus blijft willekeurig een waarde kiezen voor `movedir` totdat de waarde *wel* geldig is!
:::

### De methode `get_move`

De methode `get_move(self, state, surroundings)` krijgt een integertoestand en een omgeving (bijvoorbeeld `"xExx"`) mee en moet een tuple teruggeven die de volgende verplaatsing en de nieuwe toestand bevat. Deze methode kan gewoon de dictionary `self.rules` gebruiken om dit te bereiken.

### De methode `mutate`

De methode `mutate(self)` moet willekeurig één regel kiezen uit `self.rules` en moet de waarde (de verplaatsing en de toestand) aanpassen voor die regel. Als het programma bijvoorbeeld een regel bevat die de `(toestand, omgeving) (0, "xExx")` heeft gekoppeld aan de `(verplaatsing, nieuwe_toestand) ("N", 1)`, zou deze vervangen kunnen worden met een nieuwe willekeurig gekozen `(verplaatsing, nieuwe_toestand)` zoals `("S", 2)`. Merk op dat het niet geldig zou zijn om naar "E" te verplaatsen in dit geval, omdat het patroon laat zien dat er een muur naar het oosten is; je code moet willekeurig één van de geldige richtingen kiezen om naar te verplaatsen. (Een extra detail is dat de verandere regel niet hetzelfde moet zijn als de
  originele...)

### De methode `crossover`

De methode `crossover(self, other)` is een methode die een object `other` van het type `Program` meekrijgt. Het moet een nieuw "kind", ook van het type `Program` teruggeven die *sommige* regels van `self` en de rest van `other` bevat. Merk op dat de programma's `self` en `other` precies evenveel regels bevatten! Als we bijvoorbeed 5 toestanden hebben, zijn er omdat er maar 9 mogelijke omgevingen zijn precies 45 regels in het programma.

:::{admonition} Effectieve crossovers
:class: tip

De **effectiefste** manier om de crossover uit te voeren is om een willekeurige "crossover-toestand" te kiezen, van 1 tot en met 3. Stel dat toestand 2 gekozen is. Het kind krijgt dan alle regels van één ouder uit toestanden 0, 1 en 2 en krijgt alle regels van de *andere* ouder uit de overgebleven toestanden, 3 en 4.

Het blijkt dat als je elke regel van een willekeurige ouder kiest, de "genetische code" te veel gehusseld wordt waardoor de kinderen de goede eigenschappen van de ouders niet bewaren.
:::

:::{admonition} Veel voorkomende fout
:class: danger

Een veel voorkomende fout is om het programma van één van de ouders te *wijzigen*, in plaats van een nieuw kind van het type `Program` terug te geven. Dit is niet alleen biologisch een slecht idee, maar zal hier ook niet werken! Waarom niet? Stel je voor dat paren het genoom van een ouder zou aanpassen. Als een ouder een hoge fitness heeft, heeft hij waarschijnlijk meerdere kinderen, die hopelijk veel van de goede eigenschappen van de ouder erven. Als het genoom van de ouder echter *verandert* de eerste keer dat hij paart, is het erg waarschijnlijk dat zijn fitness kleiner wordt! Zijn verdere kinderen hebben daardoor vermoedelijk een lagere fitness dan de eerste.
:::

### Handige hulpmethodes

Het kan bij het schrijven van het genetische algoritme handig zijn om lijsten met `(fitnesswaarde, programma)`-paren te sorteren. Je hebt bijvoorbeeld een lijst van lengte 200 met de vorm: `[(fitness0, programma0), (fitness1, programma1), ..., (fitness199, programma199)]` die je willen sorteren op basis van de *floating-pointwaarde van de fitness*. De ingebouwde functie `sorted` werkt hier heel goed, *behalve als twee fitnesswaardes exact gelijk zijn*, wat zeker zal gebeuren! De functie `sorted` zal dan proberen de volgorde te bepalen door de programma's te sorteren, bijvoorbeeld `programma0` en `programma1`. Het probleem is dat het sorteren van programma's niet gedefinieerd is.

Om het sorteren van programma's te definiëren kan je deze definities van `__gt__` en `__lt__`, de groter-dan- en kleiner-dan-operatoren, in je klasse `Program` plakken. Ze vergelijken niet echt twee programma's; ze geven willekeurig `True` of `False` terug; maar dat is alles wat je nodig hebt om `sorted` te laten werken op lijsten zoals hierboven beschreven.

```python
def __gt__(self, other):
  """Greater-than operator -- works randomly, but works!"""
  return random.choice([True, False])

def __lt__(self, other):
  """Less-than operator -- works randomly, but works!"""
  return random.choice([True, False])
```

(Als je het fijn vindt mag je ook "echte" vergelijkingsoperatoren definiëren voor `Program`, maar dat is niet nodig.)

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

## Wat nu?

Je hebt nu al het grootste deel van het programma geschreven! De rest kan je schrijven in een aantal korte functies (buiten de klassen `Program` en `World`).

### Een willekeurige populatie

Je hebt bijvoorbeeld een erg korte functie nodig die de grootte van een populatie meekrijgt en een populate (een Python-lijst) met dat aantal willekeurige Picobot-programma's teruggeeft.

### Een fitness-evaluatiefunctie `evaluate_fitness`

Een erg korte fitness-evaluatiefunctie die de fitness van een gegeven Picobot-programma bepaalt. Deze functie krijgt de naam `evaluate_fitness(program, trials, steps)`. De argumenten zijn een Picobot-programma `program`, een positieve integer `trials` die het aantal willekeurige beginposities die getest moeten worden, en een positieve integer `steps` die het aantal stappen dat de simulatie mag nemen aangeeft. De functie geeft de fitness (een floating-pointgetal tussen 0.0 en 1.0) terug die overeenkomt met het percentage van de cellen die dit Picobot-programma bezoekt, gemiddeld over het aantal `trials`. Je kan hiervoor `fraction_visited_cells` gebruiken.

Stel je als voorbeeld voor dat `p` een Picobot-programma is en we `evaluate_fitness(p, 42, 1000)` uitvoeren. Deze functie kiest dan een willekeurige startpositie voor Picobot, voert het gegeven programma 1000 stappen lang uit, en berekent het percentage bezochte cellen. Daarna wist het de ruimte, kiest een nieuwe startpositie en doet het nog een keer; 42 keer in totaal.

Na alle 42 tests neemt de code het gemiddelde van het percentage van bezochte cellen van alle pogingen.

:::{admonition} Opmerking
:class: notice

De ruimte bevat 529 cellen (23 bij 23 lege cellen), dus zelfs een programma met relatief hoge fitness heeft een stuk meer dan 529 stappen nodig heeft om een groot deel van de ruimte te vullen, omdat het onwaarschijnlijk is dat het programma erg efficiënt zal zijn. Dat is waarom je misschien 1000 `steps` gebruikt, of zelfs een nog hoger aantal, in plaats van 529.
:::

### De hoofdfunctie `genetic_algorithm`

De **hoofdfunctie** moet naar het onderwerp, genetische algoritmes, vernoemd worden: `genetic_algorithm(pop_size, num_gens)`.

Deze functie `genetic_algorithm(pop_size, num_gens)` moet `pop_size` willekeurige Picobot-programma's genereren als de beginpopulatie (200 is hier een goede waarde voor). Daarna moet de fitness van al deze programma's geëvalueerd worden, en moet je de programma's met de hoogste fitness kiezen. Deze programma's overleven en dienen bovendien als "ouders" voor de volgende generatie.

:::{admonition} List-of-lists
:class: tip

Je kan een lijst met paren met (fitness, programma) sorteren. Stel dat dit de lijst `programs =  [(.4, prog1), (.2, prog2), (.3, prog3)]` is, dan kan je

```python
sorted_programs = sorted(programs)
```

aanroepen en zal je zien dat `sorted_programs` gelijk wordt aan `[(.2, prog2), (.3, prog3), (.4, prog1)]`
:::

:::{admonition} Het aantal overlevende programma's
:class: tip

10% van de populatie (bijvoorbeeld 20 van de 200) is een goede keuze voor het aantal overlevende programma's, maar je mag hier natuurlijk mee experimenteren.
:::

De overlevende programma's moeten **bewaard** blijven als onderdeel van de volgende generatie; die moet vervolgens aangevuld worden met "kinderen", nieuwe programma's.

:::{admonition} Kinderen maken
:class: tip

Om deze kinderen te maken kan je bijvoorbeeld deze aanpak gebruiken:
* Twee willekeurige ouders kiezen uit de programma's met hoge fitness.
* `crossover` gebruiken om een programma te maken die een "kind" is deze twee ouders.
* Af en toe `mutate` gebruiken (de kans hierop moet je zelf inregelen...). Als er te veel mutatie is wordt fitness niet bewaard. Als er te weinig is zal het gebrek aan nieuwe genen de evolutie beperken.

De details van het maken van kinderen bepalen hoe effectief je genetisch algoritme is; hier zul je moeten experimenteren!
:::

Je hebt nu een nieuwe populatie, hopelijk met hogere fitness, dus kan je nu het hele proces herhalen. Het is het beste om elke generatie even groot te laten zijn (`pop_size`), bijvoorbeeld 200.

Aan het eind moet je programma het beste programma uit de laatste generatie teruggeven (en als je wilt afdrukken). Je kan dan dat programma kopiëren en plakken in de Picobot-simulator om hem uit te voeren!

:::{admonition} Programma's bewaren
:class: tip

Je kan het handig vinden om het beste programma van elke generatie op te slaan in een bestand (dat is minder onoverzichtelijk en makkelijker te bewaren). Hier is een stukje code om dit makkelijker te maken:

```python
def save_to_file(filename, p):
    """Saves the data from Program p
        to a file named filename."""
    f = open(filename, 'w')
    print(p, file=f)        # print het Picobot-programma met __repr__
    f.close()

# hier is hoe je dit gebruikt... vermoedelijk in de hoofdlus van genetic_algorithm...
save_to_file('gen1.txt', best_p_in_gen_1)
save_to_file('gen2.txt', best_p_in_gen_2)  # enzovoorts...
```
:::

Ongeacht of je je programma's in bestanden opslaat of op het scherm afdrukt moet je in elke iteratie van de generatielus van `genetic_algorithm` zowel de ***gemiddelde*** als de ***maximale*** fitness van programma's in die generatie van de simulatie afdrukken. Hier is een voorbeeld (waarin de beste programma's niet getoond worden omdat ze naar aparte bestanden worden geschreven):

  ```ipython
  In [42]: genetic_algorithm(200, 15)
  Fitness wordt gemeten met 20 willekeurige tests en met 800 stappen per test:

  Generatie  0
    Gemiddelde fitness:  0.0575675
    Hoogste fitness:  0.217125

  Generatie  1
    Gemiddelde fitness:  0.08800625
    Hoogste fitness:  0.453125

  Generatie  2
    Gemiddelde fitness:  0.1041525
    Hoogste fitness:  0.343625

  Generatie  3
    Gemiddelde fitness:  0.113141875
    Hoogste fitness:  0.41525

  ...

  Generatie 14:
    Gemiddelde fitness:  0.869975625
    Hoogste fitness:  0.880875

  Beste Picobot-programma (ook in gen14.txt):
  3 xExx -> W 3
  1 xxWx -> E 2
  1 NExx -> W 4
  1 xxxS -> N 0
  0 xxWS -> N 1
  3 xxxx -> S 2
   ... rest van het programma overgeslagen ...
  ```

:::{admonition} Hulpfuncties
:class: notice

Als je een aantal hulpfuncties wilt schrijven hiervoor mag dat natuurlijk!
:::

:::{admonition} Keuzes voor de parameters
:class: tip

Als je wilt kan je wat lezen over hoe je de programma's met de hoogste fitness kan kiezen om die zich te laten voortplanten en de [keuzes voor de parameters](/support/picobot_parameters) die daar bij horen (maar het staat je natuurlijk vrij om er mee te experimenteren en andere te kiezen).
:::

### Hoe snel en hoe "goed" moet mijn programma zijn?

Met de parameterwaardes die hierboven genoemd zijn moet het uitvoeren van `genetic_algorithm(200, 20)` ongeveer 60 secondes per generatie duren. Je beginpopulatie heeft vermoedelijk een gemiddelde fitness van ongeveer 1% tot 2%. De gemiddelde fitness moet elke generatie langzaam toenemen; er kunnen hier misschien een paar uitzonderingen op zijn. De maximale fitness neemt normaal gesproken toe, maar ook hier kan die af en toe afnemen.

Na 20 generaties zou je een maximale fitness van 80% tot 90% moeten zien, soms zelfs nog hoger.

## Inleveren

Je moet dit project in drie stappen inleveren: het begin in week 11, de milestone in week 12 en ten slotte de oplevering.

(picobot-start)=
### Begin

Het begin, `begin.py`, moet aan de volgende eisen voldoen:

* Het bevat een klasse `Program` met een werkende constructor en `__repr__`
* Deze klasse bevat een werkende methode `randomize`

(picobot-milestone)=
### Milestone

De milestone, `milestone.py`, moet aan de volgende eisen voldoen:

* Het bevat een klasse `Program` met een werkende constructor en `__repr__`
* Deze klasse bevat een werkende methode `randomize`
* Het bevat een klasse `World` met een werkende constructor en `__repr__`
* Deze klasse bevat twee werkende methodes `step` en `run`

Dit betekent dat je een Picobot-simulator gebouwd hebt; in ieder geval in ASCII. Het genetisch algoritme hoeft nog niet af te zijn voor de milestone, maar als het wel zo is, des te beter!

### Oplevering

Voor de oplevering, het laatste inlevermoment voor dit project, moet je het genetisch algoritme dat Picobot-programma's evolueert afmaken. We zullen je programma testen met de hierboven beschreven functie `genetic_algorithm`.

Test je programma zorgvuldig. Het kan zijn dat je tot de conclusie komt dat je crossover-mechanisme (voor het paren van programma's) niet erg effectief is. Dan moet je experimenteren met andere manieren om crossover te regelen.

De oplevering, `oplevering.py`, moet een complete uitwerking van het project bevatten. In de uitleg moet je in ieder geval het volgende beschrijven:

* Hoe je je code hebt getest en parameters hebt gekozen voor je genetisch algoritme, bijvoorbeeld,
  * Welk percentage van elke populatie je hebt gekozen om mee te "paren"
  * Hoe je paren en mutaties hebt geregeld
* Hoe goed je best geëvolueerde Picobot-programma werkt en *hoe* het werkt.
* Voeg ook het Picobot-programma met de hoogste fitness toe, en de fitnesswaarde, zodat we het kunnen uitvoeren!

## Optionele bonusuitbreidingen

Als je de genetische-algoritmeaspecten van het probleem verder wilt verkennen, kan je deze extra vragen nog onderzoeken:

* Hoe goed kan je een programma evolueren om het *doolhof* op te lossen (met een andere ruimte in `World`...)? Het doolhof is erg moeilijk om op te lossen op deze manier; je kan de ruitvormige ruimte gebruiken als tussenweg.
* Het is mogelijk om een programma met behoorlijke fitness te evolueren *helemaal zonder crossover*! Het idee is dat je het programma met de hoogste fitness bewaart en mutatie gebruikt om de volgende generatie te maken. Dit werkt, maar duurt normaal gesproken langer.

Ontwerp en implementeer de noodzakelijke software-ondersteuning om te testen *hoeveel groter de populatie moet zijn* of *hoeveel meer generaties je nodig hebt* (of allebei) om een programma te evolueren met alleen mutatie dat een even hoge fitness heeft als een programma dat met mutatie en crossover geëvolueerd is.

## Hulp bij het debuggen...

Het kan erg lastig zijn om een Python-programma te debuggen die Picobot-programma's evolueert...

Hier is een stukje code dat hierbij kan helpen...

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


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

De code die je schrijft komt in een bestand met de naam `program.py`, `world.py` of `main.py`, afhankelijk van de fase van je project. 
Zorg ook dat je de modules die je nodig hebt importeerd, bijvoorbeeld,

* `import random`
* ... en misschien nog andere modules.

Gebruik ten slotte een aantal globale variabelen om *"magische constanten"* in je code te vermijden.

"Magische constanten" zijn simpelweg constanten in een programma die "magisch" lijken omdat hun betekenis niet uitgelegd wordt. Het is een slecht idee om ze te gebruiken omdat als je (of iemand anders) later je code opnieuw wilt lezen, het erg lastig is om te begrijpen wat deze getallen doen!

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


# De opdracht: 

`program.py`, moet aan de volgende eisen voldoen:

* Het bevat een klasse `Program` met een werkende constructor en `__repr__`, `__gt__`, `__lt__`
* Deze klasse bevat een werkende methode `randomize`, `get_move`, `mutate`, `crossover`


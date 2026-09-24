# Creature Battle Arena: soorten wezens

In week 5 bouwde je `Creature` en `Party`. Al je wezens vallen nog op dezelfde
manier aan: ze doen schade ter grootte van hun aanvalskracht. Maar een draak
spuwt vuur, een genezer valt helemaal niet aan, en een wolf wordt woedend en
bijt de tweede keer harder.

Je kunt voor elke soort een nieuwe klasse schrijven, met alles erin wat
`Creature` al heeft. Dan staat `take_damage` straks vijf keer in je bestand, en
een fout erin moet je vijf keer herstellen. In dit practicum maak je nieuwe
soorten wezens die alles van `Creature` overnemen, en alleen zelf schrijven wat
anders is.

## Waar je begint

Je werkt verder in je `creatures.py` van week 5, met de klassen `Creature` en
`Party` en de assertions eronder. Laat die assertions staan: ze horen aan het
eind van dit practicum nog steeds te slagen.

Heb je week 5 niet af, download dan
{download}`de eindstand van week 5 </practicals/assets/creatures.py>` en begin
daarmee. De assertions van week 5 staan daar al onderaan.

## Wat je gaat maken

| Stap | Wat | Doet |
|---|---|---|
| 1 | `special_move` op `Creature` | een gewone aanval, voor elk wezen |
| 2 | `Dragon`, `Goblin` en `Healer` | drie soorten wezens, elk met een eigen `special_move` |
| 3 | een lus over gemengde wezens | één aanroep, ander gedrag per soort |
| 4 | `Beast`, en een bonus op `attack` | wat twee soorten delen, op één plek |
| 5 | `Dragon` onder `Beast`, en `Wolf` | twee beesten die op een andere manier woedend worden |
| 6 | `Turret` | een wachttoren die meevecht zonder een `Creature` te zijn |
| 7 | `battle_round` | één aanval tussen twee strijders |
| 8 | `battle` | een gevecht tussen twee partijen, ronde na ronde |

Onder elke stap staan assertions. Zet ze onderaan in `creatures.py`, onder die van
week 5, en voer het bestand uit. Zie je geen foutmelding, dan klopt de stap.

## Stap 1: een speciale zet voor elk wezen

Elk wezen krijgt een speciale zet: `special_move(target)`. Voor een gewoon
`Creature` is dat een gewone aanval, met een zin die beschrijft wat er gebeurde.
Voeg deze methode toe aan `Creature`:

```python
    def special_move(self, target):
        """Doet een gewone aanval op target en beschrijft wat er gebeurde."""
        damage = self.attack(target)
        return f"{self.name} valt aan en doet {damage} schade."
```

De zin is alleen een verslag. De schade is echt gedaan, door `attack`.

```python
vlam = Creature("Vlam", 120, 25, 10)
grom = Creature("Grom", 40, 8, 2)
assert vlam.special_move(grom) == "Vlam valt aan en doet 23 schade."
assert grom.hp == 17
```

## Stap 2: drie soorten wezens

Een draak is een `Creature`: hij heeft hp, valt aan en neemt schade, precies
zoals elk wezen. Alleen zijn speciale zet is anders. Dat schrijf je zo:

```python
class Dragon(Creature):
    """Een draak, die vuur spuwt."""

    def __init__(self, name, hp=120, attack=25, defense=10):
        """Maak een draak; zonder verdere argumenten met de standaardwaarden."""
        super().__init__(name, hp, attack, defense)

    def special_move(self, target):
        """Spuwt vuur naar target."""
        damage = self.attack(target)
        return f"{self.name} spuwt vuur en doet {damage} schade!"
```

Er gebeuren vier dingen in deze paar regels:

| Code | Betekent |
|---|---|
| `class Dragon(Creature):` | `Dragon` is een **subklasse** van `Creature`, en `Creature` is de **superklasse** van `Dragon`. Een draak krijgt alle methoden van `Creature` mee: dat heet **overerving** |
| `hp=120, attack=25, defense=10` | een **standaardwaarde** voor een parameter: laat je het argument weg, dan krijgt de parameter deze waarde. `Dragon("Vlam")` is hetzelfde als `Dragon("Vlam", 120, 25, 10)` |
| `super().__init__(...)` | roept de constructor van `Creature` aan, zodat die de attributen een beginwaarde geeft. `Dragon` hoeft dat zelf niet opnieuw te schrijven |
| `def special_move` | `Dragon` **overschrijft** de methode `special_move` van `Creature`: bij een draak draait deze versie |

Parameters met een standaardwaarde staan achteraan. `name` heeft er geen, dus
een draak zonder naam kun je niet maken.

Schrijf `Goblin` en `Healer` op dezelfde manier. Ook zij zijn een subklasse van
`Creature`.

| Klasse | Standaardwaarden | `special_move(target)` | Geeft terug |
|---|---|---|---|
| `Goblin` | `hp=40, attack=8, defense=2` | een gewone aanval op `target` | `"Grom gooit een puntige steen en doet 6 schade!"` |
| `Healer` | `hp=60, attack=3, defense=5` | geneest zichzelf met `15`, en doet niets met `target` | `"Mos spreekt een genezingsspreuk uit en herstelt 15 hp."` |

`Healer` krijgt `target` dus mee zonder het te gebruiken. Dat is met opzet: zo
roep je `special_move` bij elk wezen op dezelfde manier aan, en dat heb je in de
volgende stap nodig.

```python
vlam = Dragon("Vlam")
grom = Goblin("Grom")
mos = Healer("Mos")
assert repr(vlam) == "Creature(Vlam, level 1, hp 120/120, attack 25, defense 10)"
assert repr(grom) == "Creature(Grom, level 1, hp 40/40, attack 8, defense 2)"
assert repr(Healer("Varen", 80)) == (
    "Creature(Varen, level 1, hp 80/80, attack 3, defense 5)"
)
assert vlam.special_move(grom) == "Vlam spuwt vuur en doet 23 schade!"
assert grom.special_move(mos) == "Grom gooit een puntige steen en doet 3 schade!"
assert grom.special_move(vlam) == "Grom gooit een puntige steen en doet 0 schade!"
mos.take_damage(30)
assert mos.hp == 32
assert mos.special_move(vlam) == (
    "Mos spreekt een genezingsspreuk uit en herstelt 15 hp."
)
assert mos.hp == 47
assert vlam.is_stronger_than(grom)
```

De laatste regel roept `is_stronger_than` aan, en die staat niet in `Dragon`.
Een draak heeft haar geërfd van `Creature`.

Kijk ook naar de eerste assertion: een draak drukt zichzelf af als
`Creature(...)`. Daar komt aan het eind een vraag over.

## Stap 3: één aanroep, ander gedrag

Zet een draak, een goblin en een genezer in één lijst, en laat ze om de beurt hun
speciale zet doen op een oefenpop. Neem deze code over en voer haar uit:

```python
pop = Creature("Pop", 200, 1, 0)
for creature in [Dragon("Vlam"), Goblin("Grom"), Healer("Mos")]:
    before = pop.hp
    print(creature.special_move(pop))
    print(f"hp van de pop: {before} -> {pop.hp}")
```

Je ziet dit:

```text
Vlam spuwt vuur en doet 25 schade!
hp van de pop: 200 -> 175
Grom gooit een puntige steen en doet 8 schade!
hp van de pop: 175 -> 167
Mos spreekt een genezingsspreuk uit en herstelt 15 hp.
hp van de pop: 167 -> 167
```

In de lus staat maar één aanroep, `creature.special_move(pop)`. Welke versie
daarvan draait, hangt af van het object: bij de draak die van `Dragon`, bij de
genezer die van `Healer`. Dat heet **polymorfisme**: dezelfde aanroep geeft ander
gedrag, afhankelijk van het object. De lus hoeft niet te weten welke soort wezen
ze voor zich heeft.

Ook `Party` hoeft dat niet te weten. Aan de klasse `Party` verandert niets, en
toch kan een party nu draken en genezers bevatten:

```python
party = Party([Goblin("Grom"), Dragon("Vlam"), Healer("Mos")])
assert party.strongest_attacker().name == "Vlam"
assert len(party.alive_members()) == 3
assert pop.hp == 167
```

## Stap 4: wat twee soorten delen

Een draak en een wolf zijn allebei beesten. Een beest kan woedend worden, en
doet dan extra schade. Een goblin en een genezer kunnen dat niet.

Dat gedeelde gedrag hoort op één plek: in een klasse `Beast`, die een subklasse
is van `Creature`. Straks worden `Dragon` en `Wolf` subklassen van `Beast`.
Neem `Beast` over in je bestand, onder `Creature`:

```python
class Beast(Creature):
    """Een wezen dat woedend kan worden, en dan harder aanvalt."""

    def __init__(self, name, hp, attack, defense):
        """Maak een beest dat nog niet woedend is."""
        super().__init__(name, hp, attack, defense)
        self.enraged = False

    def enrage(self):
        """Maakt het beest woedend."""
        self.enraged = True

    def rage_bonus(self, amount):
        """Geeft amount als het beest woedend is, en anders 0."""
        if self.enraged:
            return amount
        return 0
```

De constructor van `Beast` doet eerst wat elke constructor van een `Creature`
doet, via `super().__init__`, en geeft daarna het nieuwe attribuut `enraged` een
beginwaarde.

Een woedend beest moet extra schade kunnen doen, zonder dat het de berekening
van `attack` overdoet. Daarom krijgt `attack` in `Creature` een parameter
`bonus` erbij, met standaardwaarde `0`:

```python
    def attack(self, target, bonus=0):
        """Laat target schade nemen ter grootte van de aanvalskracht plus bonus."""
        return target.take_damage(self._attack_power + bonus)
```

Hiermee verandert de methode `attack` uit week 5. Door de standaardwaarde werkt
elke aanroep `attack(target)` nog precies zoals eerst, en slagen de assertions
van week 5 nog.

```python
brul = Beast("Brul", 50, 10, 0)
pop = Creature("Pop", 200, 1, 0)
assert brul.rage_bonus(5) == 0
assert brul.attack(pop, brul.rage_bonus(5)) == 10
brul.enrage()
assert brul.rage_bonus(5) == 5
assert brul.attack(pop, brul.rage_bonus(5)) == 15
assert brul.special_move(pop) == "Brul valt aan en doet 10 schade."
assert pop.hp == 165
```

`Beast` overschrijft `special_move` niet, dus een beest doet de gewone aanval van
`Creature`.

## Stap 5: twee beesten

Maak `Dragon` nu een subklasse van `Beast` in plaats van `Creature`: verander
`class Dragon(Creature):` in `class Dragon(Beast):`. Zet `Dragon` daarvoor onder
`Beast` in je bestand. Een draak is dan nog steeds een `Creature`, want `Beast`
is dat ook.

Een draak en een wolf worden allebei woedend, maar op een andere manier:

| Klasse | Standaardwaarden | `special_move(target)` |
|---|---|---|
| `Dragon` | `hp=120, attack=25, defense=10` | een aanval met bonus `self.rage_bonus(10)`; de draak maakt zichzelf nooit woedend |
| `Wolf` | `hp=50, attack=15, defense=5` | een aanval met bonus `self.rage_bonus(5)`, en daarna maakt de wolf zichzelf woedend |

| `special_move` van | Geeft terug |
|---|---|
| `Dragon` | `"Vlam spuwt vuur en doet 25 schade!"` |
| `Wolf` | `"Grijs huilt en bespringt zijn prooi voor 15 schade, en wordt woedend!"` |

Een wolf wordt dus woedend van zijn eigen zet, en zijn tweede beet is harder dan
zijn eerste. Een draak wordt alleen woedend als iemand anders `enrage()` aanroept.

:::{admonition} Hint
:class: tip

De aanval van een draak is `self.attack(target, self.rage_bonus(10))`.
`rage_bonus` staat in `Beast`, en een draak heeft haar geërfd.
:::

`Goblin` en `Healer` blijven een subklasse van `Creature`. Ze worden nooit woedend,
en hebben dus niets aan `Beast`.

```python
pop = Creature("Pop", 200, 1, 0)
grijs = Wolf("Grijs")
assert grijs.special_move(pop) == (
    "Grijs huilt en bespringt zijn prooi voor 15 schade, en wordt woedend!"
)
assert grijs.special_move(pop) == (
    "Grijs huilt en bespringt zijn prooi voor 20 schade, en wordt woedend!"
)
vlam = Dragon("Vlam")
assert vlam.special_move(pop) == "Vlam spuwt vuur en doet 25 schade!"
assert vlam.special_move(pop) == "Vlam spuwt vuur en doet 25 schade!"
vlam.enrage()
assert vlam.special_move(pop) == "Vlam spuwt vuur en doet 35 schade!"
assert pop.hp == 80
assert repr(Wolf("Grijs")) == "Creature(Grijs, level 1, hp 50/50, attack 15, defense 5)"
```

## Stap 6: een wachttoren die meevecht

Een wachttoren is geen wezen. Hij heeft geen hp en geen vaste aanvalskracht, en
geen enkele versie van een methode uit `Creature` past bij hem. Toch kan hij
meevechten, als hij de methoden en attributen heeft die een gevecht gebruikt,
met methoden die op zijn eigen manier werken.

Een `Turret` werkt helemaal anders dan een `Creature`:

- Hij vuurt elke keer een **willekeurige** schade af, van `5` tot en met `25`.
- Hij valt om na precies **drie klappen**, hoe hard die klappen ook zijn. Eén
  enorme klap telt net zo zwaar als een schampschot.

De klasse erft van niets: er staat niets tussen haakjes achter `class Turret`.
Zet `import random` bovenaan je bestand, en neem dit begin over:

```python
class Turret:
    """Een wachttoren: geen wezen, maar hij vecht wel mee."""

    def __init__(self):
        """Maak een wachttoren die nog geen klap heeft gehad."""
        self.name = "Wachttoren"
        self._hits_taken = 0
        self._max_hits = 3
        self._min_damage = 5
        self._max_damage = 25

    def __repr__(self):
        """Geeft de wachttoren als string, met het aantal klappen."""
        return f"Turret({self.name}, hits {self._hits_taken}/{self._max_hits})"
```

Schrijf de vier methoden die een gevecht nodig heeft:

| Methode | Doet |
|---|---|
| `take_damage(amount)` | telt één klap, hoe groot `amount` ook is, en geeft `amount` terug |
| `is_alive()` | `True` zolang de toren minder dan drie klappen heeft gehad |
| `attack(target)` | laat `target` een willekeurige schade van `5` tot en met `25` nemen, via `target.take_damage(...)`, en geeft terug wat `take_damage` teruggeeft |
| `special_move(target)` | doet een `attack` op `target`, en geeft `"Wachttoren vergrendelt en vuurt, en doet 12 schade!"` terug, met de echte schade in plaats van `12` |

:::{admonition} Hint
:class: tip

`random.randint(a, b)` geeft een willekeurig geheel getal van `a` tot en met `b`.
:::

Een `Turret` is geen subklasse van `Creature`, maar hij heeft wel de methoden en
attributen die een gevecht gebruikt, zoals `special_move`, `is_alive` en `name`.
Dat heet **duck typing**, naar het spreekwoord *als het loopt als een eend en
kwaakt als een eend, dan is het een eend*. Voor een aanroep telt niet van welke
klasse een object is, maar alleen of het de methoden en attributen heeft die
worden gebruikt.

De schade van een toren is elke keer anders. De assertions kijken daarom niet
naar één getal, maar naar wat voor elke worp moet gelden:

```python
stro = Creature("Stro", 1000, 1, 0)
toren = Turret()
for _ in range(20):
    assert 5 <= toren.attack(stro) <= 25

toren = Turret()
toren.take_damage(1000)
assert toren.is_alive()
toren.take_damage(1)
assert toren.is_alive()
toren.take_damage(1)
assert not toren.is_alive()
assert repr(toren) == "Turret(Wachttoren, hits 3/3)"

toren = Turret()
vlam = Dragon("Vlam")
assert vlam.attack(toren) == 25
assert toren.special_move(vlam).startswith("Wachttoren vergrendelt en vuurt")
```

De stro-pop in de eerste lus heeft verdediging `0`, zodat `take_damage` precies
de schade van de toren teruggeeft. In de laatste assertion geeft
`s.startswith(t)` `True` als de string `s` begint met de string `t`: het getal
aan het eind van de zin is elke keer anders, het begin niet.

Kijk ook naar de een na laatste assertion. `attack` van `Creature` roept
`target.take_damage(...)` aan, en een toren heeft `take_damage`. Een draak kan
een toren dus aanvallen, zonder dat `Creature` iets van torens weet.

## Stap 7: één aanval tussen twee strijders

Neem deze functie over in je bestand. Het is een gewone functie, buiten de
klassen:

```python
def battle_round(attacker, defender):
    """Laat attacker zijn speciale zet doen op defender, en meldt de afloop."""
    print(attacker.special_move(defender))
    if defender.is_alive():
        status = "levend"
    else:
        status = "verslagen"
    print(f"{defender.name} is nu {status}.")
```

`battle_round` gebruikt van de aanvaller alleen `special_move`, en van de
verdediger alleen `is_alive` en `name`. Het maakt dus niet uit of de strijders een
`Dragon`, een `Healer` of een `Turret` zijn.

```python
vlam = Dragon("Vlam")
grom = Goblin("Grom")
battle_round(vlam, grom)
battle_round(vlam, grom)
assert not grom.is_alive()

toren = Turret()
battle_round(vlam, toren)
assert toren.is_alive()
battle_round(toren, vlam)
assert 105 <= vlam.hp <= 120
```

De eerste twee aanroepen drukken dit af:

```text
Vlam spuwt vuur en doet 23 schade!
Grom is nu levend.
Vlam spuwt vuur en doet 23 schade!
Grom is nu verslagen.
```

## Stap 8: een gevecht tussen twee partijen

Schrijf een functie `battle(side_a, side_b, max_rounds)` die twee partijen tegen
elkaar laat vechten, ronde na ronde. Ook dit is een gewone functie, buiten de
klassen.

| Onderdeel | Regel |
|---|---|
| een ronde | eerst doet elk levend lid van `side_a` één `battle_round`, daarna elk levend lid van `side_b` |
| het doelwit | steeds het eerste levende lid van de andere partij |
| het einde | zodra een van beide partijen geen levende leden meer heeft, of na `max_rounds` ronden |
| teruggeven | het aantal gespeelde ronden |

`max_rounds` is nodig omdat niet elk gevecht vanzelf eindigt. Twee genezers doen
elkaar nooit schade, en een goblin doet een draak niets: `8` aanvalskracht tegen
`10` verdediging is `0` schade.

:::{admonition} Hint
:class: tip

Een partij valt aan in een lus over haar `alive_members()`. Vraag vóór elke
aanval opnieuw de levende leden van de andere partij op: het vorige doelwit kan
net verslagen zijn, en zijn er geen levende leden meer, dan valt er niemand aan
te vallen. Die aanval schrijf je twee keer, voor elke partij één keer; met een
hulpfunctie `attack_all(attackers, defenders)` hoeft dat maar één keer.
:::

```python
vlam = Dragon("Vlam")
grom = Goblin("Grom")
assert battle(Party([vlam]), Party([grom]), 10) == 2
assert not grom.is_alive()
assert vlam.hp == 120

assert battle(Party([Healer("Mos")]), Party([Healer("Varen")]), 5) == 5

team = Party([Wolf("Grijs"), Turret()])
enemies = Party([Goblin("Grom"), Goblin("Klauw")])
battle(team, enemies, 20)
assert len(enemies.alive_members()) == 0
assert len(team.alive_members()) == 2
```

In het derde gevecht vecht een wachttoren mee in een party. `battle` gebruikt van
een party alleen `alive_members`, en dat werkt ook met een toren erin.

### Wat duck typing niet belooft

Een toren kan in een `Party`, want `Party` controleert niet wat je erin stopt.
Maar niet elke methode van `Party` werkt dan nog. Probeer het, en haal de twee
regels daarna weer weg:

```python
team = Party([Wolf("Grijs"), Turret()])
team.heal_all(10)
```

```text
AttributeError: 'Turret' object has no attribute 'heal'
```

`heal_all` roept bij elk levend lid `heal` aan, en een toren heeft geen `heal`.
Hetzelfde gebeurt met `critical_members`, want een toren heeft geen
`is_critical`, en met `strongest_attacker`, want een toren heeft geen
aanvalskracht om te vergelijken.

Dat is de keerzijde van duck typing. Niemand controleert vooraf of een object de
methoden heeft die later nodig zijn. De fout komt pas op het moment dat de
ontbrekende methode wordt aangeroepen, en dat kan lang nadat de toren in de party
is gezet. Welke methoden een object nodig heeft, hangt af van wat je ermee doet:
voor `battle` volstaat een toren, voor `heal_all` niet.

## Vragen om over na te denken

1. Stel dat `battle_round` wél zou moeten weten van welke klasse zijn argumenten
   zijn. Wat zou het dan moeten controleren, en wat moet je veranderen als er een
   nieuwe soort wezen bijkomt? Waarom is dat slechter?
2. `battle_round` roept `attack` en `take_damage` niet zelf aan, alleen
   `special_move` en `is_alive`. Stel dat het `attacker.attack(defender)` zou
   aanroepen. Is een kleiner aantal methoden dat een functie nodig heeft altijd
   beter, of ligt het werk dan alleen op een andere plek?
3. Een subklasse die `special_move` vergeet te overschrijven, doet stilletjes een
   gewone aanval. Is er verschil tussen een methode die je mag overschrijven en een
   methode die je moet overschrijven? Hoe zie je van buiten welke van de twee de
   superklasse bedoelde? In week 7 leer je hoe een superklasse kan afdwingen dat
   een subklasse een methode overschrijft.
4. Omdat de schade van een toren willekeurig is, kan hetzelfde gevecht twee keer
   anders aflopen. Is dat een goede eigenschap van het spel, of een nadeel omdat je
   het gevecht slecht kunt testen? Hoe zou je één gevecht voorspelbaar maken
   zonder `random` uit de toren te halen?
5. `Dragon` en `Wolf` erven allebei `enrage` en `rage_bonus` van `Beast`, maar
   gebruiken ze heel anders: de wolf wordt vanzelf woedend, de draak alleen door
   iets van buiten. Is een gedeelde superklasse dan nog de goede keuze, of hoort
   in `Beast` iets bij elkaar wat niet bij elkaar hoort?
6. Wat zou er nu kapotgaan als `Goblin` een subklasse van `Beast` werd in plaats
   van `Creature`, terwijl hij nooit `enrage` aanroept? Gaat er niets kapot, is dat
   dan een reden om alle wezens via `Beast` te laten lopen?
7. Een `Party` heeft wezens, en een `Dragon` is een wezen. Waarom erft `Party`
   niet van `Creature`? Wat zou er misgaan als dat wel zo was?
8. `print(Dragon("Vlam"))` drukt `Creature(Vlam, ...)` af, en niet
   `Dragon(Vlam, ...)`. Waar komt die tekst vandaan? Wat zou je moeten doen om bij
   een draak `Dragon(...)` te zien, en bij een wolf `Wolf(...)`?

## Tot slot

Je hebt vijf nieuwe soorten strijders, en het meeste van hun gedrag staat maar op
één plek. Wat alle wezens delen, staat in `Creature`; wat alleen beesten delen, in
`Beast`; en elke subklasse schrijft alleen wat anders is. `battle_round` en
`battle` werken met al die soorten, en met een wachttoren die helemaal geen wezen
is, omdat ze alleen de methoden en attributen gebruiken die elke strijder heeft.

Op een paar plekken valt je code nu nog stilletjes terug: bij foute invoer in de
constructor, en bij een subklasse die `special_move` vergeet. In week 7 kom je
daarop terug.

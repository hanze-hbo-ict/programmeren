# Creature Battle Arena: operatoren en exceptions

Na week 6 kunnen je wezens vechten, maar je kunt ze niet vergelijken. Wie is de
sterkste van een party? `sorted(party.alive_members())` geeft een foutmelding,
want Python weet niet wanneer het ene wezen kleiner is dan het andere. Twee
partijen samenvoegen kan alleen met een lus.

Daarnaast valt je code op twee plekken nog stilletjes terug. Een wezen met `-5`
hp wordt zonder melding een wezen met `1` hp, en een subklasse die vergeet
`special_move` te overschrijven, doet zonder melding een gewone aanval. In dit
practicum geef je wezens en partijen operatoren, en laat je die twee plekken een
exception gooien in plaats van stil terug te vallen.

## Waar je begint

Je werkt verder in je `creatures.py` van week 6, met alle klassen en de assertions
van week 5 en 6 eronder.

Heb je week 6 niet af, download dan
{download}`de eindstand van week 6 </practicals/assets/week_6/creatures.py>` en
begin daarmee. Sla het bestand op als `creatures.py`. De assertions van week 5 en
6 staan al onderaan.

Een paar van die assertions slagen na dit practicum niet meer, omdat je code
bewust anders gaat werken. Bij de stap waar dat gebeurt, staat welke het zijn en
wat ervoor in de plaats komt.

## Wat je gaat maken

| Stap | Wat | Doet |
|---|---|---|
| 1 | `power_score` en `__eq__` | wezens op kracht vergelijken met `==` |
| 2 | `__lt__` en `__le__` | wezens sorteren, en vergelijken met `<` en `<=` |
| 3 | `>` en `>=` | werken zonder dat je ze schrijft |
| 4 | `+` en `-` op `Party` | partijen samenvoegen, en een wezen eruit halen |
| 5 | `*` op `Creature` | van één wezen een party maken |
| 6 | de constructor | foute invoer weigeren in plaats van rechtzetten |
| 7 | `special_move` | afdwingen dat elke subklasse een eigen versie heeft |
| 8 | de `hp`-setter | zelf kiezen: stil rechtzetten of weigeren |

Onder elke stap staan assertions. Zet ze onderaan in `creatures.py`, onder die van
week 6, en voer het bestand uit. Zie je geen foutmelding, dan klopt de stap.

## Stap 1: even sterk

Geef `Creature` een methode `power_score()`. Die geeft de kracht van een wezen:
zijn hp, zijn aanvalskracht en zijn verdediging bij elkaar opgeteld.

| Wezen | `power_score()` |
|---|---|
| `Dragon("Vlam")` | `120 + 25 + 10 = 155` |
| `Goblin("Grom")` | `40 + 8 + 2 = 50` |

Geef `Creature` daarna een methode `__eq__(self, other)`: twee wezens zijn gelijk
als ze even sterk zijn. Is `other` geen `Creature`, dan geeft `__eq__` `False`.
`__eq__` is een magische methode: je roept haar niet zelf aan, maar Python doet
dat bij `==`.

```python
    def __eq__(self, other):
        """Geeft True als other een wezen is dat even sterk is."""
        if not isinstance(other, Creature):
            return False
        return self.power_score() == other.power_score()
```

`__eq__` gebruikt `other.power_score()`, en niet de attributen van `other`
rechtstreeks. Zo hoeft `__eq__` niet te weten hoe de kracht wordt berekend.

De vergelijking gaat over kracht, niet over de soort. Een wolf en een wezen met
dezelfde hp, aanvalskracht en verdediging zijn dus gelijk. En `==` vergelijkt nu
de waarde, niet meer de identiteit: twee draken met een andere naam zijn gelijk,
maar het blijven twee objecten.

```python
vlam = Dragon("Vlam")
ember = Dragon("Ember")
grom = Goblin("Grom")
assert vlam.power_score() == 155
assert grom.power_score() == 50
assert vlam == ember
assert vlam is not ember
assert vlam != grom
assert Creature("Klont", 50, 15, 5) == Wolf("Grijs")
assert not vlam == "Vlam"
grom.take_damage(12)
assert grom.power_score() == 40
```

## Stap 2: sorteren

Geef `Creature` de methoden `__lt__(self, other)` voor `<` en `__le__(self, other)`
voor `<=`. Ook die vergelijken de kracht. Is `other` geen `Creature`, dan valt er
niets te vergelijken, en gooien ze een `TypeError`:

```python
raise TypeError("een wezen is alleen met een wezen te vergelijken")
```

Met `__lt__` kan `sorted` een lijst wezens sorteren, van zwak naar sterk, want
`sorted` vergelijkt met `<`.

```python
party = Party([Dragon("Vlam"), Goblin("Grom"), Wolf("Grijs"), Healer("Mos")])
names = [creature.name for creature in sorted(party.alive_members())]
assert names == ["Grom", "Mos", "Grijs", "Vlam"]
assert Goblin("Grom") < Healer("Mos")
assert Goblin("Grom") <= Goblin("Klauw")
assert not Goblin("Grom") < Goblin("Klauw")
```

## Stap 3: groter dan, zonder het te schrijven

Je hebt geen methode geschreven voor `>` of `>=`. Probeer ze toch:

```python
vlam = Dragon("Vlam")
grom = Goblin("Grom")
assert vlam > grom
assert vlam >= grom
assert not grom > vlam
assert vlam >= Dragon("Ember")
```

Ze werken. `Creature` heeft geen methode voor `>`, en dan geeft Python niet op: het
draait de vergelijking om. `vlam > grom` betekent hetzelfde als `grom < vlam`, en
daarvoor heeft `Creature` wel een methode, `__lt__`. Zo wordt `vlam >= grom`
`grom <= vlam`, met `__le__`.

Met drie methoden, `__eq__`, `__lt__` en `__le__`, werken dus alle zes de
vergelijkingen: `==`, `!=`, `<`, `<=`, `>` en `>=`.

## Stap 4: partijen optellen en aftrekken

Twee partijen die samen optrekken, en een wezen dat een party verlaat: daarvoor
krijgt `Party` twee operatoren.

| Code | Geeft |
|---|---|
| `party_a + party_b` | een nieuwe `Party` met de leden van allebei |
| `party - creature` | een nieuwe `Party` zonder dat ene wezen |

Geen van beide verandert de partijen waar ze mee begonnen. Bij lijsten is dat ook
zo: `L + M` maakt een nieuwe lijst, en `L` en `M` blijven zoals ze waren.

Schrijf `__add__(self, other)` en `__sub__(self, creature)` in `Party`. Is `other`
geen `Party`, of `creature` geen `Creature`, dan gooien ze een `TypeError`.
`__add__` mag `other._members` gebruiken: dat gebeurt binnen de klasse `Party`
zelf, net als `is_stronger_than` in week 5 de aanvalskracht van een ander wezen
las.

:::{admonition} Hint
:class: tip

`__sub__` maakt een lijst met alle leden die niet `creature` zijn. Vergelijk daarbij
met `is not`, en niet met `!=`:

```python
[member for member in self._members if member is not creature]
```

:::

Waarom `is not`? Sinds stap 1 zijn twee verschillende goblins met dezelfde kracht
gelijk voor `==`. Met `!=` zou `party - klauw` dus ook `grom` weghalen. `is`
vergelijkt de identiteit, en dat is wat "haal precies dit wezen weg" betekent.

```python
grom = Goblin("Grom")
klauw = Goblin("Klauw")
vlam = Dragon("Vlam")
goblins = Party([grom, klauw])
both = goblins + Party([vlam])
assert [creature.name for creature in both.alive_members()] == ["Grom", "Klauw", "Vlam"]
assert len(goblins.alive_members()) == 2
assert grom == klauw
rest = both - klauw
assert [creature.name for creature in rest.alive_members()] == ["Grom", "Vlam"]
assert len(both.alive_members()) == 3
```

## Stap 5: een wezen vermenigvuldigen

`vlam * 3` geeft een nieuwe `Party` met drie nieuwe wezens. Elk is een kopie van
`vlam` zoals die begon: met dezelfde naam, maximale hp, aanvalskracht en
verdediging, en met volle hp. Bij een lijst doet `*` iets vergelijkbaars:
`[x] * 3` herhaalt wat erin staat.

Een kopie van een draak moet een draak zijn, anders spuwt hij geen vuur. Daarvoor
gebruik je `self.__class__`, dezelfde truc die `__repr__` sinds week 6 gebruikt.
`self.__class__` is de klasse van het object, en die kun je aanroepen zoals elke
klasse. Bij een draak maakt dit dus een nieuwe draak:

```python
            self.__class__(self.name, self._max_hp, self._attack_power, self.defense)
```

Schrijf `__mul__(self, n)` in `Creature`:

| `n` | Resultaat |
|---|---|
| een positieve integer | een `Party` met `n` nieuwe wezens |
| `0` | een lege `Party`: een leeg leger is geen fout |
| een negatieve integer | een `ValueError` |
| geen integer, zoals `2.5` | een `TypeError` |

Of `n` een integer is, vraag je met `isinstance(n, int)`: `isinstance` werkt ook
met een ingebouwd type als `int`. Kies de foutmeldingen zelf, bijvoorbeeld
`"een wezen kun je niet met een negatief getal vermenigvuldigen"`.

```python
vlam = Dragon("Vlam")
vlam.take_damage(40)
army = vlam * 3
members = army.alive_members()
assert len(members) == 3
assert repr(members[0]) == "Dragon(Vlam, level 1, hp 120/120, attack 25, defense 10)"
assert members[0] is not members[1]
assert members[0] is not vlam
assert vlam.hp == 90
pop = Creature("Pop", 200, 1, 0)
assert members[2].special_move(pop) == "Vlam spuwt vuur en doet 25 schade!"
assert len((vlam * 0).alive_members()) == 0
```

Probeer ook `vlam * -1` en `vlam * 2.5`, en haal ze daarna weer weg. De laatste
regel van de foutmelding is de tekst die je zelf aan `ValueError` of `TypeError`
hebt meegegeven.

Tot slot van deze stap alles samen: een leger van drie draken, samengevoegd met
een andere party, en daarna de sterkste aanvaller op de bank.

```python
vlam = Dragon("Vlam")
others = Party([Goblin("Grom"), Healer("Mos")])
big = vlam * 3 + others
assert len(big.alive_members()) == 5
bench = big - big.strongest_attacker()
assert len(bench.alive_members()) == 4
assert len(others.alive_members()) == 2
assert vlam.hp == 120
```

## Stap 6: de constructor weigert foute invoer

Sinds week 5 zet de constructor foute invoer stilletjes recht: wie een wezen met
`-5` hp maakt, krijgt er een met `1` hp. Nu gooit de constructor een `ValueError`.
Vervang de constructor van `Creature` door deze:

```python
    def __init__(self, name, hp, attack, defense):
        """Maak een wezen op level 1; gooit een ValueError bij foute invoer."""
        if hp <= 0:
            raise ValueError("hp moet positief zijn")
        if attack < 1:
            raise ValueError("attack moet minstens 1 zijn")
        if defense < 0:
            raise ValueError("defense mag niet negatief zijn")
        self.name = name
        self._level = 1
        self._max_hp = hp
        self._hp = hp
        self._attack_power = attack
        self.defense = defense
```

De subklassen hoeven niet te veranderen: hun constructors roepen deze aan, via
`super().__init__`.

**Hierdoor vervalt een assertion van week 5.** In stap 1 van week 5 staat:

```python
assert repr(Creature("Pech", -5, 0, -3)) == (
    "Creature(Pech, level 1, hp 1/1, attack 1, defense 0)"
)
```

Die aanroep geeft nu een foutmelding, en dat is de bedoeling. Haal deze assertion
weg. De assertions hieronder komen ervoor in de plaats: een wezen met geldige
invoer, ook op de grens, komt er nog steeds door. Wil je de foutmelding zien, zet
dan `Creature("Pech", -5, 0, -3)` één keer onderaan, voer het bestand uit en haal
de regel weer weg. De laatste regel is:

```text
ValueError: hp moet positief zijn
```

```python
assert repr(Creature("Vlam", 120, 25, 10)) == (
    "Creature(Vlam, level 1, hp 120/120, attack 25, defense 10)"
)
assert repr(Creature("Stro", 1, 1, 0)) == (
    "Creature(Stro, level 1, hp 1/1, attack 1, defense 0)"
)
assert repr(Dragon("Vlam")) == (
    "Dragon(Vlam, level 1, hp 120/120, attack 25, defense 10)"
)
```

## Stap 7: `special_move` afdwingen

In week 6 deed `special_move` van `Creature` een gewone aanval. Een subklasse die
vergat haar eigen versie te schrijven, viel daar stilletjes op terug. Nu dwingt
`Creature` af dat elke subklasse `special_move` overschrijft: de versie van
`Creature` gooit een `NotImplementedError`, met de naam van de klasse erin.
Vervang `special_move` van `Creature` door:

```python
    def special_move(self, target):
        """Gooit een NotImplementedError: elke subklasse schrijft een eigen versie."""
        name = self.__class__.__name__
        raise NotImplementedError(f"{name} moet special_move overschrijven")
```

`Dragon`, `Wolf`, `Goblin` en `Healer` overschrijven `special_move` al, en `Turret`
heeft een eigen versie. Voor hen verandert er niets. Een gewoon `Creature` en een
`Beast` hebben geen eigen versie: bij hen gooit `special_move` nu de exception.

**Hierdoor vervallen assertions van week 6.**

| Waar in week 6 | Wat er stond | Wat ervoor in de plaats komt |
|---|---|---|
| stap 1 | `assert vlam.special_move(grom) == "Vlam valt aan en doet 23 schade."` en `assert grom.hp == 17` | niets: haal beide regels weg, want `vlam` is een gewoon `Creature` |
| stap 4 | `assert brul.special_move(pop) == "Brul valt aan en doet 10 schade."` | niets: haal de regel weg, want `brul` is een `Beast` |
| stap 4 | `assert pop.hp == 165` | `assert pop.hp == 175`: de speciale zet van `brul` deed `10` schade, en die valt nu weg |

Wil je de foutmelding zien, zet dan dit één keer onderaan, voer het bestand uit en
haal de regels weer weg:

```python
brul = Beast("Brul", 50, 10, 0)
brul.special_move(Creature("Pop", 200, 1, 0))
```

```text
NotImplementedError: Beast moet special_move overschrijven
```

```python
pop = Creature("Pop", 200, 1, 0)
assert Dragon("Vlam").special_move(pop) == "Vlam spuwt vuur en doet 25 schade!"
assert Wolf("Grijs").special_move(pop).startswith("Grijs huilt")
assert battle(Party([Dragon("Vlam")]), Party([Goblin("Grom")]), 10) == 2
```

## Stap 8: de `hp`-setter

Er is nog een plek die sinds week 5 stilletjes rechtzet: de setter van `hp`.

```python
    @hp.setter
    def hp(self, value):
        """Geeft hp de waarde value, maar nooit onder 0 of boven het maximum."""
        self._hp = max(0, min(value, self._max_hp))
```

`vlam.hp = -5` gooit niets: `hp` wordt gewoon `0`. En `vlam.hp = 200` wordt
`120`. Niets meldt dat je iets anders kreeg dan je vroeg.

Je kunt de setter ook een `ValueError` laten gooien bij een waarde onder `0` of
boven het maximum. `take_damage` en `heal` merken daar niets van: ze schrijven
rechtstreeks naar `self._hp`, en gaan niet via de setter. Een wezen dat in een
gevecht meer schade krijgt dan het hp heeft, eindigt dus nog steeds stil op `0`.
Alleen een foute toewijzing van buiten de klasse gooit dan.

Kies zelf: laat de setter zoals hij is, of laat hem gooien. **Kies je voor gooien,
dan vervallen twee assertions van week 5**, in stap 3 van week 5: `vlam.hp = 200`
met `assert vlam.hp == 120`, en `vlam.hp = -5` met `assert vlam.hp == 0`. Haal die
vier regels dan weg. De assertions hieronder slagen bij beide keuzes:

```python
vlam = Dragon("Vlam")
vlam.take_damage(500)
assert vlam.hp == 0
vlam.hp = 60
assert vlam.hp == 60
vlam.heal(1000)
assert vlam.hp == 120
```

## Wat duck typing niet belooft, opnieuw

In week 6 zag je dat een wachttoren in een party kan, maar dat niet elke methode
van `Party` dan nog werkt. Met sorteren gebeurt hetzelfde. Probeer het, en haal de
twee regels daarna weer weg:

```python
team = Party([Wolf("Grijs"), Turret()])
sorted(team.alive_members())
```

```text
TypeError: '<' not supported between instances of 'Turret' and 'Wolf'
```

`sorted` vraagt hier of de toren kleiner is dan de wolf. `Turret` heeft geen
`__lt__`. Python draait de vergelijking om, maar `Creature` heeft geen methode voor
`>`, en dan geeft Python zelf deze `TypeError`. Vraag je het andersom,
`Wolf("Grijs") < Turret()`, dan komt de foutmelding uit je eigen `__lt__`:
`een wezen is alleen met een wezen te vergelijken`.

## Vragen om over na te denken

1. Bij een lijst maakt `+` een nieuwe lijst, en verandert `+=` de lijst zelf. Stel
   dat `party += other_party` de party zelf moet uitbreiden in plaats van een
   nieuwe te maken. Wat zou je aan `Party` moeten toevoegen? Zou je allebei willen
   hebben op dezelfde klasse? In de basisopgave verandert `+=` een `Date` wel zelf.
2. In week 5 en 6 zette de constructor foute invoer stilletjes recht. Wat had
   daardoor concreet mis kunnen gaan, zonder dat iemand het merkte?
3. `take_damage` berekent `self._hp - actual`, en dat kan onder nul komen voordat
   `max(0, ...)` het rechtzet. Dat is dezelfde soort waarde als bij `vlam.hp = -5`.
   Waarom is het goed dat het ene stil gebeurt, binnen de klasse, en het andere
   niet, van buiten?
4. `vlam > grom` werkt zonder methode voor `>`, doordat Python de vergelijking
   omdraait. Heeft `Creature` daarmee alle vergelijkingen, of mist er toch iets? Wanneer
   kan het omdraaien je in de steek laten?
5. `__mul__` kopieert de naam, de maximale hp, de aanvalskracht en de verdediging,
   maar niet het level: elke kopie begint op level 1. Is dat een fout, of wat je
   van vermenigvuldigen mag verwachten? Wat zou er nodig zijn om het level mee te
   nemen?
6. `Beast` gooit nu ook een `NotImplementedError` bij `special_move`. Is dat
   terecht? Er bestaan geen beesten die geen draak of wolf zijn.
7. `team - Turret()` gooit een `TypeError`, want `__sub__` controleert met
   `isinstance` of het een `Creature` is. Toch kan een toren in een party. Is die
   controle in `__sub__` hier een goed idee?

## Tot slot

Je wezens en partijen werken nu met de operatoren van Python: `sorted`, alle zes de
vergelijkingen, `+`, `-` en `*`. Op twee plekken die in week 5 en 6 stilletjes
terugvielen, gooit je code nu een exception, en een fout valt op waar hij ontstaat.

In dit practicum gooi je exceptions, maar je vangt er geen af. Wat code die
`creatures.py` gebruikt met zo'n exception doet, is een eigen keuze. Hoe je een
exception afvangt en afhandelt, oefen je in de
[basisopgave](/problems/14_basis): daar lees je datums in en sla je de ongeldige
over.

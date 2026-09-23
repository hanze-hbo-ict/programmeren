# Creature Battle Arena

In dit practicum begin je aan een klein vechtspel. Er zijn wezens die elkaar
aanvallen, schade oplopen en genezen, en groepen wezens die samen optrekken. Je
schrijft alles in één bestand, `creatures.py`, en je begint met een leeg
bestand.

Het spel is de aanleiding. Waar het om gaat, is hoe je de klassen ontwerpt.

## Het uitgangspunt

Een object hoort zelf iets te *doen* met zijn staat, niet die staat af te geven
zodat andere code er iets mee doet. Dat is encapsulatie, en het bepaalt elke
keuze in dit practicum.

Neem de hp van een wezen: de levenspunten die het nog heeft. Je kunt die als
gewoon attribuut `hp` opslaan, zodat andere code `vlam.hp = vlam.hp - 20`
schrijft. Maar dan moet elke plek die schade doet zelf onthouden dat de
verdediging van het wezen eerst van de schade af gaat, en dat hp nooit onder
nul komt. Vergeet één plek dat, dan klopt het wezen niet meer.

Daarom krijgt het wezen een methode `take_damage`. Die kent de regels, en wie
schade wil doen, vraagt het wezen om die te nemen. Een methode die alleen een
ruwe waarde teruggeeft, levert daarbij weinig op: dan rekent de aanroeper
alsnog zelf. Elke methode in dit practicum doet dus een van twee dingen. Ze
verandert de staat op een veilige manier, of ze beantwoordt een echte vraag.

## Wat je gaat maken

| Stap | Wat | Doet |
|---|---|---|
| 1 | `Creature`, constructor en `__repr__` | een wezen maken en afdrukken |
| 2 | `take_damage`, `heal`, `is_alive`, `is_critical` | de hp veranderen en ernaar vragen |
| 3 | de properties `hp` en `level` | hp en level van buiten leesbaar maken |
| 4 | `attack`, `is_stronger_than`, `level_up` | aanvallen en groeien |
| 5 | `Party` | een groep wezens die zich via hun methoden laat aansturen |

Onder elke stap staan assertions. Zet ze onderaan in `creatures.py`, buiten de
klasse, en voer het bestand uit. Zie je geen foutmelding, dan klopt de stap.

## Stap 1: de klasse `Creature`

Een `Creature` heeft een naam, een aantal hp, een aanvalskracht (*attack*) en
een verdediging (*defense*). Elk wezen begint op level 1.

| Attribuut | Beginwaarde | Van buiten te gebruiken? |
|---|---|---|
| `self.name` | het argument `name` | ja |
| `self._hp` | `hp`, maar minstens `1` | nee |
| `self._max_hp` | dezelfde waarde als `self._hp` | nee |
| `self._attack_power` | `attack`, maar minstens `1` | nee |
| `self.defense` | `defense`, maar minstens `0` | ja |
| `self._level` | `1` | nee |

Een attribuut met een `_` ervoor is voor de klasse zelf. Van buiten de klasse
gebruik je het niet.

Schrijf de constructor `__init__(self, name, hp, attack, defense)`. Foute invoer
wordt voorlopig stilletjes rechtgezet in plaats van geweigerd: wie een wezen met
`-5` hp maakt, krijgt er een met `1` hp. Of dat een goede keuze is, is een van de
vragen aan het eind.

Schrijf daarna `__repr__(self)`. Die laat alles zien wat je bij het debuggen wilt
weten, ook de attributen met een `_`. Dat mag hier: `__repr__` is er voor jou als
programmeur, niet voor andere code die er beslissingen op neemt.

| Aanroep | Afgedrukt |
|---|---|
| `print(Creature("Vlam", 120, 25, 10))` | `Creature(Vlam, level 1, hp 120/120, attack 25, defense 10)` |
| `print(Creature("Pech", -5, 0, -3))` | `Creature(Pech, level 1, hp 1/1, attack 1, defense 0)` |

:::{admonition} Hint
:class: tip

`max(1, hp)` geeft `hp`, behalve als `hp` kleiner is dan `1`: dan geeft het `1`.
:::

```python
assert repr(Creature("Vlam", 120, 25, 10)) == (
    "Creature(Vlam, level 1, hp 120/120, attack 25, defense 10)"
)
assert repr(Creature("Pech", -5, 0, -3)) == (
    "Creature(Pech, level 1, hp 1/1, attack 1, defense 0)"
)
```

`repr(x)` roept `x.__repr__()` aan, net zoals `print` dat doet.

## Stap 2: de hp veranderen en ernaar vragen

Andere code komt niet rechtstreeks bij `_hp`. Ze gebruikt deze vier methoden:

| Methode | Doet |
|---|---|
| `take_damage(amount)` | verlaagt hp met `amount - defense`, nooit onder `0`, en geeft de schade na aftrek van de verdediging terug |
| `heal(amount)` | verhoogt hp met `amount`, nooit boven het maximum |
| `is_alive()` | `True` zolang hp groter is dan `0` |
| `is_critical()` | `True` als hp een kwart van het maximum is, of minder |

Let op de laatste twee. Ze geven geen getal terug maar een antwoord. Wie wil
weten of een wezen in de problemen zit, vraagt dat aan het wezen, en hoeft de
grens van een kwart niet te kennen. Die grens staat op één plek: in de klasse.

De eerste twee krijg je cadeau:

```python
    def take_damage(self, amount):
        actual = max(0, amount - self.defense)
        self._hp = max(0, self._hp - actual)
        return actual

    def heal(self, amount):
        self._hp = min(self._max_hp, self._hp + amount)
```

Neem ze over in je klasse, geef ze een docstring en schrijf `is_alive` en
`is_critical` zelf.

```python
grom = Creature("Grom", 40, 8, 2)
assert grom.take_damage(12) == 10
assert grom.is_alive()
assert not grom.is_critical()
assert grom.take_damage(22) == 20
assert grom.is_critical()
grom.heal(100)
assert not grom.is_critical()
assert grom.take_damage(1) == 0
assert grom.take_damage(500) == 498
assert not grom.is_alive()
```

## Stap 3: `hp` en `level` als property

Soms wil andere code de hp alleen *zien*, bijvoorbeeld om hem op het scherm te
zetten. Daarvoor krijgt `Creature` een property `hp`: van buiten lees je
`vlam.hp`, en Python roept daarvoor een methode aan. Met een tweede methode, de
*setter*, mag je `hp` ook een nieuwe waarde geven, maar nooit onder `0` of boven
het maximum:

```python
    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(value, self._max_hp))
```

`take_damage` en `heal` blijven rechtstreeks naar `self._hp` schrijven. Ze
staan zelf in de klasse en rekenen al een waarde uit waarvan ze weten dat die
klopt; via de setter zou dat alleen een omweg zijn.

Voeg daarnaast een property `level` toe, zonder setter. Die mag je lezen maar
niet veranderen.

```python
vlam = Creature("Vlam", 120, 25, 10)
assert vlam.hp == 120
vlam.hp = 200
assert vlam.hp == 120
vlam.hp = -5
assert vlam.hp == 0
assert vlam.level == 1
```

Probeer ook `vlam.level = 5`. Python weigert met
`AttributeError: property 'level' of 'Creature' object has no setter`. Haal die
regel daarna weer weg.

### Wat de property van `hp` verandert

Tot deze stap kon niets buiten `Creature` aan de hp komen. Alleen `take_damage`
en `heal` konden dat, en die twee kennen een regel van het spel: bij schade gaat
eerst de verdediging eraf. Met de setter kan het nu ook rechtstreeks, en dan
geldt die regel niet:

```python
vlam = Creature("Vlam", 120, 25, 10)
vlam.hp = vlam.hp - 20
print(vlam.hp)  # 100

vlam = Creature("Vlam", 120, 25, 10)
vlam.take_damage(20)
print(vlam.hp)  # 110
```

De setter houdt hp wel tussen `0` en het maximum. Dat deel van de bescherming
blijft. Maar de verdediging kent hij niet, want die regel staat alleen in
`take_damage`. De property van `hp` koopt dus gemak, en betaalt daarvoor met een
weg om de belangrijkste regel heen.

`level` is het schonere geval. Zonder setter blijft er maar één manier om het
level te veranderen: de methode `level_up` uit de volgende stap.

## Stap 4: aanvallen en groeien

Bij de aanvalskracht ga je een stap verder. Andere code heeft het getal
`_attack_power` nooit nodig, dus komt er geen property voor. Wie wil dat een
wezen aanvalt, vraagt het wezen om aan te vallen.

| Methode | Doet |
|---|---|
| `attack(target)` | laat `target` schade nemen ter grootte van de eigen aanvalskracht, via `target.take_damage(...)`, en geeft de toegebrachte schade terug |
| `is_stronger_than(other)` | `True` als de eigen aanvalskracht groter is dan die van `other` |
| `level_up()` | laat het wezen één level groeien |

`is_stronger_than` leest `other._attack_power`, en dat mag. De code staat zelf in
de klasse `Creature`: de klasse vergelijkt twee van haar eigen objecten. Van
buiten de klasse zou dezelfde regel niet mogen.

`level_up` doet vier dingen in één keer. Dat is de bedoeling: met vier losse
methoden kan een aanroeper er een vergeten, of ze in een verkeerde volgorde
aanroepen.

```python
    def level_up(self):
        self._level += 1
        old_max = self._max_hp
        self._max_hp = int(self._max_hp * 1.15)
        self._hp = int(self._hp * (self._max_hp / old_max))
        self._attack_power += 3
        self.defense += 2
```

Kijk naar de tweede hp-regel. Een wezen met de helft van zijn hp heeft na het
groeien nog steeds ongeveer de helft; het wordt niet vanzelf beter.

`defense` laat je bewust een gewoon attribuut, zonder `_`. Niets houdt andere
code tegen om `vlam.defense = 999` te schrijven. Dat verschil met hp en
aanvalskracht komt terug in de vragen.

```python
vlam = Creature("Vlam", 120, 25, 10)
grom = Creature("Grom", 40, 8, 2)
assert vlam.attack(grom) == 23
assert grom.hp == 17
assert grom.attack(vlam) == 0
assert vlam.is_stronger_than(grom)
assert not grom.is_stronger_than(vlam)
grom.level_up()
assert grom.level == 2
assert repr(grom) == "Creature(Grom, level 2, hp 19/46, attack 11, defense 4)"
```

## Stap 5: de klasse `Party`

Een `Party` is een groep wezens. Ook hier geldt het uitgangspunt: de party leest
nooit een ruwe waarde uit een wezen, maar vraagt het wezen iets of laat het iets
doen.

| Methode | Doet |
|---|---|
| `__init__(self, creatures)` | slaat een kopie van de lijst `creatures` op in `self._members` |
| `add(creature)` | voegt een wezen toe |
| `alive_members()` | geeft een lijst van de leden waarvoor `is_alive()` waar is |
| `critical_members()` | geeft een lijst van de leden waarvoor `is_critical()` waar is |
| `strongest_attacker()` | geeft het lid dat het hardst aanvalt, of `None` als de party leeg is |
| `heal_all(amount)` | laat elk levend lid genezen met `amount` |

Een lege party maak je met `Party([])`.

**Waarom een kopie.** Bewaar je de lijst die je meekrijgt zelf, dan kan de code
die hem meegaf hem nog steeds veranderen, buiten `add` om. Met
`self._members = list(creatures)` bewaar je een nieuwe lijst met dezelfde
wezens erin, en komt niemand anders meer bij de lijst van de party.

**`strongest_attacker` leest geen enkel getal.** Hij vraagt de wezens zelf wie
sterker is:

```python
    def strongest_attacker(self):
        strongest = None
        for creature in self._members:
            if strongest is None or creature.is_stronger_than(strongest):
                strongest = creature
        return strongest
```

Bij een lege party loopt de lus nul keer, en blijft `strongest` dus `None`.

:::{admonition} Hint
:class: tip

`alive_members` en `critical_members` schrijf je met een list comprehension, of
met een `for`-lus die een nieuwe lijst opbouwt. Allebei is goed. Voor `heal_all`
kun je `alive_members()` gebruiken.
:::

`critical_members` telt ook een dood wezen mee: hp `0` is een kwart van het
maximum of minder.

```python
vlam = Creature("Vlam", 120, 25, 10)
grom = Creature("Grom", 40, 8, 2)
mos = Creature("Mos", 60, 3, 5)
party = Party([grom, mos])
party.add(vlam)
assert party.strongest_attacker() is vlam
assert len(party.alive_members()) == 3

vlam.attack(grom)
vlam.attack(grom)
assert not grom.is_alive()
assert len(party.alive_members()) == 2
assert len(party.critical_members()) == 1

vlam.attack(mos)
party.heal_all(10)
assert mos.hp == 50
assert grom.hp == 0

assert Party([]).strongest_attacker() is None

members = [mos]
small = Party(members)
members.append(vlam)
assert len(small.alive_members()) == 1
```

## Vragen om over na te denken

1. `vlam.hp = vlam.hp - 20` en `vlam.take_damage(20)` doen iets anders zodra
   `defense` groter is dan `0`. Hoe leg je dat uit aan iemand die deze klasse voor
   het eerst gebruikt? Was een `hp` zonder setter, net als `level`, de veiligere
   keuze geweest?
2. Op `hp` en `level` na is elke methode een handeling (`take_damage`,
   `level_up`, `attack`, `heal_all`) of een ja-neevraag (`is_alive`,
   `is_critical`, `is_stronger_than`). Wat gaat er verloren als
   `strongest_attacker` zelf de aanvalskracht van elk wezen zou lezen en
   vergelijken?
3. `level_up` verandert vier dingen in één aanroep. Wat kan er misgaan als een
   aanroeper `_max_hp` kon verhogen zonder `_hp` mee te schalen, of
   `_attack_power` kon verhogen zonder `level_up`?
4. `defense` bleef een gewoon attribuut. Wat kan andere code met de verdediging
   doen wat bij hp en aanvalskracht niet kan? Maakt dat hier uit?
5. `is_stronger_than` leest `other._attack_power`. Waarom mag dat vanuit
   `Creature`, en zou het het hele idee onderuithalen als `Party` hetzelfde deed?
6. De constructor zet foute invoer stilletjes recht. Een wezen dat met `-5` hp
   wordt gemaakt, heeft er `1`. Wie merkt dat, en wanneer? Wat zou je liever
   hebben?

## Tot slot

Je hebt twee klassen die hun eigen staat bewaken. `Creature` kent de regels van
schade, genezen en groeien, en `Party` stuurt haar leden aan zonder ooit een
van hun getallen te lezen. Wie deze klassen gebruikt, hoeft die regels niet te
kennen om ze niet te breken.

"""De eindstand van het practicum Creature Battle Arena van week 6.

Gebruik dit bestand als beginstand voor week 7 als je week 6 niet af hebt.
"""

import random


class Creature:
    """Een wezen met hp, een aanvalskracht en een verdediging."""

    def __init__(self, name, hp, attack, defense):
        """Maak een wezen op level 1; foute invoer wordt stilletjes rechtgezet."""
        self.name = name
        self._level = 1
        self._max_hp = max(1, hp)
        self._hp = self._max_hp
        self._attack_power = max(1, attack)
        self.defense = max(0, defense)

    def __repr__(self):
        """Geeft het wezen als string, met alles wat je bij het debuggen wilt weten."""
        return (
            f"{self.__class__.__name__}({self.name}, level {self._level}, "
            f"hp {self._hp}/{self._max_hp}, attack {self._attack_power}, "
            f"defense {self.defense})"
        )

    def take_damage(self, amount):
        """Verlaagt hp met amount min de verdediging en geeft die schade terug."""
        actual = max(0, amount - self.defense)
        self._hp = max(0, self._hp - actual)
        return actual

    def heal(self, amount):
        """Verhoogt hp met amount, nooit boven het maximum."""
        self._hp = min(self._max_hp, self._hp + amount)

    def is_alive(self):
        """Geeft True zolang hp groter is dan 0."""
        return self._hp > 0

    def is_critical(self):
        """Geeft True als hp een kwart van het maximum is, of minder."""
        return self._hp <= self._max_hp * 0.25

    @property
    def hp(self):
        """De hp; een nieuwe waarde blijft tussen 0 en het maximum."""
        return self._hp

    @hp.setter
    def hp(self, value):
        """Geeft hp de waarde value, maar nooit onder 0 of boven het maximum."""
        self._hp = max(0, min(value, self._max_hp))

    @property
    def level(self):
        """Het level, alleen om te lezen."""
        return self._level

    def attack(self, target, bonus=0):
        """Laat target schade nemen ter grootte van de aanvalskracht plus bonus."""
        return target.take_damage(self._attack_power + bonus)

    def is_stronger_than(self, other):
        """Geeft True als de eigen aanvalskracht groter is dan die van other."""
        return self._attack_power > other._attack_power

    def special_move(self, target):
        """Doet een gewone aanval op target en beschrijft wat er gebeurde."""
        damage = self.attack(target)
        return f"{self.name} valt aan en doet {damage} schade."

    def level_up(self):
        """Laat het wezen één level groeien."""
        self._level += 1
        old_max = self._max_hp
        self._max_hp = int(self._max_hp * 1.15)
        self._hp = int(self._hp * (self._max_hp / old_max))
        self._attack_power += 3
        self.defense += 2


class Party:
    """Een groep wezens die zich via hun methoden laat aansturen."""

    def __init__(self, creatures):
        """Maak een party met een kopie van de lijst creatures."""
        self._members = list(creatures)

    def add(self, creature):
        """Voegt creature toe aan de party."""
        self._members.append(creature)

    def alive_members(self):
        """Geeft een lijst van de leden die nog leven."""
        return [creature for creature in self._members if creature.is_alive()]

    def critical_members(self):
        """Geeft een lijst van de leden die er kritiek aan toe zijn."""
        return [creature for creature in self._members if creature.is_critical()]

    def strongest_attacker(self):
        """Geeft het lid dat het hardst aanvalt, of None als de party leeg is."""
        strongest = None
        for creature in self._members:
            if strongest is None or creature.is_stronger_than(strongest):
                strongest = creature
        return strongest

    def heal_all(self, amount):
        """Laat elk levend lid genezen met amount."""
        for creature in self.alive_members():
            creature.heal(amount)


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


class Dragon(Beast):
    """Een draak, die vuur spuwt."""

    def __init__(self, name, hp=120, attack=25, defense=10):
        """Maak een draak; zonder verdere argumenten met de standaardwaarden."""
        super().__init__(name, hp, attack, defense)

    def special_move(self, target):
        """Spuwt vuur naar target, harder als de draak woedend is."""
        damage = self.attack(target, self.rage_bonus(10))
        return f"{self.name} spuwt vuur en doet {damage} schade!"


class Wolf(Beast):
    """Een wolf, die woedend wordt van zijn eigen aanval."""

    def __init__(self, name, hp=50, attack=15, defense=5):
        """Maak een wolf; zonder verdere argumenten met de standaardwaarden."""
        super().__init__(name, hp, attack, defense)

    def special_move(self, target):
        """Bespringt target, en wordt daarna woedend."""
        damage = self.attack(target, self.rage_bonus(5))
        self.enrage()
        return (
            f"{self.name} huilt en bespringt zijn prooi voor {damage} schade, "
            "en wordt woedend!"
        )


class Goblin(Creature):
    """Een goblin, die met stenen gooit."""

    def __init__(self, name, hp=40, attack=8, defense=2):
        """Maak een goblin; zonder verdere argumenten met de standaardwaarden."""
        super().__init__(name, hp, attack, defense)

    def special_move(self, target):
        """Gooit een steen naar target."""
        damage = self.attack(target)
        return f"{self.name} gooit een puntige steen en doet {damage} schade!"


class Healer(Creature):
    """Een genezer, die zichzelf geneest in plaats van aan te vallen."""

    def __init__(self, name, hp=60, attack=3, defense=5):
        """Maak een genezer; zonder verdere argumenten met de standaardwaarden."""
        super().__init__(name, hp, attack, defense)

    def special_move(self, target):
        """Geneest zichzelf met 15, en doet niets met target."""
        self.heal(15)
        return f"{self.name} spreekt een genezingsspreuk uit en herstelt 15 hp."


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

    def take_damage(self, amount):
        """Telt één klap, hoe groot amount ook is, en geeft amount terug."""
        self._hits_taken += 1
        return amount

    def is_alive(self):
        """Geeft True zolang de toren minder klappen heeft gehad dan hij aankan."""
        return self._hits_taken < self._max_hits

    def attack(self, target):
        """Laat target een willekeurige schade nemen en geeft die terug."""
        return target.take_damage(random.randint(self._min_damage, self._max_damage))

    def special_move(self, target):
        """Vuurt op target en beschrijft wat er gebeurde."""
        damage = self.attack(target)
        return f"{self.name} vergrendelt en vuurt, en doet {damage} schade!"


def battle_round(attacker, defender):
    """Laat attacker zijn speciale zet doen op defender, en meldt de afloop."""
    print(attacker.special_move(defender))
    if defender.is_alive():
        status = "levend"
    else:
        status = "verslagen"
    print(f"{defender.name} is nu {status}.")


def attack_all(attackers, defenders):
    """Laat elk levend lid van attackers het eerste levende lid van defenders aanvallen."""
    for attacker in attackers.alive_members():
        targets = defenders.alive_members()
        if len(targets) == 0:
            return
        battle_round(attacker, targets[0])


def battle(side_a, side_b, max_rounds):
    """Laat side_a en side_b vechten tot een partij verslagen is; geeft het aantal ronden."""
    rounds = 0
    while (
        rounds < max_rounds
        and len(side_a.alive_members()) > 0
        and len(side_b.alive_members()) > 0
    ):
        rounds += 1
        attack_all(side_a, side_b)
        attack_all(side_b, side_a)
    return rounds


# De assertions van week 5, stap 1 tot en met 5.

assert repr(Creature("Vlam", 120, 25, 10)) == (
    "Creature(Vlam, level 1, hp 120/120, attack 25, defense 10)"
)
assert repr(Creature("Pech", -5, 0, -3)) == (
    "Creature(Pech, level 1, hp 1/1, attack 1, defense 0)"
)

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

vlam = Creature("Vlam", 120, 25, 10)
assert vlam.hp == 120
vlam.hp = 200
assert vlam.hp == 120
vlam.hp = -5
assert vlam.hp == 0
assert vlam.level == 1

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


# De assertions van week 6, stap 1 tot en met 8.

vlam = Creature("Vlam", 120, 25, 10)
grom = Creature("Grom", 40, 8, 2)
assert vlam.special_move(grom) == "Vlam valt aan en doet 23 schade."
assert grom.hp == 17

vlam = Dragon("Vlam")
grom = Goblin("Grom")
mos = Healer("Mos")
assert repr(vlam) == "Dragon(Vlam, level 1, hp 120/120, attack 25, defense 10)"
assert repr(grom) == "Goblin(Grom, level 1, hp 40/40, attack 8, defense 2)"
assert repr(Healer("Varen", 80)) == (
    "Healer(Varen, level 1, hp 80/80, attack 3, defense 5)"
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

pop = Creature("Pop", 200, 1, 0)
for creature in [Dragon("Vlam"), Goblin("Grom"), Healer("Mos")]:
    before = pop.hp
    print(creature.special_move(pop))
    print(f"hp van de pop: {before} -> {pop.hp}")

party = Party([Goblin("Grom"), Dragon("Vlam"), Healer("Mos")])
assert party.strongest_attacker().name == "Vlam"
assert len(party.alive_members()) == 3
assert pop.hp == 167

brul = Beast("Brul", 50, 10, 0)
pop = Creature("Pop", 200, 1, 0)
assert brul.rage_bonus(5) == 0
assert brul.attack(pop, brul.rage_bonus(5)) == 10
brul.enrage()
assert brul.rage_bonus(5) == 5
assert brul.attack(pop, brul.rage_bonus(5)) == 15
assert brul.special_move(pop) == "Brul valt aan en doet 10 schade."
assert pop.hp == 165

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
assert repr(Wolf("Grijs")) == "Wolf(Grijs, level 1, hp 50/50, attack 15, defense 5)"

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
assert isinstance(vlam, Creature)
assert not isinstance(toren, Creature)

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

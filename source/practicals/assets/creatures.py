"""De eindstand van het practicum Creature Battle Arena van week 5.

Gebruik dit bestand als beginstand voor week 6 als je week 5 niet af hebt.
"""


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
            f"Creature({self.name}, level {self._level}, "
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

    def attack(self, target):
        """Laat target schade nemen ter grootte van de eigen aanvalskracht."""
        return target.take_damage(self._attack_power)

    def is_stronger_than(self, other):
        """Geeft True als de eigen aanvalskracht groter is dan die van other."""
        return self._attack_power > other._attack_power

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

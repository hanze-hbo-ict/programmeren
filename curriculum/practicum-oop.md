# Practicum PGM2 week 5 tot en met 7: de Creature Battle Arena

Opzet voor het practicum van de weken 5, 6 en 7 van Programmeren II, aangeleverd
door de vakdeskundige op 23 september 2026. Dit document is voor auteurs en
docenten, niet voor studenten; het is de bron waaruit het practicummateriaal per
week wordt geschreven, niet het materiaal zelf.

| Sessie | PGM2-week | Uitgevoerd in |
|---|---|---|
| 1 | 5 | #160, uitgevoerd in `source/practicals/12_creatures.md` |
| 2 | 6 | #270, uitgevoerd in `source/practicals/13_creatures.md` |
| 3 | 7 | #271, uitgevoerd in `source/practicals/14_creatures.md` |

Bij de uitvoering gelden de conventies zoals altijd: de tekst spreekt de student
aan, niet de docent, en de termen volgen `conventies/begrippen.md`. Daarnaast is
besloten, bij de voorbereiding van de poort van #160:

- **`Party` gebruikt in week 5 geen standaardwaarde voor een parameter.** De
  opdracht wordt zo herschreven dat `creatures=None` niet voorkomt; het begrip
  staat niet in de leerlijn.
- **Sessie 3 gooit alleen exceptions en vangt er geen af.** Leeruitkomst P4 vraagt
  het afhandelen van foutcondities. Bij de poort van #271 is besloten dat het
  afvangen een eigen opgave krijgt in de basisopgave van week 7 (VP1); het
  practicum blijft alleen gooien. Zie `leerlijn.md`, *Excepties landen in week 7*.

Bij de poort van #270 (24 september 2026) is voor sessie 2 besloten:

- **Standaardwaarden voor parameters komen in week 6** (V8). Het begrip staat nu
  in de leerlijn bij week 6, dus `attack(self, target, bonus=0)` en de
  standaardwaarden van `Dragon` en `Wolf` blijven zoals hieronder. Ook `Goblin`
  (`hp=40, attack=8, defense=2`) en `Healer` (`hp=60, attack=3, defense=5`)
  krijgen ze, zoals in de bijlage. Het besluit over `Party` in week 5 blijft staan.
- **`Turret` en de lus over meerdere rondes** (V9). De limieten van `Turret`
  worden attributen van het object in `__init__`, geen klasse-attributen. De lus
  krijgt een vaste doelkeuze en een maximum aantal rondes. Dat `Turret` in een
  `Party` `strongest_attacker`, `critical_members` en `heal_all` breekt, wordt in
  de tekst besproken als risico van duck typing. *Uitgevoerd als* (#270, een
  keuze van de auteur, geen besluit): een functie
  `battle(side_a, side_b, max_rounds)`, met als doelwit het eerste levende lid van
  de andere partij en `max_rounds` als argument zonder standaardwaarde; als
  reden voor de attributen van het object is aangehouden dat klasse-attributen
  niet in de leerlijn staan.
- **`__repr__` van een subklasse** (V10). Een `Dragon` drukt zich af als
  `Creature(...)`, zoals de `__repr__` van week 5 dat doet; daar komt een vraag
  over in het practicum. `type(self).__name__` wordt vermeden. Wat sessie 3 over
  `self.__class__` in `__repr__` zegt, is een aflevering naar #271. **Herroepen bij
  de poort van #271** (VP7): zie hieronder.
- **Stille terugval in `special_move`** (V4), zoals hieronder; een gemarkeerde
  vooruitverwijzing naar week 7 mag.
- **Een beginstand** (V12): de eindstand van week 5 staat als download in
  `source/practicals/assets/creatures.py`, voor wie week 5 niet af heeft.
- **Termen** (V7): *subklasse*, *superklasse* en *overschrijven*, niet
  *subclass*, *basisclass* of *override*; zie `conventies/begrippen.md`.

Bij de poort van #271 (25 september 2026) is besloten, voor sessie 2 en 3:

- **`self.__class__` en `isinstance` komen in week 6** (VP7, VP8). In sessie 2
  gebruikt `__repr__` voortaan `self.__class__.__name__`, dus een `Dragon` drukt
  zich af als `Dragon(...)`; de vraag daarover in het practicum van week 6
  vervalt. `isinstance` komt in week 6 naast duck typing, en `battle_round` blijft
  bewust zonder die controle. Sessie 3 gebruikt `self.__class__(...)` in
  `__mul__` en `self.__class__.__name__` in de melding van `NotImplementedError`,
  zoals hieronder. De zin dat `__repr__` die truc "al sinds Sessie 1" gebruikt,
  wordt: sinds sessie 2. Dit herroept V10.
- **Geen `NotImplemented`** (VP8). Bij een argument van een ander type geeft
  `__eq__` `False`; `__lt__`, `__le__`, `__add__`, `__sub__` en `__mul__`
  controleren met `isinstance` en gooien een `TypeError`. De gespiegelde aanroep
  (`>` via `__lt__`) blijft een stap, uitgelegd zonder `NotImplemented`. De
  discussievraag *"Waarom `NotImplemented` teruggeven ..."* vervalt. Dit wijkt af
  van de code in sessie 3 hieronder.
- **`+=` op `Party`** (VP5). `Party` krijgt alleen `__add__` en `__sub__`, die een
  nieuwe `Party` maken. De discussievraag over `__iadd__` blijft staan. `Date` in
  de basisopgave krijgt wel `__iadd__`/`__isub__`, die het object veranderen en
  `self` teruggeven.
- **Alleen `Creature.special_move` gooit** een `NotImplementedError` (VP6). Geen
  *abc*. De assertions van week 6 die daardoor vervallen, noemt de tekst.
- **`Turret` in `sorted`**: een toevoeging aan sessie 3. `sorted` over een lijst
  met een wachttoren erin geeft een `TypeError`, als vervolg op *Wat duck typing
  niet belooft* in week 6.
- **Een beginstand van week 6** (VP12) staat als download in
  `source/practicals/assets/`, met de assertions van week 5 en 6 onderaan, en volgt
  week 6 na de wijzigingen hierboven.

Wat hieronder staat is de opzet zoals aangeleverd.

Deze drie sessies zijn waar studenten dit project voor het eerst bouwen — er bestaat nog niets van bij aanvang. De eerdere sessies die de onderliggende concepten behandelden (classes, constructors, `__repr__`, encapsulatie, polymorfisme, overerving, duck typing, operator overloading) gebruikten aparte, niet-gerelateerde oefeningen. Sessie 1 begint dus met een leeg bestand, en elke latere sessie bouwt alleen voort op wat in de *vorige sessie van deze workshop* is gebouwd — niet op iets uit die eerdere lessen.

Het doel is zelfstandige toepassing, geen nieuwe lesstof: elke sessie blijft strikt binnen de onderwerpen die ervoor genoemd zijn, met minimale nieuwe syntaxis. Sessie 1 introduceert bewust `@property` voor `hp` en `level` — zie de notitie over wat die afweging doet met encapsulatie, precies waar het geïntroduceerd wordt — maar verder komt er nergens in de workshop een andere decorator voor (`@classmethod`, `@total_ordering`, enz. blijven uitgesloten). Geen container-protocol (`__len__`, `__getitem__`, enz.), geen `__call__`, geen `__hash__`. Het gooien van exceptions wordt ook bewust uitgesteld tot Sessie 3: Sessies 1 en 2 handelen foutieve invoer en ontbrekende overrides af met stille terugvalwaarden, en Sessie 3 komt expliciet op elk daarvan terug zodra exceptions in beeld zijn.

**Opzet:** Python 3.8+, geen externe libraries. Eén bestand, `creatures.py`, groeit gedurende alle drie de sessies.

---

## Sessie 1 — Classes, Objecten, Constructors, `__repr__`, Encapsulatie

### Doel

Bouw de `Creature`-class waar de rest van de workshop op draait, en een `Party`-class ernaast. Het uitgangspunt voor encapsulatie hier: het is de taak van een object om *dingen te doen* met zijn eigen state, niet om die state af te geven zodat andere code er dingen mee kan doen. Een getter die alleen een ruwe waarde teruggeeft, is nauwelijks encapsulatie — het is een container met extra stappen. Elke methode die in deze sessie wordt toegevoegd, verandert ofwel op een veilige manier de state, ofwel beantwoordt een echte vraag / voert een echte actie uit met state die de aanroeper nooit direct ziet.

### Tijdsindeling (90 min)

| Tijd | Activiteit |
|---|---|
| 0:00–0:20 | Oefening 1: `hp` en `level` — acties, dan een property |
| 0:20–0:50 | Oefening 2: `attack_power` en `level_up()` |
| 0:50–1:15 | Oefening 3: bouw `Party` rond gedrag |
| 1:15–1:30 | Oplossingen delen, discussievragen |

### Oefening 1 — `hp` en `level`: acties, dan een property

Bouw een `Creature`-class volgens deze specificatie:

- `__init__(self, name, hp, attack, defense)` — voorlopig wordt foutieve invoer stilletjes afgevlakt in plaats van geweigerd: als `hp` geen geldig positief getal is, behandel het dan als `1` in plaats van te raisen. Stelt ook `self._level = 1` in. We komen op deze keuze terug zodra exceptions in beeld zijn, in Sessie 3.
- HP wordt opgeslagen als `self._hp` en `self._max_hp`. De buitenwereld kan er iets mee doen via:
  - `take_damage(amount)` — verlaagt hp met `amount - defense`, nooit onder 0, geeft de daadwerkelijk toegebrachte schade terug
  - `heal(amount)` — verhoogt hp, nooit boven het maximum
  - `is_alive()` — een ja/nee-vraag, geen getal
  - `is_critical()` — ook een ja/nee-vraag: zit dit wezen onder de 25% van de maximale HP? De drempelwaarde, en de berekening erachter, leven volledig binnen de class — een aanroeper vraagt "zit je in de problemen?" en krijgt een antwoord, geen ruwe getallen om zelf te interpreteren.

```python
    def take_damage(self, amount):
        actual = max(0, amount - self.defense)
        self._hp = max(0, self._hp - actual)
        return actual

    def heal(self, amount):
        self._hp = min(self._max_hp, self._hp + amount)
```

Voeg nu `@property` toe voor `hp` zelf — leesbaar, en schrijfbaar binnen dezelfde grenzen:

```python
    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(value, self._max_hp))
```

Laat `take_damage()`/`heal()` er bewust *niet* doorheen lopen. De property is de grens voor aanroepers buiten `Creature`; `take_damage()`/`heal()` zitten al binnen de class, berekenen al een waarde waarvan ze weten dat die zinvol is, en kunnen gewoon direct naar `self._hp` schrijven — via de setter gaan zou alleen een omweg toevoegen om bij een attribuut te komen waar ze al toegang toe hebben. Deze twee paden apart houden betaalt zich later uit (zie Sessie 3).

Voeg ook een **alleen-lezen** `level`-property toe — puur een getter, geen setter:

```python
    @property
    def level(self):
        return self._level
```

- `__repr__` die elk veld toont dat ertoe doet bij het debuggen (naam, level, huidige/maximale hp, attack, defense) — dit is de enige plek waar interne state prima getoond mag worden, want het is voor een developer die aan het debuggen is, niet voor andere code die beslissingen neemt.

**Een notitie over wat de `hp`-property verandert.** Tot nu toe kon niets buiten `Creature` `hp` aanraken — alleen `take_damage()`/`heal()` konden dat, en beide bakken een domeinregel (defense-mitigatie, het 0/max-plafond) in wat de actie *betekent*, niet alleen in een getalscontrole. De property heropent directe lees- *en* schrijftoegang: `dragon.hp` en `dragon.hp = 200` werken nu allebei.

De setter handhaaft nog steeds de *structurele* invariant — `hp` kan nooit onder 0 of boven `_max_hp` worden geduwd, wat er ook wordt toegewezen. Dat deel overleeft. Wat niet overleeft: `dragon.hp -= 20` en `dragon.take_damage(20)` zijn niet meer hetzelfde zodra `defense > 0` — de property heeft geen idee dat schade eerst met defense verminderd hoort te worden, want die regel leefde alleen binnen `take_damage()`. Directe toewijzing loopt daar recht omheen.

Dit is dus een afweging, geen strikte verbetering: de property koopt gemakkelijke, veilig ogende lees-/schrijftoegang, ten koste van het heropenen van een pad rond de ene domeinregel die `take_damage()` juist moest afdwingen. De property van `level` is in vergelijking het schonere geval — alleen een getter, geen setter, dus `level_up()` blijft de enige manier om hem te veranderen. Er verzwakt niets aan die invariant; alleen de leesbaarheid verbetert.

### Oefening 2 — `attack_power` en `level_up()`

Zelfde idee, toegepast op attack power — maar dit keer verder doorgevoerd dan bij Oefening 1, want er is geen legitieme reden waarom andere code ooit het ruwe attack-getal nodig zou hebben:

- De constructor vloert `attack` ook op `1`, stilletjes, net als bij `hp` — een wezen moet altijd *enige* schade kunnen toebrengen, maar voorlopig wordt foutieve invoer gewoon gecorrigeerd in plaats van geweigerd. `defense` wordt op dezelfde manier op `0` gevloerd:

```python
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self._level = 1
        self._max_hp = max(1, hp)
        self._hp = self._max_hp
        self._attack_power = max(1, attack)
        self.defense = max(0, defense)
```

- Sla het op als `self._attack_power`. Er is geen getter.
- `level_up()` — de ene actie die een wezen laat groeien, in plaats van vier aparte setters die een aanroeper in willekeurige volgorde zou kunnen aanroepen (of overslaan). Eén aanroep moet:
  - `_max_hp` met een vast percentage laten groeien
  - de huidige `_hp` *proportioneel* meeschalen met het nieuwe maximum — een wezen op halve gezondheid blijft na het levelen op halve gezondheid, in plaats van achter te blijven of automatisch volgeheeld te worden
  - `_attack_power` met een vast bedrag verhogen
  - `defense` met een vast bedrag verhogen

```python
    def level_up(self):
        self._level += 1
        old_max = self._max_hp
        self._max_hp = int(self._max_hp * 1.15)
        self._hp = int(self._hp * (self._max_hp / old_max))
        self._attack_power += 3
        self.defense += 2
```

- `attack(target)` — het wezen valt iets aan. Het leest zijn eigen `_attack_power` en roept namens de aanroeper `target.take_damage(...)` aan, en geeft de toegebrachte schade terug. Niemand buiten de class hoeft ooit te weten wat het getal precies is — ze vertellen een wezen om aan te vallen, en het regelt de rest.
- `is_stronger_than(other)` — nog een ja/nee-vraag in plaats van een vergelijkbare waarde. Intern mag dit `self._attack_power` direct vergelijken met `other._attack_power` — in het onderstreepte attribuut van een ander `Creature`-object graaien is *hier* prima, omdat de code die dat doet zelf binnen de `Creature`-class leeft. Dat is anders dan externe code die naar binnen graait; de class vergelijkt zichzelf met een soortgenoot, via haar eigen privéhanddruk.

Laat `defense` verder gewoon een publiek attribuut zonder encapsulatie — `level_up()` mag het vanuit de class veranderen, maar niets weerhoudt externe code ervan om ook rechtstreeks `dragon.defense = 999` te doen. Dat contrast is bewust, voor de discussievragen hieronder.

### Oefening 3 — `Party`, gebouwd rond gedrag

Bouw een `Party`-class die een groep wezens bevat — en die, volgens hetzelfde principe, nooit in een wezen graait om er een ruwe waarde uit te trekken:

- `__init__(self, creatures=None)` — slaat de lijst op als `self._members` (of begint leeg). Beschermd op dezelfde manier als de state van `Creature`: niets buiten de class leest of schrijft er direct in, alleen via de methoden hieronder.
- `add(creature)` — voegt een wezen toe
- `alive_members()` — de wezens waarvoor `is_alive()` waar is
- `critical_members()` — de wezens waarvoor `is_critical()` waar is
- `strongest_attacker()` — vindt de sterkste aanvaller van de party *zonder* ooit zelf een attack-getal te lezen. Het moet elk wezen `is_stronger_than(...)` vragen en de wezens laten beslissen:

```python
def strongest_attacker(self):
    strongest = self._members[0]
    for creature in self._members[1:]:
        if creature.is_stronger_than(strongest):
            strongest = creature
    return strongest
```

- `heal_all(amount)` — draagt elk levend lid op om te helen. Helemaal geen vraag — `Party` stuurt gedrag aan, op dezelfde manier waarop het in Sessie 2 een `battle_round` zal aansturen.

### Discussievragen

- `dragon.hp = dragon.hp - 20` en `dragon.take_damage(20)` gedragen zich anders zodra `defense > 0`. Hoe zou je dat verschil uitleggen aan iemand die deze class voor het eerst gebruikt — en zou een alleen-lezen `hp`-property (alleen een getter, zoals `level`) de veiligere keuze zijn geweest?
- Elke methode die hier is toegevoegd, is ofwel een actie (`take_damage`, `level_up`, `attack`, `heal_all`) ofwel een ja/nee-vraag (`is_alive`, `is_critical`, `is_stronger_than`) — met `hp` en `level` als de twee bewuste uitzonderingen. Wat zou er verloren gaan als `strongest_attacker()` ook gewoon het attack-getal van elk wezen direct zou lezen en ze zelf zou vergelijken, zoals `dragon.hp` nu kan voor HP?
- `level_up()` verandert vier gerelateerde dingen in één aanroep, in plaats van vier aparte setters bloot te stellen. Wat zou er mis kunnen gaan als een aanroeper `_max_hp` kon ophogen zonder ook `_hp` mee te schalen, of `_attack_power` kon verhogen zonder ooit via `level_up()` te gaan?
- `defense` bleef een gewoon publiek attribuut. Wat zou externe code nu concreet met een `Creature` kunnen doen dat het niet met `hp` of `attack_power` zou kunnen — en maakt dat verschil hier daadwerkelijk uit?
- `is_stronger_than` graait direct in `other._attack_power`. Waarom is dat acceptabel vanuit `Creature`, maar zou het het hele punt tenietdoen als `Party` hetzelfde zou doen?

---

## Sessie 2 — Polymorfisme, Classes Uitbreiden, Duck Typing

### Waar de code staat

`Creature` (properties `hp`/`level`, `take_damage`, `heal`, `level_up`, `attack`, `is_alive`, `is_critical`, `is_stronger_than`, `__repr__`) en `Party` uit Sessie 1.

### Doel

Breid `Creature` uit tot een paar verschillende soorten, die zich elk anders gedragen via dezelfde methodeaanroep — met special moves die echt iets doen op het slagveld, niet alleen vertellen. Voeg dan een tweede laag van overerving toe waarin twee van die soorten daadwerkelijk gedrag delen, en bewijs dat je je op dezelfde manier kunt gedragen zonder overerving, voor een derde soort die er niets van deelt.

### Tijdsindeling (90 min)

| Tijd | Activiteit |
|---|---|
| 0:00–0:30 | Oefening 1: subclasses, polymorfisme, en special moves die schade doen |
| 0:30–1:00 | Oefening 2: een tweede overervingslaag |
| 1:00–1:20 | Oefening 3: duck typing en een battle-functie |
| 1:20–1:30 | Oplossingen delen, discussievragen |

### Oefening 1 — Subclasses, polymorfisme, en special moves die schade doen

Geef `Creature` een standaard `special_move(target)` die geen pure sfeertekst is — het voert een echte, gewone aanval uit, generiek beschreven:

```python
    def special_move(self, target):
        dmg = self.attack(target)
        return f"{self.name} valt aan en doet {dmg} schade."
```

Laat studenten minstens drie subclasses bouwen, die elk `super().__init__()` aanroepen en `special_move(target)` overriden met hun eigen gedrag:

```python
class Dragon(Creature):
    def special_move(self, target):
        dmg = self.attack(target)
        return f"{self.name} spuwt vuur en doet {dmg} schade!"

class Goblin(Creature):
    def special_move(self, target):
        dmg = self.attack(target)
        return f"{self.name} gooit een puntige steen en doet {dmg} schade!"

class Healer(Creature):
    def special_move(self, target):
        self.heal(15)
        return f"{self.name} spreekt een genezingsspreuk uit en herstelt 15 HP."
```

`Healer` neemt `target` ook aan en gebruikt het nooit — de signatuur blijft uniform over alle overrides heen, en dat is precies wat het mogelijk maakt dat een gemengde lijst van wezens allemaal op dezelfde aanroep `special_move(target)` reageren in de polymorfe loop hieronder, ongeacht of de versie van een bepaald wezen het argument daadwerkelijk gebruikt.

Schrijf vervolgens een loop over een gemengde lijst van deze wezens, die op elk `special_move(some_target)` aanroept — dezelfde aanroep, ander gedrag per type — en controleer de hp van `some_target` voor en na elke aanroep. Dit is het eigenlijke punt van deze oefening: het printen van de teruggegeven string was voorheen de hele show; nu is de string slechts een beschrijving van iets dat echt is gebeurd. Voeg een paar instanties toe aan een `Party` uit Sessie 1 en bevestig dat er niets aan `Party` hoefde te veranderen om de nieuwe subclasses te bevatten.

Op dit moment faalt een subclass die vergeet `special_move()` te overriden niet — hij valt gewoon stilletjes voor altijd terug op een gewone aanval. Dat is een echt gat, en Sessie 3 komt daarop terug zodra exceptions ter beschikking staan: de oplossing blijkt één regel te zijn.

### Oefening 2 — Een tweede overervingslaag

De vuuradem van `Dragon` en de howl van een `Wolf` (bouw die nu) delen iets dat `Goblin` en `Healer` niet delen: beide zijn beesten die zichzelf woedend kunnen maken voor bonusschade. Dat is een tussenliggende class waard, `Beast`, die tussen `Creature` en `Dragon`/`Wolf` in zit — met de state en het gedrag die ze daadwerkelijk delen, in plaats van een lege doorgeefluik zonder iets eigens:

```python
class Beast(Creature):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.enraged = False

    def enrage(self):
        self.enraged = True

    def rage_bonus(self, amount):
        return amount if self.enraged else 0
```

Dit breidt ook `attack(target)` uit Sessie 1 uit met een optionele `bonus`, zodat een special move om extra schade kan vragen zonder de eigen logica van `attack()` te dupliceren:

```python
    def attack(self, target, bonus=0):
        return target.take_damage(self._attack_power + bonus)
```

Verplaats `Dragon` onder `Beast`, en voeg `Wolf` ernaast toe. Beide gebruiken `rage_bonus()` uit de gedeelde basis — maar laat studenten ze zo bouwen dat de twee het daadwerkelijk *anders* triggeren, in plaats van dat gewoon te vertellen:

```python
class Dragon(Beast):
    def __init__(self, name, hp=120, attack=25, defense=10):
        super().__init__(name, hp, attack, defense)

    def special_move(self, target):
        dmg = self.attack(target, bonus=self.rage_bonus(10))
        return f"{self.name} spuwt vuur en doet {dmg} schade!"

class Wolf(Beast):
    def __init__(self, name, hp=50, attack=15, defense=5):
        super().__init__(name, hp, attack, defense)

    def special_move(self, target):
        dmg = self.attack(target, bonus=self.rage_bonus(5))
        self.enrage()
        return f"{self.name} huilt en bespringt zijn prooi voor {dmg} schade, en wordt woedend!"
```

`Wolf` maakt zichzelf woedend als neveneffect van zijn eigen special move — zijn *tweede* klap in een gevecht is groter dan zijn eerste, zonder enige externe tussenkomst. `Dragon` roept nooit zelf `enrage()` aan; zijn bonus verschijnt alleen als iets externs eerst `dragon.enrage()` aanroept. Laat studenten beide verifiëren: laat een `Wolf` twee rondes meemaken en zie de schade toenemen, roep dan `dragon.enrage()` handmatig aan en bevestig dat de volgende klap van `Dragon` ook omhoogschiet.

`Goblin` en `Healer` blijven precies waar ze waren — directe subclasses van `Creature`, geen `Beast`. Niet elke subclass heeft de extra laag nodig, en `Goblin` via `Beast` laten lopen om bij `Creature` te komen zou een class toevoegen die niets echts bevat — precies het lege doorgeefluik dat dit ontwerp probeert te vermijden.

### Oefening 3 — Duck typing en een battle-functie

Bouw een class die **geen enkele overerving** deelt met `Creature` — bijvoorbeeld een `Turret` — maar wel implementeert wat een gevecht daadwerkelijk nodig heeft: `special_move(target)` (die echte schade toebrengt en een beschrijving teruggeeft) en `is_alive()`. Maak er geen omgedoopte `Creature` van, maar geef het overlevingsregels die volledig anders werken, om het punt te maken dat duck typing alleen dezelfde *interface* vereist, nooit dezelfde interne werking:

- In plaats van een vaste `attack_power`-stat, vuurt `Turret` een **willekeurig bedrag per keer** af, ergens tussen `Turret.MIN_DAMAGE` en `Turret.MAX_DAMAGE` — onvoorspelbaar op een manier die geen ander wezen is.
- In plaats van een HP-pool overleeft `Turret` precies **3 klappen, hoeveel schade elke klap ook doet** — één overweldigende klap telt hetzelfde als een schampschot.

```python
import random

class Turret:
    HITS_TO_DESTROY = 3
    MIN_DAMAGE = 5
    MAX_DAMAGE = 25

    def __init__(self):
        self._hits_taken = 0
        self.name = "Wachttoren"

    def take_damage(self, amount):
        self._hits_taken += 1
        return amount

    def is_alive(self):
        return self._hits_taken < self.HITS_TO_DESTROY

    def attack(self, target):
        dmg = random.randint(self.MIN_DAMAGE, self.MAX_DAMAGE)
        return target.take_damage(dmg)

    def special_move(self, target):
        dmg = self.attack(target)
        return f"{self.name} vergrendelt en vuurt, en doet {dmg} schade!"

    def __repr__(self):
        return f"Turret(hits_taken={self._hits_taken}/{self.HITS_TO_DESTROY})"
```

Have students confirm both halves separately: roep `Turret.attack(dragon)` een paar keer aan en controleer dat de schade elke keer ergens anders in `[MIN_DAMAGE, MAX_DAMAGE]` uitkomt; gooi dan een enkele enorme klap naar een verse `Turret` en controleer dat hij nog steeds `is_alive()` is, gevolgd door twee kleine, en zie hem bij de derde omvallen, ongeacht de betrokken getallen. Het vermelden waard: `Turret.attack()` raakt niets aan van `target` behalve `take_damage()` erop aanroepen — geen enkele stat van het doelwit zelf speelt mee, wat een nog kleinere eis stelt aan wat het bevecht dan `Creature.attack()` doet.

```python
def battle_round(attacker, defender):
    print(attacker.special_move(defender))
    status = "levend" if defender.is_alive() else "verslagen"
    print(f"{defender.name} is nu {status}.")
```

Merk op hoe weinig `battle_round` zelf eigenlijk nodig heeft: geen `attack_power`, zelfs geen `attack()` of `take_damage()` rechtstreeks — die zijn intern aan hoe de `special_move()` van elke class zijn schade toebrengt. `take_damage` moet nog steeds bestaan op alles wat `Turret` bevecht, want *iets* moet de schade ontvangen die `Turret.special_move()` uitdeelt — het maakt alleen geen deel meer uit van wat `battle_round` zelf aanroept.

Bewijs dat `battle_round` identiek werkt of beide argumenten `Creature`-subclasses zijn, of één ervan de niet-gerelateerde `Turret` is — het controleert nooit het type, en het reikt nooit verder dan `special_move()` om iets voor elkaar te krijgen. Breid het uit tot een korte loop van meerdere rondes tussen twee `Party`-objecten: elke ronde nemen levende leden van elke kant om de beurt, totdat één party geen `alive_members()` meer heeft.

### Discussievragen

- Wat zou `battle_round` moeten controleren, en hoe, als het *wel* om de exacte class van zijn argumenten zou geven? Waarom is dat slechter?
- `battle_round` roept `attack()` of `take_damage()` niet meer rechtstreeks aan — alleen nog `special_move(target)` en `is_alive()`. Vergelijk dat met een eerdere versie die zelf `attacker.attack(defender)` aanriep. Is een kleinere vereiste interface altijd beter, of verplaatst het gewoon de verantwoordelijkheid in plaats van die weg te nemen?
- Een niet-overridden `special_move()` valt momenteel terug op een gewone aanval in plaats van te falen. Is er een echt verschil tussen "optioneel te overriden" en "verplicht te overriden" — en hoe zou je van buitenaf zelfs kunnen zien welke van de twee een basisclass bedoelde?
- Omdat de schade van `Turret` willekeurig is, kan exact dezelfde wedstrijd tweemaal draaien twee verschillende uitkomsten opleveren. Is dat een kenmerk — een chaotische, onvoorspelbare turret — of een nadeel, omdat het het gevecht moeilijk reproduceerbaar maakt voor testen? Hoe zou je een specifieke run deterministisch maken zonder `random` de rest van de tijd eruit te slopen?
- `Dragon` en `Wolf` erven allebei `enrage()`/`rage_bonus()` van `Beast`, maar triggeren de woede volledig anders — de één automatisch, als neveneffect van zijn eigen move, de ander alleen wanneer iets externs `enrage()` aanroept. Is het delen van een basisclass nog steeds de juiste keuze wanneer twee subclasses het gedeelde gedrag zo verschillend gebruiken, of is dat een teken dat `Beast` dingen samenbundelt die niet echt één concept zijn?
- Wat zou er daadwerkelijk breken, nu meteen, als `Goblin` zou overerven van `Beast` in plaats van rechtstreeks van `Creature`, ook al roept het nooit `enrage()` aan? Als er niets breekt, is dat dan een argument om alles toch via `Beast` te laten lopen?

---

## Sessie 3 — Operator Overloading

### Waar de code staat

De subclasses van `Creature` en `Turret` uit Sessie 2, `Party` uit Sessie 1, en een werkende `battle_round`/meerdere-rondes-loop.

### Doel

Geef `Creature` operators die het natuurlijk laten samenwerken met built-ins (`sorted`, alle zes vergelijkingen, en `*` om een `Party` op te tuigen), geef `Party` de operators die het eigenlijk altijd al had moeten hebben (`+`/`-` om leden te combineren en te verwijderen), en — nu exceptions eindelijk ter beschikking staan — ga terug en zorg dat twee plekken die stilletjes herstelden van foutieve invoer, dat voortaan luidruchtig doen. Kijk dan goed naar een derde plek die al sinds Sessie 1 bewust stilletjes herstelt van foutieve invoer, en beslis of dat eigenlijk wel de juiste keuze was.

### Tijdsindeling (90 min)

| Tijd | Activiteit |
|---|---|
| 0:00–0:30 | Oefening 1: `__eq__`, `__lt__`, `__le__` op `Creature` |
| 0:30–0:55 | Oefening 2: rekenkunde op `Party`, plus `Creature.__mul__` |
| 0:55–1:15 | Oefening 3: van stilzwijgend naar expliciet |
| 1:15–1:30 | Oplossingen delen, discussievragen |

### Oefening 1 — Vergelijking

Voeg een `power_score()`-methode toe (een combinatie van hp, attack en defense), en implementeer dan `__eq__` en `__lt__` erop gebaseerd:

```python
    def __eq__(self, other):
        if not isinstance(other, Creature):
            return NotImplemented
        return self.power_score() == other.power_score()

    def __lt__(self, other):
        if not isinstance(other, Creature):
            return NotImplemented
        return self.power_score() < other.power_score()
```

Laat studenten bevestigen dat `sorted(party.alive_members())` nu een zinvolle volgorde van zwakste naar sterkste oplevert, en dat `creature_a < creature_b` en `creature_a == creature_b` zich zinvol gedragen over verschillende subclasses heen (een `Goblin` en een `Dragon` kunnen prima vergeleken worden — de vergelijking is gebaseerd op `power_score()`, niet op type). Wijs erop dat dit dezelfde "graai in de privéstate van `other` vanuit de class zelf"-beweging is als `is_stronger_than` in Sessie 1, alleen nu met een operator gespeld in plaats van een methodenaam.

Voeg er nu nog een toe, in dezelfde vorm als `__lt__`:

```python
    def __le__(self, other):
        if not isinstance(other, Creature):
            return NotImplemented
        return self.power_score() <= other.power_score()
```

Dat lijkt alsof het alleen `<=` afdekt — maar laat studenten ook `dragon > goblin` en `dragon >= goblin` controleren. Beide werken al, ook al zijn `__gt__`/`__ge__` nooit geschreven. Wanneer `dragon.__gt__(goblin)` niet bestaat, geeft Python niet op; het probeert de *gespiegelde* aanroep op de andere operand — `goblin.__lt__(dragon)` voor `>`, `goblin.__le__(dragon)` voor `>=`. Omdat `__lt__` en `__le__` allebei gedefinieerd zijn, slagen beide gespiegelde aanroepen, en komt het resultaat in beide richtingen wiskundig correct uit. Drie methoden — `__eq__`, `__lt__`, `__le__` — blijken genoeg om alle zes vergelijkingen (`==`, `!=`, `<`, `<=`, `>`, `>=`) correct te laten werken, zonder `@total_ordering` en zonder `__gt__`/`__ge__` met de hand te schrijven.

### Oefening 2 — Rekenkunde: parties combineren, wezens vermenigvuldigen

Twee parties die samensmelten voor een groot gevecht, en een lid dat er één verlaat, zijn dingen die dit domein daadwerkelijk nodig heeft — en ze passen direct op operators die `Party` nog niet heeft:

- `party_a + party_b` — een nieuwe `Party` waarvan de leden beide parties gecombineerd zijn. Dezelfde taak die `+` al doet voor twee lijsten.
- `party - creature` — een nieuwe `Party` met dat ene wezen verwijderd. Dezelfde taak die `-` al doet voor sets.

Geen van beide mag de originele parties aanraken — `+` en `-` muteren ook geen lijsten of sets, dus `Party` zou zich niet anders moeten gedragen:

```python
    def __add__(self, other):
        if not isinstance(other, Party):
            return NotImplemented
        return Party(self._members + other._members)

    def __sub__(self, creature):
        if not isinstance(creature, Creature):
            return NotImplemented
        return Party([c for c in self._members if c is not creature])
```

`__sub__` controleert `c is not creature` in plaats van `c != creature`. Omdat `Creature.__eq__` vergelijkt op `power_score()`, zouden twee *verschillende* wezens met dezelfde score als `==` tellen — `!=` gebruiken zou hier het verkeerde wezen kunnen verwijderen. `is` vergelijkt identiteit, en dat is wat "verwijder precies dit wezen" daadwerkelijk betekent.

Geef `Creature` nu een `__mul__` die een `Party` oplevert: `dragon * 5` moet aanvoelen als het oproepen van een klein leger — een nieuwe `Party` van vijf aparte wezens, elk fris begonnen met de huidige stats van `dragon`. Vermenigvuldigen met een int levert elders in Python normaal gesproken geen *extra objecten* op, maar `*` op een lijst zet dat precedent al (`[x] * 3` herhaalt de inhoud), dus dit is minder vergezocht dan het in eerste instantie klinkt:

```python
    def __mul__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        if n < 0:
            raise ValueError("een creature kan niet met een negatief getal vermenigvuldigd worden")
        return Party([self.__class__(self.name, self._max_hp, self._attack_power, self.defense)
                      for _ in range(n)])
```

`self.__class__(...)` — dezelfde truc die `__repr__` al sinds Sessie 1 gebruikt — betekent dat `Dragon("Ember") * 3` drie echte `Dragon`s oplevert, geen drie gewone `Creature`s, dus hun `special_move()` blijft werken. `n < 0` raist in plaats van stilletjes naar nul af te vlakken, want Sessie 3 is precies waar dat soort foutieve invoer luidruchtig mag falen in plaats van stilletjes "gerepareerd" te worden — maar `n == 0` wordt met rust gelaten en levert gewoon een geldige, lege `Party` op, want een leeg leger is niet ongeldig op de manier waarop een negatief aantal dat wel is.

Als korte integratie om deze oefening af te sluiten: bouw een `Party` met `dragon * 3`, voeg die samen met een andere `Party` uit Sessie 2 via `+`, en gebruik dan `-` om de `strongest_attacker()` van de samengevoegde party op de bank te zetten voor een handicapronde — en bevestig dat de originele `dragon` en de andere `Party` nog precies zijn zoals ze waren.

### Oefening 3 — Van stilzwijgend naar expliciet

Twee plekken in deze codebase herstellen sinds Sessie 1 stilletjes van foutieve invoer. Nu exceptions eerlijk spel zijn, laat elke plek in plaats daarvan luidruchtig falen — kijk dan naar een derde plek die al die tijd bewust hetzelfde deed, en kijk of je het daar nog steeds mee eens bent.

**Constructorvalidatie.** Vervang de afvlakkingen uit Sessie 1 door raises:

```python
    def __init__(self, name, hp, attack, defense):
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

**`special_move()`.** Vervang de onschuldige standaardwaarde uit Sessie 2 op dezelfde manier:

```python
    def special_move(self, target):
        raise NotImplementedError(f"{self.__class__.__name__} moet special_move() implementeren")
```

`Dragon`/`Goblin`/`Healer` hoeven niet te veranderen — ze overriden het al. Een subclass die het vergeet, faalt nu op het moment dat `special_move()` wordt aangeroepen, in plaats van voor altijd stilletjes met het verkeerde gedrag door te werken.

**De `hp`-setter.** Deze is stil geweest sinds Sessie 1 en niemand heeft hem nog aangeraakt:

```python
    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(value, self._max_hp))
```

`dragon.hp = -5` raist niets — het zet `hp` gewoon stilletjes op `0`. `dragon.hp = 99999` wordt stilletjes `_max_hp`. Niets kondigt aan dat de toewijzing die je vroeg, niet de toewijzing is die daadwerkelijk gebeurde.

Je zou dit ook expliciet kunnen maken — `ValueError` raisen voor alles buiten `[0, _max_hp]` in plaats van af te vlakken. Omdat `take_damage()`/`heal()` rechtstreeks naar `self._hp` schrijven in plaats van via deze setter te gaan (Sessie 1 hield ze bewust gescheiden), raakt het aanscherpen ervan hen helemaal niet: een verdwaalde `dragon.hp = -5` van buiten de class faalt nu, terwijl een genadeklap binnen `take_damage()` een wezen nog steeds stilletjes op 0 HP laat eindigen, precies zoals het hoort. Dat is de daadwerkelijke opbrengst van de ontwerpkeuze uit Sessie 1 — de publieke grens kan strenger worden zonder dat er ook maar één regel van `take_damage()`/`heal()` hoeft te veranderen.

Als korte oefening: maak die verandering, bevestig dat `take_damage()`/`heal()` er echt geen last van hebben, en beslis zelf of je `hp` van buitenaf daadwerkelijk zo streng zou willen — of dat stilletjes afvlakken de vriendelijkere, meer geschikte standaard is voor iets zo publieks.

### Discussievragen

- Waarom `NotImplemented` teruggeven in plaats van een exception te raisen wanneer de andere operand niet het verwachte type is?
- Lijsten ondersteunen `+=` (breidt in-place uit via `__iadd__`) naast `+` (geeft een nieuwe lijst terug). Als je wilde dat `party += other_party` een `Party` in-place uitbreidt in plaats van een nieuwe te bouwen, wat zou je dan moeten toevoegen — en zou je daadwerkelijk beide gedragingen op dezelfde class beschikbaar willen hebben?
- Sessie 1 vlakte foutieve constructor-invoer stilletjes af; deze sessie raist in plaats daarvan. Wat had er concreet mis kunnen gaan terwijl die stille afvlakking nog van kracht was, vóór vandaag?
- `take_damage()` berekent `self._hp - actual`, wat onder nul kan komen voordat de `max(0, ...)`-afvlakking het opvangt — precies dezelfde soort waarde buiten bereik die een verdwaalde `dragon.hp = -5` oplevert. Waarom is het prima dat het ene stilletjes binnen de class gebeurt en het andere niet van buitenaf?
- `dragon > goblin` werkt zonder dat `__gt__` ooit geschreven is, omdat Python terugvalt op `goblin.__lt__(dragon)`. Is dat "alle vergelijkingen implementeren", of voelt een class nog steeds onvolledig aan zonder `__gt__`/`__ge__` expliciet uitgeschreven? Wanneer zou het vertrouwen op die terugval je daadwerkelijk kunnen opbreken?
- Het klonen in `__mul__` gebruikt `self._max_hp`/`self._attack_power`/`self.defense`, maar nooit `self._level` — elke kloon komt terug op level 1, zelfs als het origineel meerdere keren geleveld had. Bug, of een redelijke interpretatie van wat "vermenigvuldigen" van een geleveld wezen zou moeten betekenen? Wat zou er nodig zijn om het level wél te behouden?

---

## Bijlage: Volledige Referentie-oplossing

Een complete, geteste `creatures.py` die alle drie de sessies combineert — voor de instructeur, of om achteraf uit te delen als één uitgewerkt voorbeeld.

```python
import random

class Creature:
    def __init__(self, name, hp, attack, defense):
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

    def take_damage(self, amount):
        actual = max(0, amount - self.defense)
        self._hp = max(0, self._hp - actual)
        return actual

    def heal(self, amount):
        self._hp = min(self._max_hp, self._hp + amount)

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(value, self._max_hp))

    @property
    def level(self):
        return self._level

    def is_alive(self):
        return self._hp > 0

    def is_critical(self):
        return self._hp <= self._max_hp * 0.25

    def level_up(self):
        self._level += 1
        old_max = self._max_hp
        self._max_hp = int(self._max_hp * 1.15)
        self._hp = int(self._hp * (self._max_hp / old_max))
        self._attack_power += 3
        self.defense += 2

    def attack(self, target, bonus=0):
        return target.take_damage(self._attack_power + bonus)

    def is_stronger_than(self, other):
        return self._attack_power > other._attack_power

    def power_score(self):
        return self._hp + self._attack_power + self.defense

    def special_move(self, target):
        raise NotImplementedError(f"{self.__class__.__name__} moet special_move() implementeren")

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, lvl={self._level}, "
                f"hp={self._hp}/{self._max_hp}, attack={self._attack_power}, "
                f"defense={self.defense})")

    def __str__(self):
        return f"{self.name} [{self._hp}/{self._max_hp} HP]"

    def __eq__(self, other):
        if not isinstance(other, Creature):
            return NotImplemented
        return self.power_score() == other.power_score()

    def __lt__(self, other):
        if not isinstance(other, Creature):
            return NotImplemented
        return self.power_score() < other.power_score()

    def __le__(self, other):
        if not isinstance(other, Creature):
            return NotImplemented
        return self.power_score() <= other.power_score()

    def __mul__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        if n < 0:
            raise ValueError("een creature kan niet met een negatief getal vermenigvuldigd worden")
        return Party([self.__class__(self.name, self._max_hp, self._attack_power, self.defense)
                      for _ in range(n)])


class Party:
    def __init__(self, creatures=None):
        self._members = list(creatures) if creatures else []

    def add(self, creature):
        self._members.append(creature)

    def alive_members(self):
        return [c for c in self._members if c.is_alive()]

    def critical_members(self):
        return [c for c in self._members if c.is_critical()]

    def strongest_attacker(self):
        strongest = self._members[0]
        for creature in self._members[1:]:
            if creature.is_stronger_than(strongest):
                strongest = creature
        return strongest

    def heal_all(self, amount):
        for creature in self.alive_members():
            creature.heal(amount)

    def __add__(self, other):
        if not isinstance(other, Party):
            return NotImplemented
        return Party(self._members + other._members)

    def __sub__(self, creature):
        if not isinstance(creature, Creature):
            return NotImplemented
        return Party([c for c in self._members if c is not creature])

    def __repr__(self):
        return f"Party({self._members!r})"


class Beast(Creature):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.enraged = False

    def enrage(self):
        self.enraged = True

    def rage_bonus(self, amount):
        return amount if self.enraged else 0


class Dragon(Beast):
    def __init__(self, name, hp=120, attack=25, defense=10):
        super().__init__(name, hp, attack, defense)

    def special_move(self, target):
        dmg = self.attack(target, bonus=self.rage_bonus(10))
        return f"{self.name} spuwt vuur en doet {dmg} schade!"


class Wolf(Beast):
    def __init__(self, name, hp=50, attack=15, defense=5):
        super().__init__(name, hp, attack, defense)

    def special_move(self, target):
        dmg = self.attack(target, bonus=self.rage_bonus(5))
        self.enrage()
        return f"{self.name} huilt en bespringt zijn prooi voor {dmg} schade, en wordt woedend!"


class Goblin(Creature):
    def __init__(self, name, hp=40, attack=8, defense=2):
        super().__init__(name, hp, attack, defense)

    def special_move(self, target):
        dmg = self.attack(target)
        return f"{self.name} gooit een puntige steen en doet {dmg} schade!"


class Healer(Creature):
    def __init__(self, name, hp=60, attack=3, defense=5):
        super().__init__(name, hp, attack, defense)

    def special_move(self, target):
        self.heal(15)
        return f"{self.name} spreekt een genezingsspreuk uit en herstelt 15 HP."


class Turret:
    """Geen subclass van Creature — bewust andere interne werking, dezelfde interface."""
    HITS_TO_DESTROY = 3
    MIN_DAMAGE = 5
    MAX_DAMAGE = 25

    def __init__(self):
        self._hits_taken = 0
        self.name = "Wachttoren"

    def take_damage(self, amount):
        self._hits_taken += 1
        return amount

    def is_alive(self):
        return self._hits_taken < self.HITS_TO_DESTROY

    def attack(self, target):
        dmg = random.randint(self.MIN_DAMAGE, self.MAX_DAMAGE)
        return target.take_damage(dmg)

    def special_move(self, target):
        dmg = self.attack(target)
        return f"{self.name} vergrendelt en vuurt, en doet {dmg} schade!"

    def __repr__(self):
        return f"Turret(hits_taken={self._hits_taken}/{self.HITS_TO_DESTROY})"


def battle_round(attacker, defender):
    print(attacker.special_move(defender))
    status = "levend" if defender.is_alive() else "verslagen"
    print(f"{defender.name} is nu {status}.")
```

Dit is end-to-end getest — de properties `hp`/`level` (inclusief de begrensde `hp`-setter, waarbij `take_damage`/`heal` er bewust omheen gaan en rechtstreeks naar `self._hp` schrijven), `is_critical`, `level_up()` met proportionele HP-schaling en vaste attack/defense-groei, `attack()` (inclusief de `bonus`-parameter) en `is_stronger_than()` zonder getters buiten de twee properties, de verplichte override `special_move(target)` (bevestigd dat die raist bij een niet-overridden subclass en echte schade doet bij `Dragon`/`Wolf`/`Goblin`/`Healer`/`Turret`), de tussenliggende class `Beast` (`Wolf` die zichzelf woedend maakt als neveneffect van zijn eigen move, `Dragon` die alleen profiteert van een van buitenaf aangeroepen `enrage()`, `Goblin`/`Healer` die `Beast` helemaal overslaan), de gedragsgerichte methoden van `Party` inclusief `heal_all`, polymorfe subclasses, de duck-typed `Turret` (willekeurige schade per klap, die grote en kleine klappen tot precies 3 overleeft) in de nu smallere `battle_round`, sorteren via `__lt__`, `__eq__`, alle zes vergelijkingen via `__eq__`/`__lt__`/`__le__` (inclusief `>`/`>=` via Pythons gespiegelde-operand-terugval, zonder dat `__gt__`/`__ge__` geschreven zijn), `Creature.__mul__` dat een correct-subclassde `Party` van klonen oplevert, en `Party` die leden samenvoegt/verwijdert via `__add__`/`__sub__` (inclusief het identiteit-versus-gelijkheid-randgeval, en de bevestiging dat de originelen onaangeroerd blijven) — om te bevestigen dat het zich gedraagt zoals hierboven beschreven.

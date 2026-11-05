---
lang: nl
papersize: a4
fontsize: 12pt
geometry: margin=2.5cm
toc: false
monofont: DejaVuSansMono.ttf
title: Oefententamen PGM2
---

# Proeftoets

Deze oefentoets heeft zes opgaven en 100 punten. Je oefent de zes leeruitkomsten
van PGM2. Dit is geen uitspraak over de inhoud van het echte tentamen.
Het cijfer is `1 + 9 * behaalde punten / 100`.

## Opgave 1 _Extensies_ (15pt)

Een bestandsnaam heeft meestal een extensie, zoals `.py`. Bijlagen die eindigen
op `.exe` kunnen schadelijke programma's bevatten. Hieronder staat een complete
applicatie die alleen bestandsnamen met een toegestane extensie selecteert.
De vergelijking is hoofdlettergevoelig; een lege extensie past op elke naam.
De functies veranderen de invoerlijsten niet en bewaren volgorde en duplicaten.

```python
def check_extension(s, e):
    """Geef aan of de bestandsnaam eindigt op de gegeven extensie."""
    if e == "":
        return True
    if s == "" or s[-1] != e[-1]:
        return False
    return check_extension(s[:-1], e[:-1])


def allowed_file(filename, extensions):
    """Geef aan of een bestandsnaam op een toegestane extensie eindigt."""
    for extension in extensions:
        if check_extension(filename, extension):
            return True
    return False


def select_files(filenames, extensions):
    """Selecteer toegestane bestandsnamen met behoud van volgorde en duplicaten."""
    return [name for name in filenames if allowed_file(name, extensions)]


assert check_extension("a", "a") is True
assert select_files(["werk.py", "spel.exe", "leeg.txt"], [".py", ".txt"]) == [
    "werk.py",
    "leeg.txt",
]
```

Beantwoord de volgende vragen met verwijzingen naar de code. Je hoeft geen code
te schrijven.

1. Leg van elk van de drie functies uit welke verantwoordelijkheid die heeft,
   welke invoer die ontvangt en welk resultaat die teruggeeft. (5pt)
2. Verklaar hoe een bestandsnaam vanuit `select_files` bij `check_extension`
   terechtkomt en hoe het resultaat terugwerkt in de selectie. Gebruik
   `"spel.exe"` en `[".py", ".txt"]` als concreet voorbeeld. (5pt)
3. De toelatingsregel verandert: extensies moeten voortaan ongeacht hoofdletters
   worden herkend, zodat `"WERK.PY"` ook past op `".py"`. Benoem een geschikte
   wijzigingsplaats, onderbouw waarom en verklaar de gevolgen voor de andere
   twee functies en voor bestaande aanroepen. (5pt)

## Opgave 2 _Even op vele manieren_ (15pt)

Schrijf drie functies die een nieuwe lijst opleveren zonder de invoerlijst te
veranderen. Volgorde en dubbele waarden blijven behouden. De invoer is een lijst
integers, ook negatief of leeg.

1. Schrijf `only_even_lc(L)` met een list comprehension: geef de even waarden
   terug. (5pt)
2. Schrijf `only_even_rec(L)` met recursie, zonder lus of comprehension: geef
   dezelfde selectie terug. (5pt)
3. Schrijf `select_numbers(numbers, predicate)`. Roep het meegegeven predicaat
   voor elk getal aan en neem het getal op als het resultaat waar is. Je mag
   zelf kiezen hoe je de lijst verwerkt. Het predicaat accepteert één integer
   en geeft een boolean terug. (5pt)

```python
assert only_even_lc([-2, -1, 0, 2, 2]) == [-2, 0, 2, 2]
assert only_even_rec([]) == []
assert select_numbers([-2, 0, 3], lambda number: number > 0) == [3]
assert select_numbers([-2, 0, 3], lambda number: number % 2 == 0) == [-2, 0]
```

## Opgave 3 _Bonus_ (15pt)

Studenten die huiswerk maakten krijgen 0.5 bonus. Gebruik onderstaande fictieve
studentgegevens. Elke rij bevat studentnummer, cijfer en een boolean voor
huiswerk. Bij een dubbel studentnummer vervangt de laatste rij de hele eerdere
registratie, inclusief het huiswerkgegeven. Ken de bonus precies eenmaal toe,
na verwerking van alle rijen. Er is geen maximumcijfer in dit contract.

```python
records = [
    ["S01", 7.6, True],
    ["S02", 5.1, False],
    ["S03", 6.4, True],
    ["S01", 8.0, False],
]
participants = {"S01", "S02", "S03", "S04"}
```

`participants` bevat alle ingeschreven studentnummers, ook die zonder cijfer.
Alle nummers in `records` zijn ingeschreven. Maak achtereenvolgens:

1. `students`: een dictionary met studentnummer als sleutel en `[cijfer, huiswerk]`
   als waarde, volgens de regel voor duplicaten. (3pt)
2. Werk de cijfers in die dictionary gericht bij met de bonus voor huiswerk. (3pt)
3. `overview`: een lijst `[studentnummer, cijfer]` voor iedere sleutel, oplopend
   gesorteerd op studentnummer. (3pt)
4. `homework`: een set met de unieke nummers die volgens de definitieve
   registratie huiswerk maakten. (3pt)
5. Controleer met lidmaatschap of `"S03"` in `homework` staat en maak `missing`
   met het setverschil: alle ingeschreven nummers die niet in `homework` staan.
   Een ontbrekend cijfer telt dus als geen geregistreerd huiswerk. (3pt)

Je mag lussen of comprehensions gebruiken. Het resultaat is:

```python
assert students == {"S01": [8.0, False], "S02": [5.1, False], "S03": [6.9, True]}
assert overview == [["S01", 8.0], ["S02", 5.1], ["S03", 6.9]]
assert homework == {"S03"}
assert "S03" in homework
assert missing == {"S01", "S02", "S04"}
```

## Opgave 4 _Nim_ (35pt)

Nim speel je met twee spelers. Je begint met 16 lucifers. Om de beurt pakt een
speler 1, 2 of 3 lucifers, maar nooit meer dan er liggen. Wie de laatste pakt,
wint. Een computer kan proberen een veelvoud van vier achter te laten.
Die strategie garandeert geen winst vanuit elke mogelijke positie.

Maak precies de drie klassen hieronder en een interactieve besturing volgens
het gegeven contract. De menselijke speler begint. De besturing moet ook met
andere objecten met dezelfde spelersinterface werken.

| Onderdeel | Contract |
|---|---|
| `Nim(number_of_sticks)` | Slaat het gegeven niet-negatieve gehele aantal op als `sticks`. Je hoeft de constructorinvoer niet te valideren. |
| `Nim.player_takes(amount)` | Bij een integer met `1 <= amount <= min(3, sticks)` verminder je `sticks` met `amount`. Anders gooi je `ValueError` vóór enige wijziging. Deze methode geeft geen resultaat terug. |
| `Nim.game_over()` | Geeft precies bij nul lucifers `True` terug, anders `False`. |
| `Nim.__eq__(other)` | Twee Nim-objecten zijn gelijk als hun `sticks` gelijk zijn; een ander soort object is niet gelijk. Vergelijken verandert geen object. |
| `Player.choose_move(game)` | Vraagt met `input` een geheel aantal lucifers en geeft dit als integer terug. Verandert het spel niet. |
| `StrategicPlayer(Player)` | Erft van `Player` en overschrijft `choose_move(game)`. Bij een positief aantal kiest die `sticks % 4` als dat niet nul is, anders willekeurig uit `1` tot en met `min(3, sticks)`. Verandert het spel niet. Bij een afgelopen spel wordt deze methode niet aangeroepen. |

Bij twee resterende lucifers zijn dus alleen 1 en 2 legaal; bij nul geen enkele
zet. `Nim(2) == Nim(2)` is waar, ongeacht welke speler aan de beurt zou zijn:
alleen het aantal lucifers behoort tot een positie.

1. Implementeer de toestand, legale zet en eindcontrole. (7pt)
2. Laat de besturing om beurten `choose_move(game)` aanroepen op de menselijke
   en de computerspeler, en laat het spel de gekozen zet uitvoeren. Toon vóór
   elke beurt het aantal en meld wie wint; stop direct bij het einde. (7pt)
3. Implementeer `Player` en `StrategicPlayer` met overerving en overschrijven.
   Gebruik beide in dezelfde besturing zonder op hun type te testen. (6pt)
4. Implementeer de vergelijking van posities. (5pt)
5. Laat `player_takes` een ongeldige zet met `ValueError` weigeren. (5pt)
6. Vang alleen `ValueError` in de besturing af, zowel van de omzetting van
   invoer als van de zetmethode. Meld `"Ongeldige zet"` en probeer opnieuw met
   dezelfde speler en ongewijzigde spelstaat. Vooraf controleren vervangt het
   gooien en afvangen van de exception niet. (5pt)

Controleer ook een rechtstreeks aangeroepen zetmethode:

```python
game = Nim(2)
try:
    game.player_takes(3)
except ValueError:
    assert game.sticks == 2
game.player_takes(2)
assert game.game_over() is True
assert Nim(2) == Nim(2)
assert Nim(2) != Nim(3)
```

## Opgave 5 _Alfabetisch_ (5pt)

Bij de woorden `"adem"`, `"adders"` en `"bel"` staan de letters op
alfabetische volgorde. Gelijke opeenvolgende letters zijn toegestaan.
De woorden `"test"`, `"python"` en `"student"` voldoen niet.

Schrijf `alfabet_word(s)` voor een niet-leeg woord met uitsluitend kleine
letters a tot en met z. Geef een boolean terug. Gebruik recursie, zonder lus of
comprehension. Voeg een Nederlandse docstring en minstens drie betekenisvolle
assertions toe. Functie, docstring en assertions vormen samen één blok van 5
punten: alleen als het geheel voldoet, verdien je die punten.

Python kan letters vergelijken:

```python
assert "a" < "b"
```

Denk bij het basisgeval ook aan een woord van één letter en controleer zowel
stijgende als dalende overgangen.

## Opgave 6 _Moeilijke woorden_ (15pt)

Wat maakt een woord moeilijk? Voor deze oefening gebruik je de lengte van
woorden en zinnen als maat voor de leesbaarheid van een tekst.

| Begrip | Regel |
|---|---|
| Woord | Een deel dat `sentence.split()` oplevert. Alle tekens daarin tellen mee voor de lengte, ook een apostrof. |
| Zin | Een niet-leeg tekstdeel dat op een punt eindigt. |
| Complex woord | Langer dan 10 tekens. |
| Complexe zin | Meer dan 15 woorden. |
| Score | `100 * (complexe woorden + complexe zinnen) / (woorden + zinnen)` |

Schrijf `complexity_score(text)`, met een float als resultaat. De invoer bevat
één of meer niet-lege zinnen, ieder afgesloten met een punt. Zinnen bevatten
minstens één woord; punten komen uitsluitend voor als zinseinde.

Kies zelf een strategie en een structuur of taakverdeling. Licht beide keuzes
kort toe, bijvoorbeeld in twee alinea's naast je code. Maak een functionele
oplossing met comprehension of recursie, of een OO-oplossing met zelf gekozen
samenwerkende objecten. Beide zijn geldig. Alleen imperatieve code in een
`def` voldoet niet aan de functionele keuze. Je krijgt 5 punten voor de
onderbouwde strategie, 5 voor de onderbouwde structuur en 5 voor een correcte
implementatie die bij die keuzes past. Dezelfde code krijgt geen extra
L2- of L3-punten.

Lees eerst de volgende assertions met uitleg goed door om te begrijpen hoe de
score in deze gevallen wordt bepaald. Je zal zien dat `round` wordt gebruikt om
de score af te ronden tot één cijfer achter de komma, dit is om eenvoudiger het
resultaat van de functie (de score) te kunnen testen.

```python
assert round(complexity_score("Dit is een korte zin."), 1) == 0.0
# Uitleg:
# Woorden (5): Dit(1) is(2) een(3) korte(4) zin(5)
# Zinnen (1): 1 zin van 5 woorden (< 15, dus niet complex)
# Score: 0 complexe elementen / 6 totale elementen = 0.0%

assert (
    round(
        complexity_score(
            "Dit is een gecompliceerde zin met veel verschillende woorden erin verstopt."
        ),
        1,
    )
    == 16.7
)
# Uitleg:
# Woorden (11): Dit(1) is(2) een(3) gecompliceerde(4) zin(5) met(6) veel(7)
#               verschillende(8) woorden(9) erin(10) verstopt(11)
# Zinnen (1): 1 zin van 11 woorden (< 15, dus niet complex)
# Complex: gecompliceerde(14 letters), verschillende(13 letters)
# Score: 2 complexe woorden / 12 totale elementen ≈ 16.7%

assert (
    round(complexity_score("De intelligentie van computerprogramma's neemt toe."), 1)
    == 28.6
)
# Uitleg:
# Woorden (6): De(1) intelligentie(2) van(3) computerprogramma's(4)
#              neemt(5) toe(6)
# Zinnen (1): 1 zin van 6 woorden (< 15, dus niet complex)
# Complex: intelligentie(13 letters), computerprogramma's(19 letters)
# Score: 2 complexe woorden / 7 totale elementen ≈ 28.6%

assert (
    round(
        complexity_score(
            "Programmeren is leuk. Dit is een zeer lange zin die meer dan vijftien woorden bevat en daarom als complex wordt beschouwd bij deze analyse. Nog een zin."
        ),
        1,
    )
    == 6.7
)
# Uitleg:
# Zin 1 (3): Programmeren(1) is(2) leuk(3)
# Zin 2 (21): Dit(1) is(2) een(3) zeer(4) lange(5) zin(6) die(7) meer(8) dan(9)
#             vijftien(10) woorden(11) bevat(12) en(13) daarom(14) als(15)
#             complex(16) wordt(17) beschouwd(18) bij(19) deze(20) analyse(21)
# Zin 3 (3): Nog(1) een(2) zin(3)
# Complex: programmeren(12 letters), en zin 2 (21 woorden > 15)
# Score: 2 complexe elementen / 30 totale elementen ≈ 6.7%
```

Hint: `text.split(".")[:-1]` kan zinnen opleveren en `sentence.split()` woorden.
Dit is een hulpmiddel; je bepaalt zelf hoe je de berekening organiseert.

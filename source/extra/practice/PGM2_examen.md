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
van PGM2. Het echte tentamen kan andere vragen bevatten.
Je berekent je cijfer met `1 + 9 * behaalde punten / 100`.

## Opgave 1 _Extensies_ (15pt)

Een bestandsnaam heeft meestal een extensie, zoals `.py`. Bijlagen die eindigen
op `.exe` kunnen schadelijke programma's bevatten. Het programma hieronder
kiest uit een lijst alleen de bestanden met een toegestane extensie.

Hoofdletters en kleine letters tellen als verschillende tekens: `.PY` past dus
niet op `.py`. Een lege extensie past op elke naam. De functies veranderen de
lijsten die je meegeeft niet. Namen blijven in dezelfde volgorde staan; staat
een naam tweemaal in de invoer, dan kan die ook tweemaal in het resultaat staan.

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
    """Geef passende bestandsnamen terug, in dezelfde volgorde en met herhalingen."""
    return [name for name in filenames if allowed_file(name, extensions)]


assert check_extension("a", "a") is True
assert select_files(["werk.py", "spel.exe", "leeg.txt"], [".py", ".txt"]) == [
    "werk.py",
    "leeg.txt",
]
```

Lees de code en beantwoord de vragen. Verwijs bij je uitleg naar de functies en
hun aanroepen. Je hoeft geen code te schrijven.

1. Leg voor elk van de drie functies uit welk deel van het werk die doet,
   welke gegevens je meegeeft en wat de functie teruggeeft. (5pt)
2. Loop de aanroepen na voor `"spel.exe"` met `[".py", ".txt"]`: hoe geeft
   `select_files` de naam door aan `allowed_file` en `check_extension`? Leg ook
   uit hoe de teruggegeven waarden bepalen of de naam in de uitkomst komt. (5pt)
3. Het programma moet voortaan hoofdletters en kleine letters hetzelfde
   behandelen. Dan moet `"WERK.PY"` ook passen op `".py"`. Kies in welke functie
   je dit zou aanpassen en leg uit waarom je die kiest. Wat betekent die
   aanpassing voor de andere twee functies en voor de aanroepen die al in het
   programma staan? Licht je antwoord toe. (5pt)

## Opgave 2 _Even op vele manieren_ (15pt)

Schrijf drie functies die getallen uit een lijst kiezen. Elke functie geeft een
nieuwe lijst terug en laat de oorspronkelijke lijst heel. De getallen blijven
in dezelfde volgorde staan. Komt een getal vaker voor, neem het dan ook vaker
mee als het aan de voorwaarde voldoet. De lijst bevat integers, die ook negatief
kunnen zijn. De lijst mag leeg zijn.

1. Schrijf `only_even_lc(L)`: geef de even getallen uit `L` terug met een list
   comprehension. (5pt)
2. Schrijf `only_even_rec(L)`: geef dezelfde even getallen terug met recursie.
   Gebruik geen lus of comprehension. (5pt)
3. Schrijf `select_numbers(numbers, predicate)`. De tweede parameter is een
   functie die één integer ontvangt en `True` of `False` teruggeeft. Roep deze
   meegegeven functie voor elk getal aan. Neem het getal op als de functie
   `True` teruggeeft. Je kiest zelf hoe je de lijst doorloopt. (5pt)

De twee laatste voorbeelden geven verschillende functies mee: de ene kiest
positieve getallen, de andere even getallen.

```python
assert only_even_lc([-2, -1, 0, 2, 2]) == [-2, 0, 2, 2]
assert only_even_rec([]) == []
assert select_numbers([-2, 0, 3], lambda number: number > 0) == [3]
assert select_numbers([-2, 0, 3], lambda number: number % 2 == 0) == [-2, 0]
```

## Opgave 3 _Bonus_ (15pt)

Studenten die huiswerk maakten krijgen 0.5 punt bij hun cijfer. Gebruik de
verzonnen gegevens hieronder. Elke rij bevat een studentnummer, een cijfer en
`True` als het huiswerk gemaakt is, anders `False`.

Soms staat een studentnummer meer dan eenmaal in de lijst. Gebruik dan alleen
de laatste rij voor dat nummer, zowel voor het cijfer als voor het huiswerk.
Verwerk eerst alle rijen en geef daarna eenmaal de bonus. Je hoeft een cijfer
na de bonus niet te begrenzen op een maximum.

```python
records = [
    ["S01", 7.6, True],
    ["S02", 5.1, False],
    ["S03", 6.4, True],
    ["S01", 8.0, False],
]
participants = {"S01", "S02", "S03", "S04"}
```

De set `participants` bevat de nummers van alle ingeschreven studenten, ook
studenten voor wie nog geen cijfer is ingevuld. Alle nummers uit `records`
staan ook in `participants`.

Maak de volgende gegevens. Je mag lussen of comprehensions gebruiken.

1. Maak `students`: een dictionary met het studentnummer als sleutel en
   `[cijfer, huiswerk]` als waarde. Houd bij dubbele nummers alleen de laatste
   rij over. (3pt)
2. Zoek in die dictionary op wie huiswerk maakte en verhoog de bijbehorende
   cijfers met 0.5. (3pt)
3. Maak `overview`: een lijst met voor elke student uit de dictionary een rij
   `[studentnummer, cijfer]`. Sorteer op studentnummer, van laag naar hoog. (3pt)
4. Maak `homework`: een set met de studentnummers waarvoor in de dictionary
   staat dat het huiswerk gemaakt is. Ieder nummer komt eenmaal in de set. (3pt)
5. Controleer met `in` of `"S03"` in `homework` staat. Maak ook `missing` met
   het verschil van de sets `participants` en `homework`: wie is wel
   ingeschreven, maar staat niet bij de huiswerkmakers? Een student zonder
   cijfer hoort ook bij deze groep. (3pt)

Bij de gegeven invoer moet je dit krijgen:

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
Dat lukt niet vanuit elke stand en zorgt dus niet altijd voor winst.

Schrijf de drie klassen uit de tabel en een lus waarmee je het spel speelt.
De mens begint, daarna is de computer aan de beurt. Laat de lus elke speler op
dezelfde manier om een zet vragen: roep `choose_move(game)` aan. Zo kun je ook
een ander spelersobject gebruiken als dat dezelfde methode heeft.

| Onderdeel | Wat moet het doen? |
|---|---|
| `Nim(number_of_sticks)` | Bewaar het aantal lucifers in `sticks`. Je mag aannemen dat het gegeven aantal een integer van nul of groter is; dat hoef je niet te controleren. |
| `Nim.player_takes(amount)` | Het aantal `amount` moet een integer zijn, minstens 1 en hoogstens 3, en niet groter dan het aantal lucifers op tafel. Trek een geldig aantal van `sticks` af. Gooi anders `ValueError` en laat `sticks` ongewijzigd. De methode geeft geen waarde terug. |
| `Nim.game_over()` | Geef `True` terug als er nul lucifers over zijn, anders `False`. |
| `Nim.__eq__(other)` | Vergelijk twee Nim-objecten: ze zijn gelijk als ze evenveel lucifers hebben. Een Nim-object is niet gelijk aan een object van een ander soort. Verander de objecten niet bij het vergelijken. |
| `Player.choose_move(game)` | Vraag de speler met `input` hoeveel lucifers die wil pakken. Zet de invoer om naar een integer en geef die terug. Verander het aantal lucifers niet. |
| `StrategicPlayer(Player)` | Maak een subklasse van `Player` en overschrijf `choose_move(game)`. Kies `game.sticks % 4` als dat niet nul is. Kies anders willekeurig een legaal aantal: 1, 2 of 3, maar nooit meer dan er liggen. Geef de keuze terug zonder het spel te veranderen. Roep deze methode alleen aan zolang er nog lucifers liggen. |

Liggen er twee lucifers, dan mag je er 1 of 2 pakken, maar geen 3. Liggen er nul,
dan kun je geen zet meer doen. `Nim(2) == Nim(2)` is waar: voor de vergelijking
kijk je alleen naar het aantal lucifers, niet naar wie aan de beurt is.

1. Schrijf de methoden waarmee `Nim` het aantal lucifers bewaart, een geldige
   zet uitvoert en nagaat of het spel afgelopen is. (7pt)
2. Schrijf de spellus. Vraag om beurten een zet aan de menselijke speler en de
   computer met `choose_move(game)` en laat `Nim` die zet uitvoeren. Toon vóór
   elke beurt hoeveel lucifers er liggen. Stop zodra de laatste gepakt is en
   meld wie wint. (7pt)
3. Schrijf `Player` en de subklasse `StrategicPlayer`. Gebruik de overschreven
   methode om de computer een zet te laten kiezen. Laat dezelfde spellus met
   beide spelers werken, zonder in de lus hun type te controleren. (6pt)
4. Schrijf `__eq__` zodat je Nim-objecten met `==` kunt vergelijken zoals in de
   tabel staat. (5pt)
5. Laat `player_takes` zelf `ValueError` gooien bij een ongeldige zet, voordat
   het aantal lucifers verandert. (5pt)
6. Vang in de spellus alleen `ValueError` af. Die fout kan ontstaan bij het
   omzetten van de invoer naar een integer of bij het uitvoeren van de zet.
   Meld `"Ongeldige zet"` en laat dezelfde speler opnieuw kiezen, met evenveel
   lucifers op tafel. Alleen de invoer vooraf controleren is niet genoeg:
   `player_takes` moet zelf de fout gooien en de lus moet die afvangen. (5pt)

Controleer `player_takes` ook zonder spellus, zoals hieronder. De ongeldige zet
mag het aantal lucifers niet veranderen; de geldige zet erna moet wel lukken.

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

In de woorden `"adem"`, `"adders"` en `"bel"` staan de letters op
alfabetische volgorde. Een letter mag hetzelfde zijn als de vorige, zoals de
twee d's in `"adders"`. Bij `"test"`, `"python"` en `"student"` staan de
letters niet op volgorde.

Schrijf `alfabet_word(s)`. Je mag aannemen dat `s` minstens één letter bevat en
alleen uit kleine letters a tot en met z bestaat. Geef `True` terug als de
letters op alfabetische volgorde staan, anders `False`.

Gebruik recursie, zonder lus of comprehension. Schrijf een Nederlandse docstring
en minstens drie assertions waarmee je de functie controleert. Kies voorbeelden
die verschillende gevallen controleren. De functie, docstring en assertions
leveren samen 5 punten op: je krijgt die punten als alle drie voldoen.

Python kan letters vergelijken:

```python
assert "a" < "b"
```

Denk bij je basisgeval aan een woord van één letter. Controleer ook gelijke
letters, letters die op volgorde staan en letters die niet op volgorde staan.

## Opgave 6 _Moeilijke woorden_ (15pt)

Wat maakt een woord moeilijk? In deze oefening gebruik je de lengte van woorden
en zinnen om een score voor een tekst te berekenen. Je telt de lange woorden
en zinnen en vergelijkt dat aantal met het totale aantal woorden en zinnen.

| Wat tel je? | Regel |
|---|---|
| Woord | Elk deel dat `sentence.split()` oplevert. Tel alle tekens voor de lengte, ook een apostrof. |
| Zin | Een stuk tekst met minstens één woord, afgesloten met een punt. |
| Complex woord | Een woord met meer dan 10 tekens. |
| Complexe zin | Een zin met meer dan 15 woorden. |
| Score | `100 * (complexe woorden + complexe zinnen) / (woorden + zinnen)` |

Schrijf `complexity_score(text)` en geef de score terug als float. De tekst
bevat minstens één zin. Elke zin bevat minstens één woord en eindigt met een
punt. Er staan geen andere punten in de tekst.

Bedenk zelf hoe je het probleem oplost. Kies ook zelf hoe je de code opbouwt:
welke functies of klassen heb je nodig en welk werk laat je elk daarvan doen?
Leg beide keuzes kort uit naast je code. Eén zelf bedachte functie kan genoeg
zijn; je mag ook meerdere functies of klassen gebruiken.

Kies voor functioneel programmeren met comprehension of recursie, of voor
objectgeoriënteerd programmeren met zelf gekozen objecten die samenwerken.
Beide zijn goed. Kies je de functionele oplossing, gebruik dan comprehension
of recursie. Alleen lussen en toekenningen in een functie zetten is daarvoor
niet genoeg.

Je krijgt 5 punten voor je uitleg van de gekozen aanpak, 5 voor je uitleg van
de opbouw van je code en 5 voor een werkende oplossing die deze keuzes volgt.
De programmeerwijze die je kiest levert hier geen extra punten op; deze opgave
heeft maximaal 15 punten.

De voorbeelden hieronder laten zien hoe je telt. `round` rondt de score af op
één cijfer achter de komma om de uitkomst te controleren. Laat je functie zelf
de score zonder die afronding teruggeven.

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

Hint: met `text.split(".")[:-1]` kun je de zinnen uit de tekst halen.
Met `sentence.split()` krijg je de woorden van een zin. Je mag deze hulpmiddelen
gebruiken; je kiest zelf hoe je er de berekening mee maakt.

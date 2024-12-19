---
lang: nl
papersize: a4
fontsize: 12pt
geometry: margin=2.5cm
toc: false
monofont: DejaVuSansMono.ttf
title: Oefententamen PGM2 2024/2025
---

# Proeftoets

<!--
1. recursie
2. recursie, list comprehension , lus
3. list comprehension
4. klassen
5. recursie
6. complexe vraag

pandoc tentamen.md -o tentamen.pdf  --pdf-engine=xelatex
-->

## Opgave 1 _Extensies_ (10pt)

<!-- recursie -->

Een bestand op een computer heeft meestal een extensie die aangeeft welk type
het is. Bijvoorbeeld, ".py" geeft aan dat het om een Python bestand gaat. In een
email is het meestal niet toegestaan om een bijlage mee te sturen die eindigt op
".exe" want dit zou namelijk malware kunnen zijn die schadelijk is voor de
computer.

We kunnen recursief bepalen of een string `s` (een bestandsnaam) eindigt met een
string `e` (een extensie):

- Als string `e` leeg is, geef `True` terug
- Als string `s` leeg is, geef `False` terug
- Als de laatste letter van `e` _niet_ gelijk is aan de laatste letter van `s`,
  geef `False` terug
- Anders roep je de functie opnieuw aan, maar dan zonder de _laatste_ letters
  van beide strings en geeft het resultaat daarvan terug.

Schrijf een functie `check_extension(s, e)` die gebruik maakt van het
bovenstaande recursief algoritme. Je mag **geen** gebruik maken van list
comprehensions of lusconstructies.

Bijvoorbeeld:

```python
assert check_extension("tentamen.docx", ".exe") == False
assert check_extension("program.exe", ".exe") == True
assert check_extension("wk8ex1.py", ".py") == True
```

## Opgave 2 _Even op vele manieren_ (15pt)

<!-- recursie, list comprehension -->

In deze opgave ga je op drie manieren een functie schrijven, achtereenvolgens
met behulp van een _lus_, vervolgens met behulp van _list comprehension_ en tot
slot _recursie_.

1. Schrijf de functie `only_even_loop(L)` die een lijst `L` accepteert met
   integers en een _lijst_ teruggeeft met enkel de **even** getallen in de lijst
   `L`. Los het probleem op met behulp van een _lus_. (5pt)

   Bijvoorbeeld:

   ```python
   assert only_even_loop([0, 1, 2, 3, 4]) == [0, 2, 4]
   ```

2. Schrijf de functie `only_even_lc(L)` die een lijst `L` accepteert met
   integers en een _lijst_ teruggeeft met enkel de **even** getallen in de lijst
   `L`. Los het probleem op met behulp van een _list comprehension_. (5pt)

   Bijvoorbeeld:

   ```python
   assert only_even_lc([0, 1, 2, 3, 4]) == [0, 2, 4]
   ```

3. Schrijf de functie `only_even_rec(L)` die een lijst `L` accepteert met
   integers en een _lijst_ teruggeeft met enkel de **even** getallen in de lijst
   `L`. Los het probleem op met behulp van _recursie_. (5pt)

   Bijvoorbeeld:

   ```python
   assert only_even_rec([0, 1, 2, 3, 4]) == [0, 2, 4]
   ```

## Opgave 3 _Bonus_ (10pt)

<!-- list comprehension -->

Gegeven is een lijst van studentnummers, het cijfer dat ze hebben behaald voor
een tentamen en of ze wel of niet het huiswerk hebben gemaakt. Studenten die het
huiswerk hebben gemaakt krijgen een 0.5 bonus op hun tentamencijfer.

Schrijf een **list comprehension** (_geen_ functie) die een lijst maakt van alle
studenten die het huiswerk hebben gemaakt met hun nieuwe cijfer inclusief bonus.
Noem deze lijst `HW`.

Bijvoorbeeld,

```python
L = [
    ["0308230", 7.6, True],
    ["8273927", 5.1, False],
    ["8234987", 6.4, False],
    ["2368612", 5.9, True],
    ["9731827", 3.2, False],
]
```

zal het volgende resultaat moeten opleveren:

```python
HW = [
    ["0308230", 8.1],
    ["2368612", 6.4],
]
```

<!--
De structuur van de list comprehension geven we je hier, jouw taak is om de
`...`'s in te vullen.

```python
HW = [... for ... in ... if ...]
```
-->

## Opgave 4 _Nim_ (20pt)

<!-- klassen -->

Nim is een spel voor twee spelers. Er liggen 16 lucifers op tafel en om de beurt
pakt een speler 1, 2 of 3 lucifers. Degene die de laatste lucifer van tafel
pakt, heeft gewonnen. De speler is altijd als eerste aan de beurt en de AI (de
computer) is tweede.

Zodra het de beurt is van de AI, pakt deze net zoveel lucifers totdat er weer
een meervoud van 4 op tafel ligt. Als er bijvoorbeeld 13 lucifers op tafel
liggen, dan zou de AI er 1 pakken zodat er 12 op tafel blijven liggen. Met deze
strategie wint de AI altijd.

```python
from random import choice

class Nim:
    def __init__(self, number_of_sticks):
        self.sticks = number_of_sticks

    # schrijf hier de functie player_takes()

    def AI_turn(self):
      ...

    def game_over(self):
      ...


game = Nim(16)

while True:
    print("Aantal stokjes op tafel: ", game.sticks)

    player_turn = int(input("Hoeveel stokjes pak je? "))

    if player_turn not in [1, 2, 3]:
        print("Aantal niet toegestaan ...")
        continue

    # de beurt van de speler
    game.player_takes(player_turn)

    if game.game_over():
        print("Jij wint")
        break

    # de beurt van de computer
```

1. Schrijf de functie `player_takes` binnen de klasse `Nim`. Deze functie
   accepteert een parameter `player_turm` (een integer) die aangeeft hoeveel
   lucifers een speler van tafel pakt en de variabele `self.sticks` vervolgens
   aanpast. (5)

2. Maak de functie `AI_turn` af. Deze geeft het aantal lucifers dat de AI wil
   pakken terug. De AI wil altijd een meervoud van vier op tafel laten liggen;
   als dat niet mogelijk is, kiestx het een willekeurige hoeveelheid lucifers.
   Gebruik `random.choice([1, 2, 3])` om een random aantal lucifers tussen 1 en
   3 te kiezen. (5)

3. Maak de functie `game_over` af. Deze functie controleert of het spel voorbij
   is door te checken of er nog lucifers op tafel liggen. Als er geen lucifers
   liggen, geeft het true terug en anders false. (5)

4. De `while`-lus is niet helemaal compleet. De beurt van de computer ontbreekt.
   Maak de `while`-lus af door de beurt van de computer toe te voegen onder het
   commentaar `# de beurt van de computer`. (5)

## Opgave 5 _Alfabetisch_ (15pt)

<!-- recursie -->

De woorden "adem", "adders" en "bel" zijn woorden waarbij de letters op
alfabetische volgorde staan. Bijvoorbeeld in het geval van "bel" volgt in het
alfabet de letter "e" op "b" en de letter "l" op "e". Voor de woorden "test",
"python" en "student" geldt dit niet.

1. Schrijf de functie `alfabet_word(s)` die een string `s` accepteert (een
   woord) en als resultaat `True` teruggeeft indien de letters in alfabetische
   volgorde staan en anders `False`.

   Maak gebruik van **recursie**. Je mag _geen_ gebruik maken van list
   comprehension of lusconstructies.

2. Voeg ook een docstring en 3 assertions toe.

Bedenk dat Python weet van de volgorde van letters, bijvoorbeeld:

```python
assert "a" > "b" is True
```

## Opgave 6 _Moeilijke woorden_ (20pt)

Wat is precies een moeilijk woord? Dat lijkt een makkelijke vraag, maar welk
kenmerk van een woord bepaalt of het moeilijk is? Onderzoekers zijn hier niet
over uit, maar in sommige experimenten lijkt de lengte van woorden en zinnen
effect te hebben op de begrijpelijkheid van teksten bij lezers met een laag
niveau van leesvaardigheid.

Een onderzoeker (jij) wil de complexiteit van een tekst bepalen op basis van de
volgende regels:

1. Een woord is 'complex' als het langer is dan 10 letters
2. Een zin is 'complex' als deze meer dan 15 woorden bevat
3. De complexiteitsscore wordt als volgt berekend:
   - Tel het totaal aantal woorden en zinnen (dit is het totaal aantal
     elementen)
   - Tel het aantal complexe woorden plus het aantal complexe zinnen (dit is het
     totaal aantal _complexe_ elementen)
   - De score is: (aantal _complexe_ elementen / totaal aantal elementen)
     $\times$ 100

Het is jouw taak om een functie `complexity_score(text)` te schrijven die een
string `text` als parameter accepteert en als resultaat een score (float)
teruggeeft. De string `text` kan meerdere zinnen bevatten.

In deze opgave mag je zelf bepalen hoe je dit probleem oplost, alles is
toegestaan. Dit wil zeggen dat je lussen, list comprehension, recursie,
eventuele hulpfuncties en verder alle ingebouwde Python-functies mag gebruiken.

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
    == 15.4
)
# Uitleg:
# Woorden (11): Dit(1) is(2) een(3) gecompliceerde(4) zin(5) met(6) veel(7)
#               verschillende(8) woorden(9) erin(10) verstopt(11)
# Zinnen (1): 1 zin van 11 woorden (< 15, dus niet complex)
# Complex: gecompliceerde(13 letters), verschillende(13 letters)
# Score: 2 complexe woorden / 12 totale elementen ≈ 15.4%


assert (
    round(complexity_score("De intelligentie van computerprogramma's neemt toe."), 1)
    == 25.0
)
# Uitleg:
# Woorden (6): De(1) intelligentie(2) van(3) computerprogramma's(4)
#              neemt(5) toe(6)
# Zinnen (1): 1 zin van 6 woorden (< 15, dus niet complex)
# Complex: intelligentie(12 letters), computerprogramma's(16 letters)
# Score: 2 complexe woorden / 7 totale elementen ≈ 25.0%

assert (
    round(
        complexity_score("""Programmeren is leuk.
Dit is een zeer lange zin die meer dan vijftien woorden bevat en daarom als complex wordt beschouwd bij deze analyse.
Nog een zin."""),
        1,
    )
    == 6.5
)
# Uitleg:
# Zin 1 (3): Programmeren(1) is(2) leuk(3)
# Zin 2 (21): Dit(1) is(2) een(3) zeer(4) lange(5) zin(6) die(7) meer(8) dan(9)
#             vijftien(10) woorden(11) bevat(12) en(13) daarom(14) als(15)
#             complex(16) wordt(17) beschouwd(18) bij(19) deze(20) analyse(21)
# Zin 3 (3): Nog(1) een(2) zin(3)
# Complex: programmeren(11 letters), en zin 2 (21 woorden > 15)
# Score: 2 complexe elementen / 30 totale elementen ≈ 6.5%
```

Tot slot het volgende, de string-methode `split()` geeft een lijst van strings
terug. Gebruik deze methode om een tekst op te delen op basis van een
scheidingsteken:

- `text.split(".")` voor het opdelen van een tekst in zinnen
- `sentence.split()` voor het opdelen van een zin in woorden (hier is geen
  scheidingsteken nodig, standaard zal worden opgedeeld op basis van een spatie)

Let op: bij het splitsen van zinnen en vervolgens woorden zullen enkele woorden
toch nog een spatie bevatten, en ontstaan er soms lege zinnen. Het is _niet_
nodig om hier rekening mee te houden!

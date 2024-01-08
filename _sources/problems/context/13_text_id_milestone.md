# Tekstidentificatie

Dit is een vervolg van de context opdracht van week 12. [tekstidentificatie](12_text_id_begin.md)

## De methode `clean_string`

De methode `clean_string(self, s)` krijgt een string `s` mee en geeft een opgeschoonde versie ervan terug zonder
leestekens en zonder hoofdletters.

Je kan `s = s.lower()` gebruiken om hoofdletters te vervangen; hoe je leestekens weghaalt mag je zelf bepalen; gebruik hier echter **geen** recursie, maar lussen (recursie loopt op grote strings uit het geheugen!)

:::{admonition} Tip
:class: tip

Je kan `import string` gebruiken, en dan deze lus gebruiken:

```python
for p in string.punctuation
```

In deze lus krijgt `p` opeenvolgende de waarde van alle mogelijke leestekens, dus je kan `s = s.replace(p, '')` gebruiken om elk leesteken te vervangen door de lege string!

Probeer dit wel eerst op een korte string, als je deze aanpak wilt gebruiken...
:::

Je kan onderstaande code gebruiken om je resultaten te controleren.

```python
tm = TextModel()
tm.read_text_from_file('test.txt')
clean_text = """dit is een korte zin dit is geen korte zin omdat
deze zin meer dan 10 woorden en een getal bevat dit is
geen vraag of wel"""
clean_s = tm.clean_string(tm.text)
assert clean_s == clean_text
```

Dit moet wederom geen uitvoer geven. Merk op dat het *niet* handig is om getallen te verwijderen!

## De methode `make_word_lengths`

De methode `make_word_lengths(self)` lijkt op de methode `make_sentence_lengths`, alleen wordt hier een dictionary gemaakt van de woordlengtes (dit is wat Sarah Pavis gebruikte om J.K. Rowling te herkennen!)

Zorg dat je hiervoor de **opgeschoonde** string gebruikt, zonder leestekens!

Je kan onderstaande code gebruiken om je resultaten te controleren.

```python
tm = TextModel()
tm.read_text_from_file('test.txt')
tm.make_word_lengths()
assert tm.word_lengths == {2: 6, 3: 10, 4: 4, 5: 6, 7: 1}
```

Ook hier geldt dat de volgorde van de sleutels niet uitmaakt, *maar de sleutel-waardeparen moeten wel hetzelfde zijn*!

## De methode `make_words`

De methode `make_words(self)` lijkt op de methode `make_word_lengths`, alleen wordt hier een dictionary gemaakt van de woorden zelf (opgeschoond!) Gebruik dus ook hiervoor de **opgeschoonde** string.

Je kan onderstaande code gebruiken om je resultaten te controleren.

```python
tm = TextModel()
tm.read_text_from_file('test.txt')
tm.make_words()
assert tm.words == {
  'dit': 3, 'is': 3, 'een': 2, 'korte': 2, 'zin': 3, 'geen': 2,
  'omdat': 1, 'deze': 1, 'meer': 1, 'dan': 1, '10': 1, 'woorden': 1,
  'en': 1, 'getal': 1, 'bevat': 1, 'vraag': 1, 'of': 1, 'wel': 1
}
```

Ook hier mag de volgorde van je sleutel-waardeparen anders zijn, maar moeten het *wel* dezelfde paren zijn!

## De methode `make_stems`

De methode `make_stems(self)` lijkt op de methode `make_words`, alleen wordt hier een dictionary gemaakt van de
stammen van de woorden zelf (opgeschoond!) Ook hier moet je de **opgeschoonde** string hiervoor gebruiken.

Je kan onderstaande code gebruiken om je resultaten te controleren.

```python
tm = TextModel()
tm.read_text_from_file('test.txt')
tm.make_stems()
assert tm.stems == {
  'dit': 3, 'is': 3, 'een': 2, 'kort': 2, 'zin': 3, 'gen': 2,
  'omdat': 1, 'dez': 1, 'mer': 1, 'dan': 1, '10': 1, 'woord': 1,
  'en': 1, 'getal': 1, 'bevat': 1, 'vrag': 1, 'of': 1, 'wel': 1
}
```

Je resultaat zou hier wel kunnen afwijken, als je een andere *stemmer* (algoritme om stammen van woorden te bepalen)
gebruikt. Dat is prima, als het resultaat maar redelijk is (zodat niet elk woord dezelfde stam heeft!) is je stemmer
goed. (Je kan ook proberen een aantal verschillende vormen van dezelfde woorden aan het bestand toe te
voegen...)

Om `make_stems` te implementeren, moet je een functie schrijven die woorden als invoer krijgt en
stammen als uitvoer geeft. Je mag hierbij:

* Je eigen schrijven (het moet ten minste tien stemmingregels bevatten. *Je hoeft niet alle mogelijke regels te implementeren*; dat zou ook niet kunnen, daar zijn te veel uitzonderingen voor!)
* Online een stemming-bibliotheek zoeken en die in je project gebruiken
* Of [deze stemmer](../assets/snowball.py) gebaseerd op de Nederlandse stemmer in *Snowball*, een bibliotheek van stemmers. Deze is ook niet perfect, maar een redelijke kandidaat om te gebruiken.
* Als je deze wilt gebruiken, voeg dan deze code toe bovenaan je bestand. Je kan dan `create_stem(w)` aanroepen, waar `w` het woord is waarvan je de stam wilt hebben!

## Het bouwen van een model door `TextModel` testen

Je kan hier een aantal tests vinden die je kan gebruiken om te kijken of je code voldoet aan de eisen die we aan de milestone stellen. Je kan deze onderaan je bestand plakken en dan je bestand uitvoeren. 

Merk op dat je geen dictionary met leestekens hoeft te maken! Je moet echter wel **een andere** dictionary maken  naast de standaard vier: stammen, woorden, woordlengtes en zinlengtes. (En, als je leestekens fijn vindt, mag je die ook gebruiken!)

```python
# zet de tekst tussen de triple quotes in een bestand genaamd test.txt
test_text = """Dit is een korte zin. Dit is geen korte zin, omdat
deze zin meer dan 10 woorden en een getal bevat! Dit is
geen vraag, of wel?"""

tm = TextModel()
tm.read_text_from_file('test.txt')
assert tm.text == test_text

# maak alle dictionary's
tm.make_sentence_lengths()
tm.make_word_lengths()
tm.make_words()
tm.make_stems()
tm.make_punctuation()

# alle dictionary's bekijken!
print('Het model bevat deze dictionary\'s:')
print(tm)
```

Dit zijn de resultaten die je kan verwachten bij dit voorbeeld: controleer dat in ieder geval
de zinlengtes, woordlengtes en woorden hetzelfde zijn!

```text
Het model bevat deze dictionary's:
Woorden:
{'woorden': 1, 'is': 3, 'vraag': 1, 'en': 1, 'zin': 3, 'of': 1, 'wel': 1, 'omdat': 1, 'deze': 1, 'een': 2, 'geen': 2, 'korte': 2, 'dit': 3, 'bevat': 1, '10': 1, 'getal': 1, 'meer': 1, 'dan': 1}

Woordlengtes:
{2: 6, 3: 10, 4: 4, 5: 6, 7: 1}

Stammen:
{'dez': 1, 'mer': 1, 'kort': 2, 'vrag': 1, 'zin': 3, 'gen': 2, 'of': 1, 'een': 2, 'en': 1, 'wel': 1, 'omdat': 1, 'dit': 3, 'bevat': 1, 'is': 3, 'woord': 1, '10': 1, 'getal': 1, 'dan': 1}

Zinslengtes:
{16: 1, 5: 1, 6: 1}

Leestekens:
{'.': 1, ',': 2, '!': 1, '?': 1}
```

Je hoeft het niet precies zo af te drukken, dit is puur om te testen!


## De opdracht

De milestone, `milestone.py`, moet aan de volgende eisen voldoen:

* Het bevat een klasse `TextModel` met een werkende constructor en `__repr__`
* Deze klasse bevat twee werkende methodes `read_text_from_file` en `clean_string`
* Deze klasse bevat de werkende teksteigenschapmethode `make_sentence_lengths`, `make_word_lengths`, `make_words` en `make_stems`


# Tekstidentificatie

In dit project ga je Python gebruiken om een statistisch model van tekst te maken waarmee je een auteur of stijl kan "herkennen", met een verschillende mate van succes, aan de hand van stukken tekst!

## Achtergrond

Statistische modellen zijn één manier om in een getal te vangen hoe erg twee stukken tekst op elkaar lijken. Zulke modellen zijn bijvoorbeeld in de zomer van 2013 gebruikt als bewijs dat het boek *Koekoeksjong* (*The Cuckoo's Calling*) door J.K. Rowling geschreven was (onder de naam Robert Galbraith). Details over dat verthaal en de analyse die gedaan is kan je [op deze link vinden](https://www.scientificamerican.com/article/how-a-computer-program-helped-show-jk-rowling-write-a-cuckoos-calling/).

De vergelijkende analyse van deze werken gebruikte simpele modellen; misschien zelfs verbazingwekkend simpel; van de "stijl van een auteur", met bijvoorbeeld de verdeling van woordlengtes in een tekst. De vijf "teksteigenschappen" die we je vragen te implementeren voor dit project zijn:

* De verdeling van woorden die de auteur gebruikt.
* De verdeling van woordlengtes (zoals hierboven benoemd).
* De verdeling van gebruikte woordstammen ("loopt" en "lopen" hebben bijvoorbeeld dezelfde stam).
* De verdeling van gebruikte zinslengtes (in aantal woorden).

Je moet bovendien ten minste één extra "teksteigenschap" die je zelf ontworpen hebt toevoegen:
* Je kan bijvoorbeeld leestekens op een bepaalde manier gebruiken.
* Of je kan iets anders over de tekst berekenen; bijvoorbeeld het aantal woorden die op "heid" eindigen, iets over de hoofdletters, of iets anders dat je kan berekenen of tellen met Python...

Hier kan je een artikel vinden over een [leestekenanalyse](https://mentalfloss.com/article/75602/what-famous-novels-look-stripped-everything-punctuation) van een aantal teksten...

Misschien de *bekendste en succesvolste toepassing* van dit soort tekstanalyse is het [herkennen en filteren van e-mailspam](https://nl.wikipedia.org/wiki/Spamfilter). Tegenwoordig is het herkennen van tekst dat door een AI (bijv. chatGT) is geschreven een hot item. 

## De klasse `TextModel`

Om je tekstherkenningssysteem te maken maak je een klasse `TextModel`, die een aantal dictionary's bevat.
Elk van deze dictionary's beschrijft één "eigenschap" voor het herkennen van tekst.

Hier is wat begincode die een model maakt met de volgende vier dictionary's, die allemaal leeg beginnen:

* `words`
* `word_lengths`
* `stems`
* `sentence_lengths`

Vergeet niet nog een extra dictionary toe te voegen voor je eigen teksteigenschap! Je mag hiervoor best leestekens gebruiken, en ook andere opties zijn goed.

```python
#
# textmodel.py
#
# Opdracht: Tekstidentificatie
#
# Naam:
#


class TextModel:
    """A class supporting complex models of text."""

    def __init__(self):
        """Create an empty TextModel."""
        #
        # Maak dictionary's voor elke eigenschap
        #
        self.words = {}             # Om woorden te tellen
        self.word_lengths = {}      # Om woordlengtes te tellen
        self.stems = {}             # Om stammen te tellen
        self.sentence_lengths = {}  # Om zinslengtes te tellen
        #
        # Maak een eigen dictionary
        #
        self.my_feature = {}        # Om ... te tellen

    def __repr__(self):
        """Display the contents of a TextModel."""
        s = 'Woorden:\n' + str(self.words) + '\n\n'
        s += 'Woordlengtes:\n' + str(self.word_lengths) + '\n\n'
        s += 'Stammen:\n' + str(self.stems) + '\n\n'
        s += 'Zinslengtes:\n' + str(self.sentence_lengths) + '\n\n'
        s += 'MIJN EIGENSCHAP:\n' + str(self.my_feature)
        return s

    # Voeg hier andere methodes toe.
    # Je hebt in het bijzonder methodes nodig die het model vullen.


# Hier kan je dingen testen...
tm = TextModel()
# Zet hier aanroepen neer die het model vullen met informatie
print('TextModel:', tm)
```

We geven hieronder meer details, en een aantal tests om te zorgen dat je methodes werken.

### De methode `__repr__`

De methode `__repr__(self)` geeft een overzicht terug van alle dictionary's in het model, zodat je ermee kan testen en
kan controleren dat ze werken.

Deze methode staat al in de begincode hierboven.

### De methode `read_text_from_file(self, filename)`

De methode `read_text_from_file(self, filename)` moet een bestandsnaam (een string) meekrijgen en de inhoud van dat bestand als één hele lange string toekennen aan de variabele `self.text`.

Hier is een voorbeeld dat je kan proberen; sla deze tekst op in een bestand met de naam `test.txt`:

```
Dit is een korte zin. Dit is geen korte zin, omdat
deze zin meer dan 10 woorden en een getal bevat! Dit is
geen vraag, of wel?
```

Je kan vervolgens deze code gebruiken om de methode te testen.

```python
tm = TextModel()
# zorg dat deze tekst in een bestand genaamd test.txt staat
test_text = """Dit is een korte zin. Dit is geen korte zin, omdat
deze zin meer dan 10 woorden en een getal bevat! Dit is
geen vraag, of wel?"""

tm.read_text_from_file('test.txt')
assert tm.text == test_text
```

Dit zou niets moeten afdrukken; als je code niet werkt krijg je een `AssertionError`!

### De methode `make_sentence_lengths`

De methode `make_sentence_lengths(self)` moet de tekst in `self.text` gebruiken om de dictionary `self.sentence_lengths` te vullen.

Je kan hier voorbouwen op de code die je eerder hebt geschreven voor de [Markov-opgave](/problems/tekst_genereren.md) om het einde van zinnen te herkennen.

Je kan onderstaande code gebruiken om je resultaten te controleren.

```python
tm = TextModel()
tm.read_text_from_file('test.txt')
tm.make_sentence_lengths()
assert tm.sentence_lengths == {16: 1, 5: 1, 6: 1}
```

Dit moet geen uitvoer geven, omdat er in dit voorbeeld één zin met 16 woorden, één met 5 woorden en één met 6 woorden is.

:::{admonition} Opmerking
:class: notice

De volgorde van de sleutels in de dictionary is niet belangrijk; het maakt voor de `assert` niet uit welke volgorde ze hebben.
:::


## De Opdracht: 

Het begin, `begin.py`, moet aan de volgende eisen voldoen:

* Het bevat een klasse `TextModel` met een werkende constructor en `__repr__`
* Deze klasse bevat een werkende methode `read_text_from_file`
* Deze klasse bevat de werkende teksteigenschapmethode `make_sentence_lengths`

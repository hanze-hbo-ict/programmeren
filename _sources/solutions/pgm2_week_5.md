# PGM2 week 5

## Basis

### [Vier op een rij: Begin](/problems/basis/12_vier_op_een_rij_begin)



#### Opdracht 1

Het importerne/kopieren en testen van de twee klasses spreekt voor zich. Mocht je vragen hebben, ga naar de docent.


#### Opdracht 2

De methode `opp_char` bepaalt aan de hand van de eigen steen wat de steen van de tegenstander is.

```python
def opp_ch(self):
    """Returns the stone used by the other player."""
    if self.ox == 'O':
        return 'X'
    else:
        return 'O'
```

Om de steen van de huidige speler te kunnen benaderen, moeten we `self.` voor de relevante variabele plaatsen. Met `self.` geven we aan dat het programma een variable moet gebruiken die onderdeel is van de klasse. Deze functie staat in de klasse `Player`!


#### Opdracht 3

De methode score_board() wordt aangeroepen met een object van type board, een andere class. Dit kan gewoon zolang het programma toegang heeft tot de class.

```python
def score_board(self, b):
    """Returns the score of Board b as a float-variable."""
    # Als self het board gewonnen heeft, geef 100.0 terug
    if b.wins_for(self.ox):
        return 100.0
    # Als self verloren heeft, geef 0.0 terug
    elif b.wins_for(self.opp_ch()):
        return 0.0
    # Als self niet gewonnen of verloren heeft, geef 50.0 terug
    else:
        return 50.0
```

De uitdaging bij deze opdracht is om goed in de gaten te houden wanneer een variabele van de huidige class gebruikt wordt en dus `self.` nodig is, en hoe de variabele van de andere class te benaderen. In dit geval is `b` al een bestaand object en wordt er niet met `self.` gewerkt, maar `b.` om methoden en variabelen die onderdeel zijn van `b` te benaderen. Deze functie staat in de klasse `Player`!


## Context

### [Tekstidentificatie](/problems/context/12_text_id_begin)

In deze opdracht wordt een begin gemaakt aan een tekstherkenningssyteem welke als klasse wordt uitgewerkt.

```python
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
    def read_text_from_file(self, filename):
        """ Opens filename and assigns to content to self.text """
        f = open(filename, 'r')
        self.text = f.read()
        f.close()

    def make_sentence_lengths(self):
        """ Retrieves the lengths of the sentences """
        words = self.text.split() # Door de text in woorden te splitsen, kunnen we per woord kijken
        wordcount = 0 # Woorden tellen per zin, we beginnen met nul woorden
        # We negeren leestekens die niet het einde van een zin signaleren
        for word in words:
            wordcount += 1
            if word[-1] in '.?!': # We hebben het laatste woord van een zin
                if wordcount in self.sentence_lengths: # De zinslengte staat al in dictionary en hoeft alleen aangepast te worden.
                    self.sentence_lengths[wordcount] += 1
                else: # De zinslengte staat nog niet in de dictionary
                    self.sentence_lengths.update({wordcount: 1})
                wordcount = 0 # Vergeet niet te resetten! Het volgende woord is het eerste woord van een nieuwe zin
```
# PGM2 week 6

## Basis

### [Vier op een rij: Milestone](/problems/basis/13_vier_op_een_rij_milestone)

#### Opdracht 1

In deze opdracht wordt gevraagd een methode te schrijven die een zet terug geeft die de beste zet is afhankelijk van de input lijst met scores.

Met comments in de code wordt al uitgelegd wat wanneer gedaan wordt.

```python
def tiebreak_move(self, scores):
    """Gives column with highest score or with a tie, follows the strategy"""
    # Bepaal de hoogste score in de lijst
    max_score = max(scores)

    # Bepaal op welke kolom(men) de max gevonden is
    max_indices = []
    for x in range(len(scores)): # de lengte van indices en score is hetzelfde
        if scores[x] == max_score:
            max_indices += [x] # Index is gelijk aan kolomnummer
    # print(max_indices)

    # Bepaal de zet
    # Als er maar een kolom met de hoogste score is dan moet die terug gegeven worden
    if len(max_indices) == 1:
        return max_indices[0]
    # Als er meerdere kolommen zijn met de hoogste waarde dan bepaalt de strategie welke kolom/index gekozen moet worden
    if self.tbt == 'LEFT': # De meest linker kolom moet gekozen worden.
        # LET OP: de strategie wordt volledig in hoofdletters gegeven!
        return max_indices[0]
    elif self.tbt == 'RIGHT': # De meest rechter kolom moet gekozen worden
        # LET OP: de strategie wordt volledig in hoofdletters gegeven!
        return max_indices[-1]
    else: # De strategie is RANDOM, kies een willekeurige kolom
        # print("random")
        return random.choice(max_indices)
```


#### Opdracht 2

De methode `scores_for` geeft een lijst scores terug, waarbij de score op index c aangeeft hoe “goed” het bord is nadat de speler een zet in kolom c doet. “Goedheid” wordt gemeten door wat er in het spel zal gebeuren na self.ply zetten.

De opdracht zelf legt al uit wanneer wat moet gebeuren. Verdere uitleg staat in de code zelf als comments.

```python
def scores_for(self, b):
    """
    Gives a list of scores for each column of the board after a ply is made in the column corresponding to the list index.
    """
    # Begin scores
    scores = [50.0] * b.width
    # Check of de huidige speler of de tegenstander al gewonnen heeft en zet dit voor gemak en leesbaarheid van de code in variabelen
    self_won = b.wins_for(self.ox)
    opp_won = b.wins_for(self.opp_ch())

    # Update scores
    for col in range(len(scores)): # Kijk per kolom
        # Is de kolom vol?
        if b.data[0][col] != ' ': #De bovenste rij is rij 0, en als deze conditie true is, dan is de kolom vol
            scores[col] = -1.0
            # In een volle kolom kan geen zet gedaan worden...

        # Als een van beide spelers al gewonnen heeft dan heeft een nieuwe zet geen toegevoegde waarde
        if self_won: # De speler heeft al gewonnen
            scores[col] = 100.0
        if opp_won: # De tegenstander heeft al gewonnen
            scores[col] = 0.0

        # Tijd voor recursie
        # Basis geval, er wordt niet in de toekomst gekeken
        if self.ply == 0:
            # Omdat er niet toekomst gekeken hoeft te worden, kijk je naar de situatie nu
            scores[col] = self.score_board(b)
        else:
            # Doe een zet in de huidige kolom
            # In een volle kolom kan geen zet gedaan worden...
            # Dus check of er een zet in de kolom mogelijk is
            if b.allows_move(col):
                # Doe een zet in de huidige kolom
                b.add_move(col, self.ox)
                # Check of dit voor een win zorgt
                if b.wins_for(self.ox):
                    # Gewonnen met een zet in deze kolom, zet de score naar 100.0
                    scores[col] = 100.0
                else:
                    # Niet gewonnen, tegenstander is aan de beurt
                    # Maak tegenstander met de andere steen, zelfde strategie en ply-1 aangezien er een zet gedaan is
                    opp = Player(self.opp_ch(), self.tbt, self.ply-1)
                    # Wat zijn de scores voor de tegenstander met het nieuwe bord?
                    opp_scores = opp.scores_for(b)

                    # De score voor self moet nu geupdate worden met: "dit is honderd min de beste score van de tegenstander"
                    # Alleen de score van de huidige kolom wordt aangepast!
                    scores[col] = 100.0 - max(opp_scores)

                # Verwijder de zet van eerder
                b.del_move(col)

    return scores
```


## Context

### [Tekstidentificatie](/problems/context/13_text_id_milestone)

#### Opdracht methode `clean_string`

```python
def clean_string(self, s):
    """ Removes punctuation marks from and changes capital letters to lowercase letters in sentence s"""
    for p in string.punctuation:
        s = s.replace(p, '')
    s = s.lower()
    return s
```


#### Opdracht methode `make_word_lengths`

```python
def make_word_lengths(self):
    """ Counts and stores all the word lengths of a text """
    # Krijg alle woorden
    words = self.text.split()
    # Met een forlus gaan we over elk woord, bepalen de woord lengte en voegen we de lengte toe aan het juiste dict
    for word in words:
        word_length = len(self.clean_string(word))
        if word_length in self.word_lengths:
            self.word_lengths[word_length] += 1
        else:
            self.word_lengths.update({word_length: 1})
```


#### Opdracht methode `make_words`

```python
def make_words(self):
    """ Makes a dictionary of words and how often they were found in a text """
    words = self.text.split()
    for word in words:
        clean_word = self.clean_string(word)
        if clean_word in self.words:
            self.words[clean_word] += 1
        else:
            self.words.update({clean_word: 1})
```


#### Opdracht methode `make_stems`

```python
# Buiten de class
def create_stem(w):
    """ Generate the stem version of word w """

    # Hier zijn een paar voorbeelden van stamregels
    stem = ''
    if len(w) > 5:
        if w[-2:] == 'en':
            stem = w[0:-2]

        if stem[-2] in 'aeo':
            if stem[-3] not in 'ieaou':
                stem = stem[0:-1] + stem[-2] + stem[-1]
        elif stem[-1] == stem[-2]:
            stem = stem[:-1]

        if stem[-1] == 'z':
            stem = stem[:-1] + 's'
        elif stem[-1] == 'v':
            stem = stem[:-1] + 'f'
    else:
        stem = w

    # Voeg hier de andere regels toe

    return stem

# In de class
def make_stems(self):
    """ Makes a dictionary of the stems of words """
    words = self.text.split()
    for word in words:
        stem = create_stem(self.clean_string(word))
        if stem in self.words:
            self.words[stem] += 1
        else:
            self.words.update({stem: 1})
```
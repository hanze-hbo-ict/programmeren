# Twee voorbeelden van hoe je tekst uit een bestand kan lezen en kan verwerken.

# om dit te laten werken moet je een bestand met de naam
#
# a.txt
#
# in dezelfde directory als dit .py-bestand maken!


def count_words(filename):
    """Word-counting function.

    Opens a file named 'filename', reads it,
    and returns the number of words in the file.

    Example: count_words('a.txt')
    """
    #
    # Eerst moeten we het bestand "openen" (net als het openen van een boek
    # om dat te lezen). We vragen Python om de encoding "utf-8" te gebruiken,
    # omdat dat meer tekens dan ASCII accepteert.
    #
    fhand = open(filename, encoding="utf-8")

    #
    # Lees nu de hele inhoud van het bestand in een string met de naam "text",
    # en sluit het bestand. Merk op dat dit alleen werkt voor relatief kleine
    # bestanden; grotere bestanden moet je regel voor regel lezen door
    # 'f.readline()' in een lus aan te roepen.
    #
    text = fhand.read()
    fhand.close()

    #
    # De tekst van het bestand is één lange string. Gebruik "split" om
    # de tekst op te delen in "woorden" begrensd door whitespace.
    #
    words = text.split()

    #
    # words is een lijst woorden, dus de lengte is het aantal woorden.
    #
    return len(words)


def count_vocab(filename):
    """Vocabulary-counting function.

    Opens a file named 'filename', reads it, and breaks it into words.
    Then, for each word, counts how many times it occurs.
    Prints a message giving the number of distinct words in the file,
    and then returns a dictionary in which each word is a key and
    the word's frequency is the value.

    Example: count_vocab('a.txt') might print 3 and return
    {'I': 2, 'love': 3, 'spam': 42}
    """
    fhand = open(filename, encoding="utf-8")
    text = fhand.read()
    fhand.close()

    words = text.split()
    print("Er zijn", len(words), "woorden.")

    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    print("Er zijn", len(word_count), "*verschillende* woorden.\n")
    # op deze manier kunnen we de gegevens in word_count later gebruiken!
    return word_count

# Twee voorbeelden van hoe je tekst uit een bestand kan lezen en kan verwerken.

# om dit te laten werken moet je een bestand met de naam
#
# a.txt
#
# in dezelfde directory als dit .py-bestand maken!


def wc(filename):
    """Word-counting function.

    Opens a file named 'filename', reads it,
    and returns the number of words in the file.

    Example: wc('a.txt')
    """
    #
    # Eerst moeten we het bestand "openen" (net als het openen van een boek
    # om dat te lezen). We vragen Python om de encoding "utf-8" te gebruiken,
    # omdat dat meer tekens dan ASCII accepteert.
    #
    f = open(filename, encoding="utf-8")

    #
    # Lees nu de hele inhoud van het bestand in een string met de naam "text",
    # en sluit het bestand. Merk op dat dit alleen werkt voor relatief kleine
    # bestanden; grotere bestanden moet je regel voor regel lezen door
    # 'f.readline()' in een lus aan te roepen.
    #
    text = f.read()
    f.close()

    #
    # De tekst van het bestand is één lange string. Gebruik "split" om
    # de tekst op te delen in "woorden" begrensd door whitespace.
    #
    words = text.split()

    #
    # words is een lijst woorden, dus de lengte is het aantal woorden.
    #
    return len(words)


def vc(filename):
    """Vocabulary-counting function.

    Opens a file named 'filename', reads it, and breaks it into words.
    Then, for each word, counts how many times it occurs.
    Prints a message giving the number of distinct words in the file,
    and then returns a dictionary in which each word is a key and
    the word's frequency is the value.

    Example: vc('a.txt') might print 3 and return
    {'I': 2, 'love': 3, 'spam': 42}
    """
    f = open(filename, encoding="utf-8")
    text = f.read()
    f.close()

    words = text.split()
    print("Er zijn", len(words), "woorden.")

    d = {}
    for w in words:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1

    print("Er zijn", len(d), "*verschillende* woorden.\n")
    return d  # op deze manier kunnen we de gegevens in d later gebruiken!

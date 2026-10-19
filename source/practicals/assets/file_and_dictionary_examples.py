# Twee voorbeelden van hoe je tekst uit een bestand kan lezen en kan verwerken.

# om dit te laten werken moet je een bestand met de naam
#
# a.txt
#
# in dezelfde directory als dit .py-bestand maken!


def count_words(filename):
    """Telt de woorden in een bestand.

    Opent het bestand met de naam filename, leest het
    en geeft het aantal woorden in het bestand terug.

    Voorbeeld: count_words("a.txt") geeft 20
    """
    # Eerst moeten we het bestand "openen" (net als het openen van een boek
    # om dat te lezen). We vragen Python om de encoding "utf-8" te gebruiken,
    # omdat dat meer tekens dan ASCII accepteert.
    with open(filename, encoding="utf-8") as file:
        # Lees nu de hele inhoud van het bestand in een string met de naam
        # "text". Merk op dat dit alleen werkt voor relatief kleine
        # bestanden; grotere bestanden moet je regel voor regel lezen.
        text = file.read()

    # De tekst van het bestand is één lange string. Gebruik "split" om
    # de tekst op te delen in "woorden" begrensd door whitespace.
    words = text.split()

    # words is een lijst woorden, dus de lengte is het aantal woorden.
    return len(words)


def count_vocab(filename):
    """Telt hoe vaak elk woord in een bestand voorkomt.

    Opent het bestand met de naam filename, leest het en deelt het op in
    woorden. Telt daarna voor elk woord hoe vaak het voorkomt. Drukt het
    aantal woorden en het aantal verschillende woorden af, en geeft een
    dictionary terug met elk woord als sleutel en het aantal keer dat het
    voorkomt als waarde.

    Voorbeeld: count_vocab("a.txt") drukt 20 en 13 af en geeft
    {"Ik": 3, "wil": 2, "taarten": 2, "en": 3, ...}
    """
    with open(filename, encoding="utf-8") as file:
        text = file.read()

    words = text.split()
    print("Er zijn", len(words), "woorden.")

    vocab_count = {}
    for word in words:
        if word not in vocab_count:
            vocab_count[word] = 1
        else:
            vocab_count[word] += 1

    print("Er zijn", len(vocab_count), "*verschillende* woorden.\n")
    # op deze manier kunnen we de gegevens in vocab_count later gebruiken!
    return vocab_count

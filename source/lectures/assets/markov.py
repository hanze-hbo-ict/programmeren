import random


def create_dictionary(text):
    """Maakt een dictionary die bijhoudt welke woorden in text op welk woord volgen.

    In de dictionary words_follow die de functie teruggeeft, zijn de sleutels
    woorden. Elke waarde is een lijst met de woorden die in text op dat woord
    volgden. Een woord kan meer dan één keer in zo'n lijst staan.
    """
    words_follow = {}
    previous_word = "$"

    list_of_words = text.split()

    for next_word in list_of_words:
        if previous_word not in words_follow:
            words_follow[previous_word] = [next_word]
        else:
            words_follow[previous_word] += [next_word]

        previous_word = "$" if next_word[-1] in ".?!" else next_word

    return words_follow


def generate_text(words_follow, number_of_words):
    """Genereert een tekst van number_of_words woorden met de Markov-dictionary words_follow."""
    previous_word = "$"
    text = ""

    for _ in range(number_of_words):
        new_word = random.choice(words_follow[previous_word])
        text += new_word + " "

        if new_word[-1] in ".?!" or new_word not in words_follow:
            previous_word = "$"
        else:
            previous_word = new_word

    return text

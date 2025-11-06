import random


def create_dictionary(text):
    """Creates a dictionary based on the argument 'text', storing what
    words follow what.

    In the output dictionary 'words_follow', the keys are words, and
    each of the values is a list of strings of words that have followed
    that specific word in the provided text. This list of words can
    contain duplicates.
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
    """Generates a text of length 'number_of_words' based on the markov
    dictionary 'words_follow'.
    """

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

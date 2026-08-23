# Nederlandse stemmer op basis van het algoritme van de Snowball-stemmer.
# Algoritme: http://snowball.tartarus.org/algorithms/dutch/stemmer.html


def remove_accents(word):
    """Remove accented letters."""
    word = word.replace("ä", "a")
    word = word.replace("ë", "e")
    word = word.replace("ï", "i")
    word = word.replace("ö", "o")
    word = word.replace("ü", "u")
    word = word.replace("á", "a")
    word = word.replace("é", "e")
    word = word.replace("í", "i")
    word = word.replace("ó", "o")
    word = word.replace("ú", "u")
    return word


VOWELS = "aeoiuyè"


def replace_vowels(word):
    """Replace consonsant sounds represented by vowels with uppercase versions."""
    index = 0
    result = ""
    for char in word:
        if char == "y" and (index == 0 or word[index - 1] in VOWELS):
                result += "Y"
        elif char == "i" and index > 0 and word[index - 1] in VOWELS and \
                index < len(word) - 1 and word[index + 1] in VOWELS:
            result += "I"
        else:
            result += char
        index += 1
    return result


def valid_s_ending(word):
    """Check whether a word has a valid 's' ending."""
    return word[-1:] not in VOWELS + "j"


def valid_en_ending(word):
    """Check whether a word has a valid 'en' ending."""
    return word[-1:] not in VOWELS and word[-3:] != "gem"


def get_region(word):
    """Find a region which starts with the first non-vowel following a vowel."""
    last = word[0:1]
    offset = 1
    for char in word[1:]:
        offset += 1
        if last in VOWELS and char not in VOWELS:
            return offset
        last = char
    return len(word)


def regions(word):
    """Get two regions, one inside the other."""
    r1 = get_region(word)
    r2 = get_region(word[(r1):]) + r1
    r1 = max(r1, 3)
    return (r1, r2)


def undouble_ending(word):
    """Undouble k, d and t endings."""
    if word[-1:] == word[-2:-1] and word[-1:] in "kdt":
        word = word[:-1]
    return word


def step1(word, r1, r2):
    """Step 1: handle heden, ene, en, se and s suffixes."""
    if word[-5:] == "heden":
        if r1 <= len(word) - 5:
            word = word[:-5] + "heid"
    elif word[-3:] == "ene":
        if r1 <= len(word) - 3 and valid_en_ending(word[:-3]):
            word = word[:-3]
        word = undouble_ending(word)
    elif word[-2:] == "en":
        if r1 <= len(word) - 2 and valid_en_ending(word[:-2]):
            word = word[:-2]
        word = undouble_ending(word)
    elif word[-2:] == "se":
        if r1 <= len(word) - 2 and valid_s_ending(word[:-1]):
            word = word[:-2]
    elif word[-1:] == "s":
        if r1 <= len(word) - 1 and valid_s_ending(word[:-1]):
            word = word[:-1]
    return word


def step2(word, r1, r2):
    """Step 2: handle e suffix"""
    e_removed = False
    if word[-1:] == "e" and r1 <= len(word) - 1 and word[-2:-1] not in VOWELS:
        word = word[:-1]
        e_removed = True
    word = undouble_ending(word)
    return word, e_removed


def step3a(word, r1, r2):
    """Step 3a: handle heid suffix"""
    if word[-4:] == "heid" and r2 <= len(word) - 4 and word[-5:-4] != "c":
        word = word[:-4]
        if word[-2:] == "en":
            word = step1(word, r1, r2)
    return word


def step3b(word, r1, r2, e_removed):
    """Step 3b: handle end, ing, ig, lijk, baar and bar suffixes."""
    if word[-3:] == "end" or word[-3:] == "ing":
        if r2 <= len(word) - 3:
            word = word[:-3]
            if word[-2:] == "ig":
                if r2 <= len(word) - 2 and word[-3:-2] != "e":
                    word = word[:-2]
            else:
                word = undouble_ending(word)
    elif word[-2:] == "ig":
        if r2 <= len(word) - 2 and word[-3:-2] != "e":
            word = word[:-2]
    elif word[-4:] == "lijk":
        if r2 <= len(word) - 4:
            word = word[:-4]
            word, _ = step2(word, r1, r2)
    elif word[-4:] == "baar":
        if r2 <= len(word) - 4:
            word = word[:-4]
    elif word[-3:] == "bar":
        if r2 <= len(word) - 3 and e_removed:
            word = word[:-3]
    return word


def step4(word, r1, r2):
    """Step 4: Handle double vowel in last syllable."""
    if word[-4:-3] not in VOWELS and word[-3:-1] in ("aa", "ee", "oo", "uu") and word[-1:] not in VOWELS + "I":
        word = word[:-2] + word[-1:]
    return word


def create_stem(word):
    """Stem a Dutch word."""
    word = word.lower()
    word = remove_accents(word)
    word = replace_vowels(word)
    r1, r2 = regions(word)
    word = step1(word, r1, r2)
    word, e_removed = step2(word, r1, r2)
    word = step3a(word, r1, r2)
    word = step3b(word, r1, r2, e_removed)
    word = step4(word, r1, r2)
    word = word.lower()
    return word

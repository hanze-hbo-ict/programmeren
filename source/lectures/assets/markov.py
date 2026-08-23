import random


def create_dictionary(text):
    d = {}
    pw = "$"

    LoW = text.split()

    for nw in LoW:
        if pw not in d:
            d[pw] = [nw]
        else:
            d[pw] += [nw]

        pw = "$" if nw[-1] in ".?!" else nw

    return d


def generate_text(d, n):
    pw = "$"
    text = ""

    for i in range(n):
        nw = random.choice(d[pw])
        text += nw + " "

        if nw[-1] in ".?!" or nw not in d:
            pw = "$"
        else:
            pw = nw

    return text

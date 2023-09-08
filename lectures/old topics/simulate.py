import random


def unique(L):
    if len(L) == 0:
        return True
    elif L[0] in L[1:]:
        return False
    else:
        return unique(L[1:])


def until_a_repeat(high):
    L = []
    count = 0

    while unique(L):
        value = random.choice(range(0, high))
        L.append(value)
        count += 1

    return count


def throw_dart():
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    return x ** 2 + y ** 2 <= 1.0


def for_pi(n):
    in_circle = 0
    pi = 0.0
    for i in range(n):
        if throw_dart():
            in_circle += 1
        pi = in_circle / (i + 1) * 4.0
    return pi

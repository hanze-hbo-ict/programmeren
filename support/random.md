---
title: "Voorbeelden van random"
description: "Voorbeelden van random"
---

# Voorbeeld van `random`

## Raad het getal

Een variatie op het gebruik van `random`, raad het getal. Dit voorbeeld maakt gebruik van *recursie*.

```python
import sys
import time
from random import *

sys.setrecursionlimit(50000)  # extra ruimte voor recursie


def guess(hidden):
    """A number-guessing example
       to highlight using the
       random library
    """

    comp_guess = choice(range(100))  # 0 tot en met 99.

    if comp_guess == hidden:
        print("Ik heb het goed! Het was", comp_guess)
        print("Aantal pogingen:")
        return 1

    else:
        print("Aargh. Ik raadde", comp_guess)
        time.sleep(0.1)
        return 1 + guess(hidden)
```

Een mogelijke uitvoer:

```ipython3
In [1]: guess(42)
Aargh. Ik raadde 25
Aargh. Ik raadde 49
Aargh. Ik raadde 79
Aargh. Ik raadde 34
Aargh. Ik raadde 26
Aargh. Ik raadde 74
Aargh. Ik raadde 38
Aargh. Ik raadde 17
Aargh. Ik raadde 86
Aargh. Ik raadde 47
Aargh. Ik raadde 77
Aargh. Ik raadde 8
Aargh. Ik raadde 71
Aargh. Ik raadde 36
Aargh. Ik raadde 39
Aargh. Ik raadde 4
Aargh. Ik raadde 11
Aargh. Ik raadde 6
Aargh. Ik raadde 77
Ik heb het goed! Het was 42
Aantal pogingen:
20
```
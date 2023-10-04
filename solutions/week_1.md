# Oplossingen week 1

## Instap

### [Logische puzzles](/problems/instap/1_logic_riddles)

...

### [Picobot](/problems/instap/1_logic_riddles)

```text
0 *x** -> E 0
0 *E** -> N 1

1 x*** -> N 1
1 N*** -> W 2

2 **x* -> W 2
2 **W* -> S 3

3 ***x -> S 3
3 ***S -> E 4

4 *x** -> E 4
4 *E** -> N 1
```

## Basis

...

## Context

<!-- NB deze opgave komt uit week twee, maar hier als voorbeeld opgenomen :) -->

### [Rochambeau](/problems/context/2_rochambeau)

Twee mogelijke oplossingen (maar andere variaties zijn mogelijk!)

```python
from random import choice

user = input("Jouw keus? ")
comp = choice(["steen", "papier", "schaar"])

print("Jouw keus is:", user)
print("Mijn keus is:", comp)

if comp == user:
    print("Gelijkspel ...")
elif comp == "steen" and user == "schaar":
    print("Ik win!")
elif comp == "papier" and user == "steen":
    print("Ik win!")
elif comp == "schaar" and user == "papier":
    print("Ik win!")
else:
    print("Jij wint...")
```

```{notice}
We gebruiken hier `and` wat betekent dat beide expressies waar (`True`) moeten zijn.
```

Of een oplossing met alleen maar `if` en `else`

```python
from random import choice

user = input("Jouw keus? ")
comp = choice(["steen", "papier", "schaar"])

print("Jouw keus is:", user)
print("Mijn keus is:", comp)

if comp == user:
    print("Gelijkspel")
else:
    if comp == "steen":
        if user == "schaar":
            print("Ik win!")
        else:
            print("Jij wint...")
    else:
        if comp == "papier":
            if user == "steen":
                print("Ik win!")
            else:
                print("Jij wint...")
        else:
            if comp == "schaar":
                if user == "papier":
                    print("Ik win!")
                else:
                    print("Jij wint...")

            # "schaar" is de laatste optie,
            # er is geen else meer mogelijk
```
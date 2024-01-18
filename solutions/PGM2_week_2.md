# Oplossingen PGM2 week 2

## Basis

### [Lussen in PythonBat!](/problems/basis/9_python_bat)

#### Opdracht

Deze opdrachten worden in CodingBat gemaakt en deze controleert de code gelijk. Voor vragen over deze opdracht kun je bij de docent terecht.


## Context

### [Pi met pijltjes](/problems/context/9_pi_pijlen)

#### Opdracht

Het is misschien verbazingwekkend dat het mogelijk is om de wiskundige constante π te berekenen zonder dat je andere operaties nodig hebt dan tellen, optellen en vermenigvuldigen. In deze opgave ga je twee functies schrijven om pi (3.14159...) te benaderen door het gooien van pijltjes.

```python
import random
import math

def throw_dart():
    """ Deze functie maakt gebruik van de random library om een 
    willekeurige x- en een willekeurige y-coördinaat te genereren 
    tussen -1 en 1. Als de pijl de cirkel raakt geeft de functie 
    True terug anders False.
    """

    x = random.uniform(-1.0,1.0)
    y = random.uniform(-1.0,1.0)

    distance = math.sqrt((x * x) + (y * y))
    if distance <= 1.0: # Raakt de cirkel
        return True
    
    return False

def for_pi(n):
    """ Deze functie gooit n pijltjes om de constante pi te benaderen. 
    De geschatte waarde pi wordt door de functie terug gegeven.
    """

    timesHit = 0.0

    for dart in range(1, n+1): # Corrigeer voor range beginnen bij 0
        hit = throw_dart()
        if hit:
            timesHit += 1.0
        
        print(str(timesHit) + " raak van de " + str(dart) + " worpen dus pi is " + str((4.0*timesHit)/dart))

    return ((4.0*timesHit)/n)

# print("Laatste schattig for pi is " + str(for_pi(500)))
# Mocht je tijd hebben en een pc die dit wel aan kan:
# print("Laatste schatting for pi is " + str(for_pi(5000000)))

def find_number_of_decimals(x):
    """ Geeft het aantal cijfers achter de komma voor float x (gegeven als string!) als integer terug.
    """
    if len(x) == 0:
        return 0
    if x[-1] == '.':
        return 0
    else:
        return 1 + find_number_of_decimals(x[0:-1])
    
assert find_number_of_decimals(str(3.12345)) == 5
assert find_number_of_decimals(str(456.98756429)) == 8
assert find_number_of_decimals(str(0.1)) == 1

def while_pi(accuracy):
    """ Geeft het aantal pijltjes terug dat nodig was om nauwkeurigheid 
    x te halen.
    """
    # Omdat de schatting van pi veel meer decimalen geeft dan de mee gegeven nauwkeurigheid
    # en dit problemen geeft met een is gelijk aan statement, zullen we gebruik maken van de
    # round functie. Hiervoor houden we het aantal decimalen aan van de mee gegeven variable en
    # gebruiken we een hulp functie.
    # Maak van de float een een str om gebruik te kunnen maken van string slicing om het aantal decimalen te krijgen
    decimal = find_number_of_decimals(str(accuracy)) 
    #print("Number of decimals: " + str(decimal))
    timesHit = 0.0
    dart = 0
    correct_accuracy = True

    while correct_accuracy:
        hit = throw_dart()
        if hit:
            timesHit += 1.0
        dart += 1 # We hebben nu de eerste pijl gegooit
        guess_pi = (4.0*timesHit)/dart

        # Beperk aantal prints bij meer decimalen voor leesbaarheid output
        if decimal <= 2:
            # print("(Hit? " + str(hit) + ")\t" + str(timesHit) + " raak van de " + str(dart) + " worpen dus pi is " + str(guess_pi))
            print(str(timesHit) + " raak van de " + str(dart) + " worpen dus pi is " + str(guess_pi))
        else:
            if dart % 100 == 0:
                print(str(timesHit) + " raak van de " + str(dart) + " worpen dus pi is " + str(guess_pi))

        if round(guess_pi, decimal) == round(3.0 + accuracy, decimal):
            correct_accuracy = False

    if decimal > 2:
        print(str(timesHit) + " raak van de " + str(dart) + " worpen dus pi is " + str(guess_pi))
    return dart

```
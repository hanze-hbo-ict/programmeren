# Oplossingen PGM2 week 4

## Basis

### [ASCII Art](/problems/basis/11_ASCII)

Belangrijke beperking bij deze opdrachten: 
In deze opgave mag je de string-vermenigvuldig- en string-opteloperatoren niet gebruiken. Omdat ons doel is om lusconstructies te gebruiken, moet je lussen gebruiken om te herhalen, ook als het met deze operatoren korter zou kunnen. Hier is één uitzondering op, echter; je mag string-vermenigvuldiging gebruiken met het spatieteken

#### Opdracht 1 

Schrijf een functie met de naam print_rect die drie argumenten meekrijgt, width, height en symbol, en een vierkant van width bij height met symbolen afdrukt op het scherm.

```python
def print_rect(width, height, symbol):
    """ Drukt een vierkant van symbol af op het scherm van width bij height.
    """
    
    for row in range(height):
        for column in range(width):
            print(symbol, end=" ")
        print()
```

Om makkelijker bij te houden welke lus de rijen en welke de kolommen, wordt hier row en column als variable namen gebruikt in plaats van i en j.


#### Opdracht 2

Schrijf een functie print_triangle die drie argumenten meekrijgt: width, symbol en right_side_up, en een driehoek van symbolen op het scherm afdrukt.

```python
def print_triangle(width, symbol, right_side_up):
    """ Drukt een driehoek van symbol af op het scherm met breedte van 
    width en right_side_up bepaalt of de punt naar boven (True) of naar
    beneden (False) moet.
    """
    for i in range(0, width):
        if right_side_up : # Punt naar boven!
            for j in range(0, i + 1):
                print(symbol, end = " ")
        else:
            for j in range(0, width - i):
                print(symbol, end = " ")
        print()
```

Bij een punt naar boven bevat de eerste regel 1 symbool en hebben de volgende regels elke keer 1 symbool meer. Dit kun je ook zien als regel nummer staat gelijk aan het aantal symbolen dat naar het scherm geprint moet worden. Hier wordt gebruik van gemaakt door de range in de eerste j-for-lus (de kolom lus) af te laten hangen van i + 1. De + 1 is om te corrigeren dat de range van i begint bij nul.

Bij de punt naar beneden werken we van breed naar smal, van het maximale aantal terug naar 1 symbool. Daarom wordt in het else gedeelte met width - i gewerkt in de range van de for-lus. Hier corrigeren we de range nul van i niet omdat elke regel dan juist een symbool te weinig heeft.


#### Opdracht 3

Gebruik nu je functie print_triangle om een functie genaamd print_bumps(num, symbol1, symbol2) te schrijven die het gegeven aantal “heuvels” van twee symbolen afdrukt, waarbij elke heuvel groter is dan de volgende.

```python
def print_bumps(num, symbol1, symbol2):
    """ Deze functie drukt het gegeven aantal “heuvels” van twee symbolen 
    af, waarbij elke heuvel groter is dan de volgende.
    """
    for bumps in range(1, num + 1):
        print_triangle(bumps, symbol1, True)
        print_triangle(bumps, symbol2, False)
```

Het aantal "heuvels" neemt elke keer met 1 toe. Hier kunnen we de for-lus variable voor gebruiken.


#### Opdracht 4

Schrijf een functie print_diamond(width, symbol) die een ruit met symbolen afdrukt waarvan de maximale breedte bepaald wordt door width. Voor deze “ruit”-functies mag je string-vermenigvuldiging gebruiken, maar alleen voor strings van spaties.

```python
def print_diamond(width, symbol):
    """ Drukt een ruit af gemaakt met symbol en maximale breedte width.
    """
    # Het bovenste deel van de diamond
    for i in range(1, width + 1):
        print(" " * (width - i), end = "")
        for j in range(0, i ):
            print (symbol, end = " ")
        print()
    # Het onderste deel van de diamond
    for i in range(1, width):
        print(" " * (i), end = "")
        for j in range(0, width - i ):
            print (symbol, end = " ")
        print()
```

Net als bij de print_triangle functie maken we hier gebruik van op welke regel (i) we zitten en of we van een laag aantal symbolen naar hoog gaan (bovenste deel van de ruit) of juist de andere kant op (het onderste deel van de ruit). In dit geval beginnen we alle ranges met 1 om zo de juiste aantal spaties voor het eerste symbool te krijgen.

Als je moeite hebt met het visualiseren van de opdracht dan kun je proberen om de ruit eerst uit te tekenen op ruitjes papier. Omdat we na het symbool spatie printen wordt de breedte van het symbool veld (width * 2) - 1. Variable i is de rij en variable j is de kolom.


#### Opdracht 5

Schrijf nu een functie genaamd print_striped_diamond(width, sym1, sym2) die een “gestreepte ruit” van sym1 en sym2 afdrukt.

```python
def print_striped_diamond(width, symbol1, symbol2):
    """ Drukt een ruit gemaakt met symbol1 afgewisseld met symbol2 af met maximale breedte width.
    """
    for i in range(1, width + 1):
        print(" " * (width - i), end = "")
        for j in range(0, i):
            if j % 2 == 1:
                print (symbol1, end = " ")
            else:
                print (symbol2, end = " ")
        print()
    for i in range(1, width):
        print(" " * (i), end = "")
        for j in range(0, width - i):
            if i % 2 == 1:
                if j % 2 == 0:
                    print (symbol1, end = " ")
                else:
                    print (symbol2, end = " ")
            else:
                if j % 2 == 1:
                    print (symbol1, end = " ")
                else:
                    print (symbol2, end = " ")
        print()
```

Deze functie is hetzelfde als print_diamond, maar met toevoeging van de if-statement met de modulo operator en de rij (i) en kolom (j) variablen om te bepalen welk van de twee symbolen geprint moet worden.


#### Opdracht 6

Schrijf een functie genaamd print_crazy_striped_diamond(width, sym1, sym2, sym1_width, sym2_width) die een “gestreepte ruit” van sym1 en sym2 afdrukt waarbij de strepen verschillende breedtes kunnen hebben

```python
def print_crazy_striped_diamond(width, sym1, sym2, sym1_width, sym2_width):
    for i in range(1, width+1):
        print(" " * (width - i), end = "")
        sym1Count = 0
        sym2Count = 0
        for j in range(0, i ):
            if sym1Count < sym1_width:
                print (sym1, end = " ")
                sym1Count += 1
                if sym1Count >= sym1_width:
                    sym2Count = 0
            else:
                print (sym2, end = " ")
                sym2Count += 1
                if sym2Count >= sym2_width:
                    sym1Count = 0

        print()
    for i in range(1, width):
        print(" " * (i), end = "")
        sym1Count = i % (sym1_width + sym2_width)
        sym2Count = 0
        if sym1Count >= sym1_width:
            sym2Count = sym1Count - sym1_width
        for j in range(0, width - i ):
            if sym1Count < sym1_width:
                print (sym1, end = " ")
                sym1Count += 1
                if sym1Count >= sym1_width:
                    sym2Count = 0
            else:
                print (sym2, end = " ")
                sym2Count += 1
                if sym2Count >= sym2_width:
                    sym1Count = 0
        print()
```

Let goed op wanneer je de variablen aanmaakt in de for-lussen. Wanneer zijn ze nodig en wanneer hoeven ze niet meer te bestaan?


## Context

### [Mandelbrot](/problems/context/11_mandelbrot)

Tijdens deze opdracht ga je een programma schrijven om de punten in en rond de mandelbrotverzameling weer te geven en te verkennen.

```python
# laat deze importregel staan...
from png import *

#
# een testfunctie...
#
def test_fun():
    """ algorithmic image-creation one pixel at a time...
        this is a test function: it should output
        an image named test.png in the same directory
    """
    im = PNGImage(300, 200)  # maak een afbeelding met width=300, height = 200

    # Geneste lussen!
    for r in range(200):  # lust over de rijen met lusvariabele r
        for c in range(300):  # lust over de kolommen met c
            if c == r:
                im.plot_point(c, r, (255, 0, 0))
            # else:
            #    im.plot_point( c, r, (255,0,0))

    im.save_file()

#
# zet je functies hieronder neer:
#

def mult(c, n):
    """Mult uses only a loop and addition
       to multiply c by the positive integer n
    """
    result = 0
    for i in range(n):
        result += c
    return result

assert mult(3, 5) == 15
assert mult(6, 7) == 42
assert mult(1.5, 28) == 42.0

def update(c, n):
    """Update starts with z = 0 and runs z = z**2 + c
       for a total of n times. It returns the final z.
    """
    z = 0
    for i in range(n):
        z = z ** 2 + c
    return z

assert update(1, 3) == 5
assert update(-1, 3) == -1
assert update(-1, 10) == 0

def in_mset(c, n):
    """in_mset accepts

    c for the update step of z = z**2+c
    n, the maximum number of times to run that step

    Then, it returns

    False as soon as abs(z) gets larger than 2
    True if abs(z) never gets larger than 2 (for n iterations)
    """
    z = 0
    for i in range(n):
        z = z ** 2 + c
        if abs(z) > 2:
            return False
    #return z
    return True

c = 0 + 0j
assert in_mset(c, 25) == True
c = 3 + 4j
assert in_mset(c, 25) == False
c = 0.3 + -0.5j
assert in_mset(c, 25) == True
c = -0.7 + 0.3j
assert in_mset(c, 25) == False
c = 0.42 + 0.2j
assert in_mset(c, 25) == True
assert in_mset(c, 50) == False


def we_want_this_pixel(col, row):
    """This function returns True if we want to show
       the pixel at col, row and False otherwise.
    """
    if col % 10 == 0 and row % 10 == 0:
    # if col % 10 == 0 or row % 10 == 0:
        return True
    else:
        return False
    
def test():
    """This function demonstrates how
       to create and save a PNG image.
    """
    width = 300
    height = 200
    image = PNGImage(width, height)

    # maak een lus om wat pixels te tekenen

    for col in range(width):
        for row in range(height):
            if we_want_this_pixel(col, row):
                image.plot_point(col, row)

    # we hebben door alle pixels gelust; nu schrijven we het bestand

    image.save_file()

# test()


def scale(pix, pix_max, float_min, float_max):
    """scale accepts

    pix, the CURRENT pixel column (or row)
    pix_max, the total # of pixel columns
    float_min, the min floating-point value
    float_max, the max floating-point value
    scale returns the floating-point value
        that corresponds to pix
    """

    return float_min + (pix/pix_max * (float_max-float_min))

assert scale(100, 200, -2.0, 1.0) == -0.5
assert scale(100, 200, -1.5, 1.5) == 0.0
assert scale(100, 300, -2.0, 1.0) == -1.0
assert scale(25, 300, -2.0, 1.0) == -1.75
# print(scale(299, 300, -2.0, 1.0)) # == 0.99

def mset():
    """Creates a 300x200 image of the Mandelbrot set
    """
    NUM_ITER = 50  # aantal updates
    XMIN = -2.0   # de kleinste waarde voor de reële coördinaat
    XMAX = 1.0    # de grootste waarde voor de reële coördinaat
    YMIN = -1.0  # de kleinste waarde voor de imaginaire coördinaat
    YMAX = 1.0   # de grootste waarde voor de imaginaire coördinaat
    
    width = 300
    height = 200
    image = PNGImage(width, height)

    # maak een lus om wat pixels te tekenen

    for col in range(width):
        for row in range(height):
            # Gebruik scale twee keer:
            #   één keer om het reële deel van c te bepalen (x)
            x = scale(col, width, XMIN, XMAX)
            #   één keer om het imaginaire deel van c te bepalen (y)
            y = scale(row, height, YMIN, YMAX)
            # DAARNA ken je c toe, kies je n en test je:
            c = x + y*1j
            #n = 25
            if in_mset(c, NUM_ITER ):
                image.plot_point(col, row, (255, 175, 0) )
            else:
                image.plot_point(col, row, (0, 0, 0))

    # we hebben door alle pixels gelust; nu schrijven we het bestand
    image.save_file()

# mset()
```
# Basis

## Formules en Vars
Leerdoel: Berekening maken met variabelen

### Opdracht 1

**1a.**
Een klusjesman, Handige Harry, rekent een start/voorrijtarief van 60 Euro en per uur een tarief van 40 Euro. Schrijf een programma dat de volgende stappen doet:

1. Vraagt de gebruiker om input, dit omzet tot een integer en het resultaat opslaat in aan variable genaamd `uren`. 
2. Een bereking uitvoert om uit te rekenen hoeveel geld Harry krijgt en het resultaat opslaat in een variabele genaamd `rekening`
3. Print het resultaat uit. 

**1b.** 
Harry heeft een aanbieding lopen, namelijk dat als de klant meer dan 400 euro kwijt is, dan krijgt de klant 10% korting. Pas het programma bij a zo aan dat het ook de korting wordt meerekent, als de klant daar recht op heeft. 

### Opdracht 2
Tentamencijfers worden vaak berekend aan de hand van een formule:

punten/max_punten * 9 + 1 = cijfer

Schrijf een programma dat de gebruiker 2 keer om input vraagt; namelijk hoeveel punten er is gehaald voor de toets en hoeveel punten er maximaal te halen is. Vervolgens berekend het programma het cijfer en print dat uit. 

### Opdracht 3

**3a**
Schrijf een programma dat de gebruiker 2 keer om input vraagt;namelijk wat de temperatuur is en of dat in fahrenheit is of in Celsius. Als het in fahrenheit is rekent het programma uit wat dat in Celsius is en andersom. De formule om van Celsius naar Fahrenheit te komen is $ (Celsius×95)+32 = Fahrenheit $

**3b**
Naast Fahrenheit en Celsius is er ook Kelvin. De formule van Kelvin is $ Celsius + 237.15 = Kelvin $ . Pas het programma bij a zo aan dat als de gebruiker aangeeft dat de temperatuur in Kelvin is dat het programma de temperatuur in Celsius en in Fahrenheit uitprint. Als het Celsius is ,dan print het programma Kelvin en Fahrenheit uit. Als het fahrenheit is, dan print het programma Celsius en Kelvin uit. 


Temp?: 20   
Schaal?: Celsius  
Fahrenheit = 68  
Kelvin = 239.15  

Temp?: 20  
Schaal?: Fahrenheit  
Celsius = -6.67  
Kelvin = 266.48  


## Interactieve fictie
Leerdoel: Programma schrijven met conditionele statements

In deze opgave ga je interactieve fictie in Python schrijven, en met *interactieve* fictie bedoelen we een *kies-je-eigen-avontuur* programma!

### Een begin

```python
"""
Titel voor je avontuur: De queeste naar taart.

Opmerkingen over hoe je het avontuuur kan "winnen" of "verliezen":
* kies de tafel om te winnen
* kies de deur om te verliezen
"""

import time


def adventure():
    """Runs one session of interactive fiction

    Well, it's "fiction," depending on the pill color chosen...

    arguments: no arguments (prompted text doesn't count as an argument)
    results: no results     (printing doesn't count as a result)
    """
    # change to 0.0 for testing or speed runs,
    # ... or larger for dramatic effect!
    delay = 0.0

    username = input("Hoe noemt men u, edele avonturier? ")

    print()
    print("Welkom,", username, "in het Libracomplex, een labyrint")
    print("van gewichtige wonderen en grote hoeveelheden ... taart!")
    print()
    print("Uw queeste: om een taart te vinden, en te eten!")
    print()

    flavor = input("Welke smaak zoekt u? ")
    if flavor == "aardbeien":
        print("Uw wijsheid in taartkeuze is overweldigend!")
    elif flavor == "kersen":
        print("Een Limburgse klassieker: een goede keuze, avonturier!")
    else:
        print("Ieder zijn smaak...")

    print()
    print("Voorwaarts naar de queeste!\n\n")
    print("Een gang strekt zich voor u uit; in het gedimde licht ziet u")
    print("aan de ene kant een tafel met onduidelijke vormen en")
    print("materialen, en aan de andere kant een deur op een kier,")
    print("waarachter gelach --is dat gelach?-- van studenten klinkt.")

    time.sleep(delay)

    print()
    choice1 = input("Kiest u de tafel of de deur? [tafel/deur] ")
    print()

    if choice1 == "tafel":
        print("Als u de tafel benadert lijkt de onduidelijke massa")
        print("een steeds grotere vorm aan te nemen, tot ...")

        time.sleep(delay)

        print("... ze herkenbaar wordt als een grote stapel verpakte")
        print("taarten, het karton strak geplooid. Uw uitdaging --en")
        print("honger-- is op smakelijke wijze opgelost.")
        print()
        print("Tot ziens,", username, "!")
    else:
        print("U opent de deur en ziet een congregatie van wijze dames")
        print("en heren, die allen genieten van hun taken. Samenwerking")
        print("en vrolijkheid zijn hier in overvloed aanwezig, maar...")

        time.sleep(delay)

        print("...ze hebben ALLE taart opgegeten! Resten van dozen")
        print("liggen overal verspreid. U wordt duizelig en grijpt")
        print("naar een taart. Er is niets. U ademt uit en valt,")
        print("en ligt verslagen tussen de resten van dozen die u")
        print("langzaam bedekken tot verstikking volgt.")
        print()
        print("Vaarwel,", username, ".")
```

:::{admonition} Nieuwe regel
:class: info

Het zal je opvallen dat `print()` (ongeacht het argument, bijvoorbeeld jouw tekst) altijd een nieuwe regel start. Dit gebeurt omdat standaard de karaktercombinatie `'\n'` aan de uitvoer wordt toevoegd. `'\n'` staat voor "newline" (nieuwe regel) en kent zelfs een hele [geschiedenis](https://en.wikipedia.org/wiki/Newline) (inclusief de oudewetse typemachine, en het wordt zeker niet alleen in Python gebruikt!).

Kan je in het voorbeeldverhaal het gebruik van `'\n'` ontdekken, en zou je dit misschien straks in jouw verhaal op een slimme manier kunnen gebruiken?
:::

### Opdracht

Je mag het taartverhaal gaan aanpassen en uitbreiden, of een geheel eigen interactief-fictieverhaal schrijven! Werk met iemand samen als je wilt (dit is optioneel) en maak je eigen avontuur.

Het bovenstaande verhaal bevat al twee controlestructuren met `if`:

1. een `if`-`elif`-`else`, en
2. een `if`-`else`.

De eis voor deze opdracht is dat je *elk* van de onderstaande vijf controlestructuren ("conditional statements") gebruikt, zodanig dat ze de richting van het verhaal beïnvloeden:

- een controlestructuur met `if`, precies één `elif` en `else`
- een controlestructuur met `if`, minstens twee `elif`'s en `else`
- een controlestructuur met `if` en `else` (en geen `elif`)
- een controlestructuur met `if` en minstens één `elif` (en geen `else`)
- een controlestructuur met `if` (en geen `elif` of `else`)

Verder geldt het volgende:

- de controlestructuren hoeven niet in de genoemde volgorde te worden toegepast
- je mag meer dan 5 controlestructuren gebruiken (als je wilt!)

:::{admonition} De kunst van de eenvoud
:class: notice

Houd het alsjeblieft eenvoudig! Andere fora of cursussen zijn beter geschikt voor vormen van creatieve expressie, hier gaat het ons voornamelijk om het verkennen van condities bij programmeren. Houd ook in gedachten dat mogelijk veel mensen jouw verhaal zullen lezen, uitvoeren en beoordelen (we kijken er naar uit!).

Wees verder ook bewust van de tijd die je aan deze opdracht besteedt, het is gemakkelijk om de tijd te verliezen. Het schrijven van het taartavontuur duurde ons al veel langer dan we oorspronkelijk hadden gedacht en het telt slechts *twee* controlestructuren!
:::

Veel plezier met avonturieren!
# Week 2

## Basis

### [Interactieve fictie](/problems/basis/2_interactieve_fictie)

Dit is een van de vele mogelijke manieren om deze opdracht te maken.

```python
import time

# change to 0.0 for testing or speed runs,
# ... or larger for dramatic effect!
delay = 4.0

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
elif flavor == "appel":
    print("De oude goude die in elke situatie past, kruimelig of volgens grootmoeders recept!")
elif flavor == "slagroom":
    print("Romige met een variatie aan fruit voor hen die niet kunnen kiezen!")
elif flavor == "mokka":
    print("Een goed alternatief voor hen die niet van fruit houden!")
elif flavor == "chocolade":
    print("Bewaart u een stukje voor mij?")
else:
    print("Ieder zijn smaak...")
time.sleep(delay)
```

Er zijn zoveel meer smaken dan eerder genoemd.
Dit is daarom een makkelijke plek om meerdere elif statements toe te voegen en
zo te voldoen aan de tweede eis in de opdracht (if, minstens twee elif's en else).


```python
print()
print("Voorwaarts naar de queeste!\n")
time.sleep(delay)
print("U volgt de gang waar u begint en komt bij een kruispunt.\n")
time.sleep(delay)
# Drie opties is ideaal voor een if, elif, else constructie
# Optie 1: de linker gang
print("De gang naar links verandert snel in een donker gat.")
print("Een van de muren in deze gang lijkt een knop te hebben.\n")
time.sleep(delay)

# Optie 2: de rechter gang
print("De gang naar rechts is dim verlicht, maakt een bocht")
print("naar links en ruikt naar verse broodjes.\n")
time.sleep(delay)

# Optie 3: rechtdoor
print("De goed verlichte gang rechtdoor leidt naar een gesloten deur.\n")

time.sleep(delay)
print()
```

```{note}
Door slim gebruik te maken van `time.sleep(delay)` kun je voorkomen dat het scherm overspoeld wordt met tekst.
Dit geeft de gebruiker/speler tijd om te lezen.
```

```python
choice1 = input("Weerstaat u de verleiding om op de knop in de linker gang te drukken? [ja/nee] ")
# Twee opties en alleen een optie heeft een effect is ideaal voor een enkele if constructie
print()
if(choice1 == "nee"):
    print()
    print("Uw nieuwsgierigheid wint en u slaat op de knop.")
    print("Aan het einde van de linker gang springt een licht aan.")
    print("Een deur verschool zich in het donker.\n")
    time.sleep(delay)
```

Door een gebeurtenis in te bouwen die alleen plaats vindt als de gebruiker/speler iets wel of niet doet,
kunnen we nu een enkele if statement toepassen om aan de laatste eis te voldoen (alleen een if).


```python
print()
choice2 = input("Welke kant gaat u op? [links/rechts/rechtdoor] ")
if(choice2 == "links"):
    if(choice1 == "ja"): # Er is niet op de knop gedrukt dus het is nog steeds donker!
        print()
        print("U loopt het donker van de gang tegemoet.")
        print("Na een paar passen in het donker botst u")
        print("tegen een deur die met luid kabaal gelijk open schiet.")
        print("U stapt in het duister de deur door, maar er")
        print("is geen vloer onder uw voeten. U valt en valt.\n")
    else: # Het licht brandt
        print()
        print("U loopt naar de dichte deur.")
        print("Zodra u de klink aanraakt, schiet de deur")
        print("met veel kracht en lawaai open. Het licht laat een")
        print("vloerloze ruimte zien. U draait zich om om terug")
        print("te lopen, maar een onzichtbare muur houdt u tegen.")
        print("De enige weg vooruit is naar beneden, een sprong in het duister.")
        print("U springt en valt en valt. Het licht is niet meer te zien.\n")

    time.sleep(delay)
    time.sleep(delay)
    print("Met een plons valt u in een door maanlicht")
    print("verlichte vijver niet ver van uw huis.")
    print("Helaas geen taart voor u, ", username, ".")
    print("Snel naar huis voor droge kleding!\n")
```

We hebben hier de gebruiker/speler drie opties gegeven.
Met een if-elif-else constructie kunnen we bepalen welke keuze er gemaakt is en
voldoen aan de eerste eis (if, precies één elif en else).
Hier zien we dat er voor gekozen is om if te gebruiken voor de keuze links.
Of de gebruiker/speler wel of niet op de knop heeft gedrukt, heeft effect op het verhaal.
Daarom wordt met een nested if-else gekeken welke versie van het verhaal verteld

```python
elif(choice2 == "rechts"):
    print()
    print("U besluit uw neus te volgen en loopt de rechter gang in.")
    print("Als er vers gebakken broodjes zijn dan zal er ook taart zijn toch?\n")
    time.sleep(delay+2.0)
    print("U gaat de bocht om en nog een bocht en nog een bocht.")
    print("Uw gevoel voor richting is compleet verdwenen, maar de geur,")
    print("de geur van heerlijke verse broodjes wordt wel sterker.\n")
    time.sleep(delay+2.0)
    print("Eindelijk komt u bij een ruimte vol met ovens, werkbanken en")
    print("voorraadkasten vol met ingredienten. Behekste rollers, deegmixers")
    print("en andere keukengereedschap zijn druk in de weer met het maken van")
    print("de meest luxe broodjes die u maar kunt verzinnen. Het water loopt")
    print("u in de mond, maar er is geen taart inzicht.\n")
    time.sleep(delay)

    choice3 = input("Gaat u opzoek naar taart of is een vers broodje ook goed? [taart/brood] ")
    if(choice3 == "taart"):
        print()
        print("Verwoed gaat u opzoek naar taart. Zoveel broodjes en geen taart?")
        print("Dat kan toch niet! U trekt kastje na kastje open.")
        print("Kruiden, vers en gedroogd, alle soorten bloem,")
        print("taartvullingen en andere bakbenodigdheden komt u tegen.")
        print("Maar geen taart. Als de laatste deur open trekt, wordt alles zwart.\n")
        time.sleep(delay+3.0)
        print("U knippert een paar keer met uw ogen en beseft")
        print("dat u in uw eigen keuken staat. Alle kastjes")
        print("staan open en het is een puinhoop. Bloem overal,")
        print("ook op u. Een brandlucht komt uit de oven.\n")
        time.sleep(delay+3.0)
        print("Snel doet u de oven open om een zwart geblakerde")
        print("taart te zien. Blijkbaar probeerde u zelf een ")
        print(flavor, "taart te maken. Helaas bent u in een")
        print("dagdroom belandt en is er geen taart voor u.\n")
    elif(choice3 == "brood"):
        print()
        print("Al snel ziet u waar de verse broodjes ingepakt worden.")
        print("Het duurt niet lang voor u een zakje vindt met een assortiment")
        print("waar u blij van wordt. Met een te vrede gevoel loopt u naar")
        print("de deur met uitgang. Zodra u door de deur stapt,")
        print("stapt u uw eigen keuken in. Hier staat al een glas van uw")
        print("favoriete drankje met de juiste temperatuur klaar en een")
        print("bordje. Geen taart voor u, maar wel heerlijk vers brood.\n")

else:
    print()
    print("U loopt naar de deur recht voor u en opent hem.")
    print("Een kamer strekt zich voor u uit; in het gedimde licht ziet u")
    print("aan de ene kant een tafel met onduidelijke vormen en")
    print("materialen, en aan de andere kant een deur op een kier,")
    print("waarachter gelach --is dat gelach?-- van studenten klinkt.")
    time.sleep(delay)

    print()
    choice4 = input("Kiest u de tafel of de deur? [tafel/deur] ")
    print()

    if choice4 == "tafel":
        print("Als u de tafel benadert lijkt de onduidelijke massa")
        print("een steeds grotere vorm aan te nemen, tot ...")

        time.sleep(delay)

        print("... ze herkenbaar wordt als een grote stapel verpakte")
        print("taarten, het karton strak geplooid. Uw uitdaging --en")
        print("honger-- is op smakelijke wijze opgelost.")
        print()
        print("Tot ziens,", username, "!\n")
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
        print("Vaarwel,", username, ".\n")
```

### [Sequenties en data](/problems/basis/2_sequenties_en_data)

Goed om te onthouden: string[start:stop:stapgrootte]

#### Opdracht 1

Gebruik pi en e (of maar één, je mag voor alle verdere problemen ook maar één lijst gebruiken) om de lijst [7, 1] te maken. Bewaar de lijst, net als hierboven, in de variabele answer1.

```python
# De lists om mee te werken
e = [2, 7, 1]
pi = [3, 1, 4, 1, 5, 9]

answer0 = e[0:2] + pi[-2:]
print()
print("Voorbeeld antwoord is", answer0)

# Opgave 1: maak [7, 1]
answer1 = e[1:3]
print("Antwoord 1 is", answer1)
assert answer1 == [7, 1], "answer1 moet [7, 1] zijn."
```


#### Opdracht 2

Gebruik pi en e om de lijst [1, 1, 2] te maken. Bewaar deze lijst in de variabele answer2.

```python
# Opgave 2: maak [1, 1, 2]
answer2 = pi[1:4:2] + e[0:1]
print("Antwoord 2 is", answer2)
assert answer2 == [1, 1, 2], "answer2 moet [1, 1, 2] zijn."
```


#### Opdracht 3

Gebruik pi en e om de lijst [1, 4, 1, 5, 9] te maken. Bewaar deze lijst in de variabele answer3.

```python
# Opgave 3: maak [1, 4, 1, 5, 9]
#answer3 = pi[1:6] # Gebruik er maar een
answer3 = e[2:3] + pi[2:6] # Gebruik allebei
print("Antwoord 3 is", answer3)
assert answer3 == [1, 4, 1, 5, 9], "answer3 moet [1, 4, 1, 5, 9] zijn."
```


#### Opdracht 4

Gebruik pi en e om de lijst [1, 2, 3, 4, 5] te maken. Bewaar deze lijst in de variabele answer4.

```python
# Opgave 4: maak [1, 2, 3, 4, 5]
answer4 = e[2:3] + e[0:1] + pi[0:1] + pi[2:3] + pi[4:5]
print("Antwoord 4 is", answer4)
assert answer4 == [1, 2, 3, 4, 5], "answer4 moet [1, 2, 3, 4, 5] zijn."
```


#### Opdracht 5

Gebruik h, s of g (je mag voor elke volgende opgave één of meerdere gebruiken) om de string hoi te maken.
Bewaar de string in de variabele met naam answer5.

```python
# De strings om mee te werken
h = "hanze"
s = "hogeschool"
g = "groningen"

# Opgave 5:  'hoi' maken
answer5 = s[0:2] + g[4]
print("Antwoord 5 is", answer5)
assert answer5 == "hoi", "answer5 moet 'hoi' zijn."
```


#### Opdracht 6

Gebruik h, s of g om de string schoenen te maken en bewaar deze string in de variabele answer6. (Ons record: 4 bewerkingen)

```python
# Opgave 6: maak de string "schoenen"
answer6 = s[4:8] + 2*g[-2:]
print("Antwoord 6 is", answer6)
assert answer6 == "schoenen", "answer6 moet 'schoenen' zijn."
```


#### Opdracht 7

Gebruik h, s of g om de string anzeogeschool te maken en bewaar deze string in de variabele answer7. (Ons record: 3 bewerkingen)

```python
# Opgave 7: maak de string "anzeogeschool"
answer7 = h[1:] + s[1:]
print("Antwoord 7 is", answer7)
assert answer7 == "anzeogeschool", "answer7 moet 'anzeogeschool' zijn"
```


#### Opdracht 8

Gebruik h, s of g om de string gnagnahahahahaha te maken en bewaar deze string in de variabele answer8. (Ons record: 7 bewerkingen)

```python
# Opgave 8: maak de string "gnagnahahahahaha"
answer8 = 2*(g[0:4:3] + h[1]) + 5*h[0:2]
print("Antwoord 8 is", answer8)
assert answer8 == "gnagnahahahahaha", "answer8 moet 'gnagnahahahahaha' zijn"
```


#### Opdracht 9

Gebruik h, s of g om de string legonoego te maken en bewaar deze string in de variabele answer9. (Ons record: 7 bewerkingen)

```python
# Opgave 9: maak de string "legonoego"
answer9 = s[-1] + s[-7:-10:-1] + g[-6:-8:-1] + s[-7:-10:-1]
print("Antwoord 9 is", answer9)
assert answer9 == "legonoego", "answer9 moet 'legonoego' zijn"
```


#### Opdracht 10

Gebruik h, s of g om de string leggings en bewaar deze string in de variabele answer10. (Ons record: 7 bewerkingen)

```python
# Opgave 10: maak de string "leggings"
answer10 = s[-1:-8:-6] + g[0:7:6] + g[4:7] + s[4]
print("Antwoord 10 is", answer10)
assert answer10 == "leggings", "answer10 moet 'leggings' zijn"
```


## Context

### [Rochambeau](/problems/context/2_rochambeau)

#### Opdracht

Schrijf een programma dat steen, papier en schaar met de gebruiker kan spelen.

```python
import random  # import the module named random
import time # import the module named time

"""Play a game of rock-paper-scissors in Dutch

arguments: no arguments (prompted text doesn't count as an argument)
result: no result       (printing doesn't count as a result)
"""

print()
print("Wel wel, iemand verveeld zich!")
print("Laten we steen, papier, schaar spelen.")
print()
time.sleep(4.0)

print("Om je geheugen op te frissen zijn hier de regels:")
print("Elke speler kiest een van de volgende drie wapens steen, papier of schaar.")
time.sleep(6.0)
print()
print("Papier wint van steen, steen wint van schaar en schaar wint van papier.")
print("Hebben we allebei hetzelfde wapen gekozen dan is het gelijk spel.")
time.sleep(6.0)

user = input("Kies een wapen (steen, papier of schaar): ")
comp = random.choice(["steen", "papier", "schaar"])

print("De gebruiker (jij) koos", user)
print("De computer (ik) koos", comp)

if user == "steen": # De speler heeft steen gekozen, de nested if constructie test nu of de speler de gewonnen, verloren of gelijk gespeeld heeft
    if(comp == "papier"):
        print("Ha, ik heb papier gekozen dus jij verliest!")
        print("Hopelijk heb je de volgende keer meer geluk...")
    elif(comp == "schaar"):
        print("O nee, steen vernietigt schaar.")
        print("Jij hebt gewonnen!")
    else:
        print("Gelijk spel! ")
    time.sleep(4.0)

elif user == "papier": # De speler heeft papier gekozen, de nested if constructie test nu of de speler de gewonnen, verloren of gelijk gespeeld heeft
    if(comp == "schaar"):
        print("Ha, ik heb schaar gekozen dus jij verliest!")
        print("Hopelijk heb je de volgende keer meer geluk...")
    elif(comp == "steen"):
        print("O nee, papier vernietigt steen.")
        print("Jij hebt gewonnen!")
    else:
        print("Gelijk spel! ")
    time.sleep(4.0)

elif user == "schaar": # De speler heeft schaar gekozen, de nested if constructie test nu of de speler de gewonnen, verloren of gelijk gespeeld heeft
    if(comp == "steen"):
        print("Ha, ik heb steen gekozen dus jij verliest!")
        print("Hopelijk heb je de volgende keer meer geluk...")
    elif(comp == "papier"):
        print("O nee, schaar vernietigt papier.")
        print("Jij hebt gewonnen!")
    else:
        print("Gelijk spel! ")
    time.sleep(4.0)
```


#### Uitbreiding

Hier is een versie met de voorgestelde uitbreidingen, behalve de RPS-25 en RPS-101 opties.

```python
# Met uitbreidingen
print()
print("Er is ook een versie met 5 wapens genaamd steen, papier, schaar, Spock en hagedis.")
print("De regels zijn: schaar snijdt papier, papier bedekt steen, steen plet hagedis, ")
print("hagedis vergiftigt Spock, Spock smelt schaar, schaar onthoofdt hagedis,")
print("hagedis eet papier, papier weerlegt Spock, Spock verdampt steen en steen breekt schaar.")
time.sleep(6.0)

while True: # Uitbreiding Blijven spelen
    print()
    version = input("Wil je met drie wapens of vijf wapens spelen? [drie/vijf]: ") # Uitbreiding RPS-5
    if(version != "drie" and version != "vijf"):
        version = input("Kies 'drie of 'vijf als antwoord!")

    if(version == "drie"):
        print()
        print("Je hebt voor de normale versie gekozen")
        user = input("Kies een wapen (steen, papier of schaar): ")
        comp = random.choice(["steen", "papier", "schaar"])

        print("De gebruiker (jij) koos", user)
        print("De computer (ik) koos", comp)

        if(user != "steen" and user != "papier" and user != "schaar"): # Uitbreiding Dummie proof
            print("Ha, je hebt een ongeldige keuze gemaakt dus ik win!")
            time.sleep(4.0)
        elif user == "steen": # De speler heeft steen gekozen, de nested if constructie test nu of de speler de gewonnen, verloren of gelijk gespeeld heeft
            if(comp == "papier"):
                print("Ha, ik heb papier gekozen dus jij verliest!")
                print("Hopelijk heb je de volgende keer meer geluk...")
            elif(comp == "schaar"):
                print("O nee, steen vernietigt schaar.")
                print("Jij hebt gewonnen!")
            else:
                print("Gelijk spel! ")
            time.sleep(4.0)

        elif user == "papier": # De speler heeft papier gekozen, de nested if constructie test nu of de speler de gewonnen, verloren of gelijk gespeeld heeft
            if(comp == "schaar"):
                print("Ha, ik heb schaar gekozen dus jij verliest!")
                print("Hopelijk heb je de volgende keer meer geluk...")
            elif(comp == "steen"):
                print("O nee, papier vernietigt steen.")
                print("Jij hebt gewonnen!")
            else:
                print("Gelijk spel! ")
            time.sleep(4.0)

        elif user == "schaar": # De speler heeft schaar gekozen, de nested if constructie test nu of de speler de gewonnen, verloren of gelijk gespeeld heeft
            if(comp == "steen"):
                print("Ha, ik heb steen gekozen dus jij verliest!")
                print("Hopelijk heb je de volgende keer meer geluk...")
            elif(comp == "papier"):
                print("O nee, schaar vernietigt papier.")
                print("Jij hebt gewonnen!")
            else:
                print("Gelijk spel! ")
            time.sleep(4.0)
        else: # Misschien is er een conditie gemist?
            print("Hmm, er lijkt iets mis gegaan.")

    elif(version == "vijf"):
        print()
        print("Je hebt voor de uitgebreide versie gekozen.")
        user = input("Kies een wapen (steen, papier, schaar, Spock of hagedis): ")
        comp = random.choice(["steen", "papier", "schaar", "Spock", "hagedis"])

        print("De gebruiker (jij) koos", user)
        print("De computer (ik) koos", comp)

        if(user != "steen" and user != "papier" and user != "schaar" and user != "Spock" and user != "hagedis"): # Uitbreiding Dummie proof
            print("Ha, je hebt een ongeldige keuze gemaakt dus ik win!")
            time.sleep(4.0)

        elif(user == "steen"): # De speler heeft steen gekozen, de nested if constructie test nu of de speler de gewonnen, verloren of gelijk gespeeld heeft
            if(comp == "papier" or comp == "Spock"):
                print("Ha, mijn keuze is beter dus jij verliest!")
                print("Hopelijk heb je de volgende keer meer geluk...")
            elif(comp == "schaar" or comp == "hagedis"):
                print("O nee, steen is beter dan mijn keuze.")
                print("Jij hebt gewonnen!")
            else:
                print("Gelijk spel! Geen van onze keuzes was de betere keuze.")
            time.sleep(4.0)

        elif user == "papier": # De speler heeft papier gekozen, de nested if constructie test nu of de speler de gewonnen, verloren of gelijk gespeeld heeft
            if(comp == "schaar" or comp == "hagedis"):
                print("Ha, mijn keuze is beter dus jij verliest!")
                print("Hopelijk heb je de volgende keer meer geluk...")
            elif(comp == "steen" or comp == "Spock"):
                print("O nee, papier is beter dan mijn keuze.")
                print("Jij hebt gewonnen!")
            else:
                print("Gelijk spel! Geen van onze keuzes was de betere keuze.")
            time.sleep(4.0)

        elif user == "schaar": # De speler heeft schaar gekozen, de nested if constructie test nu of de speler de gewonnen, verloren of gelijk gespeeld heeft
            if(comp == "steen" or comp == "Spock"):
                print("Ha, mijn keuze is beter dus jij verliest!")
                print("Hopelijk heb je de volgende keer meer geluk...")
            elif(comp == "papier" or comp == "hagedis"):
                print("O nee, schaar is de betere keuze.")
                print("Jij hebt gewonnen!")
            else:
                print("Gelijk spel! Geen van onze keuzes was de betere keuze.")
            time.sleep(4.0)

        elif user == "Spock": # De speler heeft Spock gekozen, de nested if constructie test nu of de speler de gewonnen, verloren of gelijk gespeeld heeft
            if(comp == "hagedis" or comp == "papier"):
                print("Ha, mijn keuze is beter dus jij verliest!")
                print("Hopelijk heb je de volgende keer meer geluk...")
            elif(comp == "schaar" or comp == "steen"):
                print("O nee, Spock is de betere keuze.")
                print("Jij hebt gewonnen!")
            else:
                print("Gelijk spel! Geen van onze keuzes was de betere keuze.")
            time.sleep(4.0)

        elif user == "hagedis": # De speler heeft hagedis gekozen, de nested if constructie test nu of de speler de gewonnen, verloren of gelijk gespeeld heeft
            if(comp == "steen" or comp == "schaar"):
                print("Ha, mijn keuze is beter dus jij verliest!")
                print("Hopelijk heb je de volgende keer meer geluk...")
            elif(comp == "Spock" or comp == "papier"):
                print("O nee, hagedis is de betere keuze.")
                print("Jij hebt gewonnen!")
            else:
                print("Gelijk spel! Geen van onze keuzes was de betere keuze.")
            time.sleep(4.0)

        else: # Misschien is er een conditie gemist?
            print("Hmm, er lijkt iets mis gegaan.")

    else:
        print("Er werd een niet opgegeven spel optie gekozen. Probeer het opnieuw.")

    #print("Het draait nog steeds...")
    print()
    response = input("Nog een keer spelen? [ja/nee] ")
    if response == "nee":
        break
```
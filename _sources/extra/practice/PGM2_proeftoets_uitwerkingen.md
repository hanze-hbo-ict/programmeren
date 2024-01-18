# Uitwerkingen proeftoets PGM2

## Opgave 1

Bij deze opgave gaat het om begrip hebben van lijsten, list comprehensions en lusconstructies op lijsten. Wat deze opgave lastig maakt is dat het gaat om een lijst van lijsten, een nested list.

```python
# De list om
L = [
    ["0308230", 7.6, True],
    ["8273927", 5.1, False],
    ["8234987", 6.4, False],
    ["2368612", 5.9, True],
    ["9731827", 3.2, False]
]

#Opgave 1a, met list comprehension
HW = [[x[0], x[1]+0.5] for x in L if x[2] == True]
print("Opgave 1a")
print(HW)
print()
```

Met het stuk 'for x in L' gaan we alle elementen in lijst L af. Deze elementen, x genoemd, zijn ook weer lijsten.

Of de elementen van x worden door gegeven naar de nieuwe lijst hangt af van het derde element van x. Met de if statement bepalen we of het huiswerk gemaakt is en dus het studentnummer en aangepaste cijfer in de nieuwe lijst komen.

Het studentnummer hoeft niet aangepast te worden en kan zo meegegeven worden aan de nieuwe functie met x[0]. Het cijfer, het tweede element van x, moet wel aangepast worden. Dit doen we door x[1]+0.5 terug te geven.

Het verwachte resultaat is net als de originele list, een nested list. Hier houden we rekening mee in de list comprehension door de terug te geven waarden tussen [] te plaatsen.

```python
#Opgave 1b, met lusconstructie
HW = []
# Met index lusconstructie
for i in range(len(L)):
    if L[i][2] == True:
        HW += [L[i][0], L[i][1]+0.5]

# Met element lusconstructie
HW2 = []
for x in L:
    if x[2] == True:
        HW2 += [x[0], x[1]+0.5]

print("Opgave 1b")
print("HW, index", HW)
print("HW, element", HW2)
print()
```

Voor de lusconstructie begonnen wordt, moet eerst de nieuwe lijst leeg aangemaakt worden. Als de nieuwe lijst in de lusconstructie aangemaakt wordt dan bestaat hij alleen in de lus constructie en wordt hij bij elke loop opnieuw aangemaakt. De nieuwe lijst moet dus buiten de scope van de lus constructie staan om zo alle elementen te kunnen krijgen en te blijven bestaan als de lusconstructie klaar is.

Met de index lusconstructie gaan we over elk element in lijst L met behulp van de index, i genoemd. Met `range(len(L))` zal de lusconstructie beginnen met i = 0 en door gaan tot en met i = L-1, wat precies overeen komt met de indices van lijst L.

De eerste stap in de lusconstructie is om te kijken of het huiswerk gemaakt is. Is het huiswerk niet gemaakt dan gebeurt er niets. Is het huiswerk wel gemaakt dan wordt het studentnummer en het aangepaste cijfer toegevoegd aan de nieuwe nested list met de += statement.

In plaats van de index lusconstructie kan je de element lusconstructie gebruiken. Die werkt hetzelfde maar in plaats van L[][] werk je met x[], net als in de bovenstaande list comprehension.


## Opgave 2

Deze opgave gaat over functies en de scope van functies en lusconstructies.

```python
# Het origineel
# def over_hundred(L):
#     result = 0
#     for i in L:
#         result += result + L[i]
#         if result > 100:
#             return True
#         return False

# lc = [x for x in range(12, 15)]
# print(over_hundred(lc))

# De oplossing
def over_hundred(L):
    """
    Deze functie somt alle elementen uit input variable lijst L en bepaalt of de som meer dan 100 is.
    Als de som > 100 dan geeft de functie True terug en anders een False.
    """
    result = 0
    for i in L:
        result += i
        # Of, als je het += teken niet prettig vindt:
        # result = result + i
    if result > 100:
        return True
    return False

lc = [x for x in range(12, 15)]
lc2 = [20,30,40,50]
lc3 = [i for i in range(10,35,5)]
# print("Lijst 1:", lc)
# print("Lijst 2:", lc2)
# print("Lijst 3:", lc3)
assert over_hundred(lc) == False
assert over_hundred(lc2) == True
assert over_hundred(lc3) == False
```

Een goede docstring geeft weer wat de functie doet en wat de input en output waarden zijn. Deze docstring laat een van de vele manieren zien.

De functie begint goed door de result variabele buiten de scope van de lusconstructie aan te maken met de beginwaarde nul.

Bij Opgave 1 is al het verschil tussen een index lus en een elementen lus. De eerste fout in de gegeven functie is dat deze twee door elkaar gehaald worden. Er wordt een elementen lus begonnen, `for i in L:`, maar de result variabele wordt aan gepast met L[i]. Dit gaat niet, het is of de een of de ander. Hier hebben we er voor gekozen om de elementen versie aan te houden, maar `for i in range(len(L)):` had ook goed geweest.

De volgende fout is in de opbouw van de update statement van result, `result += result + L[i]`. Met deze statement wordt result twee keer gebruikt in de som. De statement `result += result + L[i]` is namelijk `result = result + result + L[i]`. Dit hebben wij gecorrigeerd door `result += i` te gebruiken.

De volgende fout is de locatie van de if statement en return statements. Deze staan beide in de scope van de lusconstructie. Dus bij de eerste iteratie wordt de if statement geactiveerd en een van de return statements zorgt ervoor dat de for-lus en de functie stoppen. De if statement en de `return False` statement worden buiten de scope van lusconstructie geplaatst.

Als laatste zijn de drie gevraagde assert statements toegevoegd.


## Opgave 3

Deze opgave test je kennis over de while constructie en hoe deze moet worden opgebouwd.

In deze opgave kun je op twee manieren de input waardes verwerken: je stopt ze in een lijst of je werkt met twee variabelen die direct worden aangepast. Beide staan in de oplossing:

```python
# Werken met een lijst: De lijst is leeg voor de while loop in gaan
L = []
# Werken met twee variablen: De twee variabelen met nul aanmaken
count = 0
sum = 0 # We gaan er van uit dat er integers gegeven worden

# De input variabele is positief om mee te beginnen
inp = 0

# tijd voor de while loop
while inp >= 0:
    inp = int(input("Geef positief getal: "))

    # Check of het een positief getal is
    if inp >= 0:
        # Werken met een lijst:
        L += [inp]
        # Werken met twee variablen:
        count += 1
        sum += inp

# Werken met een lijst: om de som te krijgen:
L_sum = 0
for i in L:
    L_sum += i

print("Getallen gegeven, lijst versie: ", str(len(L)))
print("Getallen gegeven, variabelen versie: ", str(count))
print("Getallen opgeteld, lijst versie: ", str(L_sum))
print("Getallen opgeteld, variabelen versie: ", str(sum))
print()
```

Net als met de for lussen, moet ook bij de while lussen rekening gehouden worden met de scope. De variabelen die ook na de while lus nodig zijn worden daarom voor de while lus aangemaakt.

Voor de variabelen aangepast kunnen worden, moet eerst de gebruiker om input gevraagd worden.

Werken met een lijst: De input wordt aan de lijst toegevoegd als nieuw element. Hoe veel getallen worden opgegeven wordt indirect bij gehouden met de grote van de lijst: elk nieuw toegevoegde element maakt de lijst namelijk een groter. Met `len(L)` kan vervolgens gezien worden hoe veel elementen in de lijst staan. Om de som van de getallen te krijgen is na de while-lus een extra lus nodig om over de lijst met getallen te loopen en zo de som te berekenen.

Werken met twee variabelen: De input wordt direct bij de som variabele opgeteld waardoor er na de while lus geen extra acties nodig zijn. Met `count += 1` wordt bijgehouden hoe veel getallen er gegeven zijn.

Om de som te krijgen als je alleen met een lijst werkt is er dus een extra lus nodig. om te bepalen welke van de twee voor het programma het beste is, kun je jezelf de volgende vraag stellen: "Heb ik de ingevoerde getallen later nog nodig?" Is het antwoord nee dan kun je de twee variabelen gebruiken. Is het antwoord ja, dan kun je de getallen het beste opslaan in een lijst.

**Note:** Een lijst en de sum variabele voor de while lus is ook een optie. Dan is er geen extra lus nodig voor de som.


## Opgave 4

Deze opgave gaat over het ontwerpen en schrijven van een functie en nested lusconstructie, en hoe goed je de scope van nested lusconstructies begrijpt.

```python
def number_stairs(size):
    """
    Print een ladder van nummers.
    Input: size, aantal treden.
    Ouput: een ladder van nummers op het scherm.
    """
    for rij in range(size):
        for kolom in range(1, rij+1):
            print(str(kolom), end = "")
        print()
    print()

number_stairs(5)
number_stairs(3)
```

Het kan helpen om bij nested loops te werken met variabele namen die direct laten zien wat ze (visueel) representeren. Daarom heet de lus variabele van de eerste lus 'rij' en wordt voor de tweede lus 'kolom' gebruikt.

De aan de functie mee gegeven variabele `size` bepaald hoe veel rijen er moeten komen. Daarom wordt deze meegeven aan range() bij het aanmaken van de eerste lus. Om te corrigeren voor range() begint bij nul, geven we niet alleen de eind waarde maar ook de start waarde mee voor `rij`.

Hetzelfde doen we voor kolom, maar in plaats van `size` gebruiken we `rij`. De hoeveelheid kolommen hangt namelijk af van welke rij het programma op dat moment behandelt. Omdat de kolom variabelen waarde hetzelfde zijn als de nummers die naar het scherm geprint zijn, kunnen we de kolom variable gebruiken in de print statements. De print statement heeft de optie om het einde van de string een andere waarde te geven in plaats van de standaard nieuwe regel. Hier maken we gebruik van bij het printen van de kolommen.

Met een lege print statement in de scope van de rij lus en na de kolom lus wordt ook visueel een nieuwe regel gestart voor de rij lus naar de volgende rij gaat.


## Opgave 5

Deze opgave gaat over het uitdenken en uitwerken van een programma met de hulp van functies.

### Opgave 5a

```python
def intersect(l1, l2):
    """
    Geeft welke getallen in beide lijsten voorkomen.
    Input: twee lijsten met integers, l1 en l2.
    Output: een lijst met integers.
    """
    L = []
    # Als een van beide lijsten leeg is dan zijn er sowieso geen gemene delers en kan L leeg terug gegeven worden
    if l1 == []:
        return L
    elif l2 == []:
        return L

    # Als beide lijsten een of meerdere getallen bevatten dan gaan we de for lus in om L te vullen met gemene delers
    for i in l1:
        if i in l2:
            L += [i]
    return L

l1 = [x for x in range(1,10)]
l2 = [x for x in range(3,12,2)]
l3 = [x for x in range(4,13,2)]
assert intersect(l1,l2) == [3,5,7,9]
assert intersect(l1, l3) == [4,6,8]
assert intersect(l2, l3) == []
```

Het is belangrijk om bij het ontwikkelen van een functie te bepalen wat de mogelijke wat de mogelijke situaties zijn die de functie kan tegen komen. In dit geval, als een van de lijsten leeg is dan heeft het geen nut om door een lijst te loopen om opzoek te gaan naar elementen die in beide lijsten voorkomen. Met de if-elif statement testen we dit voor de loop begint.

De functie hoeft maar over een van de twee lijsten te lussen aangezien we met de `if element in lijst2:` snel kunnen zien of een element in de andere lijst te vinden is. Als een element in beide lijsten voorkomt dan wordt dit element toegevoegd aan de nieuwe lijst. Let op dat we een lijst willen maken en het element dus tussen [] gezet moet worden op correct toegevoegd te worden.

### Opgave 5b

Een voorbeeld omschrijving:

Om de grootste gemene deler te kunnen vinden, moeten we eerst weten door welke getallen beide variabelen gedeeld kunnen worden.

Stap 1 is dus om de delers van beide getallen te vinden met behulp van een list comprehension met range(1,var+1) om alle getallen tot en met var zelf en met een if statement die gebruikt maakt van de modulo operator voor integer devision. De list comprehension wordt opgeslagen in een nieuwe lijst met een duidelijk naam voor later gebruik. Deze stap resulteert in twee lijsten, een voor elke variabele.

Nu we de delers weten, kunnen we opzoek gaan naar de delers die voor beide getallen gebruikt kunnen worden. Dit doen we door de twee lijsten met delers mee te geven aan de intersect functie. De lijst die door deze functie wordt terug gegeven, is de lijst met gemene delers en wordt opgeslagen onder een passende naam.

Als laatste moeten we met de max() het grootste getal uit de lijst met gemene delers halen. We moeten wel rekening houden met de mogelijkheid dat er geen gemene delers gevonden zijn. Als er geen gedeelde delers zijn dan is de lijst die de intersect functie terug geeft leeg. Dit kunnen we checken met een if statement die de lijst vergelijkt met een lege lijst. Is de lijst leeg dan returnt de functie het getal nul. Anders wordt het resultaat van de max functie op de lijst met gemene delers terug gegeven.

### Opgave 5c

De code is al in 5b toegelicht.

```python
def ggd(g1, g2):
    """
    Bepaalt de grootste gemene deler.
    Input: twee integers.
    output: een integer.
    """

    # Stap 1: maak lijsten met delers voor de twee variabelen
    d1 = [x for x in range(1,g1+1) if g1 % x == 0]
    d2 = [x for x in range(1,g2+1) if g2 % x == 0]

    # Stap 2: gebruik de twee delers lijsten en intersect functie om de lijst met gedeelde delers te krijgen
    gd = intersect(d1,d2)

    # Stap 3: Bepaal de ggd met de max functie en geef dit getal terug
    if gd == []: # Er werden geen gemene delers gevonden
        return 0
    else: # Er zijn gemene delers gevonden, geef de grootste terug
         return max(gd)

assert ggd(10,15) == 5
assert ggd(6,24) == 6
assert ggd(0,6) == 0
```


## Opgave 6

Deze opgave gaat over Klassen en Objecten en hoe deze verder te ontwikkelen.

### Opgave 6a

De player_takes functie.

```python
def player_takes(self, remove_sticks):
    """
    Haalt aantal speler stokjes weg.
    Input: integer remove_sticks
    Output: None
    """
    self.sticks -= remove_sticks
    return
```

Elke functie die onderdeel is van een class heeft de self argument. Na de self argument volgen eventuele aanroep argumenten. In dit geval is er een functie argument, het remove_sticks argument welke aangeeft hoe veel stokjes de speler wilt verwijderen.

De variabele die bij houdt hoe veel stokjes er zijn, `sticks`, is onderdeel van de class. Om deze aan te kunnen passen, moet er eerst `self.` voor de variable gezet worden. Verder is er geen verschil met het aanpassen een de waarde van een variabele.

De functie hoeft niks terug te geven, maar om aan te geven dat de functie klaar is, wordt er wel een return statement gebruikt.

### Opgave 6b

De AI_turn functie.

```python
def AI_turn(self):
    """
    Bepaalt aantal AI stokjes om weg te halen.
    Input: None
    Output: integer
    """
    remove_sticks = self.sticks % 4 # Integer division, wat over blijft moet verwijderd worden om een meervoud van vier over te houden
    if remove_sticks == 0: # Er ligt al een meervoud van vier op tafel, random aantal stokjes moet nu gekozen worden
        remove_sticks = random.randint(1,4)

    return remove_sticks
```

Net als de functie player_takes, is de AI_turn onderdeel van de class en vereist dus het `self` argument.

De AI bepaalt hoe veel stokjes er weg gehaald worden aan de hand van hoe veel stokjes er nog zijn en of het mogelijk is om na zijn/haar beurt een veelvoud van 4 stokjes over te houden. Met de modulo operator op `self.sticks` kan bepaald worden hoe veel stokjes er weg gehaald moeten worden. Let op: sticks in onderdeel van de class en kan alleen benaderd en aangepast worden door `self.` te gebruiken.

Nu kan het zijn dat er al een meervoud van 4 ligt. In dat geval geeft de modulo statement een nul terug. Dit is geen optie voor een keuze en verreist dan een willekeurige keuze. Dit wordt bereikt door met een if statement te controleren of remove_sticks == 0. Als dit True is dan wordt met de random.randint functie een willekeurige aantal stokjes gekozen.

Als laatste wordt de remove_sticks terug gegeven met de return statement.

### Opgave 6c

De game_over functie.

```python
def game_over(self):
    """
    Bepaald of het spel over is.
    Input: None
    Output: True or False
    """
    if self.sticks == 0: # Game over want er zijn geen stokjes meer
        return True
    return False
```

Hier geldt net als eerder dat de functie onderdeel is van een class even als de variable en dus self op de juiste manier moet worden toegepast. De rest van de functie spreekt voor zich.

### Opgave 6d

De while loop mist nog de computer beurt. De oplossing bevat ook de hier boven beschreven functies (methoden) van de class Nim.

```python
import random

class Nim:
     def __init__(self, number_of_sticks):
          self.sticks = number_of_sticks

     # hier komt de functie player_takes()
     def player_takes(self, remove_sticks):
          """
          Haalt aantal speler stokjes weg.
          Input: integer remove_sticks
          Output: None
          """
          self.sticks -= remove_sticks
          return

     def AI_turn(self):
          """
          Bepaalt aantal AI stokjes om weg te halen.
          Input: None
          Output: integer
          """
          remove_sticks = self.sticks % 4 # Integer division, wat over blijft moet verwijderd worden om een meervoud van vier over te houden
          if remove_sticks == 0: # Er ligt al een meervoud van vier op tafel, random aantal stokjes moet nu gekozen worden
               remove_sticks = random.randint(1,4)

          return remove_sticks

     def game_over(self):
          """
          Bepaald of het spel over is.
          Input: None
          Output: True or False
          """
          if self.sticks == 0: # Game over
               return True
          return False


game = Nim(16)

while(True):
     print("stokjes op tafel: ", game.sticks)
     player_turn = int(input("hoeveel stokjes? "))
     if player_turn not in [1, 2, 3]:
          print("illigal move")
          continue
     game.player_takes(player_turn)
     if game.game_over():
          print("You win")
          break

     # computer beurt
     remove_sticks_AI = game.AI_turn()
     game.sticks -= remove_sticks_AI
     print("AI stokjes:", remove_sticks_AI)
     if game.game_over():
          print("AI wins")
          break
```

Als de class klaar is dan kan er een object van het type class gemaakt worden. Om alle class elementen, dus de class variable (data) en class functies (methoden)x, te kunnen benaderen wordt nu niet meer met `self.` gewerkt, maar met de object naam. Bijvoorbeeld voor het aanroepen van een van de functies: `game.game_over()`.

De beurt van de computer begint met het bepalen van hoe veel stokjes er verwijderd moeten worden. Dit wordt gedaan door de functie `AI_turn` aan te roepen en het result op te slaan in een variable. Vervolgens wordt de class variable sticks geupdate en er wordt gekeken of de AI gewonnen heeft. Heeft de AI gewonnen dan stopt de while lus.
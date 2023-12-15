# TR Investeringen BV

```{warning}
Je mag **geen** gebruik maken van de ingebouwde functies `sum`, `min` of `max` in deze opgave. Schrijf in plaats daarvan bij het bouwen van de verschillende menu-opties hulpfuncties die de gegevens op de juiste manier kunnen verwerken. Als je deze functies *echt* wilt gebruiken, schrijf dan je eigen versies hiervan.
```

## Begincode

In deze opgave ga je een lus gebruiken voor gebruikersinteractie. Je ziet hier startcode die je verder gaat uitwerken:

```python
#
# Voorbeeldprogramma voor een lus voor gebruikersinteractie
#  (een variant van de versie van het college)
#


def menu():
    """A function that simply prints the menu"""
    print()
    print("(0) Doorgaan!")
    print("(1) Nieuwe lijst invoeren")
    print("(2) Volgende element voorspellen")
    print("(9) Stoppen! (einde)")
    print()


def predict(L):
    """Predict ignores its argument and returns
       what the next element should have been.
    """
    return 42


def find_min(L):
    """find min uses a loop to return the minimum of L.
       Argument L: a nonempty list of numbers.
       Return value: the smallest value in L.
    """
    result = L[0]
    for x in L:
        if x < result:
            result = x
    return result


def find_min_loc(L):
    """find min loc uses a loop to return the minimum of L
            and the location (index or day) of that minimum.
        Argument L: a nonempty list of numbers.
        Results:  the smallest value in L, its location (index)
    """
    min_val = L[0]
    min_loc = 0

    for i in list(range(len(L))):
        if L[i] < min_val:  # een kleinere gevonden!
            min_val = L[i]
            min_loc = i

    return min_val, min_loc


def main():
    """The main user-interaction loop"""
    secret_value = 4.2

    L = [30, 10, 20]  # een beginlijst

    while True:     # de lus voor gebruikersinteractie
        print("\n\nDe lijst is", L)
        menu()
        choice = input("Maak een keuze: ")

        #
        # De invoer van de gebruiker "opschonen en controleren"
        #
        try:
            choice = int(choice)   # omzetten naar een int!
        except:
            print("Ik begreep de invoer niet! Verder gaan...")
            continue

        # de gekozen menu-optie uitvoeren
        #
        if choice == 9:    # We willen stoppen
            break          # De hele while-lus afbreken

        elif choice == 0:  # We willen doorgaan...
            continue       # Terug naar het begin van de while-lus

        elif choice == 1:  # We willen een nieuwe lijst invoeren
            new_L = input("Voer een nieuwe lijst in: ")    # _iets_ invoeren

            #
            # De invoer van de gebruiker "opschonen en controleren"
            #
            try:
                new_L = eval(new_L)   # eval voert de Python-interpreter uit! Let op: Gevaarlijk!
                if not isinstance(new_L, list):
                    print("Dat lijkt geen lijst. L wordt niet aangepast.")
                else:
                    L = new_L  # Hier is het wel OK, dus we passen onze lijst L aan
            except:
                print("Ik begreep de invoer niet. L wordt niet aangepast.")

        elif choice == 2:   # Het volgende element voorspellen en toevoegen
            n = predict(L)  # Het volgende element uit de functie predict halen
            print("Het volgende element is", n)
            print("Het wordt toegevoegd aan je lijst...")
            L = L + [n]     # ...en toevoegen aan de lijst

        elif choice == 3:  # Geheime menu-optoe!
            pass       # Dit is het "nop"- (niets-doen) statement in Python

        elif choice == 4:  # Geheime menu-optie (iets interessanter...)
            m = find_min(L)
            print("De kleinste waarde van L is", m)

        elif choice == 5:  # Nog een geheime menu-optie (nog interessanter...)
            min_val, min_loc = find_min_loc(l)
            print("De kleinste waarde van L is", min_val, "op dag #", min_loc)

        else:
            print(choice, " ?      Dat staat niet op het menu!")

    print()
    print("Tot gisteren!")
```

## De TRI-opgave

In deze opgave ga je een (op tekst gebaseerd) menu implementeren met opties om een lijst met aandelenprijzen (of andere floating-pointwaardes) te analyseren. Hiermee kan je op een aantal verschillende manieren lussen gebruiken, en oefenen met het verwerken van gebruikersinvoer.

De hoofdfunctie die je voor deze opgave moet schrijven heet `main()`. Merk op dat deze geen argumenten meekrijgt. In plaats daarvan moet het een menu tonen met deze keuzes:

```text
(0) Voer een nieuwe lijst in
(1) Druk de huidige lijst af
(2) Bepaal de gemiddelde prijs
(3) Bepaal de standaardafwijking
(4) Bepaal het minimum en de bijbehorende dag
(5) Bepaal het maximum en de bijbehorende dag
(6) Je TR-investeringsplan
(9) Stoppen

Maak je keuze:
```

Je mag gerust de tekst aanpassen, maar je mag de functionaliteit van de functies **niet** aanpassen! Als je je eigen extra menu-opties wilt toevoegen, gebruik dan andere waardes (zie de bonusopgaven hieronder).

Nadat het menu getoond is, moet het programma wachten op invoer van de gebruiker. (Je mag ervan uitgaan dat de gebruiker een integer als invoer geeft.) De functie moet dan

* Een waarschuwing afdrukken als de integer geen geldige menu-optie is
* Stopppen als de gebruiker een `9` als invoer geeft
* De gebruiker een nieuwe lijst aandelenprijzen laten invoeren als de gebruiker een `0` kiest.
* Een tabel met dagen en prijzen, met labels, afdrukken als de gebruiker een `1` kiest.
* De gevraagde statisieken over de lijst berekenen als de gebruiker opties `2` tot en met `6` kiest.

Voor elke optie behalve `9` moet de functie na elke keuze opnieuw het menu tonen en de gebruiker om invoer vragen.

Veel van de onderdelen zijn eenduidig, maar je vindt hieronder een paar aanwijzingen voor enkele van de opties.

Daar weer onder vind je een voorbeelduitvoer die een mogelijke interactie met de functie `main()` toont.

### De tijdreisstrategie

Voor menu-optie 6 moet je de beste dagen vinden om het aandeel te kopen en verkopen om de winst zo groot mogelijk te maken. Wel moet de ***verkoopdag groter of gelijk zijn aan de koopdag***. Je kan hiervoor de voorbeeldfunctie `min_diff` uit het college aanpassen om deze maximale winst te vinden.

### De standaardafwijking berekenen

Gebruik deze formule om de standaardafwijking van de aandelen te berekenen. Merk op dat <code>L<sub>av</sub></code> de gemiddelde waarde van de elementen van lijst `L` is. Je mag er bovendien van uitgaan dat `L` nooit leeg zal zijn.

$$
\sqrt \frac{\Sigma_{i} (\text{L[i]} - \text{L}_{av} )^2}{\text{len(L)}}
$$

Mocht je niet bekend bent met de Σ-notatie, dit betekent dat je alle waardes bij elkaar moet optellen. Vraag om hulp als je er niet uitkomt!

### Hulpfuncties

Je **moet** een hulpfunctie schrijven voor de menu-opties 2 tot en met 6. (De anderen werken al of hebben geen extra functie nodig.)

Bij optie 6 is het belangrijk om te bedenken dat je altijd meer dan één waarde kan teruggeven uit een functie. Bijvoorbeeld,

```python
def f(x):
    return x, (x+4)
```

Deze functie kan als volgt worden aangeroepen:

```python
a, b = f(38)
```

In dit geval krijgt `a` de waarde `38` en `b` de waarde `42`.

### Net formatteren...

Dit is optioneel, maar als je net geformateerde kolommen wilt afdrukken kan de volgende aanpak helpen. Probeer de voorbeelden in de Pythonprompt te plakken, om te zien wat ze doen. De formatteerstring geeft aan *hoe* dingen geformateerd worden, en de invoerwaardes voor `.format` geven aan *welke* waardes op die manier geformatteerd zullen worden.

```ipython
In [3]: print("{0: >4} : € {1: >6}".format("Dag", "Prijs"))
 Dag : €  Prijs

In [4]: print("{0: >4} : € {1: >6}".format(3, 42))
   3 : €     42

In [5]: print("{0: >4} : € {1: >6}".format(11, 27042))
  11 : €  27042
```

De *formatteerstring*, te weten `"{0: >4} : $ {1: >6}"`, zegt in het kort drie dingen:

* Druk het te formatteren argument #`0` rechtsuitgelijnd af in een ruimte met een breedte van 4
* Druk daarna een spatie, een dubbele punt, een spatie, een euroteken en een spatie af (allemaal precies zoals opgegeven)
* Druk daarna het te formatteren argument #`1` rechtsuitgelijnd af in een ruimte met een breedte van 6.

Merk op dat het `.format(input0, input1)` na de formatteerstring de te formatteren waardes opgeeft!

Je kan hiermee experimenteren om het resultaat te krijgen wat je wilt. Afdrukken zonder je druk te maken over het formaat is ook goed!

### Voorbeelduitvoer van het standaard TRI-programma

Hier is een voorbeelduitvoer; je hoeft dit formaat niet precies te volgen (maar het mag wel), maar het is bedoeld om een voorbeeld te tonen van elke mogelijkheid in het menu:

```text
In [1]:  main()
(0) Voer een nieuwe lijst in
(1) Druk de huidige lijst af
(2) Bepaal de gemiddelde prijs
(3) Bepaal de standaardafwijking
(4) Bepaal het minimum en de bijbehorende dag
(5) Bepaal het maximum en de bijbehorende dag
(6) Je TR-investeringsplan
(9) Stoppen

Maak je keuze: 0
Voer een nieuwe lijst prijzen in: [20, 10, 30]
(0) Voer een nieuwe lijst in
(1) Druk de huidige lijst af
(2) Bepaal de gemiddelde prijs
(3) Bepaal de standaardafwijking
(4) Bepaal het minimum en de bijbehorende dag
(5) Bepaal het maximum en de bijbehorende dag
(6) Je TR-investeringsplan
(9) Stoppen

Maak je keuze: 1

Dag  Prijs
---  -----
  0  20.00
  1  10.00
  2  30.00


(0) Voer een nieuwe lijst in
(1) Druk de huidige lijst af
(2) Bepaal de gemiddelde prijs
(3) Bepaal de standaardafwijking
(4) Bepaal het minimum en de bijbehorende dag
(5) Bepaal het maximum en de bijbehorende dag
(6) Je TR-investeringsplan
(9) Stoppen

Maak je keuze: 2

De gemiddelde prijs is 20.0


(0) Voer een nieuwe lijst in
(1) Druk de huidige lijst af
(2) Bepaal de gemiddelde prijs
(3) Bepaal de standaardafwijking
(4) Bepaal het minimum en de bijbehorende dag
(5) Bepaal het maximum en de bijbehorende dag
(6) Je TR-investeringsplan
(9) Stoppen

Maak je keuze: 3

De standaardafwijking is 8.16496580928


(0) Voer een nieuwe lijst in
(1) Druk de huidige lijst af
(2) Bepaal de gemiddelde prijs
(3) Bepaal de standaardafwijking
(4) Bepaal het minimum en de bijbehorende dag
(5) Bepaal het maximum en de bijbehorende dag
(6) Je TR-investeringsplan
(9) Stoppen

Maak je keuze: 4

Het minimum is 10 op dag 1


(0) Voer een nieuwe lijst in
(1) Druk de huidige lijst af
(2) Bepaal de gemiddelde prijs
(3) Bepaal de standaardafwijking
(4) Bepaal het minimum en de bijbehorende dag
(5) Bepaal het maximum en de bijbehorende dag
(6) Je TR-investeringsplan
(9) Stoppen

Maak je keuze: 5

Het maximum is 30 op dag 2


(0) Voer een nieuwe lijst in
(1) Druk de huidige lijst af
(2) Bepaal de gemiddelde prijs
(3) Bepaal de standaardafwijking
(4) Bepaal het minimum en de bijbehorende dag
(5) Bepaal het maximum en de bijbehorende dag
(6) Je TR-investeringsplan
(9) Stoppen

Maak je keuze: 6
Je TRI investeringsstrategie is om

    Te kopen op dag 1  voor prijs 10
 Te verkopen op dag 2  voor prijs 30

 Dit geeft een totale winst van 20


(0) Voer een nieuwe lijst in
(1) Druk de huidige lijst af
(2) Bepaal de gemiddelde prijs
(3) Bepaal de standaardafwijking
(4) Bepaal het minimum en de bijbehorende dag
(5) Bepaal het maximum en de bijbehorende dag
(6) Je TR-investeringsplan
(9) Stoppen

Maak je keuze: 7


Optie 7 bestaat niet.
Probeer het opnieuw



(0) Voer een nieuwe lijst in
(1) Druk de huidige lijst af
(2) Bepaal de gemiddelde prijs
(3) Bepaal de standaardafwijking
(4) Bepaal het minimum en de bijbehorende dag
(5) Bepaal het maximum en de bijbehorende dag
(6) Je TR-investeringsplan
(9) Stoppen

Maak je keuze: 9


Tot gisteren!
```

## Bonusopgave: creatieve menu-opties

Als je wilt kan je extra menu-opties toevoegen (met andere numerieke labels) die de lijst op een andere, eigen ontworpen manier verwerken. Dit hoeft niet serieus te zijn! In ieder geval worden de opties beoordeeld op wat ze doen en hoe makkelijk ze te gebruiken zijn.
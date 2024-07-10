# Statistieken

## Net formatteren...

Dit is optioneel, maar als je net geformatteerde kolommen wilt afdrukken kan de volgende aanpak helpen. De formatteerstring geeft aan *hoe* dingen geformatteerd worden, en de invoerwaardes voor `.format` geven aan *welke* waardes op die manier geformatteerd zullen worden.

```ipython
In: print("{0: >4} : € {1: >6}".format("Dag", "Prijs"))
 Dag : €  Prijs

In: print("{0: >4} : € {1: >6}".format(3, 42))
   3 : €     42

In: print("{0: >4} : € {1: >6}".format(11, 27042))
  11 : €  27042
```

De *formatteerstring*, te weten `"{0: >4} : $ {1: >6}"`, zegt in het kort drie dingen:

* Druk het te formatteren argument #`0` rechts uitgelijnd af in een ruimte met een breedte van 4
* Druk daarna een spatie, een dubbele punt, een spatie, een euroteken en een spatie af (allemaal precies zoals opgegeven)
* Druk daarna het te formatteren argument #`1` rechts uitgelijnd af in een ruimte met een breedte van 6.

Merk op dat het `.format(input0, input1)` na de formatteerstring de te formatteren waardes opgeeft!

Je kan hiermee experimenteren om het resultaat te krijgen wat je wilt. Afdrukken zonder je druk te maken over het formaat is ook goed!


## Opdracht 1

a. Kopieer onderstaande code over naar een bestand genaamd 'wk3wc2.py'
```python
#
# Programma voor een lus voor gebruikersinteractie
#

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
        elif choice == 2:
            min_val = find_min(L)
            print("De kleinste waarde van L is", min_val)

        else:
            print(choice, " ?      Dat staat niet op het menu!")
    print()
    print("Tot gisteren!")


def menu():
    """A function that simply prints the menu"""
    print()
    print("(0) Doorgaan!")
    print("(1) Nieuwe lijst invoeren")
    print("(2) Kleinste waarde vinden")
    print("(9) Stoppen! (einde)")
    print()


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

main()
```

b. Test of de code werkt. Probeer een nieuwe lijst in te voeren en hiervan het minimum te bepalen.
c. Schrijf de functie `print_lijst(L)` dat een lijst accepteert en uitprint als een tabel, met de index in de eerste kolom en de waarden in de tweede.

```ipython
index  Waarde
-----  ------
0      20
1      10
2      30
```

d. Pas het programma aan zodat er een optie is om de lijst te printen.



## Opdracht 2
a. Schrijf de functie `find_max(L)` dat een lijst accepteert en de hoogste waarde van die lijst teruggeeft. Je mag niet de ingebouwde `max()` functie gebruiken.
b. Pas het programma zo aan dat het vinden van de grootste waarde een optie is.

## Opdracht 3
a. Schrijf de functie `summing(L)` dat een lijst accepteert en de som van alle waardes teruggeeft. Je mag niet de ingebouwde functie `sum()` gebruiken. Vergeet niet je functie te testen.
b. Schrijf de functie `size(L)` dat een lijst accepteert en de lengte van de lijst teruggeeft. Je mag niet de ingebouwde functie `len()` gebruiken. Vergeet niet je functie te testen.
c. Schrijf de functie `gemiddelde(L)` dat een lijst accepteert en de gemiddelde waarde van die lijst teruggeeft. Vergeet niet je functie te testen. Maak gebruik van de functies `summing()` en `size()`
d. Pas het programma zo aan dat er een optie is om de gemiddelde waarde van de lijst te printen.


## Opdracht 4: Counting sort.
Counting sort, soms ook count-sort genoemd, is een sorteeralgoritme, dat alleen kan worden gebruikt voor gehele getallen. Als de kleinste en grootste waarden niet bekend zijn, zullen deze vooraf aan het sorteren bepaald moeten worden. Daarna wordt er bijgehouden hoe vaak een waarde in de lijst voorkomt, zogenaamd turven. De kleinste waarde staat op index 0. De lijst is even lang als dat er getallen zijn tussen het minimum en maximum waarde.

Een voorbeeld: De ongesorteerde reeks gehele getallen is 6, 4, 6, 8, 9, 6, 4, 9, 5, 5, 5, 8, 5. Het kleinste getal is 4 en het grootste is 9. Op basis daarvan wordt van elk element tussen 4 en 9 geteld hoe vaak het in de rij voorkomt. Geturfd resultaat:
```ipython
index   count
0 (4)    2
1 (5)    4
2 (6)    3
3 (7)    0
4 (8)    2
5 (9)    2
```
De resultaten van de telling worden weer achter elkaar geplaatst en het sorteren is voltooid: 4, 4, 5, 5, 5, 5, 6, 6, 6, 8, 8, 9, 9.

a. Schrijf de functie `counting sort()` dat een lijst ontvangt en een gesorteerde lijst teruggeeft. Maakt gebruik van counting sort.
b. Pas het programma zo aan dat er de optie is om de lijst te sorteren.
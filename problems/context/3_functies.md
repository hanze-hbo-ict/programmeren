---
title: Rekenmachine
file: wk3co1.py
---

# Rekenmachine

Het doel van deze opgave is om een rekemachine te maken dat de oppervlakte en inhoud van verschillende figuren kan bereken. De rekenmachine zal bestaan uit verschillende functies. Vergeet niet bij de elke functie een docstring toe te voegen en test de functie met behulp van assertions. Gebruik google als je niet weet hoe je de oppervlakte of inhoud van een figuur kan berekenen.

Het programma vraagt de gebruiker wat het wil berekenen, vraagt om de juiste input en geeft het resultaat terug. Vervolgens vraagt het nogmaals wat er berekent moet worden. Als de gebruiker een verkeerde input geeft stopt het programma.

Kort voorbeeld wat het programma moet kunnen.

```ipython
out: "Wat moet er berekent worden? "
"a: Oppervlakte van een rechthoek"
"b: Oppervlakte van een cirkel"
"c: (etc...)
"elk andere input: stop het programma"
"Kies de juiste letter: "
in: a
out: "Wat is de lengte van de rechthoek?"
in: 5
out: "Wat is de breedte van de rechthoek?"
in: 8
out: "De oppervlakte van deze rechthoek is 40."
"Wat moet er berekent worden. Geeft het getal "
"a: Oppervlakte van een rechthoek?"
"b: Oppervlakte van een cirkel?"
...
"elk andere input: stop het programma"
"Kies de juiste letter: "
in: s
out: "s is geen juiste optie, programma stopt"
```

## Opdracht 1

a. Maak een nieuw bestand `wk3co1.py` met de lege functies `menu()` en `testing()`. Zet bovenaan `import math` zodat je toegang hebt tot de math library, including math.pi
b. Schrijf een functie `rechthoekOpp(lengte, breedte)` dat twee getallen accepteert en de oppervlakte van een rechthoek teruggeeft
c. Schrijf een functie `cirkelOpp(radius)` dat een getal accepteerd en de oppervlakte van een cirkel teruggeeft.
d. Schrijf een functie `cirkelOmtrek(radius)` dat een getal accepteerd en de omtrek van een cirkel teruggeeft.
e. Schrijf een functie `driehoekOpp(basis, hoogte)` dat twee getallen accepteert en de oppervlakte van een driehoek berekent.


## Opdracht 2


a. Schrijf een functie `balkInhoud(lengte, breedte, hoogte)` dat drie getallen accepteert en de inhoud van een balk teruggeeft. Maak gebruik van je `rechthoekOpp` functie.
b. Schrijf een functie `cilinderInhoud(radius, hoogte)` dat twee getallen accepteert en de inhoud van een cilinder teruggeeft. Maak gebruik van je `cirkelOpp` functie.
c. Schrijf een functie `piramideInhoud(lengte, breede, hoogte)` dat twee getallen accepteert en de inhoud van een piramide terugggeeft. Maak gebruik van je `rechthoekOpp` functie.

## Opdracht 3

a. Schrijf een functie `balkOpp(lengte, breedte, hoogte)` dat drie getallen accepteert en de oppervlakte van een balk teruggeeft. Maak gebruik van je `rechthoekOpp` functie.
b. Schrijf een functie `cilinderOpp(radius, hoogte)` dat twee getallen accepteert en de oppervlakte van een cilinder teruggeeft. Maak gebruik van je `cirkelOmtrek`, `rechthoekOpp` en `cirkelOpp` functies.

## Opdracht 4

Schrijf een functie `menu()`. Deze functie print alle opties dat de rekenmachine kan uitrekenen en vraagt de gebruiker voor input om een optie te kunnen selecteren. Selecteert de gebruiker een juiste optie, dan wordt er gevraagd om de data in te voeren. Je mag er vanuit gaan dat de gebruiker de juiste data invoert (dus getallen en geen strings).  Zodra alle data bekend is wordt de juiste functie aangeroepen om de berekening uit te voeren. Als de gekozen optie niet bestaat, sluit het programma zich af. Maak gebruik van recursie om menu te herhalen. (en dus niet for of while lussen)

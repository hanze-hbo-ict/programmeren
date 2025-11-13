---
title: Recursieve functies
file: wk3ba2.py
---

# Recursieve functies

Deze opgave bestaat uit het maken van verschillende functies **zonder** gebruik te maken van lussen. Vergeet niet elke functie te testen met assertions en vergeet de docstrings niet.

## Opdracht 1

Schrijf een functie `no_doubles(l)`die een lijst `l` accepteert, alle dubbele waarden verwijdert uit `l` en deze nieuwe lijst teruggeeft.

Voorbeelden

```python
no_doubles("test") == "est"
no_doubles([1, 2, 3, 3, 4, 5]) == [1, 2, 3, 4, 5]
```

## Opdracht 2

In de wiskunde komen de orders UNION, INTERSECT en EXCEPT voor dat op twee lijsten uitgevoerd kan worden.

UNION houdt in dat alle informatie uit twee lijsten samengevoegd worden tot 1 lijst, zonder dubbele waardes
INTERSECT houdt in dat enkel de informatie die in beide lijsten voorkomen in een nieuwe lijst worden geplaats
EXCEPT houdt in dat enkel de informatie dat uniek in lijst a en dus niet in lijst b voorkomt in een nieuwe lijst wordt geplaatst.

a.	Schrijf een functie `intersect_sets(a, b)` dat twee lijsten `a` en `b` binnen krijgt als paramaters. De functie geeft een lijst terug met elementen die zowel in lijst `a` als in lijst `b` voorkomt.


```python
intersect([1, 2, 3], [3, 4, 5]) == [3]
```

b.	Schrijf een functie `except_sets(a, b)` dat twee lijsten `a` en `b` binnen krijgt als paramaters De functie geeft een lijst terug met alle elementen van `a` die niet in `b` voorkomen.

```python
except_sets([1, 2, 3], [3, 4, 5]) == [1, 2]
```

c.	Schrijf een functie `union_sets(a, b)` dat twee lijsten `a` en `b` binnen krijgt als paramaters. De functie geeft de union terug van deze twee lijsten.

Voorbeeld
```python
union_sets([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 4, 5]
```

## Opdracht 3
De grootste gemene deler tussen twee getallen is de grootste deler die beide getallen gemeenschappelijk hebben. Doel is om een programma te maken dat de ggd kan berekenen. Dit gaan we stap voor stap doen.

a. Schrijf de functie `fact(number, counter=1)` dat twee integers `number` en `counter` accepteert. De functie verzamelt alle delers van het gegeven `number` en geeft deze allemaal terug in een lijst. De `counter` start automatisch op 1 en kan gebruikt worden om de delers van `number` te vinden.

Voorbeelden
```python
fact(24) = [1, 2, 3, 4, 6, 8, 12, 24]
fact(15) = [1, 3, ,5, 15]
```

b. Schrijf de functie `ggd(a, b)` dat twee integers `a` en `b` ontvangt en de ggd teruggeeft.

**Tips:**
1. Gebruik de `fact` functie om de delers van beide getallen te vinden
2. Gebruik de `intersect` functie om alle gemeenschappelijke delers te vinden, aka, alle delers die in beide lijsten zitten.
3. Geeft de hoogste waarde van de intersect lijst terug.

c. Een andere aanpak voor het vinden van de ggd is de het euclides algoritme.

1.	Noem het grootste van de beide getallen m, het andere n.
2.	r = m % n
3.	Wanneer r gelijk is aan 0, geef n terug.
4.	Zo niet, herhaal dan het algoritme met n en r.


ggd van 900 en 1140

1140 % 900 = 240<br/>
900 % 240 = 180<br/>
240 % 180 = 60<br/>
180 % 60 = 0<br/>

ggd is 60.


Schrijf de functie `euclides(a, b)` dat twee integers `a` en `b` accepteert en via het euclides algoritme de ggd berekent en teruggeeft.

d. Schrijf in een comment onderaan het bestand welke methode jij beter vindt en waarom.

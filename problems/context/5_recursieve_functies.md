---
title: Recursieve functies
file: wk3co1.py
---

# Recursieve functies

Maak bij onderstaande opdrachten **geen** gebruik van lussen (for of while).

## Opdracht 1

**Bubblesort**

Bubblesort is een algoritme om een lijst te sorteren op volgorde. Bubblesort begint met het doorlopen van de te sorteren rij van n elementen en vergelijk elk element met het volgende. Als ze in de verkeerde volgorde staan worden ze gewisseld en wordt er een stukje opgeschoven. Zodra dat één keer gebeurt is zal het hoogste getal achteraan staan. Nu wordt opnieuw de rij doorlopen en dit wordt dus net zoals herhaald totdat alle elementen goed staan. We zien de grotere elementen als het ware als luchtbellen naar boven drijven. Aan deze metafoor ontleent het algoritme zijn naam.

[Bubblesort Video](https://www.youtube.com/watch?v=aXXWXz5rF64&t=0s)

Schrijf de functie bubblesort(l) dat een lijst 'l' accepteert, deze via het bubblesort algoritme sorteert van klein naar groot, en de gesorteerde lijst teurggeeft.

**tips**

* Schrijf een hulpfunctie dat de lijst 1 keer doorloopt, met andere woorden, vergelijk elk element met het volgende. Als ze in de verkeerde volgorde staan worden ze gewisseld en wordt er een stukje opgeschoven.
* schrijf een hulpfunctie dat controleert of de lijst op volgorde staat, zo ja, stop de functie bubblesort, zo niet, start de bubblesort opnieuw om de lijst opnieuw te doorlopen.

## Opdracht 2

**Mergesort**

De gedachte achter mergesort is dat twee gesorteerde rijen kunnen worden samengevoegd tot één gesorteerde rij door steeds de twee eerste elementen te bekijken, de kleinste element eruit halen en op te slaan en vervolgens weer de volgend twee bekijken.

De sorteeralgoritme bestaat dan uit het herhaaldelijk in twee gelijke (of bijna gelijke) delen splitsen van een rij, tot dat er enkel nog maar rijen van 1 lang zijn en vervolgens de twee gesorteerde rijen samen te voegen.


[Mergesort Video](https://www.youtube.com/watch?v=es2T6KY45cA&t=0s)

Schrijf de functie `mergesort(l)` die een lijst `l` accepteert, deze via het *mergesort* algoritme sorteert van klein naar groot, en de gesorteerde lijst teruggeeft.

**Tip**
Schrijf een hulp functie merge dat twee gesorteerde lijsten accepteert en samenvoegt tot één gesorteerde lijst.

## Opdracht 3

Vergelijk beide sorteer algoritmes. Welke is efficiënter en waarom? Zat je antwoord onderaan je bestand in comments.

# De macht van Hmmm!

(15 punten; bestandsnaam: `wk7ex2.hmmm`)

In deze opgave maak je een Hmmm-programma in het bestand genaamd `wk7ex2.hmmm` in de map die je gedownload hebt voor het practicum.

Zorg dat je dit bestand `wk7ex2.hmmm` in *dezelfde* map `wk7ex1` laat staan, omdat je de andere bestanden daarin nodig hebt!

Je programma moet eerst **twee** niet-negatieve getallen vragen van de gebruiker. Daarna moet het programma het resultaat berekenen als je de eerste invoer tot de macht van de tweede invoer verheft. Daarna moet het dat resultaat printen en `halt`en.

Aangezien het tweede faculteitvoorbeeld in het college recursief was, maar deze opgave over lussen gaat, kan je beter het ***eerste** faculteitvoorbeeld dat in het college behandled is gebruiken als richtlijn hoe je programma moet werken. Hier is dat voorbeeld uit het college:

```text
00 read   r1         # Plaats getal van de gebruiker in r1
01 setn   r2 1       # Zet het resultaat in r2
02 jeqzn  r1 08      # Spring naar regel 7 als r1 == 0
03 mul    r2 r2 r1   # Laat r2 = r2 * r1
04 addn   r1 -1      # Laat r1 = r1 - 1
05 jumpn  02         # Spring terug naar regel 2
06 nop
07 nop
08 write  r2         # Druk het resultaat in r2 af
09 halt
```

Dit is geen oplossing voor dit probleem! Onthoud dat je dit programma moet aanpassen om een macht, geen faculteit, te berekenen.

:::{admonition} Machtsverheffen in Hmmm
:class: tip

* Gebruik het bestaande `read`-statement om het grondtal te vragen aan de gebruiker.
* Voeg nog een `read`-statement toe om de macht te op te vragen en op te slaan, bijvoorbeeld in `r2`.
* *Laat 1 nog steeds je initiële resultaat zijn! (het "basisgeval")* Gebruik bijvoorbeeld `r3`.
* ***Test*** daarna of je klaar bent!
* Je bent waarschijnlijk klaar als de macht gelijk is aan 0
* Als je nog niet klaar bent, moet je één keer vermenigvuldigen, de macht verlagen en lussen!
:::

Bij deze opgave mag je ervanuit gaan dat beide invoer waardes op zijn minst 0 zijn. De berekening van 0 tot de macht 0 (of een ander getal tot de nulde macht) moet `1` opleveren. Hier zijn een paar series in- en uitvoerwaardes als voorbeeld:

```text
Enter number: 2
Enter number: 5
32

Enter number: 42
Enter number: 1
42

Enter number: 42
Enter number: 0
1

Enter number: 0
Enter number: 0
1
```

Onthoud dat je voor elke regel code minimaal één regel commentaar moet schrijven waarin je uitlegt wat die regel doet. Test bovendien je programma zorgvuldig, sowieso in de "randgevallen" waar één of beide invoerwaardes nul is.

Lever daarna je bestand `wk7ex2.hmmm` in Gradescope in.

# ASCII Art

| Naam         | Beschrijving                                                   |
|--------------|----------------------------------------------------------------|
| Onderwerp    | Creatief met ASCII                                             |
| Bestandsnaam | `wk8ex5.py`                                                    |
| Inleveren    | Lever jouw bestand met de juiste bestandsnaam in op GradeScope |
| Opmerking    | **Dit is een bonusopgave**                                     |

In deze opgave bekijk je een klassieke kunstvorm: ASCII art!

Er zijn vijf opgaves: de eerste twee zijn ieder 1 punt waard, en de andere drie zijn ieder 2 punten waard.

De opgave `print_crazy_striped_diamond` is nog eens een extra 5 punten waard; deze is echter wel *gestoord*...

:::{admonition} Belangrijke beperking!
:class: warning
In deze opgave mag je de string-vermenigvuldig- en string-opteloperatoren **niet** gebruiken. Omdat ons doel is om lusconstructies te gebruiken, moet je lussen gebruiken om te herhalen, ook als het met deze operatoren korter zou kunnen. Hier is één uitzondering op, echter; je **mag** string-vermenigvuldiging gebruiken met het spatieteken `" "`. Dat wl zeggen, je mag een aantal opeenvolgende spaties maken met constructies als

```python
" "*5
```
:::

:::{admonition} Eerst ontwerpen!
:class: tip
De bedoeling van deze opgave is om je redeneervermogen over lussen en geneste lussen verder te vergroten. Voor veel van de opgaves (met name de gestreepte ruit) moet je zorgvuldig nadenken over de waarde van je luscontrolevariabele tijdens het uitvoeren van je lus of lussen. "Debuggen door willekeurige wijzingingen"; dat wil zeggen, je luscondities of variabelen willekeurig wijzigen; zal tot veel frustratie leiden. De oplossing is om goed na te denken over je lussen!
:::

## De functie `print_rect`

Schrijf een functie met de naam `print_rect` die drie argumenten meekrijgt, `width`, `height` en `symbol`, en een vierkant van `width` bij `height` met `symbol`en afdrukt op het scherm.

```ipython
In [1]: print_rect(4, 6, "%")
% % % %
% % % %
% % % %
% % % %
% % % %
% % % %
```

:::{admonition} Dit is op het college behandeld
:class: tip
Als je de slides over geneste lussen bekijkt, zul je zien dat deze opgave behandeld is! De enige verschillen zijn dat

-   De breedte een variabele is, in plaats van een constante
-   De hoogte een variabele is, in plaats van een constante
-   Het af te drukken teken een variabele is, in plaats van een constante
:::

## De functie `print_triangle`

Schrijf een functie `print_triangle` die drie argumenten meekrijgt: `width`, `symbol` en `right_side_up`, en een driehoek van symbolen op het scherm afdrukt. `width` is een getal die de breedte van de basis van de driehoek bepaalt en `right_side_up` is een boolean die bepaalt of de driehoek met de punt naar boven (`True`) of naar onder (`False`) moet worden afgedrukt.

```ipython
In [1]: print_triangle(3, "@", True)
@
@ @
@ @ @

In [2]: print_triangle(3, "@", False)
@ @ @
@ @
@
```

## De functie `print_bumps`

Gebruik nu je functie `print_triangle` om een functie genaamd `print_bumps(num, symbol1, symbol2)` te schrijven die het gegeven aantal "heuvels" van twee symbolen afdrukt, waarbij elke heuvel groter is dan de volgende, zoals in het volgende voorbeeld:

```ipython
In [1]: print_bumps(4, "%", "#")
%
#
%
% %
# #
#
%
% %
% % %
# # #
# #
#
%
% %
% % %
% % % %
# # # #
# # #
# #
#
```

## De functie `print_diamond`

Voor deze "ruit"-functies **mag** je string-vermenigvuldiging gebruiken, maar alleen voor strings van spaties, zoals `' ' * n` en dergelijke. Elk zichtbaar karakter moet **afzonderlijk** afgedrukt worden, net zoals in de functies eerder in de opgave. Het is echter **niet verplicht** om de operator `*` niet gebruiken voor strings van spaties.

Schrijf een functie `print_diamond(width, symbol)` die een ruit met `symbol`en afdrukt waarvan de maximale breedte bepaald wordt door `width`.

```ipython
In [1]: print_diamond(3, "&")
   &
  & &
 & & &
  & &
   &
```

## De functie `print_striped_diamond`

Schrijf nu een functie genaamd `print_striped_diamond(width, sym1, sym2)` die een "gestreepte ruit" van `sym1` en `sym2` afdrukt.

Bijvoorbeeld:

```ipython
In [1]: print_striped_diamond(7, ".", "%")
      .
     . %
    . % .
   . % . %
  . % . % .
 . % . % . %
. % . % . % .
 % . % . % .
  . % . % .
   % . % .
    . % .
     % .
      .
```

## De functie `print_crazy_striped_diamond`

Schrijf ten slotte (en dit is 5 punten waard *bovenop* de 8 voor de vorige figuren) een functie genaamd `print_crazy_striped_diamond(width, sym1, sym2, sym1_width, sym2_width)` die een "gestreepte ruit" van `sym1` en `sym2` afdrukt waarbij de strepen verschillende breedtes kunnen hebben. `sym1_width` bepaalt de breedte van de streep gemaakt van symbool 1 en `symWidth2` bepaalt de breedte van de streep gemaakt van symbool 2.

Bijvoorbeeld:

```ipython
In [1]: print_crazy_striped_diamond(7, ".", "%", 2, 1)
      .
     . .
    . . %
   . . % .
  . . % . .
 . . % . . %
. . % . . % .
 . % . . % .
  % . . % .
   . . % .
    . % .
     % .
      .
```

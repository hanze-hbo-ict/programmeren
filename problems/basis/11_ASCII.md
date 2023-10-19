# ASCII Art


In deze opgave bekijk je een klassieke kunstvorm: ASCII art!

Er zijn vijf opgaves. De opgave `print_crazy_striped_diamond` is een uitdaging, deze is echter wel *gestoord*...

:::{admonition} Belangrijke beperking!
:class: warning
In deze opgave mag je de string-vermenigvuldig- en string-opteloperatoren **niet** gebruiken. Omdat ons doel is om lusconstructies te gebruiken, moet je lussen gebruiken om te herhalen, ook als het met deze operatoren korter zou kunnen. Hier is één uitzondering op, echter; je **mag** string-vermenigvuldiging gebruiken met het spatieteken `" "`. Dat wl zeggen, je mag een aantal opeenvolgende spaties maken met constructies als

```python
" "*5
```
:::

De print functie print automatisch new line aan het einde van een output. We kunnen ook aangeven dat dit niet hoeft door specifiek aan te geven wat het einde van de zin moet zijn. 

voorbeeld:
```python
print("hello", end= " ")
print("world")
``` 
output = hello world


:::{admonition} Eerst ontwerpen!
:class: tip
De bedoeling van deze opgave is om je redeneervermogen over lussen en geneste lussen verder te vergroten. Voor veel van de opgaves (met name de gestreepte ruit) moet je zorgvuldig nadenken over de waarde van je luscontrolevariabele tijdens het uitvoeren van je lus of lussen. "Debuggen door willekeurige wijzingingen"; dat wil zeggen, je luscondities of variabelen willekeurig wijzigen; zal tot veel frustratie leiden. De oplossing is om goed na te denken over je lussen!
:::

## Opdracht 1: `print_rect`

Schrijf een functie met de naam `print_rect` die drie argumenten meekrijgt, `width`, `height` en `symbol`, en een vierkant van `width` bij `height` met `symbol`en afdrukt op het scherm.

```ipython
In: print_rect(4, 6, "%")
% % % %
% % % %
% % % %
% % % %
% % % %
% % % %
```


## Opdracht 2: `print_triangle`

Schrijf een functie `print_triangle` die drie argumenten meekrijgt: `width`, `symbol` en `right_side_up`, en een driehoek van symbolen op het scherm afdrukt. `width` is een getal die de breedte van de basis van de driehoek bepaalt en `right_side_up` is een boolean die bepaalt of de driehoek met de punt naar boven (`True`) of naar onder (`False`) moet worden afgedrukt.

```ipython
In: print_triangle(3, "@", True)
@
@ @
@ @ @

In: print_triangle(3, "@", False)
@ @ @
@ @
@
```

## Opdracht 3: `print_bumps`

Gebruik nu je functie `print_triangle` om een functie genaamd `print_bumps(num, symbol1, symbol2)` te schrijven die het gegeven aantal "heuvels" van twee symbolen afdrukt, waarbij elke heuvel groter is dan de volgende, zoals in het volgende voorbeeld:

```ipython
In: print_bumps(4, "%", "#")
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

## Opracht 4:  `print_diamond`

Voor deze "ruit"-functies **mag** je string-vermenigvuldiging gebruiken, maar alleen voor strings van spaties, zoals `' ' * n` en dergelijke. Elk zichtbaar karakter moet **afzonderlijk** afgedrukt worden, net zoals in de functies eerder in de opgave. Het is echter **niet verplicht** om de operator `*` niet gebruiken voor strings van spaties.

Schrijf een functie `print_diamond(width, symbol)` die een ruit met `symbol`en afdrukt waarvan de maximale breedte bepaald wordt door `width`.

```ipython
In: print_diamond(3, "&")
   &
  & &
 & & &
  & &
   &
```

## Opdracht 5:  `print_striped_diamond`

Schrijf nu een functie genaamd `print_striped_diamond(width, sym1, sym2)` die een "gestreepte ruit" van `sym1` en `sym2` afdrukt.

Bijvoorbeeld:

```ipython
In: print_striped_diamond(7, ".", "%")
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

## Opdracht 6:  `print_crazy_striped_diamond`

Schrijf ten slotte (en dit is 5 punten waard *bovenop* de 8 voor de vorige figuren) een functie genaamd `print_crazy_striped_diamond(width, sym1, sym2, sym1_width, sym2_width)` die een "gestreepte ruit" van `sym1` en `sym2` afdrukt waarbij de strepen verschillende breedtes kunnen hebben. `sym1_width` bepaalt de breedte van de streep gemaakt van symbool 1 en `sym2_width` bepaalt de breedte van de streep gemaakt van symbool 2.

Bijvoorbeeld:

```ipython
In: print_crazy_striped_diamond(7, ".", "%", 2, 1)
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

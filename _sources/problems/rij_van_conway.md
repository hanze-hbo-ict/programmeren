# De Rij van Conway

| Naam         | Beschrijving                                                   |
|--------------|----------------------------------------------------------------|
| Onderwerp    | Lees en zeg, of lees en huiver                                 |
| Bestandsnaam | `wk9ex3.py`                                                    |
| Inleveren    | Lever jouw bestand met de juiste bestandsnaam in op GradeScope |

## De Rij van Conway of Lees-en-Huiver

In deze opgave ga je de wiskundig interessante [Rij van Conway](https://nl.wikipedia.org/wiki/Rij_van_Conway) (ja, dezelfde Conway!), ook wel bekend onder de Engelse naam Look-and-Say, implementeren. Je code moet in een bestand met de naam `wk9ex3.py` gezet worden.

Dit is een vreemde wiskundige rij die als volgt begint:

```
1, 11, 21, 1211, 111221, 312211, 13112221, ...
```

Wat is het patroon? Het begint met 1. Als we die 1 zien, zeggen we "Ik zie één 1". Het volgende nummer in de rij is dus "één éen" of 11. Als we 11 zien, zeggen we "Ik zie twee enen". He volgende nummer in de rij is dus 21 (twee één). Nu kijken we naar dat nummer en zeggen we "Ik zie één twee en één één", dus het volgende nummer in de rij is 1211 (één twee één één). En zo verder!

De taak in deze opgave is om een programma te maken dat het volgende nummer in de rij afdrukt, *beginnend bij **elke** beginwaarde!*

Deze opgave is anders dan veel andere opgaven omdat *je het ontwerp helemaal zelf mag bepalen*! Je kan overwegen

* Een hulpfunctie te schrijven (of meerdere!)
* Welke soorten lussen je nodig hebt (`for` of `while`)
* Je mag ook best recursie gebruiken (het kan net zo goed met recursie gedaan worden...)

Je gaat de functie `next` daarna gebruiken om zoveel getallen te genereren als je wilt...

## De functie `next`

De hoofdfunctie die je schrijven is dus `next(term)`. De details:

* `term` moet een willekeurige integer zijn
* de functie `next` moet het volgende "gelezen" getal teruggeven; dit moet een `int` zijn, gebaseerd op de ingevoerde `term`

Nogmaals, het ontwerp mag je zelf bepalen. Hier zijn een paar voorbeelden die we zullen testen; er zullen er nog een paar meer zijn! Zorg dat je genoeg asserts opneemt in je code!

```ipython
In [1]: next(21)
Out[1]: 1211

In [2]: next(2222)   # merk op dat dit getal niet voorkomt in de echte rij
Out[2]: 42

In [3]: next(312211)
Out[3]: 13112221
```

:::{admonition} Waarschuwing
:class: danger

Je functie `next` moet een `int` als uitvoer geven! (Anders kom je niet door onze controle!) Gebruik `int(s)` als je dat nodig hebt!!
:::

:::{admonition} Tips
:class: tip

* Je kan een integer `x` naar een string omzetten, bijvoorbeeld met `str(x)`
* Je kan een string `s` naar een integer omzetten, bijvoorbeeld met `int(s)`
* `next` moet een integer (`int`) teruggeven, maar onthoud dat je met deze twee functies van en naar strings kan converteren!
:::

## Lees-en-Huiver

Schrijf nu een functie met de naam `read_it(n)` die de eerste `n` getallen in de Lees-en-Huiver-rij afdrukt: één per regel, te beginnen met een `1`. Deze functie `read_it` is ongebruikelijk omdat deze *geen* waarde hoeft terug te geven: ze wordt alleen gebruik om dingen af te drukken.

Hier is een voorbeeld van de uitvoer van `read_it(n)`...

```ipython
In [1]: read_it(6)
1
11
21
1211
111221
312211
```

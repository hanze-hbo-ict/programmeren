# Wisselende stelsels

| Naam         | Beschrijving                                                   |
|--------------|----------------------------------------------------------------|
| Onderwerp    | Getallen omzetten naar verschillende grondtallen               |
| Bestandsnaam | `wk6co1.py`                                                    |
| Inleveren    | Lever jouw bestand met de juiste bestandsnaam in op GradeScope |

## De functie `lingo(s, t)`

Schrijf een functie `lingo(s, t)` die twee strings `s` en `t` accepteert en een integer teruggeeft, de zogenaamde "[Lingo](https://nl.wikipedia.org/wiki/Lingo)-telling, of -score, waar `s` wordt vergeleken met `t`.

De Lingo-score is het aantal tekens in `s` dat ook voorkomt in `t`. Herhaalde letters tellen vaker, mits ze vaker voorkomen in beide strings, hoe dit werkt wordt duidelijker in de onderstaande voorbeelden. Je hoeft er bij deze functie geen rekening mee
te houden of de letters op dezelfde plek staan. Merk op dat alhoewel Lingo traditioneel gespeeld wordt met woorden van 5 (of 6) letters, de lengte van de woorden in deze functie niet beperkt is!

<!-- TODO wordt verwezen naar handige hulpfuncties behandeld in college, welke? -->

Er zijn meerdere manieren om dit probleem op te lossen, een aantal daarvan gebruikt kleinere hulpfuncties. Het staat je vrij om
zulke hulpfuncties toe te voegen als je dat handig vindt. Het zou kunnen dat je al nuttige hulpfuncties bent tegengekomen die hier van toepassing kunnen zijn. Het gebruik van lussen is niet toegestaan. 

Merk op dat als `s` of `t` een lege string is, de Lingo-score `0` moet zijn!

:::{admonition} Wel of niet
:class: tip

Op enig moment zul je moeten testen of een karakter zich wel of niet in een string bevindt. De regel `if s[0] in t:` zou een handige test kunnen zijn!
:::

Een paar voorbeelden:

```ipython
In [1]: lingo('diner', 'proza')  # alleen de 'r'
Out[1]: 1

In [2]: lingo('beeft', 'euvel')  # twee 'e's zijn gedeeld
Out[2]: 2

In [3]: lingo('gattaca', 'aggtccaggcgc') # 2 'a's, 1 't', 1 'c', 1 'g'
Out[3]: 5

In [4]: lingo('gattaca', '') # geef 0 terug bij een lege string
Out[4]: 0
```
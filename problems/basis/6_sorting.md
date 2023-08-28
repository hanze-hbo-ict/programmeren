# Caesar op orde!

| Naam         | Beschrijving                                                   |
|--------------|----------------------------------------------------------------|
| Onderwerp    | Taal ontcijferen                                               |
| Bestandsnaam | `wk6ba2.py`                                                    |
| Inleveren    | Lever jouw bestand met de juiste bestandsnaam in op GradeScope |

In deze opgave ga je een aantal functies schrijven met behulp van *functioneel programmeren*, dat wil zeggen, conditionele statements, recursie en/of list comprehensions.

Zorg bij elke opdracht dat je de naam precies zo schrijft zoals dit wordt opgegeven, inclusief hoofd-en kleine letters. Voeg verder aan elke functie een *docstring* toe waar je kort uitlegt wat de argumenten van de functie zijn en wat de functie doet.



## Opdracht 1:  `blsort(L)`

Schrijf een functie `blsort(L)` die als argument een lijst `L` accepteert en een lijst teruggeeft met dezelfde elementen als `L`, maar in oplopende volgorde. (Let op: het tweede teken van de functienaam is een "el" voor "lijst", niet een 1 (één) of een "i"!)

`blsort` hoeft alleen maar lijsten met *binaire cijfers* te sorteren, dat wil zeggen, deze functie mag en moet ervan uitgaan dat `L` altijd een lijst met alleen `0`'en en `1`'en is.

Je mag de ingebouwde Python functie `sort` niet gebruiken om dit probleem op te lossen! Je mag ook je zelfgeschreven sorteerfunctie (deze wordt later gevraagd) niet gebruiken.

Verder mag je elke andere functionele techniek gebruiken om `blsort` te implementeren. In het bijzonder is het handig te bedenken hoe je gebruik kan maken van de beperking dat het argument `L` een binaire lijst is, dit is een belangrijke beperking!

Een functie die sommigen handig vinden is `count(e, L)`, een hulpfunctie die je eerder al hebt gezien. 

Voeg `count(e, L)` toe aan jouw bestand toevoegen, en dan kun je deze functie gebruiken om te kijken hoe vaak `e` voorkomt in `L`.

Hier zijn een paar voorbeelden:

```ipython
In [1]: blsort([1, 0, 1])
Out[1]: [0, 1, 1]

In [2]: L = [1, 0, 1, 0, 1, 0, 1]

In [3]: blsort(L)
Out[3]: [0, 0, 0, 1, 1, 1, 1]
```

:::{admonition} Binaire eenvoud
:class: notice

Maak gebruik van het feit dat de lijst `L` alleen maar `0` of `1` kan bevatten. Als je het aantal 0-en weet, hoeveel 1-en zijn er dan....
```python
5 * [0] == [0, 0, 0, 0, 0]
```
:::


## Opdracht 2 `selectionSort(L)`

We gaan een lijst sorteren met een zogenaamde selection sort. We zoeken eerst het kleinste element in de lijst, zetten deze vooraan. Daarna verwijderen we deze uit de lijst en zoeken dan weer de kleinste in deze nieuw lijst. 

a. Schrijf de funtie `rem_one(L, e)` dat een lijst `L` accepteer en element `e` en vervolgens  èèn keer `e` verwijdert uit `L` en deze nieuwe lijst teruggeeft.   

b. Gebruik recursie om een algemene sorteerfunctie `selectionSort(L)` te schrijven die een lijst `L` accepteert en een lijst teruggeeft met dezelfde elementen als `L`, maar in *oplopende* volgorde. Je kan hiervoor de ingebouwde Python functie `max` (of `min`, als je deze liever hebt) gebruiken, en de functie `rem_one`. 

Bij deze opgave mag je de in Python ingebouwde sorteer functies zoals `sorted(L)` en `L.sort()` **niet** gebruiken. Je moet zelf een aanpak bedenken en implementeren! Let verder op dat `selectionSort(L)` moet werken voor *lijsten* `L`, het hoeft **niet** te werken voor strings.

Je ziet hier een paar voorbeelden:

```ipython
In [1]: selectionSort([42, 1, 3.14])
Out[1]: [1, 3.14, 42]

In [2]: L = [7, 9, 4, 3, 0, 5, 2, 6, 1, 8]

In [3]: selectionSort(L)
Out[3]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
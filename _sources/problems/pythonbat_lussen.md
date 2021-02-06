# Lussen in PythonBat!

```{include} ../class/problems/pythonbat_lussen.md
```

In deze opgave ga je oefenen met de lussen van Python: `for` en `while`.

Er staan 12 lusproblemen op de twee PythonBat-pagina's:

* Zes "medium list problems" om lussen te gebruiken op [http://codingbat.com/python/List-2]
* Zes "medium python string problems" om lussen te gebruiken op [http://codingbat.com/python/String-2]

Als je bijvoorbeeld de pagina met ["medium python string problems"](http://codingbat.com/python/String-2) opent, zie je dat het eerste probleem `double_char` heet. De pagina zegt

> Given a string, return a string where for every char in the original, there are two chars.
>
> ```
> double_char('The') → 'TThhee'
> double_char('AAbb') → 'AAAAbbbb'
> double_char('Hi-There') → 'HHii--TThheerree'
> ```

Het leuke aan de PythonBat-pagina's is dat ze je code meteen controleren.

Hier is een compleet en correct antwoord voor `double_char`:

```python
def double_char(str):
    result = ''
    for c in str:
        result += c*2
    return result
```

Je mag dit overtypen, of plakken, en controleren dat de tests werken.

Zorg dat je de ***strategie*** voor deze oplossing voor `double_char` begrijpt:

* We beginnen met een verzamelvariabele met een geschikte startwaarde
    * Hier is dat de variabele `result`, die begint op de waarde `''` (de lege string)
* We schrijven een lus die het gewenste resultaat verzamelt
* Daarna geven we het resultaat terug

:::{admonition} Je hoeft geen docstrings of asserts te schrijven!
:class: notice

***ALLEEN*** voor deze opgave voor lussen in PythonBat hoef je geen docstrings en asserts te maken. Ze zijn puur ter oefening.
:::

Nu de details...

## Los vijf PythonBat-opgaves naar keuze op

Voor deze opgave moet je vijf PythonBat-opgaves naar keuze van de twee pagina's die hierboven genoemd zijn oplossen.

* Noem de functies zoals door PythonBat gevraagd wordt
* Kopieer je werkende en geteste functies in een bestand met de naam `wk8ex2.py`
* Je hoeft geen docstrings of asserts toe te voegen aan deze functies
* Je functies moeten wel een `for`- of `while`-lus gebruiken!

Lever dan je bestand `wk8ex2.py` in in Gradescope en je bent klaar!

## Bonusopgave: Los de andere opgaves ook op!

Je kan voor 6 bonuspunten de andere zes problemen ook oplossen.

We kijken ze alle 11 na, maar de score is gebaseerd op 5 punten.

Het resultaat hiervan is dat alle functies die je buiten deze vijf oplost tellen als bonuspunten. Ze zijn bovendien een goede oefening om met lussen in Python te leren werken...

Succes met deze opgaves! De twee volgende huiswerkopgaves laten uitgebreidere *toepassingen* van Pythonlussen zien.

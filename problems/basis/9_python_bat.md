# Lussen in PythonBat!

In deze opgave ga je oefenen met de lussen van Python: `for` en `while`.

Er staan 12 lusproblemen op de twee PythonBat-pagina's:

* Zes "medium list problems" om lussen te gebruiken op [CodingBat](http://codingbat.com/python/List-2)
* Zes "medium python string problems" om lussen te gebruiken op [CodingBat](http://codingbat.com/python/String-2)

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


Maak alle 12 oefeningen. De gemaakte code kan je kopieren naar een python bestand om het te bewaren. 


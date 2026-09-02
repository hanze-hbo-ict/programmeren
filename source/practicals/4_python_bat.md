# Lussen in PythonBat

In dit werkcollege ga je oefenen met Python-lussen: `for` en `while`.

Er staan 12 lusproblemen op de twee CodingBat-pagina's:

* Zes "medium list problems" om lussen te gebruiken op [CodingBat](http://codingbat.com/python/List-2)
* Zes "medium python string problems" om lussen te gebruiken op [CodingBat](http://codingbat.com/python/String-2)

Als je bijvoorbeeld de pagina met ["medium python string problems"](http://codingbat.com/python/String-2) opent, zie je dat het eerste probleem `double_char` heet. De pagina zegt:

> Given a string, return a string where for every char in the original, there are two chars.
>
> ```text
> double_char('The') → 'TThhee'
> double_char('AAbb') → 'AAAAbbbb'
> double_char('Hi-There') → 'HHii--TThheerree'
> ```

Het voordeel van de CodingBat is dat het jouw code onmiddellijk controleert.

Hier is een compleet en correct antwoord voor `double_char`:

```python
def double_char(string):
    result = ""
    for char in string:
        result += char * 2
    return result
```

Deze oplossing volgt het [lusrecept](/lectures/4a_lussen.ipynb#het-lusrecept) uit het college. Ga na hoe:

1. de verzamelvariabele `result` begint op `''`, de lege string
2. we langs de karakters van `string` lopen, dus een `for` op element
3. er per stap `char * 2` bij komt
4. we klaar zijn als `string` op is
5. `return result` na de lus staat

## Opdracht

1. Maak alle 12 oefeningen op de CodingBat-website.
2. Kopieer de gemaakte code naar een Python-bestand om het te bewaren.
3. Probeer voor elke oefening de strategie te begrijpen en toe te passen.

## Tips

* Lees de probleemomschrijving zorgvuldig.
* Begin met het plannen van je aanpak voordat je begint met coderen.
* Test je code met de gegeven voorbeelden en probeer ook *edge cases* (bijzondere gevallen).
* Als je vastloopt, probeer het probleem op te delen in kleinere stappen.
* Vergelijk je oplossing met die van anderen nadat je klaar bent, om te leren van verschillende aanpakken.

## Conclusie

Door deze oefeningen te maken, zul je je vaardigheden in het werken met Python-lussen verbeteren. Veel succes!

# Lussen in PythonBat!

In dit werkcollege ga je oefenen met Python-lussen: `for` en `while`.

Er staan 12 lusproblemen op de twee CodingBat-pagina's:

* Zes "medium list problems" om lussen te gebruiken op [CodingBat](http://codingbat.com/python/List-2)
* Zes "medium python string problems" om lussen te gebruiken op [CodingBat](http://codingbat.com/python/String-2)

Als je bijvoorbeeld de pagina met ["medium python string problems"](http://codingbat.com/python/String-2) opent, zie je dat het eerste probleem `double_char` heet. De pagina zegt:

> Given a string, return a string where for every char in the original, there are two chars.
>
> ```
> double_char('The') → 'TThhee'
> double_char('AAbb') → 'AAAAbbbb'
> double_char('Hi-There') → 'HHii--TThheerree'
> ```

Het voordeel van de CodingBat is dat het jouw code onmiddellijk controleert.

Hier is een compleet en correct antwoord voor `double_char`:

```python
def double_char(str):
    result = ''
    for c in str:
        result += c*2
    return result
```

Zorg dat je de ***strategie*** voor deze oplossing voor `double_char` begrijpt:

1. We beginnen met een verzamelvariabele met een geschikte startwaarde
    * Hier is dat de variabele `result`, die begint met de waarde `''` (de lege string)
2. We schrijven een lus die het gewenste resultaat verzamelt
3. Daarna geven we het resultaat terug

## Opdracht

1. Maak alle 12 oefeningen op de CodingBat-website.
2. Kopieer de gemaakte code naar een Python-bestand om het te bewaren.
3. Probeer voor elke oefening de strategie te begrijpen en toe te passen.

## Tips

- Lees de probleemomschrijving zorgvuldig.
- Begin met het plannen van je aanpak voordat je begint met coderen.
- Test je code met de gegeven voorbeelden en probeer ook *edge cases* (bijzondere gevallen).
- Als je vastloopt, probeer het probleem op te delen in kleinere stappen.
- Vergelijk je oplossing met die van anderen nadat je klaar bent, om te leren van verschillende aanpakken.

## Conclusie

Door deze oefeningen te maken, zul je je vaardigheden in het werken met Python-lussen verbeteren. Veel succes!
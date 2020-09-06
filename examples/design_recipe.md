# Functie ontwerp

Een recept, of stappenplan voor het ontwerp van een functie[^pbd].

## Een probleem

Gegeven de formule voor de omzetting van een temperatuurmeting in graden Fahrenheit naar graden Celsius

$$^oC =  (^oF - 32) \cdot \frac{5}{9}$$

schrijf een functie met graden Fahrenheit als parameter en geef deze terug als graden Celsius waar graden Fahrenheit een *decimaal* getal is en graden Celsius een *decimaal* getal afgerond tot één cijfer achter de komma.

### Wat is de input

Bij elk probleem, vraag jezelf af wat de input van de functie is:

- is het in de vorm van argumenten (*parameters*) die aan de functie worden meegegeven;
- komt het van een gebruiker, bijvoorbeeld in de vorm ``name = input('Jouw naam: ')``;
- wordt het uit een bestand gelezen;
- of komt het van een apparaat als een muis, trackpad of sensor?

Bedenk dat een functie die "een waarde als input verwacht" vrijwel altijd een argument als input heeft en niet de functie [``input()``](https://docs.python.org/3/library/functions.html#input) zal aanroepen, een functie die invoer van een gebruiker zal vragen.

### Wat is de output

Wat moet met het resultaat van de functie gebeuren:

- wordt het teruggegeven met ``return`` (een *returnwaarde*);
- wordt het afgedrukt met [``print()``](https://docs.python.org/3/library/functions.html#print);
- wordt het naar een bestand geschreven;
- wordt het naar bijvoorbeeld een speaker, robot of andere machine op het internet verstuurd?

:::{admonition,info} Over input en output
Het beslissen of functies moeten worden ontworpen met parameters en returnwaarden, of met printinstructies of andere directe interacties, is een vraag die meer verdieping vereist dan in deze module kan worden aangeboden.

In de meeste gevallen zal het probleem je dus expliciet vertellen wat je moet doen (bv. "neem een getal als parameter en geef het terug als vierkantswortel" of "vraag de gebruiker om een getal in te voeren en vervolgens de vierkantswortel van dat getal af te drukken"). Lees het probleem altijd zorgvuldig door om deze belangrijke informatie te vinden.

In het algemeen is het aan te raden om elke functie met parameters en returnwaarden te schrijven. Dit maakt een functie flexibel, het programma dat het aanroept kan dan beslissen wat te doen met de returnwaarde (afdrukken, naar een robot sturen, of anders).
:::

## Stappenplan

1.  Schrijf de **signatuur** van de functie

    Hier schrijf je de *naam* van de functie en eventuele *parameters* die de functie accepteert. Vergeet niet te af te sluiten met een dubbele punt.

    ```python
    def fahrenheit_to_celsius(degrees):
    ```

2.  Bepaal het **type contract**

    Schrijf binnen een ingesprongen string met driedubbele aanhalingstekens (een [*docstring*](https://www.python.org/dev/peps/pep-0257/)) een *type contract* dat de naam en type van elke parameter identificeert. Kies een betekenisvolle naam voor elke parameter en identificeer ook het type van het resultaat van de functie (de *returnwaarde*). Bedenk dat een functie ook *niets* kan teruggeven, de returnwaarde is dan ``None``.

    ```{code-block} python
    ---
    emphasize-lines: 3, 4
    ---
    def fahrenheit_to_celsius(degrees):
        """
        :type degrees: float
        :rtype: float
        """
    ```

3.  Bedenk **voorbeelden**

    Schrijf een aantal voorbeelden hoe de functie kan worden aangeroepen en de returnwaarden die je verwacht. Begin elke aanroep van de functie met ``>>> `` en schrijf het resultaat op de volgende regel.

    ```{code-block} python
    ---
    emphasize-lines: 6, 7, 8, 9
    ---
    def fahrenheit_to_celsius(degrees):
        """
        :type degrees: float
        :rtype: float

        >>> fahrenheit_to_celsius(70.0)
        21.1
        >>> fahrenheit_to_celsius(32.0)
        0.0
        """
    ```

4.  Voeg een **beschrijving** toe

    Beschrijf direct achter de driedubbele aanhalingstekens van de docstring in één regel wat de functie *doet*.

    ```{code-block} python
    ---
    emphasize-lines: 2,
    ---
    def fahrenheit_to_celsius(degrees):
        """Convert degrees Fahrenheit to Celsius

        :type degrees: float
        :rtype: float

        >>> fahrenheit_to_celsius(70.0)
        21.1
        >>> fahrenheit_to_celsius(32.0)
        0.0
        """
    ```

    Indien nodig kan meer uitgebreide informatie worden toevoegd onder de beschrijving.

    ```{code-block} python
    ---
    emphasize-lines: 4, 5, 6
    ---
    def fahrenheit_to_celsius(degrees):
        """Convert degrees Fahrenheit to Celsius

        This function converts a Fahrenheit temperature reading as used
        in Anglo-Saxon countries to Celsius, a more common temperature
        measure scale. The result is rounded to a single decimal value.

        :type degrees: float
        :rtype: float

        >>> fahrenheit_to_celsius(70.0)
        21.1
        >>> fahrenheit_to_celsius(32.0)
        0.0
        """
    ```

5.  Schrijf de functie **body**

    Schrijf de hoofdtekst (de *body*) van de functie en let op dat de inspringing op hetzelfde niveau begint als de *docstring*. Lees weer de voorbeelden die je in *stap 3* hebt geschreven en denk terug aan hoe je tot de returnwaarden bent gekomen. Het kan handig zijn op dit moment meer voorbeelden te bedenken om er zeker van te zijn dat je in alle mogelijke gevallen tot een juiste returnwaarde komt.

    ```{code-block} python
    ---
    emphasize-lines: 20,21
    ---
    def fahrenheit_to_celsius(degrees):
        """Convert degrees Fahrenheit to Celsius

        This function converts a Fahrenheit temperature reading as used
        in Anglo-Saxon countries to Celsius, a more common temperature
        measure scale. The result is rounded to a single decimal value.

        :type degrees: float
        :rtype: float

        >>> fahrenheit_to_celsius(70.0)
        21.1
        >>> fahrenheit_to_celsius(32.0)
        0.0
        >>> fahrenheit_to_celsius(33.0) > 0.0
        True
        >>> fahrenheit_to_celsius(-10.0)
        -23.3
        """
        return round((degrees - 32) * 5/9, 1)
    ```

6.  **Test** de functie

    Test de functie voor alle voorbeelden die je hebt geschreven, inclusief extra voorbeelden die je in *stap 5* hebt bedacht. Als één of meerdere voorbeelden falen dan keer je terug naar *stap 5* en pas je de oplossing in de *body* aan.

    ```console
    $ python3 -m doctest mijn_bestand.py
    ```

    :::{admonition,warning} Uitvoeren van tests
    In dit voorbeeld wordt verondersteld dat jouw functie in het bestand ``mijn_bestand.py`` is geschreven.
    [TODO over doctest en test alternatieven. Wordt testen/debuggen integraal onderdeel van de module?]
    [doctest](https://docs.python.org/3/library/doctest.html)
    :::

[^pbd]: Het idee van *design recipes* voor programma's is gebaseerd op [Program By Design](https://programbydesign.org/)
# Van decimaal naar binair en verder!


Dit probleem gaat over het omzetten van getallen naar en van grondtal 10 (*decimaal*, wat de *meeste* mensen gebruiken) en van en naar grondtal 2 (*binair*, waar vrijwel alle computers mee werken).

Aan het einde van de opdracht zal je dit uitbreiden naar *ternair*, oftewel grondtal 3, waar minder computers en mensen, maar veel meer buitenaardse wezens mee werken!

## Opwarmen

### Opdracht 1: `is_odd(n)`

Als achtergrond voor dit probleem zullen we ons eerst gaan herinneren hoe we kunnen bepalen of de waarden in Python even of oneven zijn. Open eerst VSCode of een andere teksteditor en maak een nieuw bestand `wk6wc1.py` aan.

Schrijf dan een Python functie `is_odd(n)` die als argument een integer `n` accepteert, en  `True` teruggeeft als `n` oneven is en `False` als `n` even is. Zorg ervoor dat je deze (boolean) waarden teruggeeft, niet strings! De even- of onevenheid van een getal noemen we zijn *pariteit*.

Je moet de `%`-operator (de "modulo"-operator) gebruiken. Onthoud dat in Python `n % d` de rest na deling van `n` door `d` teruggeeft (als `n` >= 0). Hier zijn twee voorbeelden van het gebruik van `is_odd`:

```ipython
In [1]: is_odd(42)
Out[1]: False

In [2]: is_odd(43)
Out[2]: True
```

Hier zijn een paar tests:

```python
assert is_odd(42) == False
assert is_odd(43) == True
```

Als je liever kortere versies hebt van deze tests dan kan je de volgende gebruiken:

```python
assert not is_odd(42)
assert is_odd(43)
```

### Opdracht 2: `num_to_binary(n)`

In deze opdracht ga je getallen *bit voor bit* van decimaal naar binair omzetten, wat misschien "even" raar zal klinken...!

Kort samengevat, je gaat een functie `num_to_binary(n)` schrijven die als volgt werkt:

```ipython
In [1]: num_to_binary(5)
Out[1]: '101'

In [2]: num_to_binary(12)
Out[2]: '1100'
```


:::{admonition} Opmerkingen
:class: notice

Merk op dat deze functie inderdaad slechts één "bit" (nul of één) tegelijk verwerkt, verder:

-   Omdat we geen voorloopnullen willen (nullen aan het begin van de string), is het resultaat een lege string als het argument `n` nul (`0`) is.

-   Dit betekent dat `num_to_binary(0)` de *lege string* is. Dit is geen probleem, en sterker nog, het is verplicht!

-   Als het argument `n` oneven is, voegt de functie een `1` toe.

-   Als het argument `n` even is (`else`), voegt de functie een `0` toe.

Welke recursieve aanroep van `num_to_binary` (of andere berekeningen) zijn nodig?
:::

Hier zie je een aantal voorbeelden:

```ipython
In [1]: num_to_binary(0)
Out[1]: ''

In [2]: num_to_binary(1)
Out[2]: '1'

In [3]: num_to_binary(4)
Out[3]: '100'

In [4]: num_to_binary(10)
Out[4]: '1010'

In [5]: num_to_binary(42)
Out[5]: '101010'

In [6]: num_to_binary(100)
Out[6]: '1100100'
```

:::{admonition} Tips
:class: tip

-   Je zal de recursieve aanroep van `num_to_binary` met een kleinere waarde moeten doen.

-   Welke *waarde* van `n` blijft over wanneer één bit (het meest rechtse bit) van `n` wordt verwijderd? Deze waarde heb je nodig!

-   Onthoud dat de `//`-operator een integerdeling uitvoert (en naar beneden zal afronden).

<!-- TODO verwijzing naar slides: "tfw binary is fleek? Check out the gold notes' fleek version (which can easily extend to any base...") -->

:::

### Opdracht 3: `binary_to_num(s)`

Nu ga je het probleem aanpakken om van grondtal 2 naar grondtal 10 te gaan, opnieuw van *rechts naar links*. We stellen een waarde met grondtal 2 voor als een reeks van 0'en en 1'en (bits).

Kort samengevat, je gaat een functie `binary_to_num(s)` schrijven die als volgt werkt:

```ipython
In [1]: binary_to_num("101")
Out[1]: 5

In [2]: binary_to_num("101010")
Out[2]: 42
```


:::{admonition} Opmerkingen
:class: notice

Onthoud dat het argument `s` een *string* is! Verder:

-   Merk op dat ook deze functie slechts één "bit" (nul of één) tegelijk verwerkt, van rechts naar links.

-   Deze functie doet het tegenovergestelde van de vorige, dus als het argument een lege string is moet de functie `0` teruggeven. Dit is geen probleem, en sterker nog, het is verplicht!

-   Als het *laatste* cijfer van `s` een `'1'` is, telt de functie de waarde `1` op bij het resultaat.

-   Als het *laatste* cijfer van `s` een `'0'` is, telt de functie de waarde `0` op bij het resultaat. (Strikt genomen niet verplicht, maar ook geen probleem.)

Welke recursieve aanroep van `binary_to_num` (of andere berekeningen) zijn nodig in de lege (`...`) plekken hierboven?
:::

Hier zie je een aantal voorbeelden:

```ipython
In [1]: binary_to_num("100")
Out[1]: 4

In [2]: binary_to_num("1011")
Out[1]: 11

In [3]: binary_to_num("00001011")
Out[1]: 11

In [4]: binary_to_num("")
Out[1]: 0

In [5]: binary_to_num("0")
Out[1]: 0

In [6]: binary_to_num("1100100")
Out[1]: 100

In [7]: binary_to_num("101010")
Out[1]: 42
```

:::{admonition} Tips
:class: tip

-   Je zal de recursieve aanroep van `binary_to_num` met een kleinere string moeten doen.

-   Hoe krijg je de string van alles *behalve* het laatste cijfer?! (Gebruik string slicing!)

-   De recursieve aanroep zal de waarde van de kleinere string teruggeven. Dit is een te *kleine* waarde, maar...

-   Welke berekening kan en moet u uitvoeren om de waarde te laten kloppen?

-   Vergeet niet dat de recursie de waarde van een binaire string één bit korter (één plek naar rechts verschoven) teruggeeft. Bedenk hoe deze verschuiving de waarde verandert en hoe je dat effect ongedaan kan maken!

    Je kan ofwel vermenigvuldigen of verschuiven met een shift-operator, maar zorg ervoor dat je dit doet buiten en na de recursieve aanroep van `binary_to_num`.

Dat is alles wat je nodig hebt, slechts één operatie na de recursieve aanroep!
:::

## Binair tellen

Je gaat nu functies schrijven om binair te tellen, gebruik de twee functies die je eerder hebt geschreven!

### Opdracht 4: `increment(s)`

In het kort, schrijft `increment(S)`, die een binaire string `s` met `0`'en en `1`'en accepteert en het volgende getal in grondtal 2 teruggeeft.

:::{admonition} Opmerkingen
:class: notice

Merk op dat `increment('11111111')` in de voorbeelden hier beneden weer uitkomt op een string met alleen maar nullen. Dit kan een speciaal geval zijn (`if`).

Je hebt hier geen recursie nodig, gebruik in plaats recursie de functies die je eerder hebt geschreven! Hier is de pseudocode:

-   Neem `n` = de numerieke waarde van het argument `s`
-   Neem `x = n + 1` (dit is de verhoogde waarde!)
-   Zet `x` *terug* naar een binaire string met de andere functie!
-   Geef een naam, zeg `y`, aan deze nieuwe binaire string...
-   Nu ben je bijna klaar!
:::

Hier zie je een aantal voorbeelden:

```ipython
In [1]: increment("00000000")
Out[1]: '00000001'

In [2]: increment("00000001")
Out[2]: '00000010'

In [3]: increment("00000111")
Out[3]: '00001000'

In [4]: increment("11111111")
Out[4]: '00000000'
```

:::{admonition} Tips
:class: tip

-   Het lastige deel is zorgen dat je genoeg voorloopnullen hebt (voor `y`, als je die naam hebt gebruikt).

-   Je kan 42 nullen voor `y` zetten met `"0" * 42 + y`

Nu moet je nog bedenken wat het *correcte* aantal nullen is... hiervoor heb je de functie `len` nodig!
:::

### Opdracht  5: `count(s, n)`

Gebruik de functie `increment` om de functie `count(s, n)` te schrijven, die een binaire string van 8 tekens accepteert als argument en vervolgens `n` keer doortelt vanaf `s`, terwijl hij wordt afgedrukt.

:::{admonition} Opmerkingen
:class: notice

-   Dit betekent dat jouw functie in totaal `n+1` binaire strings zal afdrukken.

-   Je moet de Python `print` functie gebruiken, omdat er niets wordt teruggegeven. We printen alleen naar het scherm.

-   Je hebt hier *wel* een recursie nodig. Wat zijn de base case en de recursive case?
:::

Hier zie je een aantal voorbeelden:

```ipython
In [1]: count("00000000", 4)
00000000
00000001
00000010
00000011
00000100

In [2]: count("11111110", 5)
11111110
11111111
00000000
00000001
00000010
00000011
```

:::{admonition} Tips
:class: tip

-   Gebruik de functie `increment`!

-   Het basisgeval heeft te maken met `n` (wat is de meest "eenvoudige" waarde van `n`?)

-   Het recursieve geval gebruikt `n-1`.
:::

## Ternaire getallen

> Er zijn 10 soorten mensen in de wereld: zij die ternaire getallen kennen, zij die dat niet kennen, en zij die denken dat dit een binaire grap is.

De volgende functies gaan over ternaire getallen, oftewel waarden in grondtal 3.

### Opdracht  6: `num_to_ternary(n)`

Voor dit deel breiden we deze het idee van binaire getallen (grondtal 2) uit naar ternaire getallen (grondtal 3). Net zoals binaire getallen de twee cijfers 0 en 1 gebruiken, gebruiken ternaire getallen de cijfers 0, 1 en 2. Opeenvolgende kolommen in de ternaire getallen vertegenwoordigen opeenvolgende machten van drie. Bijvoorbeeld, het ternaire getal

`1120`

als je het van rechts naar links leest, evalueert het als `1` zevenentwintig, `1` negen, `2` drieën en `0` enen. Samengevat, het is gelijk aan `1*27 + 1*9 + 2*3 + 0*1 == 42`.

Gebruik dezelfde ideeën die je hebt gebruikt om eerder binaire conversiefuncties te schrijven om de functie `num_to_ternary(n)` te schrijven die een ternaire string teruggeeft van de waarde van het argument `n` (net als `num_to_binary`).

Hier zie je een aantal voorbeelden:

```ipython
In [1]: num_to_ternary(42)
Out[1]: '1120'

In [2]: num_to_ternary(4242)
Out[2]: '12211010'
```

:::{admonition} Opmerkingen
:class: notice

-   Baseer jouw oplossing op de overeenkomstige functie `num_to_binary`!
-   Het kopiëren en plakken van deze functie (en veranderen als dat nodig is) is de beste strategie.
:::

### Opdracht 7: `ternary_to_num(s)`

Scrijf de functie `ternary_to_num(s)`, die een integer representatie teruggeeft van de waarde van het argument `s` (net als `binary_to_num`).

Hier zie je een aantal voorbeelden:

```ipython
In [3]: ternary_to_num("1120")
Out[3]: 42

In [4]: ternary_to_num("12211010")
Out[4]: 4242
```

Ook hier geldt dat de beste strategie is om `binary_to_num` te gebruiken en aan te passen.


# Caesar op orde!

In deze opgave ga je een aantal functies schrijven met behulp van *functioneel programmeren*, dat wil zeggen, conditionele statements, recursie en/of list comprehensions.

Zorg bij elke opdracht dat je de naam precies zo schrijft zoals dit wordt opgegeven, inclusief hoofd-en kleine letters. Voeg verder aan elke functie een *docstring* toe waar je kort uitlegt wat de argumenten van de functie zijn en wat de functie doet.

## De functie `encipher(s, n)`

Schrijf een functie `encipher(s, n)` die als argumenten een string `s` en een (niet negatieve) integer 'n' met een waarde tussen `0` en `25` verwacht. De functie `encipher` moet een nieuwe string teruggeven waarin de letters in `s` met `n` letters voorwaarts zijn "geroteerd" in het alfabet, en terug naar het begin van het alfabet als dat nodig is.

Bij dit probleem mag je ervan uitgaan dat hoofdletters "geroteerd" worden naar hoofdletters, kleine letters naar kleine letters en dat alle andere tekens *niet* veranderd worden. Als we bijvoorbeeld de letter
`'y'` 3 posities willen verschuiven, krijgen we de `'b'` en als we de letter `'Y'` 3 posities willen verschuiven krijgen we `'B'`.

:::{admonition} Karakters in het alfabet
:class: tip

In Python kan je de test `if "a" <= c <= "z":` gebruiken om te controleren of een karakter `c` tussen de `'a'` en `'z'` in het alfabet zit.
:::

Je mag `encipher` schrijven hoe je wilt, mits je functioneel programmeren gebruikt. Je mag dus elke combinatie van *conditionele statements*, *recursie* en *list comprehensions* gebruiken.

We raden je aan een hulpfunctie te schrijven die een enkel karakter `n` plaatsen roteert, terug naar het begin als dat nodig is. Deze hulpfunctie zou je kunnen gebruiken om de karakters in de string één voor ééń te versleutelen. Je moet zelf bepalen hoe je dat doet!

:::{admonition} Een hulpfunctie `rot(c, n)`
:class: tip

Schrijf een functie `rot(c, n)` die een enkel karakter `c` `n` plaatsen voorwaarts roteert in het alfabet. De functie `rot13(c)` die je eerder hebt gezien lijkt heel erg op `rot(c, n)`!

Bedenk dat je soms terug naar het begin van het alfabet moet en dat tekens die geen letter zijn *niet* veranderen. Controleer vervolgens met `assert` statements of de functie `rot(c, n)` werkt:

```python
assert rot("a", 2) == "c"
assert rot("y", 2) == "a"
assert rot("A", 3) == "D"
assert rot("Y", 3) == "B"
assert rot(" ", 4) == " "
```

Bedenk verder dat je de ingebouwde functies `ord` en `chr` die een string met één karakter omzetten naar een integer en omgekeerd kan gebruiken bij het roteren:

* `ord('a')` geeft bijvoorbeeld `97` terug
* ... en `chr(97)` geeft `'a'` terug.
:::

<!-- TODO verwijzing DNA-naar-RNA opnemen -->

Als je de tip volgt en een hulpfunctie`rot(c, n)` schrijft dan kan je:

-   je kan het met behulp van `rot(c, n)` een string letter voor letter recursief doorlopen, met een lege string `s` als base case.

-   je kan ook list comprehensions gebruiken om `rot(c, n)` meerdere keren toe te passen.

    ```python
    [rot(c, n) for c in ...]
    ```

-   als je een list comprehension gebruikt, kan je onderstaande functie `list_to_str` gebruiken om er weer een string van te maken!

    ```python
    def list_to_str(L):
        """L must be a list of characters;
           this function returns a single string made from them.
        """
        if len(L) == 0:
            return ""
        return L[0] + list_to_str(L[1:])


    assert list_to_str(['h', 'a', 'n', 'z', 'e']) == 'hanze'
    ```

Hoe je `encipher` ook schrijft, zorg dat je de functie test! Hier is een begin:

```python
assert encipher("xyza", 1) == "yzab"
assert encipher("Z A", 1) == "A B"
```

Hier zijn wat meer voorbeelden, we raden je aan deze om te zetten in `assert` statements en aan jouw tests toe te voegen:

```ipython
In [1]: encipher('xyza', 1)
Out[1]: 'yzab'

In [2]: encipher('Z A', 1)
Out[2]: 'A B'

In [3]: encipher('*ab?', 1)
Out[3]: '*bc?'

In [4]: encipher('Dit is een string!', 1)
Out[4]: 'Eju jt ffo tusjoh!'

In [5]: encipher('Caesarcijfer? Ik heb liever Caesarsalade.', 25)
Out[5]: 'Bzdrzqbhiedq? Hj gda khdudq Bzdrzqrzkzcd.'
```

Tot slot, onthoud dat:

-   Hoofdletters altijd hoofdletters blijven.
-   Kleine letters altijd kleine letters blijven.
-   Andere tekens helemaal niet veranderen!

## De functie `decipher(s)`

Omgekeerd krijgt `decipher(s)` een string `s` met een (Nederlandstalige) tekst die al versleuteld is. De functie `decipher` moet, voorzover mogelijk, de *originele* tekst teruggeven, dit zal een rotatie (mogelijk ook `0`) zijn van het argument `s`.

Wees bewust dat sommige strings meer dan één "ontsleuteling" kunnen hebben. Bovendien is het moeilijk of soms zelfs onmogelijk om hele korte strings goed te ontsleutelen. De functie `decipher` hoeft dus ook niet *perfect* te zijn, maar moet wel vrijwel altijd werken met langere stukken Nederlandse tekst, bijvoorbeeld zinnen van 8 of meer woorden. Het is dus geen probleem als een enkel woord of een korte zinnen niet goed worden ontsleuteld.

:::{admonition} Lists of lists
:class: tip

Het is handig om te beginnen met het genereren van *alle mogelijke versleutelingen*, bijvoorbeeld via:

```python
L = [... for n in range(26)]
```

Vervolgens is het handig om de `LoL` "lists of lists", oftewel de  "lijst van lijsten"-techniek te gebruiken om elk element van `L` een score te geven. Het kan handig zijn om nog even op te zoeken hoe dat werkt.

```python
lists = [... for x in L]
```

Je mag zelf bepalen hoe je "Nederlandstaligheid" een score geeft, hier een paar aanknopingspunten:

-  Je kan kijken naar het voorbeeld met `best_word` dat het woord zocht met de hoogste Scrabble score in een lijst woorden. Dat lijkt heel aardig op wat je hier wilt doen!
-   Kijk daarna nog eens terug naar het college over `min` en `max` om te zien hoe je de "lijst van lijsten" `lists` kan gebruiken

<!-- TODO verwijzing naar college -->
:::

Een mogelijke aanpak is het gebruik van letterfrequenties, hieronder is een functie gegeven met de frequenties per letter en deze kan je gebruiken in de opgave. Je zou ook Scrabble scores kunnen proberen (want deze zijn ook gebaseerd op letterfrequenties). Je mag zelf extra heuristieken ("vuistregels") bedenken en verder mag je ook kleine hulpfuncties toevoegen om te helpen met het schrijven van `decipher`.

Hoe je het ook aanpakt, onthoud dat je de strategie die je gebruikt bij het schrijven van de functie `decipher` moet documenteren in een kort stukje commentaar boven de functie `decipher`.

Enkele voorbeelden van `decipher`:

```ipython
In [1]: decipher('Bzdrzqbhiedq? Hj gda khdudq Bzdrzqrzkzcd.')
Out[1]: 'Caesarcijfer? Ik heb liever Caesarsalade.'

In [2]: decipher('Aadxas ue exqotfe pq haadflqffuzs hmz baxufuqw yqf mzpqdq yuppqxqz.')
Out[2]: 'Oorlog is slechts de voortzetting van politiek met andere middelen.'

In [3]: decipher('Lvkeg lvyon')
Out[3]: 'Tdsmo tdgwv'  # Dit is fout! Maar is hier geen probleem...
```

Ook hier raden we jou aan om deze voorbeelden (in ieder geval de eerste twee!) om te zetten naar `assert` statements.

Merk verder op dat het laatste voorbeeld laat zien dat onze ontsleutelaar het niet goed doet bij sommige korte zinnen. Dit is geen probleem!  Naarmate de zinnen langer worden, moet de ontsleutelaar er steeds meer goed hebben, maar hij hoeft enkele woorden of korte zinnen niet goed te hebben, voor korte strings zijn er immers zeer waarschijnlijk rotaties met meer "Nederlandsige" letters dan het origineel!

Hier is een functie om de kans per letter te bepalen:

```python
# tabel met kansen per letter
def letter_prob(c):
    """If c is an alphabetic character,
       we return its monogram probability (for Dutch),
       otherwise we return 1.0.  We ignore capitalization.
       Adapted from
       https://www.sttmedia.com/characterfrequency-nederlands
    """
    if c == 'e' or c == 'E':
        return 0.1909
    if c == 'n' or c == 'N':
        return 0.0991
    if c == 'a' or c == 'A':
        return 0.0769
    if c == 't' or c == 'T':
        return 0.0642
    if c == 'i' or c == 'I':
        return 0.0630
    if c == 'o' or c == 'O':
        return 0.0581
    if c == 'r' or c == 'R':
        return 0.0562
    if c == 'd' or c == 'D':
        return 0.0541
    if c == 's' or c == 'S':
        return 0.0384
    if c == 'l' or c == 'L':
        return 0.0380
    if c == 'h' or c == 'H':
        return 0.0312
    if c == 'g' or c == 'G':
        return 0.0312
    if c == 'k' or c == 'K':
        return 0.0279
    if c == 'm' or c == 'M':
        return 0.0256
    if c == 'v' or c == 'V':
        return 0.0224
    if c == 'u' or c == 'U':
        return 0.0212
    if c == 'j' or c == 'J':
        return 0.0182
    if c == 'w' or c == 'W':
        return 0.0172
    if c == 'z' or c == 'Z':
        return 0.0160
    if c == 'p' or c == 'P':
        return 0.0149
    if c == 'b' or c == 'B':
        return 0.0136
    if c == 'c' or c == 'C':
        return 0.0130
    if c == 'f' or c == 'F':
        return 0.0073
    if c == 'y' or c == 'Y':
        return 0.0006
    if c == 'x' or c == 'X':
        return 0.0005
    if c == 'q' or c == 'Q':
        return 0.0001
    return 1.0
```

:::{admonition} Beslissingen
:class: tip

Voor `decipher` zal jouw programma alle 26 mogelijke rotaties van de string `s` die als argument is meegegeven moeten "bekijken" en dan beslissen welke de "beste" is...
:::

## De functie `blsort(L)`

Schrijf een functie `blsort(L)` die als argument een lijst `L` accepteert en een lijst teruggeeft met dezelfde elementen als `L`, maar in oplopende volgorde. (Let op: het tweede teken van de functienaam is een "el" voor "lijst", niet een 1 (één) of een "i"!)

`blsort` hoeft alleen maar lijsten met *binaire cijfers* te sorteren, dat wil zeggen, deze functie mag en moet ervan uitgaan dat `L` altijd een lijst met alleen `0`'en en `1`'en is.

Je mag de ingebouwde Python functie `sort` niet gebruiken om dit probleem op te lossen! Je mag ook je zelfgeschreven sorteerfunctie (deze wordt later gevraagd) niet gebruiken.

Verder mag je elke andere functionele techniek gebruiken om `blsort` te implementeren. In het bijzonder is het handig te bedenken hoe je gebruik kan maken van de beperking dat het argument `L` een binaire lijst is, dit is een belangrijke beperking!

<!-- TODO verwijzing naar eerste gebruik count(e, L) -->

Een functie die sommigen handig vinden is `count(e, L)`, een hulpfunctie die je eerder al hebt gezien. Kopieer deze of probeer het opnieuw te schrijven, het belangrijkste onderdeel is:

```python
lc = [1 for x in L if x == e]
```

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

Dit probleem is veel *makkelijker* dan gewoon sorteren! Maak gebruik van het feit dat de lijst `L` alleen maar `0` of `1` kan bevatten.
:::

## De functie `gensort(L)`

<!-- TODO verwijzing opnemen naar eerste gebruik rem_one -->

Gebruik recursie om een algemene sorteerfunctie `gensort(L)` te schrijven die een lijst `L` accepteert en een lijst teruggeeft met dezelfde elementen als `L`, maar in *oplopende* volgorde. Je kan hiervoor de ingebouwde Python functie `max` (of `min`, als je deze liever hebt) gebruiken, en de functie `rem_one` die je al eerder hebt gezien. Recursie, dat wil zeggen het sorteren van de *rest* van de lijst, is hier handig.

Je ziet hier een paar voorbeelden:

```ipython
In [1]: gensort([42, 1, 3.14])
Out[1]: [1, 3.14, 42]

In [2]: L = [7, 9, 4, 3, 0, 5, 2, 6, 1, 8]

In [3]: gensort(L)
Out[3]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Bij deze opgave mag je de in Python ingebouwde sorteer functies zoals `sorted(L)` en `L.sort()` **niet** gebruiken. Je moet zelf een aanpak bedenken en implementeren! Let verder op dat `gensort(L)` moet werken voor *lijsten* `L`, het hoeft **niet** te werken voor strings.

## De functie `lingo(s, t)`

Schrijf een functie `lingo(s, t)` die twee strings `s` en `t` accepteert en een integer teruggeeft, de zogenaamde "[Lingo](https://nl.wikipedia.org/wiki/Lingo)-telling, of -score, waar `s` wordt vergeleken met `t`.

De Lingo-score is het aantal tekens in `s` dat ook voorkomt in `t`. Herhaalde letters tellen vaker, mits ze vaker voorkomen in beide strings, hoe dit werkt wordt duidelijker in de onderstaande voorbeelden. Je hoeft er bij deze functie geen rekening mee
te houden of de letters op dezelfde plek staan. Merk op dat alhoewel Lingo traditioneel gespeeld wordt met woorden van 5 (of 6) letters, de lengte van de woorden in deze functie niet beperkt is!

<!-- TODO wordt verwezen naar handige hulpfuncties behandeld in college, welke? -->

Er zijn meerdere manieren om dit probleem op te lossen, een aantal daarvan gebruikt kleinere hulpfuncties. Het staat je vrij om
zulke hulpfuncties toe te voegen als je dat handig vindt. Het zou kunnen dat je al nuttige hulpfuncties bent tegengekomen die hier van toepassing kunnen zijn.

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

## De functie `exact_change(target_amount, L)`

Schrijf een functie `exact_change(target_amount, L)` die als argument een (niet-negatieve) integer `target_amount` en een lijst `L` met (niet-negatieve) integers accepteert en een boolean waarde (`True` of `False`) teruggeeft.

De functie geeft `True` terug als het mogelijk is om `target_amount` te halen door een aantal (of alle) waarden in `L` bij elkaar op te tellen. Als dit *niet* mogelijk is zal de functie `False` teruggeven.

`L` zou bijvoorbeeld de munten in jouw portemonnee kunnen voorstellen en `target_amount` de prijs van iets dat je wilt kopen. In dit geval bepaalt de functie `exact_change` of je dat product wel of niet *precies* kan betalen (wisselgeld krijg je niet ...).

Hier zijn een paar voorbeelden van `exact_change`. Let op dat je `0` *altijd* precies kan betalen, en dat je een negatief bedrag *nooit* precies kan betalen: dit zijn twee, maar niet alle, base cases!

```ipython
In [1]: exact_change(42, [25, 1, 25, 10, 5, 1])
Out[1]: True

In [2]: exact_change(42, [25, 1, 25, 10, 5])
Out[2]: False

In [3]: exact_change(42, [23, 1, 23, 100])
Out[3]: False

In [4]: exact_change(42, [23, 17, 2, 100])
Out[4]: True

In [5]: exact_change(42, [25, 16, 2, 15])
Out[5]: True  # de 16 moet "overgeslagen" kunnen worden...

In [6]: exact_change(0, [4, 5, 6])
Out[6]: True

In [7]: exact_change(-47, [4, 5, 6])
Out[7]: False

In [8]: exact_change(0, [])
Out[8]: True

In [9]: exact_change(42, [])
Out[9]: False
```

:::{admonition} Use it or lose it
:class: tip

Dit probleem kan net zoals `lcs`, hieronder, worden opgelost door *twee* keer recursie toe te passen en beide resultaten een naam te geven.

-   Voor het eerste geval kan je proberen het probleem op te lossen *zonder* de eerste munt, dit is het *lose-it* geval!

    Je kan zelfs de variabelenaam `loseit` gebruiken, als in

    ```python
    loseit = exact_change(...)
    ```

-   Voor het tweede geval kan je proberen het probleem op te lossen *met* de eerste munt, dit is het *use-it* geval!

    Je kan hierbij dan de variabelenaam `useit` gebruiken, als in

    ```python
    useit = exact_change(...)
    ```

-   Vervolgens kan je jouw code de geschikte boolean waarde laten bepalen om terug te geven op basis van de twee resultaten: je gaat hier letterlijk de `or` van *use it or lose it* toepassen!
:::

## De functie `lcs(s, t)`

De laatste algoritmische uitdaging heeft alles met DNA-matching te maken!

Schrijf een functie `lcs(s, t)` die twee strings `s` en `t` accepteert. De functie geeft een string terug die de langste gemeenschappelijke deelrij (LCS, *longest common subsequence*) is die `s` en `t` met elkaar delen.

De LCS is een string waarvan de letters een deelrij van `s` en een deelrij van `t` zijn (ze moeten in dezelfde volgorde, maar niet noodzakelijkerwijs na elkaar in de twee argumenten voorkomen).

Let op dat als `s` of `t` een lege string is, het resultaat ook een lege string is!

Een paar voorbeelden:

```ipython
In [1]: lcs('mens', 'chimpansee')
Out[1]: 'mns'

In [2]: lcs('gattaca', 'tacgaacta')
Out[2]: 'gaaca'

In [3]: lcs('wow', 'wauw')
Out[3]: 'ww'

In [4]: lcs('', 'wauw')     # eerste argument is de lege string
Out[4]: ''

In [5]: lcs('abcdefgh', 'efghabcd')
Out[5]: 'abcd'
```

Als meerdere resultaten van gelijke lengte mogelijk zijn dan maakt het niet uit welke je teruggeeft, in het laatste voorbeeld hierboven zou `'efgh'` ook een goed antwoord zijn geweest.

:::{admonition} Use it or lose it or lose it
:class: tip

Gebruik de volgende strategie:

-   Als de eerste twee karakters gelijk zijn, gebruik ze dan!

-   Als de eerste twee karakters niet gelijk zijn, pas dan twee keer recursie toe: je zou dit *use it or lose it or lose it* kunnen noemen!

-   Gebruik voor de eerste "lose it" recursie om de eerste letter van het ene argument weg te gooien:

    ```python
    result1 = lcs(s[1:], t)
    ```
-   Gebruik voor de tweede "lose it" recursie om de eerste letter van het andere argument weg te gooien:

    ```python
    result2 = lcs(..., ...)
    ```

    Hier moet je nog wat details invullen...

-   Geef ten slotte de *betere* van de twee resultaten terug, je moet hier nog even bedenken wat "beter" in dit geval betekent!
:::

## Bonusopgave

Kan je nog geen genoeg krijgen van algoritmes? Hier is een optionele bonusopgave om het ontwerp van algoritmes te oefenen! Het bouwt voort op `exact_change`, maar is moeilijker omdat:

-   Het de gebruikte munten moet teruggeven
-   Het ook `False` kan teruggeven, en je een aantal gevallen moet afhandelen *na* de recursie...

### De functie `make_change(target_amount, L)`

Schrijf voor maximaal 7 bonuspunten de functie `make_change(target_amount, L)`, de argumenten zijn gelijk aan de functie `exact_change` die je eerder hebt geschreven. De functie moet bepalen welke waarden uit `L` gebruikt kunnen worden om `target_amount` te betalen.

In plaats van `True` of `False` terug te geven zoals bij `exact_change` moet de functie `make_change` een *lijst* teruggeven van munten uit `L` die samen optellen tot `target_amount`. Als geen lijst kan worden samengesteld zal de functie `False` teruggeven. Als meer dan één lijst met waarden uit `L` mogelijk is mag de functie elk geldig antwoord teruggeven.

De *volgorde* van de waarden in het antwoord maakt niet uit, maar het is logisch om dezelfde volgorde aan te houden als van de oorspronkelijke lijst.

Je hoeft `exact_change` niet als hulpfunctie te gebruiken, maar het mag wel!

De voorbeelden hieronder tonen hoe `make_change` moet werken, dit zijn dezelfde voorbeelden als bij `exact_change` hierboven. Bovendien is de ingebouwde Python-functie `sorted` gebruikt voor gevallen waar het resultaat een niet-lege lijst is zodat het resultaat een duidelijke volgorde heeft:

```ipython
In [1]: sorted(make_change(42, [25, 1, 25, 10, 5, 1]))
Out[1]: [1, 1, 5, 10, 25]

In [2]: make_change(42, [25, 1, 25, 10, 5])
Out[2]: False

In [3]: make_change(42, [23, 1, 23, 100])
Out[3]: False

In [4]: sorted(make_change(42, [23, 17, 2, 100]))
Out[4]: [2, 17, 23]

In [5]: sorted(make_change(42, [25, 16, 2, 15]))
Out[5]: [2, 15, 25]

In [6]: make_change(0, [4, 5, 6])
Out[6]: []

In [7]: make_change(-47, [4, 5, 6])
Out[7]: False

In [8]: make_change(0, [])
Out[8]: []

In [9]: make_change(42, [])
Out[9]: False
```
# Sequenties en data

| Naam         | Beschrijving                                                   |
|--------------|----------------------------------------------------------------|
| Onderwerp    | Slice and dice                                 |
| Leerdoel     | List slicing en indexering                                     |
| Bestandsnaam | `wk2ba3.py`                                                    |
| Inleveren    | Lever jouw bestand met de juiste bestandsnaam in op GradeScope |


## Opgave

In deze opgave ga je oefenenen met *slicen* en *indexeren* van lijsten (lists).

Maak eerst een nieuw tekstbestand aan, kopieer vervolgens het volgende in het bestand en sla het op als `wk2ba3.py`:

```python
# Voorbeeldopgave lists, resultaat: [2, 7, 5, 9]

e = [2, 7, 1]
pi = [3, 1, 4, 1, 5, 9]

answer0 = e[0:2] + pi[-2:]
print(answer0)
```

:::{admonition} Opmerkingen bij deze code
:class: notice

- let op dat je het bestand opslaat als platte tekst met een `.py` bestandsextensie (zie werken met [platte tekst](/support/plain_text/index))
- in de code worden *twee* lists gedefiniëerd, één met de naam `e` en een ander met de naam `pi`
- wanneer je de code uitvoert zal de regel `answer0 = e[0:2] + pi[-2:]` de waarde van de variabele `answer0` definiëren. Met andere woorden, vanaf deze regel is in het programma de naam `answer0` bekend die verwijst naar het resultaat van de expressie `e[0:2] + pi[-2:]`!
- vervolgens drukt de code de waarde van de variabele `answer0` af.
:::

### Code uitvoeren

* zorg dat je op de command line in de directory bent waar `wk2ba3.py` is opgeslagen. Dit kan bijvoorbeeld het Bureaublad zijn of een andere directory (gebruik `pwd` om te zien waar je bent!)
* type in  `python wk2ba3.py` om het programma uit te voeren.

### Lijsten maken en bewerken

In deze opgave ga je een aantal lijsten maken met *alleen* maar de getallen in de lijsten `pi` en `e` met behulp van de volgende bewerkingen:

-   lijsten indexeren, bijvoorbeeld `pi[0]`
-   lijsten slicen, bijvoorbeel `e[:1]`
-   stapsgewijs slicen, bijvoorbeeld `pi[0:6:2]`
-   lijsten samenvoegen met `+`, bijvoorbeeld `e[0:2] + pi[-2:]`

    (voor deze opgaven vragen we jou `+` *niet* te gebruiken voor het optellen van getallen)

:::{admonition} Lege regels en experimenteren
:class: info

Gebruik *één of meer lege regels* tussen jouw antwoorden (zodat het zowel voor jou als voor ons goed leesbaar blijft!).

*Als je het leuk vindt* kan je proberen zo min mogelijk bewerkingen te gebruiken om tot eenvoudige, elegante en efficiënte oplossingen te komen.
:::

De opgaven zijn als volgt:

0.  Gebruik `pi` en `e` (of maar één!) om de lijst `[2, 7, 5, 9]` te maken. Dit is het voorbeeld dat je hierboven ziet, deze lijst bewaar je in de variabele met naam `answer0`.

1.  Gebruik `pi` en `e` (of maar één, je mag voor alle verdere problemen ook maar één lijst gebruiken) om de lijst `[7, 1]` te maken.

    Bewaar de lijst, net als hierboven, in de variabele `answer1`. Hier is een klein begin wat je kan kopiëren en plakken:

    ```python
    # Opgave 1: [7, 1] maken

    answer1 = e[1:2]  # niet het juiste antwoord, maar een begin...
    print(answer1)
    ```

2.  Gebruik `pi` en `e` om de lijst `[1, 1, 2]` te maken. Bewaar deze lijst in de variabele `answer2`.

3.  Gebruik `pi` en `e` om de lijst `[1, 4, 1, 5, 9]` te maken. Bewaar deze lijst in de variabele `answer3`.

4.  Gebruik `pi` en `e` om de lijst `[1, 2, 3, 4, 5]` te maken. Bewaar deze lijst in de variabele `answer4`.

### Strings slicen en indexeren

Deze opgave is in dezelfde stijl als de vorige, maar gebruikt strings in plaats van lijsten. Kopieer eerst de volgende regels naar jouw bestand onder de laatste opgave die je hebt gemaakt (gebruik lege regels om ze duidelijk van elkaar te scheiden!):

```python
# Oefeningen met strings

h = "hanze"
s = "hogeschool"
g = "groningen"
```

Je mag elke combinatie van de onderstaande vier bewerkingen gebruiken:

-   strings indexeren, bijvoorbeeld `h[0]`
-   strings slicen, bijvoorbeeld `s[1:]`
-   strings samenvoegen met `+`, bijvoorbeeld `h + s`
-   herhalingen met `*`, bijvoorbeeld `42*g`

De opgaven zijn als volgt (de eerste kijg je van ons):

5.  Gebruik `h`, `s` of `g` (je mag voor elke volgende opgave één of meerdere gebruiken) om de string `hoi` te maken.

    Bewaar de string in de variabele met naam `answer5`. De oplossing zie je hieronder, kopiëer en plak deze in jouw bestand:

    ```python
    # Opgave 5:  'hoi' maken

    answer5 = s[0:2] + g[4]
    print(answer5)
    ```

    In totaal zijn 3 bewerkingen nodig, het ophalen van `ho` met `s[0:2]` (slicen), het ophalen van `i` met `g[4]` (indexeren) en vervolgens deze twee waarden samenvoegen met `+` zodat we tot `hoi` komen als nieuwe waarde.

    :::{admonition} Meer of minder bewerkingen
    :class: warning

    Bij elk van de volgende opgaven zullen we steeds aangeven wat het minimaal aantal bewerkingen is dat wij hebben kunnen vinden. Het maakt niet uit als jij meer bewerkingen nodig hebt, zolang je maar tot een *juiste oplossing* komt!
    :::

6.  Gebruik `h`, `s` of `g` om de string `schoenen` te maken en bewaar deze string in de variabele `answer6`. (Ons record: 4 bewerkingen)

7.  Gebruik `h`, `s` of `g` om de string `anzeogeschool` te maken en bewaar deze string in de variabele `answer7`. (Ons record: 3 bewerkingen)

8.  Gebruik `h`, `s` of `g` om de string `gnagnahahahahaha` te maken en bewaar deze string in de variabele `answer8`. (Ons record: 7 bewerkingen)

9.  Gebruik `h`, `s` of `g` om de string `legonoego` te maken en bewaar deze string in de variabele `answer9`. (Ons record: 7 bewerkingen)

10. Gebruik `h`, `s` of `g` om de string `leggings` en bewaar deze string in de variabele `answer10`. (Ons record: 7 bewerkingen)

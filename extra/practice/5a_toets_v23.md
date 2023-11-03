---
version: 2023
---

# Proeftoets

## Opgave 1 (10pt)

In Nederland meten we iemands lengte meestal in meters en centimeters. In de Verenigde Staten wordt dit echter meestal gedaan in inches en feet. Hierbij geldt dat een inch 2,54 cm is, en dat er 12 inch in een foot gaan. Iemand die bijvoorbeeld 1 meter en 90,5 cm is, is (ongeveer) 6 feet en 3 inches lang.

$$
(6 \times 12 + 3) \times 2,54 = 190,5
$$

Schrijf een aantal toekenningen **toekenningen** (*geen* functie) waar je een lengte in feet en inches omrekent naar meter en centimeter waarbij feet en inches gegeven zijn, gebruik daar de variabelen `feet` en `inches` voor en ken daar de waarden `6` en `3` aan toe. Print uiteindelijk de waarden van jouw variabelen meter en centimeter.

## Opgave 2 (10pt)

De *Saffir-Simpson Hurricane Wind Scale* is een classificatie die in de meteorologie wordt gebruikt om tropische cyclonen naar hun kracht in te delen. Je ziet hier de waarden die bij de verschillende categorieën horen, waar TS staat voor tropical storm en TD voor tropical depression.

| **Categorie** |    km/h     |
| ------------- | :---------: |
| **5**         |  $\ge$ 252  |
| **4**         | 209 $-$ 251 |
| **3**         | 178 $-$ 208 |
| **2**         | 154 $-$ 177 |
| **1**         | 119 $-$ 153 |
| **TS**        | 63 $-$ 118  |
| **TD**        |  $\le$ 62   |

Gegeven is een variabele `s` die staat voor windsnelheid in km/h, deze toekenning hoef je niet te schrijven. Schrijf een **conditioneel statement** (*geen* functie) om de categorie (1, 2, 3, 4, 5, TS of TD) af te drukken (*printen*) volgens de regels hierboven. Je hoeft de categorie dus niet in een variabele op te slaan.

## Opgave 3

Gegeven is de onderstaande code

```python
def remove_double(L):
    if len(L) == 0:
        return
    if L[0] in L:
        return remove_double(L[:1])
    return L[0] + remove_double(L[:1])

assert remove_double([1, 4, 2, 3, 2]) == [1, 4, 3, 2]
```

De functie `remove_double(L)` accepteert een lijst met waarden en geeft een lijst terug met de unieke elementen. Het verwijdert dus alle dubbele waarden.

### Opgave 3a (10pt)

Helaas werkt de functie `remove_double` niet naar behoren. Pas de functie zo aan zodat het werkt. Je mag **geen** gebruik maken van list comprehensions of lusconstructies

### Opgave 3b (2pt)

Voeg een *docstring* toe aan de functie `remove_double` waarin je beschrijft wat de functie doet en de parameter die het accepteert.

### Opgave 3c (3pt)

Voeg *drie* extra assertions toe om de functie te testen.

## Opgave 4 (10pt)

Elk bestand in de computer eindigt met een bestandsextensie. Dit geeft aan wat voor bestand het is. Bijvoorbeeld, ".py" laat de computer weten dat het om een Python bestand gaat. In een email is het vaak niet toegestaan om een bijlage mee te sturen die eindigt op ".exe". Dit zou namelijk malware kunnen zijn die schadelijk is voor de computer.

We kunnen recursief bepalen of een string `s` eindigt met een string `e`:

-   Als string `e` leeg is, geef `True` terug
-   Als string `s` leeg is, geef `False` terug
-   Als de laatste letter van `e` *niet* gelijk is aan de laatste letter van `s`, geef `False` terug
-   Anders roep je de functie opnieuw aan, maar dan zonder de laatste letters van beide strings en geeft het resultaat daarvan terug.

Schrijf een functie `check_extension(s, e)` die gebruik maakt van het bovenstaande recursief algoritme. Je mag **geen** gebruik maken van list comprehensions of lusconstructies.

Gebruik de onderstaande tests om jouw oplossing te controleren:

```python
assert check_extension("tentamen.docx", ".exe") == False
assert check_extension("program.exe", ".exe") == True
assert check_extension("wk8ex1.py", ".py") == True
```

## Opgave 5 (20 pt)

![Lineup](images/lineup.png)

Een groep gevangenen staat op een rij. De meest rechter dief krijgt een beker in handen gevuld met getallen. Zijn taak is om erachter te komen of de beker alleen mar *even* getallen bevat. Heeft hij gelijk, dan is de hele groep vrij, heeft hij ongelijk, dan blijft de hele groep een jaar langer gevangen. Er zijn wel een paar regels waar de hele groep zich aan moet houden.

1.  Elke dief mag maar één getal uit de beker halen. Niemand anders mag dit getal zien. Daarna geeft hij de beker aan degene die rechts van hem zit.
2.  Elke dief mag 1 keer "True" of "False¨ fluisteren naar zijn/haar linkerbuur. De rest van de groep mag dit niet horen.

### Opgave 5a (5pt)

Beschrijf in eigen woorden met welke strategie zij dit probleem kunnen oplossen.

### Opgave 5b (15pt)

Schrijf de functie `all_even(L)` die een lijst als parameter accepteert en `False` teruggeeft als er een oneven getal in de lijst zit, anders geeft de functie `True` terug.

Bijvoorbeeld

```python
all_even([1, 2, 3, 4]) == False
all_even([2, 4, 6, 8]) == True
```

Je mag **geen** gebruik maken van list comprehensions of lusconstructies. Vergeet de docstring niet en voeg drie assertions toe om de functie te testen.

## Opgave 6

In seizoen 7, aflevering 24 van Seinfield gaat Kramer naar de bank die belooft om klanten \$100 te geven als ze niet worden begroet met "hello". Kramer wordt begroet met "hey" en eist de \$100 euro want "hey" is niet hetzelfde als "hello". De manager stelt als compromis $20 voor omdat "hey" wel begint met een "h".

In deze opdracht ga je twee functies schrijven, `starts_with` en `greeting`.

Als eerst stap hebben we een hulpfunctie `starts_with(g, s)` nodig die twee strings `g` en `s` als parameter accepteert. De functie geeft `True` of `False` terug afhankelijk van of de string `g` aan het begin staat van string `s`.

### Opgave 6a (5pt)

Beschrijf hoe je een recursieve algoritme kan gebruiken om de functie `starts_with(g, s)` te schrijven. Laat duidelijk zien wat de basis- en recursieve gevallen zijn. Je kan opdracht 4 gebruiken als voorbeeld.

### Opgave 6b (15pt)

Schrijf de functie `starts_with(g, s)`. Je mag **geen** gebruik maken van list comprehensions, lusconstructies of ingebouwde Python functies.

### Opgave 6c (10pt)

Schrijf een functie `greeting(g)` die als parameter een string `g` accepteert. De functie geeft terug hoeveel geld de bank aan een klant moet betalen.

 -  0 als de string `s` begint met "hello"
 -  20 als de string `s` begint met een "h"
 -  100 indien anders

Bijvoorbeeld

```python
greeting("dit is een test") == 100
greeting("hoi") == 20
greeting("hello world") == 0
```

Maak gebruik van de hulpfunctie `starts_with(g, s)`

**Let op**

Mocht opgave b niet zijn gelukt, dan mag je de Python functie `find` gebruiken. De functie zoekt of een string in een grotere string voorkomt. Zo ja, dan geeft het de index terug waar het de string heeft gevonden, zo niet dan geeft het een -1 terug.

Bijvoorbeeld

```python
txt = "hello and welcome"
x = txt.find("hello")  # x heeft nu de waarde 0

txt = "a very good morning."
x = txt.find("hello")  # x heeft nu de waarde -1
```

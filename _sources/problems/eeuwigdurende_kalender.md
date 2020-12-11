# Eeuwigdurende kalender

```{include} ../class/problems/eeuwigdurende_kalender.md
```

Een eeuwigdurende kalender kan je de weekdag vertellen waarop een willekeurige datum valt. Als je bijvoorbeeld geboren bent op 13 juni 1997 kan je aflezen dat je op een vrijdag geboren bent (vrijdag de dertiende, zelfs!)

In dit practicum ga je een klasse `Date` schrijven waarmee je objecten van het type `Date` kan maken. Je objecten kunnen de weekdag bepalen voor de datum waarop ze vallen, dus implementeer je in feite een eeuwigdurende kalender!

## De klasse `Date`

Download eerst het startbestand [`wk10ex1.py`](https://github.com/misja/programmeren/raw/master/problems/assets/wk10ex1.py). Kijk even rustig naar hoe het bestand er nu uitziet...

Merk op dat deze klasse `Date` drie **instantievariabelen** bevat:

* Een instantievariabele met de dag van de maand (dit is `self.day`)
* Een instantievariabele met de maand (dit is `self.month`)
* Een instantievariabele met het jaar (dit is `self.year`)

Merk ook op dat we hier `self` gebruikt wordt om *een willekeurig* object van het type `Date` aan te spreken!

### *Methodes* zijn gewoon functies

Bij objectgeoriënteerd programmeren heb je vaak aparte namen voor bekende concepten. *Methode* is bijvoorbeeld de "OOP"-naam voor *functie*. In het bijzonder is een *methode* een functie waarvan het eerste argument `self` is!

Merk op dat de klasse `Date` een methode `__init__` en een methode `__repr__` bevat. Zoals we hebben besproken tijdens het college verwacht Python deze speciale methodes in vrijwel iedere klasse. De dubbele underscores voor en na de methodenamen geven aan dat het speciale methodes zijn met een speciale betekenis voor Python. In het geval van `__init__` is dat dat Python deze methode gebruikt om een nieuw `Date`-object te maken. In het geval van `__repr__` is dat dat dit de methode is die Pythn gebruikt als het het object moet `repr`esenteren als een string.

### Een uitleg van de regel code in `__repr__`...

Bekijk de regel in `__repr__`:

```python
s = "{:02d}-{:02d}-{:04d}".format(self.day, self.month, self.year)
```

Deze regel maakt een string die lijkt op `13-10-2020` in de variabele `s`. De regel bevat de dag, de maand en het jaar, zo geformateerd dat de dag en de maand precies twee cijfers bevatten en het jaar precies vier cijfers.

We hebben ook onze eigen methode `is_leap_year` gedefinieerd. Deze bevat geen dubbele underscores, omdat Python deze methode niet "verwacht", maar er is ook geen bezwaar tegen. We hebben hier dus "gedrag" toegevoegd aan onze klasse: dit is de essentiële gedachte achter OOP: objecten bevatten zowel gegevens, instantievariabelen, als gedrag, methodes.

### De term "methode"

Normaal worden functies die door objecten wordt aangeroepen *methodes* genoemd. Hier is geen heel goede reden voor. Het zijn functies; het enige speciale is dat ze in een klasse zijn gedefinieerd en dat ze bij een aanroep worden voorafgegaan door de naam van een object en een punt. Je kan dit bijvoorbeeld dit proberen:

```ipython
In [1]: d = Date(13, 11, 2019)

In [2]: d.is_leap_year()
Out[2]: False

In [3]: nd = Date(1, 1, 2020)

In [4]: nd.is_leap_year()
Out[4]: True

In [5]: Date(1, 1, 1900).is_leap_year()   # je hebt geen variabele nodig!
Out[5]: False                             # uitzondering op de regel!
```

### Wat is er aan de hand met `self`?

Eén vreemd verschijnsel in bovenstaande code is dat **drie verschillende objecten** van het type `Date` *dezelfde* code van `is_leap_year` aanroepen. Hoe kan de methode `is_leap_year` de verschillende objecten uit elkaar houden?

De methode **weet niet** hoe de variabele heet die de methode aanroept! Sterker, in het derde voorbeeld hierboven is er *geen* variabelenaam!

Het antwoord hierop is `self`. De variabele `self` bevat **het object dat de methode aanroept**, met inbegrip van alle instantievariabelen.

Dit is waarom `self` altijd het eerste argument is van alle methodes in de klasse `Date` (en van elke andere klasse die je schrijft!): omdat `self` de manier is waarmee de methode toegang heeft tot de individuele instantievariabelen van het object dat de methode heeft aangeroepen.

:::{admonition,notice} Opmerking
Dit betekent dat een methode altijd op zijn minst één argument heeft, namelijk `self`. Deze waarde wordt echter **impliciet** meegegeven als de methode wordt aangeroepen. De variabele `self` *is het object dat de methode aanroept!*

Als voorbeeld wordt `is_leap_year` in het voorbeeld hierboven aangeroepen met `Date(1, 1, 1900).is_leap_year()`, en geeft Python automatisch `self`, in dit geval het object `Date(1, 1, 1900)`, als het eerste argument aan de methode `is_leap_year` mee.
:::

### De initiële klasse `Date` testen

Om een gevoel te krijgen van hoe je je nieuwe datatype kan testen kan je de volgende aanroepen proberen:

```ipython
# maak een object met de naam d met de constructor
In [1]: d = Date(2, 12, 2020)  # gebruik een dag naar keuze...

# toon de waarde van d
In [2]: d
Out[2]: 02-12-2020

# een voorbeeld met print
In [3]: print('Mijn favoriet dag is', d)
Mijn favoriete dag is 02-12-2020

# maak een ander object met de naam d2
# van *dezelfde dag*
In [4]: d2 = Date(2, 12, 2020)

# toon daar de waarde van
In [5]: d2
Out[5]: 02-12-2020   # _ziet_ er hetzelfde uit...

# zijn ze hetzelfde?
In [6]: d == d2
Out[6]: False

# even kijken naar hun plaats in het geheugen
In [7]: id(d)           # geef het geheugenadres terug
Out[7]: 47833453502416  # jouw resultaat zal anders zijn...

In [8]: id(d2)          # nogmaals...
Out[8]: 47833453658184  # en dit zal anders zijn dan hierboven!

# kijken of d2 in een schrikkeljaar valt...
In [9]: d2.is_leap_year()
Out[9]: True

# nog een object van het type Date
# een toekomstige nieuwjaarsdag
# Vraag: wat ga je op deze dag doen?
In [10]: d3 = Date(1, 1, 2021)

# kijken of d3 in een schrikkeljaar valt
In [11]: d3.is_leap_year()
Out[11]: False
```

## De klasse `Date` uitbreiden

Nu we hebben gezien hoe de klasse `Date` tot nu toe werkt gaan we deze klasse uitbreiden met extra methodes.

### De methode `copy`

Eerst gaan we een nieuwe methode, `copy(self)` toevoegen aan de klasse `Date`. Je kan hiervoor onderstaande code kopiëren en plakken.

```python
def copy(self):
    """Returns a new object with the same day, month, year
       as the calling object (self).
    """
    dnew = Date(self.day, self.month, self.year)
    return dnew
```

Deze methode `copy` geeft een nieuw gemaakt object terug van het type `Date` met dezelfde dag, maand en jaar als het aanroepende object heeft. Onthoud dat het object dat de methode aanroept `self` heet, dus de dag van dat object is `self.day`, de maand is `self.month` en zo verder.

Aangezien je een nieuw object wilt aanmaken, *moet je de constructor aanroepen*! Dit is wat je ziet gebeuren in de methode `copy`: de aanroep `Date(self.day, self.month, self.year)` wordt door Python doorgestuurd naar de constructor `__init__`.

Probeer deze voorbeelden, die een toekomstige nieuwjaarsdag gebruiken. Eerst gebruiken we `copy` **niet**:

```ipython
In [1]: d = Date(1, 1, 2100)  # volgende eeuw!

In [2]: d2 = d

In [3]: id(d)
Out[3]: 47833249816416  # jouw geheugenadres zal anders zijn

In [4]: id(d2)
Out[4]: 47833249816416  # maar d2 heeft HETZELFDE geheugenadres als d!

In [5]: d == d2
Out[5]: True            # dus dit moet True zijn...
```

Hieronder kan je zien dat `copy` wel een deep copy maakt (in plaats van een kopie van alleen de verwijzing, of een "shallow" copy):

```ipython
In [2]: d = Date(1, 1, 2100)    # opnieuw beginnen...

In [3]: d2 = d.copy()

In [4]: d
Out[4]: 01/01/2100

In [5]: d2
Out[5]: 01/01/2100

In [6]: id(d)
Out[6]: 47833453483400  # jouw geheugenadres zal anders zijn

In [7]: id(d2)
Out[7]: 47833453658184  # maar d2 moet anders zijn dan d!

In [8]: d == d2
Out[8]: False           # dit moet dus False zijn...
```

### De methode `equals`

Voeg ook de methode `equals(self, d2)` toe aan de klasse `Date`, met behulp van deze code:

```python
def equals(self, d2):
    """Decides if self and d2 represent the same calendar date,
       whether or not they are the in the same place in memory.
    """
    if self.year == d2.year and self.month == d2.month and self.day == d2.day:
        return True
    else:
        return False
```

Deze methode moet `True` teruggeven als het aanroepende object (met de naam `self`) en het argument (met de naam `d2`) dezelfde kalenderdatum voorstellen.

Als ze een andere kalenderdatum voorstellen, moet de methode `False` teruggeven. De voorbeelden hierboven laten zien dat dezelfde kalenderdatum op verschillende plaatsen in het geheugen kan staan; in dat geval geeft de operator `==` `False` terug. Deze methode kan gebruikt worden om te zien of twee objecten dezelfde kalenderdatum voorstellen, onafhankelijk van de plaats waarop ze in het geheugen staan.

Probeer deze voorbeelden (nadat je de code opnieuw geladen hebt) om te zien hoe deze methode `equals` werkt.

```ipython
In [1]: d = Date(1, 1, 2100)

In [2]: d2 = d.copy()

In [3]: d
Out[3]: 01-01-2100

In [4]: d2
Out[4]: 01-01-2100

In [5]: d == d2
Out[5]: False       # dit moet False zijn!

In [6]: d.equals(d2)
Out[6]: True        # maar dit moet True zijn!

In [7]: d.equals(Date(1, 1, 2100))  # dit is ook goed!
Out[7]: True

In [8]: d == Date(1, 1, 2100)       # dit vergelijkt geheugenadressen
Out[8]: False                       # dus moet het False zijn
```

### De operator `==` herdefiniëren

In Python kan je ook standaardoperators definiëren voor je eigen klassen en objecten!

Omdat bijvoorbeeld het gedrag van de functie `equals` hierboven hetzelfde is als hoe we ***zouden willen*** dat de dubbel-gelijk-aan-operator, `==`, werkt, kunnen we dit gedrag definiëren door een methode `__eq__` toe te voegen. Merk op dat de naam ***twee*** underscores heeft aan weerszijden van `eq`. Dit geeft aan dat deze methode voor Python een speciale betekenis heeft, net zoals `__init__` en `__repr__`.

```python
def __eq__(self, d2):
    """Overrides the == operator so that it declares two of the same dates
        in history as ==.  This way, we don't need to use the awkward
        d.equals(d2) syntax...
    """
    if self.year == d2.year and self.month == d2.month and self.day == d2.day:
        return True
    else:
        return False
```

Voeg dit ook toe aan je klasse `Date`. Nu werkt `==` ook zoals je verwacht met objecten van het type `Date`!

Probeer het uit!!

## De klasse `Date` verder uitbreiden...

Hierna ga je in het practicum een aantal methodes zelf implementeren in de klasse `Date`. Deze zijn besproken in het college...

Vergeet niet een docstring toe te voegen aan de methodes die je schrijft! (Een *methode* is niets anders dan een functie die onderdeel is van een klasse die door een gebruiker gedefinieerd is.)

### De methode `is_before`

Voeg de methode `is_before(self, d2)` toe aan je klasse `Date`. Deze methode moet `True` teruggeven als het object dat de methode aanroept een kalenderdatum bevat die ***eerder*** is dan die van het argument `d2` (dit zal altijd een object van het type `Date` zijn). Als `self` en `d2` dezelfde datum voorstellen, moet de methode `False` teruggeven. Ook als `self` *later* is dan `d2` moet de methode `False` teruggeven.

:::{admonition,tip} Tip
Er zijn meerdere manieren om dit aan te pakken (sommige staan misschien in je aantekeningen!) Een mogelijke aanpak is om eerst de jaren te vergelijken: `self.year < d2.year`, daarna de maanden, daarna de dagen. Maar *vergelijk de maanden **alleen** als de jaren gelijk zijn*. Er is een soortgelijke voorwaarde voor de dagen (vergelijk ze alleen als de maanden en de jaren *beide* gelijk zijn).
:::

Om je methode `is_before` te testen, kan je zelf een aantal testgevallen maken.
Hier zijn een paar voorbeelden om mee te beginnen:

```ipython
In [1]: ny = Date(1, 1, 2021)    # nieuwjaar

In [2]: d = Date(2, 12, 2020)

In [3]: ny.is_before(d)
Out[3]: False

In [4]: d.is_before(ny)
Out[4]: True

In [5]: d.is_before(d)        # moet False zijn!
Out[5]: False
```

Herdefinieer ook de operator `<`, net zoals we met `__eq__` gedaan hebbe. De methodenaam hiervoor is `__lt__`. Nadat je dit gedaan hebt, kan je het testen met

```ipython
In [4]: d < ny
Out[4]: True
```

### De methode `is_after`

Voeg de methode `is_after(self, d2)` toe aan je klasse `Date`. Deze methode moet `True` teruggeven als het object dat de methode aanroept een kalenderdatum bevat die ***later*** is dan die van het argument `d2` (dit zal altijd een object van het type `Date` zijn). Als `self` en `d2` dezelfde datum voorstellen, moet de methode `False` teruggeven. Ook als `self` *eerder* is dan `d2` moet de methode `False` teruggeven.

Je kan `is_before` op ongeveer dezelfde manier schrijven als `is_after`, maar je kan ook bedenken hoe je `is_before` en `equals` kan *gebruiken* om `is_after` te schrijven...

Om je methode `is_after` te testen, kan je zelf een aantal testgevallen maken. Je kan bijvoorbeeld te testgevallen hierboven voor `is_before` omdraaien.

Vergeet niet om de operator `>` te herdefiniëren. De naam hiervan is `__gt__`.

### De methode `tomorrow`

Voeg de methode `tomorrow(self)` toe aan je klasse `Date`. Je hebt misschien college-aantekeningen om hierbij te helpen). Deze methode moet **NIETS TERUGGEVEN**! In plaats daarvan moet ze het aanroepende object **veranderen** zodat het een kalenderdag voorstelt die een dag later is dan degene die het eerst voorstelde. Dit betekent dat `self.day` sowieso verandert. Bovendien veranderen `self.month` en `self.year` misschien.

Je kan "goochelen" met je types en `fdays = 28 + self.is_leap_year()` gebruiken... of je kan deze truc vermijden, zodat de rest van de wereld je code ook nog begrijpt en een gewone `if`-`else` schrijven om hetzelfde effect te verkrijgen. Vergeet niet dat code voor mensen is en niet voor de computer! Die zou liever assembly lezen...

Daarnaast is een lijst `dim = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]` van het aantal dagen in elke maand handig om te gebruiken! Het maakt het makkelijk om te zien hoeveel dagen er in een gegeven maand (`self.month`) zijn

:::{admonition,notice} Waarom staat er een 0 aan het begin?
Zie je waarom de 0 aan het begin handig is? Bedenk nog eens hoe lijsten geïndexeerd worden...
:::

Om je methode `tomorrow` te testen, kan je zelf een aantal testgevallen maken. Hier zijn een aantal willekeurige gevallen om mee te beginnen:

```ipython
In [1]: d = Date(31, 12, 2020)

In [2]: d
Out[2]: 31-12-2020

In [3]: d.tomorrow()

In [4]: d
Out[4]: 01-01-2021

In [5]: d = Date(28, 2, 2020)

In [6]: d.tomorrow()

In [7]: d
Out[7]: 29-02-2020

In [8]: d.tomorrow()

In [9]: d
Out[9]: 01-03-2020
```


### De methode `yesterday`

Voeg de complementaire methode `yesterday(self)` toe aan je klasse `Date`. Deze methode moet net zoals `tomorrow` niets teruggeven. Ze moet het aanroepende object zo aanpassen dat dit één kalenderdag *voor* de oorspronkelijke dag representeert. Ook hier geldt dat `self.day` sowieso zal veranderen, en `self.month` en `self.year` mogelijk ook veranderen.

Om je methode `yesterday` te testen, kan je zelf een aantal testgevallen maken. Hier zijn de omgekeerde versies van de vorige tests:

```ipython
In [2]: d = Date(1, 1, 2021)

In [3]: d
Out[3]: 01-01-2021

In [4]: d.yesterday()

In [5]: d
Out[5]: 31-21-2020

In [6]: d = Date(1, 3, 2020)

In [7]: d.yesterday()

In [8]: d
Out[8]: 29-02-2020

In [9]: d.yesterday()

In [10]: d
Out[10]: 28-02-2020
```

### De methode `add_n_days`

Voeg de methode `add_n_days(self, n)` toe aan je klasse `Date`. Deze methode hoeft alleen maar niet-negatieve integers als waarde voor het argument `n` te kunnen verwerken. Deze methode moet net zoals de methode `tomorrow` niets teruggeven. In plaats daarvan moet het het aanroepende object ***veranderen*** zodat dit een datum `n` kalenderdagen *na* de oorspronkelijke datum voorstelt.

:::{admonition,warning} Let op
Kopieer hiervoor geen code uit de methode `tomorrow`!

Bedenk ***in plaats daarvan*** hoe je de methode `tomorrow` zou kunnen ***aanroepen*** in een `for`-lus om dit te implementeren!
:::

De methode moet bovendien alle datums van de startdatum tot en met de einddatum *afdrukken*. Onthoud dat de regel `print(self)` gebruikt kan worden om een object af te drukken vanuit één van de methodes van dat object. Hieronder zie je voorbeelden van de uitvoer.

Om je methode `add_n_days` te testen, kan je zelf een aantal testgevallen maken. Hier zijn een paar voorbeelden om mee te beginnen:

```ipython
In [1]: d = Date(2, 12, 2020)

In [2]: d.add_n_days(4)
02-12-2020  # de eerste afdrukken is optioneel...
03-12-2020
04-12-2020
05-12-2020
06-12-2020

In [3]: d
Out[3]: 06-12-2020    # d is veranderd!

In [4]: d = Date(2, 12, 2020)  # de oorspronkelijke Date opnieuw maken

In [5]: d.add_n_days(1318)
02-12-2020  # de eerste afdrukken is optioneel
03-12-2020
... heel veel datums overgeslagen ...
11-07-2024
12-07-2024

In [6]: d
Out[6]: 12-07-2024    # diploma-uitreiking! (als je nu in het eerste jaar zit...)
```

Je kan je eigen datumberekeningen testen met deze website: http://www.timeanddate.com/date/dateadd.html.

### De methode `sub_n_days`

Voeg de methode `sub_n_days(self, n)` toe aan je klasse `Date`. Deze methode hoeft alleen maar niet-negatieve integers als waarde voor het argument `n` te kunnen verwerken. Deze methode moet net zoals de methode `add_n_days` niets teruggeven. In plaats daarvan moet het het aanroepende object ***veranderen*** zodat dit een datum `n` kalenderdagen *voor* de oorspronkelijke datum voorstelt. Overweeg net zoals in het vorige geval `yesterday` en een `for`-lus te gebruiken om dit te implementeren!

De methode moet bovendien alle datums van de startdatum tot en met de einddatum **afdrukken**. Ook dit spiegelt het gedrag van de methode `add_n_days`. Hieronder zie je voorbeelden van de uitvoer.

Probeer bovenstaande testgevallen om te draaien!

#### Python-operators herdefiniëren

Er zijn ook twee Python-operators die erg goed passen bij de methodes `add_n_days` en `sub_n_days`; dit zijn `+=` en `-=`. Herdefinieer deze twee operators door onderstaande methodes te maken:

* `__iadd__(self, n)` voor `add_n_days(self, n)`; hiermee kan je `d += 1` of `d += 1000` gebruiken
* `__isub__(self, n)` voor `sub_n_days(self, n)`; hiermee kan je `d -= 1` of `d -= 1000` gebruiken

:::{admonition,tip} `return self`
Merk op dat om deze operators goed te laten werken, je `return self` moet toevoegen aan het eind van beide functies. (dit heeft te maken met de interne werking van Python...)
:::

:::{admonition,notice} Nog meer operators
De [Python-handleiding](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types) kan je vertellen welke operators je nog meer kan herdefiniëren.
:::

### De methode `diff`

Voeg de methode `diff(self, d2)` toe aan je klasse `Date`. Deze methode moet een integer teruggeven met het *aantal dagen* tussen `self` en `d2`. Je kan dit zien als het teruggeven van de integer die past bij

```python
self - d2
```

De operator voor aftrekken is `__sub__`; implementeer deze ook, naast de methode `diff`.

Datums zijn complexer dan getallen!! Het implementeren van `diff` is dus nog niet zo simpel. Zie hieronder voor meer tips.

:::{admonition,warning} Belangrijk
Deze methode moet `self` en `d2` **niet** veranderen!

In plaats daarvan moet je ***kopieën*** maken van `self` en `d2`; hierdoor worden de oorspronkelijke waardes niet aangepast.
:::

Maak een kopie van zowel `self` als `d2` en gebruik en verander alleen de kopieën! Gebruik bijvoorbeeld

```python
self_copy = self.copy()
d2_copy = d2.copy()
```

Net zoals bij aftrekken is ook hier het teken van het resultaat belangrijk! Vergelijk deze drie gevallen:

* Als `self` en `d2` dezelfde kalenderdatum voorstellen moet de methode `diff(self, d2)` de waarde `0` teruggeven.
* Als `self` ***eerder*** is dan `d2`, moet de methode `diff(self, d2)` een **negatieve** integer gelijk aan het aantal dagen tussen de twee datums teruggeven.
* Als `self` ***later*** is dan `d2`, moet de methode `diff(self, d2)` een **positieve** integer gelijk aan het aantal dagen tussen de twee datums teruggeven.

Twee manieren om het probleem aan te pakken die je beter ***niet*** kan gebruiken!

* Probeer ten eerste niet de jaren, maanden en dagen tussen de twee datums af te trekken; dit is *veel*  te foutgevoelig; en er zijn te veel uitzonderingen!
* Probeer ook niet om `add_n_days` en `sub_n_days` te gebruiken om je methode `diff` te implementeren. Alle mogelijke verschillen proberen is te langzaam!
* Implementeer `diff` in plaats daarvan op dezelfde *manier* als deze twee methodes: door `yesterday` en `tomorrow` te gebruiken in een lus.

Wat bedoelen we hiermee?

* Je kan de methodes `tomorrow` en `yesterday` die je al geschreven hebt gebruiken; in combinatie met `while`-lussen!
* De test voor de `while`-lus zou iets kunnen zijn als `while day1.is_before(day2):` of het kan `is_after` gebruiken...
* Gebruik een telvariabele om het aantal keer dat je door de lus gaat voordat je klaar bent bij te houden: dit is je antwoord (misschien met een minteken)!
* Je kan nog een keer kijken naar je uitwerking van de functie `while_pi` uit [week 9](../week9/wk9ex3.md).

Om je methode `diff` te testen, moet je een aantal gevallen testen. Hier zijn twee paren datums die relatief dicht bij elkaar liggen:

```ipython
In [1]: d = Date(2, 12, 2020)       # nu...

In [2]: d2 = Date(19, 7, 2021)      # zomervakantie!

In [3]: d2.diff(d)
Out[3]: 229

In [4]: d.diff(d2)
Out[4]: -229

In [5]: d         # controleren dat ze niet veranderd zijn!
Out[5]: 12-02-2020

In [6]: d2        # controleren dat ze niet veranderd zijn!
Out[6]: 19-7-2021

# Probeer deze twee datums die over een schrikkeldag springen...
In [7]: d3 = Date(1, 12, 2019)

In [8]: d4 = Date(15, 3, 2020)

In [9]: d4.diff(d3)
Out[9]: 105

# Probeer deze twee paren datums die ver uit elkaar liggen:
In [10]: d = Date(2, 12, 2020)

In [11]: d.diff(Date(1, 1, 1899))
Out[11]: 44530

In [12]: d.diff(Date(1, 1, 2100))
Out[12]: -28884
```

Gebruik je methode `diff` om je eigen, of iemand anders, leeftijd in dagen te berekenen!
Je kan andere verschillen controleren op https://www.timeanddate.com/date/duration.html.

### De methode `dow`

Voeg de methode `dow(self)` toe aan je klasse `Date`. Deze methode moet een string teruggeven die de dag van de week (`dow`, *day of week*) teruggeeft van het `Date`-object dat de methode aanroept. Dat wil zeggen dat de methode één van de volgende strings teruggeeft: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday` of `Sunday`.

:::{admonition,tip} Tips
Hoe zou het kunnen helpen om de `diff` vanaf een ***bekende*** dag te vinden, zoals de uitzonderlijk populaire trouwdag, *zondag* 10 oktober 2010?

Hoe zou de modulusoperator (`%`) kunnen helpen?
:::

Om je methode `dow` te testen, kan je zelf een aantal testgevallen maken. Hier zijn een paar voorbeelden om mee te beginnen:

```ipython
In [1]: d = Date(7, 12, 1941)

In [2]: d.dow()
Out[2]: 'Sunday'

In [3]: Date(28, 10, 1929).dow()     # dow is toepasselijk voor de beurskrach van de Dow Jones!
Out[3]: 'Monday'

In [4]: Date(19, 10, 1987).dow()     # idem: nog een krach! Kijk uit voor maandagen in oktober!
Out[4]: 'Monday'

In [5]: d = Date(1, 1, 2100)

In [6]: d.dow()
Out[6]: 'Friday'
```

## Inleveren

Gefeliciteerd; je hebt een klasse `Date` gemaakt waarvan de objecten de verschillen en dagen van de week kunnen berekenen voor alle kalenderdagen!

Bovendien heb je dit practicum voltooid. Vergeet niet je code in `wk10ex1.py` in Gradescope in te leveren!

Als je wilt, kun je nu gaan berekenen op welke weekdag je verjaardag, of nieuwjaarsdag, het meeste voorkomt in de komende eeuw...

## Optioneel: Je klasse `Date` gebruiken...

We gaan de klasse `Date` nuttig gebruiken! We gaan onder andere kijken naar de meest waarschijnlijke dag van de week van je verjaardag, en de statistieken van onze kalender voor de dertiende dag van de maand.

Probeer de volgende code en beantwoord de drie onderstaande vragen.

Bekijk de volgende functie; je kan deze het beste onderaan het bestand `wk10ex1.py` plakken. Zorg ervoor dat je deze ***BUITEN*** de klasse `Date` plakt. Zorg er dus voor dat deze functie helemaal naar links uitgesprongen is (niet één keer naar rechts ingesprongen, want het is geen methode van de klasse `Date`)!

Deze functie `ny_counter` gebruikt een datastructuur die een *dictionary* heet. Misschien heb je deze nog niet gezien; we behandelen deze tijdens het college en het huiswerk.

Kort gezegd wordt een dictionary `d` geïnitialiseerd met de code `d = {}` (let op de accolades), maar de werking lijkt heel erg op een gewone lijst. Het grote verschil is dat je *strings* kan gebruiken om de lijst te indexeren!
Hierdoor zijn dictionaries erg geschikt om te tellen hoe vaak een string voorkomt. Hier is een voorbeeld van precies die manier van gebruiken:

```python
def ny_counter():
    """Looking ahead to 100 years of NY celebrations..."""

    dowd = {}              # dowd is een dictionary van weekdagen
    dowd["Sunday"] = 0     # een waarde van 0 voor Sunday
    dowd["Monday"] = 0     # en zo verder...
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0

    # 100 jaar vooruit kijken...
    for year in range(2021, 2121):
        d = Date(1, 1, year)   # nieuwjaar opvragen
        print('Huidige datum is', d)
        s = d.dow()        # dag van de week zoeken
        dowd[s] += 1       # tellen

    print('Totalen zijn', dowd)

    # we zouden dowd hier kunnen teruggeven
    # maar dat is nu niet nodig
    # return dowd
```

Proneer deze functie `ny_counter` nu uit:

```ipython
In [1]: ny_counter()
```

### Vraag 1

Gebruik commentaar boven deze functie `ny_counter` in je bestand `wk10ex1.py` om in één of twee zinnen te beschrijven wat `ny_counter` berekent.

### Vraag 2

Gebruik de functie `ny_counter` als voorbeeld om een functie te schrijven die dezelfde gegevens berekent voor ***je volgende 100 verjaardagen***. Voeg de resultaten toe in commentaar onder je functie.

### Vraag 3: Wat zijn de meest voorkomende weekdagen?

Schrijf op basis van deze twee voorbeelden een functie die dezelfde gegevens berekent voor de ***dertiende van elke maand*** voor de komende 400 jaar. Aangezien onze huidige kalender zichzelf elke 400 jaar herhaalt zullen je resultaten de frequentieverdeling zijn voor de dertiende van de maand zolang we hetzelfde kalendersysteem blijven gebruiken. Op welke dag van de week valt de dertiende het vaakst? Zijn er meer dagen die het meeste voorkomen?

Merk op dat je hiervoor *volledig* gebruik zult maken van de processorcapaciteit van je computer. Het kan helpen om een informatieregel af te drukken, bijvoorbeeld elk jaar, zodat je ziet dat je functie nog steeds bezig is. **Dit zal vermoedelijk nog steeds te langzaam zijn!** Je zult merken dat de datums steeds langer duren, en als je klaar bent met wachten kan je de veranderingen hieronder aanbrengen om je functie te versnellen (Control-C stopt het programma zodat je niet hoeft te wachten tot het klaar is).

Het probleem zit in `dow`; het controleert steeds grotere periodes. Hoe zou je `dow` kunnen aanpassen zodat de berekening in dit geval sneller is?

Eén manier om dit te doen is het schrijven van een **alternatieve** functie in je klasse `Date` met de naam
`dow2(self, ref_date)`. Het tweede argument van `dow2` is dan ***elke vergelijkingsdatum die op de geschikte dag van de week valt***. Je roept dan

```python
d.dow2(ref_date)
```

aan in plaats van `d.dow()`.

Dit is het idee: maak een variabele `ref_date` aan het begin van de je functie om de dertienden te tellen. Geef deze variabele initieel de waarde van de vergelijkingsdatum die je in je originele functie `dow` gebruikt. Terwijl je in de toekomst aan het zoeken bent, kijk je bij elke dertiende of die op *dezelfde dag van de week valt als je oorspronkelijke `ref_date`*. Als hij op dezelfde dag valt als de oorspronkelijke `ref_date`, vervang je de waarde van de variabele `ref_date` door de nieuwe datum; namelijk, de dertiende van de maand die je net gevonden hebt.

Hierdoor hoef je `dow2` nooit aan te roepen voor periodes van meer dan een jaar; hierdoor zou het programma binnen een minuut klaar moeten zijn. Je zult merken dat de dertiende vaker een vrijdag is dan sommige andere dagen van de week...!

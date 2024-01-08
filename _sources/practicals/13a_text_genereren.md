# Tekst genereren met Markovprocessen

## Opdracht 1: 
Gebruik deze code als beginpunt voor je bestand, en noem het `wk12pr1.py`:

```python

# functie #1
#
def create_dictionary(filename):
    pass


# functie #2
#
def generate_text(d, n):
    pass


#
# Je gegenereerde essay van ongeveer 500 woorden (plak in de onderstaande triple-quoted strings):
#
"""



"""
#
#
```

## Python's dictionaries gebruiken...

Je doel bij deze opgave is om een programma te schrijven dat uit zichzelf "betekenisvolle" tekst kan genereren! Je gaat dit doel bereiken door het schrijven van een algoritme dat met behulp van zogeheten Markovprocessen tekst genereert.

Python heeft een ingebouwd datatype (klasse) die *dictionary* heet. Probeer de voorbeelden hieronder op de Pythonshell om een idee te krijgen van hoe dictionary's werken. In het kort zijn het containers zoals lijsten, maar dan beter! (Of in ieder geval anders...)

```ipython
In [1]: d = {}   # maakt een lege dictionary, d
# Let op dat dit ACCOLADES zijn!

In [2]: d[1993] = 'haan'     # nl.wikipedia.org/wiki/Chinese_astrologie

In [3]: d
Out[3]: {1993: 'haan'}       # 1993 is een SLEUTEL, 'haan' is een WAARDE

In [4]: d[1994] = 'hond'

In [5]: d
Out[5]: {1993: 'haan', 1994: 'hond'}

In [6]: d[1994]
Out[6]: 'hond'

In [7]: d[1995]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 1995

In [8]: 1994 in d             # in controleert alleen SLEUTELS
Out[8]: True

In [9]: 1995 in d
Out[9]: False

In [10]: d.keys()
Out[10]: dict_keys([1993, 1994])

In [11]: d.values()
Out[11]: dict_values(['haan', 'hond'])

In [12]: d.items()
Out[12]: dict_items([(1993, 'haan'), (1994, 'hond')])
```

Deze opgave gebruikt een Python-dictionary om tekst te modelleren; en daarna te genereren.

### Voorbeeldcode

Je kan een paar voorbeelden vinden van hoe je in Python dictionary's kan gebruiken om tekst te analyseren met een *vocabulaireteller* (in tegenstelling tot een woordenteller) in [deze voorbeeldcode; dit kan je gebruiken als naslagwerk voor wat je nodig hebt...](assets/file_and_dictionary_examples.py)

## Tekst genereren met Markovprocessen

Hier is het basisidee: het Nederlands is een taal met veel structuur. Woorden hebben de neiging (sterker, de verplichting) om alleen in bepaalde volgordes voor te komen. De regels van de grammatica bepalen welke combinaties van verschillende stukken spraak toegestaan zijn. De zin "De kat klimt de trap op" heeft bijvoorbeeld een geldige woordvolgorde. "Trap de op kat klimt" heeft dat niet. Daarnaast beperkt de semantiek (de betekenis van een woord of zin) de mogelijke combinaties nog verder. "De trap klimt de kat op" is een perfect geldige zin, maar het is wel onzinnig en je zal deze woordvolgorde in de praktijk zeer waarschijnlijk niet tegenkomen.

Zelfs zonder de formele regels van het Nederlands te kennen, of de betekenis van Nederlandse woorden, kunnen we een idee krijgen van welke woordcombinaties geldig zijn door simpelweg naar correcte Nederlandse teksten te kijken en de combinaties van woorden te bekijken die in de praktijk voorkomen. We kunnen daarna op basis van onze observaties *nieuwe* zinnen maken door willekeurig woorden te selecteren aan de hand van hoe vaak ze in die volgorde voorkomen. Bekijk bijvoorbeeld de volgende tekst:

"Ik houd van rozen en anjers. Ik dacht, ik koop rozen voor mijn verjaardag."

Als we beginnen met het kiezen van het woord "ik", kunnen we zien dat "ik" gevolgd kan worden door "houd", "dacht" en "koop", met in deze tekst een gelijke kans. We kiezen één van deze woorden willekeurig en voegen die toe aan onze zin, bijvoorbeeld "ik koop". Hierdoor moet het volgende woord "rozen" zijn, omdat in onze voorbeeldtekst "koop" altijd (dat wil zeggen, één keer) gevolgd wordt door "rozen". Als we dit proces herhalen kunnen we bijvoorbeeld de zin "ik koop rozen en anjers" krijgen. Merk op dat dit een geldige Nederlandse zin is, maar niet één die we eerder hebben gezien. Andere nieuwe zinnen die we zouden kunnen genereren zijn "ik houd van rozen voor mijn verjaardag" en "ik koop rozen voor mijn verjaardag".

Formeel gezegd heet het proces dat we gebruiken om deze zinnen te genereren een *Markovproces van de eerste orde*. Een Markovproces van de eerste orde is een proces waarin de toestand op tijdstip *t*+1 (dat wil zeggen, het volgende woord) alleen afhankelijk is van de toestand op tijdstip *t* (dat wil zeggen, het vorige woord). In een Markovproces van de tweede orde is het volgende woord afhankelijk van de *twee* vorige woorden, en zo verder. Ons voorbeeld hierboven was een proces van de eerste orde omdat de keuze voor het volgende woord alleen afhing van het huidge woord. Merk op dat de waarde van het volgende woord onafhankelijk is van de positie van het woord, en alleen maar afhangt van zijn directe geschiedenis. Dat wil zeggen dat het niet uitmaakt of we het 2e woord kiezen of het 92e. Het maakt alleen uit wat het 1e of 91e woord is, respectievelijke.

## Teksten analyseren en genereren

In het eerste deel van deze opgave implementeer je een Markovproces van de eerste orde om teksten mee te genereren. Om deze functie te schrijven heb je twee andere functies nodig: (1) één om een bestand te verwerken en een dictionary van geldige woordcombinaties te maken en (2) een andere om de nieuwe tekst daadwerkelijk te genereren.

Als je hier geen speciale code voor schrijft zal je programma woorden als verschillend beschouwen zelfs als ze alleen maar verschillen in hoofdletters of leestekens. Dit is voor deze opgave geen probleem: `spam`, `Spam` en `spam.` (met punt erachter) mag je allemaal als verschillende woorden beschouwen.

Hier zijn de details over de twee functies die je moet schrijven:

## Opracht 2:  De functie `create_dictionary`

`create_dictionary(filename)` krijgt een string als argument mee, wat de naam van een tekstbestand is dat wat voorbeeldtekst bevat. Het moet een dictionary teruggeven waarvan de sleutels woorden zijn die in de tekst voorkomen en waarvan de waardes lijsten met woorden zijn die op het sleutelwoord kunnen volgen. Merk op dat je een manier moet bedenken waarop je bijhoudt hoe vaak een woord op het sleutelwoord volgt. Dat wil zeggen dat als het woord "fiets" twee keer zo vaak wordt gevolgd door het woord "kopen" als door het woord "repareren", je dictionary deze informatie ook moet bevatten. Je kan bijvoorbeeld het woord meerdere keren opnemen in de lijst.

De dictionary die wordt teruggegeven door `create_dictionary` geeft je de mogelijkheid om woord `t`+1 te kiezen als je woord `t` al hebt. Maar hoe kies je het *eerste* woord, als je geen bestaand woord hebt die je als sleutel voor
de dictionary kan gebruiken?

Om dit geval te kunnen afhandelen, moet je dictionary de string `$` bevatten; dit is het *startsymbool*. Het eerste woord in het bestand moet op deze string "opvolgen". Bovendien moet elke string die volgt op het laatste woord van een zin deze string opvolgen. Een woord dat een zin eindigt wordt gedefinieerd als elk woord waarvan het laatste teken een punt `.`, een vraagteken `?` of een uitroepteken `!` is.

:::{admonition} Bepalen of een woord eindigt op een leesteken
:class: tip

Het makkelijkst is om `w[-1]` te controleren. We zijn alleen geïnteresseerd in `'.'`, `'?'` en `'!'`.

Onthoud dat, als je `or` gebruikt, je elke test helemaal moet uitschrijven, bijvoorbeeld,
```python
if w[-1] == '.' or w[-1] == '?' or ...
```

Je herinnert je misschien het alternatief met `in` (van het controleren van klinkers in een vorige opgave...): `if w[-1] in '.!':`
:::

### Strategie

Merk op dat in het college *bijna* de hele functie besproken is. Hier zie je de voorbeeldcode, met de uitleg daaronder:

```python
d = {}
pw = '$'

for nw in words:
    if pw not in d:
        d[pw] = [nw]
    else:
        d[pw] += [nw]

    pw = ...
```

Als de gegeven zin `Ik lust spam. Ik eet taart!` is, moet de inhoud van d na het uitvoeren van deze code gelijk zijn aan `{'$': ['Ik', 'Ik'], 'Ik': ['lust', 'eet'], 'lust': ['spam'], 'eet' : ['taart']}`.

Verder heb je code gezien waarmee je woorden kan tellen:

```python
def vocab_count(filename):
    """vocabulary-counting program"""

    # bestand lezen
    f = open(filename)
    text = f.read()
    f.close()

    # woorden tellen
    words = text.split()
    print("Er zijn", len(words), "woorden")

    # het aantal keer dat elk woord voorkomt tellen
    d = {}
    for w in words:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1
    print("Er zijn", len(w), "verschillende woorden")

    # d teruggeven voor andere code
    return d
```

In het bijzonder heb je *wel* de code om bestanden te lezen bovenaan de functie nodig, maaar **niet** de code om woorden te tellen daaronder...

In plaats daarvan heb je de code over `nw` en `pw` (deze staan respectievelijk voor "new word" en "previous word") uit het andere fragment nodig. Hier is het resultaat:

```python
pw = '$'

for nw in words:
    if pw not in d:
        d[pw] = [nw]
    else:
        d[pw] += [nw]

    pw = nw

    # controleer hierna of de nieuwe pw eindigt op een
    # leesteken -- als dat _wel_ zo is zet dan pw op '$'
```

Het enige wat in dit voorbeeld nog niet staat is hoe je woorden die eindigen op een leesteken kan verwerken. Dat moet je zelf bedenken (maar er staan tips in het commentaar hierboven)...

### Je code controleren...

Om je code te controleren, kan je de volgende tekst in een plat tekstbestand zetten (bijvoorbeeld in een nieuw ".txt"-bestandsvenster in VSCode):

```text
A B A. A B C. B A C. C C C.
```

Sla dit bestand op als `test.txt` in dezelfde directory waar je bestand `wk10ex3.py` staat. Kijk dan of je dictionary `d` hetzelfde is als in het voorbeeld hieronder:

```ipython
In [2]: d
Out[2]:
{'$': ['A', 'A', 'B', 'C'],
 'A': ['B', 'B', 'C.'],
 'B': ['A.', 'C.', 'A'],
 'C': ['C', 'C.']}
```

De elementen in elke lijst hoeven niet in dezelfde volgorde te staan, maar ze moeten wel in dezelfde hoeveelheden aanwezig zijn als hierboven voor elk van de vier sleutels, 'A', 'C', 'B' en '$'.

Hier is de inhoud van het ***taarten***-bestand, met de naam `a.txt`, uit het college.

```text
Ik wil taarten en 42 en spam.
Ik krijg toch spam en taarten voor
de vakantie? Ik wil 42 taarten!
```

:::{admonition} Teksteditor op Mac
:class: tip

Als je de Teksteditor op een Mac gebruikt, moet je *Opmaak ... Converteer naar platte tekst* gebruiken; je hebt een `.txt`-bestand nodig, geen `.rtf`-bestand.
:::

Het is slim om te controleren of de dictionary die je als uitvoer krijgt met dit bestand hetzelfde is als
degene die je het college hebt gezien (merk op dat de volgorde van de sleutels kan veranderen):

```ipython
In [1]: d = create_dictionary('a.txt')

In [2]: d
Out[2]:
{'krijg': ['toch'],
'voor': ['de'],
'wil': ['taarten', '42'],
'toch': ['spam'],
'Ik': ['wil', 'krijg', 'wil'],
'spam': ['en'],
'42': ['en', 'taarten!'],
'$': ['Ik', 'Ik', 'Ik'],
'taarten': ['en', 'voor'],
'de': ['vakantie?'],
'en': ['42', 'spam.', 'taarten']}
```

## Opdacht 3:  De functie `generate_text`

`generate_text(d, n)` krijgt een dictionary met woordovergangen (gemaakt door je functie `create_dictionary` van hierboven) mee, en een positieve integer `n`. Hiermee moet `generate_text` een string van `n` woorden afdrukken.

Het eerste woord moet willekeurig gekozen zijn uit de woorden die kunnen volgen op het startsymbool `"$"`. Bedenk dat `random.choice` een willekeurig element ***uit een lijst*** kan kiezen! Het tweede woord moet willekeurig gekozen worden uit de lijst woorden die kunnen volgen op het eerste woord, en zo verder. Als een gekozen woord eindigt op een punt `.`, een vraagteken `?` of een uitroepteken `!`, moet de functie `generate_text` deze gebeurtenis herkennen en een nieuwe zin beginnen door opnieuw een willekeurig woord te kiezen dat kan volgen op een `"$"`.

Laat `'$'` niet terugkomen in de uitvoertekst; het is alleen een interne markering voor je functie.

In deze opgave hoef je de woorden in het tekstbestand *niet* te ontdoen van leestekens. Laat leestekens staan zoals ze in de tekst voorkomen; en als je woorden genereert, hoe je je geen zorgen te maken als de gegenereerde tekst niet eindigt op een geldig leesteken, dat wil zeggen, je zou kunnen eindigen zonder punt, maar dat is prima. De tekst die je genereert zal niet perfect zijn, maar je kan verrast worden door hoe goed hij is!

Je mag ervan uitgaan dat er geen leestekens op zichzelf (of andere randgevallen) in de invoer voorkomen. Het beste kan je bij zulke onverwachte gevallen gewoonweg een nieuwe zin beginnen. In het specifieke geval dat je bij een woord uitkomt dat alleen maar als het laatste woord in je trainingsdata voorkomt (dat wil zeggen dat er geen opvolgende woorden zijn), dan kan je gewoon verder gaan met het genereren van tekst vanaf het startsymbool `$`.

Hier zijn twee voorbeelden die de dictionary `d` van hierboven gebruiken. Je eigen uitvoer zal verschillen omdat de woorden willekeurig gekozen zijn, maar ze zouden er op moeten lijken.

```ipython
In [3]: generate_text(d, 20)
Out[3]: B C. C C C. C C C C C C C C C C C. C C C. A

In [4]: generate_text(d, 20)
Out[4]: A B A. C C C. B A B C. A C. B A. C C C C C C.
```

## Een gegenereerd essay van 500 woorden!

Voor het laatste deel van deze opdracht moet je een interessant tekstbestand vinden, hiermee een Markovmodel van de eerste orde maken, en zelf wat tekst genereren! Een kunstmatig essay dus.

Voeg onderin je bestand een triple-quoted string (commentaar) toe met:

* De naam van het bronbestand (en auteur, als die er is) die je gebruikt hebt om je essay te genereren (je hoeft de brontekst zelf **niet** toe te voegen!).
* Minstens 500 woorden gegenereerde tekst.
* Wijs ons bovenaan de string graag op erg mooie stukjes proza die je hebt gegenereerd. 🙂

Je kan zelf kiezen welke invoertekst je wilt gebruiken, en die mag ook best Engels zijn! Je kan bijvoorbeeld willekeurige [scenes uit het werk van Shakespeare](https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt) gebruiken... ook kindergedichtjes kunnen (soms) goed werken. Je kan ook songteksten, speeches, of je eigen werk gebruiken; alles is mogelijk.

:::{admonition} Waarschuwing
:class: warning

Probeer gegenereerde essays niet te gebruiken als *echte* essays!
:::

:::{admonition} Platte-tekstbestanden
:class: tip

De makkelijkste manier om een platte-tekstbestand te maken dat je als invoer kan gebruiken is door de tekst te kopiëren van waar je hem gezien hebt via het menu of Control-C (Command-C op een Mac), en daarna een leeg tekstbestand te openen met Kladblok (Windows) of Teksteditor (Mac). Sla je `.txt`-bestand met platte tekst, bijvoorbeeld `spam.txt`, op in dezelfde map als je bestand `wk10ex3.py`.
:::

:::{admonition} Teksteditor op Mac
:class: warning

Teksteditor slaat bestanden standaard op als *rich text format* of `.rtf`. Je kan dit aanpassen door *Opmaak ... Converteer naar platte tekst* te kiezen. Doe dit om te zorgen dat je een `.txt`-bestand met platte tekst krijgt.
:::

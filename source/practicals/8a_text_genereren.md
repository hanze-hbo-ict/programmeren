# Tekst genereren met Markovprocessen

Gebruik deze code als beginpunt voor je bestand:

```python
# functie #1
#
def create_dictionary(filename):
    pass


# functie #2
def generate_text(words_follow, n_words):
    pass


#
# Je gegenereerde essay van ongeveer 500 woorden (plak in de onderstaande triple-quoted strings):
#
"""


"""
#
#
```

## Python's dictionaries gebruiken

In dit practicum schrijf je een programma dat zelf "betekenisvolle" tekst kan genereren! Je schrijft daarvoor een algoritme dat tekst genereert met zogeheten Markovprocessen.

Je gebruikt een Python-dictionary om tekst te modelleren en daarna te genereren.

### Voorbeeldcode

Een *vocabulaireteller* analyseert tekst met Python-dictionaries, in tegenstelling tot een woordenteller. Voorbeelden staan in {download}`deze voorbeeldcode; dit kan je gebruiken als naslagwerk voor wat je nodig hebt... <assets/file_and_dictionary_examples.py>`. Gebruik die voorbeelden als naslagwerk.

## Tekst genereren met Markovprocessen

Het Nederlands heeft veel structuur. Woorden kunnen alleen in bepaalde volgordes voorkomen. De grammatica bepaalt welke combinaties van zinsdelen toegestaan zijn. De zin "De kat klimt de trap op" heeft bijvoorbeeld een geldige woordvolgorde. "Trap de op kat klimt" heeft dat niet. Daarnaast beperkt de betekenis van een woord of zin de mogelijke combinaties nog verder. Die betekenis heet de semantiek. "De trap klimt de kat op" is volgens de grammatica een geldige zin. Toch is hij onzinnig: je zal deze woordvolgorde in de praktijk waarschijnlijk niet tegenkomen.

We kunnen ook zonder kennis van de Nederlandse regels of woordbetekenissen onderzoeken welke woordcombinaties geldig zijn. Daarvoor kijken we naar correcte Nederlandse teksten: welke combinaties van woorden komen daarin voor? Daarna maken we op basis daarvan *nieuwe* zinnen. We kiezen de woorden willekeurig, op basis van hoe vaak ze in die volgorde voorkomen. Bekijk bijvoorbeeld de volgende tekst:

"Ik houd van rozen en anjers. Ik dacht, ik koop rozen voor mijn verjaardag."

We beginnen met het woord "ik". Daarna kan "houd", "dacht" of "koop" volgen, in deze tekst met gelijke kans. We kiezen één van deze woorden willekeurig en voegen die toe aan onze zin, bijvoorbeeld "ik koop". Het volgende woord moet dan "rozen" zijn. In onze voorbeeldtekst volgt dat altijd op "koop": die combinatie komt één keer voor. Als we dit proces herhalen kunnen we bijvoorbeeld de zin "ik koop rozen en anjers" krijgen. Merk op dat dit een geldige Nederlandse zin is, maar niet één die we eerder hebben gezien. Andere nieuwe zinnen die we zouden kunnen genereren zijn "ik houd van rozen voor mijn verjaardag" en "ik koop rozen voor mijn verjaardag".

We genereren deze zinnen met een *Markovproces van de eerste orde*. Daarin hangt de toestand op tijdstip *t*+1 alleen af van de toestand op tijdstip *t*. Hier is de volgende toestand het volgende woord, en de vorige toestand het vorige woord. In een Markovproces van de tweede orde is het volgende woord afhankelijk van de *twee* vorige woorden, en zo verder. Ons voorbeeld hierboven was een proces van de eerste orde omdat de keuze voor het volgende woord alleen afhing van het huidige woord. De keuze voor het volgende woord hangt alleen af van zijn directe geschiedenis, niet van zijn positie. Het maakt dus niet uit of we het 2e of het 92e woord kiezen. Alleen het vorige woord telt: respectievelijk het 1e of het 91e woord.

## Teksten analyseren en genereren

In het eerste deel van dit practicum implementeer je een Markovproces van de eerste orde om teksten mee te genereren. Daarvoor schrijf je twee functies: (1) één om een bestand te verwerken en een dictionary van geldige woordcombinaties te maken, en (2) een andere om met die dictionary de nieuwe tekst te genereren.

Als je hier geen speciale code voor schrijft zal je programma woorden als verschillend beschouwen zelfs als ze alleen maar verschillen in hoofdletters of leestekens. Dit is voor dit practicum geen probleem: `spam`, `Spam` en `spam.` (met punt erachter) mag je allemaal als verschillende woorden beschouwen.

Hier zijn de details over de twee functies die je moet schrijven:

## Opdracht 1: De functie `create_dictionary`

`create_dictionary(filename)` krijgt een string als argument: de naam van een tekstbestand met voorbeeldtekst. De functie moet een dictionary teruggeven. De sleutels zijn woorden uit de tekst. De waarde bij elke sleutel is een lijst met woorden die op dat woord kunnen volgen. Houd ook bij hoe vaak een woord op het sleutelwoord volgt. Volgt "kopen" bijvoorbeeld twee keer zo vaak op "fiets" als "repareren"? Dan moet die verhouding ook in je dictionary staan. Je kan daarvoor een woord meerdere keren opnemen in de lijst.

De dictionary die wordt teruggegeven door `create_dictionary` geeft je de mogelijkheid om woord `t`+1 te kiezen als je woord `t` al hebt. Maar hoe kies je het *eerste* woord, als je geen bestaand woord hebt die je als sleutel voor de dictionary kan gebruiken?

Om dit geval af te handelen, moet je dictionary de string `$` bevatten: het *startsymbool*. In de lijst bij deze sleutel staat het eerste woord van het bestand. Ook elk woord dat na het laatste woord van een zin komt, hoort in deze lijst. Een woord sluit een zin af als het laatste teken een punt `.`, een vraagteken `?` of een uitroepteken `!` is.

:::{admonition} Bepalen of een woord eindigt op een leesteken
:class: tip

Het makkelijkst is om `word[-1]` te controleren. We zijn alleen geïnteresseerd in `'.'`, `'?'` en `'!'`.

Onthoud dat, als je `or` gebruikt, je elke test helemaal moet uitschrijven, bijvoorbeeld,

<!-- codecontrole:skip -->

```python
if word[-1] == '.' or word[-1] == '?' or ...
```

Je herinnert je misschien het alternatief met `in` (van het controleren van klinkers in een vorige opgave...): `if word[-1] in '.?!':`
:::

### Strategie

Merk op dat in het college *bijna* de hele functie besproken is. Hier zie je de voorbeeldcode, met de uitleg daaronder:

```python
words_follow = {}
previous_word = "$"

for new_word in words:
    if previous_word not in words_follow:
        words_follow[previous_word] = [new_word]
    else:
        words_follow[previous_word] += [new_word]

    previous_word = ...
```

Als de gegeven zin `Ik lust spam. Ik eet taart!` is, moet de inhoud van `words_follow` na het uitvoeren van de complete code gelijk zijn aan `{'$': ['Ik', 'Ik'], 'Ik': ['lust', 'eet'], 'lust': ['spam.'], 'eet': ['taart!']}`. De leestekens blijven aan de woorden vastzitten.

Verder heb je code gezien waarmee je woorden kan tellen. Het is de functie `count_vocab` uit de voorbeeldcode hierboven:

```python
def count_vocab(filename):
    """Telt hoe vaak elk woord in een bestand voorkomt.

    Opent het bestand met de naam filename, leest het en deelt het op in
    woorden. Telt daarna voor elk woord hoe vaak het voorkomt. Drukt het
    aantal woorden en het aantal verschillende woorden af, en geeft een
    dictionary terug met elk woord als sleutel en het aantal keer dat het
    voorkomt als waarde.

    Voorbeeld: count_vocab("a.txt") drukt 20 en 13 af en geeft
    {"Ik": 3, "wil": 2, "taarten": 2, "en": 3, ...}
    """
    with open(filename, encoding="utf-8") as file:
        text = file.read()

    words = text.split()
    print("Er zijn", len(words), "woorden.")

    vocab_count = {}
    for word in words:
        if word not in vocab_count:
            vocab_count[word] = 1
        else:
            vocab_count[word] += 1

    print("Er zijn", len(vocab_count), "*verschillende* woorden.\n")
    # op deze manier kunnen we de gegevens in vocab_count later gebruiken!
    return vocab_count
```

In PGM1 zag je bij [gegevensopslag](/lectures/6a_data) hoe ASCII tekens aan getallen koppelt. Ook UTF-8 is een tekencodering: een afspraak om opgeslagen bytes als tekens te lezen. Met `encoding="utf-8"` vertel je Python dat het dit bestand volgens UTF-8 moet lezen.

Daarvan heb je *wel* het begin nodig: het `with`-blok dat het bestand leest, en `words = text.split()`, dat de tekst in woorden opdeelt. De code om woorden te tellen daaronder, van de eerste `print` tot en met de `return`, heb je **niet** nodig.

In plaats daarvan heb je de code over `new_word` en `previous_word` uit het eerste fragment nodig, `words_follow = {}` inbegrepen. Hier is het resultaat:

```python
words_follow = {}
previous_word = "$"

for new_word in words:
    if previous_word not in words_follow:
        words_follow[previous_word] = [new_word]
    else:
        words_follow[previous_word] += [new_word]

    previous_word = new_word

    # controleer hierna of de nieuwe previous_word eindigt op een
    # leesteken -- als dat _wel_ zo is zet dan previous_word op '$'
```

Dit fragment toont alleen de lus. Vul daarin nog de verwerking van woorden met een eindleesteken aan; de tips staan in het commentaar. Voor de complete functie combineer je het inlezen en opsplitsen van de tekst met deze lus. Geef na de lus de opgebouwde dictionary `words_follow` terug met `return`, zoals opdracht 1 vraagt.

### Je code controleren

Om je code te controleren, kan je de volgende tekst in een plat tekstbestand zetten (bijvoorbeeld in een nieuw ".txt"-bestandsvenster in VSCode):

```text
A B A. A B C. B A C. C C C.
```

Sla dit bestand op als `test.txt` in dezelfde directory als je Python-bestand. Kijk dan of je dictionary `words_follow` hetzelfde is als in het voorbeeld hieronder:

```ipython
In [2]: words_follow
Out[2]:
{'$': ['A', 'A', 'B', 'C'],
 'A': ['B', 'B', 'C.'],
 'B': ['A.', 'C.', 'A'],
 'C': ['C', 'C.']}
```

De elementen in elke lijst hoeven niet in dezelfde volgorde te staan, maar ze moeten wel in dezelfde hoeveelheden aanwezig zijn als hierboven voor elk van de vier sleutels, 'A', 'C', 'B' en '$'.

Hier is de tekst die in het college als voorbeeld werd gebruikt.

```text
Ik wil taarten en 42 en spam.
Ik krijg toch spam en taarten voor
de vakantie? Ik wil 42 taarten!
```

:::{admonition} Teksteditor op Mac
:class: tip

Als je de Teksteditor op een Mac gebruikt, moet je *Opmaak ... Converteer naar platte tekst* gebruiken; je hebt een `.txt`-bestand nodig, geen `.rtf`-bestand.
:::

Het is slim om te controleren of de dictionary die je als uitvoer krijgt met dit bestand hetzelfde is als degene die je in het college hebt gezien (merk op dat de volgorde van de sleutels kan veranderen):

Het voorbeeldbestand dat hieronder wordt gebruikt kun je downloaden: {download}`a.txt <assets/a.txt>`. Het bevat drie zinnen over taarten en spam.

```ipython
In [1]: words_follow = create_dictionary('a.txt')

In [2]: words_follow
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

## Opdracht 2: De functie `generate_text`

`generate_text(words_follow, n_words)` krijgt een dictionary met woordovergangen mee. Die heb je met je functie `create_dictionary` van hierboven gemaakt. Het andere argument is een positieve integer `n_words`. Hiermee moet `generate_text` een string van `n_words` woorden afdrukken.

Het eerste woord moet willekeurig gekozen zijn uit de woorden die kunnen volgen op het startsymbool `"$"`. Bedenk dat `random.choice` een willekeurig element ***uit een lijst*** kan kiezen! Het tweede woord moet willekeurig gekozen worden uit de lijst woorden die kunnen volgen op het eerste woord, en zo verder. Eindigt een gekozen woord op een punt `.`, een vraagteken `?` of een uitroepteken `!`? Dan moet de functie `generate_text` een nieuwe zin beginnen. Kies daarvoor opnieuw een willekeurig woord dat op een `"$"` kan volgen.

Laat `'$'` niet terugkomen in de uitvoertekst; het is alleen een interne markering voor je functie.

In dit practicum hoef je de woorden in het tekstbestand *niet* te ontdoen van leestekens. Laat leestekens staan zoals ze in de tekst voorkomen. De gegenereerde tekst hoeft niet op een geldig leesteken te eindigen. Een tekst zonder punt aan het eind is dus ook goed. De tekst die je genereert zal niet perfect zijn, maar je kan verrast worden door hoe goed hij is!

Je mag ervan uitgaan dat er geen leestekens op zichzelf (of andere randgevallen) in de invoer voorkomen. Het beste kan je bij zulke onverwachte gevallen gewoonweg een nieuwe zin beginnen. Een woord kan alleen als laatste woord in je trainingsdata voorkomen. Het heeft dan geen opvolgende woorden. Ga in dat geval verder met het genereren van tekst vanaf het startsymbool `$`.

Hier zijn twee voorbeelden met de dictionary uit `test.txt` van hierboven. Je eigen uitvoer zal verschillen omdat de woorden willekeurig gekozen zijn, maar ze zouden er op moeten lijken:

```ipython
In [1]: words_follow = create_dictionary('test.txt')

In [2]: generate_text(words_follow, 20)
B C. C C C. C C C C C C C C C C C. C C C. A

In [3]: generate_text(words_follow, 20)
A B A. C C C. B A B C. A C. B A. C C C C C C.
```

## Een gegenereerd essay van 500 woorden

Voor het laatste deel van dit practicum moet je een interessant tekstbestand vinden, hiermee een Markovmodel van de eerste orde maken, en zelf wat tekst genereren! Een kunstmatig essay dus.

Je kan zelf kiezen welke invoertekst je wilt gebruiken, en die mag ook best Engels zijn! Je kan bijvoorbeeld willekeurige [scenes uit het werk van Shakespeare](https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt) gebruiken... ook kindergedichtjes kunnen (soms) goed werken. Je kan ook songteksten, speeches, of je eigen werk gebruiken; alles is mogelijk.

:::{admonition} Waarschuwing
:class: warning

Probeer gegenereerde essays niet te gebruiken als *echte* essays!
:::

:::{admonition} Platte-tekstbestanden
:class: tip

Maak een platte-tekstbestand om als invoer te gebruiken.

1. Kopieer de tekst van de plek waar je hem gezien hebt. Gebruik daarvoor het menu of Control-C (Command-C op een Mac).
2. Open daarna een leeg tekstbestand met Kladblok (Windows) of Teksteditor (Mac).
3. Sla je `.txt`-bestand met platte tekst, bijvoorbeeld `spam.txt`, op in dezelfde directory als je Python-bestand.
:::

:::{admonition} Teksteditor op Mac
:class: warning

Teksteditor slaat bestanden standaard op als *rich text format* of `.rtf`. Je kan dit aanpassen door *Opmaak ... Converteer naar platte tekst* te kiezen. Doe dit om te zorgen dat je een `.txt`-bestand met platte tekst krijgt.
:::

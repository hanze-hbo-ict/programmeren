# Tekstidentificatie

Dit is een vervolg van de context opdracht van week 13. [tekstidentificatie](13_text_id_milestone.md)

## De methode `normalize_dictionary`

De methode `normalize_dictionary(self, d)` krijgt één van de dictionary's uit het model mee en geeft een genormaliseerde versie terug, dat wil zeggen, een versie waar de som van alle waardes exact `1.0` is. Deze moet je teruggeven, niet afdrukken!

:::{admonition} Complexere methodes
:class: notice

Deze methode, en de volgende zijn algoritmisch complexer, dus we beschrijven ze in meer detail.
:::

:::{admonition} Tip
:class: tip

Je kan `d.values()` gebruiken om een lijst van alle waardes in een dictionary `d` te krijgen.
:::

:::{admonition} Belangrijkere tip
:class: tip

Je kan door alle *sleutels* van een dictionary `d` lussen met:

```python
for k in d:
    # doe iets met de sleutel k en de waarde d[k]
```
:::

Hier is een voorbeeld om de methode `normalize_dictionary` te testen:

```python
tm = TextModel()
d = {'a': 5, 'b': 1, 'c': 2}
nd = tm.normalize_dictionary(d)
assert nd == {'a': 0.625, 'b': 0.125, 'c': 0.25}
```

Dit moet wederom geen uitvoer geven.

## De methode `smallest_value`

De methode `smallest_value(self, nd1, nd2)` krijgt twee dictionary's `nd1` en `nd2` mee uit het model en geeft de kleinste positieve *waarde* terug die in de dictionary's samen voorkomt.

:::{admonition} Positieve waarde
:class: notice

Een positieve waarde is een waarde die groter is dan 0; 0 is dus **geen** positieve waarde.
:::

Als je deze gaat gebruiken zullen de invoerdictionary's vermoedelijk genormaliseerd zijn, vandaar de namen `nd1` en `nd2`, maar de methode moet ook werken als ze niet genormaliseerd zijn. Geef het resultaat terug, en druk het niet af!

Hier is een voorbeeld om de methode `normalize_dictionary` te testen:

```python
tm = TextModel()
d1 = {'a': 5, 'b': 1, 'c': 2}
nd1 = tm.normalize_dictionary(d1)
d2 = {'a': 15, 'd': 1}
nd2 = tm.normalize_dictionary(d2)
assert nd1 == {'a': 0.625, 'b': 0.125, 'c': 0.25}
assert nd2 == {'a': 0.9375, 'd': 0.0625}
assert tm.smallest_value(nd1, nd2) == 0.0625
```

## De methode `compare_dictionaries`

De methode `compare_dictionaries(self, d, nd1, nd2)` is het belangrijkste onderdeel van dit project. De method `compare_dictionaries` moet **twee kansen** berekenen: de kans dat de dictionary `d` voortkomt uit de verdeling van de gegevens in de genormaliseerde dictionary `nd1`, en dezelfde kans, maar dan voor `nd2`.

Met "kans" bedoelen we hier iets wat we de [log-waarschijnlijkheid](https://en.wikipedia.org/wiki/Log_probability) noemen. We laten de berekening hiervan zien aan de hand van een gedetailleerd voorbeeld: als je de ongenormaliseerde dictionary `d = {"a": 2, "b": 1, "c": 1, "d": 1, "e": 1}` wilt vergelijken met de genormaliseerde dictionary `nd1 = {"a": 0.625, "b": 0.125, "c": 0.25}` en de genormaliseerde dictionary `nd2 = {"a": 0.9375, "d": 0.0625}` dan moet je voor de vergelijking met `nd1` het volgende berekenen:

* Begin met `total = 0.0`
* Definieer een kleine waarde, `epsilon`, om gelijk te zijn aan de **helft** van de kleinste waarde in `nd1` en `nd2`
  samen (gebruik hier de methode `smallest_value` voor) en gebruik dan een lus om de rest te berekenen:
    * Voor de twee `'a'`'s voeg je `total += 2 * math.log2(0.625)` toe
    * Voor de ene `'b'` voeg je `total += 1 * math.log2(0.125)` toe
    * Voor de ene `'c'` voeg je `total += 1 * math.log2(0.25)` toe
    * Voor de ene `'d'` voeg je `total += 1 * math.log2(epsilon)` toe (`epsilon` was de helft van de kleinste waarde)
    * Voor de ene `'e'` voeg je `total += 1 * math.log2(epsilon)` toe (weer met die kleine waarde)
    * Dit moet uitkomen op `-16.356...` (zie hieronder)

De functie moet beide log-waarschijnlijkheden als een lijst teruggeven, bijvoorbeeld `[log1, log2]` (de eerste is de log-waarschijnlijkheden voor `nd1` en de tweede voor `nd2`).

:::{admonition} Logaritmes
:class: notice

`math.log2` is een functie die de logaritme met grondtal 2 berekent. De intuïtieve manier om hier als programmeur over na te denken is dat dit ongeveer hetzelfde is als de lengte van het getal in bits, dus binair geschreven. Als een getal dus twee keer zo groot wordt, wordt dit logaritme 1 meer. Omdat deze functie niet berekent kan worden voor het getal `0` gebruiken we als een waarde niet voorkomt in de modeldictionary een kleine, in principe arbitrair gekozen waarde, namelijk de helft van de kleinste waarde die voorkomt in beide modeldictionary's `d1` en `d2` samen.
:::

:::{admonition} Normaliseren
:class: danger

Je moet zorgen dat `nd1` en `nd2` allebei ***genormaliseerd*** zijn voordat de log-waarschijnlijkheden berekend worden; aan de andere kant hoeft `d` *niet* genormaliseerd te worden (sterker, hij *moet* niet genormaliseerd zijn).
:::

:::{admonition} Opmerkingen
:class: notice

Gebruik als een sleutel `k` wel in `d` maar niet in `nd1` voorkomt een log-waarschijnlijkheid gelijk aan `math.log2(epsilon)`; hetzelfde geldt als `k` niet in `nd2` voorkomt...
:::

Hier is een voorbeeld om je methide `compare_dictionaries` mee te testen:

```python
tm = TextModel()
d = {'a': 2, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
d1 = {'a': 5, 'b': 1, 'c': 2}
nd1 = tm.normalize_dictionary(d1)
d2 = {'a': 15, 'd': 1}
nd2 = tm.normalize_dictionary(d2)
assert nd1 == {'a': 0.625, 'b': 0.125, 'c': 0.25}
assert nd2 == {'a': 0.9375, 'd': 0.0625}
list_of_log_probs = tm.compare_dictionaries(d, nd1, nd2)
assert list_of_log_probs[0] == -16.356143810225277
assert list_of_log_probs[1] == -19.18621880878296
```

Deze getallen zijn gecontroleerd, dus we weten *echt* zeker dat ze kloppen!

:::{admonition} Hoe moet je deze negatieve getallen interpreteren?
:class: notice

De log-waarschijnlijkheid kan je het best zien als een "truc" om hele kleine kansen inzichtelijk te maken. De twee getallen hierboven, ongeveer -16.4 en -19.2, betekenen dat

* De kans dat je `d` krijgt door willekeurige keuzes te maken uit model `nd1` ongeveer **2<sup>-16.4</sup>** is (dat is ongeveer 0.00001156, oftwel 0.001156%)
* De kans dat je `d` krijgt door willekeurige keuzes te maken uit model `nd2` ongeveer **2<sup>-19.2</sup>** is (dat is ongeveer 0.00000166, oftwel 0.000166%)

Deze getallen zijn allebei heel erg klein, maar de eerste kans is ongeveer zeven keer groter dan de tweede! Anders gezegd, ondanks dat ze allebei negatief zijn *"wint" de grotere waarschijnlijkheid toch nog*; in zoverre dat die (vaak veel) waarschijnlijker is.
:::

## De methode `create_all_dictionaries`

De methode `create_all_dictionaries(self)` is een kleine, handige functie die eenvoudigweg alle dictionary's vult aan de hand van de string in `self.text`. We geven je hier een versie die je kan gebruiken.

Je moet het misschien een beetje aanpassen, voornamelijk door je eigen eigenschap toe te voegen!

```python
def create_all_dictionaries(self):
    """Create out all five of self's
       dictionaries in full.
    """
    self.make_sentence_lengths()
    self.make_word_lengths()
    self.make_words()
    self.make_stems()
    self.make_my_feature()
```

Hier zijn drie voorbeelden om dit mee te testen; voer deze tests ook uit, aangezien je deze drie modellen ook in
het laatste voorbeld gaat gebruiken! Maak hiervoor drie bestanden.

1. Maak een bestand `train1.txt` met dit kleine stukje tekst:

   ```text
   Dit is een korte zin. Dit is geen korte zin, omdat
   deze zin meer dan 10 woorden en een getal bevat! Dit is
   geen vraag, of wel?
   ```
2. Maak een bestand `train2.txt` met dit kleine stukje tekst:

   ```text
   Vele jaren later, staande voor het vuurpeloton, moest kolonel
   Aureliano Buendía denken aan die lang vervlogen middag, toen
   zijn vader hem meenam om kennis te maken met het ijs.
   ```
3. Maak een bestand `unknown.txt` met dit kleine stukje tekst:

   ```text
   Deze zin bevat een jaar met ijs! Winter is ijzig, of niet?
   ```

Voer daarna deze voorbeeldcommando's uit, of plak ze in onderdaan je bestand `textmodel.py` (of hoe je het bestand ook genoemd hebt!):

```python
print(' +++++++++++ Model 1 +++++++++++ ')
tm1 = TextModel()
tm1.read_text_from_file('train1.txt')
tm1.create_all_dictionaries()  # deze is hierboven gegeven
print(tm1)

print(' +++++++++++ Model 2+++++++++++ ')
tm2 = TextModel()
tm2.read_text_from_file('train2.txt')
tm2.create_all_dictionaries()  # deze is hierboven gegeven
print(tm2)


print(' +++++++++++ Onbekende tekst +++++++++++ ')
tm_unknown = TextModel()
tm_unknown.read_text_from_file('unknown.txt')
tm_unknown.create_all_dictionaries()  # deze is hierboven gegeven
print(tm_unknown)
```

Controleer of je uitvoer op onderstaand voorbeeld lijkt. *Het hoeft niet precis overeen te komen*; kleine verschillen in hoe je stemming, zinnen tellen of strings opschonen hebt gebouwd kan het resultaat wat veranderen:

```text
+++++++++++ Model 1 +++++++++++
Woorden:
{'geen': 2, 'een': 2, 'of': 1, 'is': 3, 'korte': 2, 'bevat': 1, 'deze': 1, 'vraag': 1, 'en': 1, 'zin': 3, '10': 1, 'getal': 1, 'dan': 1, 'meer': 1, 'omdat': 1, 'wel': 1, 'woorden': 1, 'dit': 3}

Woordlengtes:
{2: 6, 3: 10, 4: 4, 5: 6, 7: 1}

Stammen:
{'bevat': 1, 'woord': 1, 'een': 2, 'mer': 1, 'is': 3, 'getal': 1, 'of': 1, 'kort': 2, 'zin': 3, '10': 1, 'gen': 2, 'dez': 1, 'dan': 1, 'en': 1, 'omdat': 1, 'wel': 1, 'vrag': 1, 'dit': 3}

Zinslengtes:
{16: 1, 5: 1, 6: 1}

Leestekens:
{',': 2, '?': 1, '!': 1, '.': 1}
+++++++++++ Model 2+++++++++++
Woorden:
{'vuurpeloton': 1, 'denken': 1, 'die': 1, 'buendía': 1, 'hem': 1, 'middag': 1, 'meenam': 1, 'voor': 1, 'te': 1, 'kennis': 1, 'aureliano': 1, 'aan': 1, 'kolonel': 1, 'toen': 1, 'vader': 1, 'het': 2, 'lang': 1, 'maken': 1, 'staande': 1, 'jaren': 1, 'met': 1, 'vervlogen': 1, 'ijs': 1, 'moest': 1, 'zijn': 1, 'vele': 1, 'later': 1, 'om': 1}

Woordlengtes:
{2: 2, 3: 7, 4: 5, 5: 5, 6: 4, 7: 3, 9: 2, 11: 1}

Stammen:
{'om': 1, 'jar': 1, 'vuurpeloton': 1, 'die': 1, 'buendia': 1, 'hem': 1, 'middag': 1, 'meenam': 1, 'vervlog': 1, 'te': 1, 'kennis': 1, 'aureliano': 1, 'aan': 1, 'kolonel': 1, 'toen': 1, 'vader': 1, 'het': 2, 'lang': 1, 'vel': 1, 'denk': 1, 'staand': 1, 'ijs': 1, 'mak': 1, 'moest': 1, 'met': 1, 'zijn': 1, 'later': 1, 'vor': 1}

Zinslengtes:
{29: 1}

Leestekens:
{',': 3, '.': 1}
+++++++++++ Onbekende tekst +++++++++++
Woorden:
{'met': 1, 'een': 1, 'winter': 1, 'is': 1, 'ijzig': 1, 'ijs': 1, 'of': 1, 'jaar': 1, 'zin': 1, 'deze': 1, 'bevat': 1, 'niet': 1}

Woordlengtes:
{2: 2, 3: 4, 4: 3, 5: 2, 6: 1}

Stammen:
{'met': 1, 'jar': 1, 'een': 1, 'winter': 1, 'is': 1, 'ijzig': 1, 'ijs': 1, 'of': 1, 'zin': 1, 'bevat': 1, 'dez': 1, 'niet': 1}

Zinslengtes:
{5: 1, 7: 1}

Leestekens:
{',': 1, '?': 1, '!': 1}
```

Je gaat hierna het onbekende model `tm_unknown` vergelijken met de getrainde modellen `tm1` en `tm2`.

## De methode `compare_text_with_two_models`

De `compare_text_with_two_models(self, model1, model2)` methode moet de methode `compare_dictionaries` die hierboven beschreven is aanroepen voor elk van de teksteigenschapdictionary's in `self` en die vergelijken met de corresponderende (genormaliseerde!) dictionary's in `model1` en `model2`. Merk op dat deze drie objecten **allemaal** van de klasse `TextModel` zijn.

De methode `compare_text_with_two_models` moet:

* De vergelijkingsresultaten met log-waarschijnlijkheden van de vijf dictionary's afdrukken; hoe je dit precies wilt vormgeven en afdrukken mag je zelf bepalen (hieronder kan je een voorbeeld zien).
* Een systeem implementeren om te bepalen op welk van de twee modellen `self` meer lijkt, bijvoorbeeld door te kijken naar de meerderheid van de vijf dictionary's, of een gewogen som van de log-waarschijnlijkheden... Dit gedeelte van het algoritme mag je zelf invullen (hieronder is een aanpak gebruikt die naar de meerderheid kijkt.)
* Een "winnaar" bepalen, namelijk het model waar `self` meer op lijkt.

Hier mag je wel de resultaten afdrukken omdat er geen andere functies zijn die ze nog verder zullen gebruiken! (Je mag ze natuurlijk *ook* teruggeven als je zelf nog extra analyses wilt doen!)

Hier is een voorbeeld; het gebruikt de drie modellen uit het vorige voorbeeld:

* `tm1` (deze wordt gebruikt als `model1`)
* `tm2` (deze wordt gebruikt als `model2`)
* `tm_unknown` (deze wordt `self` omdat hierop `compare_text_with_two_models` wordt aangeroepen)

Dit voorbeeld vergelijkt de vijf dictionary's in `tm_unknown` met de vijf (genormaliseerde!) dictionary's in `tm1` en `tm2`. Toegegeven, onze voorbeelden hebben veel te weinig tekst voor een *echte* vergelijking, maar ze hebben wel de goede hoeveelheid tekst om te debuggen en te zorgen dat alles goed werkt!

Hier is het voorbeeld dat je kan uitvoeren:

```python
# de hoofdvergelijkingsmethode
tm_unknown.compare_text_with_two_models(tm1, tm2)
```

En hier is een voorbeeld van mogelijke resultaten; hoe het er bij jouw uitziet, de keuzes van het model en wat andere details kunnen natuurlijk anders zijn:

```text
Vergelijkingsresultaten:

            naam        model1        model2
            ----        ------        ------
           words        -59.51        -68.30
    word_lengths        -28.53        -31.46
sentence_lengths         -4.17         -5.17
           stems        -59.51        -67.30
     punctuation         -5.97         -7.06

-->  Model 1 wint op 5 features
-->  Model 2 wint op 0 features

+++++     Model 1 komt beter overeen!     +++++
```

## Ten slotte: je eigen teksten en analyse

Ten slotte vragen we je in dit project om je tekstanalysesysteem te **gebruiken**! Doe dit door:

1. Op zijn minst twee verschillende tekstmodellen te maken. Dit noemen we de "getrainde" modellen. Je moet één of meer teksten vinden om elk model te trainen. Als je meerdere teksten hebt, kan je ze allemaal in een enkel bestand zetten om ze te verwerken. Je kan bijvoorbeeld Shakespeare en J.K. Rowling vergelijken; er zijn veel andere vergelijkingen mogelijk! Je twee (of meer) getrainde modellen moeten een behoorlijke hoeveelheid tekst hebben. (Modellen die gebaseerd zijn op te weinig brontekst zijn meestal "fragiel", of "breekbaar"; ze zijn te veel gebaseerd op de eigenaardigheden van die ene brontekst.)
2. Ten minste twee andere "testteksten" kiezen die vergeleken worden met de twee getrainde modellen. Je kan hier je eigen tekst voor schrijven, of *andere* teksten gebruiken van dezelfde schrijver als één of beide van de getrainde modellen, of nog iets heel anders. Deze "testteksten" of "onbekende teksten" mogen korter zijn dan de teksten die je gebruikt voor de getrainde modellen.
3. Vergelijk je twee "testteksten" met de twee getrainde modellen (je krijgt dus vier vergelijkingen) en schrijf een
   kort verslagje over de resultaten, hoe je tot deze resultaten gekomen bent (inclusief hoe je hebt bepaald welk model wint als niet alle dictionary's het daar over eens waren) en of je die resultaten *verwachtte*...!

:::{admonition} Foutmelding
:class: warning

Als je een foutmelding krijgt die lijkt op deze: `codec can't encode character ... in ... position`, dan heb je misschien een andere *encoding* nodig in `read_text_from_file`; vermoedelijk moet je dan de aanroep naar `open` zo aanpassen: `open(filename, encoding='utf-8')`
:::

## De Opdracht

Voor dit project, moet je het volledige tekstidentificatiesysteem afmaken. Je programma zal dus teksten met elkaar kunnen vergelijken en bepalen wie het heeft geschreven met behulp van de  `compare_text_with_two_models` functie.

De oplevering, `oplevering.py`, moet een complete uitwerking van het project bevatten. Lever dit bestand, samen met je uitleg hierover in `oplevering.txt` en de tekstbestanden die je gebruikt hebt voor je analyse, in Gradescope in. In de uitleg moet je in ieder geval je zelfbedachte teksteigenschap toelichten, en de gestelde tekstanalysevragen beantwoorden.


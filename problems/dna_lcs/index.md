---
title: 42EnIk
description: DNA en Longest Common Subsequence (LCS)
file: dna.py
points: 25
---

# 42EnIk

## Inleiding

Je bent aangenomen als stagiair bij het genetische testbedrijf 42EnIk. Klanten sturen 42EnIk een speekselmonster (à 45 euro), het speeksel wordt verwerkt en het DNA wordt geëxtraheerd. 42EnIk vergelijkt vervolgens gebieden van het DNA van de klant met verschillende "referentiesequenties". Als bijvoorbeeld een bepaald gebied van je DNA gelijk is aan een bepaalde referentiesequentie, kan dat iets zeggen over je voorouders, immuniteit of aanleg voor een bepaalde ziekte, etc. De vergelijking tussen een gebied van jouw DNA en een referentiesequentie gebeurt met het algoritme voor de langste gemeenschappelijke reeks (*Longest Common Subsequence*, of LCS) dat je eerder hebt gezien (zie de opgave [*Caesar op orde!*](https://hanze-hbo-ict.github.io/programmeren/problems/caesar_op_orde.html)).

``` {note}
Hoewel [edit-afstand](https://en.wikipedia.org/wiki/Edit_distance) soms een betere afstandsmaat is dan LCS, blijkt dat als de twee te vergelijken sequenties dezelfde of een vergelijkbare lengte hebben (wat in dit geval meestal het geval zal zijn) de LCS zeer goed werkt.
```

Zorg ervoor dat je de functies die je gaat schrijven de juiste naam geeft en zorgvuldig test. Neem in elke functie een docstring op die moet aangeven wat de functie doet (teruggeeft) en eventueel wat de argumenten zijn en wat ze betekenen. Neem de gegeven assertions op om jouw oplossing te testen en vul deze eventueel aan zodat je zeker weet dat jouw oplossing correct is.

## LCS

Eerder heb je een LCS-functie geschreven die twee strings `s` en `t` accepteert en de langste gemeenschappelijke reeks van `s` en `t` teruggeeft. De onderstaande versie van deze functie geeft de *lengte* van de langste gemeenschappelijke reeks terug

```python
def lcs(s, t):
    """Find the length of the longest common
       subsequence of s and t.
    """
    if s == "" or t == "":  # Base case
        return 0

    if s[0] == t[0]:  # Match
        return 1 + lcs(s[1:], t[1:])  # 1 match point and then recurse
    else:  # No match
        lose_s = lcs(s, t[1:])  # Is this use-it-or-lose-it?
        lose_t = lcs(s[1:], t)
        return max(lose_s, lose_t)
```

en de volgende assertions testen deze functie:

```python
assert lcs("mens", "chimpansee") == 3  # "mns"
assert lcs("gattaca", "tacgaacta") == 5  # "gaaca"
assert lcs("wow", "wauw") == 2  # "ww"
assert lcs("", "wauw") == 0  # ""
assert lcs("abcdefgh", "efghabcd") == 4  # "abcd"
```

## Global Sequence Alignment: Deel 1

Hoewel de functie `lcs` de lengte van de langste gemeenschappelijke subsequentie berekent heeft 42EnIk meer nodig dan dat want ze willen hun klanten de *werkelijke* langste gemeenschappelijke subsequentie laten zien.

Jouw taak is het schrijven van een geheel nieuwe functie `better_lcs(s, t)`, die twee strings `s` en `t` als argumenten accepteert en een *list* met drie items teruggeeft. Het eerste element van deze list is een getal dat de lengte aangeeft van de langste gemeenschappelijke subsequentie van deze twee strings, de volgende twee elementen zijn een kopie van `s` en een kopie van `t` maar let op, in de kopieën worden de symbolen die *niet* worden gebruikt in de langste gemeenschappelijke subsequentie vervangen door `#` symbolen.

De volgende tests maken dit duidelijk, gebruik deze ook om jouw functie te testen:

```python
# De LCS heeft lengte 0. Zowel "x" als "y"
# worden niet in de LCS gebruikt.
assert better_lcs("x", "y") == [0, "#", "#"]

# De LCS heeft lengte 0. Geen van de vier letters in
# spam worden gebruikt en geen van de (nul) letters in ""
assert better_lcs("spam", "") == [0, "####", ""]

# Geen enkele letter in beide strings wordt gebruikt
# dus vervang alles met #
assert better_lcs("spa", "m") == [0, "###", "#"]

# De "ca"  is gemeenschappelijk, maar de "t"
# en "r" komen niet overeen
assert better_lcs("cat", "car") == [2, "ca#", "ca#"]

# De "ca" is nog steeds he langste gemeenschappelijke deel
assert better_lcs("cat", "lca") == [2, "ca#", "#ca"]

# "human" en "chimpanzee" hebben een LCS van lengte 4.
# De "u" in "human" wordt niet gebruikt en veel letters
# in "chimpanzee" ook niet.
assert better_lcs("human", "chimpanzee") == [4, "h#man", "#h#m#an###"]
```

Schrijf de functie `better_lcs` door de functie `lcs` te kopiëren en aan te passen. Houd het zo eenvoudig mogelijk en laat `better_lcs` *geen* hulpfuncties aanroepen. De ingebouwde functie `len` aanroepen is prima, maar `better_lcs` moet `lcs` *niet* aanroepen want dat zou het veel ingewikkelder maken dan nodig. Los dit net als bij de functie `lcs` ook *recursief* op, gebruik hier dus *geen* lussen.

``` {tip}
Bedenk dat als je een string wilt maken van een aantal kopieën van bijvoorbeeld de string `"spam"` je `"spam" + "spam" + "spam"` of het equivalent `"spam" * 3` kunt gebruiken. Hoewel je misschien geen 3 kopieën van `"spam"` wilt zal je waarschijnlijk wel een aantal `"#"` symbolen willen hebben!
```

## Global Sequence Alignment: Deel 2

<!-- vertaling controleren vanaf hier -->
Je gaat nu een iets andere versie van `better_lcs` schrijven, de functie `super_lcs` om sequenties uit te lijnen ([sequentiealignering](https://nl.wikipedia.org/wiki/Sequentiealignering)). Begin met het kopiëren van `better_lcs` en pas het verder aan.

Deze functie `super_lcs` zal ook een lijst met drie items teruggeven: de *lengte* van de langste gemeenschappelijke reeks, en *twee* strings. Deze twee strings zijn in wezen identiek aan de twee oorspronkelijke strings, behalve dat ze allebei *dezelfde* lengte hebben en een `-` (koppelteken) bevatten op elke plaats waar ze *niet* overeenkomen. Ook de functie `super_lcs` los je recursief op.

Hier zijn enkele voorbeelden van de functie `super_lcs` in actie:

```python
# De oplossing [0, "-x", "y-"] is ook goed
assert super_lcs("x", "y") == [0, "x-", "-y"]

# Let hier op, dit is een base case...
# Merk op dat de tweede string ---- is zodat het
# dezelfde lengte als de eerste heeft
assert super_lcs("spam", "") == [0, "spam", "----"]

# De oplossing  [2, "ca-t", "car-"] is ook goed
assert super_lcs("cat", "car") == [2, "cat-", "ca-r"]

assert super_lcs("hi", "schip") == [2, "--hi-", "schip"]
```

Merk op dat de twee resultaatreeksen altijd dezelfde lengte hebben! Hierdoor kunnen we de eerste boven de ander schrijven en zien hoe ze op elkaar aansluiten.

```text
--hi-
schip
```

Je ziet dat een langste gemeenschappelijke reeks wordt gevonden overal waar de twee strings op dezelfde positie overeenkomen. Als twee strings op een bepaalde positie niet overeenkomen, heeft precies één van die strings een `-` op die positie. Merk ook op dat het geheel van de twee strings (in dit geval `hi` en `schip`) in de uitvoer verschijnt, maar met enkele toegevoegde `-` symbolen waar geen overeenkomst is.

Hier volgt nog een voorbeeld waarbij twee DNA-fragmenten worden gebruikt:

```python
assert super_lcs("ATTGC", "GATC") == [3, "-ATTGC", "GAT--C"]
```

We zetten we deze twee uitvoerstrings boven elkaar om te zien wat hier gebeurt:

```text
-ATTGC
GAT--C
```

Je kan zien dat ATC een langste gemeenschappelijke reeks is. In het algemeen kunnen er verschillende gemeenschappelijke langste opeenvolgingen van gelijke lengte zijn, die resulteren in verschillende mogelijke correcte oplossingen. Jouw `super_lcs`-functie kan elke geldige oplossing rapporteren.

## Tot slot

De `super_lcs`-functie vindt een zogenaamde "globale uitlijning" (of *globale alignering*) van de twee DNA-strings. In het laatste voorbeeld hierboven geeft de oplossing

```text
-ATTGC
GAT--C
```

aan dat deze twee DNA-strings geëvolueerd kunnen zijn uit een gemeenschappelijke voorouder die ATC had op index 1, 2 en 5 en andere onbekende nucleotiden elders. De twee strings "ATTGC" en "GATC" kunnen uit deze gemeenschappelijke voorouder zijn geëvolueerd, maar met enkele extra nucleotiden ingevoegd en andere verwijderd.

<!-- RNA folding sequel: https://www.cs.hmc.edu/twiki/bin/view/CS5/BlackRNANew -->
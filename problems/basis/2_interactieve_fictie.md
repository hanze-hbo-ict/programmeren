---
title: "Interactieve fictie"
description: ""
csa-chapter: 1
csa-level: proficiency
file: wk2ba2.py
---

# Interactieve fictie

In deze opgave ga je interactieve fictie in Python schrijven, en met *interactieve* fictie bedoelen we een *kies-je-eigen-avontuur* programma!

## Een begin

Maak een nieuw bestand aan en en plak daar het onderstaande verhaal in. Sla het bestand op als `wk2ba2.py`

```python
"""
Titel voor je avontuur: De queeste naar taart.

Opmerkingen over hoe je het avontuuur kan "winnen" of "verliezen":
* kies de tafel om te winnen
* kies de deur om te verliezen
"""

import time

# change to 0.0 for testing or speed runs,
# ... or larger for dramatic effect!
delay = 0.0

username = input("Hoe noemt men u, edele avonturier? ")

print()
print("Welkom,", username, "in het Libracomplex, een labyrint")
print("van gewichtige wonderen en grote hoeveelheden ... taart!")
print()
print("Uw queeste: om een taart te vinden, en te eten!")
print()

flavor = input("Welke smaak zoekt u? ")
if flavor == "aardbeien":
    print("Uw wijsheid in taartkeuze is overweldigend!")
elif flavor == "kersen":
    print("Een Limburgse klassieker: een goede keuze, avonturier!")
else:
    print("Ieder zijn smaak...")

print()
print("Voorwaarts naar de queeste!\n\n")
print("Een gang strekt zich voor u uit; in het gedimde licht ziet u")
print("aan de ene kant een tafel met onduidelijke vormen en")
print("materialen, en aan de andere kant een deur op een kier,")
print("waarachter gelach --is dat gelach?-- van studenten klinkt.")

time.sleep(delay)

print()
choice1 = input("Kiest u de tafel of de deur? [tafel/deur] ")
print()

if choice1 == "tafel":
    print("Als u de tafel benadert lijkt de onduidelijke massa")
    print("een steeds grotere vorm aan te nemen, tot ...")

    time.sleep(delay)

    print("... ze herkenbaar wordt als een grote stapel verpakte")
    print("taarten, het karton strak geplooid. Uw uitdaging --en")
    print("honger-- is op smakelijke wijze opgelost.")
    print()
    print("Tot ziens,", username, "!")
else:
    print("U opent de deur en ziet een congregatie van wijze dames")
    print("en heren, die allen genieten van hun taken. Samenwerking")
    print("en vrolijkheid zijn hier in overvloed aanwezig, maar...")

    time.sleep(delay)

    print("...ze hebben ALLE taart opgegeten! Resten van dozen")
    print("liggen overal verspreid. U wordt duizelig en grijpt")
    print("naar een taart. Er is niets. U ademt uit en valt,")
    print("en ligt verslagen tussen de resten van dozen die u")
    print("langzaam bedekken tot verstikking volgt.")
    print()
    print("Vaarwel,", username, ".")
```

## Uitproberen

Open een *terminal* in VSCode (of anders) en probeer het bovenstaande verhaal uit door:

- `cd` naar de directory waar je jouw bestand hebt bewaard
- vervolgens `python wk1ex2b.py` te typen.
- als het laden gelukt is, start het programma.

### Herhalen

- Je kan nu je bestand bewerken, opnieuw opslaan en *pijltje omhoog* drukken om het opnieuw uit te voeren. Of type handmatig weer `python wk1ex2b.py`

:::{admonition} Nieuwe regel
:class: info

Het zal je opvallen dat `print()` (ongeacht het argument, bijvoorbeeld jouw tekst) altijd een nieuwe regel start. Dit gebeurt omdat standaard de karaktercombinatie `'\n'` aan de uitvoer wordt toevoegd. `'\n'` staat voor "newline" (nieuwe regel) en kent zelfs een hele [geschiedenis](https://en.wikipedia.org/wiki/Newline) (inclusief de oudewetse typemachine, en het wordt zeker niet alleen in Python gebruikt!).

Kan je in het voorbeeldverhaal het gebruik van `'\n'` ontdekken, en zou je dit misschien straks in jouw verhaal op een slimme manier kunnen gebruiken?
:::

## Opdracht

Je mag het taartverhaal gaan aanpassen en uitbreiden, of een geheel eigen interactief-fictieverhaal schrijven! Werk met iemand samen als je wilt (dit is optioneel) en maak je eigen avontuur.

Het bovenstaande verhaal bevat al twee controlestructuren met `if`:

1. een `if`-`elif`-`else`, en
2. een `if`-`else`.

De eis voor deze opdracht is dat je *elk* van de onderstaande vijf controlestructuren ("conditional statements") gebruikt, zodanig dat ze de richting van het verhaal beïnvloeden:

- een controlestructuur met `if`, precies één `elif` en `else`
- een controlestructuur met `if`, minstens twee `elif`'s en `else`
- een controlestructuur met `if` en `else` (en geen `elif`)
- een controlestructuur met `if` en minstens één `elif` (en geen `else`)
- een controlestructuur met `if` (en geen `elif` of `else`)

Verder geldt het volgende:

- de controlestructuren hoeven niet in de genoemde volgorde te worden toegepast
- je mag meer dan 5 controlestructuren gebruiken (als je wilt!)

:::{admonition} De kunst van de eenvoud
:class: notice

Houd het alsjeblieft eenvoudig! Andere fora of cursussen zijn beter geschikt voor vormen van creatieve expressie, hier gaat het ons voornamelijk om het verkennen van condities bij programmeren. Houd ook in gedachten dat mogelijk veel mensen jouw verhaal zullen lezen, uitvoeren en beoordelen (we kijken er naar uit!).

Wees verder ook bewust van de tijd die je aan deze opdracht besteedt, het is gemakkelijk om de tijd te verliezen. Het schrijven van het taartavontuur duurde ons al veel langer dan we oorspronkelijk hadden gedacht en het telt slechts *twee* controlestructuren!
:::

Veel plezier met avonturieren!
# VPool

![VPool](images/pool.png)

## Overzicht

Bij dit project schrijf je een volledig interactief 3D-spel dat op pool lijkt met VPython. Het hoeft alleen maar op pool te lijken; het hoeft niet de officielë regels van pool te implementeren en **het spel mag beduidend simpeler zijn dan een volledig poolspel.** Sterker nog, "interessante" interpretaties en grote variaties in het spel zijn van harte welkom!

Je spel hoeft niet pool te zijn, maar moet wel een 3D-interactie zijn die gebruik maakt van "GlowScript" VPython (op het web), met:

* Ten minste vier spelobjecten (naar eigen inzicht).
* Ten minste twee soorten botsingen, bijvoorbeeld botsingen van een punt en een lijn en van twee punten.
* Een vorm van besturing door de gebruiker.
* Een doel van het spel!
* Lever ook tekstbestanden (`begin.txt`, `milestone.txt` en `oplevering.txt`, respectievelijke) in waarin staat hoe je het spel moet spelen; deze horen natuurlijk bij het begin, de milestone en de oplevering.
* **Optioneel**: het kan geen kwaad een "docentmodus" te hebben waarmee het spel makkelijker te spelen (en te winnen) wordt!

### Documentatie

Hieronder hebben we een aantal handige links verzameld:

* [https://www.glowscript.org](https://www.glowscript.org/): De startpagina waar je inlogt en je programma's kan vinden
* [https://www.glowscript.org/docs/VPythonDocs/index.html](https://www.glowscript.org/docs/VPythonDocs/index.html): Documentatie voor alle objecten, scenes en andere functionaliteiten van VPython en GlowScript.
* [https://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/](https://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/): Voorbeelden (de linkertab die standaard geselecteerd is is voor GlowScript-voorbeelden, dus die heb je nodig).

### Begin *niet* met een leeg bestand!

Begin dit project niet met een leeg Python-bestand!!

Begin in plaats daarvan met de je resultaat practicumopdracht van week 11, over VPython, en maak aanpassingen daarin om je spel te implementeren!

De reden hiervoor is dat je je code elke keer als je een aanpassing maakt wilt uitvoeren, gewoon om te zien dat het werkt. Ga niet hele lappen code schrijven en dan pas testen; er zijn dan teveel dingen die fout kunnen gaan. Je zal dan toch alles moeten weghalen, in kleine stukjes terugzetten en ondertussen testen!

### Voorbeelden die je kan gebruiken...

GlowScript VPython heeft een aantal voorbeelden die je als beginpunt kan gebruiken:
https://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/
De linkertab is voor GlowScript, de aanpak die wij gebruiken (de andere tabs zijn voor dit project niet handig).

Naast het practicum van week 11 kan je deze verzameling [voorbeeldprogramma's](https://www.glowscript.org/#/user/ralfvandenbroek/folder/MyPrograms/)
voor GlowScript gebruiken die laten zien:

* [**Botsingen met muren:**](https://www.glowscript.org/#/user/ralfvandenbroek/folder/MyPrograms/program/voorbeeldbotsingmetmuur) Een voorbeeld waarin herkend wordt of een bol tegen de langste kanten van een muur (of een andere box) botst.
* [**Botsingen tussen twee bollen:**](https://www.glowscript.org/#/user/ralfvandenbroek/folder/MyPrograms/program/voorbeeldbotsingtussentweebollen) Een voorbeeld die controleert of er een botsing is tussen twee bollen en de snelheden realistisch aanpast.
* [**Botsingen tussen meerdere bollen:**](https://www.glowscript.org/#/user/ralfvandenbroek/folder/MyPrograms/program/voorbeeldbotsingtussenveelbollen) Een voorbeeld die controleert of er een botsing is tussen *meerdere* bollen en de snelheden realistisch aanpast.
* [**Willekeurig beginpunt:**](https://www.glowscript.org/#/user/ralfvandenbroek/folder/MyPrograms/program/voorbeeldwillekeurigestartpunten) Een voorbeeld dat laat zien hoe je een object willekeurig kan poisitioneren (in dit geval elke keer als er op `'r'` gedrukt wordt).

## Projecteisen

Dit is waarschijnlijk het project met de meeste vrijheid. Desondanks zijn er nog steeds een aantal eisen waaraan hij moet voldoen; maar je hebt ook veel vrijheid om je eigen draai aan je spel te geven!

Hier zijn de eisen (en een paar "niet-eisen") voor je spel:

* Als het spel start, moet het een driedimensionale "tafel" met een aantal "poolballen" tonen. Je spel mag iets heel  anders zijn dan pool, maar het moet iets van een afgebakend gebied en een aantal "actoren" hebben die daarin bewegen.

    Om het simpel te houden spreken we hieronder overal over "poolballen" als we de actoren of karakters in je spel bedoelen.

* Er moet een "speelbal" zijn, dat wil zeggen, een object dat de speler kan stoten of rechtstreeks besturen, en ten minste 3 andere objecten waarmee de speelbal kan interacteren.
* Er moeten "muren" of andere obstakels zijn die het speelveld begrenzen en waar spelobjecten niet doorheen kunnen. Ze moeten "lineaire botsingen" ondersteunen, dat wil zeggen, botsingen met een object die je als punt kan beschouwen en een uitgerekt object (een lijn of vlak). Een bal die de muur raakt moet de wet dat "hoek van inval is gelijk aan hoek van weerkaatsing" gebruiken.
* Er moeten een aantal gaten in de tafel zitten waar de ballen in kunnen vallen; of een ander idee van "doelen" of "bestemmingen". Specifiek moeten hier een aantal interacties tussen twee punten voor gemodelleerd en geimplementeerd worden, naast de interacties tussen een punt en een lijn hierboven.
* Om de benodigde interacties samen te vatten, je programma moet botsingen en weerkaatsingen kunnen afhandelen. Dat wil zeggen dat de verschillende objecten duidelijk zichtbaar met elkaar moeten interacteren. Hiervoor moet je spel
  in ieder geval een aantal botsingen tussen bollen ondersteunen, dus botsingen tussen twee objecten die gedefinieerd worden door een punt. Ze hoeven geen bollen te zijn, maar dat mag wel.
* Specifiek moeten ballen (karakters) niet door elkaar heen kunnen gaan. Het is leuk als je de botsingen tussen
  twee ballen natuurkundig correct simuleert, maar je mag ook andere benaderingen of totaal niet-natuurkundige botsingen gebruiken.
* Je spel moet wel ondersteunen dat meerdere ballen of objecten "tegelijk" bewegen. Als bijvoorbeeld bal `X` bal `Y`
  raakt dan zal vermoedelijk bal `X` (in een zekere richting) blijven bewegen, en begint bal `Y` te bewegen. Beide ballen moeten een poosje blijven bewegen. Bovendien kunnen bal `X` en bal `Y` nu ook andere ballen raken en die moeten dan ook een poosje bewegen. Het is in andere woorden niet voldoende als er altijd maximaal één bal beweegt in je programma.
* Zie de tip hieronder over hoe je botsingen tussen verschillende ballen tegelijk kan berekenen...
* Je moet een duidelijk beschreven doel van het spel hebben waarbij de voorwaarden om te "winnen" helder zijn. Het mag een spel voor één speler zijn, of voor twee, of een spel tegen de computer. Dit mag je zelf bepalen!
* ***Optioneel:*** het is geen slecht idee om een "docentmodus" te hebben waarbij het spel makkelijker te spelen of te winnen is.
* Je programma moet het de gebruiker vertellen als ze het spel gewonnen hebben!
* Je programma moet een makkelijk te gebruiken VPython-interface hebben (een combinatie van muis en toetsenbord)
  waarmee de gebruiker de "speelbal" vanuit verschillende richtingen (en optioneel met verschillende snelheden) kan spelen. Je hoeft geen echte "keu" te hebben, maar dit mag natuurlijk wel. Er zijn veel andere manieren om deze interface te maken en je mag er zelf één kiezen.
* Bij het inleveren van het begin, de milestone en de oplevering moet je een platte-tekstbestand `begin.txt`, `milestone.txt` of `oplevering.txt` meeleveren die het doel van het spel en hoe de interface werkt beschrijft. Je kan ook een korte samenvatting van de besturing tonen in het spel zelf.

Je mag natuurlijk extra functionaliteiten toevoegen als je dat wilt!

## Opmerkingen en tips

### Algemene tips

Hier zijn een paar tips die handig kunnen zijn:

* Vergeet niet dat de [naslagpagina](http://vpython.org/contents/docs/index.html) van VPython de volledige documentatie bevat.
* [Dit bestand `vpython_events.py` is een voorbeeld van een manier om beweging, toetsaanslagen en muisevents te verwerken.](../assets/vpython_events.py)

  :::{admonition} Opmerking
  :class: warning

  Deze code werkt niet in GlowScript, maar er zitten wel een paar handige ideeën in.
  :::

* Het VPython-object `arrow` kan gebruikt worden in plaats van het tekenen van een keu om de richting aan te geven   waarin de speelbal geraakt zal worden. De gebruiker kan bijvoorbeeld de muis en het toetsenbord gebruiken om een pijl   die op de speelbal gericht staat te draaien. Een andere gebruikersinvoer, bijvoorbeeld de spatiebalk, kan dan
  gebruikt worden om de speelbal te stoten.
* Bekijk de naslagpagina van VPython om te zien hoe je gebruikersinvoer van de muis en het toetsenbord kan lezen...
* Het gebruik van een vector om de richting waarin de bal beweegt bij te houden maakt de animatie makkelijker. Bovendien, als de bal dan een ander object raakt hoef je alleen maar de vector op de juiste manier bij te werken.

### Wrijving implementeren

Je zou kunnen overwegen om wrijving te implementeren door alle snelheden in elke stap te vermenigvuldigen met een constante die kleiner dan 1 is. Bedenk je dat de snelheid op deze manier nooit nul wordt! **Het kan frustrerend zijn** als het heel lang duurt voordat objecten stil komen te liggen; voordat je een volgende stoot maakt, bijvoorbeeld. Eén manier om deze frustratie te voorkomen is te kijken of er objecten zijn die erg langzaam bewegen en de snelheid daarvan gewoon op 0 te zetten. Als alle snelheden 0 zijn kan de volgende "zet" in het spel gedaan  worden.

### Botsingen tussen veel objecten

Het lijkt misschien dat je heel veel conditionele statements nodig hebt om botsingen tussen veel objecten te verwerken, maar je hoeft ze niet allemaal los te doen!

Wat je in deze situatie kan doen is eerst al je objecten te maken:

```python
ball1 = sphere(...)
ball2 = sphere(...)
ball3 = sphere(...)
ball4 = sphere(...)
...
```

en dan een lijst maken: `balls = [ball1, ball2, ball3, ball4, ...]`

Om dan botsingen te berekenen, kan je twee keer door deze lijst lussen. Merk op dat we elk paar maar één keer controleren!

```python
for i in range(len(balls)):
    for j in range(i + 1, len(balls)):  # merk op dat we beginnen bij i + 1
        if collide(balls[i], balls[j]):
            # doe iets toepasselijks...
```

Op deze manier kan je een enkele functie (`collide`) schrijven om te controleren of twee ballen botsen, en dat dan gebruiken voor alle paren...

Als je code wilt voor realistische "elastische" botsingen, kan je [dit codevoorbeeld](../support/vpython-collision.md) bekijken.

## Inleveren

Je moet dit project in drie stappen inleveren: het begin in week 11, de milestone in week 12 en ten slotte de oplevering.

(vpython-start)=
### Begin

Het begin, `begin.py`, moet aan de volgende eisen voldoen:

* Het bevat een werkende implementatie in VPython die aan minimaal de eisen van het practicum van week 11 voldoet.
* Er zijn geen verdere eisen dan die voor het practicum, maar je mag natuurlijk altijd vooruit werken, als je dat wilt.

Daarnaast moet de uitleg, `begin.txt`, aan de volgende eisen voldoen:

* Het bevat de namen van de teamleden en een korte beschrijving van je plan voor het spel; één paragraaf is hier wel genoeg.
* Het bevat een URL bevatten waar we je spel kunnen spelen. De code die we op deze URL vinden moet overeenkomen met de code in `begin.py`; het is prima als dit nu nog gewoon je uitwerking van het practicum van week 11 is!

Lever deze twee bestanden in Gradescope in als onderdeel van het huiswerk van week 11.

(vpython-milestone)=
### Milestone

De milestone, `milestone.py`, moet aan de volgende eisen voldoen:

* Het bevat een werkende implementatie in VPython die aan minimaal de eisen van het practicum van week 11 voldoet.
* Daarnaast moet je in dit bestand genoeg functies implementeren, inclusief docstings, zodat het spel *iets interessants* doet (zelfs als dat nog lang niet het volledige spel is).
* Specifiek moet je programma ten minste één "lineaire" botsing (een puntobject met een lijn of vlak) en ten minste één "bol"-botsing (een puntobject met een ander puntobject) bevatten.

Daarnaast moet de uitleg, `milestone.txt`, aan de volgende eisen voldoen:

* Het bevat de namen van de teamleden en een korte beschrijving van je plan voor het spel; één paragraaf is hier wel genoeg. Geef ook een beschrijving van het doel van het spel **en hoe we het dat doel moeten bereiken!**
* Het bevat een URL bevatten waar we je spel kunnen spelen. De code die we op deze URL vinden moet overeenkomen met de code in `milestone.py`.
* Het moet bovendien aanwijzingen bevatten over hoe we het spel zoals het nu is kunnen spelen, bijvoorbeeld, "op "s" drukken doet dit, de muis laat de gebruiker dat doen, enz."

Lever deze twee bestanden in Gradescope in als onderdeel van het huiswerk van week 12.

### Oplevering

Voor de oplevering, het laatste inlevermoment voor dit project, moet je je implementatie van je VPython-spel afmaken.

De oplevering, `oplevering.py`, moet aan de volgende eisen voldoen:

* Het bevat een werkende, "voltooide" implementatie van je spel in in VPython.
* Merk op dat een creatieve definitie van "voltooid" prima is; bugs en features kunnen erg op elkaar lijken, soms kan je zelfs niet eens onderscheiden.
* Dat gezegd hebbende, je programma moet ten minste vier objecten bevatten die met elkaar interacteren, en daarnaast
    * ten minste één "lineaire" interactie (een puntobject met een vlak of lijn)
    * ten minste één "bol"-interactie (een puntobject met een ander puntobject)
    * een doel voor het spel!

Daarnaast moet de uitleg, `oplevering.txt`, aan de volgende eisen voldoen:

* Het bevat de namen van de teamleden en een korte beschrijving van je plan voor het spel; één paragraaf is hier wel genoeg. Geef ook een beschrijving van het doel van het spel **en hoe we het dat doel moeten bereiken!**
* Het bevat een URL bevatten waar we je spel kunnen spelen. De code die we op deze URL vinden moet overeenkomen met de code in `oplevering.py`.
* Het moet ons ook vertellen hoe we het spel moeten gebruiken (zeker als er een "docentmodus" is)
* Het moet aanwijzingen bevatten over hoe we het spel zoals het nu is kunnen spelen, bijvoorbeeld, "op "s" drukken doet dit, de muis laat de gebruiker dat doen, enz."

Lever deze twee bestanden in Gradescope in.

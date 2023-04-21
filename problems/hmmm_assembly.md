# Hmmm... Assembly!

| Naam         | Beschrijving                                                     |
|--------------|------------------------------------------------------------------|
| Onderwerp    | Kennismaken met `hmmm` en assemblytaal                           |
| Bestandsnaam | `wk7ex1a.hmmm`, `wk7ex1b.hmmm`, `wk7ex1c.py`                     |
| Inleveren    | Lever jouw bestanden met de juiste bestandsnaam in op GradeScope |
| Opmerking    | Let op, deze opgave bestaat uit drie bestanden                   |

## Inleiding

Begin met het downloaden van de beginbestanden in [wk7ex1.zip via deze link](https://github.com/hanze-hbo-ict/programmeren/raw/master/problems/assets/wk7ex1.zip)

Bekijk ook de [documentatie van Hmmm, alle instructies in de Hmmm-taal](/support/hmmm) en de
<a href="../assets/hmmm/index.html">Hmmm-simulator</a>.

Dit practicum gaat over het programmeren in assemblytaal op een klein model van een computer genaamd Hmmm, de "Harvey Mudd Miniature Machine".

Er zijn drie onderdelen:

* Eerst bespreken we wat achtergrondinformatie. Hiermee kan je een aantal mogelijke valkuilen vermijden.
* Daarna moet je een Hmmm-programma schrijven die aftelt naar nul, beginnend bij de *derde macht* van een positief getal.
* In het laatste deel vragen we je een *pseudorandom-number generator* te schrijven in Hmmm...

Veel succes!

## Introductie in assemblytaal

Alhoewel het Hmmm-model geen fysieke computer is, is het ontwerp ervan fundamenteel hetzelfde als dat van moderne echte computers.

Waarom gebruiken we geen "echte" computer? Het is op dit moment niet de moeite waard om de instructieset van een echte processor te leren: ze bevatten allemaal veel dingen die niet essentieel zijn. (dan valt DNA nog wel mee!) Veel van die details zijn machine-specifiek: ze zijn niet van toepassing op andere computers.

De instructies in Hmmm zijn een subset die van toepassing zijn op **alle processoren**.

Hmmm heeft ongeveer 20 instructies. Moderne computes hebben tussen de twee en twintig keer zoveel instructies. Bij Computerarchitectuur, een vak voor studenten met als major Software Engineering of Network & Security Engineeering, maak je kennis met een "echte" assemblytaal die op Hmmm lijkt maar een grotere (en meer gecompliceerde) verzameling instructies heeft.

### Waarom programmeren we in assembly?

[XKCD heeft wel een reden](https://xkcd.com/409/)

Als een computer net gemaakt is, kan hij alleen maar binaire machinetaal uitvoeren. Het is heel lastig om in deze taal te programmeren! Daarom is het maken van een "assembler" meestal het eerste wat de ontwerpers van een computer (zoals Hmmm) doen.

Met deze assembler kunnen programmeurs nu programma's schrijven met instructies zoals `add`, `jump` en de andere instructies in Hmmm. De assembler zet deze instructies om naar de corresponderende binaire versies, oftewel de "machinetaal" die de schakelingen in de computer uitvoeren.

Als de assembler gemaakt is, is de volgende stap het gebruik van de assemblytaal om krachtigere talen te schrijven, zoals Python.

Geen zorgen, we gaan je niet vragen Python te implementeren in Hmmm! Het schrijven van een paar korte assemblyprogramma's kan je echter een idee geven van hoe je het zou aanpakken om zulke toepassingen te schrijven in de "moedertaal" van de processor.

Er is nog een reden om assembly te begrijpen. Alle programma's die je uitvoert in Python (of Java of C of ...) worden uiteindelijk gecompileerd (vertaald) naar assembly zodat de computer ze kan uitvoeren. Leren programmeren in Assembly zorgt ervoor dat je begrijpt wat er **echt** gebeurt in de machine als je je programma uitvoert.

### Wat is het verschil tussen registers en geheugen?

Hmmm heeft 16 registers genaamd `r0` tot en met `r15`, en 256 geheugenlocaties ("RAM"). Een echte processor heeft meestal (ongeveer) hetzelfde aantal registers als Hmmm, misschien een paar keer meer, maar heeft heel veel RAM-geheugen, normaal gesproken in de orde van grootte van miljoenen of miljarden geheugenlocaties die hij kan aanspreken.

Registers zijn waar de computer zijn berekeningen daadwerkelijk ***uitvoert***. Registers bevatten de beperkte hoeveelheid data die de computer in zijn "hoofd" kan onthouden.

RAM-geheugen is waar alle andere data, ***en het programma zelf***, te vinden zijn. Je kan RAM zien als een "kladblok" waar de computer veel informatie onthoud die hij anders niet kan onthouden.

### Een nadere blik op de Hmmm-instructies

Elke instructie vertelt de computer in principe wat te doen met zijn registers (getallen optellen, etc.). Als de instructie voltooid is, haalt de computer de volgende instructie uit het geheugen. We spreken af dat het programma vanaf geheugenadres 0 in het geheugen wordt gezet.

Zoals bij de meeste computers "werken" de instructies van Hmmm op *registers*. Als je naar de collegeslides kijkt, zal je zien dat er instructies zijn zoals `add`, die drie registers meekrijgen als argument, bijvoorbeeld:

```asm
add r3 r1 r2
```

De waardes in de rechtertwee registers, `r1` en `r2`, worden opgeteld en het resultaat wordt opgeslagen in het linkerregister `r3`.

Deze instructie zou in Python als `r3 = r1 + r2` geschreven worden. Op dezelfde manier werken de instructies `sub` (aftrekken), `mul` (vermenigvuldigen) en vele anderen geheel op registers.

Er zijn een aantal uitzonderingen! De belangrijkste zijn `jumpn`, `addn` en `setn`. Merk op dat elk van deze instructies eindigt op de letter n. Dit betekent dat elk van deze instructies een *getal* als argument meekrijgt. Als voorbeeld geeft het getal dat meegegeven wordt aan de instructie `jumpn` aan naar welke regel het programma zal springen. De hierop lijkende instructies `jltzn`, `jgtzn`, `jnezn`, `jeqzn` krijgen allemaal een register *en* een getal mee. `jltzn r2 42` springt bijvoorbeeld naar regel 42 *als de waarde in het register `r2` kleiner is dan nul*.

De instructies `addn` en `loadn` werken op dezelfde manier. Simpel gezegd telt de instructie `addn r5 42` het getal 42 op bij de bestaande waarde van register `r5` en slaat het resultaat weer op in register `r5`.

Merk op dat de instructie `addn rX -1` een makkelijke manier is om 1 van een register af te trekken.

De instructie `setn r3 42` zet gewoon de waarde `42` in register `r3`; dit is ook handig...

Laten we beginnen met Hmmm!

## Hmmm downloaden en uitvoeren

Om Hmmm uit te voeren, moet je het volgende zipbestand downloaden:

* [wk7ex1.zip](https://github.com/hanze-hbo-ict/programmeren/raw/master/problems/assets/wk7ex1.zip), de map met alle benodigde bestanden, inclusief `wk7ex1.hmmm` en `wk7ex1b.hmmm`.

Pak dat bestand uit en je krijgt een map `wk7ex1` met een aantal bestanden erin.

### Probeer het uit!

1. Probeer Hmmm uit door naar de map `wk7ex1` te `cd`'en die je gedownload en uitgepakt hebt.
2. Voer daarna het gebruikelijke commando uit op de command line: `ipython`
3. Type daarna `run hmmm wk7ex1a.hmmm` om Hmmm zelf uit te voeren. Hmmm zal `wk7ex1a.hmmm` assembleren en uitvoeren.

:::{admonition} Werkt het niet?
:class: notice

Misschien werk je op Windows en moet je de map ***uitpakken*** voordat je de bestanden opent.

Of je hebt misschien het bestand `wk7ex1a.hmmm` verplaatst uit die map; dat werkt niet, je moet de *hele map* verplaatsen!
:::

Dit is hoe `wk7ex1a.hmmm` eruit ziet:

```asm
# wk7ex1a.hmmm is een voorbeeldprogramma dat
#   1) de gebruiker om invoer vraagt
#   2) doortelt vanaf dat getal
#   3) eeuwig door blijft gaan...
#
# Naam:
#

# Practicumopgave #1: Bouw dit programma om naar "aftellen tot de derde macht"
# Zie de practicumbeschrijving voor details

00 read r1          # lees getal van de gebruiker in r1
01 write r1         # druk de waarde van r1 af
02 addn r1 1        # voeg 1 toe aan r1
03 jumpn 01         # spring naar regel 01
04 halt             # stopt nooit! [gebruik ctrl-c]
```

Nadat je `run hmmm wk7ex1a.hmmm` hebt getypt zou je iets als dit moeten zien:

```asm
----------------------​
| ASSEMBLY SUCCESSFUL |
----------------------

0: 0000 0001 0000 0001             00 read r1          # lees getal van de geb
1: 0000 0001 0000 0010             01 write r1         # druk de waarde van r1
2: 0101 0001 0000 0001             02 addn r1 1        # voeg 1 toe aan r1
3: 1011 0000 0000 0001             03 jumpn 01         # spring naar regel 01
4: 0000 0000 0000 0000             04 halt             # stopt nooit! [gebruik
```

Daarna zie je:

```text
Enter number:
```

Alles heeft gewerkt en het programma draait. Het vraagt je om een getal in te voeren (dit komt door de instructie `read r1` aan het begin van het programma)

Typ `32000` in en druk op return. Je zou de simulator omhoog moeten zien tellen vanaf `32000` of welk getal je ook ingevoerd hebt. Als hij bij de maximumwaarde, `32767`, aankomt, stopt hij (omdat het getal *overflowt*!)

:::{admonition} Overflow
:class: notice

We hebben bij Programmeren I besproken dat integers in een computer maar een beperkt aantal bits tot hun beschikking hebben; omdat de maximumwaarde hier `32767` is, kunnen we constateren dat het aantal bits dat een integer in Hmmm tot zijn beschikking heeft 16 is (15 voor het getal en 1 voor het teken, positief of negatief). Je zou Hmmm een 16-bits *architectuur* kunnen noemen
:::

(Als je eerder wilt stoppen, druk dan op control-C.)

### Nog een voorbeeld proberen, `voorbeeld1`

Probeer het voorbeeld `voorbeeld1.hmmm`. (Het is voorbeeldig!) Hier kan je de inhoud van `voorbeeld1.hmmm` zien:

```asm
00 read r1          # lees getal van gebruiker in r1
01 read r2          # ook voor r2
02 mul r3 r1 r2     # r3 = r1 * r2
03 write r3         # druk inhoud van r3 af
04 halt             # stop.
```

Lees het programma `voorbeeld1` instructie voor instructie door zodat je begrijpt wat er gebeurt; het laat je zien hoe je meerdere waardes aan de gebruiker vraagt en er vervolgens een berekening mee uitvoert.

Probeer het maar!

1. `run hmmm voorbeeld1.hmmm`
2. Het programma draait en vraagt je om een getal. Typ 7, en typ 6 als tweede getal.

Het programma zal Het Antwoord geven!

## Aftellen tot de derde macht

Voor deze eerste opgave, die je straks inlevert als `wk7ex1a.hmmm`, is je opgave om de code in het bestand zo aan te passen dat deze het volgende doet:

1. Eerst moet het de gebruiker vragen om invoer. Hmmm staat alleen integers toe van -32768 tot en met 32767. Voor deze opgave mag je ervan uitgaan dat de invoer ***positief*** is en kleiner dan 30.
2. Hierna moet je Hmmm-programma de ***derde macht*** van de invoer berekenen. Het moet het resultaat printen. Je hebt hier *meerdere* vermenigvuldigingen voor nodig! Dit vereist meerdere instructies. Het kost in het algemeen *veel* meer Hmmm-instructies om iets te doen dan bijvoorbeeld regels Pythoncode.
3. Hierna moet je programma ***naar beneden*** tellen vanaf de berekende waarde (de derde macht van de invoer), één integer per keer. Het moet elke waarde afdrukken totdat de waarde 0 is.
4. Als deze aftelling bij nul is uitgekomen, moet het programma stoppen. De laatste waarde die afgedrukt wordt moet `0` of `1` zijn. Beide zijn acceptabel als laatste waarde.

:::{admonition} Een aantal tips
:class: tip

Een goede manier om deze opgave aan te pakken is om *één stap* uit de lijst hierboven uit te werken, en je programma goed te *testen* om te controleren dat deze stap werkt. Je kan bijvoorbeeld

* Eerst een programma schrijven die een invoer leest, de derde macht ervan uitrekent en vervolgens stopt.
* Daarna dat programma *aanpassen* zodat deze de invoer lees, de derde macht uitrekent en afdrukt, en daarna *één minder dan de derde macht* afdrukt, en dan stopt.
* Ten slotte bedenken hoe je een lus kan toevoegen die dit blijft doen tot je bij nul bent voordat hij stopt.

Je *hoeft* dit ontwikkelproces niet te gebruiken, maar de één-stap-per-keeraanpak is extra belangrijk voor assembly, omdat het lastiger is (in ieder geval voor een mens!) om bij te houden waar alles is.
:::

### Commentaar

Om dezelfde reden, dat het voor mensen erg lastig is om bij te houden wat er in elke stap gebeurt, is het verstandig om op ***elke regel*** van alle Hmmm-code die je schrijft commentaar te schrijven. Bij null-operaties, `nop`s, hoeft dit niet; die zijn handig om code uit elkaar te houden zodat je programma kan groeien zonder steeds regels te hoeven hernummeren.

## RandoHmmm getallen genereren

Voor dit gedeelte van het pracitcum heb je de bestanden `wk7ex1b.hmmm` en `wk7ex1c.py` nodig. Je kan ze beide vinden in het zip-bestand dat je gedownload hebt.

De begincode staat al in het bestand `wk7ex1b.hmmm`:

```asm
00 read r1    # input a
01 read r2    # input c
02 read r3    # input m
03 read r4    # input X_0
04 read r5    # input N
```

In de volgende paragrafen worden deze invoerwaardes uitgelegd, en daarna hoe je daarmee willekeurige getallen kan genereren met deze waardes.

### De wiskunde achter het genereren van willekeurige getallen

De getallen die door RNG's (random number generators) gegenereerd worden zijn niet *"echt"* willekeurig omdat ze worden gegenereerd door een wiskundige formule. Ze hebben echter wel statistische eigenschappen waardoor ze zich gedragen op een manier die lijkt op hoe echt willekeurige getallen zich gedragen.

Daarom is het nauwkeuriger om random number generators *pseudo-*random number generators te noemen. We zullen dit verschil hier verder laten voor wat het is.

Onze random number generator genereert een rij van willekeurige getallen, <code>X<sub>0</sub></code>, <code>X<sub>1</sub></code>, <code>X<sub>2</sub></code>, ..., <code>X<sub>n</sub></code>, <code>X<sub>n+1</sub></code>, ..., gedefinieerd door de volgende wiskundige relatie:

$$
X_{n+1} = (a X_n + c) \div m
$$

waarbij we de volgende waardes kunnen kiezen

* $a$, een vermenigvuldigingsfactor
* $c$, een optelwaarde ("offset")
* $m$, een deler, maar alleen de "mod" of rest na deling wordt gebruikt!
* $X_0$, een "seedwaarde" of startwaarde, waarbij geldt dat
  $0 \leq X_0 \leq m$, dat wil zeggen, van $0$ tot en met $m$.

In een normale random number generator worden deze waardes automatisch gekozen. Vaak wordt dit gedaan aan de hand van het aantal milliseconden op de klok van de computer.

Nu gaan we zelf deze waardes kiezen. We gaan ook een waarde voor `N` kiezen en de gebruiker kiest de seedwaarde, <code>X<sub>0</sub></code>.

### Hoe onze random number generator werkt...

Je gaat een random number generator genaamd LCG implementeren; dit staat voor *linear congruential generator*.

Een LCG random number generator werkt als volgt:

1. Begin met de seedwaarde <code>X<sub>0</sub></code>. Dat wil zeggen dat `n` gelijk is aan `0`.
2. Gebruik de formule <code>X<sub>n+1</sub> = (a X<sub>n</sub> + c) % m</code> om <code>X<sub>n+1</sub></code> te genereren.
3. Gebruik nu <code>X<sub>n+1</sub></code> als de *nieuwe* seedwaarde
4. Ga terug naar stap 2 en blijf getallen genereren zolang je wilt...

Hier is een voorbeeld met kleine getallen:

* a = 5
* c = 1
* m = 7
* x<sub>0</sub> = 0

| i | Formule       | x<sub>i</sub> |
|---|---------------|---------------|
| 0 | 0             | 0             |
| 1 | (5*0 + 1) % 7 | 1             |
| 2 | (5*1 + 1) % 7 | 6             |
| 3 | (5*6 + 1) % 7 | 3             |
| 4 | (5*3 + 1) % 7 | 2             |
| 5 | (5*2 + 1) % 7 | 4             |
| 6 | (5*4 + 1) % 7 | 0             |
| 7 | (5*0 + 1) % 7 | 1             |

Vanaf hier herhaalt alles zich...

Merk op dat omdat de willekeurige getallen die je op deze manier genereert altijd tussen 0 en `m-1` liggen omdat we onze getallen steeds modulo `m` nemen. Het `mod`-commando bestaat al in Hmmm (je hoeft het niet zelf te schrijven!).

In het voorbeeld hierboven herhaalt de LCG zichzelf na het genereren van `m` willekeurige getallen. Als een LCG zich pas herhaalt na het genereren van `m` getallen, zeggen we dat het een **volledige periode** heeft. Dit is een gewenste eigenschap, omdat het betekent dat de generator het grootst mogelijke aantal getallen genereert voordat hij zich herhaalt.

Hieronder ga je ervoor zorgen dat je generator deze eigenschap heeft.

### De RandoHmmm number generator schrijven

De opgave is om dit LCG-algoritme te implementeren in Hmmm.

Dit is de samenvatting in een enkele zin: je progamma moet `N` pseudorandom getallen genereren en afdrukken, door gebruik te maken van onze formule:

$$
X_{n+1} = (a X_n + c) \div m
$$

#### Details

Je programma moet als volgt werken: De gebruiker geeft **vijf** getallen als invoer in de
onderstaande volgorde. Deze invoer wordt al geregeld door `wk7ex1b.hmmm`:

* Als eerste geeft de gebruiker het getal `a` op, de vermenigvuldigingsfactor in het LCG-algoritme.
* Als tweede geeft de gebruiker het getal `c` op, de optelwaarde in het LCG-algoritme.
* Als derde geeft de gebruiker het getal `m` op, de modulusdeler in het LCG-algoritme.
* Als vierde geeft de gebruiker de seedwaarde <code>X<sub>0</sub></code> uit het LCG-algoritme op.
* Als vijfde geeft de gebruiker het geral `N` op, dat aangeeft hoeveel pseudorandom getallen afgedrukt moeten worden.

Daarna moet je Hmmm random number generator

* Eerst kijken of er meer getallen gegenereerd moeten worden (basisgeval!). In welk register staat de waarde die je moet bekijken?
  * Als er geen getallen meer gegenereerd hoeven te worden, spring dan naar het einde van de code.
  * Misschien weet je nog niet waar het einde zal zijn; je kan nu bijvoorbeeld te ver springen (15 is te ver) en deze regel later aanpassen als je dat wel weet...
* Schrijf daarna de instructies die je nodig hebt om de ***volgende*** waarde van `X` te berekenen, bijvoorbeeld <code>X<sub>1</sub></code>
  * Onthoud dat, met de formule van hierboven, <code>X<sub>1</sub> = (a X<sub>0</sub> + c) % m</code>
  * Of algemener <code>X<sub>n+1</sub> = (a X<sub>n</sub> + c) % m</code>
* Merk op dat het geen probleem is als je het register voor <code>X<sub>0</sub></code> hergebruikt als je <code>X<sub>1</sub></code> aan het berekenen bent, enzovoorts...
* Nadat je <code>X<sub>1</sub></code> hebt berekend, druk het af.
  * Druk <code>X<sub>0</sub></code> niet af; dat is de *seed* van de random number generator.
  * Alle andere getallen <code>X<sub>n</sub></code> (met `n ≥ 1`) zijn *wel* onderdeel van de lijst willekeurige getallen en moeten dus wel afgedrukt worden.
* Update ten slotte die waarden die geüpdatet moeten worden, zoals `N`, en spring met `jumpn` terug naar de juiste plaats.
  * Je moet aan het einde van elke branch wel een `halt`-instructie gebruiken.
* Merk op dat je op dit moment weet hoe groot je programma zal zijn, en je kan dat gebruiken in de `jumpn` regels die nog een goed regelnummer nodig hadden...

:::{admonition} Samenvatting en tips
:class: tip

Je Hmmm-programma in `wk7ex1b.hmmm` moet dus `N` pseudorandom getallen genereren, te beginnen bij <code>X<sub>1</sub></code> (ter herinnering, <code>X<sub>0</sub></code> wordt niet beschouwd als een pseudorandom getal en wordt dus niet geprint.)

* Merk op dat `mod` ingebouwd is in Hmmm! *Ga mod niet zelf schrijven!*
* Het kan handig zijn om een register naar een ander register te *kopiëren*...
* Het commando `copy r4 r8` kopieert de inhoud van register `r8` **naar** register `r4`.
  * ***Let op!***: het `copy`-commando werkt van rechts naar links.
  * *Opmerking* Dit is waarom de toekenningsoperator in Python van rechts naar links werkt!
:::

Het kan hierbij handig zijn om de [lijst van alle instructies in Hmmm](/support/hmmm.md) te raadplegen.

#### Je generator controleren

Om te controleren of je random-numbergeneratr werkt kan je het proberen met de volgende invoer:

* Gebruik als eerste invoer het getal `a = 10`, de vermenigvuldigingsfactor in het LCG-algoritme.
* Gebruik als tweede invoer het getal `c = 7`, de optelwaarde in het LCG-algoritme.
* Gebruik als derde invoer het getal `m = 11`, de modulus in het LCG-algoritme.
* Gebruik als vierde invoer de seed <code>X<sub>0</sub> = 3</code>, de startwaarde in het LCG-algoritme.
* Gebruik als vijfde invoer het getal `N = 10`, om aan te geven dat er 10 pseudorandom getallen afgedrukt moeten worden.

Kort gezegd:

```
10
7
11
3
10
```

De uitvoer zal dan afwisselend `4` en `3` moeten zijn:

```
4
3
4
3
4
3
4
3
4
3
4
3
```

Dit zijn duidelijk ***geen*** goede waardes voor onze random-numbergenerator: ze zijn niet erg "willekeurig"! In het volgende onderdeel ga je betere, en daarna ideale, waardes kiezen voor `a` en `c`.

### Goede invoerwaardes kiezen voor het genereren van willekeurige getallen

Je baas bij **SPRANG** B.V. (Spam-Processed RAndom Number Generation) heeft je gevraagd een
random-numbergenerator te maken met `m` gelijk aan 100.

Je moet nu nog waardes voor `a` en `c` vinden die gebruikt kunnen worden met deze waarde van `m` en *redelijke* willekeurige getallen produceert. Dus ga je in dit deel "goede" waardes voor de parameters `a` en `c` van ons random-numbergeneratoralgoritme kiezen.

We gebruiken hiervoor dus `m = 100`.

#### In de praktijk

Probeer twee of drie verschillende waardes voor `a` en `c` (met `m = 100`, <code>X<sub>0</sub> = 42</code> en `N = 100`).

Misschien `a = 10` en `c = 5` om mee te beginnen?

Hoe verschillend zijn alle 100 uitvoergetallen? Beoordeel dit door naar de uitvoer te kijken...

Voor de volledigheid is hier de volledige set waardes gegeven die we nu gebruiken:

* Gebruik als eerste invoer het getal `a = 10`, de vermenigvuldigingsfactor in het LCG-algoritme.
* Gebruik als tweede invoer het getal `c = 5`, de optelwaarde in het LCG-algoritme.
* Gebruik als derde invoer het getal `m = 100`, de modulus in het LCG-algoritme.
* Gebruik als vierde invoer de seed <code>X<sub>0</sub> = 42</code>, de startwaarde in het LCG-algoritme.
* Gebruik als vijfde invoer het getal `N = 100`, om aan te geven dat er 10 pseudorandom getallen afgedrukt moeten worden.

Kort gezegd:

```
10
5
100
42
100
```

#### In theorie

Het blijkt dat het LCG-algoritme zijn best mogelijke performance; dat wil zeggen, het genereert dan een volledige set van `m` verschillende waardes voordat het zich herhaalt; als aan de volgende drie voorwaardes voldaan wordt:

* Voorwaade 1: `c` is relatief priem aan `m` (dat betekent dat `c` en `m` geen gemeenschappelijke delers hebben behalve 1).
* Voorwaarde 2: `a-1` is deelbaar door alle *priemfactoren* van `m` (niet *alle* factoren
  van `m`, maar alleen de *priemfactoren*).
* Voorwaarde 3: `a-1` moet een veelvoud van 4 zijn als `m` een veelvoud van 4 is.

:::{admonition} Opmerkingen
:class: notice

* De priemfactoren van `m = 100` alleen `2` en `5` zijn.
* 100 *wel* een veelvoud van 4 is.
* Voorwaarden 2 en 3 hierboven niet over `a` gaan maar over `a-1`.
:::

Kijk of je, met deze feiten in het achterhoofd, de ***kleinste*** waardes van `c` en `a` kan vinden waarbij het lukt om **alle** 100 getallen voor `m` = 100 te genereren. Houd <code>X<sub>0</sub> = 42</code> en `N = 100`.

Het is *niet* essentieel dat je deze zonder hulp vindt; als je het niet zeker weet, vraag het dan!

Hoe je de getallen ook vind, **probeer ze uit** met `wk7ex1b.hmmm`. *Lijkt het alsof alle 100 mogelijke getallen geproduceerd worden?*

Je gaat dit hierna toetsen.

### `unique` schrijven

Het is lastig om ***zeker*** te weten dat er geen herhalingen zitten in een ljst van 100 getallen. Daarom heeft je baas bij SPRANG je gevraagd om te *controleren* dat alle getallen uit je LCG-programma uniek zijn. Deze check mag (en moet) met Python uitgevoerd worden.

Open hiervoor het bestand genaamd `wk7ex1c.py` en bewerk de Python-startfunctie genaamd `unique(L)`.

Je functie `unique(L)` krijgt als enige invoer een lijst en moet `True` teruggeven als deze lijst alleen maar unieke elementen heeft (geen elementen worden herhaald) en `False` als dat niet zo is.

:::{admonition} Een paar tips
:class: tip

* Je functie heeft alleen recursie, lijsten indexeren en slicing nodig.
* Een goed basisgeval kijkt naar de meest eenvoudige lijst `L`. *Wat is de meest eenvoudige lijst getallen `L`?* Het is niet 0, maar de ***lijst*** met lengte 0.
* Je hebt nog twee gevallen nodig.
* Je zal merken dat de Pythonoperator `in` handig is om te kijken of `L[0]` voorkomt `in` de rest van de lijst!
:::

### `unique` testen

Om `unique` te testen kan je het bestand uitvoeren en dan een paar invoerwaardes proberen, bijvoorbeeld:

```ipython
In [1]: unique([7,8,9,1001,42])
Out[1]: True

In [2]: unique([2, 42, 3, 42])
Out[2]: False
```

### 100 waardes genereren en testen

Nu gaan we je functie `unique` gebruiken om te testen of je LCG-programma, met de waardes die je berekend hebt voor `a` en `c` je inderdaad een volledige periode geven als je deze het uitvoert met `m` ingesteld op 100:

* Voer eerst je Hmmm-LCG-programma uit met deze parameters.
* Gebruik een seed naar keuze, van 0 tot en met 99. Wij hebben gekozen voor 42.
* Zet ook de vijfde invoer `N` op 100, zodat je 100 uitvoernummers krijgt,
* Ten slotte moet je controleren dat deze 100 nummers uniek zijn.

*Gelukkig* heb je de functie `unique`.

*Helaas* heeft `unique` een lijst als argument, **maar** de uitvoer die we op ons scherm hebben is geen lijst (geen komma's en geen blokhaken aan het begin en einde).

Geen probleem! Kijk eerst naar het volgende stukje Pythoncode in het bestand `wk7ex1c.py`:

```python
# Je plakt je 100 getallen in deze triple-quoted string:
NUMBERS = """
3
42
47
46
91
5
"""


def unique(L):
    ... # dit heb je hierboven geschreven...


def test(s):
    ... # zie wk7ex1c.py voor deze functie ...
```

Er zijn twee dingen om op te merken in bovenstaande code: ten eerste is er een triple-quoted string genaamd `NUMBERS` die een aantal getallen bevat.

Ten tweede is er een kleine functie met de naam `test` die een string (`s`) als parameter meekrijgt, bijvoorbeeld de string `NUMBERS` (een triple-quoted string is gewoon een string!), en daarna `unique` gebruikt om te kijken of alle getallen in die string uniek zijn.

De `print`-statements die in commentaar staan kunnen je wat meer idee geven van hoe `test` werkt.

### De functie `test` gebruiken

Kopieer en plak de uitvoer van je Hmmm-progamma (100 getallen) in de triple-quoted string `NUMBERS`. *Vervang* hierbij de huidige inhoud van de string vervangt!

Voer het bestand opnieuw uit. Voer daarna

```python
test(NUMBERS)
```

uit in de prompt van de Pythonshell.

Als alles goed gegaan is, zal Python `True` als uitvoer geven.

Dit betekent dat je 100-number random-numbergenerator inderdaad precies 100 unieke willekeurige getallen heeft gegenereerd, het best-mogelijke resultaat.

### Afronden...

Nadat je je programma hebt gecontroleerd om te zien dat het inderdaad 100 verschillende waardes geeft is het practicum af!

## Je CV bijwerken!

Gefeliciteerd! Je kan nu Hmmm offcieel op je CV zetten, naast Logisim (en Picobot!)

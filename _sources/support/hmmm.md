---
title: "HMMM documentatie"
description: ""
csa-chapter: 4
---

# HMMM documentatie

## Overzicht van instructies in Hmmm

### Systeeminstructies

| Instructie | Beschrijving | Aliassen |
|------------|--------------|----------|
| **`halt`** | Stop! | |
| **`read`** `rX` | Sla gebruikersinvoer op in register `rX` | |
| **`write`** `rX` | Druk inhoud van register `rX` af | |
| **`nop`** | Doe niets | |

### Registerwaardes instellen

| Instructie  | Beschrijving | Aliassen |
|-------------|--------------|----------|
| **`setn`** `rX N` | Stel de waarde van register `rX` gelijk aan integer `N` (-128 t/m +127) | |
| **`addn`** `rX N` | Tel integer `N` (-128 t/m 127) op bij register `rX` | |
| **`copy`** `rX rY` | Zet `rX = rY` | **`mov`** |

### Berekeningen

| Instructie  | Beschrijving | Aliassen |
|-------------|--------------|----------|
| **`add`** `rX rY rZ` | Zet `rX = rY + rZ` | |
| **`sub`** `rX rY rZ` | Zet `rX = rY - rZ` | |
| **`neg`** `rX rY` | Zet `rX = -rY` | |
| **`mul`** `rX rY rZ` | Zet `rX = rY * rZ` | |
| **`div`** `rX rY rZ` | Zet `rX = rY / rZ` (integerdeling; geen rest) | |
| **`mod`** `rX rY rZ` | Zet `rX = rY % rZ` (geeft de rest na integerdeling terug) | |

### Sprongen!

| Instructie  | Beschrijving | Aliassen |
|-------------|--------------|----------|
| **`jumpn`** `N` | Zet de programmacounter op adres `N` | |
| **`jumpr`** `rX` | Zet de programmacounter op het adres in `rX` | **`jump`** |
| **`jeqzn`** `rX N` | Als `rx == 0` spring dan naar regel `N` | **`jeqz`**
| **`jnezn`** `rX N` | Als `rx != 0` spring dan naar regel `N` | **`jnez`**
| **`jgtzn`** `rX N` | Als `rx > 0` spring dan naar regel `N` | **`jgtz`**
| **`jltzn`** `rX N` | Als `rx < 0` spring dan naar regel `N` | **`jltz`**
| **`calln`** `rX N` | Kopieer het volgende adres naar `rX` en spring dan naar adres `N` | **`call`**

### Interacteren met het geheugen (RAM)

| Instructie  | Beschrijving | Aliassen |
|-------------|--------------|----------|
| **`pushr`** `rX rY` | Zet de inhoud van register `rX` op de stack waarnaar verwezen wordt door register `rY` | |
| **`popr`** `rX rY` | Laad de inhoud van register `rX` van de stack waarnaar verwezen wordt door register `rY` | |
| **`loadn`** `rX N` | Laad register `rX` met de gegevens uit geheugenadres `N` | |
| **`storen`** `rX N` | Sla de inhoud van register `rX` op in geheugenadres `N` | |
| **`loadr`** `rX rY` | Laad register `rX` met de gegevens uit het geheugenadres dat opgeslagen is in register `rY` | **`loadi`**, **`load`** |
| **`storer`** `rX rY` | Sla de inhoud van register `rX` op in het geheugenadres dat opgeslagen is in register `rY` | **`storei`**, **`store`** |

## Introductie

Hmmm is een 16-bits gesimuleerde assemblytaal met 26-instructies en kan maximaal tot 2<sup>8</sup> = 256 16-bits woorden in geheugen hebben. Hmmm is geschreven in Python, en het is bedoeld als een introductie in programmaren in assembly in het algemeen. Programma's geschreven in Hmmm bestaan uit genummerde regels met één instructie per regel, en commentaar.

Hmmm is geïmplementeerd als een enkel programma geschreven in Python. Standaard zal `hmmm` een bestand assembleren en uitvoeren dat geschreven is in de assemblytaal Hmmm. Er zijn opties om een programma te assembleren zonder het uit te voeren, om een eerder geassembleerd programma uit te voeren en om een ingebouwde debugger aan te roepen.

## Hmmm installeren

Je kan de broncode van Hmmm [hier](Hmmmwork7/hmmm) vinden. Je hebt hiervoor alleen een werkende versie van Python 3 nodig. Download het bestand `hmmm` en sla het op in een directory waar je ook je hmmm-programma's gaat schrijven.

## Hmmm gebruiken

Je kan aanwijzingen over hoe je Hmmm kan gebruiken vinden in de collegeslides en de opdrachten.

## Overzicht

Om een Hmmm-programma te assembleren (compileren) en uit te voeren typ je simpelweg "`python hmmm`" op de prompt van de terminal. Hmmm vraagt om een invoerbestand, assembleert dit en als dat gelukt is wordt het programma ook uitgevoerd. (Op een Mac kan je dit wat verkorten door "`./hmmm `*bestandsnaam.hmmm*" te typen waar *bestandsnaam.hmmm* de naam van je Hmmm-programma is.)

## Extra opties

Hmmm accepteert de opties -h, --help, -d en -o. -h en --help drukken een uitleg af van alle opties. -d roept de debugger van Hmmm aan. Als -o gegeven is, gevolgd door een bestandsnaam, dan wordt het programma geassembleerd en weggeschreven naar het genoemde bestand; Hmmm kan later worden aangeroepen om dat bestand uit te voeren. Bijvoorbeeld:

```console
python hmmm program.hmmm -o program.hb
python hmmm -d program.hb
```

In de debugmodus kan je "h" of "help" typen op de prompt van de debugger om uitleg over debugcommando's te krijgen; je kan ook de paragraaf over [diagnostische functies](#diagnostische-functies) raadplegen.

## Bestandsextensies- en types

De assembler en de simulator stellen beide geen eisen aan bestandsextensies. Het is echter gebruikelijk dat bestanden met de extensie 'hmmm' Hmmm-assemblycode bevatten, en bestanden met de extensie 'hb' geassembleerde Hmmm-binary's bevatten. (Omdat Hmmm alleen maar een simulator is zijn de binaire bestanden in feite tektbestanden die je met een gewone teksteditor kan lezen en bewerken.)

## Codeformaat

Elke regel Hmmm-code bevat een regelnummer, een instructie en mogelijk één of meer argumenten. De regelnummers moeten bij 0 beginnen en opeenvolgende integers zijn, en ze moeten aan het begin van de regel staan zonder voorafgaande tekens. Na het regelnummer moet er minstens één spatie of tab staan voor de instructie. Het regelnummer correspondeert rechtstreeks met het geheugenadres van de regel; lege geheugenruimte begint meteen na de laatste regel van het programma.

De instructies bestaan uit een enkel woord bestaande uit een aantal kleine letters. Na de instructie volgen afhankelijk van de instructiem nul of meer argumenten. Deze worden gescheiden van de instructie door spaties, tabs en/of '('-tekens.

Elk argument is een register of een getal. Registers worden aan gegeven met een 'r' gevolgd door het nummer van het register, bijvoorbeeld 'r3'. Getallen moeten in 8 bits passen. (Hun decimale waarde moet afhankelijk van de instructie vallen in het bereik van -128 tot en met 127 of van 0 tot en met 255. Dit is omdat nummers via de zogeheten "twos-complement"-methode worden opgeslagen.) Elk argument wordt gescheiden van zijn voorganger door spaties, tabs en/of komma's, en de regel kan worden afgesloten met spaties, tabs en/of commentaar.

In de paragraaf met [voorbeelden](#voorbeelden) kan je voorbeelden vinden van goede en foute syntax.

Commentaar in Hmmm is hetzelfde als in Python: een '#'-teken begint commentaar dat eindigt aan het einde van de regel. Commentaar mag zowel op lege regels als op regels met instructies staan. Commentaar op regels die verder leeg zijn krijgt geen regelnummer, en telt niet voor het regelnummer van de volgende regel. Regels mogen ook helemaal leeg zijn.

## Machine-indeling

Hmmm simuleert een computer met 16 16-bit-registers en 256 16-bit-geheugenwoorden. Het programma wordt in het geheugen geladen vanaf geheugenadres 0, dus een programma van 12 regels heeft 244 vrije geheugenwoorden over vanaf adres 12 (adressen 0 tot en met 11 worden door de programmainstructies gevolgd). De programmacounter begint op adres 0 en wordt elke cycle met 1 verhoogd. Deze kan ook aangepast door de verschillende **jump**-instructies. Elke cycle leest de simulator de instructie op het geheugenadres die aangewezen wordt door de programmacounter en voert deze uit. Dit gaat door totdat een **halt**-instructie wordt uitgevoerd.

15 van de 16 registers zijn in principe hardwarematig allemaal hetzelfde (maar zie de conventies hieronder). Het enige speciale register is r0. Als deze gelezen wordt, bevat het altijd een 0. Elke waarde die in dit register geschreven wordt
wordt weggegooid.

## De instructieset van Hmmm

Er zijn 26 verschillende instructies in Hmmm, die allemaal tussen de 0 en 3 argumenten hebben. Drie van de instructies, loadn, setn en addn, krijgen een potentieel negatief getal als argument tussen -127 en 127. De instructies load, store, call en jump krijgen een niet-negatief argument mee tussen 0 en 255. Alle andere instructieargumenten zijn registers. In de code hieronder worden registerargumenten weergegeven als 'rX', 'rY' en 'rZ', en numerieke argumenten als '#'. In echte code kan elk van de 16 registers gebruikt worden voor 'rX', 'rY' of 'rZ'. De beschikbare instructies zijn:

| Assembly | Binair | Beschrijving |
|----------|--------|--------------|
| **halt** | `0000 0000 0000 0000` | Stop het programma |
| **nop** | `0110 0000 0000 0000` | Doe niets |
| **read** r*X* | `0000 XXXX 0000 0001` | Wacht op gebruikersinvoer en sla dit op in register r*X* (De invoer is een getal tussen -32768 en 32767). Drut "Enter number:" af om de gebruiker om invoer te vragen |
| **write** r*X* | `0000 XXXX 0000 0010` | Drukt de invoer van register r*X* af op de standaarduitvoer |
| **setn** r*X*, # | `0001 XXXX #### ####` | Laad een 8-bit-integer # (-128 tot en met 127) in register r*X* |
| **loadr** r*X*, r*Y* | `0100 XXXX YYYY 0000` | Laad register r*X* uit het geheugenwoord geaddresseerd door r*Y*: r*X* = memory\[r*Y*] |
| **storer** r*X*, r*Y* | `0100 XXXX YYYY 0001` | Sla de inhoud van register `rX` op in het geheugenwoord geadresseerd door r*Y*: memory\[r*Y*] = r*X* |
| **popr** r*X*, r*Y* | `0100 XXXX YYYY 0010` | Laad register `rX` uit de stack aangewezen door register r*Y*: r*Y* -= 1; r*X* = memory\[r*Y*] |
| **pushr** r*X*, r*Y* | `0100 XXXX YYYY 0011` | Zet de inhoud van register `rX` op de stack aangewezen door register r*Y*: memory\[r*Y*] = r*X*; r*Y* += 1 |
| **loadn** r*X*, # | `0010 XXXX #### ####` | Laad register r*X* uit het geheugenwoord op adres # |
| **storen** r*X*, # | `0011 XXXX #### ####` | Sla de inhoud van register r*X* op in het geheugenwoord op adres # |
| **addn** r*X*, # | `0101 XXXX #### ####` | Tel de 8-bit-integer # (-128 tot en met 127) op bij register r*X* |
| **copy** r*X*, r*Y* | `0110 XXXX YYYY 0000` | Zet r*X* = r*Y* |
| **neg** r*X*, r*Y* | `0111 XXXX 0000 YYYY` | Zet r*X* = -r*Y* |
| **add** r*X*, r*Y*, r*Z* | `0110 XXXX YYYY ZZZZ` | Zet r*X* = r*Y* + r*Z* |
| **sub** r*X*, r*Y*, r*Z* | `0111 XXXX YYYY ZZZZ` | Zet r*X* = r*Y* - r*Z* |
| **mul** r*X*, r*Y*, r*Z* | `1000 XXXX YYYY ZZZZ` | Zet r*X* = r*Y* * r*Z* |
| **div** r*X*, r*Y*, r*Z* | `1001 XXXX YYYY ZZZZ` | Zet r*X* = r*Y* / r*Z* |
| **mod** r*X*, r*Y*, r*Z* | `1010 XXXX YYYY ZZZZ` | Zet r*X* = r*Y* % r*Z* |
| **jump** r*X* | `0000 XXXX 0000 0011` | Zet programmacounter op het adres in r*X* |
| **jumpn** # | `1011 0000 #### ####` | Zet de programmacounter op adres # |
| **jeqz** r*X*, # | `1100 XXXX #### ####` | Als r*X* = 0 zet dan de programmacounter op adres `#` |
| **jnez** r*X*, # | `1101 XXXX #### ####` | Als r*X* ≠ 0 zet dan de programmacounter op adres `#` |
| **jgtz** r*X*, # | `1110 XXXX #### ####` | Als r*X* > 0 zet dan de programmacounter op adres `#` |
| **jltz** r*X*, # | `1111 XXXX #### ####` | Als r*X* < 0 zet dan de programmacounter op adres `#` |
| **call** r*X*, # | `1011 XXXX #### ####` | Zet r*X* op de (volgende) programmacounter, en zet dan de programmacounter op adres `#` |

## Invoer en uitvoer

Hmmm ondersteunt erg versimpelde I/O via de instructies **read** en **write**.

De instructie **read** vraagt de gebruiker om een getal en zet het getal in het gegeven register. Het controleert op de grenzen van de mogelijke invoer en vraagt de gebruiker opnieuw als het getal niet goed was. Het kan ook gebruikt worden om het programma te onderbreken door 'q' in te voeren in plaats van een getal. Dit stopt meteen de uitvoering van het programma. De instructie **write** drukt simpelweg het gegeven register af op het scherm van de gebruiker

## Het programma stoppen

De instructie **halt** stopt het programma, en is het equivalent van een **jump** naar regel -1. Dd gebruiker kan op elk punt tijdens het uitvoeren van het programma op ctrl-C drukken om het te stopen, en het programma stopt ook door 'q' op de debugprompt of de invoerprompt op te geven. Het programma stopt ook door ctrl-D te gebruiken op een willekeurige
prompt.

## Diagnostische functies

Het simulatorprogramma bevat een debugmodus die handig is om fouten in het programma op te sporen. Deze kan aangeroepen worden met de opties -d en --debug.

De debugmodus drukt informatie af na het uitvoeren van elke instructie, en toont welke instructie net is uitgevoerd en waar deze in het geheugen gevonden is (wat de programmacounter was). Het drukt ook een debugprompt af. Invoer die niet herkend wordt op deze prompt laat de simulator één instructie van het programma uitvoeren. Herkende commando's zijn onder andere 'c' of 'continue', 'd' of 'dump', 'h' of 'help', 'p' of 'print', 'q' of 'quit' en 'r' of 'run'.

| Commando | Effect |
|----------|--------|
| **continue** | Zorgt ervoor dat de debugger de rest van het programma uitvoert zonder de debugprompt te tonen; de debuginformatie wordt nog wel steeds afgedrukt. |
| **dump** | Drukt meteen de inhoud van het geheugen af, met eerst de coderegels (één per regel) en daarna de rest van het geheugen in 6 kolommen, en vraagt dan om een nieuw debugcommando. |
| **help** | Drukt een kort overzicht van de debugcommando's af en toont opnieuw de prompt. |
| **print** | Drukt de inhoud van de registers af in een enkele kolom en toont opnieuw de prompt. |
| **quit** | Zorgt ervoor dat het programma meteen stopt. |
| **run** | Zorgt ervoor dat de rest van het programma wordt uitgevoerd alsof het zonder debugmodus is uitgeoverd: er worden geen debuginformatie en debugprompts meer getoond. |
| **next #** | Voert de volgende # instructies uit zonder de debugprompt de tonen, en toont dan de prompt weer. |
| **break #** | Zet een breakpoint op adres # in het geheugen. Als de simulator normaal gesproken geen debugprompt zou tonen bij het uitvoeren van deze regel, wordt dat nu toch gedaan en wordt de debugmodus weer aangezet. Het bereiken van een breakpoint annuleert de commando's next en run. Een breakpoint wordt in de geheugenweergave aangeduid met een pijltje. |
| **clear #** | Verwijdert een breakpoint van adres # in het geheugen. Als er op dat adres geen breakpoint was is het commando niet geldig en wordt een enkele stap uitgevoerd. |

## Voorbeelden

### Goede code

Dit is een programma dat goed geschreven en van commentaar voorzien is. Het leest twee getallen, drukt het eerste af, en geeft het eerste gedeeld door het tweede terug, of 0 als het tweede getal 0 is.

```
# program title
# author and date
# descriptive comment
0   read r1     # laat de gebruiker teller opgeven
1   write r1    # druk de invoer af
2   read r2     # laat de gebruiker de deler opgeven
3   jeqzn r2, 7 # spring naar 7 als door 0 gedeeld wordt
4   div r3, r1, r2 # deel de invoer van de gebruiker door elkaar
5   write r3    # druk het resultaat af
6   halt
7   setn r3, 0  # 0 is het anwoord voor deling door 0
8   write r3    # druk het antwoord af
9   halt
```

Dit is de uitvoer van de assembler als het programma word uitgevoerd (merk op dat de assembler commentaar afkapt zodat de regels goed op het scherm passen):

```text
----------------------​
| ASSEMBLY SUCCESSFUL |
----------------------

0: 0000 0001 0000 0001             0   read r1     # laat de gebruiker teller
1: 0000 0001 0000 0010             1   write r1    # druk de invoer af
2: 0000 0010 0000 0001             2   read r2     # laat de gebruiker de dele
3: 1100 0010 0000 0111             3   jeqzn r2, 7 # spring naar 7 als door 0
4: 1001 0011 0001 0010             4   div r3, r1, r2 # deel de invoer van de
5: 0000 0011 0000 0010             5   write r3    # druk het resultaat af
6: 0000 0000 0000 0000             6   halt
7: 0001 0011 0000 0000             7   setn r3, 0  # 0 is het anwoord voor del
8: 0000 0011 0000 0010             8   write r3    # druk het resultaat af
9: 0000 0000 0000 0000             9   halt

Enter number (q to quit): 42
42
Enter number (q to quit): 6
7
```

### Slechte code

Dit is hetzelfde programma, en werkt hetzelfde. Deze code is echter van lage kwaliteit.

```text
 0  read r1
1   write r1
2   read  r2 # read r2
3   jeqzn r2, 7
  4 div r3 r1, r2
5   write r3
6   halt        # einde
7      setn r3  0
8   write r3
9   halt
```

Dit is de uitvoer van de assembler voor deze code:

```
----------------------​
| ASSEMBLY SUCCESSFUL |
----------------------

0: 0000 0001 0000 0001             0  read r1
1: 0000 0001 0000 0010             1   write r1
2: 0000 0010 0000 0001             2   read  r2 # read r2
3: 1100 0010 0000 0111             3   jeqzn r2, 7
4: 1001 0011 0001 0010             4 div r3 r1, r2
5: 0000 0011 0000 0010             5   write r3
6: 0000 0000 0000 0000             6   halt        # einde
7: 0001 0011 0000 0000             7      setn r3  0
8: 0000 0011 0000 0010             8   write r3
9: 0000 0000 0000 0000             9   halt

Enter number (q to quit): 42
42
Enter number (q to quit): 7
6
```

### Foutieve syntax

Dit is hetzelfde programma voor de derde keer, nu aangepast om ongeldige syntax te tonen. Dit programma kan niet geassembleerd worden.

```text
# program title
# program title
# author and date
# descriptive comment
0   read r1,    # er mogen geen tekens na de argumenten staan
1   write[r1]   # groeperingssymbolen zijn niet toegestaan
2   read r2, r3 # te veel argumenten voor deze instructie
3   jeqzn r2, r7 # tweede argument moet een getal zijn
4   div r3, r1r2 # argumenten moeten gescheiden zijn
5   write 3     # argument van write moet een register zijn
5   halt        # regelnummer is incorrect
7   setn r3, 128     # maximale waarde voor de instructies setn en addn is 127
                # (minimale is -128)
9   writer3     # instructie moet gescheiden zijn van argument
10halt          # instructie moet gescheiden zijn van regelnummer
```

Hier is de uitvoer van de assembler op dit programma; dit laat de foutmeldingen voor de fouten hierboven zien:

```text
ARGUMENT ERROR:
WRONG NUMBER OF ARGUMENTS.
DETECTED 2 ARGUMENTS, EXPECTED 1 ARGUMENTS
read r1,

SYNTAX ERROR ON LINE 1:
1   write[r1]   # groeperingssymbolen zijn niet toegestaan

ARGUMENT ERROR:
WRONG NUMBER OF ARGUMENTS.
DETECTED 2 ARGUMENTS, EXPECTED 1 ARGUMENTS
read r2, r3

ARGUMENT ERROR:
'r7' IS NOT A VALID NUMBER.

ARGUMENT ERROR:
WRONG NUMBER OF ARGUMENTS.
DETECTED 2 ARGUMENTS, EXPECTED 3 ARGUMENTS
div r3, r1r2

REGISTER ERROR:
'3' IS NOT A VALID REGISTER.

BAD LINE NUMBER AT LINE 6:
LINE NUMBER: 5 EXPECTED 6

ARGUMENT ERROR:
'128' IS OUT OF RANGE FOR THE ARGUMENT.

OPERATION ERROR:
'writer IS NOT A VALID OPERATION.

SYNTAX ERROR ON LINE 9:
10halt          # instructie moet gescheiden zijn van regelnummer

***** ASSEMBLY TERMINATED UNSUCCESSFULLY *****
              ASSEMBLY RESULTS:

0: ***ARGUMENT ERROR HERE***       0   read r1,    # er mogen geen tekens na d
1: ***SYNTAX ERROR HERE***         1   write[r1]   # groeperingssymbolen zijn
2: ***ARGUMENT ERROR HERE***       2   read r2, r3 # te veel argumenten voor d
3: ***ARGUMENT ERROR HERE***       3   jeqzn r2, r7 # tweede argument moet een
4: ***ARGUMENT ERROR HERE***       4   div r3, r1r2 # argumenten moeten gesche
5: ***REGISTER ERROR HERE***       5   write 3     # argument van write moet e
6: ***BAD LINE NUMBER HERE***      5   halt        # regelnummer is incorrect
7: ***ARGUMENT ERROR HERE***       7   setn r3, 128     # maximale waarde voor
8: ***OPERATION ERROR HERE***      9   writer3     # instructie moet gescheide
9: ***SYNTAX ERROR HERE***         10halt          # instructie moet gescheide

***** ASSEMBLY FAILED, SEE ABOVE FOR ERRORS *****
```

Alhoewel dit misschien niet duidelijk is aan de hand van het voorbeeld hierboven wordt het assembleren van een regel afgebroken als er een fout wordt aangetroffen. Als een regel dus meerdere fouten heeft, wordt maar een enkele fout gerapporteerd. Als die fout opgelost is, wordt de volgende fout gerapporteerd als die er nog steeds is.

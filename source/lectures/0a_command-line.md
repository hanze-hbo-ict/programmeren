# De terminal

Het **doel** van deze les is om:

* Kennis maken met de directorystructuur.
* Werken met een command-line interface

## Directorystructuur

Een programma heeft instructies nodig om te weten wat het moet doen. Deze instructies staan in bestanden, ook bekend als files. Elk bestand heeft een extensie om aan te geven wat voor type bestand het is. `bestand.py` is een python bestand, `bestand.docx` is een word bestand. Het zijn altijd de laatste drie, soms vier letters na de **laatste** punt. `bestand.docx.py` is nog steeds een python bestand.

:::{admonition} Belangrijk!
:class: important

In de verkenner van windows zijn niet alle bestanden en directories zichtbaar. Daarnaast zijn de extensies niet standaard weergegeven. Het is verstandig om via het tabblad View de optie *file name extensie* en *hidden items* te selecteren.

![View settings](images/0/view_settings.png)
:::

Vele programma's bestaan uit verschillende bestanden en om deze allemaal bij elkaar te houden staan ze in een **directory**. Als gebruiker kan je ook directories aanmaken om bestanden makkelijk terug te vinden. Binnen windows gebruik je de verkenner a.k.a. de explorer en binnen apple gebruik je Finder.

Wat de Verkenner een *map* noemt, heet in de terminal een *directory*. Het is hetzelfde ding, en wij houden directory aan, omdat de commando's het zo noemen: `pwd` staat voor *print working directory* en `cd` voor *change directory*.

Directories staan in een zogenaamde boomstructuur. Elke directory kan
directories bevatten, en die weer, zo diep als je wilt.

```{mermaid}
flowchart TD
    C["C:"] --> PF["Program Files"]
    C --> U["Users"]
    C --> W["Windows"]
    U --> A["Administrator"]
    U --> E["emily"]
    E --> D["Desktop"]
    E --> Doc["Documents"]
    E --> Dow["Downloads"]
```

In de terminal zie je diezelfde structuur zonder plaatjes, zo:

```text
C:
├── Program Files
├── Users
│   ├── Administrator
│   └── emily
│       ├── Desktop
│       ├── Documents
│       └── Downloads
└── Windows
```

Dat is geen tekening maar uitvoer: het commando `tree` drukt het zo af. Je komt
deze schrijfwijze overal tegen, dus het loont om hem te leren lezen. Wat
inspringt zit erin.

De Finder van macOS beeldt de structuur op een andere manier af.

![Directories in de Finder](images/0/finder_folders.png)

### OneDrive

OneDrive is de cloud systeem van microsoft. Het is automatisch geïnstalleerd in windows. Voor mac kan het geïnstalleerd worden met Rosetta 2 emulator. Via de Hanze heb je toegang tot een grote OneDrive om al je schoolwerk in kwijt te kunnen. Het werkt als een normale directory in de verkenner en alles wat erin staat wordt opgeslagen in de cloud. Het grote voordeel is dat je werk altijd een backup heeft. Je kan ook op verschillende apparaten inloggen dezelfde OneDrive account instellen, bijvoorbeeld op een tablet, laptop en desktop. Op deze manier heb je toegang tot je bestanden op alle drie the apparaten.

In de settings van one_drive kan je een account toevoegen, including je hanze schoolaccount. Zodra je deze hebt aangemaakt wordt er een nieuwe directory aangemaakt voor de OneDrive. Daar kan al het werk in geplaatst worden.

:::{admonition} Belangrijk!
:class: important

OneDrive staat standaard op *Files On-demand*. Dit houdt in dat het enkel een document download zodra je het opent. Voor programmeren werkt dat niet. Bestanden moeten lokaal beschikbaar zijn. Het is dus verstandig om *files on-demand* uit te zetten.

![files on demand off](images/0/files_on_demand.png)
:::

## Command Prompt

De meeste interacties die we met computers hebben zijn via vensters die door het besturingssysteem aangeboden worden. Het besturingssysteem (of *OS*, kort voor *operating system*), is meestal Windows of macOS, maar er zijn vele andere, waarvan Linux de meest voorkomende is. Het besturingssysteem dat je gebruikt voorziet in een *venstersysteem* waardoor je een muis kan gebruiken, op een gebruikersvriendelijke manier kan interacteren met de computer, en zelfs films kan bekijken. De klik-en-sleepinterface van moderne venstersystemen is zeker heel erg handig!

***Echter***, de grafische interface is ook een gordijn, dat de gebruiker afschermt van wat er echt gebeurt met de bestanden op het systeem. Het is een krachtige en nuttige vaardigheid om een duidelijk idee te hebben van hoe bestanden gebruikt worden *achter* het gordijn van het venstersysteem. De terminal is een programma dat "achter" het gordijn kijkt. Hij gebruikt tekstcommando's op de zogeheten "command line" (of commandoregel) om bestanden en acties op je computer aan te spreken.

Je op je gemak voelen op de command line is vaak handig om programma's te *maken*. Het besturingssysteem is erg geschikt voor het *gebruiken* van programma's!

***Start je terminal op!***

`````{tab-set}

````{tab-item} Windows
Vind en start *Terminal*. Als je deze applicatie niet hebt, installeer het via [Windows Store](https://apps.microsoft.com/detail/9n0dx20hk701?gl=NL&hl=nl-NL&gl=NL).
````

````{tab-item} macOS
Druk op command (⌘)+ spatie en type Terminal.
````

````{tab-item} Linux
De terminal die gebruikt wordt kan per distributie verschillen, bijvoorbeeld `xterm`, `gnome-terminal` of `ptyxis`. Je zal moeten uitzoeken welke is geïnstalleerd, raadpleeg andere de documentatie van jouw distributie.
````

`````

Als dit de eerste keer is dat je de terminal gebruikt, goed bezig!

## Paden

Zodra je de terminal opent start het vaak in je home directory. Dit is aangegeven via een pad.

```console
C:\Users\Emily>
```

De *slashes* (`/`) scheiden subdirectories van de directory waar ze in zitten. Op Windows zie je meestal backslashes `\` of dubbele backslashes; dit verschil is niet belangrijk. Linus en macOS gebruiken *forward* slashes (`/`).

Vertaling: op de C-schijf staat in de directory Users de directory Emily

Alle bestanden hebben een eigen pad, een locatie binnen het systeem. Een computer kan enkel een bestand vinden als het pad bekend is.

## De terminal en de command-line

Alles wat je kan doen met de vensters van je besturingssysteem kan je ook met de terminal en de command-line doen. (Sterker, je kan nog veel *meer* met de command line doen...)

Bij dit vak heb je een paar terminalcommando's nodig, hier is een kort overzicht:

* `pwd`; kort voor *print working directory*. Het drukt je huidige locatie af.
* `ls`; Het drukt een lijst af van alle bestanden in de huidige locatie.
* `cd`; kort voor *change directory*. Het laat je van directory naar directory door je computer navigeren.

## `pwd`

Eerst zie je de *prompt*. De prompt is het stukje tekst aan de linkerkant dat wacht totdat je wat op de command line typt en dit zal er voor Windows, macOs en Linux nét iets anders uit zien (die van macOS en Linux lijken op elkaar omdat deze besturingssystemen familie van elkaar zijn!). Dat het op input wacht kan je zien aan de knipperende cursor (het knipperende blokje).

`````{tab-set}

````{tab-item} Windows
```console
PS C:\Users\misja>
```
````

````{tab-item} macOS
```console
misja@MacBook-Air ~ %
```
````

````{tab-item} Linux
```console
misja@selenix:~$
```
````

``````

**Het commando `pwd`** staat voor *print working directory*. Het drukt je huidige locatie af. Probeer het:

`````{tab-set}

````{tab-item} Windows
```console
PS C:\Users\misja> pwd

Path
----
C:\Users\misja


PS C:\Users\misja>
```
````

````{tab-item} macOS
```console
misja@MacBook-Air ~ % pwd
/Users/misja
misja@MacBook-Air ~ %
```
````

````{tab-item} Linux
```console
misja@selenix:~$ pwd
/home/misja
misja@selenix:~$
```
````

`````

Je ziet de locatie waarin je terminal en command line op dit moment actief is. Waarschijnlijk zal je een iets ander resultaat zien, behalve als je naam toevallig `misja` is 😉

Merk ook op dat een volgende prompt verschenen is, die op een volgend commando wacht...

De uitvoer is de *naam van de directory* waar je je momenteel bevindt in de terminal.

De slashes `/` scheiden subdirectories van de directory waar ze in zitten. Op Windows zie je meestal backslashes `\` of dubbele backslashes; dit verschil is niet belangrijk.

In alle voorbeelden is de gebruiker in een subdirectory met de naam `misja` op de harde schijf. Dit zal jou "home directory" zijn, de plek waar al jouw bestanden staan.

We gaan nu kijken wat we hier kunnen vinden met het commando `ls`...

## `ls`: het *list*-commando

**Het commando `ls`** staat voor *list*.

Als je `ls` uitvoert toont dit een lijst van alle bestanden en directories in je huidige directory. Gebruik je het programma command prompt, dan gebruik je het commando `dir` (afkorting for directory). Een voorbeelduitvoer van `ls` is:

`````{tab-set}

````{tab-item} Windows
```console
PS C:\Users\misja> ls


    Directory: C:\Users\misja


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-r---         9/26/2022  12:32 AM                Contacts
d-r---        10/23/2022   8:10 PM                Desktop
d-r---        10/23/2022   9:15 PM                Documents
d-r---         8/30/2023   9:03 PM                Downloads
d-r---         9/26/2022  12:32 AM                Favorites
d-r---         9/26/2022  12:32 AM                Links
d-r---         9/26/2022  12:32 AM                Music
d-r---         9/25/2022  11:55 PM                Pictures
d-r---         9/26/2022  12:32 AM                Saved Games
d-r---         9/25/2022  11:48 PM                Searches
d-r---         10/7/2022   8:45 PM                Videos


PS C:\Users\misja>
```
````

````{tab-item} macOS
```console
misja@MacBook-Air ~ % ls
Desktop  Documents  Downloads  Library  Movies  Pictures  Public
misja@MacBook-Air ~ %
```
````

````{tab-item} Linux
```console
misja@selenix:~$ ls
Desktop  Documents  Downloads  Movies  Music  Pictures  Public
misja@selenix:~$
```
````

`````

De uitvoer is een lijst van alle bestanden en subdirectories in de huidige directory.

Probeer het commando om een lijst van de namen van bestanden en subdirectories in je huidige directory te zien in de terminal, bijvoorbeeld

````{tip}
Met `ls` kan je ook de inhoud van een subdirectory bekijken door het de naam daarvan mee te geven als extra *argument*, bijvoorbeeld

```console
ls Desktop
```
````

Nu ga je met `cd` door de directories heen bewegen...

## `cd`: het *change-directory*-commando

**Het commando `cd`** is het belangrijkste. Het staat voor *change directory*.

Het commando `cd` laat je van je huidige directory naar andere directories op je computer navigeren. Om het te gebruiken moet je natuurlijk wel weten waar je heen wilt gaan!

Je kan bijvoorbeeld het bureaublad (Desktop) proberen ... typ dus `cd Desktop` in:

`````{tab-set}

````{tab-item} Windows
```console
PS C:\Users\misja> cd Desktop
PS C:\Users\misja\Desktop>
```
````

````{tab-item} macOS
```console
misja@MacBook-Air ~ % cd Desktop
misja@MacBook-Air ~/Desktop %
```
````

````{tab-item} Linux
```console
misja@selenix:~$ cd Desktop
misja@selenix:~/Desktop$
```
````

`````

Er is niet veel gebeurd ... tot je `pwd` intypt en ziet dat je ergens anders bent! En als je goed kijkt zal je ook zien dat de *prompt* is veranderd en jou laat weten dat je nu in een andere *directory* bent ...

Als je nu `ls` typt zouden er *veel* meer bestanden kunnen zijn maar dat hangt er een beetje vanaf hoe rommelig je bureaublad is! *Probeer het maar!*

```console
ls
```

Je gaat je nu "omhoog" verplaatsen in de directorystructuur...

## `cd ..`: een directory "omhoog" gaan

Ok, je bent naar het bureaublad (Desktop) ge-`cd`'d, *maar hoe ga je terug?!*

De speciale directorynaam met twee punten achter elkaar `..` betekent "één directory *omhoog*".

Als je dus `cd ..` intypt en op return drukt ben je terug in de directory die je bureaublad *bevat*:

```console
cd ..
```

Probeer nu `pwd` en `ls` om er zeker van te zijn dat je weer terug bent!

### Oefenen

Probeer de volgende commando's op jouw computer. Twijfel je bij elke stap waar je je nu bevindt? Gebruik dan altijd `pwd` om het te controleren!

```console
cd
```

Het commando `cd` is zonder de naam van een directory waar je naartoe wilt? Dit is geen typfout! Het commando `cd` zonder een *argument* zal altijd `cd`-en naar jouw *home directory* en is de meest snelle manier om weer 🏠 te komen 😊

```console
cd Documents
```

Welke interessante bestanden heb jij in deze directory staan? Gebruik `ls`!

```console
ls
```

En maar weer een stap terug, waar je net vandaan kwam ...

```console
cd ..
```

Ben je nu weer terug in jouw *home directory*? Controleer het met `pwd` ...

```console
pwd
```

Dat is alles! Je kan nu de command line gebruiken. Er zijn een paar *erg* handige shortcuts die de command line *veel* efficiënter maken; efficiënter dan de drag-en-drop-vensterinterface! Een paar voorbeelden:

* *tab completion* Typ `cd Des` als je in je home directory staat en druk op de *tab*-toets. De command line zal je commando proberen aan te vullen. Ervaren (en luie!) gebruikers zullen lange namen bijna altijd met tab afmaken, in plaats van ze te typen. Het kan je veel tijd schelen!
* *pijltje omhoog* en *pijltje omlaag* De pijltje-omhoog- en pijltje-omlaag-toetsen onthouden wat je eerder gedaan hebt. Nadat je een commando hebt gebruikt, kan je deze met pijltje-omhoog terughalen. Je kan het ook bewerken (pijltje-links en pijltje-rechts werken hier ook) als je een fout maakt.

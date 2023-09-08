# AI voor Vier op een rij

| Naam         | Beschrijving                                                   |
|--------------|----------------------------------------------------------------|
| Onderwerp    | Meer kunstmatige intelligentie voor vier op een rij            |
| Bestandsnaam | `wk11ex2.py`                                                   |
| Inleveren    | Lever jouw bestand met de juiste bestandsnaam in op GradeScope |
| Opmerking    |                                                                |

## Overzicht

In deze opgave ga je met Python een eerste versie van een kunstmatige intelligentie bouwen om Vier op een rij te spelen.

Deze AI kan

* Eén zet vooruitkijken voor beide spelers, `'X'` en `'O'`
* Een zet kiezen waarmee het spel gewonnen wordt (als dat kan!)
* Een zet kiezen die de overwinning van de tegenstander kan ***voorkomen*** (in de volgende beurt; als dat kan)
* Zijn maker verslaan in Vier op een rij (*misschien*...)

Als je een sterkere en geavanceerdere AI wil maken voor Vier op een rij kan je dit als [project](/projects/connectfour.md) doen...

## De opgave

Kopieer eerst je bestand `wk10ex2.py` met de klasse `Board` naar een nieuw bestand, genaamd `wk11ex2.py`.

Voor deze opgave moet je twee methodes toevoegen aan de klasse `Board`; en één andere methode aanpassen:

* Voeg een methode `cols_to_win(self, ox)` toe die een lijst teruggeeft van kolommen waar `ox` mee wint op de volgende beurt, en
* Voeg een methode `ai_move(self, ox)` toe, een AI voor `ox`, dus `'X'` of `'O'`, die één zet vooruitkijkt:
    * Als de speler van `ox` kan winnen; of als dat niet kan, als deze een overwinning kan tegenhouden; dan moet die zet gedaan worden.
    * Als de AI echter geen zet heeft om te winnen of de tegenstander tegen te houden, dan mag je zelf bepalen hoe de zet gekozen wordt, bijvoorbeeld strategisch (een zet in het midden?), willekeurig, of met een andere aanpak...
* Pas ten slotte `host_game` aan om je nieuw gemaakte AI te gebruiken!

Hierna worden deze methodes en aanpassingen gedetailleerder beschreven

### De methode `cols_to_win`

De methode `cols_to_win(self, ox)` moet een onderdeel van de klasse `Board` zijn en een enkel argument `ox` meekrijgen, die een string `'X'` of een string `'O'` bevat (de twee mogelijke spelers in het spel).

De methode `cols_to_win` moet dan een ***lijst*** kolommen teruggeven waar `ox` in de volgende beurt kan spelen om het spel te winnne. De kolommen moeten op volgorde van hun nummer worden teruggegeven (als er meerdere mogelijkheden
zijn om te winnen). `cols_to_win` hoeft *niet* verder dan één beurt vooruit te kijken. Als je software wilt schrijven die verder vooruit kijkt, probeer dan het project over Vier op een rij!

:::{admonition} Tip
:class: tip

Voer onderstaande stappen uit voor elke kolom op het bord:

* Kijk of er een legale zet gedaan kan worden met behulp van `allows_move`.
* Voeg een steen van `ox` toe met behulp van `add_move`
* Kijk of de speler nu gewonnen met behulp van `wins_for`
* Als dat zo is, voeg dan het kolomnummer aan een lijst toe.
* *Vergeet niet de steen te verwijderen* voordat je verder gaat, met behulp van `del_move`!
* Vergeet niet om te lijst terug te geven aan het einde van de functie!
:::

Hier is een voorbeeld; *zorg ervoor dat deze werkt!*

```ipython
In [24]: b = Board(7, 6)

In [25]: b.set_board('334050505')

| | | | | | | |
| | | | | | | |
| | | | | | | |
|O| | | | |X| |
|O| | |O| |X| |
|O| | |X|X|X| |
---------------
 0 1 2 3 4 5 6

In [26]: b.cols_to_win('X')
Out[26]: [2, 5, 6]

In [27]: b.cols_to_win('O')
Out[27]: [0]
```

### De methode `ai_move`

De methode `ai_move(self, ox)` moet ook een onderdeel zijn van de klasse `Board` en moet een enkel argument
`ox` meekrijgen, die ofwel de string `'X'` bevat ofwel de string `'O'` (de twee mogelijke spelers in het spel).

`ai_move` moet een enkele integer teruggeven, die een geldige kolom bevat om een zet in te doen. **Bovendien**

* **moet** `ai_move` een zet (kolomnummer) teruggeven waarmee `ox` kan winnen. De AI moet winnen als dat mogelijk is. Als er meerdere manieren zijn om te winnen, mag elk van de winnende kolommen teruggegeven worden.
* **moet** `ai_move` een zet teruggeven waarmee de overwinning van de tegenstander geblokkeerd wordt, als `ox` zelf **niet** kan winnen maar **wel** een vier op een rij kan tegenhouden. Ook hier moet niet meer dan één zet vooruit gekeken worden. Als er geen mogelijkheid is om te winnen, maar er wel meer manieren zijn om de tegenstander te blokkeren, dan moet `ai_move` één van die manieren teruggeven. (Zelfs als de tegenstander op een andere manier alsnog kan winnen.)
* Als `ox` **niet** kan winnen en **geen** overwinning van de tegenstander kan blokkeren, dan moet `ai_move` een zet naar keuze van de programmeur (jij) teruggeven; deze zet moet wel legaal zijn. `ai_move` wordt *niet* aangeroepen als het bord vol is.

In het laatste geval kan de keuze willekeurig of strategisch zijn. In beide gevallen kan je meedoen aan het toernooi voor bonuspunten! We gaan de `ai_move`s vaak tegen elkaar laten spelen om te kijken welke het beste is in het spelen van Vier op een rij. (Dit doen we meestal in het laatste college...)

Er zijn een aantal strategieën die goed kunnen werken, bijvoorbeeld,

* Bij voorkeur in het midden van het bord spelen, of
* Proberen de twee op een rij van de tegenstander te blokkeren, of
* Proberen open ruimte te hebben aan één zijkant, of
* Iets anders, misschien nog geavanceerder.

Uiteindelijk mag je zelf bepalen welke strategie je volgt. De enige regel is dat `ai_move` geldige zetten moet doen, moet winnen als dat kan, en overwinningen van de tegenstander moet blokkeren als ze zelf niet kan winnen.

:::{admonition} Lus niet over de kolommen van het bord!
:class: tip

In plaats daarvan kan je

* `cols_to_win` aanroepen voor `ox`.
* `cols_to_win` aanroepen voor de tegenstander van `ox` (je hebt hiervoor een `if`/`else` nodig).
* De resultaten op de juiste manier verwerken.
* Bedenk je dat als er geen manier is om te winnen of te verliezen, elke geldige zet goed is.
* Vergeet niet het kolomnummer van de zet terug te geven.
:::

Hier zijn twee voorbeelden; zorg dat bij jou ook deze werken!

```ipython
# Voorbeeld 1

In [32]: b = Board(7, 6)

In [33]: b.set_board('334050505')

| | | | | | | |
| | | | | | | |
| | | | | | | |
|O| | | | |X| |
|O| | |O| |X| |
|O| | |X|X|X| |
---------------
 0 1 2 3 4 5 6


In [34]: b.ai_move('O')
Out[34]: 0

In [35]: b.ai_move('X')
Out[35]: 2    # 5 of 6 mogen ook hier


# Voorbeeld 2

In [42]: b = Board(7, 6)

In [43]: b.set_board('42424')

| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | |X| | |
| | |O| |X| | |
| | |O| |X| | |
---------------
 0 1 2 3 4 5 6


In [44]: b.ai_move('X')
Out[44]: 4      # moet 4 zijn

In [45]: b.ai_move('O')
Out[45]: 4      # moet 4 zijn
```

### De methode `host_game`

Pas ten slotte je methode `host_game(self)` aan zodat ofwel `'X'` ofwel `'O'` zelfstandig kan spelen;
dat wil zeggen, dat de computer deze speler bestuurt met de methode `ai_move`.

:::{admonition} Opmerking
:class: notice

Je mag zelf kiezen of de computer `'X'` of `'O'` speelt.
:::

Als de computer van je wint, gefeliciteerd! Je hebt een AI gemaakt die slimmer is gebleken dan zijn
schrijver, hoe gevaarlijk dat ook moge zijn op de langere termijn!

## Bonusopgaven

Hieronder staan een aantal functionaliteiten die je kan toevoegen voor bonuspunten.

### Meer opties voor de AI

Je kan voor maximaal 5 bonuspunten proberen onderstaande functionaliteiten toe te voegen:

* De methode `host_game` kan de speler vragen of hij of zij `'X'` of `'O'` wil spelen en de AI de andere speler laten zijn. (2 bonuspunten)
* Of je kan de speler de mogelijkheid geven om aan te geven dat `'X'` en `'O'` ALLEBEI door de AI gespeeld moeten worden. (3 bonuspunten)
  * In dat geval moet de AI tegen zichzelf spelen, en het resultaat van het spel laten zien.
* Als je nog andere creatieve functionaliteiten bedacht hebt, mag je die natuurlijk maken.

We wensen je AI veel succes!
# De evolutie van Picobot

Dit is een vervolg van de context opdracht van week 13. [De evolutie van Picobot](13_picobot_milestone.md)

## Wat nu?

Je hebt nu al het grootste deel van het programma geschreven! De rest kan je schrijven in een aantal korte functies (buiten de klassen `Program` en `World`) in de main.py file.

### Een willekeurige populatie

Je hebt bijvoorbeeld een erg korte functie nodig die de grootte van een populatie meekrijgt en een populate (een Python-lijst) met dat aantal willekeurige Picobot-programma's teruggeeft.

### Een fitness-evaluatiefunctie `evaluate_fitness`

Een erg korte fitness-evaluatiefunctie die de fitness van een gegeven Picobot-programma bepaalt. Deze functie krijgt de naam `evaluate_fitness(program, trials, steps)`. De argumenten zijn een Picobot-programma `program`, een positieve integer `trials` die het aantal willekeurige beginposities die getest moeten worden, en een positieve integer `steps` die het aantal stappen dat de simulatie mag nemen aangeeft. De functie geeft de fitness (een floating-pointgetal tussen 0.0 en 1.0) terug die overeenkomt met het percentage van de cellen die dit Picobot-programma bezoekt, gemiddeld over het aantal `trials`. Je kan hiervoor `fraction_visited_cells` gebruiken.

Stel je als voorbeeld voor dat `p` een Picobot-programma is en we `evaluate_fitness(p, 42, 1000)` uitvoeren. Deze functie kiest dan een willekeurige startpositie voor Picobot, voert het gegeven programma 1000 stappen lang uit, en berekent het percentage bezochte cellen. Daarna wist het de ruimte, kiest een nieuwe startpositie en doet het nog een keer; 42 keer in totaal.

Na alle 42 tests neemt de code het gemiddelde van het percentage van bezochte cellen van alle pogingen.

:::{admonition} Opmerking
:class: notice

De ruimte bevat 529 cellen (23 bij 23 lege cellen), dus zelfs een programma met relatief hoge fitness heeft een stuk meer dan 529 stappen nodig heeft om een groot deel van de ruimte te vullen, omdat het onwaarschijnlijk is dat het programma erg efficiënt zal zijn. Dat is waarom je misschien 1000 `steps` gebruikt, of zelfs een nog hoger aantal, in plaats van 529.
:::

### De hoofdfunctie `genetic_algorithm`

De **hoofdfunctie** moet naar het onderwerp, genetische algoritmes, vernoemd worden: `genetic_algorithm(pop_size, num_gens)`.

Deze functie `genetic_algorithm(pop_size, num_gens)` moet `pop_size` willekeurige Picobot-programma's genereren als de beginpopulatie (200 is hier een goede waarde voor). Daarna moet de fitness van al deze programma's geëvalueerd worden, en moet je de programma's met de hoogste fitness kiezen. Deze programma's overleven en dienen bovendien als "ouders" voor de volgende generatie.

:::{admonition} List-of-lists
:class: tip

Je kan een lijst met paren met (fitness, programma) sorteren. Stel dat dit de lijst `programs =  [(.4, prog1), (.2, prog2), (.3, prog3)]` is, dan kan je

```python
sorted_programs = sorted(programs)
```

aanroepen en zal je zien dat `sorted_programs` gelijk wordt aan `[(.2, prog2), (.3, prog3), (.4, prog1)]`
:::

:::{admonition} Het aantal overlevende programma's
:class: tip

10% van de populatie (bijvoorbeeld 20 van de 200) is een goede keuze voor het aantal overlevende programma's, maar je mag hier natuurlijk mee experimenteren.
:::

De overlevende programma's moeten **bewaard** blijven als onderdeel van de volgende generatie; die moet vervolgens aangevuld worden met "kinderen", nieuwe programma's.

:::{admonition} Kinderen maken
:class: tip

Om deze kinderen te maken kan je bijvoorbeeld deze aanpak gebruiken:
* Twee willekeurige ouders kiezen uit de programma's met hoge fitness.
* `crossover` gebruiken om een programma te maken die een "kind" is deze twee ouders.
* Af en toe `mutate` gebruiken (de kans hierop moet je zelf inregelen...). Als er te veel mutatie is wordt fitness niet bewaard. Als er te weinig is zal het gebrek aan nieuwe genen de evolutie beperken.

De details van het maken van kinderen bepalen hoe effectief je genetisch algoritme is; hier zul je moeten experimenteren!
:::

Je hebt nu een nieuwe populatie, hopelijk met hogere fitness, dus kan je nu het hele proces herhalen. Het is het beste om elke generatie even groot te laten zijn (`pop_size`), bijvoorbeeld 200.

Aan het eind moet je programma het beste programma uit de laatste generatie teruggeven (en als je wilt afdrukken). Je kan dan dat programma kopiëren en plakken in de Picobot-simulator om hem uit te voeren!

:::{admonition} Programma's bewaren
:class: tip

Je kan het handig vinden om het beste programma van elke generatie op te slaan in een bestand (dat is minder onoverzichtelijk en makkelijker te bewaren). Hier is een stukje code om dit makkelijker te maken:

```python
def save_to_file(filename, p):
    """Saves the data from Program p
        to a file named filename."""
    f = open(filename, 'w')
    print(p, file=f)        # print het Picobot-programma met __repr__
    f.close()

# hier is hoe je dit gebruikt... vermoedelijk in de hoofdlus van genetic_algorithm...
save_to_file('gen1.txt', best_p_in_gen_1)
save_to_file('gen2.txt', best_p_in_gen_2)  # enzovoorts...
```
:::

Ongeacht of je je programma's in bestanden opslaat of op het scherm afdrukt moet je in elke iteratie van de generatielus van `genetic_algorithm` zowel de ***gemiddelde*** als de ***maximale*** fitness van programma's in die generatie van de simulatie afdrukken. Hier is een voorbeeld (waarin de beste programma's niet getoond worden omdat ze naar aparte bestanden worden geschreven):

  ```ipython
  In [42]: genetic_algorithm(200, 15)
  Fitness wordt gemeten met 20 willekeurige tests en met 800 stappen per test:

  Generatie  0
    Gemiddelde fitness:  0.0575675
    Hoogste fitness:  0.217125

  Generatie  1
    Gemiddelde fitness:  0.08800625
    Hoogste fitness:  0.453125

  Generatie  2
    Gemiddelde fitness:  0.1041525
    Hoogste fitness:  0.343625

  Generatie  3
    Gemiddelde fitness:  0.113141875
    Hoogste fitness:  0.41525

  ...

  Generatie 14:
    Gemiddelde fitness:  0.869975625
    Hoogste fitness:  0.880875

  Beste Picobot-programma (ook in gen14.txt):
  3 xExx -> W 3
  1 xxWx -> E 2
  1 NExx -> W 4
  1 xxxS -> N 0
  0 xxWS -> N 1
  3 xxxx -> S 2
   ... rest van het programma overgeslagen ...
  ```

:::{admonition} Hulpfuncties
:class: notice

Als je een aantal hulpfuncties wilt schrijven hiervoor mag dat natuurlijk!
:::

:::{admonition} Keuzes voor de parameters
:class: tip

Als je wilt kan je wat lezen over hoe je de programma's met de hoogste fitness kan kiezen om die zich te laten voortplanten en de [keuzes voor de parameters](/support/picobot_parameters) die daar bij horen (maar het staat je natuurlijk vrij om er mee te experimenteren en andere te kiezen).
:::

### Hoe snel en hoe "goed" moet mijn programma zijn?

Met de parameterwaardes die hierboven genoemd zijn moet het uitvoeren van `genetic_algorithm(200, 20)` ongeveer 60 secondes per generatie duren. Je beginpopulatie heeft vermoedelijk een gemiddelde fitness van ongeveer 1% tot 2%. De gemiddelde fitness moet elke generatie langzaam toenemen; er kunnen hier misschien een paar uitzonderingen op zijn. De maximale fitness neemt normaal gesproken toe, maar ook hier kan die af en toe afnemen.

Na 20 generaties zou je een maximale fitness van 80% tot 90% moeten zien, soms zelfs nog hoger.

## De Opdracht

 `main.py`, moet aan de volgende eisen voldoen:

* Het importeert `program.py` en `world.py`. 
* De file bevat twee werkende functies `genetic_algorithm`,  `evaluate_fitness` en `save_to_file`
* De main functie dat alles aanstuurt. 

Test je programma zorgvuldig. Het kan zijn dat je tot de conclusie komt dat je crossover-mechanisme (voor het paren van programma's) niet erg effectief is. Dan moet je experimenteren met andere manieren om crossover te regelen.


## Optionele bonusuitbreidingen

Als je de genetische-algoritmeaspecten van het probleem verder wilt verkennen, kan je deze extra vragen nog onderzoeken:

* Hoe goed kan je een programma evolueren om het *doolhof* op te lossen (met een andere ruimte in `World`...)? Het doolhof is erg moeilijk om op te lossen op deze manier; je kan de ruitvormige ruimte gebruiken als tussenweg.
* Het is mogelijk om een programma met behoorlijke fitness te evolueren *helemaal zonder crossover*! Het idee is dat je het programma met de hoogste fitness bewaart en mutatie gebruikt om de volgende generatie te maken. Dit werkt, maar duurt normaal gesproken langer.

Ontwerp en implementeer de noodzakelijke software-ondersteuning om te testen *hoeveel groter de populatie moet zijn* of *hoeveel meer generaties je nodig hebt* (of allebei) om een programma te evolueren met alleen mutatie dat een even hoge fitness heeft als een programma dat met mutatie en crossover geëvolueerd is.


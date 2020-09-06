# Programmeren

## Wat is programmeren

**ICT != programmeren**

Eerder hebben we gezien dat programmeren maar een onderdeel is van informatica. Het is alleen van belang bij de vraag of je een proces kan ontwerpen voor het oplossen van een probleem. Of met ander woorden, het bedenken van *een recept*. (`!=` betekent *niet gelijk aan*, onze eerste programmacode!)

## Programmeren

- het schrijven van recepten
- het leren van een vreemde taal

Leren programmeren gaat zowel over het kunnen schrijven van een recept maar ook het leren van een vreemde taal!

![Not a ‘math person’?](images/2/uw_math_person_coding.png)

Het leren van een programmertaal is niet veel anders dan het leren van een natuurlijke taal als Frans of Engels. Verwacht dan ook dat je het pas leert door het te doen. En of je nou [wel of niet goed bent in wiskunde](https://www.washington.edu/news/2020/03/02/not-a-math-person-you-may-be-better-at-learning-to-code-than-you-think/) (zoals soms wordt gezegd) heeft met het leren van een programmertaal niet heel veel te maken.

![Research](images/2/Prat-Scientific-Reports-Photo-1.jpg)

Door onderzoek komen we steeds meer te weten welke vaardigheden een rol spelen bij leren programmeren. Een van de onderzoekers demonstreert hier hoe de hersenactiviteit wordt gemeten tijdens het programmeren.

## Python

![Guido van Rossum](images/2/guido.jpg)

De taal Python (vermoemd naar [Monty Python](https://en.wikipedia.org/wiki/Monty_Python)) is bedacht door [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) toen hij werkte aan de Universiteit van Amsterdam. De eerste versie verscheen in 1991 en is inmiddels uitgegroeid tot één van de meest populaire programmeertalen!

## De vreemde taal Python

- syntax
- semantiek
- intentie

Of met andere woorden:

- hoe ziet het er uit (spelling)
- wat het doet (betekenis)
- wat het zou moeten doen (bedoeling)

Deze kenmerken komen overeen met die van natuurlijke talen, bijvoorbeeld Nederlands!

### Intentie

Wat het zou moeten doen: **gewenste output**

```python
import random

name = input("Hoi, wie ben jij? ")

if name == "Bas" or name == "Marian":  # is het Bas of Marian?
    print("Ik ben offline, probeer het later.")

elif name == "Alex":  # of is het Alex?
    print("Willem Alex...? Nee? Oh.")

else:  # anders...
    print("Welkom", name, "!")
    my_choice = random.choice(["steen", "papier", "schaar"])
    print("Mijn favoriet is", my_choice, "!")
```

De *bedoeling* is dat dit programma zou een gebruiker op de juiste manier groet.

Dit is de door ons (mensen) *gewenste output* van het programma.

### Semantiek

Wat het doet: **geproduceerde output**

```python
import random

name = input("Hoi, wie ben jij? ")

if name == "Bas" or name == "Marian":  # is het Bas of Marian?
    print("Ik ben offline, probeer het later.")

elif name == "Alex":  # of is het Alex?
    print("Willem Alex...? Nee? Oh.")

else:  # anders...
    print("Welkom", name, "!")
    my_choice = random.choice(["steen", "papier", "schaar"])
    print("Mijn favoriet is", my_choice, "!")
```

De instructies hebben voor de computer *betekenis* zolang het ze kan uitvoeren.

Dit levert door de machine *geproduceerde output* op.

![Flowchart](images/2/flow.png)

### Syntax

Hoe ziet het er uit: **spellingsregels**

![Het Groene Boekje](images/2/groene_boekje_2015.png)

Vergelijk syntax met wat je kent van de Nederlandse taal. Het Groene Boekje is de gebruikelijke naam van de Woordenlijst Nederlandse Taal, een overzicht van de officiële spelling van Nederlandse woorden, met onder andere het gebruik van dubbele en enkele klinkers, hoofdletters, koppeltekens en vervoegingen van werkwoorden. Met andere woorden, alles wat met de regels van de taal te maken heeft!

## Python syntax

- gebruik van leestekens (spatie, punt, ...)
- speciale woorden ("keywords")
- formattering
- hoe het gedrag beïnvloedt

En met "hoe het gedrag wordt beïnvloedt" bedoelen we dat het gebruik van syntax kan uitmaken hoe Python zich gedraagt, of *wat het doet*. Gelukkig is Python syntax een stuk minder complex dan talen als Nederlands (Het Groene Boekje telt meer dan 1200 pagina's!).

"42" * 2

Je ziet hier valide Python syntax, en misschien had je 42 willen vermenigvuldigen met 2, maar de uitkomst is een heel andere dan je had verwacht!

42 * 2

Dit lijkt meer op de verwachte uitkomst. Blijkbaar maakt het gebruik van aanhalingstekens uit en is het voor Python een manier om betekenis te geven aan de input waar het in het eerste geval 42 als "tekst" leest, en in het tweede geval als getal (onze bedoeling!).

### `SyntaxError`

Oftwel Python's manier om jou te vertellen dat de syntax niet juist is.

print("Steen, papier of schaar?')

Python zegt ons hier dat we een syntaxfout hebben gemaakt en probeert met de `^` aan te geven waar ongeveer de fout is. Kan je de fout ontdekken? En wat kan je hier uit afleiden? We gaan in de opdrachten uitgebreid stilstaan bij deze en andere fouten en we gaan je zelfs vragen om zoveel mogelijk fouten te maken!

## De uitdaging van programmeren

- syntax
- semantiek
- intentie

Als het gaat om programmeren, waar zit nu precies de uitdaging? Laten we de bovenstaande punten voor het gemak vertalen naar de volgende:

![Cyclus](images/2/cycle.png)

Het is deze cyclus die de uitdaging van programmeren illustreert, en vaak zal je deze cyclus meerdere keren moeten doorlopen om tot een gewenste uitkomst te komen...

## Quiz

```python
  import random
    
user = input( "Kies jouw wapen! " )

comp = random.choice( ['steen','papier','schaar")

print('user (jij) koos:', 'user')
print('comp (ik!) koos:' comp)
                       
if user == rock and comp = 'paper'
      print('Het resultaat is dat JIJ VERLIEST.'
    print('tenzij je een 'docent' bent, dan WIN JE!')
```

### Vraag 1

1.   Probeer zoveel mogelijk fouten te vinden (en te verbeteren!) in de bovenstaande code

2.   De regel 

     ```python
     user = input( "Kies jouw wapen! " )
     ```
    
     doet **3** dingen, kan jij ze noemen?

3.   Welke 7 [leestekens](https://nl.wikipedia.org/wiki/Leesteken) (punctuatie) zie jij gebruikt worden?

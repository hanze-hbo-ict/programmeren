# Wat is informatica

Voordat we beginnen, moeten we iets zeggen over informatica. Wat denk je dat informatica is?

Veel mensen denken dat het *programmeren* of gewoon *leren coderen* is of dat het iets met computers is.

Informatica is het verwerken van informatie. Gegeven een input, hoe verwerken we dat tot een gewenste output? Met andere woorden, het gaat om problemen oplossen. Programmeren is een belangrijk hulpmiddel om de computer de informatie te laten verwerken en tot de oplossing te komen. De truc is om als programmeur de computer uit te leggen hoe hij de data moet verwerken.

## Hoe kan een probleem worden opgelost?

- Kun je het probleem oplossen?
- Kun je een proces ontwerpen om dit soort problemen op te lossen?

Het is niet verstandig om, als er een probleem opgelost moet worden, meteen te gaan programmeren. Probeer eerst het probleem op papier op te lossen met een klein voorbeeld. Welke stappen/instructies zijn er gebruikt om het probleem op te lossen? Dit wordt computational thinking genoemd: de vaardigheid om een set van instructies te ontwikkelen dat een gegeven probleem kan oplossen. Deze set van instructies om van A naar B te komen wordt een algoritme genoemd.

## Strategieën

De strategie die gebruikt kan worden om een oplossing te vinden verschilt per probleem. De ene strategie past beter dan de andere, maar wat wel handig is, is om pen en papier te gebruiken. Hier zijn er een aantal:

1. *Teken het probleem op papier*. Dit werkt vooral als je met ruimtelijke vragen bezig bent.
2. *Maak het probleem kleiner*. Bijvoorbeeld: wordt er gevraagd om een methode te verzinnen om getallen te sorteren? In plaats van het probleem op te lossen met 100 getallen, doe het eerst met twee getallen, daarna met drie, enz.
3. *Probeer alle opties uit*. Deze leent zich vooral als er niet te veel verschillende beginsituaties zijn.

### Longest Common Subsequence (LCS)

Het string-matching probleem in DNA:

- 'CGCTGAGCTAGGCC...'
- 'ATCCTAGGTAACTG...' (en $10^9$ meer!)

Wat is de langst *gemeenschappelijke opeenvolging* van karakters? In biologie is dit een werkelijk probleem waar het gaat om het vergelijken van DNA-sequenties. Een subsequence is een reeks karakters die in dezelfde volgorde voorkomen in beide strings, *maar niet noodzakelijk aaneengesloten*.

In plaats van het probleem op te lossen op een grote dataset is het vaak makkelijker om eerst een kleinere dataset te proberen op te lossen. Bijvoorbeeld twee woorden:

- 'HUMAN'
- 'CHIMPANZEE'

Je zult misschien redelijk snel zien dat 'HMAN' de langst gemeenschappelijke opeenvolging van karakters is, het volgende verduidelijkt dit als we de twee woorden boven elkaar plaatsen en de plekken die niet overeenkomen markeren met een `-`:

```text
-HU-M-AN---
CH-IMPANZEE
```

Dit is de eerste stap van het oplossen van een probleem: de probeerfase.

Welke stappen heb je gebruikt om tot een oplossing te komen? Zijn deze stappen ook toe te passen op een opeenvolging van 3 miljard karakters? Dit is de planfase waarin het algoritme wordt ontworpen.

Zodra er een algoritme is ontworpen kan het geprogrammeerd worden. Dat is dan de programmeerfase.

## Beslissingsboom

Beslissingsbomen (*behavior trees*) kunnen gebruikt worden om instructies te visualiseren. Het is een vorm die je misschien wel herkent.

![Beslisboom](images/1/beslisboom.gif)

Dit is het algoritme van Euclides wat gebruikt kan worden om de grootste gemene deler (ggd) tussen twee getallen te bepalen. Euclides had ontdekt dat via een paar instructies altijd te berekenen is:

1. Noem het grootste van de beide getallen *m*, het andere *n*.
2. Deel *m* door *n*, bereken hoeveel je overhoudt en noem dat *r*.
3. Wanneer er 0 over blijft zijn we klaar, en is *n* de ggd.
4. Zo niet, herhaal dan het algoritme met *n* en *r*.

Met het algoritme van Euclides kan dus de ggd van 900 en 1140 berekend worden.
Stel dat *m* 1140 is en *n* 900,

$ 1140 = 1 * 900 + 240 $

De rest is 240, wat niet gelijk is aan 0 en dus moet er verder gerekend worden. Deze keer is *m* gelijk aan 900 en *n* gelijk aan 240.

$ 900 = 3 * 240 + 180 $

De rest is 180, wat niet gelijk is aan 0 en dus moet er verder gerekend worden. Deze keer is *m* gelijk aan 240 en *n* gelijk aan 180.

$ 240 = 1 * 180 + 60 $

De rest is 60, wat niet gelijk is aan 0 en dus moet er verder gerekend worden. Deze keer is *m* gelijk aan 180 en *n* gelijk aan 60.

$ 180 = 3 * 60 + 0 $

Nu is de rest 0, en daarmee zijn we aan het einde gekomen. We hebben bepaald dat 60 de grootste gemene deler van 900 en 1140 is.

## State Machine

Een andere methode voor het ontwerpen van programma's is het gebruik van een state machine. Deze manier leent zich er vooral voor om een probleem in kleinere problemen op te breken. Een state machine bestaat uit verschillende states (een staat, of situatie) en heeft altijd een *begin* en *eind* state. Tussen de states zijn overgangen die aangeven wanneer er van state veranderd wordt.

Neem bijvoorbeeld de spoken van Pac-Man. Zodra het spel begint zoeken ze naar Pac-Man en als ze hem zien gaan ze achter hem aan. Als Pac-Man een Power Pellet pakt moeten de spoken juist vluchten. Dit idee kan afgebeeld worden in een state machine.

![State Machine](images/1/pacmanStates.png)

Na het ontwerpen van de state machine kan er nagedacht worden over hoe de afzonderlijke problemen opgelost kunnen worden en dit kan weer gedaan worden met een beslissingsboom.

## 3 p's

De drie p's van het programmeren:

1. **Probeer**: Probeer het probleem op te lossen in gedachten of op papier.
2. **Plan**: Noteer de stappen die zijn gebruikt om het probleem op te lossen.
3. **Programmeer**: Vertaal de stappen naar een programmeertaal.

## Opdrachten

Deze opdrachten zijn ontworpen om je te helpen denken als een informaticus. Bij de eerste twee ontwikkel je een strategie voor een spel, bij de derde redeneer je naar een antwoord toe. Allebei zijn het vormen van het probleemoplossend denken dat essentieel is in de informatica, en voor allebei heb je nog geen regel Python nodig.

### Opdracht 1: Nim

![Nim 16 lucifers](images/1/NimGame.png)

Nim is een spel voor twee spelers. Er liggen 16 lucifers op tafel. Om de beurt pakt een speler 1, 2 of 3 lucifers. Degene die de laatste lucifer van tafel pakt heeft gewonnen. Als de speler die als tweede aan de beurt is de juiste strategie gebruikt, kan hij of zij altijd winnen.

- **Stap 1: Proberen.** Ga uitzoeken welke strategie speler 2 moet gebruiken om altijd te winnen. Speel het spel een paar keer tegen jezelf of een medestudent om patronen te ontdekken.
- **Stap 2: Plan.** Maak een beslissingsboom voor speler 2. Begin bij de startsituatie en werk alle mogelijke zetten uit tot je de winnende strategie ziet.

### Opdracht 2: Nim variant

Leg 3 groepjes lucifers op tafel. Het aantal lucifers in elke groep maakt niet uit. Om de beurt pakt een speler 1, 2 of 3 lucifers, **uit één groep**. Degene die de laatste lucifer van tafel pakt heeft gewonnen. Ook nu kan met de juiste strategie een speler altijd de winst garanderen.

Anders dan bij de vorige opgave ligt hier niet vast wíe er kan winnen. Dat hangt af van de beginopstelling, en dus is de eerste vraag niet hoe je wint maar of je wilt beginnen.

- **Stap 1: Proberen.** Speel een paar opstellingen na, bijvoorbeeld (3,4,5) en (1,2,3), en let erop of je in die stand liever als eerste of als tweede aan de beurt bent. Ze zijn niet allebei hetzelfde.
- **Stap 2: Plan.** Beschrijf twee dingen: hoe je aan een opstelling ziet of je wilt beginnen, en hoe je daarna wint. Je strategie moet voor elke beginopstelling werken, niet alleen voor de twee die je hebt gespeeld.

### Opdracht 3: Wie liegt er?

De vorige twee opgaven gingen over een strategie bedenken. Deze gaat over
redeneren naar één antwoord toe, en dat is minstens zo vaak wat je bij het
programmeren doet.

Ze lopen op in moeilijkheid. Schrijf bij elke puzzel je redenering op, niet
alleen je antwoord: die redenering is waar het om gaat.

**a.** Nate en Jeff komen uit een land waar sommige mensen altijd de waarheid spreken en de rest altijd liegt.

> Nate zegt: "Nate liegt en Jeff spreekt de waarheid."

Liegt Nate? En Jeff?

**b.** Suzy en Spike komen uit datzelfde land.

> Suzy zegt: "Spike spreekt de waarheid."
>
> Spike zegt: "Suzy liegt en ik spreek de waarheid."

Wie liegt er, en wie niet?

**c.** Fred, Wilma en Pebbles ook.

> Fred zegt: "Pebbles spreekt de waarheid."
>
> Pebbles zegt: "Ik lieg, of Wilma spreekt de waarheid."

Wie liegt er, en wie niet?

**d.** Het eiland Quork wordt bewoond door ridders en schurken. Ridders spreken altijd de waarheid, schurken liegen altijd. Op een dag zitten er elf bewoners in het café. Een toerist vraagt aan ieder van hen: "Hoeveel ridders zijn hier aanwezig?"

Hij krijgt deze elf antwoorden:

```text
3  2  5  7  2  3  4  4  3  2  5
```

Kan de toerist hieruit vaststellen hoeveel ridders er in het café zitten? Zo ja,
hoeveel, en hoe weet je dat zeker?

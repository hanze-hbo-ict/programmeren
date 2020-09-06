# Wat is informatica

Voordat we beginnen moeten we iets zeggen over informatica. Wat denk je dat informatica is?

Veel mensen denken dat het *programmeren* of gewoon *leren coderen* is.

Hoewel dit belangrijke onderdelen binnen informatica zijn, en zeker ook belangrijke hulpmiddelen voor het helpen oplossen van problemen waar we in geïnteresseerd zijn, is informatica zo veel meer dan alleen maar programmeren.

## Oplossen van problemen

-   Hoe kan een probleem worden opgelost
-   Hoe goed kan een probleem worden opgelost
-   Kan elk probleeem worden opgelost

Als het gaat over het oplossen van problemen wil informatica deze *drie* belangrijke vragen proberen te beantwoorden.

## Hoe kan een probleem worden opgelost

- Kan je het probleem oplossen?
- Kan je een proces ontwerpen om dit soort problemen op te lossen?

Computers zijn goed in het volgen van instructies. Dat betekent dat als jij een aantal instructies kan bedenken die altijd een bepaald soort probleem kan oplossen, deze instructies waarschijnlijk ook kunnen worden omgezet in een computerprogramma.

Bijvorbeeld: het Longest Common Subsequence (LCS) probleem voor het zoeken naar de langste opeenvolging van karakters die twee woorden met elkaar gemeen hebben.

### Longest Common Subsequence (LCS)

Het string-matching probleem in biologie:

- 'HUMAN'
- 'CHIMPANZEE'

Wat is de langst *gemeenschappelijke opeenvolging* van karakters?


Het vergelijken van stukken tekst en zoeken naar overeenkomsten (string-matching).

Welke opeenvolging van karakters hebben deze twee woorden met elkaar gemeen? Je zult redelijk snel zien dat 'AN' de langst gemeenschappelijke opeenvolging van karakters is.

Zou je ook kunnen beschrijven *hoe* je tot de oplossing bent gekomen?

- 'CGCTGAGCTAGGCC...'
- 'ATCCTAGGTAACTG...' (en $10^9$ meer!)

In biologie is dit een werkelijk probleem waar het gaat om het vergelijken van DNA-sequenties.

Denk even terug aan het vorige (eenvoudige) voorbeeld en hoe je tot de oplossing bent gekomen (de stappen, het proces).

Zou je dit ook kunnen toepassen op een opeenvolging van drie miljard karakters?

We spreken hier over een proces als een aantal opeenvolgende stappen die moet worden genomen om tot de oplossing van een probleem te komen. Je kan dit vergelijken met een recept: welke handelingen moeten worden toegepast op de ingrediënten (input) om tot en een appeltaart (output) te komen. In informatica gebruiken we hier het woord *algoritme* voor.

## Hoe goed kan een probleem worden opgelost

- Hoe snel kan je de oplossingen vinden?
- Is jouw oplossing de best mogelijke oplossing?

Soms kunnen we een manier vinden om een probleem op te lossen, maar is het te traag. Het zal je misschien verbazen dat we ons zorgen moeten maken over snelheid, zeker nu computers zo snel zijn, maar er zijn problemen die zo groot dat we ons zorgen moeten maken over hoe snel het programma is.

Natuurlijk kan het ook zo zijn dat we een oplossing vinden, maar het misschien niet de beste oplossing is.

Bijvoorbeeld: wat is nodig om $N$ sterren te simuleren.

### Het N-body probleem

De interactie tussen hemellichamen

- het effect van zwaartekracht

We weten inmiddels hoe de aarde en de maan elkaars gedrag beïnvloeden ($N=2$)

Hoewel het hier specifiek gaat over zwaartekracht geldt in het algemeen het bepalen van interactie-effecten ook bijvoorbeeld op atomair niveau. Het $N=2$ probleem kan analytisch worden opgelost, bij $N=3$ wordt dit al anders en is een bekend probleem in de astrofysica (het [drie hemellichamen](https://www.volkskrant.nl/wetenschap/astrofysici-opgetogen-over-nieuwe-rekenvondst-supercomputer-enorme-stap-in-eeuwenoud-vraagstuk~b0ca9663/) probleem). Laten we eens naar ons sterrenstelsel kijken ...

### De Melkweg

100 - 400 miljard sterren ($N=10^{11}$, of meer ...)

Wat is nodig om $N$ aantal sterren te simuleren?

Hoe goed kan een probleem worden opgelost:

- Hoe snel kan je oplossingen vinden?
- Is jouw oplossing de best mogelijke oplossing?

Als we te maken hebben met zéér grote hoeveelheden data, zijn de oplossingen (algoritmen) die we hebben bedacht voor kleinere hoeveelheden nog steeds van toepassing? Bijvoorbeeld, is de tijd of rekenkracht die nodig is acceptabel of zijn betere oplossingen mogelijk?

## Kan elk probleeem worden opgelost

- Is elk probleem op te lossen?
- Hoe weet je of het kan worden opgelost?

Tot slot, als het probleem bijzonder lastig is zullen we ons moeten afvragen of het kan worden opgelost.

En bovendien zullen sommige problemen niet opgelost kunnen worden omdat onvoldoende informatie bekend is.

Bijvoorbeeld: kan een 3D model van een 2D weergave worden gemaakt?

### Van 2D naar 3D

Is het mogelijk om van een 2D afbeelding een 3D representatie te maken?

<p><iframe width="560" height="315" src="https://www.youtube.com/embed/GWWIn29ZV4Q" frameborder="0" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></iframe></p>

Is het probleem opgelost? Nee, op basis van beperkte informatie (twee dimensies) wordt een zo goed mogelijke *inschatting* gemaakt van een derde dimensie.

Met andere woorden, deze oplossing biedt niet meer dan een benadering van het probleem in de vorm van de [*suggestie*](http://make3d.cs.cornell.edu/research.html) van een derde dimensie. De mens is ontvankelijk voor suggestie: een opeenvolging van 30 afbeeldingen per seconde interpreteren wij als beweging (video).

### *Let's enhance*

Bekend van film en TV!

<p><iframe width="560" height="315" src="https://www.youtube.com/embed/LhF_56SxrGk" frameborder="0" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>

Hoe vak heb je dit niet gezien, op magische wijze een afbeelding opblazen en verscherpen tot de dader scherp in beeld komt! Dit is niet realistisch omdat de data pixels zijn (beeldpunten) waar hooguit het *contrast* van kan worden vergroot, maar niet de *resolutie* (het aantal beeldpunten).

![Training bias](images/1/depixel-white.png)

<!-- https://github.com/tg-bomze/Face-Depixelizer -->

Pogingen worden wel gedaan om ontbrekende informatie aan te vullen, bijvoorbeeld op basis van andere (vergelijkbare) afbeeldingen. Dit kan soms tot bijzondere resultaten leiden als de afbeeldingen waarmee vergeleken wordt [weinig divers](https://www.businessinsider.com/depixelator-turned-obama-white-illustrates-racial-bias-in-ai-2020-6) zijn (en een *bias* introduceren).

## De studie van complexiteit

- programmeren
- abstracties
- algoritmen

Wat de bovenstaande vragen met elkaar gemeen hebben is dat ze alle drie te maken hebben met *complexiteit*, of hoe hoe moeilijk het is om een bepaald probleem op te lossen. Je hebt technieken en gereedschappen nodig om te helpen denken over complexiteit, en je gaat met een aantal hiervan kennismaken.

### Programmeren

- Python

Bijvoorbeeld, het is handig om te kunnen programmeren, en daar ga je Python voor leren. Maar ook ga je kennismaken met Hmmm, een hele bijzonder taal!


- Kan je het probleem oplossen?
- **Kan je een proces ontwerpen om dit soort problemen op te lossen?**
- Hoe snel kan je een oplossingen vinden?
- Is jouw oplossing de best mogelijke oplossing?
- Is elk probleem op te lossen?
- Hoe *weet* je of het kan worden opgelost?

Denk even terug aan de vragen die we eerder hebben gesteld. Het enige moment waar programmeren van toepassing is is bij het laten uitvoeren van onze oplossing door de machine!

### Abstracties

- getallen
- letters
- kleuren

Het kan ook handig zijn om te weten wat jouw computer eigenlijk doet, en zo gaan we kijken naar hoe de hardware werkt en hoe het bijvoorbeeld getallen, letters en kleuren kan representeren.

### Algoritmen

Soms kan een probleem efficiënt of minder efficiënt worden opgelost, dus gaan we het ook hebben over verschillende algoritmen. Denk bij een algoritme aan een "recept", de stappen die je neemt om tot een bepaalde oplossing te komen.
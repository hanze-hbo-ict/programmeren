# Onderwerpen

![Schotel](/images/saucer.png)

## Use it or lose it en `lambda`

Deze week leer je twee dingen. Het eerste is **use it or lose it**: bij elk
element van een lijst probeer je twee keuzes uit, het element gebruiken of het
laten liggen. Dat zijn twee recursieve aanroepen, en hun uitkomsten combineer je
tot het antwoord. Zo los je problemen op waarbij je vooraf niet weet welke keuze
de goede is, zoals een bedrag precies betalen met de munten in je portemonnee.
Het tweede is een **functie als argument**: je geeft een functie mee aan een
andere functie, bijvoorbeeld aan `sorted` met `key=`, om te zeggen waarop ze
moet sorteren. Een kleine functie schrijf je daarvoor ter plekke op, als
lambda-functie met `lambda`.

Het eerste college gaat over *use it or lose it*, met het wisselgeld en de
knapzak. Dat heb je nodig voor het tweede deel van de opstap, voor de basis over
algoritmen, voor de twee extra's en voor het werkcollege, waarin je uitrekent met
hoeveel munten je een bedrag betaalt. Het tweede college gaat over `sorted`,
`max` en `min` met `key=`, over `lambda`, en over een eigen functie met een
functieparameter. Dat heb je nodig voor het eerste deel van de opstap en voor de
basis over `lambda`. *Caesar op orde* herhaalt de stof van beide colleges.

Aan het eind van de week kun je bij een probleem met keuzes beide keuzes
recursief uitproberen en de beste kiezen, en kun je een functie meegeven als
argument, als bestaande functie, als eigen functie of als lambda-functie.

### Waar je vandaan komt

In [week 3](/course/week_10) leerde je recursie: een basisgeval, een recursief
geval met de recursieve aanroep, en een frame op de stack voor elke aanroep. Daar
had elk recursief geval één recursieve aanroep. Het tweede college sloot af met
de vraag of je met munten van 20, 50 en 50 cent precies 70 of 80 cent kunt
betalen; die vraag beantwoordt het eerste college van deze week. `largest` en
`best_word` uit week 3 kozen het beste element uit een lijst. In
[week 2](/course/week_9) leerde je list comprehensions, en de extra-opgave sloot
af met een vooruitblik op `sorted(totals, key=totals.get)`. Het tweede college
legt uit hoe dat werkt.

```{tableofcontents}
```

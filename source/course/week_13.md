# Onderwerpen

![Schotel](/images/saucer.png)

## Overerving, polymorfisme en duck typing

Deze week bouw je klassen die voortbouwen op een klasse die er al is. Bij
**overerving** krijgt een **subklasse** alle attributen en methoden van haar
**superklasse** mee. Met `super()` roep je vanuit de subklasse de versie van de
superklasse aan, bijvoorbeeld de constructor. Wat bij de subklasse anders is,
schrijf je zelf: je **overschrijft** een methode met een eigen versie. Daarbij
leer je een parameter een **standaardwaarde** te geven, die geldt als je het
argument weglaat.

Bij **polymorfisme** geeft één aanroep ander gedrag, afhankelijk van het object.
Een lus die bij elk wezen `special_move` aanroept, hoeft niet te weten of ze een
draak of een genezer voor zich heeft. Bij **duck typing** doet een object mee
omdat het de methoden en attributen heeft die worden gebruikt, ook als het geen
subklasse is van dezelfde klasse.

Je leert ook vragen van welke klasse een object is. `x.__class__.__name__` is de
naam van de klasse van `x`, en `isinstance(x, K)` zegt of `x` een object is van de
klasse `K` of van een subklasse ervan. Code die met duck typing werkt, stelt die
vraag juist niet.

Een subklasse gebruik je als het nieuwe ding een soort is van het oude: een
deeltijdstudent is een student. Heeft het nieuwe ding zulke objecten als
onderdeel, zoals een studiegroep studenten heeft, dan is het compositie uit
week 5.

Aan het eind van de week kun je een klasse uitbreiden tot subklassen die alleen
schrijven wat anders is, en code schrijven die met al die klassen werkt zonder te
vragen welke het is.

### Waar je vandaan komt

In [week 5 van Programmeren 2](/course/week_12) schreef je klassen die hun eigen
staat bewaken: `Student` en de studiegroep in het college, `Creature` en `Party` in
het practicum, en `Board` in de extra-opgave. Deze week bouw je op alle drie voort.
De studiegroep uit week 5 is compositie; deze week komt overerving ernaast.

```{tableofcontents}
```

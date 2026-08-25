# Leerlijn

Wat er per week gebeurt, welke leeruitkomsten er landen, en welke begrippen er
voor het eerst worden geïntroduceerd.

Die laatste kolom is het dragende deel van dit document. Zolang vastligt waar een
begrip voor het eerst hoort, is een vooruitverwijzing te detecteren: materiaal
dat iets gebruikt wat volgens dit document later pas komt.

De weergegeven staat is **het materiaal zoals het nu is**, gemeten aan de
inhoudsopgave en aan het eerste voorkomen van begrippen in de tekst. Waar de
afgesproken richting daarvan afwijkt, staat dat erbij.

Dit document is voor auteurs en docenten, niet voor studenten.

## Programmeren I

| Week | Onderwerp | Leeruitkomsten | Voor het eerst geïntroduceerd |
|---|---|---|---|
| 1 | Introductie, Picobot | - | toestandsmachine, regels, string, methode |
| 2 | Variabelen en condities | P1, P2, P3 | toekenning, variabele, operatoren, `if`, lijst, docstring, assertion |
| 3 | Functies | P5, A2 | functiedefinitie, parameter, **recursie**, 2D-lijst |
| 4 | Lussen | A1 | `for`, begrensde herhaling |
| 5 | Geneste lussen | A1, A3 | geneste lus, ASCII-art, bordrepresentatie |
| 6 | Data | P4 | binair, talstelsel, beeldbewerking |
| 7 | Meer data | P4, A3 | dictionary, bestanden lezen, Markov |

Recursie (A4) wordt in week 3 geïntroduceerd en daarna niet meer uitgewerkt; de
uitwerking zit in PGM2. Zie het gat hieronder.

## Programmeren II

Voor PGM2 lopen twee beelden uiteen: wat het materiaal nu doet, en wat voor
studiejaar 2026 is afgesproken.

| Week | Materiaal nu | Afgesproken voor 2026 |
|---|---|---|
| 1 | List comprehension | datastructuren |
| 2 | Recursie | comprehensions (list, dict, set, range, enumerate) |
| 3 | Algoritmen (knapzak, wisselgeld) | recursie |
| 4 | Objecten en dictionaries | use it or lose it, lambda |
| 5 | Kunstmatige intelligentie | OO, klassen, encapsulatie |
| 6 | Vier op een rij, AI-speler | polymorfisme, overerving, duck typing |
| 7 | - | operator overloading, oefentoets |

Begrippen die in PGM2 voor het eerst opduiken: klasse en object (week 4 in het
huidige materiaal), operator overloading (idem), lambda (nergens).

## Gaten tussen toetsing en materiaal

Gemeten op het voorkomen van de betreffende constructies in `source/`.

| Leeruitkomst | Weging | Bevinding |
|---|---|---|
| **PGM2 P4** excepties | 10% | Twee bestanden. In `problems/5_basis` staat `try`/`except` in *gegeven* code van het menuprogramma, niet als uitleg. Nergens onderwezen. |
| **PGM2 P3** tekstbestanden | 10% | Drie plekken, waarvan twee in de Markov-opgave van PGM1 week 7. |
| **PGM1 A4** recursie | 10%, creëren | Eén college in week 3, daarna pas PGM2. Het toetsniveau is het hoogste van de matrijs; het aanbod is het smalst. |
| **PGM2 P1** lussen | 5% | Wordt in PGM1 onderwezen (week 4 en 5) en in PGM2 getoetst. Kan bedoeld zijn als herhaling, maar staat niet in de planning voor 2026. |
| **PGM2 A5** finite state machines | geen | Komt nergens voor. Voorstel is schrappen; zie [leeruitkomsten.md](leeruitkomsten.md). |

De eerste twee zijn kandidaat om in PGM1 te landen. Voor bestanden ligt de haak
er al: de Markov-opgave in week 7 leest een tekstbestand.

## Vooruitverwijzingen om na te lopen

Begrippen die eerder in het materiaal opduiken dan waar ze volgens de leerlijn
thuishoren. Niet elk geval is fout; een vooruitwijzing kan bewust zijn, mits ze
als zodanig is gemarkeerd.

| Begrip | Hoort in | Duikt op in | Opmerking |
|---|---|---|---|
| `while` | PGM1 week 4 | PGM1 week 2, `practicals/2_rochambeau` | Bewust; de tekst zegt erbij dat lussen later komen |
| list comprehension | PGM2 week 1 | PGM1 week 6, `practicals/6b_images` | Onderwerp van een hele PGM2-week |
| binair, talstelsel | PGM1 week 6 | PGM1 week 4, `problems/4_basis` | Opgave loopt twee weken voor op het college |
| 2D-lijst | PGM1 week 5 | PGM1 week 3, `problems/3_opstap` | Traversal vereist geneste lussen uit week 5 |
| functiedefinitie | PGM1 week 3 | PGM1 week 2, `problems/2_basis` | Mogelijk als gegeven voorbeeld |

Deze lijst is met tekstpatronen gemaakt en dus indicatief. Ze is het uitgangspunt
voor de controle die dit wil mechaniseren, niet het eindoordeel.

## Onderhoud

Verandert er iets aan de weekindeling of aan waar een begrip wordt
geïntroduceerd, werk dan dit document bij in dezelfde wijziging. Dit is de bron
waartegen coherentie over weken heen wordt getoetst; loopt hij achter, dan
controleert de toets niets meer.

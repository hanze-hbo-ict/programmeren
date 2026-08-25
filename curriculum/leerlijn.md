# Leerlijn

Wat er per week gebeurt, welke leeruitkomsten er landen, en welke begrippen er
voor het eerst worden geïntroduceerd.

Die laatste kolom is het dragende deel van dit document. Zolang vastligt waar een
begrip voor het eerst hoort, is een vooruitverwijzing te detecteren: materiaal
dat iets gebruikt wat volgens dit document later pas komt.

Voor PGM2 is de planning voor studiejaar 2026 leidend. Voor PGM1 liggen de
onderwerpen nog niet vast; wat hieronder staat is het huidige materiaal, gemeten
aan de inhoudsopgave en aan het eerste voorkomen van begrippen in de tekst.

Dit document is voor auteurs en docenten, niet voor studenten.

## Programmeren I

| Week | Onderwerp | Leeruitkomsten | Voor het eerst geïntroduceerd |
|---|---|---|---|
| 1 | Introductie, Picobot | - | toestandsmachine, regels, string, methode |
| 2 | Variabelen en condities | P1, P2, P3 | toekenning, variabele, operatoren, `if`, lijst, docstring, assertion |
| 3 | Functies | P5, A2 | functiedefinitie, parameter, zelfaanroep, 2D-lijst |
| 4 | Lussen | A1 | `for`, begrensde herhaling |
| 5 | Geneste lussen | A1, A3 | geneste lus, ASCII-art, bordrepresentatie |
| 6 | Data | P4 | binair, talstelsel, beeldbewerking |
| 7 | Meer data | P4, A3 | dictionary, bestanden lezen, Markov |

Recursie wordt in PGM1 niet onderwezen. Week 3 laat bij de functies alleen zien
dát een functie zichzelf kan aanroepen; het gedrag zelf komt in PGM2 aan bod. Dat
is zo bedoeld, maar leeruitkomst A4 staat er wel op. Zie het gat hieronder.

### Verdeling van het opgavemateriaal

Omvang in woorden per niveau, gemeten over `problems/` voor de weken 2 tot en met
7. Een ruwe maat, maar de verhoudingen zijn te groot om aan de meetmethode te
liggen.

| Week | opstap | basis | extra | Totaal |
|---|---|---|---|---|
| 2 | 1.145 | 1.089 | 463 | 2.697 |
| 3 | 242 | 389 | 176 | **807** |
| 4 | 616 | 1.034 | 1.048 | 2.698 |
| 5 | 238 | 1.865 | **5.265** | 7.368 |
| 6 | 372 | 1.067 | 1.162 | 2.601 |
| 7 | geen | 453 | **3.713** | 4.166 |
| **Totaal** | **2.613** | **5.897** | **11.827** | 20.337 |

Drie dingen vallen op.

**Het zwaartepunt ligt in de optionele laag.** Extra is 58% van het materiaal,
tweemaal zo groot als basis. Daar zitten Mandelbrot, Game of Life, Pi met
pijltjes en beeldcompressie: precies de opgaven waarin een probleem stap voor
stap wordt opgebouwd. Zie [uitgangspunten.md](uitgangspunten.md) voor de
achtergrond.

**Week 3 is de dunste week van de cursus.** Met 807 woorden is ze negen keer
kleiner dan week 5, terwijl ze functies draagt: P5 en A2, samen 20% van het
tentamen.

**De structuur is onvolledig.** Week 7 heeft geen opstap. In week 5 loopt de
nummering van opstap van 1 naar 5, 6, 7, 8: er is uit geknipt zonder te
hernummeren.

## Programmeren II

**De planning voor 2026 is leidend.** Wat het materiaal nu doet is de
uitgangssituatie, niet de norm; het verschil tussen beide kolommen is het werk.

| Week | Leidend voor 2026 | Verantwoordelijk | Materiaal nu |
|---|---|---|---|
| 1 | Datastructuren | BRRA | List comprehension |
| 2 | Comprehensions (list, dict, set, range, enumerate) | HOEM | Recursie |
| 3 | Recursie | HOEM | Algoritmen (knapzak, wisselgeld) |
| 4 | Use it or lose it, lambda | HOEM | Objecten en dictionaries |
| 5 | OO, klassen, encapsulatie | BRRA | Kunstmatige intelligentie |
| 6 | Polymorfisme, overerving, duck typing | BRRA | Vier op een rij, AI-speler |
| 7 | Operator overloading, oefentoets | BRRA | - |

Een deel van deze onderwerpen komt in het huidige materiaal niet of nauwelijks
voor. Dat is bekend en verwacht: de planning beschrijft waar PGM2 heen gaat, niet
waar het staat.

## Volgorde van het werk

**Eerst wordt PGM1 herzien, met de PGM2-lijn als randvoorwaarde.**

Dat betekent dat PGM1 niet op zichzelf ontworpen wordt: wat PGM2 in week 1
veronderstelt, moet PGM1 hebben geleverd. Bij elke keuze in PGM1 is de vraag dus
niet alleen of ze op zichzelf klopt, maar ook of ze de bovenstaande lijn
ondersteunt.

De onderwerpen voor PGM1 liggen nog niet vast; de tabel hierboven voor PGM1
beschrijft het huidige materiaal. Ze vaststellen is het eerste inhoudelijke werk,
en de twee gaten hieronder horen daarin te worden meegenomen.

## Gaten tussen toetsing en materiaal

Gemeten op het voorkomen van de betreffende constructies in `source/`.

| Leeruitkomst | Weging | Bevinding |
|---|---|---|
| **PGM2 P4** excepties | 10% | Twee bestanden. In `problems/5_basis` staat `try`/`except` in *gegeven* code van het menuprogramma, niet als uitleg. Nergens onderwezen. |
| **PGM2 P3** tekstbestanden | 10% | Drie plekken, waarvan twee in de Markov-opgave van PGM1 week 7. |
| **PGM1 A4** recursie | 10%, creëren | Wordt in PGM1 niet onderwezen; week 3 toont alleen de zelfaanroep. Het oefententamen toetst het ook niet. Voorstel: verplaatsen naar de PGM2-matrijs. |
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

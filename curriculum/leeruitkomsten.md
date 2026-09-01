# Leeruitkomsten en toetsmatrijs

De bindende laag: wat de student moet kunnen en hoe zwaar het meetelt in het
tentamen. Alle overige keuzes moeten hiermee te rijmen zijn.

Dit document is de kopie onder versiebeheer van de toetsmatrijzen die eerder
alleen in `ontwikkeling/` stonden, een directory die niet in git zit. Daardoor was het
bindende document niet gedeeld en niet gevolgd in de tijd.

> **Formele status.** Een toetsmatrijs wordt vastgesteld en is geen document dat
> je terloops bijwerkt. De correcties hieronder staan daarom als *voorstel*
> genoteerd, niet doorgevoerd.

## Programmeren I

### Competenties (HBO-i-model)

| Code | Omschrijving |
|---|---|
| **SOn1** | Maken van een ontwerp voor een softwaresysteem, inclusief database, met modelleertechnieken volgens een standaardmethode. |
| **SRe1** | Bouwen, testen en beschikbaar stellen van een eenvoudig softwaresysteem. Het opzetten, vullen en bevragen van een database maakt onderdeel uit van het softwaresysteem. |
| **OP-I** | Het identificeren van het probleem, richting van de oplossing bepalen en een passende aanpak kiezen. |
| **OP-II** | Gedurende het hele oplosproces nieuwsgierig zijn en vragen stellen vanuit verschillende perspectieven, deze vragen met een passende aanpak pragmatisch, kritisch en gebaseerd op bronnen beantwoorden. |

### Leeruitkomsten en weging

| Code | Omschrijving | Competentie | Niveau | Weging |
|---|---|---|---|---|
| **P1** | Student past toekenningen en variabelen toe. | SRe1 | Toepassen | 5% |
| **P2** | Student past rekenkundige en logische operatoren toe. | SRe1 | Toepassen | 10% |
| **P3** | Student past conditionele statements toe. | SRe1 | Toepassen | 10% |
| **P4** | Student past lijsten en strings en de bijbehorende methodes toe. | SRe1 | Toepassen | 10% |
| **P5** | Student definieert functies met positionele parameters en past ze toe. | SRe1 | Toepassen | 10% |
| **P6** | Student past assertions toe om fouten in functies op te sporen. | SRe1 | Toepassen | 10% |
| **P7** | Student past docstrings toe om functies te documenteren. | SRe1 | - | **geen** |
| **A1** | Student implementeert eenvoudige algoritmes door middel van functioneel programmeren. | SRe1 | Toepassen | 15% |
| **A2** | Student verdeelt eenvoudige computationele problemen in kleinere deelproblemen. | SRe1 | Toepassen | 10% |
| **A3** | Student ontwerpt algoritmes om eenvoudige computationele problemen op te lossen. | OP-I | Analyseren | 10% |

Totaal: 80% toepassen, 10% analyseren. **Samen 90%**; de 10% die met de
verplaatsing van A4 vrijkwam is nog niet herverdeeld, en PGM1 heeft daarmee geen
uitkomst op creëren-niveau. Zie *Voorgestelde correcties*.

> De eerder vermelde verdeling "70% toepassen" klopte niet met de som van de rijen,
> ook vóór deze wijziging niet.

## Hoe de percentages zich tot de toets verhouden

De matrijzen hierboven sluiten op 100%, en beide oefententamens tellen 90 punten.
Dat is geen fout. Het cijfer wordt zo berekend:

$$
\text{cijfer} = 9 \times \frac{\text{behaalde punten}}{\text{totaal aantal punten}} + 1
$$

waarbij het totaal 90 is. De **+1** is de basis: een student die niets goed heeft
haalt een 1 en geen 0. Wie alle 90 punten haalt komt op een 10 uit.

Die basis wordt niet over de leeruitkomsten verdeeld. De percentages van de matrijs
gaan dus over de negentig punten die te verdienen zijn, en een uitkomst van 10% komt
overeen met 9 punten op de toets.

Dit staat hier omdat het uit de repository niet af te leiden is. Een veegronde die
de punten in het oefententamen telt, komt op 90 uit en concludeert dan dat er iets
niet klopt; dat is precies wat er op 31 augustus 2026 gebeurde. Vastgesteld door de
vakdeskundige.

## Programmeren II

### Competenties (HBO-i-model)

| Code | Omschrijving |
|---|---|
| **SOn1** | Maken van een ontwerp voor een softwaresysteem, inclusief database, met modelleertechnieken volgens een standaardmethode. |
| **SRe1** | Bouwen, testen en beschikbaar stellen van een eenvoudig softwaresysteem. Het opzetten, vullen en bevragen van een database maakt onderdeel uit van het softwaresysteem. |
| **OP-II** | Het identificeren van het probleem, richting van de oplossing bepalen en een passende aanpak kiezen. |
| **OP-III** | Gedurende het hele oplosproces nieuwsgierig zijn en vragen stellen vanuit verschillende perspectieven, deze vragen met een passende aanpak pragmatisch, kritisch en gebaseerd op bronnen beantwoorden. |

### Leeruitkomsten en weging

| Code | Omschrijving | Competentie | Niveau | Weging |
|---|---|---|---|---|
| **P1** | Student past begrensde en onbegrensde lusconstructies toe. | SRe1 | Toepassen | 5% |
| **P2** | Student past dictionaries en de bijbehorende methodes toe. | SRe1 | Toepassen | 10% |
| **P3** | Student leest en schrijft tekstbestanden met behulp van de bestandsinvoer- en -uitvoerfuncties. | SRe1 | Toepassen | 10% |
| **P4** | Student past excepties toe om foutcondities af te handelen. | SRe1 | Toepassen | 10% |
| **P5** | Student past objecten en klassen toe. | SRe1 | Toepassen | 10% |
| **P6** | Student gebruikt magische methodes om operatoren te overloaden. | SRe1 | - | **geen** |
| **P7** | Student gebruikt externe bibliotheken. | SRe1 | - | **geen** |
| **A1** | Student implementeert eenvoudige algoritmes door middel van imperatief programmeren. | SRe1 | Toepassen | 15% |
| **A2** | Student implementeert eenvoudige algoritmes door middel van object-georiënteerd programmeren. | SRe1 | Toepassen | 10% |
| **A3** | Student implementeert complexere applicaties, gebruikmakend van functioneel, imperatief en object-georiënteerd programmeren. | SRe1 | Creëren | 10% |
| **A4** | Student ontwerpt algoritmes om complexere computationele problemen op te lossen. | SOn1, OP-III | Creëren | 10% |
| **A5** | Student ontwerpt finite state machines voor eenvoudige talen. | SOn1 | - | **geen** |
| **A6** | Student ontwerpt en past eenvoudige recursieve oplossingen toe. | SOn1 | Creëren | 10% |

Totaal: 70% toepassen, 30% creëren. Samen 100%.

> A6 is per 1 september 2026 overgekomen uit de PGM1-matrijs; recursie wordt sinds
> het besluit "recursie na de lussen" in PGM2 week 3 onderwezen en in het
> PGM2-tentamen getoetst, met 30 van de 90 punten. De uitkomst heeft het nummer
> A6 gekregen omdat A4 en A5 al bezet zijn; hernummeren zou verwijzingen elders
> breken. De eerder vermelde verdeling "80% toepassen, 20% creëren" telde op tot
> 90% en klopte niet met de som van de rijen.

## Voorgestelde correcties

Vier leeruitkomsten hebben geen weging in het tentamen. Dat hoeft geen fout te
zijn, maar het verdient per geval een besluit, want een leeruitkomst zonder
toetsing is een belofte die niemand nakijkt.

| Uitkomst | Bevinding | Voorstel |
|---|---|---|
| **PGM2 A5** (finite state machines) | Niet onderwezen, niet getoetst, en de bijbehorende theoretische afsluiting is bewust losgelaten. Zie [uitgangspunten.md](uitgangspunten.md). | **Schrappen.** |
| **PGM1 P7** (docstrings) | Wél onderwezen en overal in het materiaal toegepast, maar niet getoetst. | Weging geven of expliciet als vormeis opnemen. |
| **PGM2 P6** (operator overloading) | Wél onderwezen, en in de planning voor 2026 krijgt het een hele week. | Weging geven, of de week heroverwegen. |
| **PGM2 P7** (externe bibliotheken) | Verspreid aanwezig, niet als onderwerp behandeld. | Besluiten of dit een leeruitkomst moet blijven. |
| **PGM1: 10% onverdeeld, en geen creëren-niveau** | Met het vertrek van A4 telt de PGM1-matrijs 90% en heeft het vak geen enkele uitkomst op creëren-niveau meer. Dat laatste is niet vanzelf een gebrek - PGM1 is een introductievak - maar het is wel een keuze die niemand expliciet heeft gemaakt. De veegronde stelde bovendien vast dat het oefententamen 40 van de 90 punten aan ontwerpwerk besteedt, tegen 10% analyseren in de matrijs. | Herverdelen binnen PGM1. De meting wijst richting A3 (ontwerpen, analyseren), dat nu 10% weegt terwijl de toets er aanzienlijk meer aan besteedt. |
| **PGM1 P4** (lijsten/strings en de bijbehorende methodes) | Het methodes-deel wordt al jaren niet meer in PGM1 onderwezen of getoetst. Vanaf de herziening van PGM1 week 7 en PGM2 week 1 introduceert PGM1 geen objectmethoden meer; dat verschuift volledig naar PGM2 week 1. Zie [leerlijn.md](leerlijn.md) en [uitgangspunten.md](uitgangspunten.md). | Herformuleren tot wat lijsten/strings betreft zonder de methodes, of het methodes-deel schrappen. |

Daarnaast staat één uitkomst in de verkeerde matrijs:

| Uitkomst | Bevinding | Voorstel |
|---|---|---|
| ~~**PGM1 A4** (recursie)~~ | **Uitgevoerd op 1 september 2026.** De uitkomst staat nu als **PGM2 A6**. Zij stond op creëren-niveau voor 10% van het PGM1-tentamen terwijl recursie in PGM1 niet wordt onderwezen; het PGM2-tentamen besteedt er 30 van de 90 punten aan. PGM2 telde vóór de verplaatsing 90% en komt er nu mee op 100% uit. | Gedaan. Wat resteert: de 10% die in PGM1 vrijkomt, zie de rij hieronder. |

## Gaten tussen toetsing en onderwijs

Twee leeruitkomsten die samen 20% van het PGM2-tentamen zijn, worden in het
materiaal nauwelijks behandeld. Zie [leerlijn.md](leerlijn.md) voor de meting.

| Uitkomst | Weging | Aanwezig in het materiaal |
|---|---|---|
| **PGM2 P3** (tekstbestanden) | 10% | Drie plekken, vrijwel alle in PGM1 week 7 |
| **PGM2 P4** (excepties) | 10% | Twee plekken, en uitsluitend als gegeven code |

Beide zijn kandidaat om in PGM1 te worden geïntroduceerd; bestandsinvoer sluit
daar al aan op de Markov-opgave in week 7.

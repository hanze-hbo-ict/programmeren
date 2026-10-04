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
| **A3** | Student ontwerpt algoritmes om eenvoudige computationele problemen op te lossen. | OP-I | Analyseren | 20% |

Totaal: 80% toepassen, 20% analyseren. **Samen 100%.** PGM1 heeft geen uitkomst
op creëren-niveau; dat is een besluit en geen gat. Zie
[uitgangspunten.md](uitgangspunten.md), *De weging van de PGM1-matrijs*, voor
beide besluiten en voor de meting waarop ze rusten.

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
toetsing is een belofte die niemand nakijkt. Zij staan in de eerste vier rijen;
daaronder volgen de overige bevindingen over de matrijs: formuleringen en
plaatsingen die niet meer beschrijven wat de vakken doen, en wat inmiddels is
uitgevoerd.

| Uitkomst | Bevinding | Voorstel |
|---|---|---|
| **PGM2 A5** (finite state machines) | Niet onderwezen, niet getoetst, en de bijbehorende theoretische afsluiting is bewust losgelaten. Zie [uitgangspunten.md](uitgangspunten.md), *De theoretische afsluiting*. | **Schrappen.** |
| **PGM1 P7** (docstrings) | Wél onderwezen en overal in het materiaal toegepast, maar niet getoetst. | Weging geven of expliciet als vormeis opnemen. |
| **PGM2 P6** (operator overloading) | Wél onderwezen, en in de planning voor 2026 krijgt het een hele week. | Weging geven, of de week heroverwegen. |
| **PGM2 P7** (externe bibliotheken) | Verspreid aanwezig, niet als onderwerp behandeld. | Besluiten of dit een leeruitkomst moet blijven. |
| ~~**PGM1: de weging van de matrijs**~~ | **Uitgevoerd op 4 oktober 2026.** Het gewicht dat A4 achterliet is aan A3 toegekend: A3 weegt 20% en de matrijs sluit op 100%. Dat PGM1 geen uitkomst op creëren-niveau heeft, is daarbij als keuze vastgelegd en niet als restant. De grond, de niveaumeting van het oefententamen en wat beide besluiten zou heropenen staan in [uitgangspunten.md](uitgangspunten.md), *De weging van de PGM1-matrijs*. | Gedaan. |
| **PGM1 P4** (lijsten/strings en de bijbehorende methodes) | Het methodes-deel wordt al jaren niet meer in PGM1 onderwezen of getoetst. Vanaf de herziening van PGM1 week 7 en PGM2 week 1 introduceert PGM1 geen objectmethoden meer; dat verschuift volledig naar PGM2 week 1. Zie [leerlijn.md](leerlijn.md) en [uitgangspunten.md](uitgangspunten.md). | Herformuleren tot wat lijsten/strings betreft zonder de methodes, of het methodes-deel schrappen. |
| **PGM1 A1** (*functioneel*) en **PGM2 A1** (*imperatief*) | De twee A1's gaan nog uit van de oorspronkelijke indeling van PGM1 en PGM2. Recursie, en daarmee het functionele deel, zit al een paar jaar in PGM2, en `for` en `while` zijn naar PGM1 verplaatst. De comprehensionweek, PGM2 week 2, dekt daardoor feitelijk PGM1 A1, terwijl `leerlijn.md` haar onder PGM2 A1 zet. Opgemerkt door de vakdeskundige op 30 september 2026, bij de poort van #326 (VP3); de matrijs is daarbij niet aangepast. | De leeruitkomsten van PGM1 en PGM2 een keer doorlichten; zie #329. Tot dan houdt PGM2 week 2 in `leerlijn.md` A1, met een verwijzing naar deze opmerking. |
| **PGM2 P1** (lussen) | PGM1 toetst lussen voor 20 van de 90 punten (opgave 4 en 5) en onderwijst ze in week 4 en 5, terwijl de lusuitkomst als PGM2 P1 voor 5% in de andere matrijs staat en in geen enkele PGM2-week voorkomt; `leerlijn.md` zet dat gat op "open". Dit is het spiegelbeeld van de A4-verplaatsing, en het raakt dezelfde A1-formulering als de rij hierboven. Gemeten bij #104. | Meenemen in de doorlichting van #329, samen met de rij hierboven. |
| **PGM1 week 6** (bestanden) | Week 6 noemt in `leerlijn.md` geen PGM1-uitkomst maar "bestanden", met een voetnoot naar de PGM2-matrijs. Bestanden worden in week 6 wel onderwezen en in PGM1 niet getoetst; de uitkomst is PGM2 P3. Eén van de zeven PGM1-weken draagt daarmee geen uitkomst van de matrijs die het eigen tentamen beschrijft. Gemeten bij #104. | Meenemen in de doorlichting van #329. |
| **PGM2 P7** (externe bibliotheken) in `leerlijn.md` | Vier PGM2-uitkomsten komen in geen enkele week voor. Voor P1, P3 en A5 staat de grond in *Gaten tussen toetsing en materiaal* in [leerlijn.md](leerlijn.md), voor P7 niet; de bevinding over P7 hierboven is daar dus niet terug te vinden. Gemeten bij #104. | Meenemen in de doorlichting van #329. |

Daarnaast staat één uitkomst in de verkeerde matrijs:

| Uitkomst | Bevinding | Voorstel |
|---|---|---|
| ~~**PGM1 A4** (recursie)~~ | **Uitgevoerd op 1 september 2026.** De uitkomst staat nu als **PGM2 A6**. Zij stond op creëren-niveau voor 10% van het PGM1-tentamen terwijl recursie in PGM1 niet wordt onderwezen; het PGM2-tentamen besteedt er 30 van de 90 punten aan. PGM2 telde vóór de verplaatsing 90% en komt er nu mee op 100% uit. | Gedaan. Het gewicht dat in PGM1 achterbleef is op 4 oktober 2026 aan A3 toegekend; zie de rij over de weging van de matrijs hierboven. |

## Gaten tussen toetsing en onderwijs

Twee leeruitkomsten die samen 20% van het PGM2-tentamen zijn, worden in het
materiaal nauwelijks behandeld. Zie [leerlijn.md](leerlijn.md) voor de meting.

| Uitkomst | Weging | Aanwezig in het materiaal |
|---|---|---|
| **PGM2 P3** (tekstbestanden) | 10% | Drie plekken, vrijwel alle in PGM1 week 7 |
| **PGM2 P4** (excepties) | 10% | Twee plekken, en uitsluitend als gegeven code |

Tekstbestanden gaan naar PGM1 week 6; excepties blijven in PGM2 en landen daar in
week 7. Zie [uitgangspunten.md](uitgangspunten.md), *Bestanden en excepties*.
Hier stond eerder dat beide kandidaat waren voor PGM1; dat liep achter op dat
besluit.

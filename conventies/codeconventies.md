# Codeconventies

Dit document gaat over de Python in het materiaal: voorbeelden, startcode,
opgaven en uitwerkingen. Het beschrijft welke taal we gebruiken, hoe we namen
kiezen en wat een docstring of een test moet doen.

De opmaak van code (`ruff format`) en hoe die wordt afgedwongen, staat in
[technische-conventies.md](technische-conventies.md). Hier gaat het over de
inhoud van de code, niet over de witruimte.

Dit document is voor auteurs, niet voor studenten. Het staat bewust buiten
`source/` en maakt geen deel uit van het boek.

## Taal

### Namen zijn Engels, vanaf week 1

Functienamen en de parameters die bij een opdracht horen, zijn Engels. Dat is geen
wens maar vrijwel een vaststelling: een scan over alle functiedefinities in
`source/` telt 295 unieke functienamen, en daarvan zijn er drie niet Engels.
`midden_van` staat in `lectures/7a_lists_advanced` en in `solutions/7_opstap`, en de
opgave `problems/7_opstap` vraagt die naam met zoveel woorden. `generaties` staat in
`problems/7_basis` en `solutions/7_basis`. `alfabet_word` staat in
`solutions/PGM2_examen`, een van de vier oefententamens die bij besluit bevroren
zijn. Hier stond dat alle functienamen het al waren en dat `s_afwijking` in
`solutions/5_basis` tot de herziening van week 5 de enige uitzondering was; die heet
inderdaad `std_dev`, maar de drie hierboven staan er nog.

Daar zijn goede redenen voor. De naam van een functie *is* de opdracht:
`flipside`, `count_vowels` en `num_to_base_b` staan in de opgavetekst en worden
door de nakijkomgeving getoetst. Vertalen zou de opgave veranderen. Bovendien is
die woordenschat dezelfde als die van Python zelf; `list`, `count` en `string`
leert de student toch al.

### Docstrings en commentaar: Nederlands, in beide vakken

Docstrings en commentaar zijn Nederlands, in PGM1 en in PGM2. Er is geen moment
waarna het materiaal overstapt op Engels. Wie voor het eerst programmeert, heeft
genoeg te verwerken zonder dat de uitleg ook nog in een vreemde taal staat, en
dat houdt in PGM2 niet op.

Hier stond eerder een langzame onderdompeling: eerst Nederlands, en na een
expliciet overgangsmoment Engels. Voor dat moment waren twee kandidaten genoemd,
het begin van PGM2 en de eerste klasse van formaat, maar er was er nooit een
gekozen. Bij de voorbereiding van de poort van #160, de week waarin die klasse
landt, is besloten dat er geen overgang komt. Vastgesteld door de vakdeskundige
op 23 september 2026.

De uitzondering hieronder blijft staan.

### Gedeelde bestanden zijn Engels

Bestanden die vanuit beide studiejaren worden gebruikt, zoals
`board.py` (sinds #271 buiten `source/`, in `practicals/assets/`), `practicals/assets/file_and_dictionary_examples.py`
en `lectures/assets/markov.py`, kunnen niet twee talen tegelijk hebben. Die zijn
Engels. Dat is een bewuste uitzondering, geen slordigheid.

## Naamgeving

### De regel: de naam groeit mee met de scope

Een korte naam mag wanneer je de hele scope in één blik overziet en het type de
betekenis draagt. Zodra de scope groeit, groeit de naam mee.

Dit is de vakregel, en het materiaal past haar al toe. Gemeten over de
oorspronkelijke CS5-code, parameternamen tegen functiegrootte:

| functiegrootte | korte naam | beschrijvende naam |
|---|---|---|
| tot 5 regels | 70% | 29% |
| 6 tot 15 regels | 58% | 41% |
| meer dan 15 regels | 34% | 65% |

Die gradiënt is de conventie. We leggen haar vast, we bedenken haar niet.

Een prettig gevolg: er is geen aparte regel per studiejaar nodig. Functies
groeien vanzelf door de cursus heen, dus dezelfde regel levert korte namen op in
week 2 en uitgeschreven namen in week 11.

### Het typewoordenboek

Waar een korte naam past, gebruiken we deze. Ze zijn in het materiaal vrijwel
volledig consistent: `s` is in alle 16 gemeten toekenningen een string, `L` in
alle 15 een lijst, `d` in alle 8 een dictionary.

| Naam | Betekenis |
|---|---|
| `s` | string |
| `L` | lijst |
| `d` | dictionary |
| `n` | aantal of grootte |
| `i`, `j`, `k` | lusindex; zie de scoperegel hieronder |
| `x`, `y` | getal of coördinaat; generiek, niet typegebonden |
| `b`, `p` | grondtal en exponent, waar de formule ze zo noemt |
| `_` | bewust ongebruikt |

Samenstellingen volgen hetzelfde idee: `LoL` voor een lijst van lijsten, `LoW`
voor een lijst van woorden.

### Wanneer een korte index, en wanneer een naam die de les draagt

Of een lusvariabele `i` heet of `row`, hangt niet af van de vorm van de lus maar
van wat de variabele betekent. Er zijn drie gevallen, en ze sluiten elkaar uit.

| De variabele | Dan | Zoals |
|---|---|---|
| wijst alleen een plek aan, en de les heeft er geen eigen woord voor | een korte index | `for i in range(len(L))` met `L[i]` |
| wijst iets aan dat de les wél bij naam noemt | die naam | `for row` en `for col`; `first` en `rest` |
| wordt niet gelezen | `_` | besluit VP7, zie hieronder |

**Een korte index** past waar de variabele alleen een plek aanwijst en de les
daar geen eigen woord voor heeft. Dat geldt ook voor een geneste lus, zolang de
twee variabelen geen rij en geen kolom zijn: `min_diff` in
`lectures/5a_geneste_lus.ipynb` loopt over paren uit één lijst, en daar zijn het
twee posities. Dat die twee in dat college `ix1` en `ix2` heten, is de
naamafwijking bij *index* uit *Huidige staat* hieronder; die wordt per bestand
rechtgezet. Het geval zelf is een korte index.

**Een naam die de les draagt** hoort waar de variabele het ding aanwijst dat de
les bij naam noemt. Het materiaal kent er twee.

Bij een geneste lus over een raster zijn dat `row` en `col`. In de les wordt
gehamerd op denken in rijen, en in de kolommen binnen een rij. Die twee namen
wijzen daar rechtstreeks naar, en de berekening eromheen wordt er leesbaar van:
`width - row` zegt wat het is, en `width - i` in `solutions/5a_ascii_art.ipynb`
zegt dat niet.

Gemeten over de code in `source/`: van de 83 geneste lussen heeft de buitenste
lus 19× `row` (met `col` als binnenste, 17×), 19× `i` (met `j`), 11× `ix1` (met
`ix2`), 5× `regel` en 4× `col`. De `i`-vorm staat in vijf bestanden, de andere
buitenste namen samen in 27. Zwaarder dan die verhouding weegt waar ze staan:
het college dat dit onderwerp onderwijst, `lectures/5a_geneste_lus.ipynb`,
gebruikt in zijn zeven geneste lussen geen `i`, terwijl de uitwerking van
dezelfde week, `solutions/5a_ascii_art.ipynb`, dat in zeven van haar acht wel
doet. De les en haar eigen uitwerking spraken elkaar tegen; deze regel kiest de
kant van de les. Methode: elke `for`-regel met binnen haar blok een dieper
ingesprongen `for`-regel, per codecel of fence geteld en nooit over een
celgrens heen.

Bij recursie zijn dat `first` en `rest`: het geval dat je zelf afhandelt, en de
rest die je aan de recursie overlaat. Dat is het mantra van de recursieweken,
letterlijk in de namen.

**De toets** is of het proza de naam moet terugvertalen. Moet het dat, dan
draagt de naam zijn betekenis niet. `solutions/5a_ascii_art.ipynb` schrijft in
`print_triangle` `for i in range(0, width)` met daarbinnen
`for j in range(0, i + 1)`, en de markdowncel direct erna moet beide namen
terugvertalen: "het regelnummer is gelijk aan het aantal symbolen" voor `i`, en
"de eerste `j`-lus (de kolomlus)" voor `j`. Het proza levert daar de woorden
*regel* en *kolom* die de namen zelf niet dragen. Dat is het signaal.

**Wordt de variabele niet gelezen, dan is er niets te kiezen.** Dan heet zij
`_`, ook in een comprehension. Dat is besluit VP7, vastgelegd in
[`curriculum/leerlijn.md`](../curriculum/leerlijn.md) r676, en het staat
hierboven in het typewoordenboek als "bewust ongebruikt". Deze regel gaat over
de lusvariabele die wél gelezen wordt: `for row in range(height)` zonder dat
`row` ergens gelezen wordt, valt onder VP7 en niet hieronder. Over VP7 legt deze
regel niets nieuws vast.

**De code in de recursieweken houdt `first` en `rest`.** Het mantra "jij bent
verantwoordelijk voor het eerste geval, de recursie voor de rest" blijft in het
proza, waar het leeft; `mine` komt niet in de code. De grond is dat er voldoende
afstand zit tussen de onderwerpen en hun opgaven. Dat is ook de reden
om `other` niet aan *de rest* te binden: in `source/` is `other` de andere
operand, in 17 signaturen van operatormethoden (`__eq__` 7×, `__lt__` 7×,
`__gt__` 2× en `__sub__` 1×) verdeeld over zes bestanden, en dat is de
Python-conventie en niet onze keuze. Besloten door de vakdeskundige bij de poort
van #368.

**Dat `rest` twee dingen betekent, blijft zo, en dat is een keuze.** Van de
zestien toekenningen aan `rest` in de code zijn er zes de resterende lijst —
zoals `rest = items[1:]` naast `first = items[0]`, alle in PGM2 week 4 — en
zeven de uitkomst van de recursieve aanroep, zoals `rest = fac(n - 1)` en
`rest = largest(L[1:])` in PGM2 week 3. Twee zijn een placeholder in
`lectures/10b_recursief_ontwerpen`, en één, `rest = both - klauw` in
`practicals/14_creatures.md`, staat er los van. Tussen die twee onderwerpen en
hun opgaven zit voldoende afstand, dus één naam voor twee betekenissen hindert
de student hier niet. Daarom bindt deze regel aan de betekenis en niet aan de
naam. Dit is geen bekende afwijking die op een opruimactie wacht: het is een
verschil met een grond. Besloten door de vakdeskundige bij de poort van #368.

De tellingen bij recursie, over heel `source/`: `first` 29× in code en 6× in
proza, `rest` 51× in code en 83× in proza. Over de 32 bestanden van PGM2 week 3
en 4 alleen: `first` 20× en 5×, `rest` 44× en 52×. `mine` komt in `source/` nul
keer voor, in code noch in proza. `other` komt in die 32 bestanden nul keer voor
en in de rest van `source/` 81× in code en 47× in proza.

> **Let op de meting.** Een eerdere telling gaf voor `rest` 59 in code en 74 in
> proza, samen 133. Het totaal komt vrijwel uit — hier 134, één verschil — maar
> de splitsing niet, en latere tellingen gaven telkens een andere verdeling. Wat
> schuift is de grens tussen code en proza, niet het aantal vindplaatsen.
>
> De grens die hierboven is gebruikt, gemeten op commit `f3db28e6`. Het corpus
> is alle 228 `.ipynb`-, `.md`- en `.py`-bestanden onder `source/`. *Code* is de
> codecellen van notebooks, de ` ```python `-fences in markdown — zowel in
> `.md`-bestanden als in markdowncellen — en de hele inhoud van een
> `.py`-bestand. *Proza* is al het overige in markdown: de gewone tekst, de
> fence-regels zelf, de inline code-spans, en elk blok met een andere
> infostring. Celuitvoer, celmetadata en de JSON-structuur van een notebook doen
> niet mee. Geteld met een woordgrens om het hele woord, in kleine letters.
> PGM2 week 3 en 4 zijn de bestanden waarvan de naam begint met `10` of `11`,
> plus `opgaven_`, `practical_`, `solutions_` en `week_` met 10 of 11 erachter.
>
> Aan één beslissing hangt dit getal. Het corpus heeft 32 ` ```ipython `-fences,
> sessietranscripten met uitvoer erin, en die gelden hier als proza. In
> `projects/picobot.md` staat binnen zo'n transcript de regel "... rest van het
> programma overgeslagen ...". Reken je `ipython` als code, dan leest `rest` 52
> en 82 in plaats van 51 en 83; op elk ander getal hierboven maakt het geen
> verschil. Wie dit hermeet, ijkt zijn patroon eerst op een bekend getal.
> *Objectmethoden pas vanaf PGM2 week 1* hieronder geeft er twee, met de commit
> waaraan ze hangen.

**Binnen één bestand is de keuze overal dezelfde**, en binnen één week ook. Dat
is dezelfde eis als bij de twee naamgevingssystemen hieronder: welke naam wint
mag per bestand verschillen, maar niet per lus.

Deze regel is niet bedacht. Het college dat geneste lussen onderwijst, maakt het
onderscheid al binnen één bestand: een korte index in `compute_sum` en in
`min_diff`, en `row` en `col` in `print_board`. We schrijven het alleen op.

### Wat niet mag

- **Nooit de kleine letter `l`.** Die is in veel lettertypen niet te
  onderscheiden van `1` of `I`, en linters merken hem aan als ambigu. Precies
  daarom koos CS5 de hoofdletter. In `source/` komt de naam niet meer voor.

  > **Let op de meting.** Hier stond dat het materiaal er nog 48 bevatte. Bij de
  > herziening van week 3 is dat nagemeten en niet te reproduceren: geteld als
  > `NAME`-token in de codecellen en de ` ```python `-blokken van `source/`
  > waren het er **acht**, alle acht in de twee colleges van week 3, en die zijn
  > met die herziening verdwenen. Welk patroon of welk corpus tot 48 leidde is
  > niet te achterhalen. Wie dit hermeet, ijkt zijn patroon eerst op een bekend
  > getal.
- **Geen fantasienamen.** Een naam die niets betekent, leert de student iets
  verkeerds op de plek waar hij naamgeving voorgedaan krijgt. Voor voorbeelden
  waarin de naam er juist *niet* toe doet, is `function` of `f` de gangbare
  keuze, en die staat al in het materiaal. Tot de herziening van week 3 stond er
  een functie `blaat` in het college over functies aanroepen; die heet nu
  `triangle` en rekent iets uit.
- **Niet `string` als variabelenaam.** Het materiaal leert de student
  `import string` te gebruiken voor `string.punctuation`. Een variabele met
  dezelfde naam overschaduwt die module. Gebruik `s` waar de scope kort is en
  `text` waar hij dat niet is; `markov.py` doet dat al.

### Huidige staat

Het materiaal bevat op dit moment twee naamgevingssystemen naast elkaar. PR #71
verving een deel van de korte namen door beschrijvende, en deed dat niet overal
en niet met één naam per begrip: `L` werd op verschillende plekken `lst`,
`my_list` en `numbers_lst`.

| begrip | namen in gebruik |
|---|---|
| lijst | `L` 214× · `lst` 143× · `my_list` 54× · `numbers_lst` 14× |
| string | `s` 361× · `string` 142× · `text` 30× |
| 2D-array | `a` 323× · `array` 143× |
| karakter | `c` 138× · `char` 49× · `ch` 16× |
| dictionary | `d` 61× · `words_follow` 21× · `word_count` 18× |
| index | `i` 107× · `ix` 75× |

Dit wordt niet in een aparte opruimactie rechtgezet, maar per bestand tijdens de
inhoudelijke herziening. De regel hierboven beslist dan welke naam wint: in een
functie van drie regels de korte, in een functie van dertig de uitgeschreven.
Binnen één bestand is de keuze wel overal dezelfde.

## Objectmethoden pas vanaf PGM2 week 1

Een methode is een handeling die bij een object hoort. Een student die
`L.append(x)` schrijft voordat hij weet wat een object is, gebruikt dat begrip
zonder het te hebben.

**In heel PGM1 gebruikt het materiaal functies en operatoren, geen
methoden:**

| Niet vóór PGM2 week 1 | Wel |
|---|---|
| `L.append(x)` | `L[i] = x`, of `L = L + [x]` |
| `s.isdigit()` | `from string import digits`, en dan `c in digits` |

**Vanaf PGM2 week 1 mogen methoden.** Die grens valt niet meer samen met de
mutatiegrens: PGM1 week 7 laat mutatie zien via `L[i] = x`, wat geen
methodeaanroep vraagt. Methodeaanroep zelf wordt voor het eerst
geïntroduceerd in PGM2 week 1, samen met dictionaries en sets. Zie
[`curriculum/uitgangspunten.md`](../curriculum/uitgangspunten.md) en
[`curriculum/leerlijn.md`](../curriculum/leerlijn.md).

Leeruitkomst **P4** vroeg lange tijd letterlijk om "lijsten en strings en de
bijbehorende methodes" in PGM1, maar wordt daar al jaren niet meer op
getoetst. Dat staat als voorgestelde correctie in
[`curriculum/leeruitkomsten.md`](../curriculum/leeruitkomsten.md#voorgestelde-correcties).

**Het materiaal volgt deze regel nog niet.** `problems/5_extra.md` (PGM1 week 5,
laag extra) introduceert methode, object én tuple vóór PGM2 week 1, via
`image.plot_point(...)` en `image.save_file()`. Dat is bekend en hoort te
worden rechtgezet bij de herziening van PGM1 week 7 (issue #102) — het is nu
nog geen conventie die te handhaven is.

**Week 7 volgt de regel inmiddels wel.** Hier stond dat
`lectures/7a_lists_advanced.ipynb` `.append()` vier keer expliciet als methode
introduceert, plus één keer in `problems/7_opstap.ipynb`. Commit `92df099e`, de
herziening van week 7, heeft die vijf vindplaatsen verwijderd. In de vier
week-7-bronnen (`7a_lists_advanced`, `7_opstap`, `7_basis` en `7_extra`) staat
`.append(` nu nul keer, geijkt op `lectures/8a_datastructuren.ipynb`, dat er zes
heeft.

:::{note}
Het woord *methode* komt in week 1 wel voor, in `lectures/1a_intro_programmeren`,
maar in de gewone Nederlandse betekenis: "een methode verzinnen om getallen te
sorteren". Dat is geen vooruitverwijzing en hoeft niet weg.
:::

## Docstrings

Elke functie die de student schrijft of leest, heeft een docstring. Dat is een
van de weinige gewoonten die het materiaal expliciet wil aanleren, en het
materiaal moet die dus zelf voordoen.

- **Eén regel** voor een functie die met één zin te beschrijven is. Dit is de
  hoofdvorm: 168 van de 290 docstrings in het materiaal.
- **Meer regels** waar het iets toevoegt: wat de argumenten zijn, wat er
  teruggegeven wordt, en welke aannames gelden.
- **Beschrijf wat de functie doet, niet hoe.** De code zegt hoe.
- De taal volgt de afspraak hierboven: Nederlands, behalve in de gedeelde
  bestanden.

**De maatstaf voor de student is de lezer, niet een stijl.** Er bestaan meerdere
docstringconventies naast elkaar, waaronder PEP 257, en wij schrijven er geen voor.
Wat de student schrijft is goed als iemand anders er genoeg aan heeft om de functie
te gebruiken zonder de code te lezen. Beoordeel daarop, en niet op de vorm.

Voor het materiaal zelf ligt dat anders: daar geldt de vorm hierboven wél, omdat het
materiaal voordoet wat het aanleert. Een cursus die vijf docstringstijlen laat zien,
leert de student dat het niet uitmaakt hoe je het opschrijft, terwijl de boodschap
juist is dat het uitmaakt wat je opschrijft.

**De reST-velden `:param:`, `:type:`, `:rtype:` en `:return:` vervallen.** Vastgesteld
door de vakdeskundige op 10 september 2026. Dat is de Sphinx-stijl, bedoeld om
documentatie uit code te genereren - iets wat deze cursus niet doet en wat de student
niet leert. Zij dwingt bovendien een lange vorm af waar één regel volstaat, en dat
botst met de hoofdvorm hierboven: het practicum van week 3 eiste met zoveel woorden dat
een docstring de argumenten én de returnwaarde beschrijft, waarmee de eenregelige
docstring in `lectures/3b_functies_aanroepen.md` fout zou zijn. Dat is zij niet.

Het staan er nu **93**, verdeeld over zes bestanden, met het zwaartepunt in
`solutions/6_basis` (30), `7_basis` (18), `8_basis` (18) en `8_extra` (16). Het waren
er 149 in tien bestanden; de 56 van week 3 zijn met de herziening van die week
verdwenen. Ze worden niet in één opruimactie weggewerkt maar per week, met de
herziening van die week mee. Tot dan is dit een bekende afwijking; wat er nieuw bij
komt, draagt de hoofdvorm.

Docstrings komen bovendien pas in week 3 aan de orde als begrip; in week 2 ziet de
student ze al staan in gegeven code. Zie *Onderdompeling gaat vooraf aan uitleg* in
[`../curriculum/uitgangspunten.md`](../curriculum/uitgangspunten.md).

**Uitzondering: code in een leesvraag draagt geen docstring.** Bij een vraag van
het type *"wat drukt dit programma af?"* is een docstring die beschrijft wat de
functie doet het antwoord, en dan toetst de vraag niets meer. Dit geldt voor de
oefenmidterms en voor de leesopdrachten in de opstap en de colleges - overal waar
de student de code moet lezen in plaats van gebruiken. Vastgesteld bij de poort
van #146; zie *Leesvragen mogen fout aflopen* in
[`../curriculum/uitgangspunten.md`](../curriculum/uitgangspunten.md).

De plicht geldt onverkort voor alles wat de student als voorbeeld of uitwerking
krijgt om ván te leren.

## Assertions

Opgaven worden getest met `assert`. Dat is de standaardvorm in dit materiaal:
144 codeblokken bevatten er een, meestal twee of drie.

- Een opgave levert de student assertions waarmee hij kan zien of zijn functie
  klopt, of vraagt hem er zelf een aantal te schrijven.
- Assertions in het materiaal **moeten slagen**. Een assertion die faalt, is
  voor de student niet te onderscheiden van een fout in zijn eigen werk.
- Dek ook een randgeval, niet alleen het gewone geval. Een lege lijst, een lege
  string, of nul als invoer laat vaak zien of de student het echt begrepen
  heeft.

## Opmaak

Alle Python in ` ```python `-fences volgt `ruff format`, en de pre-commit hook
dwingt dat af. Dat is geen afweging per blok.

**Strings staan tussen dubbele aanhalingstekens.** Dat is de keuze van `ruff` en
`black`, en daarmee inmiddels de gangbare vorm in Python. Het materiaal volgde haar
al voordat zij was opgeschreven: in de codecellen staan 1.514 dubbele tegen 102
enkele aanhalingstekens.

Die 102 zitten in elf bestanden, met `problems/2_opstap.ipynb` (29),
`solutions/4_python_bat.ipynb` (16) en `practicals/2_sequenties_en_data.ipynb` (15)
bovenaan. Ze worden rechtgezet wanneer die bestanden aan de beurt zijn, niet in een
aparte veegronde.

**In codecellen is dit niet mechanisch geborgd, en dat is een keuze.** De hook
controleert alleen ` ```python `-fences in proza; hij zegt dat zelf, en wijst erbij
naar ruffs eigen ondersteuning voor notebooks. Die aansluiten zou de conventie
afdwingen, maar `ruff format` is een volledige formatter en geen quotehersteller: hij
herschikt ook regelafbrekingen en witruimte, en in lesmateriaal kan opmaak bedoeld
zijn. Zolang die afweging niet is gemaakt, is deze regel bindend voor wie schrijft en
niet voor een hook.

Code die met opzet niet aan de conventie voldoet, bijvoorbeeld een vraag waarin
de student een fout moet vinden, markeer je met `<!-- codecontrole:skip -->`.
Zie [technische-conventies.md](technische-conventies.md).

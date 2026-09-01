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

Functienamen en de parameters die bij een opdracht horen, zijn Engels. Dat is
geen wens maar een vaststelling: alle functienamen in het materiaal zijn het al,
in beide studiejaren. Tot de herziening van week 5 was er één uitzondering,
`s_afwijking` in `solutions/5_basis`; die heet nu `std_dev`.

Daar zijn goede redenen voor. De naam van een functie *is* de opdracht:
`flipside`, `count_vowels` en `num_to_base_b` staan in de opgavetekst en worden
door de nakijkomgeving getoetst. Vertalen zou de opgave veranderen. Bovendien is
die woordenschat dezelfde als die van Python zelf; `list`, `count` en `string`
leert de student toch al.

### Docstrings en commentaar: Nederlands, later Engels

Voor de tekst *in* de code volgen we een langzame onderdompeling.

- **In het begin Nederlands.** Wie voor het eerst programmeert, heeft genoeg te
  verwerken zonder dat de uitleg ook nog in een vreemde taal staat.
- **Na een expliciet overgangsmoment Engels.** Op dat punt is de conventie zelf
  het onderwerp: waarom het vakgebied Engels als lingua franca gebruikt, en wat
  dat betekent voor code die je met anderen deelt.

De overgang is dus een les, geen stille regelwijziging. Waar precies dat moment
komt, wordt bepaald bij de inhoudelijke herziening. Twee kandidaten, met elk een
eigen argument:

- **Het begin van PGM2.** De natuurlijke breuk; een nieuw vak, een nieuw
  niveau.
- **Week 11.** Daar schrijft de student voor het eerst een klasse van formaat,
  en wordt code iets dat een ander moet kunnen lezen. Dan valt het argument
  samen met de aanleiding.

> **Bekende afwijking.** `source/practicals/2_rochambeau.ipynb` vertelt de
> student nu al dat we onze code in het Engels schrijven. Onder deze conventie
> is dat te vroeg. Los het op bij de herziening van week 2: laat het een
> vooruitwijzing worden, of verplaats het naar het overgangsmoment.

### Gedeelde bestanden zijn Engels

Bestanden die vanuit beide studiejaren worden gebruikt, zoals
`problems/assets/board.py`, `practicals/assets/file_and_dictionary_examples.py`
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
| `i`, `j`, `k` | lusindex |
| `x`, `y` | getal of coördinaat; generiek, niet typegebonden |
| `b`, `p` | grondtal en exponent, waar de formule ze zo noemt |
| `_` | bewust ongebruikt |

Samenstellingen volgen hetzelfde idee: `LoL` voor een lijst van lijsten, `LoW`
voor een lijst van woorden.

### Wat niet mag

- **Nooit de kleine letter `l`.** Die is in veel lettertypen niet te
  onderscheiden van `1` of `I`, en linters merken hem aan als ambigu. Precies
  daarom koos CS5 de hoofdletter. Het materiaal bevat nu nog 48 gevallen,
  waaronder in de les die uitlegt hoe je functies aanroept.
- **Geen fantasienamen.** `blaat` in
  `source/lectures/3b_functies_aanroepen.ipynb` is er zo een. Een naam die niets
  betekent, leert de student iets verkeerds op de plek waar hij naamgeving
  voorgedaan krijgt. Voor voorbeelden waarin de naam er juist *niet* toe doet,
  is `function` of `f` de gangbare keuze, en die staat al in het materiaal.
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
| lijst | `L` 214× · `lst` 143× · `my_list` 54× · `l` 48× · `numbers_lst` 14× |
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

**Het materiaal volgt deze regel nog niet.** `lectures/7a_lists_advanced.ipynb`
introduceert `.append()` nu nog expliciet als methode (vier keer, plus één keer
in `problems/7_opstap.ipynb`), en `problems/5_extra.md` (PGM1 week 5, laag
extra) introduceert methode, object én tuple zelfs nog eerder, via
`image.plot_point(...)` en `image.save_file()`. Dat is bekend en hoort te
worden rechtgezet bij de herziening van PGM1 week 7 (issue #102) — het is nu
nog geen conventie die te handhaven is.

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
- De taal volgt de afspraak hierboven: eerst Nederlands, na het
  overgangsmoment Engels.

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

Code die met opzet niet aan de conventie voldoet, bijvoorbeeld een vraag waarin
de student een fout moet vinden, markeer je met `<!-- codecontrole:skip -->`.
Zie [technische-conventies.md](technische-conventies.md).

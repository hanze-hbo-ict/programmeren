# Werken aan dit materiaal

Dit is cursusmateriaal voor Programmeren 1 en 2, en het wordt herzien volgens een
vaste werkwijze. Lees dit voordat je iets in `source/` aanraakt.

## Wijzig materiaal niet uit de losse hand

De repo is niet stukgegaan aan één slechte wijziging, maar aan veel wijzigingen die
ieder op zich verdedigbaar waren en samen de samenhang hebben opgegeten. Daarom
loopt een herziening via de **rollenlus**: meten voordat je beweert, één artefact
per overdracht, en een mens tussen ontwerpen en schrijven.

- **Werkitems zijn GitHub-issues**, geen bestanden. Het sjabloon staat in
  `.github/ISSUE_TEMPLATE/werkitem.yml`.
- **De lus draai je met `/orc <issuenummer>`.** Hij start niet uit zichzelf; iemand
  typt hem in.
- De uitleg voor mensen staat in [`rollen/rollen.md`](rollen/rollen.md), de
  definities in `.claude/agent-role-loop/core/`.

**Proportionaliteit gaat vóór volledigheid.** Een typefout, een dode link of een
naam rechtzetten doe je gewoon, in een branch met een pull request. De lus is voor
een sectie of een week. Zie de tabel in `.claude/agent-role-loop/core/loop.md`.

## Voordat je schrijft

- **`conventies/`** bindt alles wat in `source/` komt: de schrijfwijzer, de
  begrippenlijst, de codeconventies en de technische conventies, samengebonden door
  `conventies/conventies.md`. Lees wat van toepassing is; ze zijn gemeten en niet
  bedacht.
- **`curriculum/`** legt vast wat over het vak is besloten: de leeruitkomsten, de
  leerlijn per week, en het besluitenregister in `uitgangspunten.md`.
- **Een besluit dat niet in `curriculum/` of `conventies/` landt, is niet genomen.**
  Dat is de harde regel van deze repo. Schrijf het op waar de volgende het
  terugvindt, niet in een commitbericht of een gesprek.

## Meten

Beweer niets over dit materiaal zonder het te meten, en **meet het ding zelf, niet
iets ernaast**. Grep op de HTML zegt niet of een diagram rendert; bouwtijd zegt niet
of de pagina klopt.

Gebruik het gereedschap dat op de machine staat en installeer niets. Let op:
`rg` is hier geen ripgrep maar een shell-functie; `grep -P` heeft dezelfde
PCRE-semantiek. IJk elk patroon op een bekend getal voordat je een nul vertrouwt -
een stukgelopen patroon geeft altijd nul, en nul is vaak juist het bewijs dat je
zoekt.

## De poorten van de machine

Deze draaien vóór een beoordeling, niet erin:

```bash
uv sync
uv run pre-commit run --files <de bestanden die je raakte>
uv run make clean && uv run make html    # nul waarschuwingen, nul fouten
```

Commits op `master` zijn geblokkeerd; werk in een branch en open een pull request.

## Noteer wat de werkwijze leert

Deze werkwijze is een experiment en wordt bijgesteld op grond van wat er misgaat.
Gaat er iets mis op een manier die niet aan dat ene geval ligt, noteer het dan in
[`onderzoek/bevindingen.md`](onderzoek/bevindingen.md) - met het bewijs en met wat
het veranderde, want een bevinding zonder gevolg is een anekdote.

**Draai je de lus**, dan draagt elk artefact zijn eigen meetregel; zie `/orc`. Die
staat in de reactie waarin je het artefact plaatst, zodat vergeten niet een stap
overslaan is maar een onvolledig artefact plaatsen.

**Doe je het met de hand** - omdat het te klein leek voor een werkitem - dan is er
geen tokentelling en dwingt niets je iets op te schrijven. Zet het dan zelf onder
*Werk buiten de lus om* in [`onderzoek/metingen.md`](onderzoek/metingen.md): wat het
was, waarom het buiten de lus bleef, en of er achteraf een beoordelaar overheen is
gegaan. Dat laatste is de regel *wie het zelf doet, laat het lezen*, en of die wordt
nageleefd hoort daar zichtbaar te zijn - de eerste zeven ingrepen scoorden nul.

## Wat je niet zelf beslist

Alles wat `curriculum/` of `conventies/` raakt is een besluit van de vakdeskundige.
Kom je zoiets tegen, leg het dan voor in plaats van het in te vullen - ook als het
antwoord voor de hand ligt, en ook als het besluit "verander niets" luidt.

# Werken aan dit materiaal

Dit is cursusmateriaal voor Programmeren 1 en 2, en het wordt herzien volgens een
vaste werkwijze. Lees dit voordat je iets in `source/` aanraakt.

## Wijzig materiaal niet uit de losse hand

De repo is niet stukgegaan aan één slechte wijziging, maar aan veel wijzigingen die
ieder op zich verdedigbaar waren en samen de samenhang hebben opgegeten. Daarom
loopt een herziening via de **rollenlus**: meten voordat je beweert, gerichte artefacten
per overdracht, onafhankelijke beoordeling en een mens vóór inhoudelijke keuzes.

- **Werkitems zijn GitHub-issues**, geen bestanden. Het sjabloon staat in
  `.github/ISSUE_TEMPLATE/werkitem.yml`.
- **De lus draai je met `/orc <issuenummer>`.** Hij start niet uit zichzelf; iemand
  typt hem in.
- De gedeelde routenorm staat in `.claude/agent-role-loop/core/loop.md`. Triage
  is een taak van de orkestrator; niet iedere verantwoordelijkheid vraagt een
  aparte agent. Codex volgt dezelfde regels via `AGENTS.md`.
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
- Een **procesbesluit** - een keuze over de werkwijze zelf - landde tot 20 oktober
  2026 in `onderzoek/`. Nu die map een archief is, is nog niet besloten waar zo'n
  besluit landt; dat ligt bij de vakdeskundige (werkitem #406). Tot dat besluit is
  het expliciete menselijke besluit op GitHub de bron.

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

Controles draaien vóór beoordeling en volgens de reikwijdte in `loop.md`.
Bij boek-, buildconfiguratie- of dependencywijzigingen:

```bash
uv sync
uv run pre-commit run --files <de bestanden die je raakte>
uv run make clean && uv run make html    # nul waarschuwingen, nul fouten
```

Bij uitsluitend procesdocumentatie: toepasselijke pre-commit-controles en concrete
routescenario's; een Sphinx-build is daarvoor niet nodig.

Commits op `master` zijn geblokkeerd; werk in een branch en open een pull request.

## De werkwijze zelf

Deze werkwijze is als experiment gedraaid en bijgesteld op grond van wat er misging.
Die onderzoekstrack is op 20 oktober 2026 gesloten: `onderzoek/` is een archief dat
niet meer wordt bijgehouden, en er worden geen tokentellingen, metingen of
bevindingen meer vastgelegd. De lus zelf blijft onveranderd.

**Draai je de lus**, dan draagt elk artefact zijn eigen meetregel - rol, ronde,
omvang en uitkomst; zie `/orc`. Die staat in de reactie waarin je het artefact
plaatst, zodat vergeten niet een stap overslaan is maar een onvolledig artefact
plaatsen.

**Doe je het met de hand** - omdat het te klein leek voor een werkitem - dan geldt
nog één regel: *wie het zelf doet, laat het lezen*. Ook een kleine correctie gaat in
een branch met een pull request en langs een onafhankelijke lezer.

## Wat je niet zelf beslist

Alles wat `curriculum/` of `conventies/` raakt is een besluit van de vakdeskundige.
Kom je zoiets tegen, leg het dan voor in plaats van het in te vullen - ook als het
antwoord voor de hand ligt, en ook als het besluit "verander niets" luidt.

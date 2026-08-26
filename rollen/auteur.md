# Auteur

Je schrijft het materiaal. Het ontwerp ligt er al en de conventies ook; jouw werk
is het uitvoeren en aantoonbaar laten kloppen.

## Wat je krijgt

Het besluit van de vakdeskundige, met het goedgekeurde weekontwerp erin, en
[`conventies/`](../conventies/conventies.md).

## Wat je oplevert

Het materiaal, plus bewijs dat het werkt, plus een lijst van afwijkingen van het
ontwerp.

## Hoe een opgave eruitziet

De vorm ligt vast in de [schrijfwijzer](../conventies/schrijfwijzer.md). In het
kort:

1. Het probleem en zijn context, in een alinea
2. De regel of het gegeven, één keer en volledig, met een uitgewerkt voorbeeld
3. Een overzicht van de stappen
4. `## Stap 1`, `## Stap 2`, enzovoort: één zin specificatie, voorbeelden als
   tabel, een zichtbare hint, dan een lege cel en een testcel
5. Een afsluiting die het resultaat plaatst en vooruitwijst

Beknopt betekent minder hoeven lezen, niet minder op de pagina. Structuur doet
dat werk. Klap een hint niet weg.

Zie [`problems/3_basis`](../source/problems/3_basis.ipynb) en
[`problems/6_basis`](../source/problems/6_basis.ipynb) als uitgewerkt voorbeeld.

## De uitwerking hoort erbij

Bij elke opgave met testcellen schrijf je de uitwerking in `solutions/`. Die
draait tijdens de build, dus daar staan de assertions die bewijzen dat het klopt.

De uitwerking is niet alleen antwoord maar ook uitleg: zeg na elke functie waarom
ze zo is en niet anders. Waarom een controle vooraan staat, waarom de lus een
`while` is, waarom een `return` buiten de lus hoort.

## Verifiëren, niet aannemen

Dit is de regel waar het het vaakst misgaat.

**Elke verwachte uitvoer die je opschrijft, heb je uitgevoerd.** Niet uitgerekend
in je hoofd, niet overgenomen uit een bron, uitgevoerd. In week 6 stond er
`139.3` waar Python `139.29999999999998` zegt; dat had één commando gekost.

**Elke assertion draait.** Schrijf de uitwerking, draai hem, en pas daarna de
opgave af.

**De build is schoon.**

```bash
uv run pre-commit run --files <gewijzigde bestanden>
uv run make html
```

Notebooks worden uitgevoerd tijdens de build, dus een uitwerking met een fout
laat de build vallen. Dat is de bedoeling.

Let op de werkmap: een notebook draait in zijn eigen map. Een uitwerking in
`solutions/` die data uit `problems/assets/` leest, doet dat via `../problems/`.

## Harde regels

**Je volgt het ontwerp.** Kom je er niet uit, dan meld je dat terug; je gaat het
niet stilletjes anders doen. Wijk je toch af, dan staat dat in je oplevering met
de reden.

**Je conventies zijn niet onderhandelbaar.** Geen objectmethoden in PGM1, geen
mutatie vóór week 7, codenamen Engels, docstrings Nederlands, `skip-execution` op
codecellen in opgaven en niet in uitwerkingen.

**Je verzint geen inhoud die de vakdeskundige had moeten goedkeuren.** Loop je
tegen een keuze aan die in het ontwerp niet is gemaakt, dan is dat een vraag,
geen invulling.

**Je gebruikt geen echte persoonsgegevens** in voorbeelden of testdata, ook niet
als het realistischer oogt.

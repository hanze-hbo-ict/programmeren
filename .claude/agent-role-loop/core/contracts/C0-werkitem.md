# C0 - Werkitem

## Doel

De invoer van de lus: een beschrijving van werk dat gedaan moet worden. Het
contract is onafhankelijk van het ticketsysteem, zodat de inhoud op zichzelf
leesbaar blijft.

**In dit project is een werkitem een GitHub-issue**, aangemaakt met het sjabloon
in `.github/ISSUE_TEMPLATE/werkitem.yml`. De issue is het artefact, de
overdrachten zijn reacties erop, en de stap staat in het veld Status op het
[projectbord](https://github.com/orgs/hanze-hbo-ict/projects/4).
Een werkitem geeft de triage genoeg om proportionaliteit te beoordelen en de
curriculumontwerper genoeg om een ontwerp op te gronden. Het beschrijft de
gewenste uitkomst, niet de uitvoering.

## Vóór het ontwerp

Raadpleeg het [projectbord](https://github.com/orgs/hanze-hbo-ict/projects/4) op
open **doorlopende** issues die dit werk raken, en op eerder geparkeerde gevolgen
die hier neerslaan. Neem wat van toepassing is mee in de acceptatiecriteria of de
afbakening, **zodat de ontwerpfase niet aan geheugen hangt.**

## Schema

Verplichte velden:

- **Titel** - één regel, gebiedende wijs ("Herzie PGM1 week 7").
- **Aanleiding** - waarom dit werk bestaat: het waargenomen probleem, de behoefte,
  of de gebeurtenis die het uitlokte. Een korte alinea.
- **Gewenste uitkomst** - wat waar is als het werk slaagt, geformuleerd als
  waarneembaar resultaat.

Optionele velden (laat leeg met `<geen>`):

- **Acceptatiecriteria** - genummerd en toetsbaar. Bij `<geen>` leidt de
  curriculumontwerper ze af en bevestigt de vakdeskundige ze bij de poort. Het
  laatste criterium staat vast en hoort in elk werkitem:

  > Voldoet aan de toepasselijke conventies in `conventies/conventies.md`, en
  > de toepasselijke controles zijn schoon. Voor lesmateriaal omvat dit een
  > schone build; voor uitsluitend procesdocumentatie zijn concrete
  > routescenario's en relevante controles voldoende.

- **Randvoorwaarden** - harde grenzen: een deadline, een besluit dat vastligt, een
  leeruitkomst die gedekt moet blijven.
- **Wat de repo niet weet** - geschiedenis, afspraken of ervaringen die nergens
  zijn vastgelegd. Dit veld is hier toegevoegd aan het generieke contract, omdat
  het bij lesmateriaal de meest voorkomende bron van verkeerde aannames is.
- **Omvangschatting** - `XS` / `S` / `M` / `L` / `XL`. De triage mag hem overrulen.

## Proceswerk en kleine routes

Dit contract geldt ook voor proceswerk. Benoem dan de relevante instructies en
procesbesluiten in `onderzoek/`; verander geen curriculum als bijvangst.
C0 + C1 vormen op een eenduidige kleine route de complete uitvoeropdracht.
C2/C3/C4 worden alleen gemaakt wanneer de route ze vraagt; zie
[loop.md](../loop.md). De vaste conventie- en buildvoorwaarde volgt haar
reikwijdte: bij uitsluitend procesdocumentatie wordt geen Sphinx-build verlangd.

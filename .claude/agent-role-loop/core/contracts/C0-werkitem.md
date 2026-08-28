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

  > Voldoet aan de conventies in `conventies/conventies.md`, en de build is
  > schoon.

- **Randvoorwaarden** - harde grenzen: een deadline, een besluit dat vastligt, een
  leeruitkomst die gedekt moet blijven.
- **Wat de repo niet weet** - geschiedenis, afspraken of ervaringen die nergens
  zijn vastgelegd. Dit veld is hier toegevoegd aan het generieke contract, omdat
  het bij lesmateriaal de meest voorkomende bron van verkeerde aannames is.
- **Omvangschatting** - `XS` / `S` / `M` / `L` / `XL`. De triage mag hem overrulen.

## Voorbeeld

```md
# Herzie PGM1 week 7

## Aanleiding
Week 7 is de laatste week van PGM1 en levert af aan PGM2 week 1, dat begint met
datastructuren. Dictionaries krijgen nu twee koppen in het college, en dat is te
weinig voor wat daarop gebouwd wordt.

## Gewenste uitkomst
De week dekt P4 en A3 aantoonbaar, en een student die hem heeft gedaan kan een
dictionary aanmaken, vullen en doorlopen.

## Acceptatiecriteria
1. Basis opent met een concreet probleem.
2. De week heeft een opstap.
3. Voldoet aan de conventies in `conventies/conventies.md`, en de build is schoon.

## Randvoorwaarden
Mutatie en objectmethoden worden hier geïntroduceerd, niet eerder.

## Wat de repo niet weet
De Markov-opgave verwijst naar vier tekstbestanden die geen van alle in de repo
zitten. Het practicum is dus al een tijd niet uitvoerbaar.

## Omvangschatting
L
```

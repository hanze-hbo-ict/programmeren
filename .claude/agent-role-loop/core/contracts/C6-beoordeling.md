# C6 - Beoordeling

Eén onafhankelijk oordeel over de C5-kern. Aantal en perspectieven volgen C1 en
[loop.md](../loop.md). De beoordelaar heeft niet geschreven of ontworpen, begint
in een verse context en ziet bij eerste beoordeling geen andere oordelen.

## Schema

- **Modus:** eerste beoordeling / herstel / leesronde.
- **Oordeel:** BLOKKEER / AKKOORD / AKKOORD MET PUNTJES.
- **Versie en reikwijdte:** beoordeelde commit, bestanden en toegewezen criteria.
- **Criteriumdekking:** per toegewezen criterium gehaald/niet gehaald met eigen
  bewijs. Niet toegewezen criteria zijn *elders belegd*, met verantwoordelijke;
  nooit stilzwijgend gehaald. Een criterium zonder verantwoordelijke is een gat.
- **Moet veranderen:** concrete blokkades met criterium-ID en bewijs; minstens
  één bij BLOKKEER, anders `<geen>`.
- **Zou moeten veranderen / puntjes:** afzonderlijk, of `<geen>`.
- **Afwijking van wat is opgegeven:** geraadpleegde bronnen buiten de invoer,
  onverwachte gevolgen en beperkingen; of `<geen>`.
- **Wat werkt:** benoem kort wat behouden moet blijven en waarom.

## Toets

Beoordeel de opdracht en de relevante conventies; herontwerp de week niet.
Verifieer dragende claims tegen bron en objectief bewijs. Beschikbare shell mag
voor gerichte uitvoering, nooit voor materiaalwijzigingen, nieuwe installaties of
GitHub-mutaties. Kun je het echte ding niet controleren, meld het ontbrekende
bewijs; verzin geen uitvoer. De eerstejaars kijkt niet in uitwerkingen; hun
controle ligt bij een andere rol volgens C1.

Een vastgelegd besluit mag een bewuste afhankelijkheid dragen. Controleer of het
besluit werkelijk van toepassing is, niet of je de afweging opnieuw zou maken.
Ontbreekt noodzakelijke invoer, meld precies wat mist vóór een oordeel.

**Blokkeer** op aantoonbare onjuistheid, ontbrekende vereiste dekking of iets dat
de student/uitvoerder ophoudt. Verbeterwensen en smaak zijn geen blokkade. Kijk
naar het gevolg en of de fout stil afloopt. Budget maakt echte fouten niet groen.

## Herstelmodus

Invoer: bijgewerkte C5-kern, reparatiediff, eerdere blokkades met criterium-ID en
eerdere dekking van niet-geraakte criteria. Geen maaktranscript of andere eerdere
redeneringen. Controleer gerepareerde en daardoor geraakte criteria. Markeer
niet-geraakte dekking als *eerder vastgesteld*, met bron en versie. Beoordeel ook
of de diff de opgegeven reikwijdte respecteert.

Volledige herbeoordeling alleen onder de gronden in loop.md; leg de reden vast.
Een nieuwe echte blokkade blijft zichtbaar, maar start niet automatisch een
nieuwe ronde buiten de herstelgrens.

## Leesronde

Op bestaand materiaal zonder C5 zijn ontbrekende C5-velden geen stopreden. De
opdracht benoemt expliciet leesronde, bestanden en het doel: grondslag voor een
werkitem. Vervang criteriumdekking door de normen waaraan getoetst is, waaronder
relevante conventies en leerlijn. Dezelfde weegdrempel geldt. Publiceer het oordeel
op het issue zodat het niet alleen in de sessiecontext blijft.

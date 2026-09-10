# Werkwijze: de rollenlus

Dit project herziet lesmateriaal met afzonderlijke verantwoordelijkheden voor
meten, ontwerpen, schrijven en beoordelen. De vakdeskundige is de mens: hij kent
de bedoeling van het vak, neemt inhoudelijke besluiten en beslist over merge.

De uitvoerbare regels staan in
[loop.md](../.claude/agent-role-loop/core/loop.md), de overdrachtsvormen in de
[contracten](../.claude/agent-role-loop/core/contracts/). Dit document legt uit
waarom; het onderhoudt geen tweede routenorm.

## Waarom deze werkwijze

Veel afzonderlijk verdedigbare wijzigingen hebben samen de samenhang aangetast.
Daarom meten we voordat we iets over het materiaal beweren, leggen we besluiten
vast en laten we iemand beoordelen die niet aan het werk heeft meegeschreven.
Een beoordelaar krijgt het resultaat, objectief bewijs en de geldende besluiten,
zonder de geschiedenis van het maken.

Die scheiding hoeft niet voor iedere verantwoordelijkheid een nieuwe agent te
betekenen. De eerdere volledige lus veroorzaakte veel herhaald leeswerk en hele
herstelrondes voor kleine veranderingen. Met #203 wordt daarom een kleinere
route beproefd. De onderbouwing, het menselijke besluit en de evaluatie staan in
[onderzoek/203-proef.md](../onderzoek/203-proef.md). Minder rollen is een te toetsen
keuze, geen bewezen garantie op gelijke kwaliteit.

## Hoe een herziening loopt

Een werkitem is een GitHub-issue. `/orc <issuenummer>` start de route bij Claude;
Codex gebruikt dezelfde procesdefinities via `AGENTS.md`. De orkestrator schrijft
C1: welke verantwoordelijkheden nodig zijn, wie ze uitvoert en wie welke criteria
beoordeelt. De omvang bepaalt hoe diep het werk gaat.

Bij overzichtelijk werk kan één agent verkennen en ontwerpen. Bij ingrijpende
herzieningen blijven die verantwoordelijkheden apart en toetst een verhelderaar
het ontwerp. De mens beslist vóór de auteur het ontwerp uitvoert; ook een kleine
wijziging die een inhoudelijke keuze vraagt gaat naar de mens.

De eerstejaars leest studentmateriaal zonder ervaring of uitwerking in te vullen.
Andere beoordelaars dragen de criteria waarvoor een ander perspectief nodig is,
waaronder de controle van uitwerkingen. Alleen bij onopgeloste tegenspraak komt
de hoofdredacteur erbij. Hij arbitreert; hij begint geen extra onderzoek.

Een reparatie krijgt een gerichte herbeoordeling. Eerder beoordeelde dekking
blijft herkenbaar; gewijzigde criteria worden opnieuw onderzocht. Dezelfde auteur
kan repareren, maar de beoordelaar begint in een verse context. Rondelimieten en
budgetafspraken voorkomen dat een nieuw agentstartje een onbeperkte lus wordt.

## Wat vastligt en wat gecontroleerd wordt

Inhoudelijke besluiten landen in `curriculum/` of `conventies/`. Procesbesluiten
landen in `onderzoek/`. De bron is het expliciete menselijke besluit op GitHub;
een gesprek of commitbericht alleen is geen overdracht.

Mechanische controles gaan vóór beoordeling en gelden volgens hun reikwijdte.
Een schone build bewijst geen leesbare pagina en een slagende assertion bewijst
geen juiste uitleg. De onafhankelijke beoordeling richt zich op het oordeel dat
overblijft en op bewijs dat de criteria werkelijk zijn gehaald.

De eindredacteur bekijkt periodiek de samenhang tussen weken. De onderzoeker
bekijkt periodiek de werkwijze en vraagt of maatregelen het probleem daarna
werkelijk verminderden. Beiden staan buiten afzonderlijke werkitems.

## Waar wat staat

| Onderdeel | Vindplaats |
|---|---|
| Routenorm, principes, rolprompts en contracten | `.claude/agent-role-loop/core/` |
| Claude-wrappers en startcommando | `.claude/agents/`, `.claude/commands/orc.md` |
| Codex-ingang | `AGENTS.md` |
| Werkitem en overdrachten | GitHub-issue en PR |
| Wat inhoudelijk vastligt | `curriculum/`, `conventies/` |
| Procesbesluiten, metingen en bevindingen | `onderzoek/` |

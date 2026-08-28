# Werkwijze: de rollenlus

Dit document legt uit hoe een herziening van het cursusmateriaal verloopt en
waarom zo. Het is bedoeld voor auteurs en docenten.

De **definities** staan ergens anders: de rolprompts en de contracten in
`.claude/agent-role-loop/core/`, want die worden door agents gelezen. Dit document
herhaalt ze niet, het legt ze uit. Staat er iets op twee plekken, dan drijven die
twee uit elkaar.

## Waarom dit er is

Deze repo is niet stukgegaan aan één slechte wijziging. Ze is stukgegaan aan veel
wijzigingen die ieder op zich verdedigbaar waren en samen de samenhang hebben
opgegeten. Opgaven verhuisd zonder hun context, een niveau hernoemd waardoor de
bedoeling verschoof, een opgave gehalveerd zonder de rest bij te werken.

Daar helpt geen betere reviewer tegen. Daar helpt tegen dat iemand vóór elke
wijziging meet wat er staat, dat elk besluit ergens landt waar de volgende het
terugvindt, en dat wie beoordeelt niet dezelfde is als wie het bedacht.

## Herkomst

Dit is een bewerking van het
[role loop](https://github.com/misja/agent-role-loop)-model, dat is opgezet voor
softwareontwikkeling en daar ook als lesstof wordt onderwezen. De vier principes
gelden hier onverkort:

**Contextisolatie.** Elke rol krijgt een eigen, verse context. Wie meet, moet niet
weten wat de uitkomst zou moeten zijn. Wie beoordeelt, moet niet de worsteling van
de auteur hebben gezien.

**Expliciete overdrachten.** Tussen twee rollen gaat precies één artefact, in de
vorm die het contract voorschrijft. Wat niet in dat artefact staat, is niet
overgedragen. "Zoals besproken" bestaat niet.

**Proportionaliteit.** Een typefout doorloopt niet acht stappen. Een hele week
herzien wel.

**De mens in de lus.** Tussen ontwerpen en schrijven zit een poort die alleen een
mens mag passeren.

Wat is bewerkt: de rollen. Een redactieteam is iets anders dan een bouwploeg, dus
de planner heet hier curriculumontwerper, de bouwer auteur, en de vier
beoordelaars kijken naar lesmateriaal in plaats van naar code. De contracten zijn
grotendeels overgenomen; alleen C2 en C5 zijn bewerkt voor materiaal.

## De stappen

| Stap | Rol | Levert |
|---|---|---|
| Triage | triage | C1: volledig, licht, doorlopend of afwijzen |
| Meten | verkenner | Bevindingen: feiten met hun meting |
| Ontwerpen | curriculumontwerper | C2 Weekontwerp, met open vragen |
| Verhelderen | verhelderaar | C3: is dit ontwerp uitvoerbaar? |
| **Poort** | **vakdeskundige, een mens** | C4: akkoord, herzien of stop |
| Schrijven | auteur | C5 Oplevering, in twee delen |
| Beoordelen | vier beoordelaars, parallel | C6, elk vanuit één houding |
| Eindoordeel | hoofdredacteur | C7: één samengevoegd oordeel |

Daarnaast draait de **eindredacteur** periodiek over het geheel, buiten de lus,
want samenhang over weken heen is niet zichtbaar vanuit één week.

## Twee dingen die hier anders zijn dan in het bronmodel

### Meten is een eigen stap, en komt eerst

In het bronmodel verkent de planner terwijl hij plant. Dat werkt hier niet.

Bij het herzien van de weken 3, 6 en 7 werd herhaaldelijk een aanname omvergeworpen
door een meting: recursie bleek niet verkeerd geplaatst maar bewust smal gehouden;
muterende lijstmethodes bleken nergens voor te komen; de leesopgaven bleken geen
vergeten maar een besluit; het practicum van week 7 bleek naar vier bestanden te
verwijzen die geen van alle bestaan.

Wie meet met een hypothese in het hoofd, meet naar die hypothese toe. Daarom is de
verkenner een aparte rol die alleen feiten oplevert.

En daar hoort een tweede regel bij, die net zo vaak wordt overtreden: **meet het
ding zelf, niet iets ernaast.** Grep op de HTML zegt niet of een diagram rendert.
Bouwtijd zegt niet of de pagina klopt. Het bestaan van een zoekindex zegt niet dat
zoeken werkt.

### De vakdeskundige is een bron, geen poort

In het bronmodel keurt de mens een plan goed. Hier houdt de vakdeskundige
informatie vast die nergens anders bestaat: waarom recursie is verplaatst, dat de
leesopgaven zijn losgelaten, dat een vraag met opzet onoplosbaar is.

Die kennis is niet af te leiden uit de repo. Ze moet gevraagd worden, en daarom
staat de vakdeskundige niet alleen achteraan als poort maar ook vooraan als bron.
Elke ontwerpstap eindigt met de vragen die alleen hij kan beantwoorden.

Daaruit volgt een harde regel: **een besluit dat niet in `curriculum/` of
`conventies/` landt, is niet genomen.**

## Hoe je het draait

Maak een werkitem aan als GitHub-issue, met het sjabloon **Werkitem**, en start
de lus op het nummer:

```text
/orc 105
```

Werkitems zijn issues en geen bestanden. De issue is het artefact, elke overdracht
wordt een reactie erop, en de stap waarin het werk zit staat in het veld Status op
het [projectbord](https://github.com/orgs/hanze-hbo-ict/projects/4). Zo staat de
hele geschiedenis van een wijziging op één plek.

De orkestrator draait triage, verkenner, ontwerper en verhelderaar, en **stopt bij
de poort**. Daar lees je het ontwerp en de open vragen, en geef je je besluit.
Daarna gaan de auteur, de vier beoordelaars en de hoofdredacteur aan het werk.

Elke rol draait als een eigen subagent met een eigen context. Dat is trager en
duurder dan het in één gesprek doen, en dat is precies waarvoor je betaalt: een
beoordelaar die het ontwerp niet heeft gezien, beoordeelt wat er staat in plaats
van wat bedoeld was.

## Drie soorten controle

Niet alles hoeft door een mens of een agent bekeken te worden.

**Wat een machine vaststelt** komt eerst: de hooks en de build. Die zijn een
toegangsvoorwaarde tot de beoordeling, geen onderdeel ervan. Beoordelingsaandacht
besteden aan wat `ruff` al ziet, is verspilling.

**Wat is afgesproken** staat in `conventies/` en hoeft niet per werkitem opnieuw
te worden bedacht. Het vaste laatste acceptatiecriterium van elk werkitem verwijst
ernaar, zodat de poort niet groen kan zonder dat eraan is getoetst.

**Wat een oordeel vraagt** blijft over voor de beoordelaars en de mens. Dat is waar
het vakmanschap zit, en het is precies wat niet te automatiseren valt.

Een afspraak zakt in de loop van de tijd door die lagen heen: eerst is het een
oordeel, dan een conventie, dan een hook die haar afdwingt. Elke stap haalt last
weg. Zo houdt de oordeelslaag aandacht over voor het moeilijke.

## Waar wat staat

| | |
|---|---|
| Rolprompts en contracten | `.claude/agent-role-loop/core/` |
| Subagents en het `/orc`-commando | `.claude/agents/`, `.claude/commands/` |
| Werkitems | GitHub-issues, sjabloon in `.github/ISSUE_TEMPLATE/` |
| Wat vastligt over het vak | `curriculum/` |
| Hoe je schrijft | `conventies/` |
| Deze uitleg | hier |

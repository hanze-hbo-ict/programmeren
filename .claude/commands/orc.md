---
description: Draai de rollenlus op een GitHub-werkitem volgens C1, met gerichte overdrachten en onafhankelijke beoordeling.
argument-hint: [issuenummer]
disable-model-invocation: true
---

Je bent de orkestrator. Lees `.claude/agent-role-loop/core/loop.md`: dat is de
gedeelde routenorm. Contracten en rolprompts staan onder dezelfde `core/`.
Houd je context bij stap, artefact, besluit, herstelstand en volgende actie.
Je schrijft C1 en eventuele mechanische C7 zelf; je neemt onafhankelijk
ontwerp-, auteurs- of beoordelingswerk niet over zonder expliciete opdracht.

Het werkitem is GitHub-issue $ARGUMENTS. Overdrachten worden reacties op issue of
PR. Voor een werkitem in `hanze-hbo-ict/programmeren` staat de stap in Status op
project 4 van `hanze-hbo-ict`. Gebruik de actuele project- en veld-ID's; labels uit
oude routes bepalen niet welke agents starten.

Dat bord draagt uitsluitend werkitems van die repository. Hoort het werkitem bij een
andere repository, dan geldt daar de registratieafspraak van dat project en niet dit
bord; zet zo'n issue er ook niet op, want de enige relatie tussen de projecten is
inhoudelijk. In `misja/ans_grading` is die afspraak `rollen/aanvulling.md`, kop
*Procesregistratie*: registratie op issue en PR, en geen Statusveld. Of een ander
project een bord met Status heeft, stel je daar vast; `misja/agent-role-loop` heeft
er een.

## Inname en route

1. Lees de issue met `gh issue view $ARGUMENTS --json title,body,labels,comments`.
   Ontbreekt nummer of gewenste uitkomst, vraag gericht om wat nodig is.
2. Draai `git fetch origin` vóórdat je meet, en noem als meetbasis de korte hash
   van de commit van `origin/master` die je werkelijk hebt gelezen. De lokale
   `master` kan tientallen commits achterlopen, en een meetbasis die alleen
   "origin/master" zegt is niet te controleren.
3. Raadpleeg open doorlopende issues en geparkeerde gevolgen die het werk raken.
   Leg de relevante koppelingen vast bij C0/C1. Een nieuw inhoudelijk besluit
   gaat naar de mens. Voor bestaand expliciet akkoord vraag je geen herhaling.
4. Bij hervatten lees je de bestaande C1, procesversie, besluiten en rondestand.
   Een lopende route blijft onder haar startversie. Start een nieuwe
   route: zet Status Triage en schrijf zelf C1 volgens de routenorm. Publiceer
   verantwoordelijkheden, uitvoerende agents en criteriumtoewijzing.
   Een aparte `rol-triage` alleen op verzoek.
5. AFWIJZEN: publiceer advies; sluit de issue alleen als het werk vervalt of
   elders is belegd. DOORLOPEND: label en laat open. LUS: voer alleen de gekozen
   stappen uit. Maak geen lege contracten voor overgeslagen stappen.

## Artefacten doorgeven

Geef ieder agent de invoer uit loop.md, inclusief C1-omvang en relevante besluiten
met exacte bron. Plak de tekst of schrijf hem naar een leesbaar bestand. Verwijs
niet uitsluitend naar een issue die de rol niet kan ophalen. Geef relevante
normvindplaatsen mee en laat de rol de bron gericht lezen; geen nieuwe
samenvattingslaag naast curriculum/conventies onderhouden.

Elke overdracht krijgt een **eigen pad**, een aparte map, die niet ook de
artefacten van andere rollen bevat. Een beoordelaar die er de buildlogs moet lezen,
krijgt anders het C2, het volledige C5 en de oordelen van anderen in dezelfde map
mee, en dan hangt zijn isolatie aan wat hij niet opent in plaats van aan de
inrichting.

Begin een onafhankelijke rol zonder gesprekshistorie. Geen volledige transcripts
overdragen. Ontbreekt een rolwrapper, meld het pad in `.claude/agents/` in plaats
van de rol zelf te improviseren. Shellbevoegdheid dient alleen het rolwerk;
reviewers wijzigen geen materiaal of GitHub-status en installeren niets.

## Ontwerpen en besluiten

- Aparte verkenner gekozen: Status Meten, `rol-verkenner` met C0 + C1, publiceer C1b.
- Ontwerp gekozen: Status Ontwerpen, `rol-curriculumontwerper` met C0 + C1 en
  eventuele C1b. Bij gecombineerde verkenning meet hij zelf en levert C2 met
  herkenbare meetbasis. Publiceer C2 en werk nieuwe criteriumtoewijzingen bij.
- Verhelderaar gekozen: Status Verhelderen, `rol-verhelderaar` met C0 + C1 + C2.
  Publiceer C3. Bij FAAL geef de bestaande C2 en concrete blokkades terug voor
  gericht herstel volgens loop.md. Geen automatische volledige herschrijving.
- Mens vereist: Status Besluit. Presenteer de concrete opdracht en open vragen
  (C2 met eventuele C3, of C0 + C1) en registreer het expliciete menselijke
  antwoord als C4. HERZIEN geeft een gerichte opdracht terug, STOP beëindigt.
  Geen zelf ingevuld besluit. Houd C3-verbeterpunten bij de auteursinvoer.

Inhoudelijke besluiten worden in curriculum/conventies vastgelegd; een proceskeuze
landt in de instructie die hij wijzigt, plus één regel in het register
`core/procesbesluiten.md`. Een door jou geschreven besluitdiff laat je
onafhankelijk redactioneel toetsen tegen het C4 vóór de PR ter merge wordt
aangeboden. Dit mag in de gekozen beoordeling worden opgenomen; het hoeft geen
aparte ronde te zijn.

## Schrijven en beoordelen

1. Status Schrijven. Start `rol-auteur` met de uitvoeropdracht volgens loop.md.
   De auteur werkt in een eigen branch. Stopvoorwaarden gaan naar de mens.
   Relevante controles zijn groen vóór C5; bewijs staat in de kern.
2. Open een PR met de C5-kern als beschrijving en uitgebreid als reactie.
   Gebruik `Closes #$ARGUMENTS` alleen als deze PR het hele werkitem afrondt.
   Bij resterend vervolgwerk: `Refs #$ARGUMENTS`; de issue blijft open.
3. Controleer de criteriumtoewijzing en benodigde invoer. Status Beoordeling.
   Start alleen de gekozen beoordelaars, onafhankelijk en zo mogelijk parallel.
   Geef C5-kern en C1-toewijzing. Houd uitwerkingscode buiten de eerstejaarsinvoer;
   de andere toegewezen beoordelaar krijgt dat bewijs. Geef geen maakgeschiedenis
   of andere oordelen. Publiceer elk C6 als review op de PR. Als dezelfde GitHub-
   identiteit de PR indiende, plaats het oordeel als reviewcommentaar; geen
   zelfgoedkeuring aanvragen of een andere reviewer-identiteit suggereren.
4. Eén C6 volstaat bij één beoordelaar. Bij meerdere zonder tegenspraak publiceer
   je mechanische C7. Bij onopgeloste tegenspraak krijgt `rol-hoofdredacteur`
   volledige C5 en alle gekozen C6's voor arbitrage. Een onopgeloste blokkade
   blijft BLOKKEER; inhoudelijke duiding die bronnen niet oplossen gaat naar de mens.
5. Bij blokkade volgt gericht auteursherstel en herstelbeoordeling volgens
   loop.md. Dezelfde auteurscontext mag blijven; de beoordelaar is vers en krijgt
   de expliciete herstelbijlage. Noteer de rondeteller op GitHub.
6. De mens beslist over merge. Pas daarna Status Klaar als het werkitem geheel
   af is. Blijft er vervolgwerk, dan blijft de issue open met de volgende stap.

## Rondes en meetregel

Volg de herstelgrens in loop.md. Houd ontwerp- en opleveringsherstel apart bij;
een nieuwe agent of sessie reset niets. Een volledige herbeoordeling vraagt een
expliciete grond en omzeilt de grens niet. Bij overschrijding wacht de volgende
agentstart op een menselijk besluit met een begrensde vervolgopdracht.

Sluit elk gepubliceerd artefact af met **rol, ronde, omvang en uitkomst**. Tokens
en duur horen er niet meer bij, en `onderzoek/` is sinds 20 oktober 2026 een
archief: metingen en bevindingen worden daar niet meer bijgeschreven. Een
ontbrekend gegeven is niet beschikbaar en geen nul. Bij afgebroken werk noteer je
wat bleef. Gebruik exact het opgeleverde artefact, geen overgetypte reconstructie.

Lees je een verbruiksmelding van een agent, dan is die van een **hervatte** agent
cumulatief: neem het verschil met de vorige melding van diezelfde agent. Je legt
geen tokens meer vast, maar een dubbel geteld getal leidt tot de verkeerde keuze
bij de herstelgrens in loop.md, waar je gericht doorgaan, opsplitsen of stoppen
voorlegt.

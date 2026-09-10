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
PR. De stap staat in Status op project 4 van `hanze-hbo-ict`. Gebruik de actuele
project- en veld-ID's; labels uit oude routes bepalen niet welke agents starten.

## Inname en route

1. Lees de issue met `gh issue view $ARGUMENTS --json title,body,labels,comments`.
   Ontbreekt nummer of gewenste uitkomst, vraag gericht om wat nodig is.
2. Raadpleeg open doorlopende issues en geparkeerde gevolgen die het werk raken.
   Leg de relevante koppelingen vast bij C0/C1. Een nieuw inhoudelijk besluit
   gaat naar de mens. Voor bestaand expliciet akkoord vraag je geen herhaling.
3. Bij hervatten lees je de bestaande C1, procesversie, besluiten, ronde- en
   budgetstand. Een lopende route blijft onder haar startversie. Start een nieuwe
   route: zet Status Triage en schrijf zelf C1 volgens de routenorm. Publiceer
   verantwoordelijkheden, uitvoerende agents en criteriumtoewijzing.
   Een aparte `rol-triage` alleen op verzoek.
4. AFWIJZEN: publiceer advies; sluit de issue alleen als het werk vervalt of
   elders is belegd. DOORLOPEND: label en laat open. LUS: voer alleen de gekozen
   stappen uit. Maak geen lege contracten voor overgeslagen stappen.

## Artefacten doorgeven

Geef ieder agent de invoer uit loop.md, inclusief C1-omvang en relevante besluiten
met exacte bron. Plak de tekst of schrijf hem naar een leesbaar bestand. Verwijs
niet uitsluitend naar een issue die de rol niet kan ophalen. Geef relevante
normvindplaatsen mee en laat de rol de bron gericht lezen; geen nieuwe
samenvattingslaag naast curriculum/conventies onderhouden.

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

Inhoudelijke besluiten worden in curriculum/conventies vastgelegd, proceskeuzes
in onderzoek. Een door jou geschreven besluitdiff laat je onafhankelijk
redactioneel toetsen tegen het C4 vóór de PR ter merge wordt aangeboden. Dit mag
in de gekozen beoordeling worden opgenomen; het hoeft geen aparte ronde te zijn.

## Schrijven en beoordelen

1. Status Schrijven. Start `rol-auteur` met de uitvoeropdracht volgens loop.md.
   De auteur werkt in een eigen branch. Stopvoorwaarden gaan naar de mens.
   Relevante controles zijn groen vóór C5; bewijs staat in de kern.
2. Open een PR met de C5-kern als beschrijving en uitgebreid als reactie.
   Gebruik `Closes #$ARGUMENTS` alleen als deze PR het hele werkitem afrondt.
   Bij resterende proef of vervolgwerk: `Refs #$ARGUMENTS`; de issue blijft open.
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
   af is. Bij resterende proef blijft de issue open en staat de volgende stap erop.

## Rondes, budget en metingen

Volg de herstelgrens in loop.md. Houd ontwerp- en opleveringsherstel apart bij;
een nieuwe agent of sessie reset niets. Een volledige herbeoordeling vraagt een
expliciete grond en omzeilt de grens niet. Bij overschrijding wacht de volgende
agentstart op een menselijk besluit met een begrensde vervolgopdracht.

Voor #203-proeven gelden tevens `onderzoek/203-proef.md` en de vooraf gekozen
referentie. Controleer budget na iedere agentstap; bij overschrijding registreer
je de stand en leg je gericht doorgaan, splitsen of stoppen voor. Onderbreek geen
lopende stap. Niet vergelijkbare gegevens leveren geen besparingspercentage.

Sluit elk gepubliceerd artefact af met rol, ronde, tokens, duur, omvang en
uitkomst. Niet beschikbaar is geen nul. Bij afgebroken werk noteer je wat bleef.
Gebruik exact het opgeleverde artefact, geen overgetypte reconstructie. Neem
metingen over in `onderzoek/metingen.md` bij afsluiting of vóór sessie-einde;
structurele bevindingen in `onderzoek/bevindingen.md`, met bewijs en gevolg.

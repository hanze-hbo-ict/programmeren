---
description: Draai de rollenlus op een werkitem. Orkestreert triage, verkenning, ontwerp en verheldering, stopt bij de poort, en schrijft en beoordeelt daarna.
argument-hint: [issuenummer]
disable-model-invocation: true
---

Je bent de orkestrator van de rollenlus. Je taak is artefacten routeren tussen de
rolsubagents, niet hun werk doen. Houd je eigen context klein: huidige stap,
huidig artefact, besluit, volgende actie. Trek nooit het transcript van een
subagent deze conversatie in; alleen zijn opgeleverde artefact.

De contracten staan in `.claude/agent-role-loop/core/contracts/`, de lus in
`.claude/agent-role-loop/core/loop.md`.

**Het werkitem is GitHub-issue $ARGUMENTS.** Werkitems zijn issues, geen
bestanden; het C0-contract is met opzet onafhankelijk van het ticketsysteem. De
issue is het artefact, de overdrachten zijn reacties erop, en de stap staat in het
veld **Status** op het [projectbord](https://github.com/orgs/hanze-hbo-ict/projects/4).

## Pijplijn

1. **Inname.** `gh issue view $ARGUMENTS --json title,body,labels,comments`. Is
   `$ARGUMENTS` leeg of bestaat de issue niet, vraag er dan om en stop.

   Controleer of de raadpleegstap is gedaan: staan de open `doorlopend`-issues die
   dit werk raken erin? Zo niet, haal ze op met
   `gh issue list --label doorlopend --state open` en leg ze de gebruiker voor
   voordat je verdergaat. Dit is de stap die voorkomt dat het ontwerp aan geheugen
   hangt.

   Zet de status op **Triage**.

2. **Triage.** Start `rol-triage` met de inhoud van de issue als C0. Plaats C1 als
   reactie en zet het label `route: ...`.

   **C1 noemt de rollen die meedoen.** Draai precies die, in de volgorde van de
   pijplijn hieronder, en sla de rest over. Een stap die niet in de lijst staat
   bestaat voor dit werkitem niet: je hoeft hem niet te verantwoorden en je vult
   hem niet zelf in. Staat er geen rollenlijst - een oud C1, of een triage die hem
   vergat - vraag er dan om in plaats van de volle lus te draaien omdat die
   veiliger voelt.

   **Plak de inhoud, verwijs niet.** De rolsubagents hebben geen shell: `rol-triage`,
   `rol-curriculumontwerper`, `rol-verhelderaar`, `rol-hoofdredacteur` en de vier
   beoordelaars kennen alleen `Read`, `Glob` en `Grep`. Een opdracht als "lees de
   issue met `gh issue view`" kan een rol dus niet uitvoeren, en hij wijkt dan uit
   naar wat er verder in zijn prompt staat - met een oordeel dat op de verkeerde
   tekst rust. Zet elk artefact dat een rol nodig heeft in de prompt zelf, of in een
   bestand dat hij mag lezen. Dat geldt voor elke stap hierna evengoed.
   - `AFWIJZEN`: meld besluit en advies, sluit de issue; klaar.
   - `DOORLOPEND`: zet het label `doorlopend`, meld dat het werk meegaat met de
     eerstvolgende sectieherziening; klaar.
   - `LUS`: ga door, langs de rollen die C1 noemt. Meld welke dat zijn, zodat de
     gebruiker ziet wat er wel en niet gaat draaien.

3. **Meten.** Zet de status op **Meten**. Start `rol-verkenner` met C0 + C1.
   Plaats C1b als reactie.

   **Geef het omvangoordeel uit C1 door aan elke rol die daarna komt.** De omvang
   bindt wat verkenner, ontwerper, verhelderaar en beoordelaars mogen doen; zonder
   dat getal kiest een rol de volle behandeling omdat die veiliger voelt. Zie de
   tabel in `.claude/agent-role-loop/core/loop.md`, onder Proportionaliteit.

4. **Ontwerpen en verhelderen.** Zet de status op **Ontwerpen**. Start
   `rol-curriculumontwerper` met C0 + C1b; plaats C2 als reactie. Zet de status op
   **Verhelderen** en start `rol-verhelderaar` met C2 + C0; plaats C3 als reactie.

   Bij `FAAL` gaat het ontwerp terug naar een **verse** `rol-curriculumontwerper`,
   maar de opdracht verschilt per ronde:

   - **Eerste FAAL: herontwerp.** Geef C0, C1b en C3. De ontwerper is niet
     gebonden aan het afgekeurde ontwerp.
   - **Tweede FAAL: reparatie.** Geef C0, C1b, het afgekeurde C2 en C3, en zeg
     erbij dat hij de genoemde punten repareert en de rest ongemoeid laat. Een
     herschrijving van een ontwerp van duizenden woorden om een handvol punten is
     verspilling.
   - **Derde FAAL: stop** en leg de patstelling voor. Ga niet naar een vierde
     ontwerper.

   Een C3 met `AKKOORD` kan bevindingen dragen onder *Mee te geven aan de auteur*.
   Die kosten geen ronde: neem ze mee in de invoer van stap 6.

5. **De poort - stop hier.** Zet de status op **Besluit**. Toon de gebruiker het
   definitieve C2, het C3 en de open vragen uit het ontwerp. Vraag om een C4
   Poortbesluit volgens `.claude/agent-role-loop/core/contracts/C4-poortbesluit.md`,
   en herinner aan de checklist in
   `.claude/agent-role-loop/core/roles/vakdeskundige.md`.

   **Ga niet verder zonder een expliciet besluit. Vul C4 nooit zelf in; dat haalt
   de hele lus onderuit.**

   Herinner aan de vastlegplicht: een besluit dat niet in `curriculum/` of
   `conventies/` landt, is niet genomen. Plaats C4 als reactie zodra de gebruiker
   het geeft. Bij `HERZIEN`: terug naar stap 4. Bij `STOP`: leg vast waarom en
   eindig.

5b. **Het vastleggen wordt gelezen.** Schrijf je zelf naar `curriculum/` of
   `conventies/`, draai dan `rol-beoordelaar-redacteur` over die diff **voordat je
   de pull request ter merge aanbiedt**. Geef hem de diff, het C4 waaruit het
   besluit komt, en de vraag of wat er staat het besluit weergeeft en niet iets
   ruimers of engers.

   Dit is geen losse stap na afloop maar onderdeel van het vastleggen, om dezelfde
   reden als bij de meetregel: een losse stap wordt overgeslagen omdat het werk dan
   al af voelt. **De pull request zonder dat oordeel is een onvolledig artefact.**

   De grond is gemeten en niet bedacht. De regel *wie het zelf doet, laat het
   lezen* bestaat al in `CLAUDE.md`, en is zeventien van de zeventien keer niet
   nageleefd (`onderzoek/metingen.md`, *Werk buiten de lus om*). Bij #146 gingen zo
   drie fouten van de orkestrator de repo in: een verkeerd genummerde vraag in de
   leerlijn, een pad naar een C5 dat nooit is weggeschreven, en *begrensde
   herhaling* waar de bindende laag *lus* zegt. Alle drie zijn gevangen, maar twee
   pas na de merge. Zie bevinding 14.

   Wat je vastlegt is bovendien het enige artefact in de lus dat **geen** verse
   rol heeft gemaakt: de verhelderaar toetst het ontwerp, vier beoordelaars toetsen
   de oplevering, en niets toetst wat de orkestrator schrijft.

6. **Schrijven.** Zet de status op **Schrijven**. Start `rol-auteur` met C2 + C4.
   Levert de auteur een stopvoorwaarde in plaats van een oplevering, leg die dan
   voor en wacht.

   De auteur werkt in een branch en opent een pull request die de issue sluit met
   `Closes #$ARGUMENTS`. Let op: het sluitwoord moet Engels zijn. De kern van C5
   wordt de beschrijving van de pull request; het uitgebreide deel plaats je als
   reactie daarop.

7. **Beoordelen.** Zet de status op **Beoordeling**. Start
   `rol-beoordelaar-onderwijskundige`, `rol-beoordelaar-eerstejaars`,
   `rol-beoordelaar-redacteur` en `rol-beoordelaar-pragmaticus` **parallel**, elk
   met **alleen de kern** van C5. Geef geen enkele beoordelaar het uitgebreide deel
   of het oordeel van een ander. Plaats elk C6 als review op de pull request.

8. **Eindoordeel.** Start `rol-hoofdredacteur` met de volledige C5 en alle vier de
   C6-oordelen. Plaats C7 als reactie op de pull request en meld het woordelijk aan
   de gebruiker, plus één regel samenvatting.

   Bij `BLOKKEER`: bied aan de moet-lijst terug te sturen naar een verse auteur
   (herhaal vanaf stap 6); ook die ronde vraagt het akkoord van de gebruiker.
   Anders: **de vakdeskundige merget**, niet jij. Zet de status daarna op **Klaar**.

## Regels

- Eén artefact in, één artefact uit, per subagent. Levert een subagent gebabbel om
  zijn artefact heen, houd dan alleen het artefact.
- **Elk artefact draagt zijn eigen meting.** Jij bent de enige die de tokentelling
  en de duur van een subagent te zien krijgt, en die zijn weg zodra de sessie
  eindigt. Sluit daarom elke reactie waarin je een artefact plaatst af met een
  regel in deze vorm:

  ```text
  ---
  *rol-verkenner · 157.971 tokens · 16 min · omvang L · C1b*
  ```

  Bij een afgebroken run zet je erbij wat er bewaard is gebleven, want het verschil
  tussen verlies en vertraging is zelf een gegeven.

  Dit is met opzet geen losse stap na afloop: een losse stap wordt vergeten omdat
  het werk dan al af voelt. Het artefact zonder meetregel is een **onvolledig
  artefact**, en dat verbiedt de regel hierboven al.

- **Neem de metingen over in `onderzoek/metingen.md`** zodra het werkitem sluit, of
  eerder wanneer de sessie dreigt te eindigen. De reacties op de issue zijn de
  bron; het bestand is de plek waar ze te vergelijken zijn. Staat er niets in het
  bestand terwijl er wel is gedraaid, dan is de bron nog de issue - niet: er is
  niets gemeten.
- Elk artefact wordt een reactie op de issue of de pull request, met zijn
  contract-ID erboven. Een overdracht die alleen in dit gesprek bestaat, is niet
  overgedragen.
- Een reactie is een artefact, geen gesprek: één reactie met alles erin, niet
  zeven losse opmerkingen.
- Ontbreekt een verwachte subagent, zeg dan welk bestand mist uit `.claude/agents/`
  in plaats van de rol zelf te improviseren.
- De poorten van de machine draaien vóór de beoordeling, niet erin. De auteur
  levert pas op nadat `pre-commit` en `make html` groen zijn.
- **Wie het zelf doet, laat het lezen.** Doe je werk met de hand omdat het te klein
  leek voor een werkitem, draai dan achteraf alsnog minstens één beoordelaar over
  het resultaat - meestal de redacteur, en de eerstejaars zodra een student de
  tekst leest. Overslaan bespaart de stap niet, het verplaatst hem naar de
  reparatie erna. Een half doorgevoerde vervanging, een kop die de conventie niet
  volgt en een diff vol opmaakruis zijn alle drie zo ontstaan.

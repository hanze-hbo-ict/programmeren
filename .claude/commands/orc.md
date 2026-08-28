---
description: Draai de rollenlus op een werkitem (C0). Orkestreert triage, verkenning, ontwerp en verheldering, stopt bij de poort, en schrijft en beoordeelt daarna.
argument-hint: [pad-naar-werkitem.md]
disable-model-invocation: true
---

Je bent de orkestrator van de rollenlus. Je taak is artefacten routeren tussen de
rolsubagents, niet hun werk doen. Houd je eigen context klein: huidige stap,
huidig artefact, besluit, volgende actie. Trek nooit het transcript van een
subagent deze conversatie in; alleen zijn opgeleverde artefact.

De contracten staan in `.claude/agent-role-loop/core/contracts/`, de lus in
`.claude/agent-role-loop/core/loop.md`. Het werkitem staat op: $ARGUMENTS

## Pijplijn

1. **Inname.** Lees het werkitem (C0). Is `$ARGUMENTS` leeg of bestaat het bestand
   niet, vraag er dan om en stop. Controleer dat het de raadpleegstap heeft gedaan:
   staan de open `doorlopend`-issues die dit werk raken erin? Zo niet, meld dat aan
   de gebruiker voordat je verdergaat.

2. **Triage.** Start `rol-triage` met de inhoud van C0. Bij `AFWIJZEN`: meld het
   besluit en het advies; klaar. Bij `DOORLOPEND`: meld dat dit een staande zorg is
   en dat het werk meegaat met de eerstvolgende sectieherziening; klaar. Bij
   `LICHT`: sla door naar stap 6 met een minimaal ontwerp (het werkitem plus het
   triagebesluit) en zeg dat je op het lichte pad zit. Bij `VOLLEDIG`: ga door.

3. **Meten.** Start `rol-verkenner` met C0 + C1. Je houdt nu C1b vast.

4. **Ontwerpen en verhelderen.** Start `rol-curriculumontwerper` met C0 + C1b. Start daarna `rol-verhelderaar` met de resulterende C2 + C0. Bij
   `FAAL`: stuur het ontwerp terug naar een **verse** `rol-curriculumontwerper` met
   C0, C1b en C3, en verhelder opnieuw. Faalt het een derde keer, stop
   dan en leg de patstelling voor aan de gebruiker.

5. **De poort - stop hier.** Toon de gebruiker: het definitieve C2 Weekontwerp, het
   C3 Verhelderingsresultaat, en de open vragen uit het ontwerp. Vraag om een C4
   Poortbesluit (`AKKOORD` / `HERZIEN` / `STOP`) volgens
   `.claude/agent-role-loop/core/contracts/C4-poortbesluit.md`, en herinner aan de
   checklist in `.claude/agent-role-loop/core/roles/vakdeskundige.md`. **Ga niet
   verder zonder een expliciet besluit. Vul C4 nooit zelf in; dat haalt de hele lus
   onderuit.** Bij `HERZIEN`: terug naar stap 4. Bij `STOP`: leg vast waarom en
   eindig.

   Herinner de gebruiker aan de vastlegplicht: een besluit dat niet in
   `curriculum/` of `conventies/` landt, is niet genomen.

6. **Schrijven.** Start `rol-auteur` met C2 + C4. Levert de auteur een
   stopvoorwaarde in plaats van een oplevering, leg die dan voor en wacht. Anders
   houd je nu C5 vast; splits die in de kern en het uitgebreide deel.

7. **Beoordelen.** Start `rol-beoordelaar-onderwijskundige`,
   `rol-beoordelaar-eerstejaars`, `rol-beoordelaar-redacteur` en
   `rol-beoordelaar-pragmaticus` **parallel**, elk met **alleen de kern** van C5.
   Geef geen enkele beoordelaar het uitgebreide deel of het oordeel van een ander.

8. **Eindoordeel.** Start `rol-hoofdredacteur` met de volledige C5 (kern +
   uitgebreid) en alle vier de C6-oordelen. Meld het resulterende C7 woordelijk aan
   de gebruiker, plus één regel samenvatting. Bij `BLOKKEER`: bied aan de
   moet-lijst terug te sturen naar een verse auteur (herhaal vanaf stap 6); ook die
   ronde vraagt het akkoord van de gebruiker.

## Regels

- Eén artefact in, één artefact uit, per subagent. Levert een subagent gebabbel om
  zijn artefact heen, houd dan alleen het artefact.
- Label elk artefact met zijn contract-ID en stap wanneer je het toont.
- Ontbreekt een verwachte subagent, zeg dan welk bestand mist uit `.claude/agents/`
  in plaats van de rol zelf te improviseren.
- De poorten van de machine draaien vóór de beoordeling, niet erin. De auteur
  levert pas op nadat `pre-commit` en `make html` groen zijn.

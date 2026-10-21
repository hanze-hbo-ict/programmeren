# Procesbesluiten

Een procesbesluit - een keuze over de werkwijze zelf - landt in de **instructie die
hij wijzigt**: [loop.md](loop.md), `.claude/commands/orc.md`, de betrokken rolprompt
in [roles/](roles/) of het betrokken contract in [contracts/](contracts/). Daar
staat de regel zelf, met haar onderbouwing. Hier staat één regel per besluit, zodat
de volgende terugvindt wat er besloten is en waar het is ingevoerd.

**Dit bestand blijft dun.** Eén regel per besluit, geen onderbouwing, geen bewijs,
geen verhaal; dat hoort in de instructie. Een register dat dat niet volhoudt, is
geen register meer.

**Inhoudelijke** besluiten horen hier niet: die landen in `curriculum/` of
`conventies/`, en een besluit dat daar niet landt is niet genomen. Dat is de harde
regel van deze repo en dit register verandert er niets aan.

Het register zelf is ingevoerd op het voorbehoud waarmee de vakdeskundige het gaf -
*"met register - denk ik?"*. Dat het besluit in de instructie landt, is gemeten
onderbouwd; het register is dat niet. Verzandt het zoals `onderzoek/bevindingen.md`,
dan is dit één bestand om te schrappen.

| Datum | Besluit | Bron | Ingevoerd in |
|---|---|---|---|
| 20 oktober 2026 | De onderzoekstrack is gesloten: `onderzoek/` is een archief, de meetregel is rol, ronde, omvang en uitkomst, en de onderzoekersrol vervalt | #406, C4 van de vakdeskundige; PR #407 | `CLAUDE.md`, `AGENTS.md`, `README.md`, `rollen/rollen.md`, `onderzoek/README.md`, `loop.md`, `principles.md`, `roles/auteur.md`, `roles/vakdeskundige.md`, `contracts/C0`, `C1`, `C4`, `commands/orc.md`; `roles/onderzoeker.md` en `agents/rol-onderzoeker.md` verwijderd |
| 20 oktober 2026 | Een procesbesluit landt in de instructie die hij wijzigt, plus één regel in dit register; inhoudelijke besluiten blijven in `curriculum/` en `conventies/` | #406, C4 van de vakdeskundige | dit bestand, `CLAUDE.md`, `rollen/rollen.md`, `loop.md`, `principles.md`, `commands/orc.md`, `contracts/C4`, `roles/vakdeskundige.md` |
| 20 oktober 2026 | Het mechanische criterium wordt niet aan een beoordelaar toegewezen: de auteur levert het bewijs, de orkestrator rekent het na | #406, C4 van de vakdeskundige | `loop.md`, de vier prompts in `roles/beoordelaar-*.md` |
| 21 oktober 2026 | Project 4 draagt uitsluitend werkitems van `programmeren`; een lus in een ander project heeft geen Statusveld en registreert op issue en PR | `ans`#16, C4 van de vakdeskundige: “dit is idd een apart project, de enige relatie met programmeren is inhoudelijk” | `commands/orc.md` |

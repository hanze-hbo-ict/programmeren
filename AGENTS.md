# Werken aan dit project met Codex

Lees `CLAUDE.md` voor de projectafspraken. De gedeelde routenorm staat in
`.claude/agent-role-loop/core/loop.md`; contracten en rolprompts staan daarnaast.
Dit bestand is alleen de Codex-ingang en bevat geen tweede procesdefinitie.

Bij een opdracht om de rollenlus over te nemen voer je de stappen uit
`.claude/commands/orc.md` uit met de beschikbare Codex-tools. Het Claude-commando
zelf is geen Codex-tool. Werkitems en overdrachten blijven op GitHub.

Start gekozen onafhankelijke rollen als subagents zonder gesprekshistorie
(`fork_turns: none`). Geef roldefinitie, exacte invoerartefacten, C1 en relevante
normvindplaatsen mee. Beoordelaars schrijven niet mee en zien geen maaktranscript;
herstelmodus krijgt alleen de expliciete herstelbijlage volgens C6. De auteur
mag zijn context behouden bij gerichte reparatie. Roltooling volgt de taak en de
werkelijke Codex-permissies; `.claude/settings.local.json` verleent hier geen rechten.

De meetregel bij een overdracht noemt rol, ronde, omvang en uitkomst; tokens en
duur horen er niet meer bij. Noem een ontbrekend gegeven als niet beschikbaar en
nooit als nul. `onderzoek/` is op 20 oktober 2026 als archief gesloten en krijgt
geen nieuwe metingen of bevindingen. De mens beslist over merge.

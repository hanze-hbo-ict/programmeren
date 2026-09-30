# Browserreproducties voor de Pyodide-watchdog

Start vanuit de repositoryroot een lokale server, bijvoorbeeld `python -m http.server`,
en open `extensions/tests/browser/pyodide-watchdog.html` in Chromium. De fixture bevat
een snelle cel, een oneindige lus, een gewone exception en `input()`. De tekst bovenaan
legt vast welke deploymentmeting ontbreekt bij een server zonder COOP/COEP.

De watchdog gebruikt centraal een celgrens van **5000 ms** en een interruptgrace van
**250 ms**. Een Chromium-timercontrole (`performance.now()`, virtuele tijd) mat
5,033 s voor de eerste grens en 5,271 s na de extra grace; daarmee is de gekozen
grace zichtbaar als ongeveer 238 ms in die run. De echte Pyodide-run moet in de
fixture apart worden gemeten: laad- en initialisatietijd horen niet bij de celgrens.

Voer daarnaast deze scenario's uit en noteer browser, headers en cacheconditie in het
issue- of PR-commentaar:

| Scenario | Verwachting |
| --- | --- |
| snelle code, daarna opnieuw | uitvoer en tweede uitvoer werken |
| oneindige lus | pagina blijft klikbaar, timeoutmelding, runtime-reset |
| eindige CPU-code onder 5 s | voltooit zonder timeout |
| exception | Python-fout zonder timeouttekst |
| `input()` beantwoorden | niet-blokkerend formulier en resultaat |
| `input()` annuleren | run stopt en runtime reset |
| open `input()` | 5 s-grens blijft lopen; timeout reset de worker |
| oude worker-event na reset | geen uitvoer/status in de nieuwe run |
| ontbrekende COOP/COEP | `crossOriginIsolated: false`; harde workerfallback |
| koude/warme cache | alleen initialisatie verschilt |

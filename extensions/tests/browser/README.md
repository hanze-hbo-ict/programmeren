# Browserreproducties voor de Pyodide-watchdog

Start vanuit de repositoryroot een lokale server, bijvoorbeeld `python -m http.server`,
en open `extensions/tests/browser/pyodide-watchdog.html` in Chromium. De fixture bevat
een snelle cel, een oneindige lus, een gewone exception en `input()`. De tekst bovenaan
legt vast welke deploymentmeting ontbreekt bij een server zonder COOP/COEP.

De watchdog gebruikt centraal een celgrens van **5000 ms** en een interruptgrace van
**250 ms**. In Chromium met de echte Pyodide-fixture gaf `performance.now()` voor
`while True: pass` **5029,8 ms** tot de timeoutmelding. Na die harde reset gaf een
nieuwe run `42\n`; een statecontrole op een verse runtime gaf `MISSING\n` voor de
variabele uit de vorige runtime. De eerdere timercontrole gaf 5,033 s voor de eerste
grens en 5,271 s inclusief de grace. Laad- en initialisatietijd horen niet bij de
celgrens.

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

De herstelrun in Chromium mat de echte lus op **5029,8 ms** tot de Nederlandse
timeoutmelding, waarna alle runknoppen weer actief waren. Een snelle vervolgrun gaf
`42\n`; een aparte verse-runtimecontrole gaf `MISSING\n` voor de eerdere variabele.
Een gewone `ValueError("voorbeeld")` gaf een `Python-fout:`-melding zonder
timeouttekst. Input is in deze controleomgeving met `crossOriginIsolated: false`
overgeslagen; daarvoor is een deploymentmeting met COOP/COEP nodig. De code ruimt de
input-overlay op via hetzelfde cleanup-pad voor resultaat, timeout, annulering en
workerfouten.

// Vanilla ES module — no build step required.
// Depends on: Pyodide (CDN), CodeMirror 6 (esm.sh CDN)
//
// Pyodide `v314.0.7` draagt CPython 3.14.2 - gemeten in zijn `pyodide-lock.json`,
// niet afgeleid uit het versienummer. Vanaf de 314-reeks draagt het versienummer de
// Python-versie; daarvóór heette dezelfde reeks 0.27 (3.12.7) en 0.28 (3.13.2). De
// repo bouwt zelf op 3.14, dus browser en build draaien nu dezelfde taalversie.
//
// De versies staan vast, tot op de patch. `@6` lost bij elk paginabezoek opnieuw op
// naar de nieuwste 6.x, en dan kan een breaking change in een minor de editor bij een
// student breken zonder dat er in deze repo iets verandert - en zonder dat een build
// faalt om het te melden. Wie ze verhoogt, doet dat in een branch en kijkt live.

const DEFAULT_PYODIDE_URL =
  "https://cdn.jsdelivr.net/pyodide/v314.0.7/full/pyodide.js";

// ---------------------------------------------------------------------------
// i18n — strings injected by Sphinx as window.SIC_I18N, English fallbacks here
// ---------------------------------------------------------------------------

const _I18N_DEFAULTS = {
  run: "Run",
  loadingPython: "Loading Python\u2026",
  running: "Running\u2026",
  inputPrompt: "Input:",
  barReady: "Python is ready \u2014 run the code below",
  btnLoading: "Loading\u2026",
  btnReady: "Ready",
  editorLoadError: "Could not load editor: ",
  pythonLoadError: "Could not load Python: ",
  pyodideLoadError: "Could not load Pyodide from ",
  timeout: "De uitvoering duurde te lang en is afgebroken. Eerdere variabelen en imports moet je opnieuw aanmaken.",
  cancelled: "De uitvoering is geannuleerd; de Python-omgeving is opnieuw gestart.",
  pythonError: "Python-fout: ",
  workerError: "De Python-omgeving kon niet worden gestart: ",
  inputCancel: "Invoer annuleren",
};

function t(key) {
  return window.SIC_I18N?.[key] ?? _I18N_DEFAULTS[key];
}

const EXECUTION_TIMEOUT_MS = 5000;
const INTERRUPT_GRACE_MS = 250;

class PageRuntime {
  #worker = null;
  #generation = 0;
  #ready = null;
  #active = null;
  #url = null;
  #interrupt = null;

  constructor() {
    this.#newWorker();
  }

  #newWorker() {
    this.#generation += 1;
    const generation = this.#generation;
    this.#worker?.terminate();
    this.#worker = new Worker(new URL("./pyodide-worker.js", import.meta.url), { type: "module" });
    this.#ready = new Promise((resolve, reject) => {
      const onMessage = (event) => {
        const message = event.data;
        if (message.generation !== generation) return;
        if (message.type === "ready") resolve(message);
        if (message.type === "load-error") reject(new Error(message.message));
      };
      this.#worker.addEventListener("message", onMessage);
      this.#worker.addEventListener("error", (event) => reject(event.error || new Error(event.message)));
    });
    this.#worker.addEventListener("message", (event) => this.#message(event.data));
    this.#worker.addEventListener("error", (event) => this.#message({
      type: "worker-error", generation, runId: this.#active?.runId, message: event.message,
    }));
    this.#worker.addEventListener("error", (event) => console.error("[interactive-code] worker error:", event.message));
  }

  start(url) {
    if (this.#url === url) return this.#ready;
    this.#url = url;
    const buffer = self.crossOriginIsolated && typeof SharedArrayBuffer !== "undefined"
      ? new SharedArrayBuffer(4) : null;
    this.#interrupt = buffer ? new Int32Array(buffer) : null;
    this.#worker.postMessage({ type: "start", generation: this.#generation, url, interruptBuffer: buffer });
    return this.#ready;
  }

  run(code, callbacks, url) {
    if (this.#active) return Promise.reject(new Error("Er draait al een cel."));
    const runId = `${this.#generation}:${++PageRuntime.nextRunId}`;
    this.#active = { runId, callbacks, timer: null, grace: null };
    return this.start(url).then(() => new Promise((resolve) => {
      this.#active.resolve = resolve;
      this.#active.timer = setTimeout(() => this.#stop("timeout"), EXECUTION_TIMEOUT_MS);
      this.#worker.postMessage({ type: "run", generation: this.#generation, runId, code });
    })).catch((error) => {
      this.#active = null;
      return { kind: "worker", message: error?.message || String(error) };
    });
  }

  cancel() { if (this.#active) this.#stop("cancelled"); }

  #message(message) {
    const active = this.#active;
    if (!active || message.generation !== this.#generation || message.runId !== active.runId) return;
    if (message.type === "stdout" || message.type === "stderr") active.callbacks.output(message.text, message.type === "stderr");
    if (message.type === "input-buffer") active.callbacks.input(message.buffer);
    if (message.type === "result") this.#finish({ kind: "result", value: message.value });
    if (message.type === "error") this.#finish({ kind: message.kind, message: message.message });
    if (message.type === "worker-error") this.#finish({ kind: "worker", message: message.message });
  }

  #finish(result) {
    const active = this.#active;
    if (!active) return;
    clearTimeout(active.timer); clearTimeout(active.grace);
    this.#active = null;
    active.resolve(result);
  }

  #stop(kind) {
    const active = this.#active;
    if (!active) return;
    if (kind === "timeout" && this.#interrupt) {
      Atomics.store(this.#interrupt, 0, 2);
      active.grace = setTimeout(() => this.#hardStop(kind), INTERRUPT_GRACE_MS);
    } else this.#hardStop(kind);
  }

  #hardStop(kind) {
    const active = this.#active;
    if (!active) return;
    this.#finish({ kind });
    this.#newWorker();
    this.#url = null;
  }

  answer(buffer, value) {
    const bytes = new TextEncoder().encode(value);
    const view = new Uint8Array(buffer, 8);
    view.set(bytes.slice(0, view.length));
    const control = new Int32Array(buffer, 0, 2);
    Atomics.store(control, 1, Math.min(bytes.length, view.length));
    Atomics.store(control, 0, 1); Atomics.notify(control, 0);
  }
}
PageRuntime.nextRunId = 0;
const pageRuntime = new PageRuntime();

// ---------------------------------------------------------------------------
// Octicon SVG icons (inline, no external dependency)
// ---------------------------------------------------------------------------

const ICON_CHECK = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="14" height="14" fill="currentColor" style="vertical-align:-2px"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"/></svg>`;

const ICON_PLAY = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="14" height="14" fill="currentColor" style="vertical-align:-2px"><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"/></svg>`;

// ---------------------------------------------------------------------------
// Shadow DOM — only the CodeMirror editor host + slot for light DOM projection
// ---------------------------------------------------------------------------

const SHADOW_STYLE = `
:host { display: block; }
.sic-editor-host .cm-editor { font-size: 0.9em; }
`;

// ---------------------------------------------------------------------------
// Light DOM HTML — inherits page (Sphinx theme) styles
// ---------------------------------------------------------------------------

function buildLightHtml() {
  return buildLightHtml._html ??= `
<div class="sic-toolbar">
  <button class="sic-btn-run" type="button">${ICON_PLAY} ${t("run")}</button>
  <span class="sic-status"></span>
</div>
<pre class="sic-output" hidden></pre>
`;
}

window.sicActivate = function (btn) {
  document.querySelectorAll(".sic-nb-static").forEach(e => e.style.display = "none");
  document.querySelectorAll(".sic-nb-interactive").forEach(e => e.style.display = "");
  // De uitvoer die bij de build is opgeslagen hoort bij de statische weergave. Laat
  // je hem staan, dan leest de student na het activeren twee antwoorden onder elkaar:
  // dat van de build en dat van zichzelf.
  document.querySelectorAll("div.cell_output").forEach(e => e.style.display = "none");
  document.dispatchEvent(new CustomEvent("sic:activate"));

  // De balk blijft staan. Tussen de klik en het moment dat er iets kan zit een
  // merkbare wachttijd - Pyodide is een WASM-runtime die per pagina één keer wordt
  // opgehaald - en juist dan weghalen wat de student net heeft aangeklikt laat hem in
  // het ongewisse: er gebeurt niets zichtbaars en er staat niets meer om op te
  // wachten. Hoe lang die wachttijd is, is hier niet gemeten en doet er niet toe;
  // het ontwerp rust erop dat zij niet nul is.
  const bar = btn.closest(".sic-bar");
  const label = btn.querySelector(".sic-btn-label");
  const icon = btn.querySelector(".sic-btn-icon");
  btn.disabled = true;
  bar.classList.add("is-loading");
  if (label) label.textContent = t("btnLoading");

  // De URL komt van de eerste cel op de pagina; ze delen er één.
  const cel = document.querySelector("interactive-code-cell");
  pageRuntime.start(cel?.dataset.pyodideUrl || DEFAULT_PYODIDE_URL).then(
    () => {
      bar.classList.remove("is-loading");
      bar.classList.add("is-ready");
      if (icon) icon.innerHTML = ICON_CHECK;
      if (label) label.textContent = t("btnReady");
      const tekst = bar.querySelector(".sic-bar-text");
      if (tekst) tekst.textContent = t("barReady");
    },
    (err) => {
      bar.classList.remove("is-loading");
      bar.classList.add("is-error");
      const tekst = bar.querySelector(".sic-bar-text");
      if (tekst) tekst.textContent = `${t("pythonLoadError")}${err.message}`;
    },
  );
};

// ---------------------------------------------------------------------------
// Web Component
// ---------------------------------------------------------------------------

class InteractiveCodeCell extends HTMLElement {
  #editor = null;
  #activateHandler = null;
  #statusEl = null;

  connectedCallback() {
    if (this.dataset.dormant === "true") {
      this.#activateHandler = () => {
        this.#activateHandler = null;
        this.#renderActive(this.textContent.trim());
      };
      document.addEventListener("sic:activate", this.#activateHandler, { once: true });
      return;
    }
    this.#renderActive(this.textContent.trim());
  }

  disconnectedCallback() {
    if (this.#activateHandler) {
      document.removeEventListener("sic:activate", this.#activateHandler);
      this.#activateHandler = null;
    }
    this.#editor?.destroy();
  }

  #renderActive(code) {
    const shadow = this.attachShadow({ mode: "open" });
    const style = document.createElement("style");
    style.textContent = SHADOW_STYLE;
    shadow.appendChild(style);
    const editorHost = document.createElement("div");
    editorHost.className = "sic-editor-host";
    shadow.appendChild(editorHost);
    // Slot projects the light DOM toolbar/output/help after the editor
    shadow.appendChild(document.createElement("slot"));

    this.innerHTML = buildLightHtml();

    this.#bindEvents();
    this.#init(code, editorHost, shadow);
  }

  // ---- Initialisation -------------------------------------------------------

  async #init(code, editorHost, shadow) {
    const pyodideUrl = this.dataset.pyodideUrl || DEFAULT_PYODIDE_URL;

    // Start Pyodide loading in the background - het is een WASM-runtime en het duurt
    // merkbaar lang. (Hier stond "~10 s"; dat getal is nooit in deze repo gemeten.)
    const pyodidePromise = pageRuntime.start(pyodideUrl);

    try {
      const [
        { EditorView, keymap, lineNumbers, drawSelection, highlightActiveLine },
        { EditorState },
        { defaultKeymap, historyKeymap, history, indentWithTab },
        { syntaxHighlighting, HighlightStyle, indentOnInput, bracketMatching, indentUnit },
        { python },
        { tags },
      ] = await Promise.all([
        import("https://esm.sh/@codemirror/view@6.43.11?deps=@codemirror/state@6.7.4"),
        import("https://esm.sh/@codemirror/state@6.7.4"),
        import("https://esm.sh/@codemirror/commands@6.11.0?deps=@codemirror/state@6.7.4,@codemirror/view@6.43.11,@codemirror/language@6.12.4,@lezer/highlight@1.2.3"),
        import("https://esm.sh/@codemirror/language@6.12.4?deps=@codemirror/state@6.7.4,@codemirror/view@6.43.11,@lezer/highlight@1.2.3"),
        import("https://esm.sh/@codemirror/lang-python@6.2.1?deps=@codemirror/state@6.7.4,@codemirror/view@6.43.11,@codemirror/language@6.12.4,@lezer/highlight@1.2.3"),
        import("https://esm.sh/@lezer/highlight@1.2.3"),
      ]);

      // Geen eigen kleuren. De editor is doorzichtig, zodat de achtergrond van de
      // cel doorschijnt - die van myst-nb in een notebook, die van de pagina daarbuiten -
      // en tekst en tokens komen uit CSS-variabelen die met het thema meedraaien.
      // Custom properties erven het schaduw-DOM in, dus dit werkt zonder de stylesheet
      // hier te herhalen. De gemarkeerde regel is een grijswaarde met alfa: die werkt
      // op een lichte én een donkere ondergrond, dus daar is geen schakelaar voor nodig.
      const inheritTheme = EditorView.theme({
        "&": { background: "transparent", color: "var(--sic-code-fg)" },
        ".cm-scroller": { background: "transparent" },
        ".cm-content": { caretColor: "var(--sic-code-fg)" },
        ".cm-gutters": {
          background: "transparent",
          color: "var(--sic-gutter-fg)",
          borderRight: "1px solid var(--sic-gutter-border)",
        },
        ".cm-activeLine": { background: "rgba(128, 128, 128, 0.08)" },
        ".cm-activeLineGutter": { background: "rgba(128, 128, 128, 0.08)" },
      });

      const themeHighlight = HighlightStyle.define([
        { tag: tags.keyword, color: "var(--sic-tok-keyword)", fontWeight: "var(--sic-tok-keyword-weight)" },
        { tag: [tags.string, tags.special(tags.string)], color: "var(--sic-tok-string)" },
        { tag: [tags.comment, tags.lineComment, tags.blockComment], color: "var(--sic-tok-comment)", fontStyle: "var(--sic-tok-comment-style)" },
        { tag: [tags.number, tags.bool, tags.null], color: "var(--sic-tok-number)" },
        { tag: [tags.function(tags.variableName), tags.function(tags.propertyName)], color: "var(--sic-tok-function)" },
        { tag: [tags.standard(tags.variableName), tags.standard(tags.name)], color: "var(--sic-tok-builtin)" },
        { tag: [tags.operator, tags.operatorKeyword], color: "var(--sic-tok-operator)" },
        { tag: tags.invalid, color: "var(--sic-tok-error)" },
      ]);

      this.#editor = new EditorView({
        state: EditorState.create({
          doc: code,
          extensions: [
            lineNumbers(), highlightActiveLine(), drawSelection(), history(),
            syntaxHighlighting(themeHighlight, { fallback: true }),
            indentOnInput(), bracketMatching(),
            // CodeMirror springt standaard twee spaties in; de code op deze pagina's
            // volgt PEP 8 en springt vier in. Zonder deze regel levert doortypen in
            // een bestaande functie een IndentationError op.
            indentUnit.of("    "),
            keymap.of([...defaultKeymap, ...historyKeymap, indentWithTab]),
            python(), inheritTheme,
          ],
        }),
        parent: editorHost,
        root: shadow,
      });

      // Sphinx' doctools.js luistert op document-niveau mee en kaapt "/" naar de
      // zoekbalk. Het slaat die afhandeling alleen over voor TEXTAREA, INPUT,
      // SELECT en BUTTON, en kijkt daarvoor naar document.activeElement - dat is
      // bij een editor in een schaduw-DOM het element <interactive-code-cell>
      // zelf. Een deling typen bracht de student dus in de zoekbalk. Toetsen die
      // in de editor vallen, blijven daarom in de editor.
      editorHost.addEventListener("keydown", (event) => event.stopPropagation());
    } catch (err) {
      this.#setStatus(`${t("editorLoadError")}${err.message}`, true);
      console.error("[interactive-code] CodeMirror init failed:", err);
      return;
    }

    this.#setStatus(t("loadingPython"));
    try {
      await pyodidePromise;
      this.#setStatus("");
    } catch (err) {
      this.#setStatus(`${t("pythonLoadError")}${err.message}`, true);
      console.error("[interactive-code] Pyodide init failed:", err);
    }
  }

  #bindEvents() {
    this.#statusEl = this.querySelector(".sic-status");

    this.querySelector(".sic-btn-run")
      .addEventListener("click", () => this.#run());
  }

  #setRunButtons(disabled) {
    document.querySelectorAll(".sic-btn-run").forEach((button) => { button.disabled = disabled; });
  }

  #askInput(buffer, outputEl) {
    return new Promise((resolve) => {
      const dialog = document.createElement("form");
      dialog.className = "sic-input-dialog";
      dialog.innerHTML = `<label>${t("inputPrompt")} <input autofocus></label><button type="submit">${t("run")}</button><button type="button" data-cancel>${t("inputCancel")}</button>`;
      outputEl.parentElement.appendChild(dialog);
      const input = dialog.querySelector("input");
      const close = (value) => { dialog.remove(); pageRuntime.answer(buffer, value); resolve(); };
      dialog.addEventListener("submit", (event) => { event.preventDefault(); close(input.value); });
      dialog.querySelector("[data-cancel]").addEventListener("click", () => { dialog.remove(); pageRuntime.cancel(); resolve(); });
      input.focus();
    });
  }

  // ---- Uitvoerplek ----------------------------------------------------------

  // Op een notebookpagina staan invoer en uitvoer naast elkaar in `div.cell`, en het
  // thema lijmt ze: zodra er iets onder de invoer hangt worden de onderste hoeken van
  // het invoerkader vierkant, en de uitvoer krijgt zijn eigen tint en rand. Schrijven
  // we daarin, dan ziet een interactieve cel eruit als elke andere notebookcel en
  // hoeven wij niets te tekenen. Dat is hoe Thebe het in Jupyter Book doet.
  //
  // Op een markdownpagina bestaat `div.cell` niet. Dan valt het terug op het `<pre>`
  // in onze eigen lichte DOM, dat wel een kader krijgt.
  #outputTarget() {
    const cell = this.closest("div.cell");
    if (!cell) return this.querySelector(".sic-output");

    let host = cell.querySelector(":scope > .sic-nb-output");
    if (!host) {
      host = document.createElement("div");
      host.className = "cell_output docutils container sic-nb-output";
      // `output stream` zonder een `.highlight`-kind is precies het patroon waar
      // myst-nb de stdout-tint en -rand op zet.
      host.innerHTML = '<div class="output stream notranslate"><pre class="sic-stream"></pre></div>';
      cell.appendChild(host);
    }
    return host.querySelector("pre");
  }

  #markError(el, isError) {
    const wrapper = el.closest(".output");
    if (wrapper) {
      wrapper.classList.toggle("stream", !isError);
      wrapper.classList.toggle("stderr", isError);
    } else {
      el.classList.toggle("is-error", isError);
    }
  }

  // ---- Code execution -------------------------------------------------------

  async #run() {
    if (!this.#editor) return;

    const code = this.#editor.state.doc.toString();
    const outputEl = this.#outputTarget();

    // De vorige uitvoer blijft staan zolang het draait. Verbergen we hem hier, dan
    // zakt het vak in en groeit het meteen daarna weer terug - bij een tweede run
    // met dezelfde uitkomst is dat puur geflikker. `sic-stale` dooft hem alleen.
    this.#setStatus(t("running"));
    this.#setRunButtons(true);
    outputEl.textContent = "";
    outputEl.classList.add("sic-stale");
    this.#markError(outputEl, false);

    try {
      const result = await pageRuntime.run(code, {
        output: (text, isError) => { outputEl.textContent += text; this.#markError(outputEl, isError); outputEl.hidden = false; },
        input: (buffer) => this.#askInput(buffer, outputEl),
      }, this.dataset.pyodideUrl || DEFAULT_PYODIDE_URL);
      if (result.kind === "result") outputEl.textContent += result.value;
      if (result.kind === "python" || result.kind === "interrupt") {
        outputEl.textContent += `${t("pythonError")}${result.message}`;
        this.#markError(outputEl, true);
      }
      if (result.kind === "timeout") {
        outputEl.textContent = t("timeout"); this.#markError(outputEl, true);
      }
      if (result.kind === "cancelled") {
        outputEl.textContent = t("cancelled"); this.#markError(outputEl, true);
      }
      if (result.kind === "load" || result.kind === "worker") {
        outputEl.textContent = `${t("workerError")}${result.message}`; this.#markError(outputEl, true);
      }
      outputEl.hidden = false;
    } catch (err) {
      outputEl.textContent = err.message;
      this.#markError(outputEl, true);
      outputEl.hidden = false;
    } finally {
      outputEl.classList.remove("sic-stale");
      this.#setRunButtons(false);
      this.#setStatus("");
    }
  }

  // ---- Helpers --------------------------------------------------------------

  #setStatus(text, isError = false) {
    this.#statusEl.textContent = text;
    this.#statusEl.classList.toggle("is-error", isError);
  }
}

customElements.define("interactive-code-cell", InteractiveCodeCell);

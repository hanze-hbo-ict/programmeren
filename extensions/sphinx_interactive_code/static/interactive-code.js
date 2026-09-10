// Vanilla ES module — no build step required.
// Depends on: Pyodide (CDN), CodeMirror 6 (esm.sh CDN)
//
// De versies staan vast, tot op de patch. `@6` lost bij elk paginabezoek opnieuw op
// naar de nieuwste 6.x, en dan kan een breaking change in een minor de editor bij een
// student breken zonder dat er in deze repo iets verandert - en zonder dat een build
// faalt om het te melden. Wie ze verhoogt, doet dat in een branch en kijkt live.

const DEFAULT_PYODIDE_URL =
  "https://cdn.jsdelivr.net/pyodide/v0.27.0/full/pyodide.js";

// ---------------------------------------------------------------------------
// i18n — strings injected by Sphinx as window.SIC_I18N, English fallbacks here
// ---------------------------------------------------------------------------

const _I18N_DEFAULTS = {
  run: "Run",
  loadingPython: "Loading Python\u2026",
  running: "Running\u2026",
  inputPrompt: "Input:",
  editorLoadError: "Could not load editor: ",
  pythonLoadError: "Could not load Python: ",
  pyodideLoadError: "Could not load Pyodide from ",
};

function t(key) {
  return window.SIC_I18N?.[key] ?? _I18N_DEFAULTS[key];
}

// ---------------------------------------------------------------------------
// Pyodide singleton — loaded once per page, shared across all cells
// ---------------------------------------------------------------------------

let _pyodidePromise = null;

function getPyodide(url) {
  if (_pyodidePromise) return _pyodidePromise;
  _pyodidePromise = new Promise((resolve, reject) => {
    const script = document.createElement("script");
    script.src = url;
    script.onload = () =>
      window.loadPyodide().then(resolve).catch(reject);
    script.onerror = () => reject(new Error(`${t("pyodideLoadError")}${url}`));
    document.head.appendChild(script);
  });
  return _pyodidePromise;
}

// ---------------------------------------------------------------------------
// Octicon SVG icons (inline, no external dependency)
// ---------------------------------------------------------------------------

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
  btn.closest(".sic-bar").remove();
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

    // Start Pyodide loading in the background — it's slow (~10 s)
    const pyodidePromise = getPyodide(pyodideUrl);

    try {
      const [
        { EditorView, keymap, lineNumbers, drawSelection, highlightActiveLine },
        { EditorState },
        { defaultKeymap, historyKeymap, history, indentWithTab },
        { syntaxHighlighting, HighlightStyle, indentOnInput, bracketMatching },
        { python },
        { tags },
      ] = await Promise.all([
        import("https://esm.sh/@codemirror/view@6.43.11"),
        import("https://esm.sh/@codemirror/state@6.7.4"),
        import("https://esm.sh/@codemirror/commands@6.11.0"),
        import("https://esm.sh/@codemirror/language@6.12.4"),
        import("https://esm.sh/@codemirror/lang-python@6.2.1"),
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
            keymap.of([...defaultKeymap, ...historyKeymap, indentWithTab]),
            python(), inheritTheme,
          ],
        }),
        parent: editorHost,
        root: shadow,
      });
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
    const pyodide = await getPyodide(this.dataset.pyodideUrl || DEFAULT_PYODIDE_URL);
    if (!pyodide || !this.#editor) return;

    const code = this.#editor.state.doc.toString();
    const outputEl = this.#outputTarget();

    // De vorige uitvoer blijft staan zolang het draait. Verbergen we hem hier, dan
    // zakt het vak in en groeit het meteen daarna weer terug - bij een tweede run
    // met dezelfde uitkomst is dat puur geflikker. `sic-stale` dooft hem alleen.
    this.#setStatus(t("running"));
    outputEl.classList.add("sic-stale");
    this.#markError(outputEl, false);

    let stdout = "";

    try {
      // `write` in plaats van `batched`: dat laatste levert pas iets op bij een
      // nieuwe regel, en de vraag van `input("Geef een getal: ")` heeft er geen.
      // Zonder dit staat de vraag nog in de buffer op het moment dat we hem als
      // label nodig hebben.
      const uit = new TextDecoder();
      const fout = new TextDecoder();
      pyodide.setStdout({ write: (buf) => { stdout += uit.decode(buf, { stream: true }); return buf.length; } });
      pyodide.setStderr({ write: (buf) => { stdout += fout.decode(buf, { stream: true }); return buf.length; } });

      // Zonder stdin valt elke input() om met een I/O-fout. De browser heeft een
      // synchrone prompt, en dat is precies wat Pyodide hier verwacht. Wat er na de
      // laatste nieuwe regel in de uitvoer staat is de vraag die het programma net
      // heeft gesteld; dat is het label. Het antwoord gaat ook de uitvoer in, anders
      // leest het transcript als een gesprek waarin de helft ontbreekt.
      pyodide.setStdin({
        stdin: () => {
          const vraag = stdout.slice(stdout.lastIndexOf("\n") + 1).trim();
          const antwoord = window.prompt(vraag || t("inputPrompt")) ?? "";
          stdout += antwoord + "\n";
          return antwoord + "\n";
        },
      });

      const result = await pyodide.runPythonAsync(code);
      const combined =
        stdout + (result !== undefined && result !== null ? String(result) : "");

      // Vanaf de eerste run blijft het uitvoervak staan, ook als er niets is
      // afgedrukt. Verbergen bij lege uitvoer laat het vak alsnog inklappen, en een
      // leeg vak zegt bovendien iets waars: het heeft gedraaid en er kwam niets uit.
      const output = combined.trim();
      outputEl.textContent = output;
      outputEl.hidden = false;
    } catch (err) {
      outputEl.textContent = err.message;
      this.#markError(outputEl, true);
      outputEl.hidden = false;
    } finally {
      pyodide.setStdout({ batched: console.log });
      pyodide.setStderr({ batched: console.error });
      pyodide.setStdin();
      outputEl.classList.remove("sic-stale");
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

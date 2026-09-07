// Vanilla ES module — no build step required.
// Depends on: Pyodide (CDN), CodeMirror 6 (esm.sh CDN)

const DEFAULT_PYODIDE_URL =
  "https://cdn.jsdelivr.net/pyodide/v0.27.0/full/pyodide.js";

// ---------------------------------------------------------------------------
// i18n — strings injected by Sphinx as window.SIC_I18N, English fallbacks here
// ---------------------------------------------------------------------------

const _I18N_DEFAULTS = {
  run: "Run",
  loadingPython: "Loading Python\u2026",
  running: "Running\u2026",
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
        { syntaxHighlighting, defaultHighlightStyle, indentOnInput, bracketMatching },
        { python },
      ] = await Promise.all([
        import("https://esm.sh/@codemirror/view@6"),
        import("https://esm.sh/@codemirror/state@6"),
        import("https://esm.sh/@codemirror/commands@6"),
        import("https://esm.sh/@codemirror/language@6"),
        import("https://esm.sh/@codemirror/lang-python@6"),
      ]);

      const whiteTheme = EditorView.theme({
        "&": { background: "#ffffff" },
        ".cm-scroller": { background: "#ffffff" },
        ".cm-gutters": { background: "#ffffff", borderRight: "1px solid #e5e7eb", color: "#9ca3af" },
        ".cm-activeLineGutter": { background: "#f0f9ff" },
        ".cm-activeLine": { background: "#f8faff" },
      });

      this.#editor = new EditorView({
        state: EditorState.create({
          doc: code,
          extensions: [
            lineNumbers(), highlightActiveLine(), drawSelection(), history(),
            syntaxHighlighting(defaultHighlightStyle, { fallback: true }),
            indentOnInput(), bracketMatching(),
            keymap.of([...defaultKeymap, ...historyKeymap, indentWithTab]),
            python(), whiteTheme,
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

  // ---- Code execution -------------------------------------------------------

  async #run() {
    const pyodide = await getPyodide(this.dataset.pyodideUrl || DEFAULT_PYODIDE_URL);
    if (!pyodide || !this.#editor) return;

    const code = this.#editor.state.doc.toString();
    const outputEl = this.querySelector(".sic-output");

    this.#setStatus(t("running"));
    outputEl.hidden = true;
    outputEl.classList.remove("is-error");

    let stdout = "";

    try {
      pyodide.setStdout({ batched: (s) => { stdout += s + "\n"; } });
      pyodide.setStderr({ batched: (s) => { stdout += s + "\n"; } });

      const result = await pyodide.runPythonAsync(code);
      const combined =
        stdout + (result !== undefined && result !== null ? String(result) : "");

      const output = combined.trim();
      outputEl.textContent = output;
      outputEl.hidden = !output;
    } catch (err) {
      outputEl.textContent = err.message;
      outputEl.classList.add("is-error");
      outputEl.hidden = false;
    } finally {
      pyodide.setStdout({ batched: console.log });
      pyodide.setStderr({ batched: console.error });
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

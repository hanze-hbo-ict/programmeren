// Vanilla ES module — no build step required.
// Depends on: Pyodide (CDN), CodeMirror 6 (esm.sh CDN), marked + DOMPurify (esm.sh CDN)

const DEFAULT_PYODIDE_URL =
  "https://cdn.jsdelivr.net/pyodide/v0.27.0/full/pyodide.js";

// ---------------------------------------------------------------------------
// i18n — strings injected by Sphinx as window.SIC_I18N, English fallbacks here
// ---------------------------------------------------------------------------

const _I18N_DEFAULTS = {
  run: "Run",
  help: "Help",
  askPlaceholder: "Ask a question\u2026",
  loadingPython: "Loading Python\u2026",
  running: "Running\u2026",
  editorLoadError: "Could not load editor: ",
  pythonLoadError: "Could not load Python: ",
  pyodideLoadError: "Could not load Pyodide from ",
  httpError: "Error: HTTP ",
  connectionError: "Connection error: ",
  error: "Error: ",
};

function t(key) {
  return window.SIC_I18N?.[key] ?? _I18N_DEFAULTS[key];
}

import { marked } from "https://esm.sh/marked@15";
import DOMPurify from "https://esm.sh/dompurify@3";

// Restrict markdown to inline formatting + lists only — no headings, hr, images, tables.
marked.use({
  renderer: {
    heading({ text }) { return `<p><strong>${text}</strong></p>\n`; },
    hr() { return ""; },
    blockquote({ body }) { return body; },
    image() { return ""; },
    table() { return ""; },
  },
});

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
const ICON_QUESTION = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="14" height="14" fill="currentColor" style="vertical-align:-2px"><path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Zm8-6.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM6.92 6.085h.001a.749.749 0 1 1-1.342-.67c.169-.339.436-.701.849-.977C6.845 4.16 7.369 4 8 4a2.756 2.756 0 0 1 1.637.525c.503.377.863.965.863 1.725 0 .448-.115.83-.329 1.15-.205.307-.47.513-.692.662-.109.073-.22.138-.313.195l-.006.004a6.24 6.24 0 0 0-.26.17.748.748 0 0 0-.095.085V9a.75.75 0 0 1-1.5 0v-.5c0-.325.182-.6.428-.75.14-.085.293-.173.438-.257.11-.065.212-.124.301-.186.173-.115.23-.191.253-.228a.47.47 0 0 0 .054-.241c0-.186-.077-.343-.247-.469A1.255 1.255 0 0 0 8 5.5c-.384 0-.618.115-.74.198-.136.09-.225.2-.34.387ZM8.5 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z"/></svg>`;

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
  <button class="sic-btn-help" type="button">${ICON_QUESTION} ${t("help")}</button>
  <span class="sic-status"></span>
</div>
<pre class="sic-output" hidden></pre>
<div class="sic-help" hidden>
  <div class="sic-messages" role="log" aria-live="polite"></div>
  <form class="sic-input-form">
    <input class="sic-help-input" type="text" placeholder="${t("askPlaceholder")}" autocomplete="off">
  </form>
</div>
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
  #messages = [];
  #lastRunContext = "";
  #abortController = null;
  #activateHandler = null;
  #activeReader = null;
  #msgsEl = null;
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
    if (this.#abortController) this.#abortController.abort();
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

    if (this.dataset.coachOpen === "true") {
      this.querySelector(".sic-help").hidden = false;
      this.querySelector(".sic-btn-help").classList.add("is-active");
    }

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
    this.#msgsEl = this.querySelector(".sic-messages");
    this.#statusEl = this.querySelector(".sic-status");

    this.querySelector(".sic-btn-run")
      .addEventListener("click", () => this.#run());

    this.querySelector(".sic-btn-help")
      .addEventListener("click", () => {
        const helpEl = this.querySelector(".sic-help");
        const btnEl = this.querySelector(".sic-btn-help");
        helpEl.hidden = !helpEl.hidden;
        btnEl.classList.toggle("is-active", !helpEl.hidden);
      });

    this.querySelector(".sic-input-form")
      .addEventListener("submit", (e) => {
        e.preventDefault();
        this.#sendMessage();
      });
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

      this.#lastRunContext = combined.trim();
      outputEl.textContent = this.#lastRunContext;
      outputEl.hidden = !this.#lastRunContext;
    } catch (err) {
      this.#lastRunContext = err.message;
      outputEl.textContent = err.message;
      outputEl.classList.add("is-error");
      outputEl.hidden = false;
    } finally {
      pyodide.setStdout({ batched: console.log });
      pyodide.setStderr({ batched: console.error });
      this.#setStatus("");
    }
  }

  // ---- LLM chat -------------------------------------------------------------

  async #sendMessage() {
    const input = this.querySelector(".sic-help-input");
    const text = input.value.trim();
    if (!text || !this.#editor) return;

    input.value = "";
    this.#messages.push({ role: "user", content: text });
    this.#addMessage("user", text);

    const assistantEl = this.#addMessage("assistant", "\u2026");

    if (this.#abortController) {
      this.#abortController.abort();
      this.#activeReader?.cancel();
    }
    this.#abortController = new AbortController();

    const solution = this.dataset.solution ? atob(this.dataset.solution) : "";
    let assistantText = "";

    try {
      const response = await fetch(
        `${this.dataset.proxyUrl || "/llm-proxy"}/chat`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          signal: this.#abortController.signal,
          body: JSON.stringify({
            messages: this.#messages,
            code: this.#editor.state.doc.toString(),
            output: this.#lastRunContext,
            assignment: this.dataset.assignment || "",
            solution,
          }),
        }
      );

      if (!response.ok) {
        assistantEl.textContent = `${t("httpError")}${response.status}`;
        return;
      }

      assistantEl.textContent = "";
      const reader = response.body.getReader();
      this.#activeReader = reader;
      const decoder = new TextDecoder();
      let renderPending = false;

      outer: while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        for (const line of decoder.decode(value, { stream: true }).split("\n")) {
          if (!line.startsWith("data:")) continue;
          const raw = line.slice(5).trim();
          if (raw === "[DONE]") break outer;

          const payload = JSON.parse(raw);
          if (payload.error) {
            assistantEl.textContent = `${t("error")}${payload.error}`;
            return;
          }
          assistantText += payload.text;
          if (!renderPending) {
            renderPending = true;
            requestAnimationFrame(() => {
              assistantEl.innerHTML = this.#md(assistantText);
              this.#scrollMessages();
              renderPending = false;
            });
          }
        }
      }

      assistantEl.innerHTML = this.#md(assistantText);
      this.#scrollMessages();
    } catch (err) {
      if (err.name !== "AbortError") {
        assistantEl.textContent = `${t("connectionError")}${err.message}`;
        return;
      }
    } finally {
      this.#activeReader = null;
    }

    if (assistantText) this.#messages.push({ role: "assistant", content: assistantText });
  }

  // ---- Helpers --------------------------------------------------------------

  #md(text) {
    return DOMPurify.sanitize(marked.parse(text));
  }

  #addMessage(role, text) {
    const el = document.createElement("div");
    el.className = `sic-message sic-message--${role}`;
    el.textContent = text;
    this.#msgsEl.appendChild(el);
    this.#scrollMessages();
    return el;
  }

  #scrollMessages() {
    this.#msgsEl.scrollTop = this.#msgsEl.scrollHeight;
  }

  #setStatus(text, isError = false) {
    this.#statusEl.textContent = text;
    this.#statusEl.classList.toggle("is-error", isError);
  }
}

customElements.define("interactive-code-cell", InteractiveCodeCell);

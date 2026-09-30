/* Pyodide runtime worker.  The page owns the watchdog; this worker only owns
 * the runtime and speaks a small, generation/run tagged protocol. */

let pyodide = null;
let interruptBuffer = null;
let generation = 0;

function send(type, runId, payload = {}) {
  self.postMessage({ type, generation, runId, ...payload });
}

function textDecoder() {
  return new TextDecoder();
}

async function start(message) {
  generation = message.generation;
  try {
    // pyodide.js is a classic bundled script without an ES export. Evaluate it
    // in the worker global so this file can remain a module worker.
    const source = await fetch(message.url).then((response) => {
      if (!response.ok) throw new Error(`Pyodide laden mislukt (HTTP ${response.status})`);
      return response.text();
    });
    const loadPyodide = new Function(`${source}\nreturn loadPyodide;`)();
    if (!loadPyodide) throw new Error("loadPyodide ontbreekt in de geladen runtime");
    pyodide = await loadPyodide({ indexURL: message.url.replace(/pyodide\.js$/, "") });
    if (message.interruptBuffer) {
      interruptBuffer = new Int32Array(message.interruptBuffer);
      pyodide.setInterruptBuffer(interruptBuffer);
    }
    send("ready", null, { interrupt: Boolean(interruptBuffer) });
  } catch (error) {
    send("load-error", null, { message: error?.message || String(error) });
  }
}

async function run(message) {
  const runId = message.runId;
  if (!pyodide) {
    send("error", runId, { kind: "load", message: "Python is nog niet geladen." });
    return;
  }
  const stdout = textDecoder();
  const stderr = textDecoder();
  pyodide.setStdout({
    write: (buffer) => {
      send("stdout", runId, { text: stdout.decode(buffer, { stream: true }) });
      return buffer.length;
    },
  });
  pyodide.setStderr({
    write: (buffer) => {
      send("stderr", runId, { text: stderr.decode(buffer, { stream: true }) });
      return buffer.length;
    },
  });
  pyodide.setStdin({
    stdin: () => {
      if (typeof SharedArrayBuffer === "undefined") {
        throw new Error("input() vereist een browser met SharedArrayBuffer");
      }
      let inputBuffer;
      try { inputBuffer = new SharedArrayBuffer(65540); }
      catch { throw new Error("input() vereist cross-origin isolation"); }
      const control = new Int32Array(inputBuffer, 0, 2);
      const bytes = new Uint8Array(inputBuffer, 8);
      // The main thread writes UTF-8 into the shared buffer and wakes us. This
      // blocks only the worker, so the page watchdog keeps running during input.
      self.postMessage({ type: "input-buffer", generation, runId, buffer: inputBuffer });
      Atomics.wait(control, 0, 0);
      return new TextDecoder().decode(bytes.slice(0, Atomics.load(control, 1)));
    },
  });
  try {
    const result = await pyodide.runPythonAsync(message.code);
    send("result", runId, {
      value: result === undefined || result === null ? "" : String(result),
    });
  } catch (error) {
    send("error", runId, {
      kind: error?.name === "KeyboardInterrupt" ? "interrupt" : "python",
      message: error?.message || String(error),
    });
  } finally {
    pyodide.setStdout();
    pyodide.setStderr();
    pyodide.setStdin();
  }
}

self.onmessage = (event) => {
  const message = event.data;
  if (message.type === "start") start(message);
  if (message.type === "run") run(message);
};

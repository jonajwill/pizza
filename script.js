'use strict';

const $ = (selector, scope = document) => scope.querySelector(selector);
const $$ = (selector, scope = document) => Array.from(scope.querySelectorAll(selector));

/* ==========================================================================
   Pyodide: loads the real .py files once, then runs their functions.
   No cooking math lives in this file — it's all in the three .py files.
   ========================================================================== */
let pyodideReady = null;

function getPyodide() {
  if (!pyodideReady) {
    pyodideReady = loadPyodide().then(async (pyodide) => {
      await loadPyFile(pyodide, 'marmeladenRechner.py', /^marmeladenRechner\(/m);
      await loadPyFile(pyodide, 'pizzateigRechner.py', /^pizza\(/m);
      await loadPyFile(pyodide, 'zutatenRechner.py', /^zutaten\(/m);
      return pyodide;
    });
  }
  return pyodideReady;
}

// Fetches a .py file and runs everything above its trailing demo call
// (e.g. `marmeladenRechner(fruchtmenge)` at the bottom of the file),
// so the original function definition ends up in Pyodide unchanged.
async function loadPyFile(pyodide, path, trailingCall) {
  const source = await (await fetch(path)).text();
  const match = source.match(trailingCall);
  await pyodide.runPythonAsync(match ? source.slice(0, match.index) : source);
}

// Sets `vars` as Python globals, runs `call` (a call to a function from one
// of the .py files) and returns whatever it printed, as a string.
async function runPython(vars, call) {
  const pyodide = await getPyodide();
  Object.entries(vars).forEach(([name, value]) => pyodide.globals.set(name, value));
  return pyodide.runPythonAsync(
    'import io, contextlib\n' +
    '_buf = io.StringIO()\n' +
    'with contextlib.redirect_stdout(_buf):\n' +
    `    ${call}\n` +
    '_buf.getvalue()'
  );
}

function showLoading(el) {
  el.innerHTML = '<p class="empty">wird berechnet …</p>';
}

function showOutput(el, text) {
  el.innerHTML = `<pre>${text.trim()}</pre>`;
}

function showError(el, err) {
  el.innerHTML = `<p class="empty">Fehler: ${err.message}</p>`;
}

/* ==========================================================================
   Tabs
   ========================================================================== */
function initTabs() {
  const tabButtons = $$('.tab-btn');

  tabButtons.forEach((btn) => {
    btn.addEventListener('click', () => activateTab(btn.dataset.tab));
  });

  function activateTab(id) {
    tabButtons.forEach((btn) => {
      const isActive = btn.dataset.tab === id;
      btn.classList.toggle('active', isActive);
      btn.setAttribute('aria-selected', String(isActive));
    });

    $$('.panel').forEach((panel) => {
      panel.hidden = panel.id !== id;
    });
  }
}

/* ==========================================================================
   Marmeladenrechner  →  marmeladenRechner.py
   ========================================================================== */
function initMarmelade() {
  const fruchtInput = $('#m-frucht');
  const output = $('#m-output');

  async function update() {
    const fruchtmenge = parseFloat(fruchtInput.value) || 0;
    showLoading(output);
    try {
      const text = await runPython({ _fruchtmenge: fruchtmenge }, 'marmeladenRechner(_fruchtmenge)');
      showOutput(output, text);
    } catch (err) {
      showError(output, err);
    }
  }

  fruchtInput.addEventListener('input', update);
  update();
}

/* ==========================================================================
   Pizzateigrechner  →  pizzateigRechner.py
   ========================================================================== */
function initPizzateig() {
  const artSelect = $('#p-art');
  const anzahlInput = $('#p-anzahl');
  const gewichtInput = $('#p-gewicht');
  const hydrationInput = $('#p-hydration');
  const poolishanteilInput = $('#p-poolishanteil');
  const bigaanteilInput = $('#p-bigaanteil');
  const modusButtons = $$('#p-modus-field button');
  const poolishField = $('#p-poolish-field');
  const bigaField = $('#p-biga-field');
  const modusField = $('#p-modus-field');
  const output = $('#p-output');

  let modus = 'an';

  modusButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
      modusButtons.forEach((b) => {
        b.classList.remove('active');
        b.setAttribute('aria-checked', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-checked', 'true');
      modus = btn.dataset.mode;
      update();
    });
  });

  function updateVisibleFields(art) {
    poolishField.hidden = art !== 'poolish';
    bigaField.hidden = !(art === 'biga' || art === 'biga capvin');
    modusField.hidden = art === 'biga';
  }

  async function update() {
    const art = artSelect.value;
    updateVisibleFields(art);

    const anzahl = parseFloat(anzahlInput.value) || 0;
    const gewicht = parseFloat(gewichtInput.value) || 0;
    const h = (parseFloat(hydrationInput.value) || 0) / 100;
    const p = (parseFloat(poolishanteilInput.value) || 0) / 100;
    const b = (parseFloat(bigaanteilInput.value) || 0) / 100;

    $('#p-hydration-val').textContent = `${Math.round(h * 100)} %`;
    $('#p-poolishanteil-val').textContent = `${Math.round(p * 100)} %`;
    $('#p-bigaanteil-val').textContent = `${Math.round(b * 100)} %`;

    showLoading(output);
    try {
      const text = await runPython(
        {
          _teigart: art,
          _anzahl: anzahl,
          _gewicht: gewicht,
          _hydration: h,
          _poolishanteil: p,
          _bigaanteil: b,
          _modus: modus,
        },
        'pizza(_teigart, _anzahl, _gewicht, _hydration, _poolishanteil, _bigaanteil, _modus)'
      );
      showOutput(output, text);
    } catch (err) {
      showError(output, err);
    }
  }

  [artSelect, anzahlInput, gewichtInput, hydrationInput, poolishanteilInput, bigaanteilInput].forEach((el) => {
    el.addEventListener('input', update);
    el.addEventListener('change', update);
  });

  update();
}

/* ==========================================================================
   Zutatenrechner  →  zutatenRechner.py
   ========================================================================== */
// Order matches the parameter order of zutaten() in zutatenRechner.py exactly.
const PIZZA_DEFS = [
  ['marinara', 'Marinara', 0],
  ['margherita', 'Margherita', 2],
  ['funghi', 'Funghi', 1],
  ['salame', 'Salame vegetariano', 1],
  ['funghiesalame', 'Funghi e salame', 0],
  ['caprese', 'Caprese', 1],
  ['cacioepepe', 'Cacio e pepe', 0],
  ['verdura', 'Verdura', 0],
  ['quattrostagioni', 'Quattro stagioni', 0],
  ['rossa', 'Rossa', 2],
  ['parmigiana', 'Parmigiana', 1],
  ['caprino', 'Caprino', 1],
  ['stracciatella', 'Stracciatella di burrata', 1],
  ['cipolle', 'Cipolle caramellate', 0],
];

function buildZutatenForm() {
  const form = $('#zutaten-form');
  const fragment = document.createDocumentFragment();

  PIZZA_DEFS.forEach(([key, label, defaultValue]) => {
    const field = document.createElement('div');
    field.className = 'zut-field';
    field.innerHTML = `
      <label for="z-${key}">${label}</label>
      <input type="number" inputmode="numeric" id="z-${key}" name="${key}" value="${defaultValue}" min="0" step="1">
    `;
    fragment.appendChild(field);
  });

  form.appendChild(fragment);
}

function initZutaten() {
  buildZutatenForm();
  const form = $('#zutaten-form');
  const output = $('#z-output');

  async function update() {
    const setupVars = {};
    PIZZA_DEFS.forEach(([key]) => {
      setupVars[`_${key}`] = parseFloat($(`#z-${key}`).value) || 0;
    });
    const callExpr = `zutaten(${PIZZA_DEFS.map(([key]) => `_${key}`).join(', ')})`;

    showLoading(output);
    try {
      const text = await runPython(setupVars, callExpr);
      showOutput(output, text);
    } catch (err) {
      showError(output, err);
    }
  }

  form.addEventListener('input', update);
  update();
}

/* ==========================================================================
   Init
   ========================================================================== */
document.addEventListener('DOMContentLoaded', () => {
  initTabs();
  initMarmelade();
  initPizzateig();
  initZutaten();
});
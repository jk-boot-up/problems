/*
 * Step-by-step algorithm animator with spoken narration.
 *
 * A problem page defines `trace(A)` and a global PROBLEM object (title, complexity...).
 * The tracer registers one or more scenarios:
 *     A.scenario('Example 1', 'nums = [1,2,3]', () => { ... A.step('narration', A.arr(...)) ... });
 * Each scenario automatically gets an intro step and a closing "complexity" step.
 * Narration uses the browser's built-in Web Speech API (speechSynthesis), so no audio files are needed.
 */
(function () {
  const P = window.PROBLEM || {};
  const scenarios = [];
  let frames = [];
  const clone = v => (v === undefined ? undefined : JSON.parse(JSON.stringify(v, (k, x) => x instanceof Set ? [...x] : x instanceof Map ? Object.fromEntries(x) : x)));
  const toMap = o => {
    const m = new Map();
    if (!o) return m;
    const list = Array.isArray(o) ? o : Object.entries(o);
    for (const [k, v] of list) {
      const key = String(k);
      m.set(key, m.has(key) ? m.get(key) + ',' + v : String(v));
    }
    return m;
  };
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const show = v => (v === null || v === undefined ? '' : typeof v === 'object' ? JSON.stringify(v) : String(v));
  const cls = s => (s || '').split(',').join(' ');
  let nodeSeq = 100000;
  /* Java-compatible hashCode for numbers, single characters and strings. */
  function jhash(k) {
    if (typeof k === 'number' && Number.isInteger(k)) return k | 0;
    if (typeof k === 'boolean') return k ? 1231 : 1237;
    const s = typeof k === 'string' ? k : JSON.stringify(k);
    if (typeof k === 'string' && s.length === 1) return s.charCodeAt(0);
    let h = 0;
    for (let i = 0; i < s.length; i++) h = (Math.imul(31, h) + s.charCodeAt(i)) | 0;
    return h;
  }

  /* ---------- tree helpers ---------- */
  function mkTree(arr) {
    if (!arr.length || arr[0] === null) return null;
    const nodes = arr.map((v, i) => (v === null ? null : { val: v, left: null, right: null, id: i }));
    let q = [nodes[0]], i = 1;
    while (q.length && i < nodes.length) {
      const n = q.shift();
      if (i < nodes.length) { n.left = nodes[i++]; if (n.left) q.push(n.left); }
      if (i < nodes.length) { n.right = nodes[i++]; if (n.right) q.push(n.right); }
    }
    return nodes[0];
  }
  function layoutTree(root, nextPtrs) {
    const out = [], edges = [], nexts = [];
    let x = 0;
    const seen = new Set();
    (function walk(n, d, p) {
      if (!n || seen.has(n)) return;
      seen.add(n);
      walk(n.left, d + 1, n);
      out.push({ id: n.id, val: n.val, x: x++, y: d });
      if (p) edges.push([p.id, n.id]);
      walk(n.right, d + 1, n);
      if (nextPtrs && n.next) nexts.push([n.id, n.next.id]);
    })(root, 0, null);
    return { nodes: out, edges, nexts };
  }

  /* ---------- tracer API ---------- */
  const A = {
    scenario(title, desc, fn) { scenarios.push({ title, desc: desc || '', fn }); },
    step(say, ...comps) { frames.push({ say: String(say), comps: comps.flat().filter(Boolean) }); },
    arr(label, values, o = {}) { return { t: 'arr', label, values: clone([...values]), hl: [...toMap(o.hl)], ptr: [...toMap(o.ptr)], range: o.range, noIdx: !!o.noIdx }; },
    chars(label, str, o = {}) { return A.arr(label, [...str], o); },
    grid(label, m, o = {}) { return { t: 'grid', label, m: clone(m), hl: [...toMap(o.hl)] }; },
    list(label, values, o = {}) { return { t: 'list', label, values: clone([...values]), hl: [...toMap(o.hl)], ptr: [...toMap(o.ptr)], note: o.note }; },
    tree(label, root, o = {}) { return { t: 'tree', label, L: layoutTree(root, o.next), hl: [...toMap(o.hl)] }; },
    graph(label, nodes, edges, o = {}) { return { t: 'graph', label, nodes: clone(nodes), edges: clone(edges), hl: [...toMap(o.hl)], directed: !!o.directed }; },
    vars(obj, label = 'Variables') { return { t: 'vars', label, obj: clone(obj) }; },
    map(label, m) {
      const obj = {};
      if (m instanceof Map) for (const [k, v] of m) obj[show(k)] = v instanceof Set ? [...v] : v;
      else if (m instanceof Set) [...m].forEach(k => (obj[show(k)] = '✓'));
      else Object.assign(obj, m);
      return { t: 'vars', label, obj: clone(obj) };
    },
    /* Hash table internals: the same bucket index MyHashMap computes (Java hashCode, h ^ h>>>16, & (capacity-1)). */
    hashTable(label, m, o = {}) {
      const entries = m instanceof Map ? [...m] : m instanceof Set ? [...m].map(k => [k, undefined]) : Object.entries(m);
      let cap = o.capacity || 8;
      while (entries.length > cap * 0.75) cap *= 2;
      const rows = Array.from({ length: cap }, () => []);
      entries.forEach(([k, v]) => { const h = jhash(k); rows[(h ^ (h >>> 16)) & (cap - 1)].unshift({ k: show(k), v: v === undefined ? undefined : show(v instanceof Set ? [...v] : v), hl: o.hl && o.hl === k }); });
      return { t: 'hash', label, rows };
    },
    stack(label, items, o = {}) { return { t: 'stack', label, items: clone([...items]), top: o.top !== false }; },
    text(label, s, c = '') { return { t: 'text', label, s: String(s), cls: c }; },
    mkTree,
    node(val) { return { val, left: null, right: null, id: nodeSeq++ }; }
  };

  /* ---------- complexity chart ---------- */
  const CLASSES = [
    ['1', 'O(1)', n => 1], ['log', 'O(log n)', n => Math.log2(n)], ['n', 'O(n)', n => n],
    ['nlogn', 'O(n log n)', n => n * Math.log2(n)], ['n2', 'O(n²)', n => n * n], ['exp', 'O(2ⁿ)', n => 2 ** n]
  ];
  function chartSvg(me) {
    const W = 360, H = 200, pad = 28, maxN = 12, maxY = 36;
    let s = `<svg class="chart" width="100%" viewBox="0 0 ${W} ${H}" role="img" aria-label="growth curves">`;
    s += `<line class="ax" x1="${pad}" y1="${H - pad}" x2="${W - 8}" y2="${H - pad}"/><line class="ax" x1="${pad}" y1="8" x2="${pad}" y2="${H - pad}"/>`;
    s += `<text x="${W - 70}" y="${H - 10}">input size n</text><text x="4" y="14">ops</text>`;
    CLASSES.forEach(([k, label, f]) => {
      const pts = [];
      for (let n = 1; n <= maxN; n += 0.25) { const y = f(n); if (y > maxY) break; pts.push([pad + (n / maxN) * (W - pad - 12), H - pad - (y / maxY) * (H - pad - 12)]); }
      const last = pts[pts.length - 1];
      s += `<polyline class="curve ${k === me ? 'me' : ''}" points="${pts.map(p => p.map(v => v.toFixed(1)).join(',')).join(' ')}"/>`;
      s += `<text class="${k === me ? 'me' : ''}" x="${k === 'exp' ? last[0] - 44 : Math.min(last[0] + 4, W - 64)}" y="${Math.max(last[1] - 6, 12)}">${label}</text>`;
    });
    return s + '</svg>';
  }
  function scaleHtml(me) { return '<div class="scale">' + CLASSES.map(([k, l]) => `<span class="${k === me ? 'me' : ''}">${l}</span>`).join('') + '</div>'; }
  function cxCard(kind) {
    const big = kind === 'time' ? P.time : P.space, why = kind === 'time' ? P.timeWhy : P.spaceWhy, k = kind === 'time' ? P.tc : P.sc;
    return `<div class="card cxcard"><h3>${kind === 'time' ? '⏱ Time' : '🧠 Extra space'}</h3><div class="big">${esc(big || '?')}</div><p class="why">${esc(why || '')}</p>${chartSvg(k)}${scaleHtml(k)}</div>`;
  }

  /* ---------- renderers ---------- */
  function cellsRow(c, kind, prev) {
    const hl = new Map(c.hl), ptr = new Map(c.ptr);
    let h = '<div class="row">';
    c.values.forEach((v, i) => {
      const k = String(i);
      let cl = cls(hl.get(k));
      if (c.range && (i < c.range[0] || i > c.range[1])) cl += ' dim';
      else if (c.range) cl += ' win';
      if (prev && prev.values && i < prev.values.length && show(prev.values[i]) !== show(v)) cl += ' chg';
      if (kind === 'list' && i > 0) h += '<span class="arrow">→</span>';
      const p = ptr.get(k) || '';
      h += `<div class="cellwrap"><div class="ptr ${p ? 'has' : ''}">${esc(p)}</div><div class="cell ${cl}">${esc(show(v))}</div>${c.noIdx || kind === 'list' ? '<div class="idx">&nbsp;</div>' : `<div class="idx">${i}</div>`}</div>`;
    });
    if (kind === 'list') h += `<span class="arrow">→ ${esc(c.note || 'null')}</span>`;
    if (!c.values.length) h += '<div class="cell dim">∅</div>';
    return h + '</div>';
  }
  function gridHtml(c, prev) {
    const hl = new Map(c.hl);
    const cols = Math.max(1, ...c.m.map(r => r.length));
    let h = `<div class="grid" style="grid-template-columns:repeat(${cols},auto)">`;
    c.m.forEach((r, i) => r.forEach((v, j) => {
      const ch = prev && prev.m && prev.m[i] && show(prev.m[i][j]) !== show(v) ? ' chg' : '';
      const hc = cls(hl.get(i + ',' + j));
      h += `<div class="cell ${hc}${ch}${!hc && show(v) === '' ? ' empty' : ''}">${esc(show(v))}</div>`;
    }));
    return h + '</div>';
  }
  function treeSvg(c) {
    const { nodes, edges, nexts } = c.L, hl = new Map(c.hl);
    if (!nodes.length) return '<div class="textc">(empty tree)</div>';
    const W = 54, H = 66, pos = new Map();
    nodes.forEach(n => pos.set(n.id, [n.x * W + 30, n.y * H + 30]));
    const w = nodes.length * W + 20, ht = (Math.max(...nodes.map(n => n.y)) + 1) * H + 10;
    let s = `<svg width="${w}" height="${ht}" viewBox="0 0 ${w} ${ht}"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z" fill="var(--alt)"/></marker></defs>`;
    edges.forEach(([a, b]) => { const p = pos.get(a), q = pos.get(b); const ec = hl.get(String(b)); s += `<line class="edge ${ec && /ok|cur|sel/.test(ec) && hl.get(String(a)) ? cls(ec) : ''}" x1="${p[0]}" y1="${p[1]}" x2="${q[0]}" y2="${q[1]}"/>`; });
    (nexts || []).forEach(([a, b]) => { const p = pos.get(a), q = pos.get(b); if (p && q) s += `<path class="nextp" marker-end="url(#ah)" d="M${p[0] + 18},${p[1] - 8} Q${(p[0] + q[0]) / 2},${p[1] - 34} ${q[0] - 18},${q[1] - 8}"/>`; });
    nodes.forEach(n => { const [x, y] = pos.get(n.id); s += `<circle class="${cls(hl.get(String(n.id)))}" cx="${x}" cy="${y}" r="20"/><text x="${x}" y="${y}">${esc(n.val)}</text>`; });
    return s + '</svg>';
  }
  function graphSvg(c) {
    const hl = new Map(c.hl), N = c.nodes.length, R = Math.max(90, N * 16), pos = new Map();
    const w = 2 * R + 80, h = 2 * R + 60;
    c.nodes.forEach((n, i) => {
      const a = (2 * Math.PI * i) / N - Math.PI / 2;
      pos.set(String(n.id), n.x !== undefined ? [n.x, n.y] : [w / 2 + R * Math.cos(a), h / 2 + R * Math.sin(a)]);
    });
    let s = `<svg width="${w}" height="${h}"><defs><marker id="ga" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" fill="var(--mut)"/></marker></defs>`;
    c.edges.forEach(e => {
      const [a, b, lab, ec] = e, p = pos.get(String(a)), q = pos.get(String(b));
      if (!p || !q) return;
      const dx = q[0] - p[0], dy = q[1] - p[1], L = Math.hypot(dx, dy) || 1, ux = dx / L, uy = dy / L;
      const x1 = p[0] + ux * 23, y1 = p[1] + uy * 23, x2 = q[0] - ux * 23, y2 = q[1] - uy * 23;
      s += `<line class="edge ${ec || ''}" x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" ${c.directed ? 'marker-end="url(#ga)"' : ''}/>`;
      if (lab !== undefined && lab !== null && lab !== '') s += `<text class="elabel" x="${(x1 + x2) / 2 + uy * 10}" y="${(y1 + y2) / 2 - ux * 10}">${esc(lab)}</text>`;
    });
    c.nodes.forEach(n => { const [x, y] = pos.get(String(n.id)); s += `<circle class="${cls(hl.get(String(n.id)))}" cx="${x}" cy="${y}" r="21"/><text x="${x}" y="${y}">${esc(n.label ?? n.id)}</text>`; });
    return s + '</svg>';
  }
  function render(c, prev) {
    let body = '';
    switch (c.t) {
      case 'arr': body = cellsRow(c, 'arr', prev); break;
      case 'list': body = cellsRow(c, 'list', prev); break;
      case 'grid': body = gridHtml(c, prev); break;
      case 'tree': body = treeSvg(c); break;
      case 'graph': body = graphSvg(c); break;
      case 'vars': body = '<div class="vars">' + (Object.keys(c.obj).length ? Object.entries(c.obj).map(([k, v]) => `<div class="kv ${prev && prev.obj && show(prev.obj[k]) !== show(v) ? 'chg' : ''}"><b>${esc(k)}</b> = ${esc(show(v))}</div>`).join('') : '<div class="kv">(empty)</div>') + '</div>'; break;
      case 'stack': body = '<div class="stack">' + c.items.map((v, i) => `<div class="cell ${i === c.items.length - 1 && c.top ? 'cur' : ''}">${esc(show(v))}</div>`).join('') + '</div>'; break;
      case 'text': body = `<div class="textc ${c.cls}">${esc(c.s)}</div>`; break;
      case 'hash': body = '<div class="htable">' + c.rows.map((chain, i) => `<div class="hcol"><div class="hidx">[${i}]</div>${chain.length ? chain.map((e, j) => `${j ? '<div class="hdown">↓</div>' : ''}<div class="cell hentry ${e.hl ? 'cur' : ''}">${esc(e.k)}${e.v !== undefined ? `<small>→ ${esc(e.v)}</small>` : ''}</div>`).join('') : '<div class="hnull">·</div>'}</div>`).join('') + `</div><div class="hnote">${c.rows.length} buckets · bucket = (h ^ h>>>16) & ${c.rows.length - 1} · collisions chain downwards</div>`; break;
      case 'cx': body = `<div class="cxstage">${cxCard('time')}${cxCard('space')}</div>`; break;
      case 'intro': body = `<div class="idea">${esc(c.s)}</div>`; break;
    }
    return `<div class="comp">${c.label ? `<div class="comp-label">${esc(c.label)}</div>` : ''}${body}</div>`;
  }

  /* ---------- build scenarios ---------- */
  function build(sc) {
    frames = [];
    try { sc.fn(); } catch (e) { frames.push({ say: 'Tracer error: ' + e.message, comps: [] }); console.error(e); }
    const first = frames[0] ? frames[0].comps : [];
    frames.unshift({ say: `Scenario: ${sc.title}. ${sc.desc}`.trim(), comps: [{ t: 'intro', label: 'Scenario · ' + sc.title, s: (sc.desc ? sc.desc + '\n' : '') + (P.idea || '') }, ...first], kind: 'intro' });
    frames.push({ say: `Complexity. Time is ${spoken(P.time)}: ${P.timeWhy || ''} Extra space is ${spoken(P.space)}: ${P.spaceWhy || ''}`, comps: [{ t: 'cx', label: 'Cost of this solution' }], kind: 'cx' });
    return frames;
  }
  const spoken = s => String(s || '').replace(/O\(/g, 'big O of ').replace(/\)/g, '').replace(/\^2|²/g, ' squared').replace(/·|\*/g, ' times ').replace(/\blog\b/g, 'log');

  /* ---------- player ---------- */
  let cur = 0, playing = false, token = 0, voiceOn = true, rate = 1, voice = null, timer = null, scIdx = 0;
  const $ = id => document.getElementById(id);
  const synth = 'speechSynthesis' in window ? window.speechSynthesis : null;

  function compPrev(i, c) {
    if (i <= 0) return null;
    return frames[i - 1].comps.find(p => p.t === c.t && p.label === c.label) || null;
  }
  function draw(i) {
    cur = Math.max(0, Math.min(frames.length - 1, i));
    const f = frames[cur];
    $('stage').innerHTML = f.comps.map(c => render(c, compPrev(cur, c))).join('');
    $('say').textContent = f.say;
    $('counter').textContent = `Step ${cur + 1} / ${frames.length}`;
    [...$('timeline').children].forEach((el, k) => (el.className = (k < cur ? 'done' : k === cur ? 'now' : '') + (frames[k].kind === 'cx' ? ' cx' : '')));
  }
  function stopAudio() { token++; clearTimeout(timer); if (synth) synth.cancel(); $('narr').classList.remove('speaking'); }
  function speak(text, done) {
    const my = token;
    const est = Math.max(1500, text.split(/\s+/).length * 400) / rate;
    const finish = () => { if (my !== token) return; $('narr').classList.remove('speaking'); clearTimeout(timer); timer = setTimeout(() => my === token && done && done(), 450 / rate); };
    if (voiceOn && synth) {
      const u = new SpeechSynthesisUtterance(text);
      u.rate = rate; u.pitch = 1.05; if (voice) { u.voice = voice; u.lang = voice.lang; }
      let ended = false;
      u.onstart = () => my === token && $('narr').classList.add('speaking');
      u.onend = u.onerror = () => { if (!ended) { ended = true; finish(); } };
      synth.speak(u);
      timer = setTimeout(() => { if (!ended) { ended = true; finish(); } }, est * 2.5 + 3000); // safety net
    } else timer = setTimeout(finish, est);
  }
  function loop() {
    if (!playing) return;
    speak(frames[cur].say, () => {
      if (!playing) return;
      if (cur < frames.length - 1) { draw(cur + 1); loop(); } else setPlaying(false);
    });
  }
  function setPlaying(p) {
    playing = p;
    $('play').textContent = p ? '⏸ Pause' : '▶ Play';
    stopAudio();
    if (p) { if (cur >= frames.length - 1) draw(0); loop(); }
  }
  function go(i) { const was = playing; stopAudio(); draw(i); if (was) loop(); else if (voiceOn) speak(frames[cur].say, null); }
  function selectScenario(i) {
    setPlaying(false);
    scIdx = i;
    build(scenarios[i]);
    [...$('scen').children].forEach((b, k) => b.classList.toggle('on', k === i));
    $('timeline').innerHTML = frames.map(() => '<i></i>').join('');
    [...$('timeline').children].forEach((el, k) => (el.onclick = () => go(k)));
    draw(0);
  }
  function tab(name) {
    document.querySelectorAll('nav.tabs button').forEach(b => b.classList.toggle('on', b.dataset.tab === name));
    document.querySelectorAll('.tab').forEach(t => t.classList.toggle('on', t.id === 'tab-' + name));
    if (name !== 'walk') setPlaying(false);
  }
  function setTheme(t) {
    document.documentElement.dataset.theme = t;
    try { localStorage.setItem('algo-theme', t); } catch (e) { }
    document.querySelectorAll('.themes button').forEach(b => b.classList.toggle('on', b.dataset.theme === t));
  }
  /* Prefer a female English voice: "Amy" first, then well-known female system voices. */
  const FEMALE = [/\bamy\b/i, /uk english female/i, /\b(aria|jenny|libby|sonia|zira|hazel|susan|emma|ava|allison|samantha|serena|kate|karen|moira|tessa|fiona|victoria|joanna|salli|kimberly|olivia|natasha|clara)\b/i, /female/i, /woman/i];
  function rankVoice(v) {
    const i = FEMALE.findIndex(re => re.test(v.name));
    return (i < 0 ? 50 : i) + (/en[-_]GB/i.test(v.lang) ? 0 : 0.5);
  }
  function loadVoices() {
    if (!synth) return;
    const vs = synth.getVoices().filter(v => /^en/i.test(v.lang)).sort((a, b) => rankVoice(a) - rankVoice(b));
    const sel = $('voice');
    sel.innerHTML = vs.map((v, i) => `<option value="${i}">${esc(v.name)}${rankVoice(v) < 50 ? ' ♀' : ''}</option>`).join('') || '<option>default voice</option>';
    let saved = null;
    try { saved = localStorage.getItem('algo-voice'); } catch (e) { }
    voice = vs.find(v => v.name === saved) || vs[0] || null;
    if (voice) sel.value = String(vs.indexOf(voice));
    sel.onchange = () => { voice = vs[+sel.value] || null; try { localStorage.setItem('algo-voice', voice ? voice.name : ''); } catch (e) { } };
  }
  function setVoiceOn(on) {
    voiceOn = on;
    const b = $('voiceOn');
    b.textContent = on ? '🔊 Narration on' : '🔇 Narration off';
    b.classList.toggle('on', on);
    b.setAttribute('aria-pressed', String(on));
    $('voice').disabled = !on;
    try { localStorage.setItem('algo-narration', on ? 'on' : 'off'); } catch (e) { }
    if (!on && synth) { synth.cancel(); $('narr').classList.remove('speaking'); }
  }
  function highlightJava(src) {
    return esc(src)
      .replace(/(\/\/[^\n]*|\/\*[\s\S]*?\*\/)/g, '<span class="cm">$1</span>')
      .replace(/\b(public|private|protected|static|final|class|record|interface|new|return|if|else|for|while|do|int|long|double|boolean|char|void|var|null|true|false|this|import|package|break|continue|switch|case|default|throw|throws|try|catch|extends|implements|String)\b(?![^<]*<\/span>)/g, '<span class="kw">$1</span>');
  }

  window.addEventListener('DOMContentLoaded', () => {
    let saved = 'dark';
    try { saved = localStorage.getItem('algo-theme') || (matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark'); } catch (e) { }
    setTheme(saved);
    document.querySelectorAll('.themes button').forEach(b => (b.onclick = () => setTheme(b.dataset.theme)));
    document.querySelectorAll('nav.tabs button').forEach(b => (b.onclick = () => tab(b.dataset.tab)));
    document.querySelectorAll('[data-goto]').forEach(b => (b.onclick = () => tab(b.dataset.goto)));
    $('javacode').innerHTML = highlightJava($('javacode').textContent);
    $('cx-cards').innerHTML = cxCard('time') + cxCard('space');

    try { window.trace(A); } catch (e) { console.error(e); }
    if (!scenarios.length && frames.length) { const fr = frames; scenarios.push({ title: 'Example', desc: '', fn: () => frames.push(...fr) }); }
    if (!scenarios.length) scenarios.push({ title: 'Example', desc: '', fn: () => A.step('No steps.') });
    $('scen').innerHTML = scenarios.map((s, i) => `<button title="${esc(s.desc)}">${i + 1}. ${esc(s.title)}<small>${esc(s.desc)}</small></button>`).join('');
    [...$('scen').children].forEach((b, i) => (b.onclick = () => selectScenario(i)));
    $('scount').textContent = scenarios.length;
    window.__scenarios = scenarios.map((s, i) => () => { selectScenario(i); return frames; });

    $('play').onclick = () => setPlaying(!playing);
    $('prev').onclick = () => go(cur - 1);
    $('next').onclick = () => go(cur + 1);
    $('first').onclick = () => go(0);
    $('last').onclick = () => go(frames.length - 1);
    $('speed').onchange = e => (rate = +e.target.value);
    $('voiceOn').onclick = () => setVoiceOn(!voiceOn);
    document.addEventListener('keydown', e => {
      if (/SELECT|INPUT|TEXTAREA/.test(e.target.tagName) || !$('tab-walk').classList.contains('on')) return;
      if (e.key === ' ') { e.preventDefault(); setPlaying(!playing); }
      if (e.key === 'ArrowRight') go(cur + 1);
      if (e.key === 'ArrowLeft') go(cur - 1);
      if (e.key === 'n' || e.key === 'N') setVoiceOn(!voiceOn);
      if (/^[1-9]$/.test(e.key) && +e.key <= scenarios.length) selectScenario(+e.key - 1);
    });
    let pref = 'on';
    try { pref = localStorage.getItem('algo-narration') || 'on'; } catch (e) { }
    if (synth) { loadVoices(); synth.onvoiceschanged = loadVoices; setVoiceOn(pref === 'on'); }
    else { setVoiceOn(false); $('voiceOn').disabled = true; $('voiceOn').title = 'This browser has no speech synthesis'; }
    selectScenario(0);
  });
})();

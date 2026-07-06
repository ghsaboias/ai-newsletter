#!/usr/bin/env node
// headless-render.js — render/eval de chart via Chromium headless + CDP (Linux/Pi).
// Sem dependências npm: usa o WebSocket nativo do Node 22+.
//
// uso: headless-render.js render <chart.html> <out.png>
//      headless-render.js eval   <chart.html> '<expressão JS>'
//
// Espelha o fluxo do render.sh macOS (browser-tools): DSF=2 fixado ANTES do load
// (o Chart.js rasteriza o canvas no DPR do load), viewport 800×altura-do-card,
// screenshot recortado no #capture via clip do CDP (dispensa ImageMagick).

import { spawn } from 'node:child_process';
import { mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const [mode, htmlPath, extra] = process.argv.slice(2);
if (!['render', 'eval'].includes(mode) || !htmlPath || !extra) {
  console.error('uso: headless-render.js render <chart.html> <out.png>\n     headless-render.js eval <chart.html> <expressão>');
  process.exit(1);
}
const url = htmlPath.startsWith('file://') ? htmlPath : 'file://' + htmlPath;

const CHROMIUM = process.env.CHROMIUM_BIN || 'chromium';
const profile = mkdtempSync(join(tmpdir(), 'chart-render-'));
const chrome = spawn(CHROMIUM, [
  '--headless',
  '--remote-debugging-port=0',
  '--remote-allow-origins=*',
  `--user-data-dir=${profile}`,
  '--no-first-run',
  '--hide-scrollbars',
  '--force-color-profile=srgb',
  '--window-size=800,1000',
  'about:blank',
], { stdio: ['ignore', 'ignore', 'pipe'] });

function cleanup() {
  try { chrome.kill('SIGKILL'); } catch {}
  try { rmSync(profile, { recursive: true, force: true }); } catch {}
}
process.on('exit', cleanup);
const die = (msg) => { console.error('ERRO: ' + msg); process.exit(1); };

// 1) porta do DevTools via stderr ("DevTools listening on ws://127.0.0.1:PORT/...")
const port = await new Promise((resolve, reject) => {
  let buf = '';
  const t = setTimeout(() => reject(new Error('timeout esperando o DevTools do chromium')), 30000);
  chrome.stderr.on('data', (d) => {
    buf += d;
    const m = buf.match(/DevTools listening on ws:\/\/127\.0\.0\.1:(\d+)\//);
    if (m) { clearTimeout(t); resolve(m[1]); }
  });
  chrome.on('exit', () => { clearTimeout(t); reject(new Error('chromium saiu antes de abrir o DevTools')); });
}).catch((e) => die(e.message));

// 2) websocket da aba inicial
const targets = await fetch(`http://127.0.0.1:${port}/json/list`).then((r) => r.json());
const page = targets.find((t) => t.type === 'page');
if (!page) die('nenhuma aba encontrada no chromium headless');

const ws = new WebSocket(page.webSocketDebuggerUrl);
await new Promise((res, rej) => { ws.onopen = res; ws.onerror = () => rej(die('websocket CDP falhou')); });

let msgId = 0;
const pending = new Map();
const events = [];
ws.onmessage = (ev) => {
  const msg = JSON.parse(ev.data);
  if (msg.id !== undefined) {
    const p = pending.get(msg.id);
    pending.delete(msg.id);
    msg.error ? p.reject(new Error(msg.error.message)) : p.resolve(msg.result);
  } else {
    events.push(msg);
  }
};
function cdp(method, params = {}) {
  const id = ++msgId;
  ws.send(JSON.stringify({ id, method, params }));
  return new Promise((resolve, reject) => pending.set(id, { resolve, reject }));
}
async function evalJS(expression) {
  const r = await cdp('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true });
  if (r.exceptionDetails) throw new Error('eval: ' + (r.exceptionDetails.exception?.description || r.exceptionDetails.text));
  return r.result.value;
}
const waitEvent = (name, ms = 30000) => new Promise((resolve, reject) => {
  const t0 = Date.now();
  (function poll() {
    const i = events.findIndex((e) => e.method === name);
    if (i >= 0) return resolve(events.splice(i, 1)[0]);
    if (Date.now() - t0 > ms) return reject(new Error(`timeout esperando ${name}`));
    setTimeout(poll, 50);
  })();
});

// 3) DSF=2 ANTES do load, depois navega e espera o Chart.js desenhar
await cdp('Page.enable');
await cdp('Emulation.setDeviceMetricsOverride', { width: 800, height: 1000, deviceScaleFactor: 2, mobile: false });
await cdp('Page.navigate', { url });
await waitEvent('Page.loadEventFired').catch((e) => die(e.message));
await evalJS('document.fonts.ready.then(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))))');

if (mode === 'eval') {
  try {
    console.log(JSON.stringify(await evalJS(extra)));
  } catch (e) { die(e.message); }
  process.exit(0);
}

// 4) viewport na altura do card (+76 = padding do body), re-layout, rect final
const H = await evalJS("Math.ceil(document.getElementById('capture').getBoundingClientRect().height)+76");
if (!Number.isInteger(H) || H <= 0) die(`altura inválida (${H}) — chart não renderizou? rode de novo`);
await cdp('Emulation.setDeviceMetricsOverride', { width: 800, height: H, deviceScaleFactor: 2, mobile: false });
await evalJS('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');

// guarda anti-borrão (mesma do render.sh macOS)
const crisp = await evalJS("(function(){var c=document.querySelector('canvas');return (window.devicePixelRatio===2 && c && c.width===c.clientWidth*2) ? 'ok' : ('dpr='+window.devicePixelRatio+' buf='+(c?c.width+'x'+c.height:'?')+' css='+(c?c.clientWidth+'x'+c.clientHeight:'?'));})()");
if (crisp !== 'ok') console.error(`aviso: render não-retina (${crisp}) — a região do gráfico pode sair pixelada`);

const rect = await evalJS("(function(){var r=document.getElementById('capture').getBoundingClientRect();return {x:Math.round(r.left),y:Math.round(r.top),w:Math.round(r.width),h:Math.round(r.height)};})()");

// 5) screenshot recortado no #capture (clip em px CSS; DSF=2 dá o 2× físico)
const shot = await cdp('Page.captureScreenshot', {
  format: 'png',
  clip: { x: rect.x, y: rect.y, width: rect.w, height: rect.h, scale: 1 },
});
const png = Buffer.from(shot.data, 'base64');
writeFileSync(extra, png);

// dimensões reais do PNG (IHDR: width/height em big-endian nos offsets 16/20)
const outW = png.readUInt32BE(16), outH = png.readUInt32BE(20);
if (outW !== rect.w * 2) console.error(`aviso: PNG saiu ${outW}px de largura (esperado ${rect.w * 2})`);
console.log(`ok: ${extra}  (card recortado: ${outW}×${outH}px)`);
process.exit(0);

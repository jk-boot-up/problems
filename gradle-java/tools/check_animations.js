// Opens each animation page in headless Chromium, runs every scenario and renders every step,
// and fails on tracer or page errors. Usage: node tools/check_animations.js <project-dir>...
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  let failed = 0;
  for (const dir of process.argv.slice(2)) {
    const page = await browser.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    page.on('console', m => m.type() === 'error' && errors.push(m.text()));
    await page.goto('file://' + path.resolve(dir, 'animation/index.html'));
    const res = await page.evaluate(() => {
      document.querySelector('[data-tab="walk"]').click();
      return (window.__scenarios || []).map(run => {
        const fr = run();
        for (let i = 0; i < fr.length; i++) document.getElementById('next').click();
        const err = fr.find(f => f.say.startsWith('Tracer error'));
        return { n: fr.length, err: err ? err.say : '' };
      });
    });
    const bad = res.filter(r => r.n < 4 || r.err);
    const cx = await page.evaluate(() => [PROBLEM.time, PROBLEM.space, PROBLEM.tc, PROBLEM.sc].join(' '));
    const ok = res.length > 0 && !bad.length && !errors.length && !cx.includes('?');
    if (!ok) failed++;
    console.log(`${ok ? 'OK  ' : 'FAIL'} ${path.basename(dir)} scenarios=${res.length} steps=${res.map(r => r.n).join('/')} cx=[${cx}] ${errors.join(' | ')} ${bad.map(b => b.err).join(' | ')}`);
    await page.close();
  }
  await browser.close();
  process.exit(failed ? 1 : 0);
})();

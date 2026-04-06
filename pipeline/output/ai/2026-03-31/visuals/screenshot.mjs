import { chromium } from 'playwright';
import { resolve } from 'path';

const htmlFile = resolve(process.argv[2]);
const outFile = resolve(process.argv[3]);

const browser = await chromium.launch();
const context = await browser.newContext({
  viewport: { width: 1000, height: 800 },
  deviceScaleFactor: 3,
});
const page = await context.newPage();

await page.goto(`file://${htmlFile}`, { waitUntil: 'networkidle' });
await page.waitForTimeout(500); // let fonts settle

const card = await page.locator('#capture');
await card.screenshot({ path: outFile, type: 'png' });

await browser.close();
console.log(`Saved: ${outFile}`);

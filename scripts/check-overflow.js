#!/usr/bin/env node
/**
 * check-overflow.js — Detect slides where content overflows the visible area.
 *
 * Usage:
 *   node check-overflow.js                  # check all slides.html files
 *   node check-overflow.js path/to/slides.html  # check one file
 *
 * Marp renders each slide as a <section> with a fixed height.
 * If scrollHeight > clientHeight, the slide overflows.
 */

const puppeteer = require("puppeteer");
const path = require("path");
const fs = require("fs");
const { glob } = require("puppeteer").default ? {} : {};

async function checkFile(browser, filePath) {
  const absPath = path.resolve(filePath);
  if (!fs.existsSync(absPath)) {
    console.error(`  File not found: ${absPath}`);
    return [];
  }

  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });
  await page.goto(`file://${absPath}`, { waitUntil: "networkidle0" });

  const overflows = await page.evaluate(() => {
    const sections = document.querySelectorAll("section");
    const results = [];
    sections.forEach((section, i) => {
      const sh = section.scrollHeight;
      const ch = section.clientHeight;
      if (sh > ch + 2) { // 2px tolerance
        results.push({
          slide: i + 1,
          scrollHeight: sh,
          clientHeight: ch,
          overflow: sh - ch,
          // grab first 80 chars of text content as a hint
          preview: section.textContent.trim().substring(0, 80).replace(/\s+/g, " "),
        });
      }
    });
    return results;
  });

  await page.close();
  return overflows;
}

async function main() {
  const args = process.argv.slice(2);
  let files;

  if (args.length > 0) {
    files = args;
  } else {
    // Find all slides.html files
    const { execSync } = require("child_process");
    const output = execSync(
      'find . -name "slides.html" -not -path "./node_modules/*"',
      { encoding: "utf-8" }
    );
    files = output.trim().split("\n").filter(Boolean).sort();
  }

  if (files.length === 0) {
    console.error("No slides.html files found. Run: marp --html <slides.md>");
    process.exit(1);
  }

  const browser = await puppeteer.launch({
    headless: "new",
    executablePath: process.env.CHROMIUM_PATH || "/home/agent/.cache/puppeteer/chrome/linux_arm-145.0.7632.76/chrome-linux64/chrome",
    args: ["--no-sandbox", "--disable-setuid-sandbox", "--disable-gpu"],
  });

  let totalOverflows = 0;

  for (const file of files) {
    const rel = path.relative(".", file);
    const overflows = await checkFile(browser, file);

    if (overflows.length === 0) {
      console.log(`✓ ${rel} — no overflow`);
    } else {
      console.log(`✗ ${rel} — ${overflows.length} slides overflow:`);
      for (const o of overflows) {
        console.log(
          `    slide ${o.slide}: ${o.overflow}px over (${o.scrollHeight}px content in ${o.clientHeight}px slide)`
        );
        console.log(`      "${o.preview}..."`);
      }
      totalOverflows += overflows.length;
    }
  }

  await browser.close();

  console.log(`\n${"=".repeat(50)}`);
  if (totalOverflows === 0) {
    console.log("All slides fit within their bounds.");
  } else {
    console.log(`${totalOverflows} slides overflow across ${files.length} decks.`);
  }

  process.exit(totalOverflows > 0 ? 1 : 0);
}

main().catch((err) => {
  console.error(err);
  process.exit(2);
});

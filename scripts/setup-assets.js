#!/usr/bin/env node

/**
 * Cross-platform asset copier.
 * Copies Bootstrap CSS/JS, font files and Bootstrap Icons
 * from node_modules into the Django static directories so
 * we don’t rely on any external CDN.
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const STATIC_DIR = path.join(ROOT, 'parco_verismo', 'static');

const tasks = {
  bootstrap: () => {
    copyFile(
      path.join(ROOT, 'node_modules', 'bootstrap', 'dist', 'css', 'bootstrap.min.css'),
      path.join(STATIC_DIR, 'css', 'bootstrap.min.css')
    );
    copyFile(
      path.join(ROOT, 'node_modules', 'bootstrap', 'dist', 'js', 'bootstrap.bundle.min.js'),
      path.join(STATIC_DIR, 'js', 'bootstrap.bundle.min.js')
    );
  },
  fonts: () => {
    // Fonts are committed directly into parco_verismo/static/fonts/
    // No automatic copying from node_modules for Montserrat/Inter.
  },
  icons: () => {
    copyDir(
      path.join(ROOT, 'node_modules', 'bootstrap-icons', 'font'),
      path.join(STATIC_DIR, 'fonts', 'bootstrap-icons')
    );
  },
};

function ensureDir(dirPath) {
  fs.mkdirSync(dirPath, { recursive: true });
}

function copyFile(src, dest) {
  ensureDir(path.dirname(dest));
  fs.copyFileSync(src, dest);
  console.log(`Copied ${relativePath(src)} -> ${relativePath(dest)}`);
}

function copyDir(srcDir, destDir) {
  ensureDir(destDir);
  fs.readdirSync(srcDir).forEach(entry => {
    const srcPath = path.join(srcDir, entry);
    const destPath = path.join(destDir, entry);
    const stat = fs.statSync(srcPath);
    if (stat.isDirectory()) {
      copyDir(srcPath, destPath);
    } else {
      copyFile(srcPath, destPath);
    }
  });
}

function relativePath(p) {
  return path.relative(ROOT, p);
}

function run(selectedTask) {
  if (selectedTask) {
    const fn = tasks[selectedTask];
    if (!fn) {
      console.error(`Unknown task "${selectedTask}". Available tasks: ${Object.keys(tasks).join(', ')}`);
      process.exit(1);
    }
    fn();
  } else {
    Object.values(tasks).forEach(fn => fn());
  }
  console.log('Assets copied successfully.');
}

const args = process.argv.slice(2);
const onlyIndex = args.indexOf('--only');
if (onlyIndex !== -1 && args[onlyIndex + 1]) {
  run(args[onlyIndex + 1]);
} else {
  run();
}


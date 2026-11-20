/**
 * GoalZone – main.js
 * Shared utilities: active nav, mobile menu, scroll animations, API fetch, helpers.
 */

// ── API fetch helper ─────────────────────────────────────────────────────────
const API_BASE_URL = "";

async function fetchAPI(path) {
  const res = await fetch(`${API_BASE_URL}${path}`);

  if (!res.ok) {
    throw new Error(`HTTP ${res.status}`);
  }

  return res.json();
}
// ── Date formatter ───────────────────────────────────────────────────────────
function formatDate(dateStr) {
  return new Date(dateStr + 'T00:00:00').toLocaleDateString('en-GB', {
    day: 'numeric', month: 'short', year: 'numeric',
  });
}

// ── Active nav link ──────────────────────────────────────────────────────────
function setActiveNav() {
  const page = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link').forEach(a => {
    if (a.getAttribute('href') === page || (page === '' && a.getAttribute('href') === 'index.html')) {
      a.classList.add('active');
    }
  });
}

// ── Hamburger toggle ─────────────────────────────────────────────────────────
function initHamburger() {
  const btn = document.getElementById('hamburger');
  const menu = document.getElementById('mobile-menu');
  if (!btn || !menu) return;
  btn.addEventListener('click', () => {
    btn.classList.toggle('open');
    menu.classList.toggle('open');
  });
  menu.querySelectorAll('.nav-link').forEach(a =>
    a.addEventListener('click', () => { btn.classList.remove('open'); menu.classList.remove('open'); })
  );
}

// ── Scroll fade-up animations ────────────────────────────────────────────────
function initScrollAnimations() {
  const els = document.querySelectorAll('.fade-up:not(.visible)');
  if (!els.length) return;
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => entry.target.classList.add('visible'), i * 60);
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  els.forEach(el => io.observe(el));
}

// ── Loading / error helpers ──────────────────────────────────────────────────
function showLoading(id) {
  const el = document.getElementById(id);
  if (el) el.innerHTML = `<div class="loading"><div class="spinner"></div><span>Loading…</span></div>`;
}

function showError(id, msg) {
  const el = document.getElementById(id);
  if (el) el.innerHTML = `<div class="empty-state"><div class="empty-icon">⚠️</div><p>${msg}</p></div>`;
}

// ── Init ─────────────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  setActiveNav();
  initHamburger();
  initScrollAnimations();
});

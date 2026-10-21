from pathlib import Path

root = Path(r"c:\Users\user\Desktop\Portfolio's\College website")
(root / "css").mkdir(parents=True, exist_ok=True)
(root / "js").mkdir(parents=True, exist_ok=True)
(root / "assets" / "images").mkdir(parents=True, exist_ok=True)
(root / "assets" / "icons").mkdir(parents=True, exist_ok=True)

css = '''
:root {
  --navy: #0f213d;
  --navy-deep: #091a30;
  --navy-soft: #1e3858;
  --gold: #c9a76a;
  --gold-soft: #e7d2a5;
  --ivory: #f7f3ee;
  --white: #ffffff;
  --slate: #56657a;
  --slate-soft: #dfe6ee;
  --shadow: 0 18px 38px rgba(11, 20, 34, 0.12);
  --radius: 20px;
  --radius-small: 12px;
  --container: 1180px;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: "Segoe UI", Arial, sans-serif;
  background: var(--ivory);
  color: var(--navy);
  line-height: 1.6;
}
img { max-width: 100%; display: block; }
a { color: inherit; text-decoration: none; }
button, input, select, textarea { font: inherit; }
.container {
  width: min(var(--container), calc(100% - 2rem));
  margin: 0 auto;
}
img { vertical-align: middle; }

h1, h2, h3, h4 {
  margin: 0 0 0.75rem;
  line-height: 1.12;
  color: var(--navy-deep);
  font-weight: 700;
}

p { margin: 0 0 1rem; color: var(--slate); }

.eyebrow {
  display: inline-block;
  margin-bottom: 1rem;
  padding: 0.45rem 0.8rem;
  border-radius: 999px;
  background: rgba(201, 167, 106, 0.12);
  color: var(--navy);
  font-size: 0.75rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-weight: 700;
}

.page-hero {
  padding: 7.5rem 0 4rem;
  background: linear-gradient(180deg, rgba(15, 33, 61, 0.95), rgba(15, 33, 61, 0.82)),
    url('https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=1400&q=80') center/cover no-repeat;
  color: var(--white);
}
.page-hero h1 { color: var(--white); font-size: clamp(2.2rem, 4vw, 4rem); }
.page-hero p { color: rgba(255,255,255,0.8); max-width: 700px; }
.page-hero .breadcrumbs { font-size: 0.9rem; color: rgba(255,255,255,0.8); }

.section { padding: 6rem 0; }
.section-header {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  align-items: end;
  margin-bottom: 2rem;
}
.section-header h2 { font-size: clamp(2rem, 3vw, 2.8rem); }
.section-header p { max-width: 600px; }

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  font-weight: 600;
  border: 1px solid transparent;
  border-radius: 999px;
  padding: 0.9rem 1.5rem;
  transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
  cursor: pointer;
}
.btn:hover,
.btn:focus-visible {
  transform: translateY(-2px);
  box-shadow: 0 12px 20px rgba(15, 33, 61, 0.14);
}
.btn-primary {
  background: var(--gold);
  color: var(--navy-deep);
}
.btn-secondary {
  background: transparent;
  color: var(--navy);
  border-color: rgba(15, 33, 61, 0.2);
}
.btn-neutral {
  background: var(--navy);
  color: var(--white);
}

.site-announcement {
  background: var(--navy);
  color: rgba(255,255,255,0.8);
  padding: 0.9rem 0;
  font-size: 0.92rem;
  text-align: center;
}
.site-announcement strong { color: var(--white); }

.site-header {
  position: sticky;
  top: 0;
  z-index: 50;
  background: rgba(247, 243, 238, 0.92);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(15, 33, 61, 0.08);
}
.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.25rem;
  min-height: 84px;
}
.brand {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  font-weight: 800;
  letter-spacing: 0.02em;
}
.brand-mark {
  width: 52px;
  height: 52px;
  border-radius: 16px;
  background: linear-gradient(135deg, var(--navy), #183867);
  color: var(--white);
  display: grid;
  place-items: center;
  font-size: 1.3rem;
  font-weight: 900;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.12);
}
.brand-text small {
  display: block;
  font-size: 0.68rem;
  color: var(--slate);
  letter-spacing: 0.12em;
  text-transform: uppercase;
}
.brand-text strong { font-size: 1rem; }

.primary-nav {
  display: flex;
  align-items: center;
  gap: 0.35rem;
}
.nav-item { position: relative; }
.nav-item > a,
.nav-item > button {
  background: transparent;
  border: none;
  color: var(--navy);
  font-weight: 600;
  padding: 0.8rem 0.95rem;
  border-radius: 10px;
  cursor: pointer;
}
.nav-item > a:hover,
.nav-item > a:focus-visible,
.nav-item > button:hover,
.nav-item > button:focus-visible,
.nav-item.is-active > a {
  background: rgba(15, 33, 61, 0.05);
  outline: none;
}
.nav-item.is-active > a { color: var(--navy-deep); }
.dropdown-menu {
  position: absolute;
  top: calc(100% + 0.6rem);
  left: 0;
  min-width: 220px;
  background: var(--white);
  border-radius: 16px;
  box-shadow: var(--shadow);
  border: 1px solid rgba(15, 33, 61, 0.08);
  opacity: 0;
  visibility: hidden;
  transform: translateY(8px);
  transition: all 0.2s ease;
  padding: 0.7rem;
}
.nav-item.open .dropdown-menu,
.nav-item:focus-within .dropdown-menu {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}
.dropdown-menu a {
  display: block;
  padding: 0.7rem 0.8rem;
  border-radius: 10px;
  color: var(--navy);
}
.dropdown-menu a:hover,
.dropdown-menu a:focus-visible { background: rgba(15, 33, 61, 0.05); }

.header-actions { display: flex; align-items: center; gap: 0.8rem; }
.mobile-toggle {
  display: none;
  background: transparent;
  border: 1px solid rgba(15, 33, 61, 0.12);
  width: 46px;
  height: 46px;
  border-radius: 12px;
  cursor: pointer;
}

.hero {
  padding: 5.5rem 0 4rem;
  background: linear-gradient(90deg, rgba(247,243,238,0.96) 0%, rgba(247,243,238,0.9) 45%, rgba(247,243,238,0.7) 100%);
}
.hero-grid {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 2rem;
  align-items: center;
}
.hero-copy h1 {
  font-size: clamp(2.7rem, 5vw, 5rem);
  letter-spacing: -0.06em;
  margin-bottom: 1.2rem;
}
.hero-copy .lead {
  font-size: 1.1rem;
  max-width: 620px;
  color: var(--slate);
}
.hero-actions { display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 2rem; }
.hero-stats {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
  margin-top: 2.5rem;
}
.stat-box {
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(15, 33, 61, 0.06);
  border-radius: 20px;
  padding: 1rem 1.2rem;
}
.stat-box strong {
  display: block;
  font-size: 1.8rem;
  color: var(--navy-deep);
}

.hero-visual { position: relative; }
.hero-image-wrap {
  position: relative;
  border-radius: 28px;
  overflow: hidden;
  box-shadow: var(--shadow);
}
.hero-image-wrap img {
  width: 100%;
  height: 620px;
  object-fit: cover;
}
.hero-badge {
  position: absolute;
  right: 1.2rem;
  bottom: 1.2rem;
  background: rgba(255,255,255,0.9);
  border: 1px solid rgba(15,33,61,0.08);
  border-radius: 18px;
  padding: 1rem 1.2rem;
  max-width: 250px;
  box-shadow: var(--shadow);
}
.hero-badge strong { display: block; font-size: 1.3rem; }

.card-grid,
.program-grid,
.feature-grid,
.facility-grid,
.events-grid,
.news-grid,
.testimonials-grid,
.leadership-grid,
.value-grid,
.timeline,
.contact-grid,
.form-grid {
  display: grid;
  gap: 1.5rem;
}
.program-grid,
.feature-grid,
.facility-grid,
.events-grid,
.news-grid,
.testimonials-grid,
.leadership-grid,
.value-grid,
.contact-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.card {
  background: var(--white);
  border: 1px solid rgba(15, 33, 61, 0.08);
  border-radius: var(--radius);
  padding: 1.5rem;
  box-shadow: 0 12px 25px rgba(15, 33, 61, 0.04);
}
.card img {
  border-radius: 16px;
  width: 100%;
  height: 220px;
  object-fit: cover;
  margin-bottom: 1rem;
}
.program-card .meta,
.news-card .meta,
.event-card .meta { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.8rem; }
.meta span {
  display: inline-flex;
  align-items: center;
  background: rgba(201, 167, 106, 0.12);
  padding: 0.38rem 0.7rem;
  border-radius: 999px;
  font-size: 0.72rem;
  color: var(--navy);
  font-weight: 700;
}

.feature-icon,
.info-icon {
  width: 58px;
  height: 58px;
  border-radius: 16px;
  display: grid;
  place-items: center;
  background: rgba(201, 167, 106, 0.15);
  color: var(--navy);
  margin-bottom: 1rem;
  font-size: 1.6rem;
}
.feature-grid .card,
.value-grid .card {
  min-height: 100%;
}

.highlight-band {
  background: var(--navy);
  color: var(--white);
  padding: 2.2rem 0;
}
.highlight-band .band-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}
.highlight-band strong { font-size: clamp(1.5rem, 2vw, 2.4rem); }

.process-grid,
.stats-panel {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1.25rem;
}
.step-box {
  background: var(--white);
  border-radius: 18px;
  padding: 1.5rem;
  border: 1px solid rgba(15,33,61,0.06);
}
.step-number {
  width: 42px;
  height: 42px;
  display: grid;
  place-items: center;
  background: var(--gold);
  color: var(--navy);
  border-radius: 12px;
  font-weight: 800;
  margin-bottom: 1rem;
}

.quote-card {
  background: linear-gradient(135deg, rgba(201, 167, 106, 0.12), rgba(255,255,255,0.9));
}

.news-card strong,
.program-card strong,
.event-card strong {
  font-size: 1.2rem;
}

.faq-list {
  max-width: 860px;
  margin: 0 auto;
}
.faq-item {
  background: var(--white);
  border: 1px solid rgba(15, 33, 61, 0.08);
  border-radius: 18px;
  margin-bottom: 0.9rem;
  overflow: hidden;
}
.faq-question {
  width: 100%;
  text-align: left;
  background: transparent;
  border: none;
  padding: 1.2rem 1.3rem;
  color: var(--navy);
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  cursor: pointer;
}
.faq-answer {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.25s ease;
}
.faq-answer p { padding: 0 1.3rem 1.2rem; margin: 0; }
.faq-item.open .faq-answer { max-height: 200px; }
.faq-item .toggle-sign { font-size: 1.4rem; }

.footer {
  background: var(--navy-deep);
  color: rgba(255,255,255,0.8);
  padding: 4rem 0 2rem;
}
.footer-grid {
  display: grid;
  grid-template-columns: 1.4fr 0.9fr 0.9fr 1.2fr;
  gap: 2rem;
}
.footer h3, .footer h4 { color: var(--white); }
.footer a { color: rgba(255,255,255,0.8); }
.footer a:hover { color: var(--white); }
.footer-bottom {
  border-top: 1px solid rgba(255,255,255,0.08);
  margin-top: 2rem;
  padding-top: 1.2rem;
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.back-to-top {
  position: fixed;
  right: 1.2rem;
  bottom: 1.3rem;
  width: 48px;
  height: 48px;
  border: none;
  border-radius: 50%;
  background: var(--gold);
  color: var(--navy);
  box-shadow: var(--shadow);
  cursor: pointer;
  opacity: 0;
  visibility: hidden;
  transform: translateY(12px);
  transition: all 0.2s ease;
}
.back-to-top.show {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.page-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  align-items: start;
}

details summary { cursor: pointer; }

.image-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
}
.image-grid figure {
  margin: 0;
  position: relative;
  overflow: hidden;
  border-radius: 18px;
  cursor: pointer;
}
.image-grid img {
  width: 100%;
  height: 260px;
  object-fit: cover;
  transition: transform 0.25s ease;
}
.image-grid figure:hover img { transform: scale(1.02); }

.gallery-caption {
  position: absolute;
  left: 1rem;
  right: 1rem;
  bottom: 1rem;
  background: rgba(9,26,48,0.7);
  color: var(--white);
  padding: 0.6rem 0.8rem;
  border-radius: 10px;
  font-size: 0.85rem;
}

.lightbox {
  position: fixed;
  inset: 0;
  background: rgba(9,26,48,0.82);
  display: grid;
  place-items: center;
  padding: 1.5rem;
  z-index: 120;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.2s ease;
}
.lightbox.open {
  opacity: 1;
  visibility: visible;
}
.lightbox-inner {
  position: relative;
  max-width: min(900px, 90vw);
  background: var(--white);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: var(--shadow);
}
.lightbox-inner img {
  width: 100%;
  max-height: 78vh;
  object-fit: cover;
}
.lightbox-close {
  position: absolute;
  top: 0.8rem;
  right: 0.8rem;
  border: none;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(9,26,48,0.9);
  color: var(--white);
  cursor: pointer;
}

.form-panel {
  background: var(--white);
  border-radius: 22px;
  padding: 2rem;
  border: 1px solid rgba(15,33,61,0.08);
  box-shadow: 0 12px 20px rgba(15,33,61,0.04);
}
.form-row {
  display: grid;
  grid-template-columns: repeat(2, minmax(0,1fr));
  gap: 1rem;
}
label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: var(--navy);
}
input, select, textarea {
  width: 100%;
  padding: 0.9rem 1rem;
  border: 1px solid rgba(15,33,61,0.15);
  border-radius: 14px;
  background: #fff;
  color: var(--navy);
}
input:focus-visible, select:focus-visible, textarea:focus-visible, button:focus-visible {
  outline: 3px solid rgba(201,167,106,0.35);
  outline-offset: 2px;
}
textarea { min-height: 140px; resize: vertical; }
.form-actions {
  display: flex;
  justify-content: space-between;
  gap: 0.8rem;
  margin-top: 1.4rem;
}
.form-step { display: none; }
.form-step.active { display: block; }
.progress-steps {
  display: grid;
  grid-template-columns: repeat(5, minmax(0,1fr));
  gap: 0.8rem;
  margin-bottom: 2rem;
}
.progress-step {
  text-align: center;
  padding: 0.8rem 0.5rem;
  border-radius: 12px;
  background: rgba(15,33,61,0.04);
  color: var(--slate);
  font-size: 0.8rem;
  font-weight: 700;
}
.progress-step.active {
  background: var(--navy);
  color: var(--white);
}
.progress-step.complete {
  background: rgba(201,167,106,0.2);
  color: var(--navy);
}
.error-message {
  display: none;
  color: #b42318;
  font-size: 0.82rem;
  margin-top: 0.45rem;
}
.field-error { border-color: #b42318; }
.form-success {
  display: none;
  margin-top: 1rem;
  padding: 1rem 1.2rem;
  background: rgba(73, 155, 94, 0.08);
  border: 1px solid rgba(73, 155, 94, 0.2);
  border-radius: 12px;
  color: #1d5b3b;
  font-weight: 600;
}

.filter-bar {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  align-items: center;
  margin-bottom: 2rem;
}
.filter-bar .field {
  min-width: 200px;
  flex: 1;
}
.filter-bar .field select,
.filter-bar .field input {
  background: var(--white);
}
.empty-state {
  display: none;
  background: var(--white);
  border: 1px dashed rgba(15,33,61,0.2);
  border-radius: 18px;
  padding: 2rem;
  text-align: center;
}
.empty-state.show { display: block; }

.news-filter-wrap,
.contact-parts {
  display: grid;
  grid-template-columns: 1.3fr 0.7fr;
  gap: 2rem;
  align-items: start;
}

.portal-wrap {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 4rem 1rem;
  background: linear-gradient(180deg, rgba(15, 33, 61, 0.96), rgba(15,33,61,0.9)),
    url('https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=1600&q=80') center/cover no-repeat;
}
.portal-card {
  width: min(520px, 100%);
  background: rgba(255,255,255,0.98);
  border-radius: 24px;
  padding: 2rem;
  box-shadow: var(--shadow);
}
.portal-demo {
  background: rgba(201,167,106,0.12);
  color: var(--navy);
  border-radius: 12px;
  padding: 0.8rem 1rem;
  margin-bottom: 1.5rem;
  font-size: 0.92rem;
}
.form-inline { display: flex; align-items: center; gap: 0.8rem; }
.checkbox-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  font-size: 0.96rem;
}
.checkbox-row label { margin: 0; }
.password-toggle { position: relative; }
.password-toggle button {
  position: absolute;
  right: 0.7rem;
  top: 50%;
  transform: translateY(-50%);
  background: transparent;
  border: none;
  color: var(--slate);
  cursor: pointer;
}

.reveal {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}

.card-list { list-style: none; padding: 0; margin: 0; }
.card-list li { margin-bottom: 0.6rem; color: var(--slate); }

@media (max-width: 1024px) {
  .program-grid,
  .feature-grid,
  .facility-grid,
  .events-grid,
  .news-grid,
  .testimonials-grid,
  .leadership-grid,
  .value-grid,
  .contact-grid,
  .footer-grid,
  .page-grid,
  .news-filter-wrap,
  .contact-parts {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
  .hero-grid { grid-template-columns: 1fr; }
  .hero-image-wrap img { height: 480px; }
  .process-grid { grid-template-columns: repeat(2, minmax(0,1fr)); }
}

@media (max-width: 780px) {
  .site-header { position: sticky; }
  .mobile-toggle { display: inline-grid; place-items: center; }
  .primary-nav {
    position: absolute;
    left: 1rem;
    right: 1rem;
    top: calc(100% + 0.4rem);
    background: rgba(255,255,255,0.98);
    border: 1px solid rgba(15,33,61,0.08);
    box-shadow: var(--shadow);
    border-radius: 18px;
    padding: 0.8rem;
    display: none;
    flex-direction: column;
    align-items: stretch;
  }
  .site-header.nav-open .primary-nav { display: flex; }
  .nav-item > a,
  .nav-item > button {
    width: 100%;
    text-align: left;
    padding: 0.8rem 0.7rem;
  }
  .dropdown-menu {
    position: static;
    box-shadow: none;
    border-radius: 10px;
    border: 1px solid rgba(15,33,61,0.06);
    margin-top: 0.35rem;
    opacity: 1; visibility: visible; transform: none; display: none;
  }
  .nav-item.open .dropdown-menu { display: block; }
  .header-actions .btn { display: none; }
  .program-grid,
  .feature-grid,
  .facility-grid,
  .events-grid,
  .news-grid,
  .testimonials-grid,
  .leadership-grid,
  .value-grid,
  .contact-grid,
  .footer-grid,
  .page-grid,
  .news-filter-wrap,
  .contact-parts,
  .process-grid,
  .stats-panel,
  .image-grid,
  .progress-steps,
  .form-row {
    grid-template-columns: 1fr;
  }
  .hero-stats { grid-template-columns: 1fr; }
  .section-header,
  .highlight-band .band-inner,
  .footer-bottom,
  .form-actions,
  .checkbox-row {
    display: block;
  }
  .section { padding: 4.5rem 0; }
  .form-panel { padding: 1.2rem; }
  .page-hero { padding-top: 6rem; }
  .hero-copy h1 { font-size: clamp(2.3rem, 10vw, 3.5rem); }
}

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
'''

js_main = '''
const setActiveNav = () => {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-item > a');
  navLinks.forEach((link) => {
    const href = link.getAttribute('href');
    if (href && href.includes(currentPath)) {
      const parent = link.closest('.nav-item');
      parent?.classList.add('is-active');
    }
  });
};

const setupMobileNav = () => {
  const header = document.querySelector('.site-header');
  const toggle = document.querySelector('.mobile-toggle');
  const closeNav = () => {
    header?.classList.remove('nav-open');
    document.querySelectorAll('.nav-item').forEach((item) => item.classList.remove('open'));
  };

  toggle?.addEventListener('click', () => {
    header?.classList.toggle('nav-open');
  });

  document.querySelectorAll('.nav-item > button').forEach((button) => {
    button.addEventListener('click', (event) => {
      const item = button.closest('.nav-item');
      const isOpen = item?.classList.contains('open');
      document.querySelectorAll('.nav-item').forEach((el) => el.classList.remove('open'));
      if (!isOpen) item?.classList.add('open');
      event.stopPropagation();
    });
  });

  document.addEventListener('click', (event) => {
    if (!event.target.closest('.nav-item')) closeNav();
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeNav();
  });
};

const setupFaqs = () => {
  document.querySelectorAll('.faq-item').forEach((item) => {
    const button = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');
    if (!button || !answer) return;
    button.setAttribute('aria-expanded', 'false');
    const toggle = () => {
      const isOpen = item.classList.toggle('open');
      button.setAttribute('aria-expanded', String(isOpen));
      answer.style.maxHeight = isOpen ? answer.scrollHeight + 'px' : '0px';
    };
    button.addEventListener('click', toggle);
    if (item.classList.contains('open')) {
      answer.style.maxHeight = answer.scrollHeight + 'px';
      button.setAttribute('aria-expanded', 'true');
    }
  });
};

const setupBackToTop = () => {
  const button = document.querySelector('.back-to-top');
  if (!button) return;
  const toggle = () => {
    if (window.scrollY > 420) button.classList.add('show');
    else button.classList.remove('show');
  };
  window.addEventListener('scroll', toggle);
  toggle();
  button.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
};

const revealOnScroll = () => {
  const items = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.2 });
  items.forEach((item) => observer.observe(item));
};

const setupGallery = () => {
  const lightbox = document.getElementById('galleryLightbox');
  const lightboxImage = document.getElementById('lightboxImage');
  const closeButton = document.getElementById('lightboxClose');
  document.querySelectorAll('[data-gallery-image]').forEach((button) => {
    button.addEventListener('click', () => {
      if (!lightbox || !lightboxImage) return;
      lightboxImage.src = button.dataset.galleryImage;
      lightbox.classList.add('open');
      lightbox.setAttribute('aria-hidden', 'false');
    });
  });
  const closeLightbox = () => {
    if (!lightbox) return;
    lightbox.classList.remove('open');
    lightbox.setAttribute('aria-hidden', 'true');
  };
  closeButton?.addEventListener('click', closeLightbox);
  lightbox?.addEventListener('click', (event) => {
    if (event.target === lightbox) closeLightbox();
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && lightbox?.classList.contains('open')) closeLightbox();
  });
};

const setupNewsletterForm = () => {
  const form = document.getElementById('newsletterForm');
  if (!form) return;
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const emailInput = document.getElementById('newsletterEmail');
    const status = document.getElementById('newsletterStatus');
    if (!emailInput || !status) return;
    const email = emailInput.value.trim();
    if (!email || !email.includes('@')) {
      status.textContent = 'Please enter a valid email address.';
      status.style.color = '#b42318';
      return;
    }
    status.textContent = 'Thanks! Your demo newsletter signup is ready.';
    status.style.color = '#1d5b3b';
    form.reset();
  });
};

const setupDetailPage = () => {
  const detailRoot = document.getElementById('detailContent');
  if (!detailRoot) return;

  const params = new URLSearchParams(window.location.search);
  const slug = params.get('slug');
  const type = params.get('type');

  const data = {
    news: [
      { slug: 'research-innovation', title: 'Research and Innovation Lab Opens at Crestfield', category: 'Campus', description: 'A new multidisciplinary lab brings students and faculty together around entrepreneurship, design thinking, and applied research.', date: 'April 11, 2026', image: 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=1400&q=80' },
      { slug: 'new-solar', title: 'New Solar Energy Initiatives Reduce Campus Emissions', category: 'Sustainability', description: 'Crestfield has launched a solar installation and student-led sustainability program to lower the campus carbon footprint.', date: 'March 29, 2026', image: 'https://images.unsplash.com/photo-1497440001374-f26997328c1b?auto=format&fit=crop&w=1400&q=80' },
      { slug: 'career-network', title: 'Career Network Connects Students with Industry Leaders', category: 'Student Success', description: 'The Career Development Office hosted a signature networking event linking students with employers and alumni across sectors.', date: 'March 15, 2026', image: 'https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=1400&q=80' }
    ],
    events: [
      { slug: 'open-day', title: 'Future Leaders Open Day', category: 'Admissions', description: 'Meet faculty, explore programs, and tour our innovation labs during an engaging campus visit experience.', date: 'May 16, 2026', image: 'https://images.unsplash.com/photo-1523580494863-6f3031224c94?auto=format&fit=crop&w=1400&q=80' },
      { slug: 'hackathon', title: 'Global Challenge Hackathon', category: 'Innovation', description: 'Students collaborate in interdisciplinary teams to solve real world challenges using design, data, and applied engineering.', date: 'June 04, 2026', image: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1400&q=80' },
      { slug: 'mentor', title: 'Mentor Connect Week', category: 'Community', description: 'Students are paired with alumni and industry mentors for guidance, networking, and career planning.', date: 'June 24, 2026', image: 'https://images.unsplash.com/photo-1516321165247-4aa89a48be28?auto=format&fit=crop&w=1400&q=80' }
    ]
  };

  const all = [...data.news, ...data.events];
  const record = all.find((item) => item.slug === slug && (!type || item.category.toLowerCase() === type.toLowerCase()));
  if (!record) {
    detailRoot.innerHTML = '<div class="card"><h2>Detail not found</h2><p>This sample entry is not available in this demo build.</p><a class="btn btn-primary" href="./news.html">Return to news</a></div>';
    return;
  }

  detailRoot.innerHTML = `
    <article class="card">
      <img src="${record.image}" alt="${record.title}" style="height: 420px; object-fit: cover; border-radius: 18px; margin-bottom: 1.5rem;" />
      <div class="meta"><span>${record.category}</span><span>${record.date}</span></div>
      <h1>${record.title}</h1>
      <p>${record.description}</p>
      <p>Sample content for demonstration purposes only. Crestfield College is a fictional higher-education institution created for a portfolio website project. This detail page is a static front-end mockup and does not connect to a live backend or CMS.</p>
      <p>Students at Crestfield benefit from interdisciplinary coursework, experiential learning, professional mentoring, and an innovation-focused campus culture designed to prepare graduates for meaningful careers in a changing world.</p>
      <a class="btn btn-primary" href="./news.html">Back to News & Events</a>
    </article>
  `;
};

const setupProgramDetail = () => {
  const detailRoot = document.getElementById('programDetail');
  if (!detailRoot) return;
  const params = new URLSearchParams(window.location.search);
  const slug = params.get('program');
  const programs = [
    { slug: 'computer-science', title: 'Computer Science', faculty: 'Faculty of Computing', qualification: 'Bachelor', duration: '4 years', description: 'Build a strong foundation in software systems, machine learning, and algorithmic thinking for professional tech careers.', outcome: 'Software engineering, AI, systems design, research.' },
    { slug: 'software-engineering', title: 'Software Engineering', faculty: 'Faculty of Computing', qualification: 'Bachelor', duration: '4 years', description: 'Design reliable digital products through agile development, testing, architecture, and collaborative workflows.', outcome: 'Product engineering, application development, QA, full-stack delivery.' },
    { slug: 'information-technology', title: 'Information Technology', faculty: 'Faculty of Computing', qualification: 'Bachelor', duration: '4 years', description: 'Balance technical problem solving with systems support, infrastructure management, and digital transformation.', outcome: 'IT support, cybersecurity, cloud services, business systems.' },
    { slug: 'data-science', title: 'Data Science', faculty: 'School of Analytics', qualification: 'Bachelor', duration: '4 years', description: 'Turn data into strategic decisions through statistics, AI, data storytelling, and applied analytics.', outcome: 'Analytics, predictive modeling, insights, research.' },
    { slug: 'electrical-electronics-engineering', title: 'Electrical and Electronics Engineering', faculty: 'School of Engineering', qualification: 'Bachelor', duration: '5 years', description: 'Develop energy, control, communications, and embedded systems through design and laboratory work.', outcome: 'Automation, electronics, power systems, connected devices.' },
    { slug: 'business-administration', title: 'Business Administration', faculty: 'School of Business', qualification: 'Bachelor', duration: '4 years', description: 'Prepare for leadership roles with entrepreneurship, operations, management, and strategic decision-making.', outcome: 'Management, consulting, operations, marketing leadership.' },
    { slug: 'accounting', title: 'Accounting', faculty: 'School of Business', qualification: 'Bachelor', duration: '4 years', description: 'Learn financial reporting, tax, auditing, and business analysis with a professional focus.', outcome: 'Audit, finance, tax, business advisory.' },
    { slug: 'mass-communication', title: 'Mass Communication', faculty: 'School of Media & Communication', qualification: 'Bachelor', duration: '4 years', description: 'Explore media production, journalism, branding, and communication strategies for modern audiences.', outcome: 'Media production, journalism, public relations, digital content.' }
  ];

  const record = programs.find((item) => item.slug === slug);
  if (!record) {
    detailRoot.innerHTML = '<div class="card"><h2>Program not found</h2><p>The requested program could not be found in this sample catalog.</p><a class="btn btn-primary" href="./programs.html">Return to programs</a></div>';
    return;
  }

  detailRoot.innerHTML = `
    <article class="card">
      <div class="eyebrow">Illustrative academic sample</div>
      <h1>${record.title}</h1>
      <div class="meta"><span>${record.faculty}</span><span>${record.qualification}</span><span>${record.duration}</span></div>
      <p>${record.description}</p>
      <p><strong>Career pathways:</strong> ${record.outcome}</p>
      <p>This academic profile is illustrative and clearly labeled as sample content for a static front-end website demonstration. It is not an official institutional catalog.</p>
      <div class="form-actions">
        <a class="btn btn-primary" href="./programs.html">Back to programs</a>
        <a class="btn btn-secondary" href="./admissions.html">Apply now</a>
      </div>
    </article>
  `;
};

const setupProgramSearch = () => {
  const list = document.getElementById('programGrid');
  if (!list) return;
  const cards = [...list.querySelectorAll('.program-card')];
  const searchField = document.getElementById('programSearch');
  const facultyField = document.getElementById('facultyFilter');
  const qualificationField = document.getElementById('qualificationFilter');
  const emptyState = document.getElementById('programEmpty');

  const applyFilters = () => {
    const search = (searchField?.value || '').trim().toLowerCase();
    const faculty = facultyField?.value || 'all';
    const qualification = qualificationField?.value || 'all';
    let visible = 0;

    cards.forEach((card) => {
      const title = (card.dataset.title || '').toLowerCase();
      const facultyValue = (card.dataset.faculty || '');
      const qualificationValue = (card.dataset.qualification || '');
      const matchesSearch = !search || title.includes(search);
      const matchesFaculty = faculty === 'all' || facultyValue === faculty;
      const matchesQualification = qualification === 'all' || qualificationValue === qualification;
      const visibleCard = matchesSearch && matchesFaculty && matchesQualification;
      card.style.display = visibleCard ? '' : 'none';
      if (visibleCard) visible += 1;
    });

    if (emptyState) emptyState.classList.toggle('show', visible === 0);
  };

  [searchField, facultyField, qualificationField].forEach((field) => field?.addEventListener('input', applyFilters));
  [facultyField, qualificationField].forEach((field) => field?.addEventListener('change', applyFilters));
  document.getElementById('resetFilters')?.addEventListener('click', () => {
    if (searchField) searchField.value = '';
    if (facultyField) facultyField.value = 'all';
    if (qualificationField) qualificationField.value = 'all';
    applyFilters();
  });
};

const setupNewsSearch = () => {
  const list = document.getElementById('newsGrid');
  if (!list) return;
  const cards = [...list.querySelectorAll('.news-card, .event-card')];
  const searchInput = document.getElementById('newsSearch');
  const categoryField = document.getElementById('newsCategory');

  const applyFilters = () => {
    const search = (searchInput?.value || '').trim().toLowerCase();
    const category = categoryField?.value || 'all';
    let visible = 0;
    cards.forEach((card) => {
      const title = (card.dataset.title || '').toLowerCase();
      const matchText = title.includes(search) || (card.dataset.category || '').toLowerCase().includes(search);
      const matchCategory = category === 'all' || card.dataset.category === category;
      const shouldShow = matchText && matchCategory;
      card.style.display = shouldShow ? '' : 'none';
      if (shouldShow) visible += 1;
    });
    const emptyState = document.getElementById('newsEmpty');
    if (emptyState) emptyState.classList.toggle('show', visible === 0);
  };

  searchInput?.addEventListener('input', applyFilters);
  categoryField?.addEventListener('change', applyFilters);
};

const setupAdmissionsForm = () => {
  const form = document.getElementById('admissionsForm');
  if (!form) return;
  const steps = [...form.querySelectorAll('.form-step')];
  const indicators = [...document.querySelectorAll('.progress-step')];
  const nextButton = document.getElementById('nextStep');
  const prevButton = document.getElementById('prevStep');
  const submitButton = document.getElementById('submitApplication');
  const successMessage = document.getElementById('formSuccess');
  let currentStep = 0;

  const validateStep = () => {
    const currentFields = steps[currentStep].querySelectorAll('input, select, textarea');
    let isValid = true;
    currentFields.forEach((field) => {
      const required = field.hasAttribute('required');
      const value = (field.value || '').trim();
      const errorEl = field.closest('.field-group')?.querySelector('.error-message');
      if (!required) return;
      if (!value) {
        field.classList.add('field-error');
        if (errorEl) {
          errorEl.textContent = 'This field is required.';
          errorEl.style.display = 'block';
        }
        isValid = false;
        return;
      }
      if (field.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
        field.classList.add('field-error');
        if (errorEl) {
          errorEl.textContent = 'Please provide a valid email address.';
          errorEl.style.display = 'block';
        }
        isValid = false;
        return;
      }
      field.classList.remove('field-error');
      if (errorEl) errorEl.style.display = 'none';
    });
    return isValid;
  };

  const renderStep = () => {
    steps.forEach((step, index) => step.classList.toggle('active', index === currentStep));
    indicators.forEach((step, index) => {
      step.classList.toggle('active', index === currentStep);
      step.classList.toggle('complete', index < currentStep);
    });
    prevButton.style.display = currentStep === 0 ? 'none' : 'inline-flex';
    nextButton.style.display = currentStep === steps.length - 1 ? 'none' : 'inline-flex';
    submitButton.style.display = currentStep === steps.length - 1 ? 'inline-flex' : 'none';
    successMessage.style.display = 'none';
  };

  nextButton?.addEventListener('click', () => {
    if (!validateStep()) return;
    currentStep += 1;
    renderStep();
  });

  prevButton?.addEventListener('click', () => {
    currentStep -= 1;
    renderStep();
  });

  submitButton?.addEventListener('click', (event) => {
    event.preventDefault();
    if (!validateStep()) return;
    successMessage.style.display = 'block';
    successMessage.textContent = 'Demo submitted successfully. This form is only a front-end example; no real application has been sent.';
    form.reset();
    currentStep = 0;
    renderStep();
  });

  renderStep();
};

const setupContactForm = () => {
  const form = document.getElementById('contactForm');
  if (!form) return;
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const name = document.getElementById('contactName');
    const email = document.getElementById('contactEmail');
    const message = document.getElementById('contactMessage');
    const status = document.getElementById('contactStatus');
    let valid = true;
    const setError = (field, msg) => {
      field.classList.add('field-error');
      const error = field.closest('.field-group')?.querySelector('.error-message');
      if (error) {
        error.textContent = msg;
        error.style.display = 'block';
      }
      valid = false;
    };
    [name, email, message].forEach((field) => field.classList.remove('field-error'));
    document.querySelectorAll('.error-message').forEach((el) => el.style.display = 'none');
    if (!name.value.trim()) setError(name, 'Please enter your name.');
    if (!email.value.trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())) setError(email, 'Please enter a valid email address.');
    if (!message.value.trim()) setError(message, 'Please enter your message.');
    if (!valid) {
      status.textContent = 'Please correct the highlighted fields.';
      status.style.color = '#b42318';
      return;
    }
    status.textContent = 'This demo form is working. No email service is connected, so no real message is sent.';
    status.style.color = '#1d5b3b';
    form.reset();
  });
};

const setupPortalForm = () => {
  const form = document.getElementById('portalForm');
  if (!form) return;
  const passwordInput = document.getElementById('password');
  const toggle = document.getElementById('togglePassword');
  const status = document.getElementById('portalStatus');
  toggle?.addEventListener('click', () => {
    const isVisible = passwordInput.type === 'text';
    passwordInput.type = isVisible ? 'password' : 'text';
    toggle.textContent = isVisible ? 'Show' : 'Hide';
  });
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const email = document.getElementById('studentEmail').value.trim();
    const password = passwordInput.value.trim();
    if (!email || !password) {
      status.textContent = 'Please enter both your student ID or email and password.';
      status.style.color = '#b42318';
      return;
    }
    status.textContent = 'Demo mode only: a real backend and secure authentication are required for production student login.';
    status.style.color = '#1d5b3b';
  });
};

document.addEventListener('DOMContentLoaded', () => {
  setActiveNav();
  setupMobileNav();
  setupFaqs();
  setupBackToTop();
  revealOnScroll();
  setupNewsletterForm();
  setupGallery();
  setupDetailPage();
  setupProgramDetail();
  setupProgramSearch();
  setupNewsSearch();
  setupAdmissionsForm();
  setupContactForm();
  setupPortalForm();
  document.getElementById('year')?.replaceChildren(String(new Date().getFullYear()));
});
'''

js_programs = '''
const programCatalog = [
  { title: 'Computer Science', faculty: 'Faculty of Computing', qualification: 'Bachelor', duration: '4 years', description: 'A rigorous computing foundation spanning software, systems, and AI.', slug: 'computer-science' },
  { title: 'Software Engineering', faculty: 'Faculty of Computing', qualification: 'Bachelor', duration: '4 years', description: 'Design scalable systems through agile delivery, testing, and architecture.', slug: 'software-engineering' },
  { title: 'Information Technology', faculty: 'Faculty of Computing', qualification: 'Diploma', duration: '3 years', description: 'Build practical IT skills in networking, support, and digital transformation.', slug: 'information-technology' },
  { title: 'Data Science', faculty: 'School of Analytics', qualification: 'Bachelor', duration: '4 years', description: 'Learn analytics, statistics, and machine learning for strategic decisions.', slug: 'data-science' },
  { title: 'Electrical and Electronics Engineering', faculty: 'School of Engineering', qualification: 'Bachelor', duration: '5 years', description: 'Design energy, automation, and electronic systems for modern infrastructure.', slug: 'electrical-electronics-engineering' },
  { title: 'Business Administration', faculty: 'School of Business', qualification: 'Bachelor', duration: '4 years', description: 'Prepare for leadership roles in business strategy, operations, and innovation.', slug: 'business-administration' },
  { title: 'Accounting', faculty: 'School of Business', qualification: 'Bachelor', duration: '4 years', description: 'Build expertise in financial reporting, taxation, and advisory decision-making.', slug: 'accounting' },
  { title: 'Mass Communication', faculty: 'School of Media & Communication', qualification: 'Bachelor', duration: '4 years', description: 'Create compelling narratives across journalism, media production, and digital campaigns.', slug: 'mass-communication' }
];

const renderPrograms = () => {
  const list = document.getElementById('programGrid');
  if (!list) return;
  list.innerHTML = programCatalog.map((program) => `
    <article class="card program-card reveal" data-title="${program.title}" data-faculty="${program.faculty}" data-qualification="${program.qualification}">
      <div class="meta">
        <span>${program.faculty}</span>
        <span>${program.qualification}</span>
      </div>
      <h3>${program.title}</h3>
      <p>${program.description}</p>
      <div class="meta">
        <span>Duration: ${program.duration}</span>
      </div>
      <a class="btn btn-secondary" href="./program-detail.html?program=${program.slug}">View Details</a>
    </article>
  `).join('');
};

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', renderPrograms);
} else {
  renderPrograms();
}
'''

js_admissions = '''
const programOptions = [
  'Computer Science', 'Software Engineering', 'Information Technology', 'Data Science',
  'Electrical and Electronics Engineering', 'Business Administration', 'Accounting', 'Mass Communication'
];

const populatePrograms = () => {
  const select = document.getElementById('programChoice');
  if (!select) return;
  select.innerHTML = '<option value="">Select a program</option>' + programOptions.map((program) => `<option value="${program}">${program}</option>`).join('');
};

document.addEventListener('DOMContentLoaded', populatePrograms);
'''

js_contact = '''
const setupContactBehavior = () => {
  const form = document.getElementById('contactForm');
  if (!form) return;
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const name = document.getElementById('contactName');
    const email = document.getElementById('contactEmail');
    const subject = document.getElementById('contactSubject');
    const message = document.getElementById('contactMessage');
    const status = document.getElementById('contactStatus');
    const valid = name.value.trim() && email.value.includes('@') && message.value.trim() && subject.value.trim();
    if (!valid) {
      status.textContent = 'Please complete all required fields.';
      status.style.color = '#b42318';
      return;
    }
    status.textContent = 'Demo form submitted. No backend email service is attached.';
    status.style.color = '#1d5b3b';
    form.reset();
  });
};

document.addEventListener('DOMContentLoaded', setupContactBehavior);
'''

shared_header = '''
<div class="site-announcement"><div class="container"><strong>Admissions Open:</strong> Fall 2026 applications now available for undergraduate and postgraduate study.</div></div>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="./index.html" aria-label="Crestfield College homepage">
      <span class="brand-mark">C</span>
      <span class="brand-text"><small>Crestfield</small><strong>College of Technology</strong></span>
    </a>
    <nav class="primary-nav" aria-label="Main navigation">
      <div class="nav-item"><a href="./index.html">Home</a></div>
      <div class="nav-item"><a href="./about.html">About</a></div>
      <div class="nav-item">
        <button type="button" aria-expanded="false">Academics</button>
        <div class="dropdown-menu">
          <a href="./programs.html">All Programs</a>
          <a href="./program-detail.html?program=computer-science">Computer Science</a>
          <a href="./program-detail.html?program=data-science">Data Science</a>
          <a href="./program-detail.html?program=business-administration">Business Administration</a>
        </div>
      </div>
      <div class="nav-item"><a href="./admissions.html">Admissions</a></div>
      <div class="nav-item"><a href="./campus-life.html">Campus Life</a></div>
      <div class="nav-item"><a href="./news.html">News &amp; Events</a></div>
      <div class="nav-item"><a href="./contact.html">Contact</a></div>
    </nav>
    <div class="header-actions">
      <a class="btn btn-primary" href="./admissions.html">Apply Now</a>
      <button class="mobile-toggle" type="button" aria-label="Toggle menu" aria-expanded="false">☰</button>
    </div>
  </div>
</header>
'''

shared_footer = '''
<footer class="footer">
  <div class="container footer-grid">
    <div>
      <a class="brand" href="./index.html" aria-label="Crestfield College homepage">
        <span class="brand-mark">C</span>
        <span class="brand-text"><small>Crestfield</small><strong>College of Technology</strong></span>
      </a>
      <p style="margin-top:1rem; max-width: 320px;">Preparing career-ready graduates through academic excellence, innovation, and meaningful student experiences.</p>
    </div>
    <div>
      <h4>Explore</h4>
      <ul class="card-list">
        <li><a href="./about.html">About us</a></li>
        <li><a href="./programs.html">Academic programs</a></li>
        <li><a href="./admissions.html">Admissions</a></li>
        <li><a href="./campus-life.html">Campus life</a></li>
      </ul>
    </div>
    <div>
      <h4>Resource</h4>
      <ul class="card-list">
        <li><a href="./news.html">News &amp; events</a></li>
        <li><a href="./contact.html">Contact</a></li>
        <li><a href="./student-portal.html">Student portal</a></li>
        <li><a href="./404.html">Support</a></li>
      </ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul class="card-list">
        <li>101 Academy Way, Crestfield</li>
        <li>hello@crestfieldcollege.edu</li>
        <li>+1 (555) 014-9832</li>
        <li>Mon–Fri: 8:00am–5:00pm</li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>© <span id="year"></span> Crestfield College of Technology</span>
    <span>Illustrative sample website for a portfolio project.</span>
  </div>
</footer>
<button class="back-to-top" type="button" aria-label="Back to top">↑</button>
'''

def page_shell(content, title, description, body_class=''):
    return f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="{description}" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{description}" />
    <meta property="og:type" content="website" />
    <meta property="og:image" content="https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=1400&q=80" />
    <title>{title}</title>
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='18' fill='%230f213d'/%3E%3Ctext x='50%25' y='54%25' dominant-baseline='middle' text-anchor='middle' fill='white' font-size='36' font-family='Arial, sans-serif'%3EC%3C/text%3E%3C/svg%3E" />
    <link rel="stylesheet" href="./css/style.css" />
  </head>
  <body class="{body_class}">
    {shared_header}
    {content}
    {shared_footer}
    <script src="./js/main.js"></script>
  </body>
</html>
'''

pages = {
    'index.html': page_shell('''
<main>
  <section class="hero">
    <div class="container hero-grid">
      <div class="hero-copy reveal">
        <span class="eyebrow">Academic excellence • Career readiness</span>
        <h1>Build Your Future. Shape What Comes Next.</h1>
        <p class="lead">At Crestfield College of Technology, students learn by doing, think critically, and grow into confident professionals ready for the demands of a changing world.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="./programs.html">Explore Programs</a>
          <a class="btn btn-secondary" href="./admissions.html">Apply for Admission</a>
        </div>
        <div class="hero-stats">
          <div class="stat-box"><strong>12k+</strong><span>Students</span></div>
          <div class="stat-box"><strong>88%</strong><span>Graduate employment</span></div>
          <div class="stat-box"><strong>35+</strong><span>Academic programs</span></div>
        </div>
      </div>
      <div class="hero-visual reveal">
        <div class="hero-image-wrap">
          <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=1200&q=80" alt="Students collaborating in a modern campus environment" />
        </div>
        <div class="hero-badge"><strong>2026 Intake</strong><span>Applications open for new scholarships and early admission pathways.</span></div>
      </div>
    </div>
  </section>

  <section class="section"><div class="container">
    <div class="section-header reveal">
      <div><span class="eyebrow">Popular programs</span><h2>Study fields designed for tomorrow.</h2></div>
      <p>Our academic portfolio blends theory, hands-on practice, and professional mentoring to prepare students for dynamic careers.</p>
    </div>
    <div class="program-grid">
      <article class="card program-card reveal"><div class="meta"><span>Faculty of Computing</span></div><h3>Computer Science</h3><p>Explore software design, programming, AI, and systems engineering with a strong emphasis on problem solving.</p><div class="meta"><span>4 years</span><span>Bachelor</span></div><a class="btn btn-secondary" href="./program-detail.html?program=computer-science">View Details</a></article>
      <article class="card program-card reveal"><div class="meta"><span>School of Analytics</span></div><h3>Data Science</h3><p>Build data literacy and advanced analytical skills to uncover insights and drive data-informed decisions.</p><div class="meta"><span>4 years</span><span>Bachelor</span></div><a class="btn btn-secondary" href="./program-detail.html?program=data-science">View Details</a></article>
      <article class="card program-card reveal"><div class="meta"><span>School of Business</span></div><h3>Business Administration</h3><p>Develop strategic leadership and entrepreneurial skills suited to modern organizations and startups.</p><div class="meta"><span>4 years</span><span>Bachelor</span></div><a class="btn btn-secondary" href="./program-detail.html?program=business-administration">View Details</a></article>
    </div>
  </div></section>

  <section class="section" style="background: rgba(255,255,255,0.7);"><div class="container">
    <div class="section-header reveal"><div><span class="eyebrow">Why Crestfield</span><h2>Learning built around real outcomes.</h2></div></div>
    <div class="feature-grid">
      <article class="card reveal"><div class="feature-icon">✦</div><h3>Career-focused curriculum</h3><p>Programs align with professional standards, internship opportunities, and employability pathways.</p></article>
      <article class="card reveal"><div class="feature-icon">▣</div><h3>World-class facilities</h3><p>Hands-on labs, innovation hubs, maker spaces, and digital learning environments support exploration.</p></article>
      <article class="card reveal"><div class="feature-icon">◎</div><h3>Mentorship culture</h3><p>Students learn with faculty mentors, alumni networks, and personal development support throughout their journey.</p></article>
    </div>
  </div></section>

  <section class="section"><div class="container">
    <div class="section-header reveal"><div><span class="eyebrow">Campus experience</span><h2>Facilities designed for exploration.</h2></div><a class="btn btn-secondary" href="./campus-life.html">See campus life</a></div>
    <div class="facility-grid">
      <article class="card reveal"><img src="https://images.unsplash.com/photo-1498243691581-b145c3f54a5a?auto=format&fit=crop&w=900&q=80" alt="Modern computer laboratory" /><h3>Innovation Labs</h3><p>Collaborative spaces equip students with tools for prototyping, experimentation, and project-based learning.</p></article>
      <article class="card reveal"><img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=900&q=80" alt="Students in a lecture hall" /><h3>Learning Commons</h3><p>Flexible study zones and academic support services help students build confidence and community.</p></article>
      <article class="card reveal"><img src="https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=900&q=80" alt="Students in a modern campus meeting space" /><h3>Student Hub</h3><p>Networking, counseling, clubs, and student life resources connect students to a vibrant campus network.</p></article>
    </div>
  </div></section>

  <section class="section highlight-band"><div class="container band-inner reveal"><strong>Academic opportunity, personal growth, and future-ready skills in one experience.</strong><a class="btn btn-primary" href="./about.html">Meet the College</a></div></section>

  <section class="section"><div class="container"><div class="section-header reveal"><div><span class="eyebrow">Admissions</span><h2>Your next chapter starts here.</h2></div></div><div class="process-grid"><article class="step-box reveal"><div class="step-number">1</div><h3>Explore</h3><p>Review programs, learning outcomes, and support services to find the right fit.</p></article><article class="step-box reveal"><div class="step-number">2</div><h3>Apply</h3><p>Complete your application and submit the required information through a guided process.</p></article><article class="step-box reveal"><div class="step-number">3</div><h3>Submit Documents</h3><p>Share transcripts, supporting records, and any required certification materials.</p></article><article class="step-box reveal"><div class="step-number">4</div><h3>Enroll</h3><p>Receive your offer and begin orientation, advising, and course registration.</p></article></div></div></section>

  <section class="section" style="background: rgba(255,255,255,0.7);"><div class="container"><div class="section-header reveal"><div><span class="eyebrow">Student life</span><h2>Campus moments beyond the classroom.</h2></div></div><div class="facility-grid"><article class="card reveal"><img src="https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=900&q=80" alt="Students at a campus event" /><h3>Clubs & societies</h3><p>Join entrepreneurial clubs, design societies, and student organizations that build leadership and belonging.</p></article><article class="card reveal"><img src="https://images.unsplash.com/photo-1541534401786-2077eed87a74?auto=format&fit=crop&w=900&q=80" alt="Students engaged in sports activity" /><h3>Sports & recreation</h3><p>Stay active, join inter-campus events, and connect through wellness programs and athletics.</p></article><article class="card reveal"><img src="https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=900&q=80" alt="Students at a campus festival" /><h3>Student events</h3><p>From cultural festivals to tech showcases, campus events spark creativity and new friendships.</p></article></div></div></section>

  <section class="section"><div class="container"><div class="section-header reveal"><div><span class="eyebrow">Upcoming events</span><h2>What is happening on campus.</h2></div></div><div class="events-grid"><article class="card event-card reveal"><div class="meta"><span>Admissions</span><span>May 16</span></div><h3>Future Leaders Open Day</h3><p>Meet faculty, tour our labs, and explore admissions pathways for the next academic intake.</p><a class="btn btn-secondary" href="./news-detail.html?slug=open-day&type=events">Learn more</a></article><article class="card event-card reveal"><div class="meta"><span>Innovation</span><span>June 4</span></div><h3>Global Challenge Hackathon</h3><p>Students collaborate in teams to design solutions to today’s world challenges with mentorship from experts.</p><a class="btn btn-secondary" href="./event-detail.html?slug=hackathon">Learn more</a></article><article class="card event-card reveal"><div class="meta"><span>Community</span><span>June 24</span></div><h3>Mentor Connect Week</h3><p>Hear from industry professionals and alumni on building a strong career strategy and network.</p><a class="btn btn-secondary" href="./event-detail.html?slug=mentor">Learn more</a></article></div></div></section>

  <section class="section" style="background: rgba(255,255,255,0.7);"><div class="container"><div class="section-header reveal"><div><span class="eyebrow">Latest news</span><h2>Fresh campus stories.</h2></div><a class="btn btn-secondary" href="./news.html">Browse all news</a></div><div class="news-grid"><article class="card news-card reveal"><div class="meta"><span>Campus</span><span>Apr 11</span></div><h3>Research and Innovation Lab Opens at Crestfield</h3><p>A new lab brings faculty and students together to pursue applied research and entrepreneurship.</p><a class="btn btn-secondary" href="./news-detail.html?slug=research-innovation&type=news">Read article</a></article><article class="card news-card reveal"><div class="meta"><span>Sustainability</span><span>Mar 29</span></div><h3>New Solar Energy Initiatives Reduce Campus Emissions</h3><p>Our sustainability vision is advancing through student co-designed environmental initiatives.</p><a class="btn btn-secondary" href="./news-detail.html?slug=new-solar&type=news">Read article</a></article><article class="card news-card reveal"><div class="meta"><span>Student Success</span><span>Mar 15</span></div><h3>Career Network Connects Students with Industry Leaders</h3><p>Students explore pathways in technology, media, and business through mentorship opportunities.</p><a class="btn btn-secondary" href="./news-detail.html?slug=career-network&type=news">Read article</a></article></div></div></section>

  <section class="section"><div class="container"><div class="section-header reveal"><div><span class="eyebrow">Testimonials</span><h2>What students say.</h2></div></div><div class="testimonials-grid"><article class="card quote-card reveal"><p>“The practical learning environment at Crestfield helped me transition from coursework into a successful internship and early career path.”</p><strong>— Aisha O., Computer Science</strong></article><article class="card quote-card reveal"><p>“The faculty and mentoring culture shaped my confidence, especially when I worked on interdisciplinary projects and startup ideas.”</p><strong>— Daniel K., Business Administration</strong></article><article class="card quote-card reveal"><p>“I loved the balance of academic rigor and student life. The campus experience made my university journey memorable.”</p><strong>— Nia T., Mass Communication</strong></article></div></div></section>

  <section class="section"><div class="container"><div class="card reveal" style="padding: 2rem; background: linear-gradient(135deg, rgba(201,167,106,0.18), rgba(255,255,255,0.9));"><div class="page-grid"><div><span class="eyebrow">Start your journey</span><h2>Ready to discover a future built for impact?</h2></div><div style="display:flex; justify-content:flex-end; align-items:center; gap:1rem; flex-wrap:wrap;"><a class="btn btn-primary" href="./admissions.html">Apply now</a><a class="btn btn-secondary" href="./contact.html">Book a campus visit</a></div></div></div></div></section>
</main>
''', 'Crestfield College of Technology | Home', 'Crestfield College of Technology offers innovative, career-aware education in technology, business, and applied disciplines.', 'home'),
    'about.html': page_shell('''
<main>
  <section class="page-hero"><div class="container"><div class="breadcrumbs">Home / About</div><h1>About Crestfield</h1><p>Crestfield College of Technology is a fictional institution designed to reflect the spirit of modern higher education—ambitious, practical, and community-focused.</p></div></section>
  <section class="section"><div class="container page-grid"><div class="reveal"><span class="eyebrow">Our story</span><h2>Prepared for progress.</h2><p>Crestfield was established to create a university experience that bridges academic depth with professional readiness. We believe students thrive when ideas are challenged, creativity is encouraged, and skills are grounded in practice.</p><p>From our early roots in applied learning to our current interdisciplinary model, Crestfield has evolved with a clear mission: to educate forward-looking graduates who can contribute meaningfully to industry, communities, and society.</p></div><div class="card reveal"><h3>Vision</h3><p>To be a leading institution that empowers students to innovate, lead, and shape the future through high-quality, career-relevant education.</p><h3>Mission</h3><p>To create a transformative learning environment grounded in academic excellence, research, mentorship, and student opportunity.</p></div></div></section>
  <section class="section" style="background: rgba(255,255,255,0.7);"><div class="container"><div class="section-header reveal"><div><span class="eyebrow">Core values</span><h2>What guides us.</h2></div></div><div class="value-grid"><article class="card reveal"><h3>Excellence</h3><p>We expect thoughtful scholarship, ambitious thinking, and measurable achievement in every area of the student experience.</p></article><article class="card reveal"><h3>Innovation</h3><p>We encourage experimentation, creative problem solving, and a mindset that transforms ideas into action.</p></article><article class="card reveal"><h3>Integrity</h3><p>We champion honesty, professionalism, and responsible leadership in both academic and personal growth.</p></article></div></div></section>
  <section class="section"><div class="container"><div class="section-header reveal"><div><span class="eyebrow">College history</span><h2>Milestones in our growth.</h2></div></div><div class="timeline"><article class="card reveal"><h3>2010</h3><p>Crestfield College began as a focused technology institute designed to serve students seeking practical higher education.</p></article><article class="card reveal"><h3>2015</h3><p>We expanded academic offerings, strengthening our business, communications, and engineering programs.</p></article><article class="card reveal"><h3>2020</h3><p>New research laboratories, mentorship pathways, and innovation hubs positioned the college for broader regional impact.</p></article></div></div></section>
  <section class="section" style="background: rgba(255,255,255,0.7);"><div class="container"><div class="section-header reveal"><div><span class="eyebrow">Leadership</span><h2>Leaders shaping the student experience.</h2></div></div><div class="leadership-grid"><article class="card reveal"><img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=900&q=80" alt="Sample portrait of a college leader" /><h3>Dr. Amelia Hart</h3><p>President &amp; Chief Academic Officer</p></article><article class="card reveal"><img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=900&q=80" alt="Sample portrait of a dean" /><h3>Professor Daniel Reed</h3><p>Dean of Engineering and Applied Sciences</p></article><article class="card reveal"><img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=900&q=80" alt="Sample portrait of a student support leader" /><h3>Ms. Priya Thompson</h3><p>Vice President for Student Success</p></article></div></div></section>
  <section class="section"><div class="container page-grid"><div class="reveal"><span class="eyebrow">Campus profile</span><h2>Facilities that support ambitious learning.</h2><ul class="card-list"><li>Digital classrooms and collaborative learning spaces</li><li>Innovation labs for applied technology and research</li><li>Student support services, counseling, and mentoring</li><li>Recreational and wellness facilities for balance and belonging</li></ul></div><div class="card reveal"><h3>Accreditation information</h3><p>This website contains sample placeholder content. Accreditation claims, rankings, or approvals are not presented as verified institutional information.</p><p>Students and applicants should verify all academic and institutional claims directly with the official college admissions office.</p></div></div></section>
  <section class="section"><div class="container"><div class="card reveal" style="padding: 2rem; background: linear-gradient(135deg, rgba(201,167,106,0.15), rgba(255,255,255,0.9));"><div class="page-grid"><div><span class="eyebrow">Academic pathways</span><h2>Explore programs built for real-world outcomes.</h2></div><div style="display:flex; justify-content:flex-end; align-items:center; gap:1rem; flex-wrap:wrap;"><a class="btn btn-primary" href="./programs.html">View Programs</a></div></div></div></div></section>
</main>
''', 'About Crestfield College', 'Learn about Crestfield College, our mission, values, leadership, and sample institutional profile.', 'about-page'),
    'programs.html': page_shell('''
<main>
  <section class="page-hero"><div class="container"><div class="breadcrumbs">Home / Academics / Programs</div><h1>Academic Programs</h1><p>These sample program listings are illustrative and clearly labeled as educational portfolio content.</p></div></section>
  <section class="section"><div class="container"><div class="filter-bar reveal"><div class="field"><label for="programSearch">Search programs</label><input id="programSearch" type="search" placeholder="Search by title or keyword" /></div><div class="field"><label for="facultyFilter">Faculty</label><select id="facultyFilter"><option value="all">All faculties</option><option value="Faculty of Computing">Faculty of Computing</option><option value="School of Analytics">School of Analytics</option><option value="School of Engineering">School of Engineering</option><option value="School of Business">School of Business</option><option value="School of Media &amp; Communication">School of Media &amp; Communication</option></select></div><div class="field"><label for="qualificationFilter">Qualification</label><select id="qualificationFilter"><option value="all">All qualifications</option><option value="Bachelor">Bachelor</option><option value="Diploma">Diploma</option></select></div><button id="resetFilters" class="btn btn-secondary" type="button">Reset filters</button></div><div id="programGrid" class="program-grid"></div><div id="programEmpty" class="empty-state"><h3>No programs match your current search.</h3><p>Try changing your filters or resetting the search criteria.</p></div></div></section>
</main>
''', 'Programs | Crestfield College', 'Browse illustrative undergraduate programs at Crestfield College and use the live search and filters.', 'programs-page'),
    'admissions.html': page_shell('''
<main>
  <section class="page-hero"><div class="container"><div class="breadcrumbs">Home / Admissions</div><h1>Admissions</h1><p>Follow the steps below to explore the admissions journey. This demo form is intentionally front-end only and does not submit to a real college database.</p></div></section>
  <section class="section"><div class="container"><div class="progress-steps reveal" aria-label="Application progress"><div class="progress-step active">1. Personal</div><div class="progress-step">2. Contact</div><div class="progress-step">3. Academics</div><div class="progress-step">4. Program</div><div class="progress-step">5. Review</div></div><div class="form-panel reveal"><form id="admissionsForm" novalidate><div class="form-step active" data-step="1"><h2>Step 1: Personal information</h2><div class="form-row"><div class="field-group"><label for="firstName">First name</label><input id="firstName" name="firstName" type="text" required /><div class="error-message">This field is required.</div></div><div class="field-group"><label for="lastName">Last name</label><input id="lastName" name="lastName" type="text" required /><div class="error-message">This field is required.</div></div></div><div class="form-row" style="margin-top:1rem;"><div class="field-group"><label for="dateOfBirth">Date of birth</label><input id="dateOfBirth" name="dateOfBirth" type="date" required /><div class="error-message">This field is required.</div></div><div class="field-group"><label for="nationality">Nationality</label><input id="nationality" name="nationality" type="text" required /><div class="error-message">This field is required.</div></div></div></div><div class="form-step" data-step="2"><h2>Step 2: Contact details</h2><div class="form-row"><div class="field-group"><label for="emailAddress">Email</label><input id="emailAddress" name="emailAddress" type="email" required /><div class="error-message">This field is required.</div></div><div class="field-group"><label for="phoneNumber">Phone number</label><input id="phoneNumber" name="phoneNumber" type="tel" required /><div class="error-message">This field is required.</div></div></div><div class="form-row" style="margin-top:1rem;"><div class="field-group"><label for="addressLine">Address</label><input id="addressLine" name="addressLine" type="text" required /><div class="error-message">This field is required.</div></div><div class="field-group"><label for="city">City</label><input id="city" name="city" type="text" required /><div class="error-message">This field is required.</div></div></div></div><div class="form-step" data-step="3"><h2>Step 3: Academic background</h2><div class="form-row"><div class="field-group"><label for="schoolName">School or institution</label><input id="schoolName" name="schoolName" type="text" required /><div class="error-message">This field is required.</div></div><div class="field-group"><label for="qualificationLevel">Qualification level</label><select id="qualificationLevel" name="qualificationLevel" required><option value="">Select an option</option><option>High school diploma</option><option>Associate degree</option><option>Undergraduate</option><option>Postgraduate</option></select><div class="error-message">This field is required.</div></div></div><div class="form-row" style="margin-top:1rem;"><div class="field-group"><label for="gpaScore">Academic average / GPA</label><input id="gpaScore" name="gpaScore" type="text" required /><div class="error-message">This field is required.</div></div><div class="field-group"><label for="intakeTerm">Preferred intake term</label><select id="intakeTerm" name="intakeTerm" required><option value="">Select a term</option><option>Fall 2026</option><option>Spring 2027</option><option>Summer 2027</option></select><div class="error-message">This field is required.</div></div></div></div><div class="form-step" data-step="4"><h2>Step 4: Program selection</h2><div class="field-group"><label for="programChoice">Chosen program</label><select id="programChoice" name="programChoice" required><option value="">Select a program</option></select><div class="error-message">This field is required.</div></div><div class="field-group" style="margin-top:1rem;"><label for="statement">Why this program?</label><textarea id="statement" name="statement" required placeholder="Tell us about your interests and goals."></textarea><div class="error-message">This field is required.</div></div></div><div class="form-step" data-step="5"><h2>Step 5: Review and confirmation</h2><p>Please review the information you have entered before submitting a demo application.</p></div><div class="form-actions"><button id="prevStep" class="btn btn-secondary" type="button">Previous</button><button id="nextStep" class="btn btn-primary" type="button">Next</button><button id="submitApplication" class="btn btn-primary" type="submit" style="display:none;">Submit demo application</button></div><div id="formSuccess" class="form-success" aria-live="polite"></div></form></div></div></section>
</main>
''', 'Admissions | Crestfield College', 'Review admissions requirements and explore a sample multi-step application form for Crestfield College.', 'admissions-page'),
    'campus-life.html': page_shell('''
<main>
  <section class="page-hero"><div class="container"><div class="breadcrumbs">Home / Campus Life</div><h1>Campus Life</h1><p>Student life at Crestfield is built around belonging, wellbeing, creativity, and community development.</p></div></section>
  <section class="section"><div class="container page-grid"><div class="reveal"><span class="eyebrow">Student experience</span><h2>Where learning extends beyond the classroom.</h2><p>Our campus culture encourages students to take initiative, connect with others, and contribute to a vibrant intellectual community.</p><ul class="card-list"><li>Student organizations that support leadership and cultural expression</li><li>Wellbeing programs and support services for balanced student life</li><li>Active recreational opportunities and sports participation</li><li>Events that foster belonging, creativity, and entrepreneurship</li></ul></div><div class="card reveal"><h3>Campus support</h3><p>From orientation to graduation, students have access to academic advising, counseling, accommodations planning, and personal development resources.</p></div></div></section>
  <section class="section" style="background: rgba(255,255,255,0.7);"><div class="container"><div class="section-header reveal"><div><span class="eyebrow">Clubs & societies</span><h2>Find your community.</h2></div></div><div class="facility-grid"><article class="card reveal"><h3>Innovation Society</h3><p>Students prototype ideas, solve challenges, and connect with entrepreneurs and mentors.</p></article><article class="card reveal"><h3>Media & Arts Club</h3><p>Explore podcasts, storytelling, photography, brand content, and campus events.</p></article><article class="card reveal"><h3>Sports Council</h3><p>Join recreational leagues, fitness activities, and inter-campus athletic experiences.</p></article></div></div></section>
  <section class="section"><div class="container"><div class="section-header reveal"><div><span class="eyebrow">Accommodation</span><h2>Comfortable and connected living spaces.</h2></div></div><div class="page-grid"><div class="card reveal"><h3>On-campus residence</h3><p>Secure, student-focused housing with common areas, study lounges, wellness access, and roommate support.</p></div><div class="card reveal"><h3>Off-campus support</h3><p>Students can access guidance on local housing options, budgeting, and transition planning for life beyond campus.</p></div></div></div></section>
  <section class="section" style="background: rgba(255,255,255,0.7);"><div class="container"><div class="section-header reveal"><div><span class="eyebrow">Gallery</span><h2>Moments from campus life.</h2></div></div><div class="image-grid reveal"><figure data-gallery-image="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=1200&q=80"><img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=900&q=80" alt="Students collaborating in a classroom" /><div class="gallery-caption">Student collaboration</div></figure><figure data-gallery-image="https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=1200&q=80"><img src="https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=900&q=80" alt="Students in a campus forum" /><div class="gallery-caption">Campus forum</div></figure><figure data-gallery-image="https://images.unsplash.com/photo-1541534401786-2077eed87a74?auto=format&fit=crop&w=1200&q=80"><img src="https://images.unsplash.com/photo-1541534401786-2077eed87a74?auto=format&fit=crop&w=900&q=80" alt="Students playing sport" /><div class="gallery-caption">Recreation</div></figure><figure data-gallery-image="https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=1200&q=80"><img src="https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=900&q=80" alt="Students enjoying campus cultural event" /><div class="gallery-caption">Cultural event</div></figure><figure data-gallery-image="https://images.unsplash.com/photo-1498243691581-b145c3f54a5a?auto=format&fit=crop&w=1200&q=80"><img src="https://images.unsplash.com/photo-1498243691581-b145c3f54a5a?auto=format&fit=crop&w=900&q=80" alt="Modern technology lab" /><div class="gallery-caption">Innovation lab</div></figure><figure data-gallery-image="https://images.unsplash.com/photo-1517486808906-6ca8b3d7a5be?auto=format&fit=crop&w=1200&q=80"><img src="https://images.unsplash.com/photo-1517486808906-6ca8b3d7a5be?auto=format&fit=crop&w=900&q=80" alt="Students in a library or study space" /><div class="gallery-caption">Study lounge</div></figure></div></div></section>
  <div id="galleryLightbox" class="lightbox" aria-hidden="true"><div class="lightbox-inner"><button class="lightbox-close" id="lightboxClose" type="button" aria-label="Close image view">×</button><img id="lightboxImage" src="" alt="Expanded campus gallery image" /></div></div>
</main>
''', 'Campus Life | Crestfield College', 'Explore student life, clubs, accommodation, and gallery highlights at Crestfield College.', 'campus-page'),
    'news.html': page_shell('''
<main>
  <section class="page-hero"><div class="container"><div class="breadcrumbs">Home / News &amp; Events</div><h1>News &amp; Events</h1><p>Stay connected with storylines, campus updates, and exciting opportunities for students and family visitors.</p></div></section>
  <section class="section"><div class="container news-filter-wrap"><div class="reveal"><div class="filter-bar"><div class="field"><label for="newsSearch">Search stories</label><input id="newsSearch" type="search" placeholder="Search by title or keyword" /></div><div class="field"><label for="newsCategory">Category</label><select id="newsCategory"><option value="all">All items</option><option value="Campus">Campus</option><option value="Sustainability">Sustainability</option><option value="Student Success">Student Success</option><option value="Admissions">Admissions</option><option value="Innovation">Innovation</option><option value="Community">Community</option></select></div></div></div><div class="card reveal"><h3>Featured article</h3><p>Explore what is happening across Crestfield, from cutting-edge research to student-led innovation and campus community growth.</p><a class="btn btn-primary" href="./news-detail.html?slug=research-innovation&type=news">Read the feature</a></div></div><div class="container" style="margin-top:2rem;"><div id="newsGrid" class="news-grid"><article class="card news-card reveal" data-title="Research and Innovation Lab Opens at Crestfield" data-category="Campus"><div class="meta"><span>Campus</span><span>Apr 11</span></div><h3>Research and Innovation Lab Opens at Crestfield</h3><p>A new campus lab expands hands-on learning, entrepreneurship, and interdisciplinary collaboration.</p><a class="btn btn-secondary" href="./news-detail.html?slug=research-innovation&type=news">Read article</a></article><article class="card news-card reveal" data-title="New Solar Energy Initiatives Reduce Campus Emissions" data-category="Sustainability"><div class="meta"><span>Sustainability</span><span>Mar 29</span></div><h3>New Solar Energy Initiatives Reduce Campus Emissions</h3><p>Energy-saving projects and student research are helping the campus pursue greener operations.</p><a class="btn btn-secondary" href="./news-detail.html?slug=new-solar&type=news">Read article</a></article><article class="card news-card reveal" data-title="Career Network Connects Students with Industry Leaders" data-category="Student Success"><div class="meta"><span>Student Success</span><span>Mar 15</span></div><h3>Career Network Connects Students with Industry Leaders</h3><p>Students meet alumni and employers through networking events designed to build confidence and career direction.</p><a class="btn btn-secondary" href="./news-detail.html?slug=career-network&type=news">Read article</a></article><article class="card event-card reveal" data-title="Future Leaders Open Day" data-category="Admissions"><div class="meta"><span>Admissions</span><span>May 16</span></div><h3>Future Leaders Open Day</h3><p>Tour campus, meet faculty, and learn more about the programs, support systems, and admissions process.</p><a class="btn btn-secondary" href="./event-detail.html?slug=open-day">View event</a></article><article class="card event-card reveal" data-title="Global Challenge Hackathon" data-category="Innovation"><div class="meta"><span>Innovation</span><span>June 4</span></div><h3>Global Challenge Hackathon</h3><p>Students form cross-disciplinary teams and solve meaningful real-world issues with expert guidance.</p><a class="btn btn-secondary" href="./event-detail.html?slug=hackathon">View event</a></article><article class="card event-card reveal" data-title="Mentor Connect Week" data-category="Community"><div class="meta"><span>Community</span><span>June 24</span></div><h3>Mentor Connect Week</h3><p>Students gain advice and insight from alumni and professionals across disciplines and industries.</p><a class="btn btn-secondary" href="./event-detail.html?slug=mentor">View event</a></article></div><div id="newsEmpty" class="empty-state"><h3>No news or events match your search.</h3><p>Adjust your filters to explore more campus updates.</p></div></div></div></section>
</main>
''', 'News & Events | Crestfield College', 'Read campus stories, event updates, and sample student-focused articles from Crestfield College.', 'news-page'),
    'contact.html': page_shell('''
<main>
  <section class="page-hero"><div class="container"><div class="breadcrumbs">Home / Contact</div><h1>Contact Crestfield</h1><p>Have questions about admissions, programs, or campus life? Reach out and our support team will guide you.</p></div></section>
  <section class="section"><div class="container contact-parts"><div class="form-panel reveal"><h2>Send us a message</h2><form id="contactForm" novalidate><div class="field-group"><label for="contactName">Full name</label><input id="contactName" type="text" name="name" required /><div class="error-message">Please enter your name.</div></div><div class="field-group" style="margin-top:1rem;"><label for="contactEmail">Email address</label><input id="contactEmail" type="email" name="email" required /><div class="error-message">Please enter a valid email.</div></div><div class="field-group" style="margin-top:1rem;"><label for="contactSubject">Subject</label><input id="contactSubject" type="text" name="subject" required /><div class="error-message">Please enter a subject.</div></div><div class="field-group" style="margin-top:1rem;"><label for="contactMessage">Message</label><textarea id="contactMessage" name="message" required></textarea><div class="error-message">Please enter your message.</div></div><div class="form-actions"><button class="btn btn-primary" type="submit">Submit enquiry</button></div><div id="contactStatus" aria-live="polite" style="margin-top:1rem; font-weight:600;"></div></form></div><div class="card reveal"><h3>Contact details</h3><ul class="card-list"><li><strong>Address:</strong> 101 Academy Way, Crestfield, CT 90002</li><li><strong>Email:</strong> hello@crestfieldcollege.edu</li><li><strong>Phone:</strong> +1 (555) 014-9832</li><li><strong>Office hours:</strong> Mon–Fri, 8:00am–5:00pm</li></ul><div style="margin-top:1.5rem; background:#f3f6fb; border-radius:16px; padding:1rem; min-height:220px; display:grid; place-items:center; color:#51637a; font-weight:700;">Map placeholder</div></div></div></section>
  <section class="section" style="background: rgba(255,255,255,0.7);"><div class="container"><div class="section-header reveal"><div><span class="eyebrow">FAQ</span><h2>Frequently asked questions.</h2></div></div><div class="faq-list reveal"><div class="faq-item open"><button class="faq-question" type="button" aria-expanded="true"><span>How do I apply for admission?</span><span class="toggle-sign">+</span></button><div class="faq-answer"><p>Visit the admissions page, complete the multi-step form, and submit all required documents for review.</p></div></div><div class="faq-item"><button class="faq-question" type="button" aria-expanded="false"><span>Do you offer campus tours?</span><span class="toggle-sign">+</span></button><div class="faq-answer"><p>Yes. Prospective families and students can schedule guided campus visits and open day appointments.</p></div></div><div class="faq-item"><button class="faq-question" type="button" aria-expanded="false"><span>Can I speak with an admissions adviser?</span><span class="toggle-sign">+</span></button><div class="faq-answer"><p>Absolutely. Contact our admissions office by email or phone to arrange a consultation.</p></div></div></div></div></section>
</main>
''', 'Contact | Crestfield College', 'Get in touch with Crestfield College for admissions, program, and campus questions.', 'contact-page'),
    'student-portal.html': page_shell('''
<main class="portal-wrap"><div class="portal-card reveal"><div class="eyebrow">Student portal</div><h1>Welcome back</h1><div class="portal-demo">Demo mode only: this front-end example does not authenticate real students or store personal credentials.</div><form id="portalForm" novalidate><div class="field-group"><label for="studentEmail">Student ID or email</label><input id="studentEmail" type="text" name="studentEmail" placeholder="student@crestfieldcollege.edu" required /></div><div class="field-group" style="margin-top:1rem;"><label for="password">Password</label><div class="password-toggle"><input id="password" type="password" name="password" required /><button id="togglePassword" type="button" aria-label="Show or hide password">Show</button></div></div><div class="checkbox-row" style="margin-top:1rem;"><label for="rememberMe"><input id="rememberMe" type="checkbox" /> Remember me</label><a href="#" aria-label="Forgot password">Forgot password?</a></div><div class="form-actions" style="margin-top:1.2rem;"><button class="btn btn-primary" type="submit" style="width:100%;">Sign in</button></div><div id="portalStatus" aria-live="polite" style="margin-top:1rem; font-weight:600;"></div></form></div></main>
''', 'Student Portal | Crestfield College', 'Demo-only student portal login page for a static college website built with HTML, CSS, and JavaScript.', 'portal-page'),
    '404.html': page_shell('''
<main class="section"><div class="container" style="display:grid; place-items:center; text-align:center;"><div class="card reveal" style="max-width: 620px;"><span class="eyebrow">404 Error</span><h1>Page not found</h1><p>The page you are looking for may have moved, or the link may be outdated. Use the navigation below to continue exploring Crestfield College.</p><div class="hero-actions" style="justify-content:center;"><a class="btn btn-primary" href="./index.html">Go to homepage</a><a class="btn btn-secondary" href="./programs.html">Browse programs</a></div></div></div></main>
''', 'Page Not Found | Crestfield College', 'The requested page could not be found.', 'error-page'),
    'news-detail.html': page_shell('''<main class="section"><div class="container"><div id="detailContent"></div></div></main>''', 'News Detail | Crestfield College', 'Detailed sample article page for Crestfield College.', 'news-detail-page'),
    'event-detail.html': page_shell('''<main class="section"><div class="container"><div id="detailContent"></div></div></main>''', 'Event Detail | Crestfield College', 'Detailed sample event page for Crestfield College.', 'event-detail-page'),
    'program-detail.html': page_shell('''<main class="section"><div class="container"><div id="programDetail"></div></div></main>''', 'Program Detail | Crestfield College', 'Sample program detail page for Crestfield College.', 'program-detail-page'),
}

# write files
for relative, content in pages.items():
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')

(root / 'css' / 'style.css').write_text(css, encoding='utf-8')
(root / 'js' / 'main.js').write_text(js_main, encoding='utf-8')
(root / 'js' / 'programs.js').write_text(js_programs, encoding='utf-8')
(root / 'js' / 'admissions.js').write_text(js_admissions, encoding='utf-8')
(root / 'js' / 'contact.js').write_text(js_contact, encoding='utf-8')
(root / 'README.md').write_text('''# Crestfield College Website\n\nThis project is a static, responsive college website built with plain HTML, CSS, and JavaScript. It is designed to work without a build step and is suitable for manual upload to GitHub Pages.\n\n## Project structure\n\n- `index.html` – homepage\n- `about.html` – institution overview\n- `programs.html` – program catalog with search and filters\n- `admissions.html` – admissions information and multi-step form demo\n- `campus-life.html` – campus experience and gallery\n- `news.html` – news and events discovery page\n- `contact.html` – contact form and FAQs\n- `student-portal.html` – login page mockup\n- `css/style.css` – shared styles\n- `js/main.js` – shared interactions\n- `js/programs.js` – program card rendering\n- `js/admissions.js` – admissions options\n- `js/contact.js` – contact interaction\n\n## Run locally\n\nOpen any page directly in a browser, or run a local static server from the project directory:\n\n```bash\npython -m http.server 8000\n```\n\nThen visit: http://localhost:8000/\n\n## Upload to GitHub\n\n1. Create a repository in GitHub.\n2. Push the project files to the repository root.\n3. In GitHub, open **Settings** → **Pages**.\n4. Set source to **Deploy from a branch** and choose `main` or `master`.\n5. Ensure the root folder contains `index.html`.\n6. Save the configuration to enable GitHub Pages.\n\n## Notes\n\n- The site is intentionally static and requires no Node.js or npm install step.\n- Forms are front-end demos only and do not send real data to a backend.\n- Content is sample and clearly labeled as illustrative for a portfolio website.\n''', encoding='utf-8')
(root / '.nojekyll').write_text('', encoding='utf-8')
print('Website files created successfully.')

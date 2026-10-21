
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

  const source = type === 'news' ? data.news : type === 'events' ? data.events : [...data.news, ...data.events];
  const record = source.find((item) => item.slug === slug);
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

  const searchField = document.getElementById('programSearch');
  const facultyField = document.getElementById('facultyFilter');
  const qualificationField = document.getElementById('qualificationFilter');
  const emptyState = document.getElementById('programEmpty');

  const getCards = () => [...list.querySelectorAll('.program-card')];

  const applyFilters = () => {
    const cards = getCards();
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

  if (list.dataset.programSearchBound !== 'true') {
    [searchField, facultyField, qualificationField].forEach((field) => field?.addEventListener('input', applyFilters));
    [facultyField, qualificationField].forEach((field) => field?.addEventListener('change', applyFilters));
    document.getElementById('resetFilters')?.addEventListener('click', () => {
      if (searchField) searchField.value = '';
      if (facultyField) facultyField.value = 'all';
      if (qualificationField) qualificationField.value = 'all';
      applyFilters();
    });
    list.dataset.programSearchBound = 'true';
  }

  applyFilters();
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
  document.addEventListener('programs:rendered', setupProgramSearch);
  setupNewsSearch();
  setupAdmissionsForm();
  setupPortalForm();
  document.getElementById('year')?.replaceChildren(String(new Date().getFullYear()));
});

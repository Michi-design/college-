
const setupContactBehavior = () => {
  const form = document.getElementById('contactForm');
  if (!form) return;

  const fields = {
    name: document.getElementById('contactName'),
    email: document.getElementById('contactEmail'),
    subject: document.getElementById('contactSubject'),
    message: document.getElementById('contactMessage')
  };

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const status = document.getElementById('contactStatus');
    const fieldEntries = Object.entries(fields);
    let isValid = true;

    fieldEntries.forEach(([key, field]) => {
      const value = field.value.trim();
      const error = field.closest('.field-group')?.querySelector('.error-message');
      field.classList.remove('field-error');
      if (error) error.style.display = 'none';

      if (key === 'email') {
        if (!value || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
          field.classList.add('field-error');
          if (error) {
            error.textContent = 'Please enter a valid email address.';
            error.style.display = 'block';
          }
          isValid = false;
        }
        return;
      }

      if (!value) {
        field.classList.add('field-error');
        if (error) {
          const message = key === 'subject' ? 'Please enter a subject.' : key === 'name' ? 'Please enter your name.' : 'Please enter your message.';
          error.textContent = message;
          error.style.display = 'block';
        }
        isValid = false;
      }
    });

    if (!isValid) {
      status.textContent = 'Please correct the highlighted fields.';
      status.style.color = '#b42318';
      return;
    }

    status.textContent = 'Demo form submitted. No backend email service is attached.';
    status.style.color = '#1d5b3b';
    form.reset();
  });
};

document.addEventListener('DOMContentLoaded', setupContactBehavior);

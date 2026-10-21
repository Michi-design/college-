# Crestfield College Website

This project is a static, responsive college website built with plain HTML, CSS, and JavaScript. It is designed to work without a build step and is suitable for manual upload to GitHub Pages.

## Project structure

- `index.html` – homepage
- `about.html` – institution overview
- `programs.html` – program catalog with search and filters
- `admissions.html` – admissions information and multi-step form demo
- `campus-life.html` – campus experience and gallery
- `news.html` – news and events discovery page
- `contact.html` – contact form and FAQs
- `student-portal.html` – login page mockup
- `css/style.css` – shared styles
- `js/main.js` – shared interactions
- `js/programs.js` – program card rendering
- `js/admissions.js` – admissions options
- `js/contact.js` – contact interaction

## Run locally

Open any page directly in a browser, or run a local static server from the project directory:

```bash
python -m http.server 8000
```

Then visit: http://localhost:8000/

## Upload to GitHub

1. Create a repository in GitHub.
2. Push the project files to the repository root.
3. In GitHub, open **Settings** → **Pages**.
4. Set source to **Deploy from a branch** and choose `main` or `master`.
5. Ensure the root folder contains `index.html`.
6. Save the configuration to enable GitHub Pages.

## Notes

- The site is intentionally static and requires no Node.js or npm install step.
- Forms are front-end demos only and do not send real data to a backend.
- Content is sample and clearly labeled as illustrative for a portfolio website.

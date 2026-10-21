
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
  document.dispatchEvent(new CustomEvent('programs:rendered'));
};

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', renderPrograms);
} else {
  renderPrograms();
}

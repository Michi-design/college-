
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

// Category and Context Label Functionality
document.addEventListener('DOMContentLoaded', function() {
  const categoryLabels = document.querySelectorAll('.category-options label');
  const contextLabels = document.querySelectorAll('.context-options label');

  const toggleSelectedClass = (checkbox, label) => {
    if (checkbox.checked) {
      label.classList.add('selected');
    } else {
      label.classList.remove('selected');
    }
  };

  categoryLabels.forEach(label => {
    const checkbox = document.getElementById(label.getAttribute('for'));

    label.addEventListener('click', () => {
      checkbox.checked = !checkbox.checked;
      toggleSelectedClass(checkbox, label);
    });

    toggleSelectedClass(checkbox, label);
  });

  contextLabels.forEach(label => {
    const checkbox = document.getElementById(label.getAttribute('for'));

    label.addEventListener('click', () => {
      checkbox.checked = !checkbox.checked;
      toggleSelectedClass(checkbox, label);
    });

    toggleSelectedClass(checkbox, label);
  });
});


// Label functionality
document.addEventListener('DOMContentLoaded', function() {
  const enjoyLabels = document.querySelectorAll('.enjoyment-options label');
  const proficientLabels = document.querySelectorAll('.proficiency-options label');
  const experienceLabels = document.querySelectorAll('.experience-options label');

  // CGPT help for first label (repeated and modified to suit for the rest)
  enjoyLabels.forEach(label => {
    label.addEventListener('click', () => {
      // Uncheck all labels and remove 'selected' class from all labels
      enjoyLabels.forEach(lbl => lbl.classList.remove('selected'));

      // Get the radio associated with the clicked label
      const radio = document.getElementById(label.getAttribute('for'));

      // Check the clicked radio button and add 'selected' class to the clicked label
      radio.checked = true;
      label.classList.add('selected');
    });
  });

  proficientLabels.forEach(label => {
    label.addEventListener('click', () => {
      // Uncheck all labels and remove 'selected' class from all labels
      proficientLabels.forEach(lbl => lbl.classList.remove('selected'));

      // Get the radio associated with the clicked label
      const radio = document.getElementById(label.getAttribute('for'));

      // Check the clicked radio button and add 'selected' class to the clicked label
      radio.checked = true;
      label.classList.add('selected');
    });
  });

  experienceLabels.forEach(label => {
    label.addEventListener('click', () => {
      // Uncheck all labels and remove 'selected' class from all labels
      experienceLabels.forEach(lbl => lbl.classList.remove('selected'));

      // Get the radio associated with the clicked label
      const radio = document.getElementById(label.getAttribute('for'));

      // Check the clicked radio button and add 'selected' class to the clicked label
      radio.checked = true;
      label.classList.add('selected');
    });
  });
});




// Search Bar
document.getElementById('searchInput').addEventListener('input', function() {
  let query = this.value;
  fetch(`/search-skills/?search=${query}`)
    .then(response => response.json())
    .then(data => {
      const autocompleteList = document.getElementById('autocompleteList');
      autocompleteList.innerHTML = '';
      data.suggestions.forEach(function(skill) {
        const li = document.createElement('li');
        li.textContent = skill.name;
        autocompleteList.appendChild(li);
      });
      autocompleteList.classList.remove('hidden');
    });
});
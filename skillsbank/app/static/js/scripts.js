/*
const apiUrl = "http://localhost:3001/skills";
      const searchInput = document.getElementById('searchInput');
      const autocompleteList = document.getElementById('autocompleteList');
      const skillList = document.getElementById('skillList');
      const skillsFoundList = document.getElementById('skillsFoundList');
      const noSkillsMessage = document.getElementById('noSkillsMessage');
  
      let skills = [];
      let foundSkills = [];
  
      function fetchSkills() {
        fetch(apiUrl)
          .then(response => response.json())
          .then(data => {
            skills = data;
            renderSkills();
            updateSkillCounts(); // Call after fetching skills
          });
      }
  
      function renderSkills() {
        skillList.innerHTML = ''; // Clear existing list
  
        skills.forEach((skill) => {
          const listItem = document.createElement('li');
          listItem.className = 'text-gray-700 flex items-center gap-2 px-4 py-1 cursor-pointer hover:bg-gray-100 rounded';
          listItem.innerHTML = `<span>${skill.name}</span>`;
  
          // Add click event to add the skill to the "Skills Found" list
          listItem.addEventListener('click', () => {
            if (!foundSkills.some((foundSkill) => foundSkill.name === skill.name)) {
              foundSkills.push(skill); // Add skill to the "Skills Found" list
              renderFoundSkills(); // Update the "Skills Found" list
            }
          });
  
          skillList.appendChild(listItem);
        });
      }
  
      function renderFoundSkills() {
        skillsFoundList.innerHTML = ''; // Clear the found skills list
  
        foundSkills.forEach((skill, index) => {
          const skillItem = document.createElement('li');
          skillItem.className = 'text-gray-700 flex items-center justify-between gap-2 p-2 border-b';
  
          skillItem.innerHTML = `
            <div class="flex items-center gap-2">
              <span class="text-green-500">&#10003;</span>
              <span>${skill.name}</span>
            </div>
            <button class="text-red-500 hover:text-red-700 focus:outline-none remove-skill-button" aria-label="Remove skill">
              &#10005;
            </button>
          `;
  
          // Add event listener for the remove button
          const removeButton = skillItem.querySelector('.remove-skill-button');
          removeButton.addEventListener('click', () => {
            removeSkillFromFoundList(index);
          });
  
          skillsFoundList.appendChild(skillItem);
        });
      }
  
      function removeSkillFromFoundList(index) {
        foundSkills.splice(index, 1); // Remove the skill from the foundSkills array
        renderFoundSkills(); // Re-render the list
      }
  
      function handleSearchInput() {
        const inputValue = searchInput.value.trim();
        const queries = inputValue.split(',').map(q => q.trim()).filter(Boolean);
  
        const currentQuery = queries[queries.length - 1]?.toLowerCase() || '';
  
        if (currentQuery) {
          const filteredSkills = skills.filter(skill =>
            skill.name.toLowerCase().includes(currentQuery)
          );
  
          autocompleteList.innerHTML = '';
  
          if (filteredSkills.length > 0) {
            noSkillsMessage.classList.add('hidden'); // Hide "No skills found" message
            autocompleteList.classList.remove('hidden'); // Show dropdown
  
            filteredSkills.forEach(skill => {
              const item = document.createElement('li');
              item.textContent = skill.name;
  
              item.addEventListener('click', () => {
                addSkillToFoundList(skill, queries);
                autocompleteList.classList.add('hidden'); // Hide dropdown
              });
  
              autocompleteList.appendChild(item);
            });
          } else {
            autocompleteList.classList.add('hidden');
            noSkillsMessage.classList.remove('hidden'); // Show "No skills found" message
          }
        } else {
          autocompleteList.classList.add('hidden');
          noSkillsMessage.classList.add('hidden');
        }
      }
  
      function addSkillToFoundList(skill, queries) {
        if (!foundSkills.includes(skill)) {
          foundSkills.push(skill);
          renderFoundSkills();
  
          // Update input with selected skill
          queries[queries.length - 1] = skill.name;
          searchInput.value = queries.join(', ') + ', ';
        }
      }
  
      searchInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
          event.preventDefault(); // Prevent form submission or default behavior
          handleEnterKey();
        }
      });
  
      function handleEnterKey() {
        const inputValue = searchInput.value.trim();
        const queries = inputValue.split(',').map((query) => query.trim()).filter(Boolean);
  
        // Check each query and add valid skills to the "Skills Found" list
        queries.forEach((query) => {
          const skill = skills.find((s) => s.name.toLowerCase() === query.toLowerCase());
          if (skill && !foundSkills.some((foundSkill) => foundSkill.name === skill.name)) {
            foundSkills.push(skill); // Add valid skill
          }
        });
  
        // Update the display for the "Skills Found" list
        renderFoundSkills();
        updateSkillCounts();
        searchInput.value = '';
  
        autocompleteList.classList.add('hidden'); // Hide the autocomplete dropdown
        noSkillsMessage.classList.add('hidden'); // Hide "No skills found" message
      }
  
      searchInput.addEventListener('input', handleSearchInput);
      
      function updateSkillCounts() {
        const skillsTotalCount = document.getElementById('skillsTotalCount');
        const skillsFoundCount = document.getElementById('skillsFoundCount');
        
        skillsTotalCount.textContent = `(${skills.length})`; // Update total skill count
        skillsFoundCount.textContent = `(${foundSkills.length})`; // Update found skill count
      }
  
      // Initialize the skill list when the page loads
      fetchSkills();

      */

document.addEventListener('DOMContentLoaded', function () {
  const categoryLabels = document.querySelectorAll('.category-options label');

  categoryLabels.forEach(label => {
    label.addEventListener('click', () => {
      const checkbox = document.getElementById(label.getAttribute('for'));
      checkbox.checked = !checkbox.checked;
      label.classList.toggle('selected');
    });
  });
});
      
      
document.addEventListener('DOMContentLoaded', function () {
  const contextLabels = document.querySelectorAll('.context-options label');

  contextLabels.forEach(label => {
    label.addEventListener('click', () => {
      const checkbox = document.getElementById(label.getAttribute('for'));
      checkbox.checked = !checkbox.checked;
      label.classList.toggle('selected');
    });
  });
});

document.addEventListener('DOMContentLoaded', function () {
  const enjoyLabels = document.querySelectorAll('.enjoyment-options label');
  const proficientLabels = document.querySelectorAll('.proficiency-options label');
  const experienceLabels = document.querySelectorAll('.experience-options label');

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

document.addEventListener('DOMContentLoaded', function () {
  // Fetch the character data from the URL
  fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
      // Extract the character name from the data
      const characterName = data.name;
      // Display the character name in the div#character
      document.getElementById('character').textContent = characterName;
    })
    .catch(error => {
      console.error('Error:', error);
    });
});

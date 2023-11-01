document.addEventListener('DOMContentLoaded', function () {
  // Fetch the list of movies from the URL
  fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      // Extract movie titles from the data
      const movies = data.results;
      const ul = document.getElementById('list_movies');

      // Loop through the movie data and add each title to the UL
      movies.forEach(movie => {
        const li = document.createElement('li');
        li.textContent = movie.title;
        ul.appendChild(li);
      });
    })
    .catch(error => {
      console.error('Error:', error);
    });
});

#!/usr/bin/node

const request = require('request');

// Check if the Star Wars API URL is provided as an argument
if (process.argv.length !== 3) {
  process.exit(1); // Exit with an error code
}

// Get the Star Wars API URL from the command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the Star Wars API films endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to retrieve movie information. Status Code: ${response.statusCode}`);
  } else {
    try {
      const filmsData = JSON.parse(body);
      const characterId = '18'; // Wedge Antilles character ID

      // Filter movies that include "Wedge Antilles"
      const moviesWithWedge = filmsData.results.filter(movie => {
        return movie.characters.includes(characterId);
      });

      console.log(moviesWithWedge.length);
    } catch (parseError) {
      console.error('Error occurred while parsing the response:');
      console.error(parseError);
    }
  }
});

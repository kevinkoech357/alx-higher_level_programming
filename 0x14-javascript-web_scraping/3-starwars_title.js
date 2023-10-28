#!/usr/bin/node

const request = require('request');

// Check if a movie ID is provided as an argument
if (process.argv.length !== 3) {
  process.exit(1); // Exit with an error code
}

// Get the movie ID from the command line arguments
const id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${id}`;

// Make a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to retrieve movie information. Status Code: ${response.statusCode}`);
  } else {
    try {
      const movieData = JSON.parse(body);
      console.log('Title:', movieData.title);
    } catch (parseError) {
      console.error('Error occurred while parsing the response:');
      console.error(parseError);
    }
  }
});

#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(filmUrl, (error, response, filmBody) => {
  if (error) {
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    process.exit(1);
  }

  const filmData = JSON.parse(filmBody);
  const characterUrls = filmData.characters;

  if (characterUrls.length === 0) {
    process.exit(0); // Exit gracefully with a success status code
  }

  // Create an array of promises for character requests
  const characterPromises = characterUrls.map((charUrl) => {
    return new Promise((resolve, reject) => {
      request(charUrl, (charError, charResponse, charBody) => {
        if (charError) {
          reject(charError);
        } else if (charResponse.statusCode === 200) {
          resolve(JSON.parse(charBody).name);
        } else {
          process.exit(1);
        }
      });
    });
  });

  // Execute all character requests in parallel and handle the results
  Promise.all(characterPromises)
    .then((characterNames) => {
      characterNames.forEach((name) => {
        console.log(name);
      });
    })
    .catch((err) => {
      console.error(err);
    });
});

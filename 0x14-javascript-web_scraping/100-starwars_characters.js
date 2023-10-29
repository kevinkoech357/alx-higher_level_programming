#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    process.exit(1);
  }

  const characters = JSON.parse(body).characters;

  if (characters.length === 0) {
    process.exit(0);
  } else {
    characters.forEach((charUrl) => {
      request(charUrl, (err, resp, bodyChar) => {
        if (err) {
          process.exit(1);
        } else {
          const characterName = JSON.parse(bodyChar).name;
          console.log(characterName);
        }
      });
    });
  }
});

#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Check if both URL and file path arguments are provided
if (process.argv.length !== 4) {
  process.exit(1); // Exit with an error code
}

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error(writeError);
      } else {
        console.log(`${filePath} has been successfully written.`);
      }
    });
  }
});

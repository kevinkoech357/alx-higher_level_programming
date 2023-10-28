#!/usr/bin/node

const request = require('request');

// Check if a URL is provided as an argument
if (process.argv.length !== 3) {
  console.error('Usage: node get_request_status.js <URL>');
  process.exit(1); // Exit with an error code
}

// Get the URL from the command line arguments
const url = process.argv[2];

// Make a GET request to the specified URL
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('Status Code:', response.statusCode);
  }
});

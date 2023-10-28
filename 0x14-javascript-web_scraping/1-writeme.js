#!/usr/bin/node

const fs = require('fs');

// Check if both file path and content arguments are provided
if (process.argv.length !== 4) {
  process.exit(1); // Exit with an error code
}

// Get the file path and content from the command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the content to the file with utf-8 encoding
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log('Content has been successfully written to the file.');
  }
});

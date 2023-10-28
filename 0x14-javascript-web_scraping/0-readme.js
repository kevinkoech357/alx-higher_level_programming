#!/usr/bin/node

const fs = require('fs');

// Check if a file path is provided as an argument
if (process.argv.length !== 3) {
  process.exit(1); // Exit with an error code
}

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Read the file with utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});

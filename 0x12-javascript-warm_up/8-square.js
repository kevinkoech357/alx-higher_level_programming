#!/usr/bin/node

// Prints a square
// The first argument is the size of the square
// If the first argument can’t be converted to an integer, print “Missing size”

const args = process.argv[2];
const squareSize = parseInt(args);

if (Number.isNaN(squareSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < squareSize; i++) {
    let row = '';
    for (let j = 0; j < squareSize; j++) {
      row += 'X';
    }
    console.log(row);
  }
}

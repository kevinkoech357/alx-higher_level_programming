#!/usr/bin/node

// Prints addition of 2 integers

// addition function

function add (a, b) {
  return a + b;
}

const firstInt = parseInt(process.argv[2]);
const secondInt = parseInt(process.argv[3]);

if (Number.isNaN(firstInt) || Number.isNaN(secondInt)) {
  console.log('NaN');
} else {
  const result = add(firstInt, secondInt);
  console.log(result);
}

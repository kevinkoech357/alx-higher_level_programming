#!/usr/bin/node

// prints x times “C is fun”

const x = process.argv[2];
const occurrences = parseInt(x);

if (Number.isNaN(occurrences)) {
  console.log('Missing number of occurrences');
} else {
  let i = occurrences;
  while (i > 0) {
    console.log('C is fun');
    i--;
  }
}

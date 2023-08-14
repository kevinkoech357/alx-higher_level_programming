#!/usr/bin/node

// prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer

const myNumber = process.argv[2];
const parsedNumber = parseInt(myNumber);

if (!Number.isNaN(parsedNumber) && Number.isInteger(parsedNumber)) {
  console.log('My number: ' + parsedNumber);
} else {
  console.log('Not a number');
}

#!/usr/bin/node

// prints two arguments passed to it, in the following format:
// argv[2] is argv[3]

const argument1 = process.argv[2];
const argument2 = process.argv[3];

if (argument1 === undefined) {
  console.log(argument1 + ' is ' + argument2);
} else {
  console.log(argument1 + ' is ' + argument2);
}

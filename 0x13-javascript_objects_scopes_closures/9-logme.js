#!/usr/bin/node

// prints the number of arguments already printed and the new argument value

// declared outside so it doesnt retain value
let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
}

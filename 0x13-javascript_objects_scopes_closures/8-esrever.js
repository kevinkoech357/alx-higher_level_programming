#!/usr/bin/node

// returns the reversed version of a list

exports.esrever = function (list) {
  // get length
  const length = list.length;
  // get center of the list
  const center = Math.floor(length / 2);

  // iterate to center of list
  // then swap each element with corresponding element at the back
  for (let i = 0; i < center; i++) {
    const temp = list[i];
    list[i] = list[length - 1 - i];
    list[length - 1 - i] = temp;
  }

  return list;
}

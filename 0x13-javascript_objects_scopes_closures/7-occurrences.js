#!/usr/bin/node

// Returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  // iterating through list comparing elements at index i
  // and the target element
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }

  return count;
};

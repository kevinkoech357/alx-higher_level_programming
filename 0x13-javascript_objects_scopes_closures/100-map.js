#!/usr/bin/node

// Imports an array and computes a new array

const dataModule = require('./100-data');

// extract list array from imported dataModule

const importedList = dataModule.list;

// map function creates a new array by applying a provided function
// to each element of original array

function computeNewArray (list) {
  const newArray = list.map((value, index) => value * index);
  return newArray;
}

const computedList = computeNewArray(importedList);
console.log(importedList);
console.log(computedList);

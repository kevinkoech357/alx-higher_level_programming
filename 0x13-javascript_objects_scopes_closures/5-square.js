#!/usr/bin/node

// importing class Rectangle
const Rectangle = require('./4-rectangle');

// creating class Square
// which inherits from class Rectangle

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;

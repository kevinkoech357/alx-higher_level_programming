#!/usr/bin/node

/*
 * a class Rectangle that defines a rectangle:
 * You must use the class notation for defining your class
 * The constructor must take 2 arguments w and h
 * Initialize the instance attribute width with the value of w
 * Initialize the instance attribute height with the value of h
*/

class Rectangle {
  constructor (w, h) {
    if (w === 0 || h === 0 || w < 0 || h < 0) {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
  // Print instance method

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;

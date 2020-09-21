#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle of 4-rectangle.js
// The constructor of Rectangle must be called (by using super())

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // Here, it calls the parent class's constructor with size
    // provided for the Rectangle's width and height
    super(size, size);
    // Note: In derived classes, super() must be called before you
    // can use 'this'. Leaving this out will cause a reference error.
  }
}

module.exports = Square;

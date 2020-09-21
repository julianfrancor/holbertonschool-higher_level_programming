#!/usr/bin/node

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

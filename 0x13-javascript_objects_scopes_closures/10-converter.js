#!/usr/bin/node
// function that converts a number from base 10 to another base passed as argument
// number.toString(radix)
// Which base to use for representing a numeric value. Must be an integer between 2 and 36.
// 2 - The number will show as a binary value
// 8 - The number will show as an octal value
// 16 - The number will show as an hexadecimal value
// here we are using a Closure

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};

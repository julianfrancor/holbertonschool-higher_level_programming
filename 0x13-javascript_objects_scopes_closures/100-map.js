#!/usr/bin/node
const numbers = require('./100-data').list;

const newArray = numbers.map(function (number, index) {
  return number * index;
});

console.log(numbers);
console.log(newArray);

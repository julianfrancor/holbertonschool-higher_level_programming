#!/usr/bin/node
// script that prints the addition of 2 integers

const myArgs = process.argv.slice(2);
const a = parseInt(myArgs[0], 10);
const b = parseInt(myArgs[1], 10);

function add (a, b) {
  const result = a + b;
  console.log(result);
}
add(a, b);

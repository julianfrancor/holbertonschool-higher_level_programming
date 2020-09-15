#!/usr/bin/node
// script that prints a message depending of the number of arguments passed
// using process.argv

const myArgs = process.argv.slice(2);

if (myArgs) {
  console.log('Argument Found');
} else {
  console.log('No argument');
}

#!/usr/bin/node
// script that prints the first argument passed to it

const myArgs = process.argv.slice(2);

if (myArgs[0] === undefined) {
  console.log('No argument');
} else {
  console.log(myArgs[0]);
}

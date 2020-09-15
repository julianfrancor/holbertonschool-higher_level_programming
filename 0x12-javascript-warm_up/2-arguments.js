#!/usr/bin/node
// script that prints a message depending of the number of arguments passed
// using process.argv

if (process.argv.length < 3) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument Found');
} else {
  console.log('Arguments Found');
}

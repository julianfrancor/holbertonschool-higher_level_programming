#!/usr/bin/node
// script that prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer

const myArgs = process.argv.slice(2);

if (Number(myArgs[0])) {
  console.log('My number: ' + Number(myArgs[0]));
} else {
  console.log('Not a number');
}

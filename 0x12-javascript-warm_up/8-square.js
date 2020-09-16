#!/usr/bin/node
// script that prints a square

const size = process.argv.slice(2);

if (isNaN(parseInt(size[0], 10))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(size[0], 10); i++) {
    console.log('X'.repeat(parseInt(size[0], 10)));
  }
}

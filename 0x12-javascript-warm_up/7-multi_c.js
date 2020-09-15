#!/usr/bin/node
// script that prints x times “C is fun”
// parseInt(string, radix) radix can be (16 (hexadecimal), 8 (octal), 10 (decimal))

const xTimes = process.argv.slice(2);

if (isNaN(parseInt(xTimes[0], 10))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(xTimes[0], 10); i++) {
    console.log('C is fun');
  }
}

#!/usr/bin/node
// script that computes and prints a factorial

const a = parseInt(process.argv.slice(2)[0]);

function factorial (a) {
  if (a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

if (!isNaN(a)) {
  console.log(factorial(a));
} else {
  console.log(1);
}

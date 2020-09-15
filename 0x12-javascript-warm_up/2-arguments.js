#!/usr/bin/node
// script that prints a message depending of the number of arguments passed
// using process.argv

const myArgs = process.argv.length;

if (myArgs == 2) {
    console.log('No argument');
} else if (myArgs == 3){
    console.log('Argument Found');
} else {
    console.log('Arguments Found');
}

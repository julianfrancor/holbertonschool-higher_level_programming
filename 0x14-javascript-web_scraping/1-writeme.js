#!/usr/bin/node
// script that writes a string to a file.
// The first argument is the file path
// The second argument is the string to write
// The content of the file must be written in utf-8
// If an error occurred during while writing, print the error object
const fs = require('fs');
const newFileName = process.argv[2];
const text = process.argv[3];
fs.writeFile(newFileName, text, 'utf-8', function (err) {
  if (err) {
    return console.log(err);
  }
});

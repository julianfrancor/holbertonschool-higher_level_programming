#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.
// The first argument is the URL to request
// The second argument the file path to store the body response
// The file must be UTF-8 encoded
// You must use the module request
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];
request(url, function (err, resp, body) {
  if (resp.statusCode === 200) {
    fs.writeFile(filename, body, 'utf-8', function (err, data) {
      if (err) {
        return console.log(err);
      }
    });
  } else {
    console.log(err);
  }
});

#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.
// The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
// Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API

const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, function (err, resp, body) {
  if (resp.statusCode === 200) {
    for (const result of JSON.parse(body).results) {
      for (const character of result.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
  } else {
    console.log(err);
  }
  console.log(count);
});

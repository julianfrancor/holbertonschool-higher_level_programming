#!/usr/bin/node

const url = 'https://swapi-api.hbtn.io/api/films/';
const request = require('request');
const movieID = process.argv[2];
const requestURL = url + movieID;
request.get(requestURL).on('response', function (resp, err, body) {
  if (resp.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log(err);
  }
});

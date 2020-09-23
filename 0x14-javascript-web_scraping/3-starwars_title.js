#!/usr/bin/node
// You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
// You must use the module request
const url = 'https://swapi-api.hbtn.io/api/films/';
const request = require('request');
const movieID = process.argv[2];
const requestURL = url + movieID;
request(requestURL, function (err, resp, body) {
  if (resp.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log(err);
  }
});

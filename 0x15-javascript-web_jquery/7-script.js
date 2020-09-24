#!/usr/bin/node
// Javascript script that fetches and replaces the name of this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
// The name must be displayed in the HTML tag DIV#character
// https://api.jquery.com/Jquery.get/

$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('#character').text(data.name);
});

#!/usr/bin/node
// Javascript script that fetches and lists all movies title by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
// All movie titles must be list in the HTML tag UL#list_movies
// You must use the jQuery API
// https://api.jquery.com/each/
// $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
//   const movies = data.results;
//   for (let i = 0; i < movies.length; i++) {
//     $('#list_movies').append(`<li> ${movies[i].title} </li>`);
//   }
// });

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (i, movie) {
    $('#list_movies').append(`<li> ${movie.title} </li>`);
  });
});

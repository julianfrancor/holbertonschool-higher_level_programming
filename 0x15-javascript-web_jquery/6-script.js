#!/usr/bin/node
// Javascript script that updates the text of the HTML tag HEADER to “New Header!!!” when the user clicks on DIV#update_header
// You must use the jQuery API
$('#update_header').click(function () {
  $('HEADER').text('New Header!!!');
});

#!/usr/bin/node
// Javascript script that adds the class red to the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header
// You must use the jQuery API
// https://www.w3schools.com/jquery/html_addclass.asp
$('DIV#red_header').click(function(){
  $('HEADER').addClass('red');
});

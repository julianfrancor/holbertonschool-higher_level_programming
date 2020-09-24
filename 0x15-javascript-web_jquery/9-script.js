#!/usr/bin/node
// script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML’s tag DIV#hello.
// You must use the jQuery API
// Your script must work when it is imported from the HEAD tag
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('#hello').text(data.hello);
});

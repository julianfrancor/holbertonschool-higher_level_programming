#!/usr/bin/node
// Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000)
// You can’t use document.querySelector to select the HTML tag
// You must use the jQuery API
$(function()
{
	$("HEADER").css("color", "#FF0000");
});

#!/usr/bin/node
// Javascript script that adds a LI element to a list when the user clicks on the tag DIV#add_item
// The new element must be: <li>Item</li>
// The new element must be added to UL.my_list
// You must use the jQuery API
$('#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});

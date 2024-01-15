// Adds a <li> element to a list
const $ = window.$;
$('#add_item').bind('click', function () {
  $('UL.my_list').append('<li>Item</li>');
});

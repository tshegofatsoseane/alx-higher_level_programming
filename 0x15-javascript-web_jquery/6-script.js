// Updates the text of the <header> element
const $ = window.$;
$('#update_header').bind('click', function () {
  $('header').replaceWith('New Header!!!');
});

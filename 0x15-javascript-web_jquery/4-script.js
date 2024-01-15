// Toggles the class of the <header> element
const $ = window.$;
$('#toggle_header').bind('click', function () {
  $('header').toggleClass('green red');
});

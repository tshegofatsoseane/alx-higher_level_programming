//  Fetches displays the value of hellofrom https://fourtonfish.com/hellosalut/?lang=fr
const $ = window.$;
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, status) {
  console.log(data.hello);
  $('#hello').html(data.hello);
});

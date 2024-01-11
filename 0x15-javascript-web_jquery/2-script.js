<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Change Text Color with jQuery</title>
    <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
  </head>
  <body>
    <div id="red_header">
     change text color
    </div>

    <header>
    header text
    </header>

    <script>
      $('#red_header').click(function() {
        $('header').css('color', '#FF0000');
      });
    </script>
  </body>
</html>

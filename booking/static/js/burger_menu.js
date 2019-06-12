$(document).ready(function() {
    $(".burger-menu").click(function() {
      $(".stick").toggleClass(function () {
        return $(this).is('.open, .close') ? 'open close' : 'open';
      });
    });
  });
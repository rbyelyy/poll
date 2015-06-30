$(function () {
  var loading = $('#loadbar').hide();
  $('label.btn').on('click', function () {
    var user_choice = $(this).find('input:radio').val();
    var already_stored_choices = localStorage.getItem('answer');

    if (already_stored_choices == null) {

      localStorage.setItem('answer',JSON.stringify(user_choice));

    }
    else{

          var all_choices = already_stored_choices + ',' + (JSON.stringify(user_choice));
          localStorage.setItem('answer', all_choices);

    }
    var glyphincon = $(this).find('i');
    if ($(glyphincon).hasClass('glyphicon glyphicon-chevron-right')) {
      $(glyphincon).attr('class', 'glyphicon glyphicon-check');
    } else {
      $(glyphincon).attr('class', 'glyphicon glyphicon-chevron-right');
    }
  });
});

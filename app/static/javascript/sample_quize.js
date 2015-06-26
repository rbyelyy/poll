$(function () {
  $('#next').on('click', function () {
    var question_id = parseInt(Cookies.get('question_id')) + 1
    Cookies.set('question_id', question_id, {
      expires: 1,
      path: ''
    });
    $.ajax({
      url: '',
      context: document.body,
      success: function (s, x) {
        $(this).html(s);
      }
    });
  });
  $('#back').on('click', function () {
    var question_id = parseInt(Cookies.get('question_id')) - 1
    Cookies.set('question_id', question_id, {
      expires: 1,
      path: ''
    });
    $.ajax({
      url: '',
      context: document.body,
      success: function (s, x) {
        $(this).html(s);
      }
    });
  });
});


$(function () {
  $('#finish').on('click', function () {
    $( "div.modal-dialog" ).load( "/sampletour/_quize" );
  });
});
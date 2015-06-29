$(function () {
  var loading = $('#loadbar').hide();
  $('label.btn').on('click', function () {
    var choice = $(this).find('input:radio').val();
    var glyphincon = $(this).find('i');
    $.ajax({
      type: 'GET',
      url: '/sampletour/_answer',
      data: {
        answer: choice
      },
      beforeSend: function () {
        $('#loadbar').show();
        $('#quiz').fadeOut();
        setTimeout(function () {
          $('#quiz').show();
          $('#loadbar').fadeOut();
        }, 10);
      }
    }).fail(function (jqXHR, textStatus, errorThrown) {
      console.log('Ajax request is failed');
    });
    if ($(glyphincon).hasClass('glyphicon glyphicon-chevron-right')) {
      $(glyphincon).attr('class', 'glyphicon glyphicon-check');
    } 
    else {
      $(glyphincon).attr('class', 'glyphicon glyphicon-chevron-right');
    }
  });
});

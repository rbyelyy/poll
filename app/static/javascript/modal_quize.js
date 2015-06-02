$(function(){
    var loading = $('#loadbar').hide();
    $("label.btn").on('click',function () {
    	var choice = $(this).find('input:radio').val();
    	$.ajax({
            type: "GET",
            url: "/sampletour/_answer",
            data: { answer: choice },
            beforeSend: function() {
                $('#loadbar').show();
                $('#quiz').fadeOut();
                setTimeout(function(){
                $('#quiz').show();
                $('#loadbar').fadeOut();
                }, 1000);
    	}
        })
        .done  (function(data, textStatus, jqXHR){ console.log("Ajax request is success") ; })
        .fail  (function(jqXHR, textStatus, errorThrown) { console.log("Ajax request is failed") ; })
        ;
    });
});
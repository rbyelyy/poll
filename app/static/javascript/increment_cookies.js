$(function(){
    $("#next").on('click',function () {
        var question_id = parseInt(Cookies.get('question_id')) + 1
        Cookies.set('question_id', question_id, { expires: 1, path: '' });
    });
        	$.ajax({
            type: "GET",
            url: "/sampletour",
        })
});



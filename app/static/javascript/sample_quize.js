function getCookie(name) {
    var matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

function setCookie(name, value, options) {
    options = options || {};

    var expires = options.expires;

    if (typeof expires == "number" && expires) {
        var d = new Date();
        d.setTime(d.getTime() + expires * 1000);
        expires = options.expires = d;
    }
    if (expires && expires.toUTCString) {
        options.expires = expires.toUTCString();
    }

    value = encodeURIComponent(value);

    var updatedCookie = name + "=" + value;

    for (var propName in options) {
        updatedCookie += "; " + propName;
        var propValue = options[propName];
        if (propValue !== true) {
            updatedCookie += "=" + propValue;
        }
    }

    document.cookie = updatedCookie;
}

function decrement_cookies() {
    localStorage.removeItem('answer');
    var question_id = getCookie('question_id');
    var incremeneted_question_id = +question_id - 1;
    setCookie('question_id', incremeneted_question_id, '');
}

function increment_cookies() {
    localStorage.removeItem('answer');
    var question_id = getCookie('question_id');
    var incremeneted_question_id = +question_id + 1;
    setCookie('question_id', incremeneted_question_id, '');
}


function updateSample() {
    $.ajax({
        url: '',
        context: document.body,
        success: function (s, x) {
            $(this).html(s);
        }
    });
}



if (document.getElementById('back') !== null) {
    document.getElementById('back').onclick = function () {
        decrement_cookies();
        updateSample();
    };
}

if (document.getElementById('next') !== null) {
    document.getElementById('next').onclick = function () {
        var choice  = localStorage.getItem('answer');



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



        increment_cookies();
        updateSample();
    };
}

if (document.getElementById('finish') !== null) {
    document.getElementById('finish').onclick = function () {
        document.location.replace("/sampletour/_quize");
    };
}


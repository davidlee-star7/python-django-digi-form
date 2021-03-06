// todo: Move to another file
// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

var userSignedUp = false;
try {
    var store = window.localStorage;
    if ('true' === store.getItem('signed_up')) {
        userSignedUp = true;
    }
} catch(e) {}

var submitEmailAddress = function(email, form) {
    $.post('/', {
        email: email,
        tagIndex: form.find('input[name="tag_index"]').val(),
        formName: form.data('name')
    }, function () {
        $('[data-remodal-id=submitFinished]').remodal({
            hashTracking: false
        }).open();
        try {
            var store = window.localStorage;
            store.setItem('signed_up', 'true');
        } catch (e) { }
        userSignedUp = true;
        $('input[name="email"]').val('');
        $('.input-enter-prompt').hide();
        // Now hide the input hint
    });
};

$(document).on('opened', '.remodal', function () {
  $(document).on('keyup', function(e) {
    if (e.which === 13) {
        var inst = $('[data-remodal-id=submitFinished]').remodal();
        if (inst) {
            inst.close();
        }
    }
  });
});

$(document).on('closed', '.remodal', function () {
    if (userSignedUp) {
        $(".fixed-header-wrapper").hide();
    }
    $(document).off('keyup');
});


var isSmallDevice = function() {
    return $(window).width() <= 480; // This is synced with includemedia.scss
};



$(document).ready(function(){

    if (!userSignedUp) {

        setTimeout(function(){
            $(".fixed-header-wrapper").slideDown(200);
        }, 1000 * 60); //Display the signup section for unregistered users after 1 minute

    }

    $('form').submit(function(e){
        e.preventDefault();
    });

    if(!isSmallDevice()) {
        $('input[name="email"]').keyup(function(e){
            var $this = $(this);
            var emailAddr = $this.val();
            if (/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(emailAddr)) {
                // So the placeholer will not outside the box
                var textDimension = calculateSize(emailAddr, {font: $this.css('font-family'), fontSize: $this.css('font-size')});
                var leftDistance = Math.min(textDimension.width + 20, $this.innerWidth() - 80);
                $this.siblings('.input-enter-prompt').css({'left': leftDistance }).show();
                if (e.which === 13) {
                    // Enter key
                    submitEmailAddress(emailAddr, $this.parents('form'));
                }
            } else {
                $this.siblings('.input-enter-prompt').hide();
            }
        });
    }


    // click action
    $('.js-submit').click(function (e) {
        e.stopPropagation();
        e.preventDefault();
        var target = $(e.target);
        if (isSmallDevice() && target.parents('.fixed-header-wrapper').length > 0 && !userSignedUp) {
            $('html,body').animate({ scrollTop: $('.row.cta').position().top }, 'slow');
            return false;
        }


        var form = target.parents('form');
        var email = target.parents('form').find('input[name="email"]:visible').val();
        if (!/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(email)) {
            alert('Email format is invalid');
            return false;
        }

        submitEmailAddress(email, form);
    });

});
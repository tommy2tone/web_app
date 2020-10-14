$("#conf_pwd").keyup(function(){
        if ($("#pwd").val() != $("#conf_pwd").val()) {
            $("#msg").html("Password do not match").css("color","red");
        }else{
            $("#msg").html("Password matched").css("color","green");
    }
});

$('.dropdown').hover(function(){
    $('.dropdown-menu').toggle('fast');
});

$('#pwd').keyup(function(){
    var regexUpper = /[A-Z]/;
    var regexLower = /[a-z]/;
    var regexDigit = /[0-9]/;
    var regexSpace = /\s/;
    var regexSpecial = /[!@#$%^&*]/;
    let value = $(this).val();
    if (value.length < 8 || value.length > 32) {
        $('#pwd-length').addClass('x').removeClass('checked');
    }
    if (value.length >= 8 && value.length <= 32){
        $('#pwd-length').removeClass('x').addClass('checked');
    }
    if (regexLower.test(value) == false) {
        $('#pwd-lower').addClass('x').removeClass('checked');
    }
    if (regexLower.test(value) == true) {
        $('#pwd-lower').addClass('checked').removeClass('x');
    }
    if (regexUpper.test(value) == false){
        $('#pwd-upper').addClass('x').removeClass('checked');
    }
    if (regexUpper.test(value) == true){
        $('#pwd-upper').addClass('checked').removeClass('x');
    }
    if (regexDigit.test(value) == false){
        $('#pwd-number').addClass('x').removeClass('checked');
    }
    if (regexDigit.test(value) == true){
        $('#pwd-number').addClass('checked').removeClass('x');
    }
    if (regexSpace.test(value) == true){
        $('#pwd-spaces').addClass('x').removeClass('checked');
    }
    if (regexSpace.test(value) == false){
        $('#pwd-spaces').addClass('checked').removeClass('x');
    }
    if (regexSpecial.test(value) == false){
        $('#pwd-special').addClass('x').removeClass('checked');
    }
    if (regexSpecial.test(value) == true){
        $('#pwd-special').addClass('checked').removeClass('x');
    }
});

$('#BSbtninfo').jfilestyle({
    buttonName : 'btn-info',
    buttonText : 'Select a File'

});
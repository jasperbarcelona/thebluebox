$(document).ready(function(){

var category = ''

$('.overlay').hide();
$('#item-modal').hide();

$('.item-container').css('height',($('.item-container').width()));

$('.form-control').floatlabel({
    labelEndTop:'-5px'
});

$(window).resize(function() {
    $('.item-container').css('height',($('.item-container').width()));
    var st = $(this).scrollTop();
    $('#banner-background').css('top',-st/3);

    if(st >= 100){
    $('.header').css('opacity', (st/$('#banner').height()) + .1);
    }
    else if(st < 100){
        $('.header').css('opacity', (st/$('#banner').height()));
    }
});

$(window).load(function() {
    var st = $(this).scrollTop();
    $('#banner-background').css('top',-st/3);

    if(st >= 100){
    $('.header').css('opacity', (st/$('#banner').height()) + .1);
    }
    else if(st < 100){
        $('.header').css('opacity', (st/$('#banner').height()));
    }
    if ((st+78) >= $('#banner').height()){
        $("#navigation").css("position","fixed");
        $("#navigation").css("top","78px");
        $("#main").css("padding-top","70px");
    }

    if ((st+78) < $('#banner').height()){
        $("#navigation").css("position","relative");
        $("#navigation").css("top","0px");
        $("#main").css("padding-top","0px");
    }

    $('#preloader').fadeOut();
    $('body').css('position', 'relative');
});

$("#item-modal").on('click', function(e) {
    if(e.target != this){
        return;
    }
    else{
        $('body').css('overflow-y','scroll')
        $(this).fadeOut();
    }
});

if (document.documentElement.clientWidth > 752) {

$(window).on('scroll', function(){
    var st = $(this).scrollTop();
    $('#banner-background').css('top',-st/3);
    if(st >= 100){
        $('.header').css('opacity', (st/$('#banner').height()) + .1);
    }
    else if(st < 100){
        $('.header').css('opacity', (st/$('#banner').height()));
    }

    if(st >= 2){
        $(".cart-icon").css("color","#1E2226");
        $(".cart-icon").css("border","2px solid #1E2226");
    }
    else if (st<2){
        
        $(".cart-icon").css("color","#FFFFFF");
        $(".cart-icon").css("border","2px solid #FFFFFF");
    }

    if ((st+78) >= $('#banner').height()){
        $("#navigation").css("position","fixed");
        $("#navigation").css("top","78px");
        $("#main").css("padding-top","70px");
    }

    if ((st+78) < $('#banner').height()){
        $("#navigation").css("position","relative");
        $("#navigation").css("top","0px");
        $("#main").css("padding-top","0px");
    }
});

$('#shop-btn').on('click', function(){
    $(window).scrollTo('#main',{
        duration: 800,
        offset: -73
    });
});

}

$('#checkout_first_name').on('change', function(){
    var value = $(this).val();
    if (!validate_non_numeric(value)){
        $(this).css('border-bottom','2px solid #CB1E20');
        $('#checkout-first-name-error').show();
    }
    else{
        $(this).css('border-bottom','1px solid #999');
        $('#checkout-first-name-error').hide();
    }
});

$('#checkout_last_name').on('change', function(){
    var value = $(this).val();
    if (!validate_non_numeric(value)){
        $(this).css('border-bottom','2px solid #CB1E20');
        $('#checkout-last-name-error').show();
    }
    else{
        $(this).css('border-bottom','1px solid #999');
        $('#checkout-last-name-error').hide();
    }
});

$('#checkout_password').on('change', function(){
    var value = $(this).val();
    if (value.length < 8){
        $(this).css('border-bottom','2px solid #CB1E20');
        $('#checkout-password-error').show();
    }
    else{
        $(this).css('border-bottom','1px solid #999');
        $('#checkout-password-error').hide();
    }
});

$('#checkout_password').on('change', function(){
    var value = $(this).val();
    if (!value == $('#checkout_password').val()){
        $(this).css('border-bottom','2px solid #CB1E20');
        $('#checkout-confirm-password-error').show();
    }
    else{
        $(this).css('border-bottom','1px solid #999');
        $('#checkout-confirm-password-error').hide();
    }
});

})
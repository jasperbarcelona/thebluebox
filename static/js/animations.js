$(document).ready(function(){

var ready = true;
var category = ''
/*$('.item-container').hide();*/
$('#item-modal').hide();
$('.overlay').hide();

/*$('.item-container').css("height","calc("+String($(window).height()/2) + "px - 70px)");*/

/*$(window).load(function() {
    $('.item-container').delay(2000).fadeIn(1500);
});*/

$(".item-container").click(function() {
    $("#item-modal").fadeIn();
});

$(".item-container").hover(function() {
    $(this).find(".overlay").fadeIn(200);
});

$(".item-container").mouseleave(function() {
    $(this).find(".overlay").fadeOut(200);
});

$("#item-modal").on('click', function(e) {
    if(e.target != this){
        return;
    }
    else{
    $(this).fadeOut();
    }
});

$("#shop-btn").click(function() {
    $(".container").animate({scrollTop:$(window).height()},1000);
});

$(".container").on('scroll', function(){
    st = $(this).scrollTop();
    if(st >= 2){
        $(".cart-icon").css("color","#6D6D6D");
        $(".cart-icon").css("border","1px solid #6D6D6D");
    }
    else if (st<2){
        $(".cart-icon").css("color","#FFFFFF");
        $(".cart-icon").css("border","1px solid #FFFFFF");
    }
});

/*$(".container").on('scroll', function(){
    st = $(this).scrollTop();
    if((st >= $(window).height()/2) && (st < $(window).height()-40)){
        $("#navigation").fadeIn();
        $("#navigation").css("background-color","transparent");
        $("#navigation").css("color","#FFFFFF");
    }
    else if(st >= $(window).height()-40){
        $("#navigation").css("background-color","rgba(0,0,0,1)");
        /*$("#navigation").css("color","#000000");
    }
    else{

    }
});


/*var lastScrollTop = 0;
multiplier = 1
$("#container-right").on('scroll', function() {
    var $this = jQuery(this);
    if ($this.data('activated')) return false;  // Pending, return

    $this.data('activated', true);
    setTimeout(function() {
        $this.data('activated', false)
    }, 1000);

    st = $(this).scrollTop();
    if(st > lastScrollTop){
        $("#container-right").animate({scrollTop:$("#container-right").height() * multiplier});
        multiplier++
        lastScrollTop = $(this).scrollTop();
    }
    else{
       $("#container-right").animate({scrollTop:$("#container-right").height() * (multiplier - 2)});
       multiplier--
       lastScrollTop = $(this).scrollTop();
    }
});*/
/*var multiplier = 0

var mousewheelevt = (/Firefox/i.test(navigator.userAgent)) ? "DOMMouseScroll" : "mousewheel" //FF doesn't recognize mousewheel as of FF3.x
$('#container-right').bind(mousewheelevt, function(e){
    e.preventDefault();
    var $this = jQuery(this);
    if ($this.data('activated')) return false;  // Pending, return

    $this.data('activated', true);
    setTimeout(function() {
        $this.data('activated', false)
    }, 1000);

    var evt = window.event || e //equalize event object     
    evt = evt.originalEvent ? evt.originalEvent : evt; //convert to originalEvent if possible               
    var delta = evt.detail ? evt.detail*(-40) : evt.wheelDelta //check for detail first, because it is used by Opera and FF

    if(delta > 0) {
        $("#container-right").animate({scrollTop:$("#container-right").height() * (multiplier - 1)});
        multiplier--
    }
    else{
        $("#container-right").animate({scrollTop:$("#container-right").height() * (multiplier + 1)});
        multiplier++
    }   
});*/


})
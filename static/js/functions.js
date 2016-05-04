var selected_size = '';
var current_tab = '';

function change_tab(tab){
  current_tab = tab;
  var $this = jQuery('.nav-li');
  if ($this.data('activated')) return false;  // Pending, return
  $this.data('activated', true);
  setTimeout(function() {
    $this.data('activated', false)
  }, 500); // Freeze for 500ms

  $('.nav-li').removeClass('active');
  $('#'+tab+'-nav').addClass('active');

  st = $(this).scrollTop();
  if (st < $('#banner').height()-60){
    $(window).scrollTo('.main-items-container',{
      duration: 800,
      offset: -140
    });
  }
  setTimeout(function(){ 
    $('.main-container').scrollTo('#'+tab,{
      duration: 800
    });
    onScrollInit( $('.'+tab) );
  }, 0);
}

function select_size(buttonId){
  selected_size = $('#'+buttonId).attr('value');
  $('.modal-item-size-active').removeClass('modal-item-size-active');
  $('#'+buttonId).addClass('modal-item-size-active');
}

function supply_data(itemId){
  $('#item-preloader').show();
  $.post('/item/info/get',{
        item_id:itemId,
    },
    function(data){
        $("#info-container").html(data);
        selected_size = $('.modal-item-size-active').attr('value')
        $('#item-preloader').hide();
    });
}

function close_modal(){
  $("#item-modal").modal('hide');
  $('body').css('overflow-y','scroll');
}

function open_cart(){
  $("body").scrollTo('#main',1000);
  $.post('/cart/open',
    function(data){
        $("#main").html(data);
    });
}

function quantity_control(id,operation){
    qty = $('#'+id).text();
    $.post('/quantity/control',{
        item_id:id,quantity:qty,operation:operation
    },
    function(data){
        $('#'+id).html(data.quantity);
        $('.'+id).html(data.item_price);
        $('#cart-total').html(data.total);
    });
}


function add_to_cart(itemId){
    $.post('/cart/item/add',{
        item_id:itemId,size:selected_size
    },
    function(data){
        $("#item-modal").modal('hide');
        $('body').css('overflow-y','scroll');
        var cart = $('.cart-icon');
        var imgtodrag = $("#modal-item-image").eq(0);
        if (imgtodrag) {
            var imgclone = imgtodrag.clone()
                .offset({
                top: $('#'+itemId).offset().top,
                left: $('#'+itemId).offset().left
            })
                .css({
                    'position': 'absolute',
                    'height': '150px',
                    'width': '150px',
                    'z-index': '10000'
            })
                .appendTo($('.container'))
                .animate({
                'top': cart.offset().top + 10,
                    'left': cart.offset().left + 10,
                    'width': 75,
                    'height': 75
            }, 1000, 'easeInOutExpo');

            setTimeout(function () {
                cart.effect("shake", {
                    times: 2
                }, 200);
            }, 1500);

            imgclone.animate({
                'width': 0,
                'height': 0
            });
        }
    });
}

function onScrollInit( items, trigger ) {
  items.each( function() {
    var osElement = $(this),
        osAnimationClass = osElement.attr('data-os-animation'),
        osAnimationDelay = osElement.attr('data-os-animation-delay');
 
    osElement.css({
        '-webkit-animation-delay':  osAnimationDelay,
        '-moz-animation-delay':     osAnimationDelay,
        'animation-delay':          osAnimationDelay
    });
 
    var osTrigger = ( trigger ) ? trigger : osElement;
 
    osTrigger.waypoint(function() {
        osElement.addClass('animated').addClass(osAnimationClass);
    },{
        triggerOnce: true,
        offset: '70%'
    });
  });
}

function validate_non_numeric(value){    
    var re = /^[a-zA-z]+( [a-zA-z]+)*$/;
    if(re.test(value))
       return true;
    else
       return false;    
}
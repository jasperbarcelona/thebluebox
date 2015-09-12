var selected_size = '';

function select_size(buttonId){
  selected_size = $('#'+buttonId).attr('value');
  $('.modal-item-size-active').removeClass('modal-item-size-active');
  $('#'+buttonId).addClass('modal-item-size-active');
}

function supply_data(itemId){
  $.post('/item/info/get',{
        item_id:itemId,
    },
    function(data){
        $("#item-modal").html(data);
        selected_size = $('.modal-item-size-active').attr('value')
    });
}

function close_modal(){
  $("#item-modal").fadeOut();
}

function open_cart(){
  $.post('/cart/open',
    function(data){
        $("#main").html(data);
    });
}


function add_to_cart(itemId){
    $.post('/cart/item/add',{
        item_id:itemId,size:selected_size
    },
    function(data){
        $("#item-modal").fadeOut();
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
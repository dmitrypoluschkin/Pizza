var nam = document.querySelector('#name');
var size = document.querySelector('#size');
var price = document.querySelector('#price');
var bill = document.querySelector('#total');
var rm = document.querySelector('#rm');


function shoppingCart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;

    nam.innerHTML = '<h3>Name</h3>';
    size.innerHTML = '<h3>Size</h3>';
    price.innerHTML = '<h3>Price</h3>';
    rm.innerHTML = '<h3><br></h3>';

    for (let i = 0; i < cartSize; i++) {
        rm.innerHTML += '<div class="btn-group"><h4><button class="btn-danger" onclick="removeItem(' + i + ')">x</button><h4></div>';
        nam.innerHTML += '<h4>' + orders[i][0] + '</4>';
        size.innerHTML += '<h4>' + orders[i][1] + '</4>';
        price.innerHTML += '<h4>' + orders[i][2] + '</4>';
    }
    bill.innerHTML = 'Total:' + total + '$';
}

shoppingCart()


function removeItem(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);

    // updating number of items of shopping Cart
    var cart = document.querySelector('#cart');
    cart.innerHTML = orders.length;

    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    shoppingCart();
}


var note = document.querySelector('#message');

$.ajaxSetup({
    headers: {
        'X-Requested-With': 'XMLHttpRequest'
    }
});

function order(){
    var msg = note.value;
    var orders = localStorage.getItem('orders');

    var ur = '/food/order';
    var orderData = {};
    orderData['orders'] = orders;
    orderData['note'] = msg;
    $.ajax({
        url: ur,
        type: "POST",
        data: orderData,
        headers: { 'X-Requested-With': 'XMLHttpRequest' },
        success: function(data){
            if (data.success) {
                window.location.replace('/food/success');
            }
            else {
                console.log('The data was not sent');
            }
        }
    })
}

axios.post('/food/order', { test: 'value' }, { headers: { 'X-Requested-With': 'XMLHttpRequest' } })

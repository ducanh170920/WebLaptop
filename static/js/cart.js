var updateBtns = document.getElementsByClassName('update-cart');

var productId;
var action;
var quantity = 0;
for(var i = 0 ; i < updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
            productId = this.dataset.product;
            action = this.dataset.action;
            console.log("productID:",productId,"action:",action)


    console.log('User:'+user);
    if(user == 'AnonymousUser'){
        console.log('User is not authenticated')

    }else{
        UpdateCart(productId,action,0);
    }
 });

}
var updateBtns = document.getElementsByClassName('update-cart1');
for(var i = 0 ; i < updateBtns.length;i++){
    updateBtns[i].addEventListener('input',function(){
           productId = this.dataset.product;
           action = this.dataset.action;
           quantity=this.value;
           console.log("productID1:",productId,"action:",action,'quantity:',quantity)


    console.log('User:'+user);
    if(user == 'AnonymousUser'){
        console.log('User is not authenticated')

    }else{
        if(action == 'update'){
            UpdateCart(productId,action,quantity);
        }
        else UpdateCart(productId,action,0);
    }
 });

}
function UpdateCart(productId,action,quantity){
    var url ='/update_item/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId,'action':action,'quantity':quantity})

    })
    .then((response) =>{
        return response.json();
    })
    .then((data) =>{
        location.reload();
    });

}

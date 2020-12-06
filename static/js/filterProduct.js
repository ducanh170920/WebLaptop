var filterSearch = document.getElementsByClassName('search_header');
filterSearch[0].addEventListener('click',function(){
           data = document.getElementsByClassName('input');
           SendProduct(data[0].value);


 });
function SendProduct(data1){
    var url ='/'
    fetch(url,{
        method:'GET',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'data':data1})

    })
    .then((response) =>{
        return response.json();
    })
    .then((data) =>{
        location.reload();
    });



}
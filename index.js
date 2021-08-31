// document.getElementById("quote").innerHTML = "this is a new quote

var n_arr = []; 
var q_arr = [];
var count = 0;
var len = 0;

$.getJSON( "data.json", function(data){
    // adding elements to arrays
    $.each(data,function(key,value){
        n_arr.push(key);
        q_arr.push(value);
    });
    // checks
    len = q_arr.length;
    document.getElementById("quote").innerHTML = q_arr[count];
    document.getElementById("name").innerHTML = n_arr[count];
});
    
document.getElementById("b_prev").addEventListener("click", go_prev);
document.getElementById("b_next").addEventListener("click", go_next);

function go_prev(){
    count -= 1;
    if (count < 0) {
        count = q_arr.length - 1;
    }
    document.getElementById("quote").innerHTML = q_arr[count];
    document.getElementById("name").innerHTML = n_arr[count];
    console.log(count)
}

function go_next(){
    count += 1;
    if (count > q_arr.length - 1) {
        count = 0;
    }
    document.getElementById("quote").innerHTML = q_arr[count];
    document.getElementById("name").innerHTML = n_arr[count];
    console.log(count);
}


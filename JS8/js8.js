
let js8_onCheck = false;
document.querySelector("#js8_sutinku").addEventListener("change", function(){
    js8_onCheck = !js8_onCheck;
    if(js8_onCheck){
        console.log("On");
    }else{
        console.log("off");
    }
});

function getEmailVal(e) {
    e.preventDefault();
    let js8_getEmail = document.querySelector("[name=email]").value;
    if (js8_getEmail === "" || js8_onCheck == false) {
        console.log("Tuščias");
        document.querySelector(".js8_Msg").style.display = "block";
    } else if ((isNaN(js8_getEmail)) && (js8_onCheck)) {
        console.log("Viskas OK");
        document.querySelector("h1").textContent = "Viskas OK";
        document.querySelector(".js8_Msg").style.display = "none";
    }
    document.querySelector("[name=email]").value = "";

    let js8_Myitems = document.getElementById("js8_Myitems");
    alert(js8_Myitems.options[js8_Myitems.selectedIndex].value);
}

document.querySelector("#js8_emailForm").addEventListener("submit", getEmailVal);


document.querySelector("[name=items]").onchange = function(){
    let js8_selecteditem = document.querySelector("#js8_Myitems").value;
    console.log("1 " + js8_selecteditem);
}

document.querySelector("[name=items]").onchange = function(){
    let js8_selecteditem = document.querySelector("#js8_Myitems").value;
    console.log("1.1 " + js8_selecteditem);
}

document.querySelector("[name=items]").addEventListener("change", function(){
    let js8_selecteditem = document.querySelector("#js8_Myitems").value;
    console.log("2 " + js8_selecteditem);
});

document.querySelector("[name=items]").addEventListener("change", function(){
    let js8_selecteditem = document.querySelector("#js8_Myitems").value;
    console.log("2.1 " + js8_selecteditem);
});

document.querySelector("[name=items]").addEventListener("change", ()=>{
    let js8_selecteditem = document.querySelector("#js8_Myitems").value;
    console.log("3 " + js8_selecteditem);
});

document.querySelector("[name=items]").addEventListener("change", ()=>{
    let js8_selecteditem = document.querySelector("#js8_Myitems").value;
    console.log("3.1 " + js8_selecteditem);
});


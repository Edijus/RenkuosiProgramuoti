let getNameOutside = "";
let prekes = "TV";

function getName() {
    let manoVardas = "Edijs";
    getNameOutside = manoVardas;

    if (manoVardas != "") {
        document.getElementById("myName").textContent = "Vardas: " + manoVardas;
    }
    else {
        document.getElementById("myName").textContent = "Vardas: ";
    }
}

let testas = getName();

function skaiciuoti(num1, num2, tekstas) {
    return tekstas + (num1 + num2);
    console.log("test");
}

document.getElementById("skaiciai").textContent = skaiciuoti(10, 5, " Rezultatas = ");


function TheColor(myColor) {
    return myColor;
}

document.querySelector("h1").style.color = TheColor("blue");


function TheColor2(myColor) {
    document.getElementById("belekas").style.color = myColor;
    return myColor;
}

document.getElementById("belekas").addEventListener("click", function () { TheColor2("green") });

document.getElementById("myBtn").addEventListener("click", function () { TheColor2("green") });



function getData() {
    let myData = document.getElementById("myData").value;
    let myDataObj = document.getElementById("myData");
    document.getElementById("showData").innerText = myDataObj.value;
    // document.getElementById("myData").value = "";
    myDataObj.value = "";
}


document.getElementById("myGetData").addEventListener("click", getData);

let left_right = 0;
let top_bottom = 0;
document.onkeydown = function (e) {
    let keys = e.keyCode;
    document.getElementById("keys").textContent = keys + String.fromCharCode(e.keyCode);

    if (keys == 39) {
        left_right = left_right + 1;
    }
    else if (keys == 37) {
        left_right = left_right - 1;
    }

    document.getElementById("box").style.left = left_right + "px";


    if (keys == 40) {
        top_bottom = top_bottom + 1;
    }
    else if (keys == 38) {
        top_bottom = top_bottom - 1;
    }

    document.getElementById("box").style.top = top_bottom + "px";
}

let left_right1 = 0;
function speedTest1() {
    let keys = 39;
    if (keys == 39) {
        left_right1 = left_right1 + 1;
    }
    if (keys == 37) {
        left_right1 = left_right1 - 1;
    }
}

left_right1 = 0;
function speedTest2() {
    let keys = 39;
    if (keys == 39) {
        left_right1 = left_right1 + 1;
    }
    else if (keys == 37) {
        left_right1 = left_right1 - 1;
    }
}

let iterations = 1000000000;
console.time('Function #1');
for (var i = 0; i < iterations; i++) {
    speedTest2();
};
console.timeEnd('Function #1');


console.time('Function #2');
for (var i = 0; i < iterations; i++) {
    speedTest1();
};
console.timeEnd('Function #2');
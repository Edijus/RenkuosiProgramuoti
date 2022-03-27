//let js7_countAllElements = 0;
for (i = 0; i < document.getElementsByTagName("h1").length; i++) {
    document.getElementsByTagName("h1")[i].textContent = "Ola " + (i + 1);
}


let js7_allh1lem = document.getElementsByTagName("h1").length;
/*alert(js7_allh1lem);*/


let js7_arr = ["10", "20", "30", "40", "Edijs"];


for (let js7_countAllElm = 0; js7_countAllElm < js7_arr.length; js7_countAllElm++) {
    console.log(js7_arr[js7_countAllElm]);
}

document.addEventListener("keyup", function () {
    let js7_findItem = document.getElementsByName("findItem")[0].value;
    document.getElementById("js7_out").textContent = js7_findItem;
});


let js7_item;
js7_item = () => { return "Mobilus" };
console.log(js7_item());

let js7_calc = (a, b) => { return a * b };
console.log(js7_calc(5, 4));


function nameValidation(event) {
    event.preventDefault();
    let js7_myText = document.querySelector("[name=myName]").value;
    let js7_validText = "";
    if (js7_myText === "") {
        js7_validText = "Tuščias";
    } else if(isNaN(js7_myText)) {
        js7_validText = "Viskas OK";
    } else {
        js7_validText = "Skaičiai negalimi";
    }
    document.querySelector("#js7_showText").textContent = js7_validText;
}

document.getElementById("js7_valid").addEventListener("submit", nameValidation);
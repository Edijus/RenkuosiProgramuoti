function CreateButton() {
    const js11_button = document.createElement("button");
    const js11_btnId = document.createAttribute("id");
    js11_btnId.value = "add_item";
    js11_button.setAttributeNode(js11_btnId);
    const js11_btnText = document.createTextNode("Add item");
    js11_button.append(js11_btnText);
    document.querySelector("body").prepend(js11_button);
}

function Createitems(p_Text) {
    let js11_Li = document.createElement("li");
    let js11_P = document.createElement("h1");
    const js11_myText = document.createTextNode(p_Text);
    js11_P.append(js11_myText);
    js11_Li.append(js11_P);

    document.querySelector("ul").append(js11_Li);
}

CreateButton();
Createitems("Vos užkrovus dokumentą");

document.getElementById("add_item").addEventListener("click", function () { Createitems("Hi") });

document.getElementById("js11_myForm").addEventListener("submit", function () {
    const js11_inputText = document.querySelector("input[type=text]").value;
    Createitems(js11_inputText);
});

for (let i = 0; i < 16; i++) {
    let js11_myDiv = document.createElement("div");
    js11_myDiv.className = "js11_box";
    const js11_myText = document.createTextNode(i + 1);
    js11_myDiv.append(js11_myText);
    document.getElementById("js_11Box").append(js11_myDiv);

    const js11_btnId = document.createAttribute("id");
    js11_btnId.value = i + 1;
    js11_myDiv.setAttributeNode(js11_btnId);

    /*js11_myDiv.addEventListener("click", function () { 
        this.style.backgroundColor = "red";
        alert(this.id); 
    });*/
}


let js11_getAllId = document.querySelectorAll(".js11_box");
for(let i = 0; i < js11_getAllId.length; i++){
    js11_getAllId[i].addEventListener("click", ()=> { 
        alert(js11_getAllId[i].id);
        js11_getAllId[i].style.backgroundColor = "red";
    });
}

let b = "dollars";
document.querySelector("p").textContent = `We love ${b}.`;
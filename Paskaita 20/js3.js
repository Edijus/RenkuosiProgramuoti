const preke = "Televizorius";
let ek_preke;

switch (preke) {
    case "Televizorius":
        console.log("Suradau" + ":" + preke);
        ek_preke = preke;
        break;
    case "Puodelis":
        console.log("Suradau" + ":" + preke);
        ek_preke = preke;
        break;
    case "Obuolys":
        console.log("Suradau" + ":" + preke);
        ek_preke = preke;
        break;
    case "Lėkštė":
        console.log("Suradau" + ":" + preke);
        ek_preke = preke;
        break;
    default:
        console.log("Nieko nerasta");
        ek_preke = "Nieko neradau";
}

document.getElementById("item").innerHTML = ek_preke;

document.getElementsByClassName("item2")[0].innerHTML = "Edijs";
document.getElementsByClassName("item2")[1].innerHTML = "Edijs2";

// ternary
let amzius = 18;
amzius === 18 ?  console.log("Tinkamas") :  console.log("Netinkamas");
const naujas_amzius = amzius === 18 ?  "Tinkamas" :  "Netinkamas";
console.log(naujas_amzius);

for(let n = 0; n < 10; n++){
    console.log(n);
}

let x = 0;
for(x; x < 10; x++){
    console.log(x);
}

console.log("Hi" + x);


let prekes = ["TV", "Obuolys", "Puodelis", "Viryklė", "Lėkštė"];
for(let n = 0; n < prekes.length; n++){
    console.log(n + 1 + "." + prekes[n]);
}

for(let i in prekes){
    console.log(i);
}

for(let i in prekes){
    console.log(prekes[i]);
}

let itemText = "";
for(let i in prekes){
    console.log(prekes[i]);
    itemText = itemText + prekes[i] +  ", ";
}
document.getElementById("item3").innerHTML = itemText;

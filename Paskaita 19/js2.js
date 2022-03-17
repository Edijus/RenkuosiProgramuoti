let skaicius = 11;
let tekstas = "11";
let skaicius2 = 5;
let preke = "Televizorius";
let start = 0;
// Triguba lygybė tikrina ir duomenų tipą
console.log("triguba ", skaicius === tekstas);
// Dviguba lygybė netirina duomenų tipo
console.log(skaicius == tekstas);
// Nelygu
console.log(skaicius2 != skaicius);

console.log(5 > 4);
console.log(5 < 4);
// if x=x AND y=y
console.log(5 === 5 && 10 === 10);
// OR
console.log(5 === 3 || 10 === 10);


if (skaicius == 10) {
    console.log("lygu");
} else {
    console.log("nelygu");
}

if (preke === tekstas) {
    console.log("lygu");
} else {
    console.log("nelygu");
}

if ((preke === "Televizorius" || preke === "Siurblys") && skaicius === 11) {
    console.log("tv arba siurblys: lygu" + preke);
} else {
    console.log("nelygu" + preke);
}

if (start < 4) {
    console.log("Radau");
}
else {
    console.log("Neradau");
}
/*
if(){

}else if(){

}else{

}*/

if (start < 4) {
    if (start < 5) {

    }
}
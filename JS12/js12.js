const js12_myText = "Paskaita 12";
const js12_newText = "Duomenų tipų metodai";
const js12_badText = "     *  Prekės  *   ";
const js12_myNumbers = "1,2,3,4,5";
const js12_realNumber = 12;
const js12_myFloatStr = "2144.74dddd5";
const js12_MyFloatNum2 = 10.45;

console.log(`Teksto ilgis ${js12_myText.length}`);

console.log(`Tekstas didžiosiomis ${js12_myText.toUpperCase()}`);

console.log(js12_myText.lastIndexOf("1"));
console.log(js12_myText.lastIndexOf("2"));
console.log(js12_myText.lastIndexOf("9"));
console.log(js12_myText.search(/12/));
console.log(js12_myText.slice(4,js12_myText.length));
console.log(js12_myText.substring(4,2));
console.log(js12_myText.replace("12", "super duper"));
console.log(js12_myText.includes("12"));
console.log(js12_myText.concat(js12_newText));
console.log(js12_myText.charAt(3));
console.log(js12_badText.trim());
console.log(js12_newText.match(/tipų/));
console.log(document.location.pathname);
console.log((js12_myNumbers.split(",")));
console.log(js12_realNumber.toString());
console.log(typeof(js12_realNumber.toString()));
console.log(js12_myNumbers.valueOf());

if (js12_myNumbers.valueOf() == js12_myNumbers){
  console.log("yes");
}

console.log(js12_myNumbers.concat(" ").repeat(3));
console.log(typeof(js12_myFloatStr));
console.log(typeof(parseFloat(js12_myFloatStr)));
console.log(parseFloat(js12_myFloatStr));
console.log(parseInt(js12_myFloatStr));
console.log(js12_MyFloatNum2.toFixed(2));

const js12_Tekstas = "darbas";
console.log(js12_Tekstas.charAt(0).toUpperCase() + js12_Tekstas.slice(1));

let js12_oldArr = "12345".split("");
console.log(js12_oldArr);
let js12_NewArr = [];
for(let i = 0; i < js12_oldArr.length; i ++){
    js12_NewArr[i] = parseInt(js12_oldArr[i]);
}
console.log(js12_NewArr);
console.log(typeof(js12_NewArr));
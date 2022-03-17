let data = new Date();
let valandos = data.getHours();
let minutes = data.getMinutes();
let sekundes = data.getSeconds();

console.log(valandos + ":" + minutes + ":"+ sekundes);
if (valandos < 18){
    console.log("Dar vis diena");
}else{
    console.log("Jau vakaras");
}

// Bet kokią reikšmę paverčia į boolean
console.log(!!"Labas");
console.log(!!0);
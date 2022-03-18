let n = 0;
let daiktai = ["Siurblys", "TV", "Vidrulys"];
while (n < daiktai.length) {
    console.log(daiktai[n]);
    n = n + 1;
}

let i = 0;
do {
    console.log("Labas " + i);
    i = i + 1;
}
while (i < 5);

for (let myItem in daiktai) {
    console.log(myItem);
}

let myH1 = document.querySelector("#item");
document.querySelector("#myBtn").addEventListener("click", () => {
    const myRand = Math.floor(Math.random() * 10);
    console.log(myRand);
    myH1.textContent = myRand;

    if (myRand === 3) {
        myH1.style.color = "red";
    }
    else {
        myH1.style.color = "black";
    }
});



document.getElementById("testas").innerHTML = "<p>innerHTML nėra saugus</p>";

console.log(document);


document.querySelector("#testas2").textContent = document.lastModified;

document.querySelector("#testas2").style.backgroundColor = "red";


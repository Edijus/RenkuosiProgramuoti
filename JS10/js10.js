console.dir(document.querySelector("h1").style.backgroundColor = "red");
console.dir(document.location.search);

let spalva = document.location.search;
spalva = spalva.replace("?color=", "");
document.querySelector("h1").style.backgroundColor = spalva;
console.log(spalva);

const item =
    [
        {
            "pavadinimas": "TV", "kaina": 1256.00, "kiekis": 20
        },
        {
            "pavadinimas": "Arbatinukas", "kaina": 16.88, "kiekis": 2
        },
        {
            "pavadinimas": "telefonas", "kaina": 165.77, "kiekis": 5
        }
    ]

console.log(item);
console.log(typeof (item[0].kaina));
console.log(item[0].kaina.toString());
console.log(item[0].kaina.toFixed(2));
console.log(item[0].pavadinimas);
console.log(typeof (item[0].kaina.toFixed(2)));

document.querySelector("h1").textContent = item[0].kaina.toFixed(2);

for (let n = 0; n < item.length; n++) {
    console.log(item[n].pavadinimas);
    document.querySelector("h2").innerHTML = document.querySelector("h2").innerHTML + " " + item[n].pavadinimas + "<br>";
}

const js10_item = [
    { "pavadinimas": "Televizorius", "kaina": 1256.00, "kiekis": 20, "akcija": 50 },
    { "pavadinimas": "Arbatinukas", "kaina": 16.00, "kiekis": 2, "akcija": 30 },
    {
        "pavadinimas": "Telefonas", "kaina": 165.00, "kiekis": 5,
        visi: function () { alert("Atrakcija"); }, "akcija": 10,
        "colors": ["balta", "mėlyna", "geltona"]
    },
    {
        "spalvu_masyvas": [
            { "spalva": "balta" },
            { "spalva": "mėlyna" },
            { "spalva": "geltona" }
        ]
    }
];

console.log(js10_item[2].visi());

console.log(js10_item[2].colors);
console.log(js10_item[2].colors[0]);

console.log(js10_item[3][0]);

console.log("spalvų mąsyvas: " + js10_item[3].spalvu_masyvas);
console.log("spalvų mąsyvas 0: " + js10_item[3].spalvu_masyvas[0].spalva);

for (let n = 0; n < js10_item.length; n++) {
    console.log(js10_item[n].pavadinimas);
    document.querySelector("h2").innerHTML = document.querySelector("h2").innerHTML + " " + js10_item[n].pavadinimas + "<br>";
}

const js10_json_str = JSON.stringify(js10_prekes);
console.log("js10_json_str: " + js10_json_str);
let js10_json = JSON.parse(js10_json_str);
function js6_getData(ivykis) {
    ivykis.preventDefault(); /* Sustabdo formą nuo persikrovimo */
    let js6_itemVal = document.querySelector('[name=preke]').value;
    /*alert(js6_itemVal);*/
    document.getElementById("js6_out").textContent = js6_itemVal;
    document.getElementById("js6_myForm").reset();

    document.getElementsByName("result")[0].value = js6_itemVal;
}

document.getElementById("js6_myForm").addEventListener("submit", js6_getData);
/*
let js6_getId = document.getElementById("js6_out").id;
alert(js6_getId);

js6_getId = document.getElementById("js6_out").getAttribute("name");
alert(js6_getId);*/

function getId(js6_getId){
    /*let js6_getId = document.getElementById("2").getAttribute("id");*/
    alert(js6_getId.id);
}
const allElements = document.querySelectorAll("p");

for (let n = 0; n < allElements.length; n++) {
    //allElements[n].textContent = "Labas vakaras" + (n + 1);
    if (n % 2 == 0) {
        allElements[n].style.backgroundColor = "black";
        allElements[n].style.color = "white";
    } else {
        allElements[n].style.backgroundColor = "green";
        allElements[n].style.color = "white";
    }
    allElements[n].id = n;
    allElements[n].setAttribute("value", "eeeeeeee" + n);
    allElements[n].addEventListener("click", function () {
        alert(this.getAttribute("value") + " " + this.textContent + " ID: " + this.id);
    })
}

let count = -1;
const js9_allDivs = document.querySelectorAll("div");
for (let i = 0; i < js9_allDivs.length; i++) {
    js9_allDivs[i].style.backgroundColor = "blue";
    js9_allDivs[i].style.color = "white";
    js9_allDivs[i].style.margin = "1rem auto";
    js9_allDivs[i].style.fontSize = "1.2rem";
    js9_allDivs[i].style.padding = "1rem";
    js9_allDivs[i].style.width = "400px";
    js9_allDivs[i].style.borderRadius = "0.3rem";
}

let previousVal = 0;
function rollout() {

    count++;
    if (count < js9_allDivs.length) {
        js9_allDivs[count].style.backgroundColor = "purple";
    };

    if (count > 0) {
        previousVal = count - 1;
        js9_allDivs[previousVal].style.backgroundColor = "blue";
    }

    if (previousVal === js9_allDivs.length - 1) {
        count = 0;
        js9_allDivs[count].style.backgroundColor = "purple";
    }
}

const myTimer = setInterval(rollout, 500);

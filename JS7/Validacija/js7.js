function isNumber(char) {
    if (typeof char !== 'string') {
        return false;
    }

    if (char.trim() === '') {
        return false;
    }

    return !isNaN(char);
}

function isSpecialChar(char) {
    const specialChars = `\`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~`;

    // Nematomi simboliai
    if ((char.trim() == "") && (String.fromCharCode(32) !== char)) {
        console.log("'" + char + "'");
        return true;
    }else{
        for (let i = 0; i < specialChars.length; i++){
            if(char == specialChars[i]){
              return true;
            }
        }
    }
}

function nameValidation(event) {
    event.preventDefault();
    const viskasOK = "Viskas OK";
    let js7_myText = document.querySelector("[name=myName]").value;
    let js7_validText = "";
    let js7_validatedText = "";

    let js7_yraSkaiciu = false;
    let js7_yraSpec = false;
    for (let i = 0; i < js7_myText.length; i++) {
        let js7_simbolis = js7_myText[i];
        if (isNumber(js7_simbolis)) {
            js7_yraSkaiciu = true;
        } else if (isSpecialChar(js7_simbolis)) {
            js7_yraSpec = true;
        } else {
            js7_validatedText = js7_validatedText + js7_simbolis;
        }
    }

    if (js7_myText === "") {
        js7_validText = "Tuščias";
    } else if (js7_yraSkaiciu) {
        js7_validText = "Skaičiai negalimi";
    } else if (js7_yraSpec) {
        js7_validText = "Spec simboliai negalimi";
    } else {
        js7_validText = viskasOK;
    }

    let js7_display = document.querySelector("#js7_showText");
    js7_display.textContent = js7_validText;
    if (js7_validText == viskasOK) {
        js7_display.style.display = "none";
        alert("Teksto formatas yra tinkamas");
    } else {
        js7_display.style.display = "block";
        alert("Teksto formatas yra netinkamas");
    }
    //console.log(js7_validatedText);
    document.getElementById("js7_validatedText").textContent = "Tekstas, pašalinus nevalidžius simbolius: '" + js7_validatedText + "'";
}

document.getElementById("js7_valid").addEventListener("submit", nameValidation);
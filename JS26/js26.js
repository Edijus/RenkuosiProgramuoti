function getExperiences() {
    fetch("https://zany-skitter-caper.glitch.me/experiences").then(_Response => {
        if (_Response.ok) {
            console.log("Duomenys gauti");
            return _Response.json();
        } else {
            console.log("Kažkas negerai");
        }
    }).then(_APIData => {
        document.getElementById("profile_exp").innerHTML = "";
        console.log(_APIData);
        CreateExperiences(_APIData);
    }).catch(err => console.log("nepavyko", err))
}

function CreateExperiences(AData) {
    AData.forEach((AItem, AIndex) => {
        CreateExperience(AItem);
    });
}

function CreateExperience(AItem) {
    let _SingleExp = document.createElement('div');
    _SingleExp.setAttribute('class', 'single_exp');

    let _ExpYear = document.createElement('div');
    _ExpYear.setAttribute('class', 'exp_year');
    _SingleExp.appendChild(_ExpYear);

    let _Year = document.createElement('h3');
    _Year.innerText = AItem.startYear + " - " + AItem.finishYear;
    _ExpYear.appendChild(_Year);

    let _CompanyName = document.createElement('p');
    _CompanyName.innerText = AItem.companyName;
    _ExpYear.appendChild(_CompanyName);

    let _ExpDescription = document.createElement('div');
    _ExpDescription.setAttribute('class', 'exp_description');

    let _Position = document.createElement('h2');
    _Position.innerText = AItem.position;
    _ExpDescription.appendChild(_Position);

    let _JobDescription = document.createElement('p');
    _JobDescription.innerText = AItem.description;
    _ExpDescription.appendChild(_JobDescription);

    _SingleExp.appendChild(_ExpDescription);

    document.getElementById('profile_exp').appendChild(_SingleExp);
}

getExperiences();
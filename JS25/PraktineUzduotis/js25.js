const BASE_URL = 'https://golden-whispering-show.glitch.me/';

function getApi(AFilter) {
    fetch(BASE_URL).then(_Response => {
        if (_Response.ok) {
            console.log("Duomenys gauti");
            return _Response.json();
        } else {
            console.log("Kažkas negerai");
        }
    }).then(_APIData => {
        document.getElementById("parent").innerHTML = "";
        console.log(_APIData);
        CreateCards(_APIData, AFilter);
    }).catch(err => console.log("nepavyko", err))
}

function CreateCards(AData, AFilter) {
    AData.forEach((AItem, AIndex) => {
        let _Title = AItem.title;
        console.log(_Title);
        if ((_Title == AFilter) || (AFilter == "")) {
            CreateCard(AItem);
        }
    });
}

function CreateCard(AItem) {
    let _CardDiv = document.createElement('div');
    _CardDiv.setAttribute('class', 'card');

    let _Img = document.createElement('img');
    _Img.setAttribute('src', AItem.image);
    _Img.setAttribute('class', 'card-img-top');

    _CardDiv.appendChild(_Img);

    let _CardBody = document.createElement('div');
    _CardBody.setAttribute('class', 'card-body');

    let _CardTitle = document.createElement('h6');
    _CardTitle.innerText = AItem.title;
    _CardTitle.setAttribute('class', 'card-title');
    _CardBody.appendChild(_CardTitle);

    let _CardPrice = document.createElement('h5');
    _CardPrice.innerText = "€" + AItem.price;
    _CardPrice.setAttribute('class', 'card-title');
    _CardBody.appendChild(_CardPrice);

    let _DeleteBtn = document.createElement('button');
    _DeleteBtn.innerText = "Ištrinti";
    _DeleteBtn.setAttribute('class', 'card-text');
    _DeleteBtn.id = AItem.id;
    _DeleteBtn.addEventListener("click", function () {
        DeleteCard(this.id)
    })
    _CardBody.appendChild(_DeleteBtn);

    _CardDiv.appendChild(_CardBody);
    document.getElementById('parent').appendChild(_CardDiv);
}

function DeleteCard(AID) {
    let _URL = BASE_URL + AID;
    fetch(_URL, {
        method: "DELETE"
    }).then(js25_Response => js25_Response.json()
    ).then(js25_Data => window.location.assign("index.html"))
}

getApi("");
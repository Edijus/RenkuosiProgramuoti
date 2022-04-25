const BASE_URL = 'https://radial-reinvented-shoe.glitch.me';

function getApi(AFilter) {
    fetch(BASE_URL).then(_Response => {
        if (_Response.ok) {
            console.log("Duomenys gauti");
            return _Response.json();
        } else {
            console.log("Kažkas negerai");
        }
    }).then(_APIData => {
        document.getElementById("content").innerHTML = "";
        console.log(_APIData);
        CreateCards(_APIData, AFilter);
    }).catch(err => console.log("nepavyko", err))
}

function CreateCards(AData, AFilter) {
    AData.forEach((AItem, AIndex) => {
        let _City = AItem.city;
        if ((_City == AFilter) || (AFilter == "")) {
            CreateCard(AItem);
        }
    });
}

function CreateCard(AItem) {
    let _CardDiv = document.createElement('div');
    _CardDiv.setAttribute('class', 'card');
    _CardDiv.style.width = '10rem';

    let _Img = document.createElement('img');
    _Img.setAttribute('src', AItem.image);
    _Img.setAttribute('class', 'card-img-top');

    _CardDiv.appendChild(_Img);

    let _CardBody = document.createElement('div');
    _CardBody.setAttribute('class', 'card-body');

    let _CardPrice = document.createElement('h5');
    _CardPrice.innerText = "€" + AItem.price;
    _CardPrice.setAttribute('class', 'card-title');
    _CardBody.appendChild(_CardPrice);

    let _CardCity = document.createElement('h6');
    _CardCity.innerText = AItem.city;
    _CardCity.setAttribute('class', 'card-title');
    _CardBody.appendChild(_CardCity);

    let _CardDescription = document.createElement('p');
    _CardDescription.innerText = AItem.description;
    _CardDescription.setAttribute('class', 'card-text');
    _CardBody.appendChild(_CardDescription);

    _CardDiv.appendChild(_CardBody);
    document.getElementById('content').appendChild(_CardDiv);
}

const _Cities = document.getElementsByClassName('list-group-item');
for (let i = 0; i < _Cities.length; i++) {
    _Cities[i].addEventListener('click', FilterCards);
}

function FilterCards() {
    //alert(this.innerText);
    getApi(this.innerText);
}

getApi("");

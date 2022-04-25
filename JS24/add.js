const BASE_URL = 'https://radial-reinvented-shoe.glitch.me';

const form = document.getElementById('form');
form.addEventListener('submit', AddProperty);

function AddProperty(event) {
    event.preventDefault();

    let _Img = document.getElementById("exampleFormControlInput1").value;

    let _Price = document.getElementById("exampleFormControlInput2").value;

    let _Description = document.getElementById("exampleFormControlTextarea1").value;

    let _CityObj = document.getElementById("exampleFormControlSelect1");
    let _City = _CityObj.options[_CityObj.selectedIndex].text;

    fetch(BASE_URL, {
        method: "POST",
        headers: {
            'Accept': 'application/json, text/plain',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ image: _Img, price: _Price, city: _City, description: _Description })
    })
        .then(js23_resp => js23_resp.json())
        .then(js23_data => {
            alert(js23_data.msg);
            window.location.assign("index.html");
        })
}
const BASE_URL = 'https://golden-whispering-show.glitch.me/';

const form = document.getElementById('form');
form.addEventListener('submit', AddProduct);

function AddProduct(event) {
    event.preventDefault();

    let _Img = document.getElementById("exampleFormControlInput1").value;

    let _Price = document.getElementById("exampleFormControlInput3").value;

    let _Title = document.getElementById("exampleFormControlInput2").value;

    fetch(BASE_URL, {
        method: "POST",
        headers: {
            'Accept': 'application/json, text/plain',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ image: _Img, price: _Price, title: _Title})
    })
        .then(js25_resp => js25_resp.json())
        .then(js25_data => {
            alert(js25_data.msg);
            window.location.assign("index.html");
        })
}
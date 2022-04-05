function getData() {
    document.getElementById("js13_getData").textContent = "Start";
}

function checkData() {
    document.getElementById("js13_checkData").textContent = "Middle";
}

function ShowData() {
    document.getElementById("js13_showData").textContent = "End";
}

getData();
checkData();
ShowData();


const posts = [
    { "title": "Kas naujo?", "body": "Bodžiuko tekstas" },
    { "title": "Kas seno?", "body": "Bodžiuko text" },
    { "title": "Kas new?", "body": "Booody tekstas" }
];

function getAllPost() {
    console.log(Date());
    setTimeout(() => {
        posts.forEach((my_element, index) => {
            let js13_CreateP = document.createElement("p");
            let js13_CreateT = document.createTextNode((index + 1) + ". " + `${my_element.title}`);
            js13_CreateP.append(js13_CreateT);
            document.getElementById("js13_output").append(js13_CreateP);
        });
    }, 1000/* ms */);
};


function CreateNewPost(newPost, callbakas) {
    setTimeout(() => {
        posts.push(newPost);
        callbakas();
    }, 2000);
};


function CreateNewPost2(newPost,) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            posts.push(newPost);

            const js13_error = false; // true
            if (!js13_error) {
                resolve()
            }
            else {
                reject("Nepavyko sukurti įrašo");
            }
        }, 2000);
    })
};


/*
CreateNewPost({ "title": "Naujas dyn", "body": "Bodžiuko ami6kai" }, getAllPost);
console.log(Date());*/
//getAllPost();

CreateNewPost2({ "title": "Naujas dyn2", "body": "Per Promise" }).then(getAllPost).catch(err => console.log(err));

const prekes = ["TV", "Monitorius", "Mobilus", "Siurblys"];
const kainos = [295.00, 55.00, 250.00, 145.00];

const js13_JoinArr = prekes.concat(kainos);
console.log(js13_JoinArr);

document.getElementById("js13_ShowArrayToString").textContent = prekes.join(":");

const js13_modArr = prekes.map((item, index) => "<p>" + (index + 1) + ". " + item + "</p>");
const js13_ShowHTML = js13_modArr.join("");
document.getElementById("js13_ModArr").innerHTML = js13_ShowHTML;

const js13_ModArrObj = prekes.map((item) => {
    return { "myItem": item };
});

for (let n = 0; n < js13_ModArrObj.length; n++) {
    document.getElementById("js13_ModArrObj").innerText += js13_ModArrObj[n].myItem + "->";
};
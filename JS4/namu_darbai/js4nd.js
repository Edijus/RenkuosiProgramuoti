const listItems = document.getElementsByTagName("li");
listItems[listItems.length - 1].innerText = "Sūris";


const listItems2 = document.getElementsByTagName("li");
const item1 = listItems2[0].innerText;
const item2 = listItems2[1].innerText;
listItems2[0].innerText = item2;
listItems2[1].innerText = item1;

console.log(Math.floor(Math.random() * (12+1-5)+5));



//console.log(Math.floor(Math.random() * (max+1-min)+min));
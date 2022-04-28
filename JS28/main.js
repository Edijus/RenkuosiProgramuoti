import User, {ShowName, ShowSurname} from "./oop.js";
//import  {User} from "./oop.js";
import {myItems} from "./items.js";

const vartotojas = new User("Vytautas","Landsbergis");
console.log(vartotojas);
ShowName(vartotojas);
ShowSurname(vartotojas);
myItems();
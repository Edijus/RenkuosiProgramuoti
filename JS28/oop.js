export default class User {
    constructor(firstname,lastname){
        this.firstname = firstname;
        this.lastname = lastname;
    }
}

export function ShowName(user){
    console.log(`User firstname: ${user.firstname}`)
}

export function ShowSurname(user){
    console.log(`User lastname = ${user.lastname}`)
}


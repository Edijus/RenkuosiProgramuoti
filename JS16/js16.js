class Animal{
    constructor(AnimalName, color, LivingPlace){
      this.AnimalName = AnimalName;
      this.color = color;
      this.LivingPlace = LivingPlace;
    }
    getAnimalName(){
        console.log(this.AnimalName);
        return this;
    }
    getAnimalColor(){
        console.log(this.color);
        return this;
    }
    getAnimalProperties(){
        console.log('getAnimalProperties:');
        this.getAnimalName();
        this.getAnimalColor();
        return this;
    }
}

let AClass = new Animal("Liūtas", "Albinosas", "Zoo");
AClass.getAnimalName();
AClass.getAnimalColor();

let AClass2 = new Animal("Tigras", "Oranžinis", "Afrika");
AClass2.getAnimalName();

AClass2.getAnimalProperties();

AClass.getAnimalName().getAnimalColor();


class AnimalEats extends Animal{
    constructor(AnimalName, color, LivingPlace, eats){
        super(AnimalName, color, LivingPlace);
        this.eats = eats;
    }
    AnimalEat(){
        console.log("child class gyvena" + this.LivingPlace);
    }
}


let AnimalEater = new AnimalEats("Liūtas", "Albinosas", "Zoo");
AnimalEater.AnimalEat();

let arr = ["Laba", "diena"];
class AllInArr{
      getArr(){
          console.log(arr);
      }
}

let _Arr = new AllInArr();
_Arr.getArr();


class Car {
    constructor(brand) {
      this.carname = brand;
    }
    present() {
      return 'I have a ' + this.carname;
    }
  }
  
  class Model extends Car {
    constructor(brand, mod) {
      super(brand);
      this.model = mod;
    }
    show() {
      return this.present() + ', it is a ' + this.model;
    }
  }

  let myCar = new Model("Ford", "Mustang");
  console.log(myCar.show());


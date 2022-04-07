class car {
    constructor(brand, model, engine) {
        this.brand = brand;
        this.model = model;
        this.engine = engine;
    }

    turnOn() {
        alert("vrooom");
    }
}


const _Car = new car("BMW", "E3", "electric");
_Car.turnOn();



//

class car2 {
    constructor(brand, model, engine, basePrice) {
        this.brand = brand;
        this.model = model;
        this.engine = engine;
        this.basePrice = basePrice;
    }

    turnOn() {
        alert("vrooom");
    }

    getPric() {
        if (this.engine = "electric") {
            return this.basePrice + 10000;
        } else if (this.engine = "diesel") {
            return this.basePrice + 5000;
        }
        else {
            return this.basePrice;
        }
    }
}


const _Car2 = new car2("BMW", "E3", "electric", 1000);
const ripOff = _Car2.getPric();
console.log(ripOff);
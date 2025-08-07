class Vehicle {
    protected brand: string;
    protected year: number;
    constructor(brand: string, year: number) {
        this.brand = brand;
        this.year = year;
    }
    public getDetails(){
        return `Brand: [${this.brand}], Year [${this.year}]`;
    }
}

class Car extends Vehicle {
    private numberOfDoors: number;
    constructor(
        brand: string, 
        year: number, 
        numberOfDoors: number
    ){
        super(brand, year);
        this.numberOfDoors = numberOfDoors;
    }
    public getDetails(): string {
        return `${this.getDetails()}, Doors: [${this.numberOfDoors}]`;
    }
}

const carData = {
  brand: "Honda",
  year: 2021,
  doors: 4
};

const car = new Car(carData.brand, carData.year, carData.doors);
// car.brand <-  wrong
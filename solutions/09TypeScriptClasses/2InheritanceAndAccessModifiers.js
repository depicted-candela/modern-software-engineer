"use strict";
class Vehicle {
    constructor(brand, year) {
        this.brand = brand;
        this.year = year;
    }
    getDetails() {
        return `Brand: [${this.brand}], Year [${this.year}]`;
    }
}
class Car extends Vehicle {
    constructor(brand, year, numberOfDoors) {
        super(brand, year);
        this.numberOfDoors = numberOfDoors;
    }
    getDetails() {
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

var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Vehicle = /** @class */ (function () {
    function Vehicle(brand, year) {
        this.brand = brand;
        this.year = year;
    }
    Vehicle.prototype.getDetails = function () {
        return "Brand: [".concat(this.brand, "], Year [").concat(this.year, "]");
    };
    return Vehicle;
}());
var Car = /** @class */ (function (_super) {
    __extends(Car, _super);
    function Car(brand, year, numberOfDoors) {
        var _this = _super.call(this, brand, year) || this;
        _this.numberOfDoors = numberOfDoors;
        return _this;
    }
    Car.prototype.getDetails = function () {
        return "".concat(this.getDetails(), ", Doors: [").concat(this.numberOfDoors, "]");
    };
    return Car;
}(Vehicle));
var carData = {
    brand: "Honda",
    year: 2021,
    doors: 4
};
var car = new Car(carData.brand, carData.year, carData.doors);
// car.brand <-  wrong

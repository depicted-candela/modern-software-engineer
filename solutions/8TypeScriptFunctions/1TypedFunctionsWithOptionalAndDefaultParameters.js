"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var console_1 = require("console");
var user1 = {
    firstName: 'Nicolás',
    middleName: 'Alberto',
    lastName: 'Córdoba'
};
var user2 = {
    firstName: 'Alan',
    lastName: 'Turing'
};
function createUserGreeting(firstName, salutation, middleName) {
    if (salutation === void 0) { salutation = "Hello"; }
    var message = "[".concat(salutation, "], [").concat(firstName, "]");
    return middleName ? "".concat(message, " [").concat(middleName, "]!") : "".concat(message, "!");
    // return message + middleName ? ` [${middleName}]!` : '!';
}
(0, console_1.log)(createUserGreeting(user1.firstName, 'Hello', user1.middleName));
(0, console_1.log)(createUserGreeting(user2.firstName, 'Hello'));

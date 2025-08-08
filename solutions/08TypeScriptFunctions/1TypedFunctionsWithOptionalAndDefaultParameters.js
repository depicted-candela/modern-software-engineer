"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const console_1 = require("console");
const user1 = {
    firstName: 'Nicolás',
    middleName: 'Alberto',
    lastName: 'Córdoba'
};
const user2 = {
    firstName: 'Alan',
    lastName: 'Turing'
};
function createUserGreeting(firstName, salutation = "Hello", middleName) {
    var message = `[${salutation}], [${firstName}]`;
    return middleName ? `${message} [${middleName}]!` : `${message}!`;
    // return message + middleName ? ` [${middleName}]!` : '!';
}
(0, console_1.log)(createUserGreeting(user1.firstName, 'Hello', user1.middleName));
(0, console_1.log)(createUserGreeting(user2.firstName, 'Hello'));

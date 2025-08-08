"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const console_1 = require("console");
const crypto_1 = require("crypto");
class User {
    constructor(username, email) {
        this.id = (0, crypto_1.randomInt)(0, 10);
        this.username = username;
        this.email = email;
    }
    getProfileSummary() {
        return `ID: [${this.id}], Username: [${this.username}], Email: [${this.email}]`;
    }
}
const userData = {
    username: "johndoe",
    email: "john.doe@example.com"
};
const user = new User(userData.username, userData.email);
(0, console_1.log)(user.getProfileSummary());

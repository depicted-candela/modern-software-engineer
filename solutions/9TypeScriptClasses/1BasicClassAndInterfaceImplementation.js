"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var console_1 = require("console");
var crypto_1 = require("crypto");
var User = /** @class */ (function () {
    function User(username, email) {
        this.id = (0, crypto_1.randomInt)(0, 10);
        this.username = username;
        this.email = email;
    }
    User.prototype.getProfileSummary = function () {
        return "ID: [".concat(this.id, "], Username: [").concat(this.username, "], Email: [").concat(this.email, "]");
    };
    return User;
}());
var userData = {
    username: "johndoe",
    email: "john.doe@example.com"
};
var user = new User(userData.username, userData.email);
(0, console_1.log)(user.getProfileSummary());

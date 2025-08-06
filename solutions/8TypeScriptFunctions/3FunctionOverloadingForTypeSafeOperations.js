"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var console_1 = require("console");
var singleString = "hello world";
var stringArray = ["typescript", "is", "powerful"];
function formatInput(string) {
    if (typeof string == 'string')
        return string.toUpperCase();
    return string.join(", ");
}
(0, console_1.log)(formatInput(singleString));
(0, console_1.log)(formatInput(stringArray));

"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const console_1 = require("console");
const singleString = "hello world";
const stringArray = ["typescript", "is", "powerful"];
function formatInput(string) {
    if (typeof string == 'string')
        return string.toUpperCase();
    return string.join(", ");
}
(0, console_1.log)(formatInput(singleString));
(0, console_1.log)(formatInput(stringArray));

"use strict";
const inputs = [
    "hello world",
    12345,
    true,
    { message: "this is an object" },
    null
];
function logError(message) {
    throw Error(message);
}
function processInput(input) {
    const error_log = `The input <${input}> is unexpectedly neither a number nor a string`;
    switch (typeof input) {
        case "string": return input;
        case "number": return input.toString();
        default: logError(error_log);
    }
}
for (const input of inputs) {
    try {
        const response = processInput(input);
        console.log(response);
    }
    catch (error) {
        console.log(`Error: ${error}`);
        continue;
    }
}

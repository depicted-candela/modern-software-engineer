var inputs = [
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
    var error_log = "The input <".concat(input, "> is unexpectedly neither a number nor a string");
    switch (typeof input) {
        case "string": return input;
        case "number": return input.toString();
        default: logError(error_log);
    }
}
for (var _i = 0, inputs_1 = inputs; _i < inputs_1.length; _i++) {
    var input = inputs_1[_i];
    try {
        var response = processInput(input);
        console.log(response);
    }
    catch (error) {
        console.log("Error: ".concat(error));
        continue;
    }
}

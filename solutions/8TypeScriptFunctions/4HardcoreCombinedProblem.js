var users = [
    {
        id: 1,
        name: "Alice",
        email: "alice@example.com",
        isActive: true
    },
    {
        id: 2,
        name: "Bob",
        email: "bob@example.com",
        isActive: false
    },
    {
        id: 3,
        name: "Charlie",
        email: "charlie@example.com",
        isActive: true
    },
];
// Default callback if none is provided
var defaultCallback = function (result) { return console.log("Pipeline Result:", result); };
// Implementation
function createDataPipeline() {
    var args = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        args[_i] = arguments[_i];
    }
    // Check if the first argument is data (for immediate execution)
    var isImmediate = Array.isArray(args[0]);
    var transformers = isImmediate ? args.slice(1) : args;
    var pipelineLogic = function (initialData, onComplete) {
        if (onComplete === void 0) { onComplete = defaultCallback; }
        var result = transformers.reduce(function (currentData, transformer) { return transformer(currentData); }, initialData);
        onComplete(result);
    };
    if (isImmediate) {
        pipelineLogic(args[0]);
        return;
    }
    else {
        return pipelineLogic;
    }
}
var filterActive = function (data) { return data.filter(function (u) { return u.isActive; }); };
var getEmails = function (data) { return data.map(function (u) { return u.email; }); };
var countItems = function (data) { return console.log("There exists ".concat(data.length, " items")); };
// --- Usage 1: Immediate Execution ---
console.log("--- Immediate Execution ---");
createDataPipeline(users, filterActive, getEmails, countItems);
createDataPipeline(users, filterActive, getEmails, countItems); // Uses default console.log callback
// --- Usage 2: Deferred Execution ---
console.log("\n--- Deferred Execution ---");
var reusablePipeline = createDataPipeline(filterActive);
reusablePipeline(users);
var nameToUppercase = function (data) {
    return data.map(function (u) { return ({ name: u.name.toUpperCase() }); });
};
var reusablePipeline1 = createDataPipeline(nameToUppercase);
reusablePipeline1(users, function (finalData) {
    console.log("Transformed User Names:", finalData);
});
var reusablePipeline2 = createDataPipeline(filterActive);
reusablePipeline2(users, function (finalData) {
    console.log("Transformed User Names:", finalData);
});
var reusablePipeline3 = createDataPipeline(getEmails);
reusablePipeline3(users, function (finalData) {
    console.log("Transformed User Names:", finalData);
});

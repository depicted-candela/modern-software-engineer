"use strict";
const users = [
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
const defaultCallback = (result) => console.log("Pipeline Result:", result);
// Implementation
function createDataPipeline(...args) {
    // Check if the first argument is data (for immediate execution)
    const isImmediate = Array.isArray(args[0]);
    const transformers = isImmediate ? args.slice(1) : args;
    const pipelineLogic = (initialData, onComplete = defaultCallback) => {
        const result = transformers.reduce((currentData, transformer) => transformer(currentData), initialData);
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
const filterActive = (data) => data.filter((u) => u.isActive);
const getEmails = (data) => data.map(u => u.email);
const countItems = (data) => console.log(`There exists ${data.length} items`);
// --- Usage 1: Immediate Execution ---
console.log("--- Immediate Execution ---");
createDataPipeline(users, filterActive, getEmails, countItems);
createDataPipeline(users, filterActive, getEmails, countItems); // Uses default console.log callback
// --- Usage 2: Deferred Execution ---
console.log("\n--- Deferred Execution ---");
const reusablePipeline = createDataPipeline(filterActive);
reusablePipeline(users);
const nameToUppercase = (data) => data.map(u => ({ name: u.name.toUpperCase() }));
const reusablePipeline1 = createDataPipeline(nameToUppercase);
reusablePipeline1(users, (finalData) => {
    console.log("Transformed User Names:", finalData);
});
const reusablePipeline2 = createDataPipeline(filterActive);
reusablePipeline2(users, (finalData) => {
    console.log("Transformed User Names:", finalData);
});
const reusablePipeline3 = createDataPipeline(getEmails);
reusablePipeline3(users, (finalData) => {
    console.log("Transformed User Names:", finalData);
});

"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const console_1 = require("console");
const numericData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const filterEvenNumber = (n) => n % 2 == 0;
const filterGreaterThan5Number = (n) => n > 5;
function filterData(data, predicate) {
    const filtered_records = [];
    data.forEach((record) => predicate(record));
    for (const record of data)
        if (predicate(record))
            filtered_records.push(record);
    return filtered_records;
}
const evenNumbers = filterData(numericData, filterEvenNumber);
const greaterThan5Numbers = filterData(numericData, filterGreaterThan5Number);
(0, console_1.log)(evenNumbers);
(0, console_1.log)(greaterThan5Numbers);

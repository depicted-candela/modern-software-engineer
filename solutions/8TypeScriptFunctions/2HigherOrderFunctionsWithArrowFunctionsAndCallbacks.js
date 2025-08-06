"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var console_1 = require("console");
var numericData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var filterEvenNumber = function (n) { return n % 2 == 0; };
var filterGreaterThan5Number = function (n) { return n > 5; };
function filterData(data, predicate) {
    var filtered_records = [];
    data.forEach(function (record) { return predicate(record); });
    for (var _i = 0, data_1 = data; _i < data_1.length; _i++) {
        var record = data_1[_i];
        if (predicate(record))
            filtered_records.push(record);
    }
    return filtered_records;
}
var evenNumbers = filterData(numericData, filterEvenNumber);
var greaterThan5Numbers = filterData(numericData, filterGreaterThan5Number);
(0, console_1.log)(evenNumbers);
(0, console_1.log)(greaterThan5Numbers);

"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// src/index.ts
var stack_1 = require("./lib/stack");
// Number Stack
var numberStack = new stack_1.default();
numberStack.push(10);
numberStack.push(20);
console.log('Popped from numberStack:', numberStack.pop()); // 20
console.log('Peek numberStack:', numberStack.peek()); // 10
console.log('numberStack size:', numberStack.size()); // 1
// String Stack
var stringStack = new stack_1.default();
stringStack.push("hello");
stringStack.push("world");
console.log('Popped from stringStack:', stringStack.pop()); // "world"
console.log('Is stringStack empty?', stringStack.isEmpty()); // false

// src/index.ts
import Stack from './lib/stack';

// Number Stack
const numberStack = new Stack<number>();
numberStack.push(10);
numberStack.push(20);
console.log('Popped from numberStack:', numberStack.pop()); // 20
console.log('Peek numberStack:', numberStack.peek());       // 10
console.log('numberStack size:', numberStack.size());       // 1

// String Stack
const stringStack = new Stack<string>();
stringStack.push("hello");
stringStack.push("world");
console.log('Popped from stringStack:', stringStack.pop()); // "world"
console.log('Is stringStack empty?', stringStack.isEmpty()); // false
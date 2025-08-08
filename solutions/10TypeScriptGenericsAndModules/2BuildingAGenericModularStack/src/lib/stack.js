"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Stack = /** @class */ (function () {
    function Stack() {
        this.items = [];
    }
    Stack.prototype.push = function (item) {
        this.items.push(item);
    };
    Stack.prototype.pop = function () {
        return this.items.pop();
    };
    Stack.prototype.peek = function () {
        return this.items[0];
    };
    Stack.prototype.isEmpty = function () {
        return this.items.length == 0;
    };
    Stack.prototype.size = function () {
        return this.items.length;
    };
    return Stack;
}());
exports.default = Stack;

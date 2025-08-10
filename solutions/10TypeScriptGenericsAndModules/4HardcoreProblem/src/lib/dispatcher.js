"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var EventDispatcher = /** @class */ (function () {
    function EventDispatcher() {
        this.listeners = {};
    }
    EventDispatcher.prototype.on = function (eventName, callback) {
        (this.listeners[eventName] = this.listeners[eventName] || []).push(callback);
    };
    EventDispatcher.prototype.dispatch = function (eventName, payload) {
        var _a;
        (_a = this.listeners[eventName]) === null || _a === void 0 ? void 0 : _a.forEach(function (cb) { return cb(payload); });
    };
    return EventDispatcher;
}());
exports.default = EventDispatcher;

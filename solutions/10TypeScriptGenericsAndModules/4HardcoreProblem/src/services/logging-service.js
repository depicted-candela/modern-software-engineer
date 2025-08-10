"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.setupLogging = setupLogging;
//   'user:created': { userId: number; name: string; timestamp: Date };
//   'user:deleted': { userId: number; timestamp: Date };
function setupLogging(dispatcher) {
    dispatcher.on('user:created', function (payload) { return console.log("With id ".concat(payload.userId, ", name ").concat(payload.name, ", at ").concat(payload.timestamp, " an user was created")); });
    dispatcher.on('user:deleted', function (payload) { return console.log("The user ".concat(payload.userId, " was deleted at ").concat(payload.timestamp)); });
}

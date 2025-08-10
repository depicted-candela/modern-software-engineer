"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.createUser = createUser;
function createUser(dispatcher, payload) {
    dispatcher.dispatch('user:created', { userId: payload.userId, name: payload.name, timestamp: new Date() });
}

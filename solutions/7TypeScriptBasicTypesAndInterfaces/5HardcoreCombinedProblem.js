var rawEvents = [
    { eventType: "USER_SIGN_IN", userId: "user-123", timestamp: 1672531200 },
    "this is not an event",
    { eventType: "MESSAGE_BROADCAST", senderId: "user-456", message: "Hello everyone!" },
    { eventType: "USER_SIGN_OUT", userId: "user-123", timestamp: 1672534800 },
    { eventType: "MESSAGE_BROADCAST", senderId: "user-789", recipientId: "user-456", message: "Hi there!" },
    null,
    { eventType: "UNKNOWN_EVENT", data: "..." }
];
function isSystemEvent(obj) {
    if (obj == null || typeof obj !== 'object')
        return false;
    if (!('eventType' in obj) || !('timestamp' in obj) || typeof obj.eventType !== 'string' || typeof obj.timestamp !== 'number') {
        return false;
    }
    var event = obj;
    switch (event.eventType) {
        case "USER_SIGN_IN":
        case "USER_SIGN_OUT": return 'userId' in event && typeof event.userId === 'string';
        case "MESSAGE_BROADCAST":
            return 'senderId' in event && typeof event.senderId === 'string' && 'message' in event && typeof event.message === 'string';
        default: return false;
    }
}
function processEvent(event) {
    switch (event.eventType) {
        case "USER_SIGN_IN":
        case "USER_SIGN_OUT":
            console.log("uid: ".concat(event.userId, ", tstmp: ").concat(event.timestamp));
            break;
        case "MESSAGE_BROADCAST":
            console.log("uid: ".concat(event.senderId, ", tstmp: ").concat(event.recipientId));
            break;
        default: unreachable(event);
    }
}
function unreachable(x) {
    throw Error("Unexpected object ".concat(x));
}
for (var _i = 0, rawEvents_1 = rawEvents; _i < rawEvents_1.length; _i++) {
    var event_1 = rawEvents_1[_i];
    if (isSystemEvent(event_1))
        processEvent(event_1);
}

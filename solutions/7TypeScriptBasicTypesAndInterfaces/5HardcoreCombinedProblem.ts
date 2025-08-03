interface EventMetadata { timestamp: number; }
interface UserSignInEvent { eventType: "USER_SIGN_IN"; userId: string; }
interface UserSignOutEvent { eventType: "USER_SIGN_OUT"; userId: string; }
interface MessageBroadcastEvent {
    eventType: "MESSAGE_BROADCAST";
    senderId: string;
    message: string;
    recipientId?: string;
}

type SystemEvent = ( 
        UserSignInEvent | UserSignOutEvent | MessageBroadcastEvent
    ) & EventMetadata;

const rawEvents: unknown[] = [
    { eventType: "USER_SIGN_IN", userId: "user-123", timestamp: 1672531200 },
    "this is not an event",
    { eventType: "MESSAGE_BROADCAST", senderId: "user-456", message: "Hello everyone!" },
    { eventType: "USER_SIGN_OUT", userId: "user-123", timestamp: 1672534800 },
    { eventType: "MESSAGE_BROADCAST", senderId: "user-789", recipientId: "user-456", message: "Hi there!" },
    null,
    { eventType: "UNKNOWN_EVENT", data: "..." }
];

function isSystemEvent(obj: unknown): obj is SystemEvent {
    if (obj == null || typeof obj !== 'object') return false;
    if (!('eventType' in obj) || !('timestamp' in obj) || typeof obj.eventType !== 'string' || typeof obj.timestamp !== 'number') {
        return false;
    }
    const event = obj as { eventType: string; timestamp: number; [key: string]: unknown };
    switch (event.eventType) {
        case "USER_SIGN_IN":
        case "USER_SIGN_OUT": return 'userId' in event && typeof event.userId === 'string';
        case "MESSAGE_BROADCAST": 
            return 'senderId' in event && typeof event.senderId === 'string' && 'message' in event && typeof event.message === 'string';
        default: return false;
    }
}

function processEvent(event: SystemEvent): void {
    switch (event.eventType) {
        case "USER_SIGN_IN":
        case "USER_SIGN_OUT": console.log(`uid: ${event.userId}, tstmp: ${event.timestamp}`); break;
        case "MESSAGE_BROADCAST": console.log(`uid: ${event.senderId}, tstmp: ${event.recipientId}`); break;
        default: unreachable(event);
    }
}

function unreachable(x: never): never {
    throw Error(`Unexpected object ${x}`);
} 

for (const event of rawEvents) {
    if (isSystemEvent(event)) processEvent(event);
}
import { log } from 'console';
import EventDispatcher from '../lib/dispatcher';
import EventMap from '../lib/event-types';

//   'user:created': { userId: number; name: string; timestamp: Date };
//   'user:deleted': { userId: number; timestamp: Date };

export function setupLogging(
    dispatcher: EventDispatcher<EventMap>
) {
    dispatcher.on('user:created', 
        (
            payload
        ) => log(`With id ${payload.userId}, name ${payload.name}, at ${payload.timestamp} an user was created`)
    );
    dispatcher.on('user:deleted', 
        (payload) => log(`The user ${payload.userId} was deleted at ${payload.timestamp}`)
    );
}
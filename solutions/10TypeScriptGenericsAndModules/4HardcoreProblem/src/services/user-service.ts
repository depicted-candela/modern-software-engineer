import EventDispatcher from '../lib/dispatcher';
import EventMap from '../lib/event-types';

export function createUser(
    dispatcher: EventDispatcher<EventMap>,
    payload: EventMap['user:created']
) {
    dispatcher.dispatch(
        'user:created', 
        {
            userId: payload.userId, 
            name: payload.name, 
            timestamp: new Date()
        }
    );
}
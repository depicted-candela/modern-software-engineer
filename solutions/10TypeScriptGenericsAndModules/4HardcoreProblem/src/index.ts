import EventDispatcher from "./lib/dispatcher";
import EventMap from "./lib/event-types";
import { createUser } from "./services/user-service";
import { setupLogging } from "./services/logging-service";

const dispatcher = new EventDispatcher<EventMap>;

setupLogging(dispatcher)
createUser(dispatcher, {userId: 1, name: 'Nicolas', timestamp: new Date});
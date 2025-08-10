"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var dispatcher_1 = require("./lib/dispatcher");
var user_service_1 = require("./services/user-service");
var logging_service_1 = require("./services/logging-service");
var dispatcher = new dispatcher_1.default;
(0, logging_service_1.setupLogging)(dispatcher);
(0, user_service_1.createUser)(dispatcher, { userId: 1, name: 'Nicolas', timestamp: new Date });

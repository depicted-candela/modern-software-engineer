"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const console_1 = require("console");
class AppConfig {
    constructor() {
        AppConfig.instanceCounter++;
        this.configId = AppConfig.instanceCounter;
    }
    static getInstanceCount() {
        return this.instanceCounter;
    }
}
AppConfig.appName = "MyApp";
AppConfig.instanceCounter = 0;
const appconf1 = new AppConfig();
const appconf2 = new AppConfig();
(0, console_1.log)(AppConfig.appName);
(0, console_1.log)("DIrect Counters");
(0, console_1.log)(`Instance 1: ${appconf1.configId}, Instance 2: ${appconf2.configId}`);
(0, console_1.log)("Methodic counters");
(0, console_1.log)(`Instance 1: ${AppConfig.getInstanceCount()}, Instance 2: ${AppConfig.getInstanceCount()}`);

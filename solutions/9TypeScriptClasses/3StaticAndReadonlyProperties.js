"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var console_1 = require("console");
var AppConfig = /** @class */ (function () {
    function AppConfig() {
        AppConfig.instanceCounter++;
        this.configId = AppConfig.instanceCounter;
    }
    AppConfig.getInstanceCount = function () {
        return this.instanceCounter;
    };
    AppConfig.appName = "MyApp";
    AppConfig.instanceCounter = 0;
    return AppConfig;
}());
var appconf1 = new AppConfig();
var appconf2 = new AppConfig();
(0, console_1.log)(AppConfig.appName);
(0, console_1.log)("DIrect Counters");
(0, console_1.log)("Instance 1: ".concat(appconf1.configId, ", Instance 2: ").concat(appconf2.configId));
(0, console_1.log)("Methodic counters");
(0, console_1.log)("Instance 1: ".concat(AppConfig.getInstanceCount(), ", Instance 2: ").concat(AppConfig.getInstanceCount()));

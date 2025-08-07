import { log } from "console";

class AppConfig {
    public static readonly appName = "MyApp";
    private static instanceCounter = 0;
    public readonly configId: number;
    constructor() {
        AppConfig.instanceCounter++;
        this.configId = AppConfig.instanceCounter;
    }
    public static getInstanceCount(): number {
        return this.instanceCounter;
    }
}

const appconf1: AppConfig = new AppConfig();
const appconf2: AppConfig = new AppConfig();

log(AppConfig.appName);
log("DIrect Counters");
log(`Instance 1: ${appconf1.configId}, Instance 2: ${appconf2.configId}`);
log("Methodic counters");
log(`Instance 1: ${AppConfig.getInstanceCount()}, Instance 2: ${AppConfig.getInstanceCount()}`);
import { log } from "console";
import { randomInt } from "crypto";

interface IUser {
    readonly id: number;
    username: string;
    email: string;
    getProfileSummary: () => string;
}

class User implements IUser {
    readonly id: number;
    username: string;
    email: string;
    constructor(username: string, email: string) {
        this.id = randomInt(0, 10);
        this.username = username;
        this.email = email;
    }
    public getProfileSummary(): string {
        return `ID: [${this.id}], Username: [${this.username}], Email: [${this.email}]`;
    }
}

const userData = {
  username: "johndoe",
  email: "john.doe@example.com"
};

const user: User = new User(userData.username, userData.email);
log(user.getProfileSummary());
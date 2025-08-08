interface IUser {
    id: number;
    name: string;
    email: string;
}

const user: IUser = {
    id: 1,
    name: "Alice",
    email: "alice@example.com"
};

function getProperty<T, K extends keyof T>(obj: T, key: K) {
    return obj[key];
}

const user_name = getProperty(user, "name");
const user_id = getProperty(user, "id");
console.log(`User Name: ${user_name}`);
console.log(`User ID: ${user_id}`);
var user = {
    id: 1,
    name: "Alice",
    email: "alice@example.com"
};
function getProperty(obj, key) {
    return obj[key];
}
var user_name = getProperty(user, "name");
var user_id = getProperty(user, "id");
console.log("User Name: ".concat(user_name));
console.log("User ID: ".concat(user_id));

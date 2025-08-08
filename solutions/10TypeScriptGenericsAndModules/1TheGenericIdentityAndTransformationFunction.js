// --- Test cases for your implementation ---
function identity(value) {
    return value;
}
function transformTuple(tupl1, tupl2) {
    return [tupl2, tupl1];
}
// Identity function
var numIdentity = identity(123);
var strIdentity = identity("hello"); // Type inference
console.log("Identity Number: ".concat(numIdentity, ", Type: ").concat(typeof numIdentity));
console.log("Identity String: ".concat(strIdentity, ", Type: ").concat(typeof strIdentity));
// TransformTuple function
var transformed = transformTuple("world", 42);
console.log("Transformed Tuple: [".concat(transformed[0], ", ").concat(transformed[1], "]"));
console.log("Type of first element: ".concat(typeof transformed[0]));
console.log("Type of second element: ".concat(typeof transformed[1]));

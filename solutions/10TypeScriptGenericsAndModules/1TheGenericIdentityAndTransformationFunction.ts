// --- Test cases for your implementation ---

function identity<T>(value: T): T {
    return value;
}

function transformTuple<T, U>(tupl1: T, tupl2: U): [U, T] {
    return [tupl2, tupl1];
}

// Identity function
const numIdentity = identity<number>(123);
const strIdentity = identity("hello"); // Type inference

console.log(`Identity Number: ${numIdentity}, Type: ${typeof numIdentity}`);
console.log(`Identity String: ${strIdentity}, Type: ${typeof strIdentity}`);

// TransformTuple function
const transformed = transformTuple<string, number>("world", 42);

console.log(`Transformed Tuple: [${transformed[0]}, ${transformed[1]}]`);
console.log(`Type of first element: ${typeof transformed[0]}`);
console.log(`Type of second element: ${typeof transformed[1]}`);
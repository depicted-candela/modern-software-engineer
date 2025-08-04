### Exercise 1: Typed Functions with Optional and Default Parameters

**Objective**: Master the creation of strongly-typed functions, understanding how to handle optional data gracefully with optional parameters and provide fallback values using default parameters. This exercise builds directly on the type and interface definitions from Chunk 7.

**Entities**:
- **Concepts**: Function declaration, typed parameters (`userName: string`), return types (`: string`), optional parameters (`middleName?: string`), default values (`salutation: string = 'Hello'`).
- **Patterns**: String interpolation for creating formatted output.
- **Relationships**: Utilizes the `string` and `undefined` primitive types (Chunk 7) to define the function's contract. The optional parameter `middleName` has the type `string | undefined`.
- **Software Engineering Principle**: **Robustness**. The function is designed to work correctly even when optional data (middle name) is missing, preventing runtime errors.

**Problem**:
Create a function `createUserGreeting` that accepts a user's first name, an optional middle name, and a salutation that defaults to "Hello". The function should return a formatted greeting string.

**Artificial Data**:
```typescript
// Represents user data, possibly from an API (relates to Chunk 7 Interfaces)
interface UserProfile {
  firstName: string;
  middleName?: string;
  lastName: string;
}

const user1: UserProfile = { firstName: 'Nicolás', middleName: 'Alberto', lastName: 'Córdoba' };
const user2: UserProfile = { firstName: 'Alan', lastName: 'Turing' };
```

**Task**:
1.  Define the `createUserGreeting` function with the following signature:
    - `firstName`: a required `string`.
    - `salutation`: a `string` with a default value of `'Hello'`.
    - `middleName`: an optional `string`.
2.  The function should return a greeting in the format: `"[Salutation], [FirstName] [MiddleName]!"` if the middle name exists, and `"[Salutation], [FirstName]!"` if it does not.
3.  Call the function for `user1` and `user2` to demonstrate its behavior.

**Source Reference**:
-   **Theory**: TypeScript Handbook - [Functions](https://www.typescriptlang.org/docs/handbook/2/functions.html#optional-parameters) and [Functions](https://www.typescriptlang.org/docs/handbook/2/functions.html#default-parameters). These sections detail the syntax and behavior of `?` for optional parameters and `=` for default values, which are central to solving this problem.
-   **Implementation**: `typescript-handbook-v4.1.pdf`, Page 47, "Optional and Default Parameters", provides the core syntax and rules, such as the fact that optional parameters must follow required ones.

**Solution**:
```typescript
function createUserGreeting(firstName: string, salutation: string = 'Hello', middleName?: string): string {
  if (middleName) {
    return `${salutation}, ${firstName} ${middleName}!`;
  } else {
    return `${salutation}, ${firstName}!`;
  }
}

// Data
const user1 = { firstName: 'Nicolás', middleName: 'Alberto', lastName: 'Córdoba' };
const user2 = { firstName: 'Alan', lastName: 'Turing' };

// Usage
const greeting1 = createUserGreeting(user1.firstName, 'Welcome', user1.middleName);
console.log(greeting1); // Expected: "Welcome, Nicolás Alberto!"

const greeting2 = createUserGreeting(user2.firstName);
console.log(greeting2); // Expected: "Hello, Alan!"
```

---

### Exercise 2: Higher-Order Functions with Arrow Functions and Callbacks

**Objective**: Understand the power of higher-order functions by creating one that accepts a callback. Use arrow functions for a concise and lexically-scoped implementation.

**Entities**:
- **Concepts**: Function types as parameters (callbacks), anonymous functions.
- **Patterns**: Higher-order functions, arrow functions (`=>`). Arrow functions are particularly useful for callbacks as they maintain the lexical `this` context, which becomes critical in class-based components (Chunk 9).
- **Relationships**: Relies heavily on defining function types (e.g., `(item: number) => boolean`), a concept from Chunk 7's Type Aliases.
- **Software Engineering Principle**: **Modularity & Reusability**. Logic is decoupled. The `filterData` function provides the "how" (iteration), while the callback provides the "what" (the filtering condition), making the function reusable for any filtering criterion.

**Problem**:
Create a higher-order function named `filterData` that takes an array of numbers and a callback function. The callback, a "predicate," should accept a number and return `true` if the number should be included in the output. `filterData` should return a new array containing only the numbers for which the predicate returned `true`.

**Artificial Data**:```typescript
const numericData: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
```

**Task**:
1.  Define a type alias `NumberPredicate` for the callback function: `(n: number) => boolean`.
2.  Implement `filterData` with the signature `(data: number[], predicate: NumberPredicate): number[]`.
3.  Use `filterData` with an arrow function to filter for even numbers.
4.  Use `filterData` with another arrow function to filter for numbers greater than 5.

**Source Reference**:
-   **Theory**: TypeScript Handbook - [Function Types](https://www.typescriptlang.org/docs/handbook/2/functions.html#function-type-expressions). This section explains how to define types for functions, which is necessary for typing the `predicate` parameter.
-   **Implementation**: `typescript-handbook-v4.1.pdf`, Page 45, "Typing the function", demonstrates defining a function's type, which we use here for the callback. Basarat’s TypeScript Deep Dive - [Functions](https://basarat.gitbook.io/typescript/type-system/functions) provides further examples of callbacks and arrow function syntax.

**Solution**:
```typescript
type NumberPredicate = (n: number) => boolean;

function filterData(data: number[], predicate: NumberPredicate): number[] {
  const result: number[] = [];
  for (const item of data) {
    if (predicate(item)) {
      result.push(item);
    }
  }
  return result;
}

// Data
const numericData: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Usage 1: Filter for even numbers
const isEven: NumberPredicate = (n) => n % 2 === 0;
const evenNumbers = filterData(numericData, isEven);
console.log(evenNumbers); // Expected: [2, 4, 6, 8, 10]

// Usage 2: Filter for numbers greater than 5
const greaterThanFive = filterData(numericData, (n) => n > 5);
console.log(greaterThanFive); // Expected: [6, 7, 8, 9, 10]
```

---

### Exercise 3: Function Overloading for Type-Safe Operations

**Objective**: Implement a function that behaves differently based on input types, using function overloading to provide compile-time type safety for each call signature.

**Entities**:
- **Concepts**: Function overloading.
- **Patterns**: Providing multiple function signatures for a single implementation function. The implementation signature must be general enough to handle all overload signatures.
- **Relationships**: Leverages union types (`string | string[]`) from Chunk 7 in the implementation signature to handle the different possible inputs specified in the overloads.
- **Software Engineering Principle**: **Clarity & Type Safety**. Overloading creates a clear, self-documenting API. Consumers of the function get specific, correct type information for their inputs, preventing incorrect usage at compile time.

**Problem**:
Create an overloaded function `formatInput`.
- If it receives a `string`, it should return the string in uppercase.
- If it receives an array of `string`s, it should join them with a comma and return the single resulting string.

**Artificial Data**:
```typescript
const singleString = "hello world";
const stringArray = ["typescript", "is", "powerful"];
```

**Task**:
1.  Declare two overload signatures for `formatInput`.
2.  Provide a single implementation for `formatInput` that checks the type of the input and performs the correct logic.
3.  Call both versions of the function and observe that TypeScript provides the correct return type for each call.

**Source Reference**:
-   **Theory**: TypeScript Handbook - [Function Overloads](https://www.typescriptlang.org/docs/handbook/2/functions.html#function-overloads). This is the primary source, explaining the "declaration" and "implementation" signature pattern.
-   **Implementation**: `typescript-handbook-v4.1.pdf`, Page 56, "Overloads", provides a clear example of a function `pickCard` that returns different types based on its input, which directly maps to this exercise.

**Solution**:
```typescript
// Overload signatures
function formatInput(input: string): string;
function formatInput(input: string[]): string;

// Implementation signature
function formatInput(input: string | string[]): string {
  if (typeof input === 'string') {
    return input.toUpperCase();
  } else {
    return input.join(', ');
  }
}

// Data
const singleString = "hello world";
const stringArray = ["typescript", "is", "powerful"];

// Usage
const result1 = formatInput(singleString);
console.log(result1); // Expected: "HELLO WORLD"

const result2 = formatInput(stringArray);
console.log(result2); // Expected: "typescript, is, powerful"

// const result3 = formatInput(123); // This would be a compile-time error
```

---

### Hardcore Combined Problem: Generic, Overloaded Data Processing Pipeline

**Objective**: Synthesize all concepts from this chunk to build a sophisticated, type-safe, and flexible data processing pipeline. This algorithm must leverage generics for type reusability, rest parameters for dynamic composition, overloads for API flexibility, and callbacks for final actions.

**Entities**:
- **Concepts**: Function Declarations, Typed Parameters, Return Types, Optional/Default Parameters, Rest Parameters, Function Overloading.
- **Patterns**: Arrow Functions, Callback Functions, Generic Functions, Higher-Order Functions.
- **Relationships**: This problem is a culmination of this chunk and heavily relies on advanced types from Chunk 7 (Type Aliases, Union Types, Function Types) to define its complex signatures.
- **Software Engineering Principles**:
    - **Scalability**: The pipeline can be extended with any number of transformation steps without changing its core logic.
    - **Flexibility**: Generics make the pipeline adaptable to any data type.
    - **Modularity**: Each transformer is a self-contained unit of logic.
    - **Clarity**: Overloading provides two clear, distinct ways to use the pipeline: immediate execution or deferred execution (currying).

**Problem**:
Create a function `createDataPipeline` that builds and executes a data processing pipeline.
1.  **Flexibility through Overloading**: The function must have two call signatures:
    *   One that accepts an initial dataset and a variable number of transformer functions, executing immediately.
    *   Another that accepts only the transformer functions and returns a new function that will accept the data later.
2.  **Type Safety through Generics**: The pipeline must be generic to handle any data type transformations (e.g., from `T[]` to `U[]` to `V[]`, etc.).
3.  **Dynamic Composition**: Use rest parameters to accept an arbitrary number of transformer functions.
4.  **Asynchronous-like Final Step**: Use an optional callback to handle the final, transformed data. If no callback is provided, log the result to the console.

**Artificial Data**:
```typescript
interface User {
  id: number;
  name: string;
  email: string;
  isActive: boolean;
}

const users: User[] = [
  { id: 1, name: "Alice", email: "alice@example.com", isActive: true },
  { id: 2, name: "Bob", email: "bob@example.com", isActive: false },
  { id: 3, name: "Charlie", email: "charlie@example.com", isActive: true },
];
```

**Task**:
1.  Define the necessary type aliases for transformer functions.
2.  Implement the two overload signatures for `createDataPipeline`.
3.  The implementation should process the data by applying each transformer function in sequence.
4.  Create and use the pipeline in both ways:
    *   **Immediate Execution**: A pipeline that filters active users, extracts their emails, and then prints the count.
    *   **Deferred Execution**: Create a reusable pipeline that transforms user names to uppercase. Apply this pipeline to the user data later.

**Source Reference**:
-   This problem requires a synthesis of all concepts in the chunk. The solution structure will resemble patterns from the *TypeScript Handbook* on [Functions](https://www.typescriptlang.org/docs/handbook/2/functions.html) and [Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html), combining ideas from overloading, rest parameters, and generic function types into a single, cohesive algorithm. The pattern of returning a function (currying) is an advanced application of higher-order functions.

**Solution**:
```typescript
// Type alias for any transformation function
type Transformer<T, U> = (data: T) => U;

// Default callback if none is provided
const defaultCallback = (result: any) => console.log("Pipeline Result:", result);

// Overload 1: Immediate execution
function createDataPipeline<T>(
  initialData: T[],
  ...transformers: Transformer<any, any>[]
): void;

// Overload 2: Deferred execution (returns a new function)
function createDataPipeline<T, U>(
  ...transformers: Transformer<any, any>[]
): (initialData: T[], onComplete?: (finalData: U) => void) => void;

// Implementation
function createDataPipeline(
  ...args: any[]
): void | ((initialData: any[], onComplete?: (finalData: any) => void) => void) {
  // Check if the first argument is data (for immediate execution)
  const isImmediate = Array.isArray(args[0]);
  
  const transformers: Transformer<any, any>[] = isImmediate ? args.slice(1) : args;

  const pipelineLogic = (
    initialData: any[], 
    onComplete: (finalData: any) => void = defaultCallback
  ) => {
    const result = transformers.reduce((currentData, transformer) => transformer(currentData), initialData);
    onComplete(result);
  };

  if (isImmediate) {
    pipelineLogic(args[0]);
    return;
  } else {
    return pipelineLogic;
  }
}

// Data
interface User {
  id: number;
  name: string;
  email: string;
  isActive: boolean;
}
const users: User[] = [
  { id: 1, name: "Alice", email: "alice@example.com", isActive: true },
  { id: 2, name: "Bob", email: "bob@example.com", isActive: false },
  { id: 3, name: "Charlie", email: "charlie@example.com", isActive: true },
];

// --- Usage 1: Immediate Execution ---
console.log("--- Immediate Execution ---");
const filterActive: Transformer<User[], User[]> = (data) => data.filter(u => u.isActive);
const getEmails: Transformer<User[], string[]> = (data) => data.map(u => u.email);
const countItems: Transformer<string[], string> = (data) => `Found ${data.length} active user emails.`;

createDataPipeline(users, filterActive, getEmails, countItems); // Uses default console.log callback

// --- Usage 2: Deferred Execution ---
console.log("\n--- Deferred Execution ---");
const nameToUppercase: Transformer<User[], { name: string }[]> = (data) => 
  data.map(u => ({ name: u.name.toUpperCase() }));

const reusablePipeline = createDataPipeline(nameToUppercase);

reusablePipeline(users, (finalData) => {
  console.log("Transformed User Names:", finalData);
});
```
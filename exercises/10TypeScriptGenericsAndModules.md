### **Exercise 1: The Generic Identity and Transformation Function**

*   **Objective**: Understand the fundamental syntax of generic functions and how type parameters create a link between input and output types.
*   **Problem Description**:
    1.  Create a generic function named `identity` that takes one argument of type `T` and returns a value of the same type `T`.
    2.  Create a second generic function named `transformTuple` that takes two arguments, one of type `T` and one of type `U`, and returns a tuple `[U, T]`.
*   **Artificial Data / Starter Code**:
    ```typescript
    // --- Test cases for your implementation ---

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
    ```
*   **Expected Output / Behavior**:
    ```
    Identity Number: 123, Type: number
    Identity String: hello, Type: string
    Transformed Tuple: [42, world]
    Type of first element: number
    Type of second element: string
    ```
*   **Theoretical Foundation & Source Reference**:
    *   **TypeScript Handbook**: The concept of the "Hello World of Generics" using an identity function is introduced, explaining how a type variable `T` captures and reuses a type. This exercise directly implements that concept.
        *   *Source*: `typescript-handbook-v4.1/04_Handbook.pdf`, Page 109, "Hello World of Generics".
    *   **C++ Templates**: Generics in TypeScript are conceptually similar to templates in C++, where a function or class can operate on generic types without knowing the specifics of those types beforehand.
        *   *Source*: `TheC++ProgrammingLanguage_BjarneStroustrup_2013_FourthEdition/Chapter_23_Templates.pdf`, Page 684, Section 23.5 "Function Templates".
*   **Software Engineering Principle Emphasis**:
    *   **Reusability**: A single generic function can operate on any data type, avoiding code duplication for different types (e.g., `identityNumber`, `identityString`). This adheres to the DRY (Don't Repeat Yourself) principle.

---

### **Exercise 2: Building a Generic, Modular Stack**

*   **Objective**: Apply generics to a class and structure a project using modules for better organization and scalability.
*   **Problem Description**:
    1.  In a file named `src/lib/stack.ts`, create a generic class `Stack<T>`. It should have the following methods:
        *   `push(item: T): void`: Adds an item to the top of the stack.
        *   `pop(): T | undefined`: Removes and returns the top item, or `undefined` if the stack is empty.
        *   `peek(): T | undefined`: Returns the top item without removing it.
        *   `isEmpty(): boolean`: Returns true if the stack is empty.
        *   `size(): number`: Returns the number of items in the stack.
    2.  In a file named `src/index.ts`, import the `Stack` class and demonstrate its functionality by creating two stacks: one for `number`s and one for `string`s.
*   **Artificial Data / Starter Code**:
    ```typescript
    // src/index.ts
    // import { Stack } from './lib/stack';

    // Number Stack
    const numberStack = new Stack<number>();
    numberStack.push(10);
    numberStack.push(20);
    console.log('Popped from numberStack:', numberStack.pop()); // 20
    console.log('Peek numberStack:', numberStack.peek());       // 10
    console.log('numberStack size:', numberStack.size());       // 1

    // String Stack
    const stringStack = new Stack<string>();
    stringStack.push("hello");
    stringStack.push("world");
    console.log('Popped from stringStack:', stringStack.pop()); // "world"
    console.log('Is stringStack empty?', stringStack.isEmpty()); // false
    ```
*   **Expected Output / Behavior**:
    ```
    Popped from numberStack: 20
    Peek numberStack: 10
    numberStack size: 1
    Popped from stringStack: world
    Is stringStack empty? false
    ```
*   **Theoretical Foundation & Source Reference**:
    *   **TypeScript Handbook**: This exercise directly implements a "Generic Class" as described in the handbook. The type parameter `<T>` on the class ensures that all its properties and methods operate consistently on the same type.
        *   *Source*: `typescript-handbook-v4.1/04_Handbook.pdf`, Page 115, "Generic Classes".
    *   **Modules**: The file structure (`stack.ts`, `index.ts`) follows the principles of ES modules, using `export` in the source file and `import` in the consuming file to manage dependencies and create a clear API boundary.
        *   *Source*: `typescript-handbook-v4.1/05_Handbook_Reference.pdf`, Pages 110-111, "Modules" and "Exporting a declaration".
*   **Software Engineering Principle Emphasis**:
    *   **Scalability**: By organizing code into modules (`stack.ts`), the project becomes easier to manage and scale. Other parts of the application can import the `Stack` without needing to know its implementation details.
    *   **Type Safety**: The generic `Stack<T>` prevents runtime errors by ensuring that a stack created for numbers cannot have strings pushed onto it, and vice-versa.

---

### **Exercise 3: Constrained Generics for Type-Safe Property Access**

*   **Objective**: Understand how to use generic constraints (`extends keyof`) to create functions that are both flexible and type-safe.
*   **Problem Description**:
    1.  Create an interface `User` with properties `id: number`, `name: string`, and `email: string`.
    2.  Create a generic function `getProperty<T, K extends keyof T>(obj: T, key: K)`. This function should accept an object `obj` and a key `key`, and return the value of the property at that key.
    3.  The generic constraint `K extends keyof T` ensures that the `key` passed to the function is a valid key of the object `T`.
*   **Artificial Data / Starter Code**:
    ```typescript
    interface User {
        id: number;
        name: string;
        email: string;
    }

    const user: User = {
        id: 1,
        name: "Alice",
        email: "alice@example.com"
    };

    // --- Your implementation of getProperty here ---

    // Valid calls
    const userName = getProperty(user, "name");
    const userId = getProperty(user, "id");
    console.log(`User Name: ${userName}`);
    console.log(`User ID: ${userId}`);

    // This should cause a compile-time error because 'address' is not a key of User
    // const userAddress = getProperty(user, "address");
    ```
*   **Expected Output / Behavior**:
    ```
    User Name: Alice
    User ID: 1
    ```
    A compile-time error should be reported for the call with the key `"address"`.
*   **Theoretical Foundation & Source Reference**:
    *   **TypeScript Handbook**: This exercise is a direct application of "Generic Constraints" and "Using Type Parameters in Generic Constraints". The `keyof` type operator creates a union of the known public property names of a type, which is then used as a constraint for the key parameter `K`.
        *   *Source*: `typescript-handbook-v4.1/04_Handbook.pdf`, Page 117, "Generic Constraints" and Page 119, "Using Type Parameters in Generic Constraints".
    *   **Basarat’s TypeScript Deep Dive**: The `keyof` operator and its use in creating type-safe lookup functions are core concepts of TypeScript's structural type system.
        *   *Source*: [Generics section in Basarat's Deep Dive](https://basarat.gitbook.io/typescript/type-system/generics).
*   **Software Engineering Principle Emphasis**:
    *   **Reliability**: Generic constraints prevent a whole class of runtime errors. Instead of failing silently or throwing an error at runtime when accessing a non-existent property, the compiler catches the mistake immediately. This creates more robust and reliable code.

---

### **Hardcore Problem: A Type-Safe, Modular Event Dispatcher**

*   **Objective**: Combine generics, constraints, interfaces, and modules to build a complex, yet type-safe and decoupled system.
*   **Problem Description**:
    Design and implement a modular Event Dispatcher system. The system should allow different parts of an application to communicate without being directly coupled. It must be fully type-safe, meaning that subscribing to an event guarantees the payload received is of the correct type.

    1.  **`src/lib/event-types.ts`**:
        *   Define an interface `EventMap` that maps string event names to their payload types.
        *   Export this interface. This will act as a single source of truth for all events in the application.
        *   Example: `{ 'user:created': { userId: number; name: string; }; 'user:deleted': { userId: number; }; }`

    2.  **`src/lib/dispatcher.ts`**:
        *   Create a generic class `EventDispatcher<T extends object>`. The generic `T` will be constrained to an object type (like our `EventMap`).
        *   Implement the following methods:
            *   `on<K extends keyof T>(eventName: K, callback: (payload: T[K]) => void): void`: Subscribes a callback to an event. The `eventName` must be a key of `T`, and the `callback`'s `payload` parameter must be of the type `T[K]`.
            *   `dispatch<K extends keyof T>(eventName: K, payload: T[K]): void`: Dispatches an event to all its subscribers, passing the typed payload.
        *   Export this class.

    3.  **`src/services/user-service.ts`**:
        *   A module that uses the dispatcher to announce user-related events.
        *   It should import the `EventDispatcher` and the `EventMap`.
        *   Create a function `createUser` that dispatches a `'user:created'` event with the correct payload.

    4.  **`src/services/logging-service.ts`**:
        *   A module that listens for events to perform logging.
        *   It should import the dispatcher and subscribe to `'user:created'` and `'user:deleted'` events, logging the correctly typed payload.

    5.  **`src/index.ts`**:
        *   The main entry point. It should create a single instance of the `EventDispatcher` with the `EventMap`, pass this instance to the services (dependency injection), and then trigger the `createUser` function to see the system in action.
*   **Artificial Data / Starter Code**:
    ```typescript
    // src/lib/event-types.ts
    export interface EventMap {
      'user:created': { userId: number; name: string; timestamp: Date };
      'user:deleted': { userId: number; timestamp: Date };
      'order:placed': { orderId: string; amount: number; userId: number };
    }

    // src/lib/dispatcher.ts
    // Your implementation of EventDispatcher<T> here...

    // src/services/user-service.ts
    // Import dispatcher instance and EventMap
    // export function createUser(dispatcher, name: string) { ... }

    // src/services/logging-service.ts
    // Import dispatcher instance and EventMap
    // export function setupLogging(dispatcher) { ... }

    // src/index.ts
    // Main setup and execution logic...
    // Create dispatcher, setup logging, and call createUser.
    ```
*   **Expected Output / Behavior**:
    *   The console should log messages from the `logging-service` when `createUser` is called.
    *   Attempting to dispatch an event with the wrong payload type (e.g., `dispatch('user:created', { userId: 123 })` without a `name`) should result in a compile-time error.
    *   Attempting to subscribe with a callback that expects the wrong payload type should also result in a compile-time error.
*   **Theoretical Foundation & Source Reference**:
    *   **Generics & Constraints**: The core of this problem lies in `K extends keyof T` and the indexed access type `T[K]`. This pattern creates a type-safe link between an event's name (the key) and its payload (the value associated with that key).
        *   *Source*: `typescript-handbook-v4.1/04_Handbook.pdf`, Page 119, "Using Type Parameters in Generic Constraints", and Page 117, "Generic Constraints".
    *   **Modules**: The entire architecture is based on modules. The dispatcher, services, and type definitions are in separate files. This promotes loose coupling: `user-service` and `logging-service` do not know about each other; they only know about the `EventDispatcher` contract.
        *   *Source*: `typescript-handbook-v4.1/07_Declaration_Files.pdf`, Pages 12-13, "Modular Libraries" and "Templates For Modules" demonstrate how to structure such code.
    *   **Interfaces**: `EventMap` serves as a central contract or "schema" for all events, making the system predictable and self-documenting.
        *   *Source*: `typescript-handbook-v4.1/04_Handbook.pdf`, Page 22, "Our First Interface".
*   **Software Engineering Principle Emphasis**:
    *   **Decoupling & Scalability**: This design exemplifies the publish-subscribe pattern, which decouples components. New services can be added to listen for events without modifying the event producers, making the system highly scalable and maintainable.
    *   **Single Source of Truth**: The `EventMap` interface acts as a single, authoritative source for what events exist and what their shapes are, which is crucial for reliability in large systems.
    *   **Type Safety & Reliability**: The use of advanced generics eliminates a major source of bugs in event-driven architectures: mismatched event payloads. Errors are caught at compile time, not at runtime, leading to a far more reliable application.
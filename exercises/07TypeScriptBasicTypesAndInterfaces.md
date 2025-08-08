## Chunk 7: TypeScript Basic Types And Interfaces

### Exercise 1: Foundational Types and Data Structures

**Description:**
You are building a user profile system. Define the basic data structures for a user. Create a type alias for a `UserID` which can only be a `number`. Define another type alias `UserContact` which is a tuple containing an email (`string`) and a phone number (`number`). Finally, create a user profile variable that holds an array of `UserContact` tuples, a `UserID`, a username (`string`), and a boolean flag `isActive`. Populate this variable with artificial data.

**Key Skills:** Manipulating primitive/collection types, type conversions, applying operators.
**Complexity:** Basic type operations.

**Artificial Data:**

```typescript
// Data for the user profile
const userID: number = 101;
const userName: string = "alex_jones";
const isUserActive: boolean = true;
const userContacts: [string, number][] = [
    ["alex.jones@example.com", 1234567890],
    ["secondary.aj@work.com", 9876543210]
];
```

**Task:**
1.  Define a type alias `UserID` for the `number` type.
2.  Define a type alias `UserContact` for a tuple that holds a `string` (email) and a `number` (phone number).
3.  Declare a variable `userProfile` and annotate it with a structure that includes:
    *   `id` of type `UserID`.
    *   `username` of type `string`.
    *   `active` of type `boolean`.
    *   `contacts` which is an array of `UserContact`.
4.  Initialize `userProfile` with the provided artificial data.

**Software Engineering Principles:**
*   **Modifiability:** Using type aliases like `UserID` makes the code easier to refactor. If the user ID format changes (e.g., to a string), you only need to update the type alias definition.

**Source Reference:**
*   **Concepts**: Primitive Types (`number`, `string`, `boolean`), Array Types, Tuple Types, Type Aliases.
*   **Theory**: `typescript-handbook-v4.1.pdf`, Pages 6-8 (Boolean, Number, String, Array, Tuple), `typescript-handbook-v4.1-reference.pdf`, Page 11 (Type Aliases).

---

### Exercise 2: Structuring API Data with Interfaces

**Description:**
You are fetching data from a movie database API. The API returns a complex object for each movie. Your task is to define a strict `interface` named `Movie` to model this data. The `Movie` object has a required `title`, `director`, and `releaseYear`. It also has an optional `boxOffice` object, which itself contains `budget` and `gross` numbers. Not all movies in the database have box office information.

**Key Skills:** Defining types, applying interfaces.
**Exercise Context:** Create interfaces for API data.
**Complexity:** Interfaces with nested objects and optional properties.

**Artificial Data:**

```typescript
// Movie with complete data
const movie1 = {
    title: "Inception",
    director: "Christopher Nolan",
    releaseYear: 2010,
    boxOffice: {
        budget: 160000000,
        gross: 829900000
    }
};

// Movie without box office data
const movie2 = {
    title: "Primer",
    director: "Shane Carruth",
    releaseYear: 2004
};
```

**Task:**
1.  Define an interface `BoxOffice` with two `number` properties: `budget` and `gross`.
2.  Define an interface `Movie` with the following properties:
    *   `title`: `string`
    *   `director`: `string`
    *   `releaseYear`: `number`
    *   `boxOffice`: An optional (`?`) property of type `BoxOffice`.
3.  Declare two variables, `inception` and `primer`, both of type `Movie`.
4.  Initialize them with the provided artificial data, ensuring TypeScript validates both objects against the `Movie` interface.

**Software Engineering Principles:**
*   **Reliability:** By defining a strict interface for the API response, you prevent runtime errors that could occur from accessing non-existent properties (e.g., trying to read `movie2.boxOffice.gross`).

**Source Reference:**
*   **Concepts**: Interfaces, Optional Properties (`?`).
*   **Theory**: `typescript-handbook-v4.1.pdf`, Pages 22-25 (Our First Interface, Optional Properties).

---

### Exercise 3: Flexible Data Representation with Unions and Intersections

**Description:**
Your application needs to handle various types of media content. Some content is basic, while other types have extended attributes. Create a system using type aliases that combines these attributes. All media has an `id` and a `sourceUrl`. `Video` media has a `duration` in seconds. `Image` media has `width` and `height` dimensions. A `PromotedPost` can be either a `Video` or an `Image` and also has a `sponsor` name and `campaignId`.

**Key Skills:** Applying interfaces, using unions for flexible inputs, combining types.
**Complexity:** Complex interfaces and unions.

**Artificial Data:**

```typescript
const promotedVideo = {
    id: 1,
    sourceUrl: "https://example.com/video.mp4",
    duration: 120,
    sponsor: "TechCorp",
    campaignId: "TC-001"
};

const promotedImage = {
    id: 2,
    sourceUrl: "https://example.com/image.jpg",
    width: 1920,
    height: 1080,
    sponsor: "AdCo",
    campaignId: "AC-002"
};
```

**Task:**
1.  Create a base `type` alias `Media` for an object with `id: number` and `sourceUrl: string`.
2.  Create a `type` alias `Video` by intersecting (`&`) `Media` with an object containing `duration: number`.
3.  Create a `type` alias `Image` by intersecting (`&`) `Media` with an object containing `width: number` and `height: number`.
4.  Create a `type` alias `PromotableContent` which is a union (`|`) of `Video` and `Image`.
5.  Create a final `type` alias `PromotedPost` by intersecting `PromotableContent` with an object containing `sponsor: string` and `campaignId: string`.
6.  Declare and initialize two variables of type `PromotedPost` with the provided data.

**Software Engineering Principles:**
*   **Scalability & Modifiability:** Using unions and intersections allows you to compose complex types from smaller, reusable pieces. Adding a new media type (e.g., `Audio`) only requires defining a new type and adding it to the `PromotableContent` union, without breaking existing logic.

**Source Reference:**
*   **Concepts**: Type Aliases, Union Types (`|`), Intersection Types (`&`).
*   **Theory**: `typescript-handbook-v4.1.pdf`, Pages 66-68 (Union Types), Page 75 (Intersection Types); `typescript-handbook-v4.1-reference.pdf`, Pages 11-12 (Type Aliases).

---

### Exercise 4: Safe Data Processing with `unknown`, `any`, and `never`

**Description:**
You are processing raw input from an external, untrusted source, which could be anything. Your function must safely parse this input. If the input is a `string`, parse it. If it's a `number`, convert it to a string. If it's anything else, log an error. Also, create a special error-logging function that never returns, indicating a process failure. Avoid using `any` where type safety can be enforced.

**Key Skills:** Ensuring type safety, type narrowing.
**Exercise Context:** Handling unknown data, distinguishing `any` from `unknown`.
**Complexity:** Advanced/utility types.

**Artificial Data:**

```typescript
const inputs: unknown[] = [
    "hello world",
    12345,
    true,
    { message: "this is an object" },
    null
];
```

**Task:**
1.  Create a function `processInput(input: unknown): string`.
2.  Inside the function, use `typeof` guards to check if `input` is a `string` or a `number`.
    *   If it's a `string`, return it directly.
    *   If it's a `number`, return its string representation.
3.  If the input is neither a `string` nor a `number`, the function should call a separate error-handling function `logError`.
4.  Define the function `logError(message: string): never`. This function should throw an `Error` with the provided message. This use of `never` signals to the TypeScript compiler that this path will never return a value, ensuring exhaustive checks.
5.  Loop through the `inputs` array and call `processInput` for each item, wrapping it in a try/catch block to handle the thrown errors.

**Software Engineering Principles:**
*   **Reliability:** Using `unknown` forces you to perform explicit type checks (narrowing), preventing unsafe operations and making the code more robust compared to `any`, which would bypass the type checker. The `never` type ensures that all possible code paths are handled.

**Source Reference:**
*   **Concepts**: Utility Types (`unknown`, `any`, `never`), Type Narrowing (`typeof`).
*   **Theory**: `typescript-handbook-v4.1.pdf`, Pages 12-16 (Unknown, Any, Never); `typescript-handbook-v4.1-reference.pdf`, Page 7 (typeof type guards).

---

### Hardcore Combined Problem: Type-Safe Event Processing System

**Description:**
You are architecting a client-side event processing system. The system receives a raw, untrusted array of event objects from a WebSocket. Your task is to create a type-safe pipeline that validates, discriminates, and processes these events.

The system must handle three types of events:
1.  `UserSignIn`: Contains `userId` (string) and `timestamp` (number).
2.  `UserSignOut`: Contains `userId` (string) and `timestamp` (number).
3.  `MessageBroadcast`: Contains `message` (string), `senderId` (string), and an optional `recipientId` (string).

**Key Skills:** Defining types, applying interfaces, ensuring type safety, type narrowing, combining types.
**Complexity:** Combination of all concepts from the chunk.

**Artificial Data:**

```typescript
const rawEvents: unknown[] = [
    { eventType: "USER_SIGN_IN", userId: "user-123", timestamp: 1672531200 },
    "this is not an event",
    { eventType: "MESSAGE_BROADCAST", senderId: "user-456", message: "Hello everyone!" },
    { eventType: "USER_SIGN_OUT", userId: "user-123", timestamp: 1672534800 },
    { eventType: "MESSAGE_BROADCAST", senderId: "user-789", recipientId: "user-456", message: "Hi there!" },
    null,
    { eventType: "UNKNOWN_EVENT", data: "..." }
];
```

**Task:**
1.  **Base Interface and Intersection:**
    *   Define an `interface` `EventMetadata` with `timestamp: number`.
    *   Define an `interface` `UserSignInEvent` with `eventType: "USER_SIGN_IN"`, `userId: string`.
    *   Define an `interface` `UserSignOutEvent` with `eventType: "USER_SIGN_OUT"`, `userId: string`.
    *   Define an `interface` `MessageBroadcastEvent` with `eventType: "MESSAGE_BROADCAST"`, `senderId: string`, `message: string`, and an optional `recipientId?: string`.

2.  **Union Type Alias:**
    *   Create a `type` alias `SystemEvent` that is a union of three types created by intersecting the specific event interfaces with `EventMetadata` (e.g., `(UserSignInEvent & EventMetadata)`). This ensures all valid events have a `timestamp`.

3.  **Validation and Type Assertion:**
    *   Create a function `isSystemEvent(obj: unknown): obj is SystemEvent`.
    *   This function should validate that `obj` is an object, has a valid `eventType` literal, and contains the required properties for that type. Return `true` if it's a valid `SystemEvent`, otherwise `false`. This is your user-defined type guard.

4.  **Discriminated Union Processing:**
    *   Create a function `processEvent(event: SystemEvent): void`.
    *   Use a `switch` statement on the `event.eventType` property (the discriminant) to handle each event type.
    *   Inside each `case`, TypeScript should correctly narrow the `event` type, allowing you to safely access properties specific to that event (e.g., `event.userId` or `event.message`).
    *   Log a descriptive message for each event type.
    *   Use a `default` case that calls an `unreachable` function with the event.

5.  **Exhaustiveness Checking:**
    *   Create the `unreachable(x: never): never` function that throws an error. This ensures that if a new event type is added to the `SystemEvent` union, the compiler will raise an error if it's not handled in the `switch` statement.

6.  **Main Pipeline:**
    *   Iterate over the `rawEvents` array.
    *   For each raw event, use your `isSystemEvent` type guard to validate it.
    *   If valid, pass it to the `processEvent` function. If invalid, log a validation error.

**Software Engineering Principles:**
*   **Reliability & Testability:** The entire pipeline is designed for robustness. `unknown` forces validation at the entry point. The discriminated union pattern makes the processing logic clean, safe, and easy to test, while the `never` type in the `default` case guarantees that all event types are handled at compile time.
*   **Modifiability:** To add a new event type, you only need to: 1) define its interface, 2) add it to the `SystemEvent` union, 3) update the `isSystemEvent` validator, and 4) add a new `case` to the `processEvent` function. The compiler will guide you to ensure all necessary changes are made.

**Source Reference:**
*   **Concepts**: All concepts from Chunk 7 are used here: Interfaces, Type Aliases, Union (`|`) & Intersection (`&`) types, `unknown`, `never`, Literal Types, Type Assertions (`as`), and Type Narrowing (`typeof` and user-defined type guards).
*   **Theory**: This problem combines concepts from across the `typescript-handbook-v4.1.pdf` and its reference, particularly "Interfaces" (p. 21), "Union Types" (p. 66), "Literal Types" (p. 61), "Type Guards" (`-reference.pdf`, p. 3), and "Unknown/Never" (p. 12-16).
### Exercise 1: Basic Class and Interface Implementation

**Objective**: Master basic class syntax, including constructors, properties, methods, and implementing interfaces. This exercise connects to **Chunk 7** (Interfaces) and **Chunk 8** (Functions) by applying them in a class context.

**Task**:
1.  Define an interface `IUser` with the following properties:
    *   `id`: a `readonly` number.
    *   `username`: a string.
    *   `email`: a string.
    *   `getProfileSummary()`: a method that returns a string.
2.  Create a class `User` that implements the `IUser` interface.
3.  The constructor should initialize `id`, `username`, and `email`. The `id` should be a random number.
4.  Implement the `getProfileSummary` method to return a string like: `ID: [id], Username: [username], Email: [email]`.
5.  Instantiate the `User` class with the provided data and log the profile summary to the console.

**Artificial Data**:
```typescript
const userData = {
  username: "johndoe",
  email: "john.doe@example.com"
};
```

**Software Engineering Principle**: **Modifiability**. By implementing an interface, you create a contract that separates the "what" from the "how". Other parts of an application can depend on the `IUser` interface, making it easier to swap in different implementations of a `User` later without breaking dependent code.

**Source Reference**:
*   **Theory**: The fundamental structure of a class, including properties, a constructor for initialization, and methods, is detailed in the TypeScript Handbook. The concept of ensuring a class structure conforms to a contract is covered under interface implementation. [typescript-handbook-v4.1.pdf: Pages 76-78, 91]

### Exercise 2: Inheritance and Access Modifiers

**Objective**: Understand how to build a class hierarchy using `extends` and `super()`. Apply `public`, `private`, and `protected` access modifiers to control visibility and enforce encapsulation.

**Task**:
1.  Create a base class `Vehicle` with the following members:
    *   A `protected` property `brand` (string).
    *   A `protected` property `year` (number).
    *   A `public` constructor to initialize `brand` and `year`.
    *   A `public` method `getDetails()` that returns a string: `Brand: [brand], Year: [year]`.
2.  Create a derived class `Car` that `extends` `Vehicle`.
    *   A `private` property `numberOfDoors` (number).
    *   A constructor that initializes `brand`, `year`, and `numberOfDoors`. It must call the parent constructor.
    *   Override the `getDetails` method to include the number of doors: `Brand: [brand], Year: [year], Doors: [numberOfDoors]`.
3.  Instantiate `Car` with data and log its details. Try to access the `brand` and `numberOfDoors` properties from outside the class to observe the access modifier restrictions.

**Artificial Data**:
```typescript
const carData = {
  brand: "Honda",
  year: 2021,
  doors: 4
};
```

**Software Engineering Principle**: **Reliability**. Access modifiers are crucial for reliability. Making `numberOfDoors` `private` prevents external code from setting an invalid value (e.g., a negative number), ensuring the object's internal state remains consistent and valid. `protected` allows subclasses to build upon the base class's state while still hiding it from the public interface.

**Source Reference**:
*   **Theory**: The TypeScript Handbook explains class inheritance using the `extends` keyword and the necessity of `super()` in derived class constructors. It also details the behavior of `public`, `private`, and `protected` modifiers. The `private` modifier ensures that a member is only visible within its containing class, while `protected` allows visibility in derived classes as well. [typescript-handbook-v4.1.pdf: Pages 78-79, 82-85]

### Exercise 3: Static and Readonly Properties

**Objective**: Implement and correctly use `static` members for class-level data/methods and `readonly` properties for immutable instance attributes.

**Task**:
1.  Create a class `AppConfig` to manage application settings.
2.  Add a `public static readonly` property `appName` initialized to "MyApp".
3.  Add a `private static` property `instanceCounter` initialized to `0`.
4.  Add a `public readonly` instance property `configId` (number).
5.  The constructor should not take any arguments but should increment the `instanceCounter` and assign its value to `configId`.
6.  Add a `public static` method `getInstanceCount()` that returns the value of `instanceCounter`.
7.  Create two instances of `AppConfig`. Log the `appName` and the total instance count using the static members. Log the unique `configId` for each instance. Attempt to modify `appName` and `configId` to confirm they are readonly.

**Artificial Data**: No external data is needed for this exercise.

**Software Engineering Principle**: **Testability**. Static methods like `getInstanceCount` can be tested without creating an instance of the class, simplifying unit tests. `readonly` properties enhance predictability by ensuring that instance-specific identifiers (`configId`) or global settings (`appName`) remain constant after initialization.

**Source Reference**:
*   **Theory**: The TypeScript Handbook specifies that `static` members belong to the class itself, not to instances. `readonly` properties can only be set during initialization (in their declaration or in the constructor). This combination is powerful for creating constants that are globally accessible via the class without needing an instance. [typescript-handbook-v4.1.pdf: Pages 89, 85-86]

### Hardcore Combined Problem: A Digital Media Lending Library

**Objective**: Integrate all concepts from Chunk 9 (Classes, Inheritance, Access Modifiers, Abstract Classes, Interfaces, Static & Readonly properties) to build a small but robust system. This problem requires you to architect a class hierarchy that is scalable and reliable.

**Task**:
1.  **Define an Interface**: Create an `ILendable` interface with two methods: `borrow()` and `returnItem()`, both returning `void`.
2.  **Create an Abstract Class**:
    *   Design an `abstract` class named `LibraryItem`.
    *   It should have a `public readonly` property `libraryId` (number).
    *   It should have a `protected static` counter `nextId` initialized to `1`, used to assign a unique `libraryId` to each new item in the constructor.
    *   The constructor should accept a `public title` (string).
    *   Include a `public abstract` method `getDetails()` that returns a string.
3.  **Create Concrete Classes**:
    *   Create a `Book` class that `extends LibraryItem` and `implements ILendable`.
        *   It should have a `private author` (string) and a `protected isBorrowed` (boolean) flag.
        *   The constructor should call `super` and initialize the `author`.
        *   Implement `getDetails()` to return a summary including title, author, and borrowed status.
        *   Implement the `ILendable` methods: `borrow` should set `isBorrowed` to `true` if it's not already borrowed, and `returnItem` should set it to `false`.
    *   Create a `Magazine` class that `extends LibraryItem` and `implements ILendable` with similar logic, but with a `private issueNumber` (number) instead of an author.
4.  **Build and Test the System**:
    *   Instantiate several `Book` and `Magazine` objects.
    *   Log the details of each item.
    *   Borrow an item, then log its details again to see the status change.
    *   Attempt to borrow an already borrowed item.
    *   Return the item and log its details.

**Artificial Data**:
```typescript
const bookData = { title: "Designing Data-Intensive Applications", author: "Martin Kleppmann" };
const magazineData = { title: "Communications of the ACM", issue: 12 };
```

**Software Engineering Principles**:
*   **Scalability**: The use of an `abstract` base class and an interface means the system can be easily extended with new types of media (e.g., `DVD`, `Audiobook`) without changing existing code that works with `LibraryItem` or `ILendable`.
*   **Reliability**: `private` and `protected` modifiers ensure that the internal state (like `isBorrowed` or the `static` ID counter) cannot be corrupted from outside the class, leading to a more robust and predictable system.
*   **Modifiability**: The logic for borrowing is encapsulated within each lendable item, making it easy to change how borrowing works for one type of item without affecting others.

**Source Reference**:
*   **Theory**: This problem synthesizes multiple concepts from the TypeScript Handbook. **Abstract Classes** [p. 90-91] serve as a template for derived classes. **Inheritance** (`extends`) and **Interface Implementation** (`implements`) create the structure [p. 36, 78-79]. **Access Modifiers** (`private`, `protected`, `public`) enforce encapsulation [p. 82-85]. **Static members** manage class-level state (`nextId`) [p. 89], and `readonly` ensures instance identifiers are immutable once created [p. 85-86]. This structure is a canonical example of object-oriented design in TypeScript.
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lecture: TypeScript Basic Types and Interfaces</title>
    <link rel="stylesheet" href="styles/lecture.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code&family=Lato:wght@400;700&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>

<div class="toc-popup-container">
    <input type="checkbox" id="toc-toggle" class="toc-toggle-checkbox" checked>
    <label for="toc-toggle" class="toc-toggle-label">
        <span>Lecture Navigation</span>
        <span class="toc-icon-open"></span>
    </label>
    <div class="toc-content">
        <h4>Table of Contents</h4>
        <ul>
            <li><a href="#section-1">1. Foundational Types</a></li>
            <li><a href="#section-2">2. Structuring with Interfaces</a></li>
            <li><a href="#section-3">3. Composable Types</a></li>
            <li><a href="#section-4">4. Handling Untrusted Data</a></li>
            <li><a href="#section-5">5. Discriminated Unions</a></li>
        </ul>
    </div>
</div>

<div class="container">
    <h1>Lecture: TypeScript Basic Types and Interfaces</h1>

<h2 id="section-1">1. Foundational Types: Primitives, Collections, and Aliases</h2>
<p><strong>Concept</strong>: TypeScript provides a static type layer over JavaScript. The most fundamental types are primitives, which represent simple, immutable data. They are the <strong>digital atoms</strong> of our code. Collections group this data, and type aliases provide readable, reusable names for any type.</p>
<ul>
    <li><strong>Primitive Types</strong>:
        <ul>
            <li><code>string</code>: Textual data. e.g., <code>"alex_jones"</code>.</li>
            <li><code>number</code>: Floating-point numbers. e.g., <code>101</code>.</li>
            <li><code>boolean</code>: <code>true</code> or <code>false</code> values. e.g., <code>true</code>.</li>
            <li><code>null</code> & <code>undefined</code>: These represent the <strong>intentional absence</strong> and the <strong>unintentional void</strong>. They are distinct types.</li>
        </ul>
    </li>
    <li><strong>Collection Types</strong>:
        <ul>
            <li><strong>Array</strong>: A typed list of elements. Syntax: <code>type[]</code> or <code>Array<type></code>. A container for multiples of the same kind.</li>
            <li><strong>Tuple</strong>: An array with a fixed number of elements of known types. It’s an array that has become a <strong>structure absolute</strong>. Syntax: <code>[type1, type2, ...]</code>.</li>
        </ul>
    </li>
    <li><strong>Type Alias</strong>: A custom name for a type. A type alias is a <strong>convenience name</strong>; it doesn't create a new, distinct type but acts as a pointer to another. Syntax: <code>type AliasName = existingType;</code>.</li>
</ul>

<h3>Example: Defining User Contact Information</h3>
<p>Use type aliases to create domain-specific types from primitives (e.g., <code>type UserID = number;</code>). This enhances readability and makes future refactoring easier. If <code>UserID</code> needs to become a <code>string</code>, you only change the alias definition.</p>
    
```typescript
// --- Artificial Data ---
const userId: number = 101;
const contactEmail: string = "contact@example.com";
const contactPhone: number = 1234567890;

// --- Type Definitions ---
// A UserID is a 'number name'—it gives a specific role to a primitive.
type UserID = number;

// A UserContact is a 'data pair'—a tuple defining a strict two-part structure.
type UserContact = [string, number]; // [email, phone]

// --- Variable Declaration ---
// The `userProfile` variable is strongly typed.
const userProfile: {
  id: UserID;
  contacts: UserContact[];
} = {
  id: userId,
  contacts: [
    [contactEmail, contactPhone],
  ],
};
```
<div class="oracle-specific">
    <h3>Software Engineering Principle</h3>
    <p><strong>Modifiability</strong>: With type aliases, your code becomes a <strong>forgiving history</strong>. If <code>UserID</code> must change from <code>number</code> to <code>string</code>, the change is localized, preventing a cascade of errors.</p>
</div>
<div class="postgresql-bridge">
    <h4>Source Reference</h4>
    <p><strong>Theory</strong>: <code>typescript-handbook-v4.1.pdf</code>, Pages 6-8 (Boolean, Number, String, Array, Tuple). <code>typescript-handbook-v4.1-reference.pdf</code>, Page 11 (Type Aliases).</p>
</div>

<h2 id="section-2">2. Structuring Complex Data with Interfaces</h2>
<p><strong>Concept</strong>: An <code>interface</code> defines a "contract" or shape. It’s not just a set of properties; it's a <strong>thought architecture</strong> for your objects, ensuring they are built correctly.</p>
<ul>
    <li><strong>Properties</strong>:
        <ul>
            <li><strong>Required</strong>: The non-negotiable fields.</li>
            <li><strong>Optional (<code>?</code>)</strong>: A property that might exist. The question mark provides a <strong>guarantee of uncertainty</strong>, forcing you to check for its existence.</li>
            <li><strong>Readonly</strong>: Properties that are <strong>change forbidden</strong> after an object is created. They are set in stone upon initialization.</li>
        </ul>
    </li>
</ul>

<h3>Example: Modeling a Product Catalog</h3>
<p>Define interfaces for any complex object structure, especially for data from external sources like APIs. An interface acts as a <strong>customs declaration</strong> for data entering your application.</p>
    
```typescript
// --- Artificial Data ---
const productA = {
    id: "abc-123",
    name: "Quantum Keyboard",
    price: 199.99,
    specs: {
        switches: "Mechanical",
        layout: "TKL"
    }
};

const productB = {
    id: "def-456",
    name: "Photon Mouse",
    price: 89.50
};

// --- Interface Definitions ---
interface ProductSpecs {
    readonly switches: string;
    readonly layout: string;
}

interface Product {
    readonly id: string; // The product's identity is an immutable fact.
    name: string;
    price: number;
    specs?: ProductSpecs; // 'specs' is optional, a potential but not promised feature.
}

// --- Variable Declarations ---
const keyboard: Product = productA;
const mouse: Product = productB;

// keyboard.id = "new-id"; // Error: Cannot assign to 'id' because it is a read-only property.
```
<div class="oracle-specific">
    <h3>Software Engineering Principle</h3>
    <p><strong>Reliability</strong>: Interfaces prevent runtime errors by catching invalid data shapes at compile time. Attempting to access <code>mouse.specs.layout</code> would be a compile-time error. It makes your code a <strong>serene process</strong>.</p>
</div>
<div class="postgresql-bridge">
    <h4>Source Reference</h4>
    <p><strong>Theory</strong>: <code>typescript-handbook-v4.1.pdf</code>, Pages 21-26 (Our First Interface, Optional Properties, Readonly properties).</p>
</div>

<h2 id="section-3">3. Creating Flexible and Composable Types</h2>
<p><strong>Concept</strong>: While interfaces define specific shapes, <code>union</code> and <code>intersection</code> types provide a powerful way to create <strong>type-borgs</strong>—new types assembled from existing parts.</p>
<ul>
    <li><strong>Union Types (<code>|</code>)</strong>: A value that can be one of several types. It’s a <strong>state dual</strong>, existing as one possibility among many. You can only access properties common to all types until you clarify its identity.</li>
    <li><strong>Intersection Types (<code>&</code>)</strong>: Combines multiple types into one. The new type is a <strong>conceptual fusion</strong>, possessing all properties from its constituent parts.</li>
</ul>

<h3>Example: Application Notifications</h3>
<p>Use intersections to build complex types from reusable parts and unions to model values that can exist in different forms.</p>
    
```typescript
// --- Artificial Data ---
const alertNotification = { id: 1, read: false, level: "warning", message: "Storage is almost full." };
const messageNotification = { id: 2, read: true, sender: "Admin", content: "Maintenance tomorrow." };

// --- Type Definitions ---
type BaseNotification = { readonly id: number; read: boolean; };
type Alert = BaseNotification & { level: "info" | "warning" | "error"; message: string; };
type Message = BaseNotification & { sender: string; content: string; };
type Notification = Alert | Message;

// --- Variable Declarations ---
const notifications: Notification[] = [alertNotification, messageNotification];

function getNotificationIcon(notification: Notification): string {
    // This is a 'veil of simplicity'. Without narrowing, we only see the common ground.
    // console.log(notification.message); // Error!

    if ("level" in notification) {
        return notification.level === "error" ? "error-icon" : "info-icon";
    }
    return "message-icon";
}
```
<div class="oracle-specific">
    <h3>Software Engineering Principle</h3>
    <p><strong>Scalability</strong>: Composing types allows your system to undergo <strong>synthetic evolution</strong>. Adding a new notification type is a small, localized change, and the compiler will guide you to handle the new case everywhere.</p>
</div>
<div class="postgresql-bridge">
    <h4>Source Reference</h4>
    <p><strong>Theory</strong>: <code>typescript-handbook-v4.1.pdf</code>, Pages 66-68 (Union Types), Page 75 (Intersection Types). <code>typescript-handbook-v4.1-reference.pdf</code>, Pages 13 (Interfaces vs. Type Aliases).</p>
</div>

<h2 id="section-4">4. Handling Untrusted Data Safely: <code>any</code>, <code>unknown</code>, and <code>never</code></h2>
<p><strong>Concept</strong>: TypeScript provides special types for navigating the boundary between the type-safe world and the unpredictable wild of external data.</p>
<ul>
    <li><code>any</code>: The <strong>type anarchist</strong>. It disables all type checking. It offers <strong>freedom traded</strong> for safety. Use it sparingly, as it creates a <strong>trap invisible</strong>.</li>
    <li><code>unknown</code>: The <strong>locked box</strong>. It accepts any value, but to operate on it, you must first prove what it is through type-narrowing.</li>
    <li><code>never</code>: The <strong>impossible type</strong>. It represents a state that cannot exist. It is the sound of a code path that logically cannot be taken.</li>
</ul>

<h3>Example: Parsing a Raw Configuration Object</h3>
<p>Always prefer <code>unknown</code> over <code>any</code> for external data. This forces safe, defensive code that validates data before use.</p>
    
```typescript
// --- Artificial Data ---
const rawConfig: unknown = JSON.parse('{ "port": 8080, "host": "localhost" }');
const invalidConfig: unknown = "not a config";

// --- Type Definitions and Functions ---
interface AppConfig { port: number; host: string; }

function logAndExit(message: string): never {
    console.error(message);
    throw new Error(message);
}

function loadConfig(config: unknown): AppConfig {
    if (typeof config === "object" && config !== null && "port" in config && "host" in config) {
        return config as AppConfig;
    }
    logAndExit("Invalid configuration object provided.");
}

// --- Usage ---
const appConfig = loadConfig(rawConfig);
console.log(`Server running on ${appConfig.host}:${appConfig.port}`);
```

<div class="oracle-specific">
    <h3>Software Engineering Principle</h3>
    <p><strong>Reliability</strong>: Using <code>unknown</code> forces a clear boundary between trusted and untrusted data. <code>never</code> ensures that failure paths are deliberate and absolute, preventing the system from continuing in a corrupted state.</p>
</div>
<div class="postgresql-bridge">
    <h4>Source Reference</h4>
    <p><strong>Theory</strong>: <code>typescript-handbook-v4.1.pdf</code>, Pages 12-16 (Unknown, Any, Never). <code>typescript-handbook-v4.1-reference.pdf</code>, Page 3-7 (Type Guards).</p>
</div>

<h2 id="section-5">5. The Discriminated Union Pattern</h2>
<p><strong>Concept</strong>: This is where our linguistic tools converge to create a <strong>perfectly hollow mountain</strong>: an architecture that is powerful on the inside and elegantly simple on the outside. It combines literal types, interfaces, and unions for fully type-safe state modeling.</p>
<ol>
    <li>A common, string literal property—the <strong>discriminant</strong> (e.g., <code>eventType</code>).</li>
    <li>A type alias that is a <strong>union</strong> of the different shapes.</li>
    <li>Type guards (usually a <code>switch</code> statement) on the discriminant to narrow the union.</li>
</ol>

<h3>Example: A Type-Safe Event Handling System</h3>
<p>Whenever you have an object that can be one of several distinct variants, use a discriminated union.</p>
    
```typescript
// --- Artificial Data ---
const signInEventData = { eventType: "USER_SIGN_IN", userId: "user-1", timestamp: Date.now() };
const messageEventData = { eventType: "MESSAGE_SENT", senderId: "user-2", content: "Hello!", timestamp: Date.now() };

// --- Interface and Type Definitions ---
interface BaseEvent { timestamp: number; }
interface UserSignInEvent extends BaseEvent { eventType: "USER_SIGN_IN"; userId: string; }
interface MessageSentEvent extends BaseEvent { eventType: "MESSAGE_SENT"; senderId: string; content: string; }

type AppEvent = UserSignInEvent | MessageSentEvent;

// --- Processing Logic ---
function handleEvent(event: AppEvent) {
    console.log(`Processing event at ${new Date(event.timestamp).toLocaleTimeString()}`);
    // The switch statement is where chaos harmonizes.
    switch (event.eventType) {
        case "USER_SIGN_IN":
            console.log(`User ${event.userId} signed in.`);
            break;
        case "MESSAGE_SENT":
            console.log(`Message from ${event.senderId}: ${event.content}`);
            break;
        default:
            // This case should be unreachable.
            const _exhaustiveCheck: never = event;
            return _exhaustiveCheck;
    }
}

// --- Usage ---
handleEvent(signInEventData);
handleEvent(messageEventData);
```

<div class="oracle-specific">
    <h3>Software Engineering Principle</h3>
    <p><strong>Maintainability & Reliability</strong>: Discriminated unions make future extensions safe. When a new event type is added, the compiler becomes your co-pilot. The <code>never</code> type ensures that <strong>complexity surrenders</strong> to the type checker, forcing you to handle all possible states.</p>
</div>
<div class="postgresql-bridge">
    <h4>Source Reference</h4>
    <p><strong>Theory</strong>: <code>typescript-handbook-v4.1-reference.pdf</code>, Pages 69-74 (Discriminating Unions, Union Exhaustiveness checking). This pattern synthesizes all concepts from the chunk.</p>
</div>

</div>
</body>
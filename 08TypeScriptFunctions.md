<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lecture: TypeScript Functions - The Core of Abstraction</title>
    <link rel="stylesheet" href="styles/lecture.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code&family=Lato:wght@400;700&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>

<div class="toc-popup-container">
    <input type="checkbox" id="toc-toggle" class="toc-toggle-checkbox">
    <label for="toc-toggle" class="toc-toggle-label">
        <span>Contents</span>
        <span class="toc-icon-open"></span>
    </label>
    <div class="toc-content">
        <h4>Lecture Navigation</h4>
        <ul>
            <li><a href="#part1">Part 1: Anatomy of a Typed Function</a>
                <ul>
                    <li><a href="#section1-1">1.1: The Function as a Code Contract</a></li>
                </ul>
            </li>
            <li><a href="#part2">Part 2: Handling Parameter Variability</a>
                <ul>
                    <li><a href="#section2-1">2.1: Optional Parameters</a></li>
                    <li><a href="#section2-2">2.2: Default Parameters</a></li>
                    <li><a href="#section2-3">2.3: Rest Parameters</a></li>
                </ul>
            </li>
            <li><a href="#part3">Part 3: Advanced Function Patterns</a>
                <ul>
                    <li><a href="#section3-1">3.1: Arrow Functions</a></li>
                    <li><a href="#section3-2">3.2: Higher-Order Functions</a></li>
                </ul>
            </li>
            <li><a href="#part4">Part 4: Function Overloading</a></li>
        </ul>
    </div>
</div>

<div class="container">

<h1 id="top">TypeScript Functions: The Core of Abstraction</h1>

<h2 id="part1">Part 1: The Anatomy of a Typed Function</h2>

<h3 id="section1-1">1.1 Core Concepts: The Function as a Code Contract</h3>

<p>
    In TypeScript, a function signature is not a suggestion; it is a <strong>code contract</strong>. It’s an explicit, unbreakable pact between the function and its caller, enforced by the compiler. This is the bedrock of predictable, scalable software.
</p>

<ul>
    <li>
        <strong>Typed Parameters</strong>: Each parameter is a named entry in the contract, defined with a strict type (e.g., <code>id: number</code>).
        <div class="oracle-specific">
            <strong>Grounded Example </strong>: This creates a <strong>predictable function</strong>.
        </div>
        <p>This is your primary defense against the chaos of unexpected data types. It transforms an entire category of runtime errors into compile-time impossibilities.</p>
    </li>
    <li>
        <strong>Return Type</strong>: The function promises to deliver a value of a specific type (e.g., <code>): User | undefined</code>). This is the function's non-negotiable deliverable. If it returns nothing, it promises <code>void</code>—a guarantee of emptiness.
        <div class="postgresql-bridge">
            <strong>Paradoxical Example (Inversion)</strong>: A function signature is <strong>freedom defined</strong>. It frees you from ever having to second-guess what a piece of code does or returns, giving you the liberty to build upon its guarantees.
        </div>
    </li>
</ul>

<div class="caution">
    <strong>Software Engineering Principle — Type Safety & Clarity</strong>: A well-typed function signature is the ultimate form of self-documenting code. It tells a clear, unambiguous story of its purpose and usage.
</div>

<h4>Example: The Database Gatekeeper</h4>
<p>This function acts as a gatekeeper to a user database. Its contract is simple: give it a <code>number</code>, and it will return a <code>User</code> object or the explicit absence of one (`undefined`). Nothing else is possible.</p>

```typescript
// Artificial Data: A 'digital ledger' this function consults.
interface User {
  id: number;
  username: string;
}
const userDatabase: User[] = [
  { id: 101, username: 'nicolas.castelblanco' },
  { id: 102, username: 'alan.turing' },
];

// The Function Declaration: A 'code contract' in action.
function findUserById(id: number, users: User[]): User | undefined {
  return users.find(u => u.id === id);
}

// Structural Usage: Honoring the contract.
const user = findUserById(101, userDatabase); // 'user' is correctly inferred as 'User | undefined'.

// A failed negotiation. The compiler rejects this before it can ever become a runtime error.
// const invalidUser = findUserById('101', userDatabase);
```

<p><small><strong>Source Reference</strong>: The theory behind this contract-based approach is detailed in the TypeScript Handbook, specifically in the <a href="https://www.typescriptlang.org/docs/handbook/2/functions.html">Functions</a> section (pages 43-45 in the PDF).</small></p>

<h2 id="part2">Part 2: Handling Parameter Variability—The Art of Flexibility</h2>

<h3 id="section2-1">2.1 Optional Parameters: The Present Absence</h3>
<p>
    A parameter marked with <code>?</code> is a <strong>present absence</strong>. It exists in the function's type signature, but it may be absent from the actual call. Internally, TypeScript treats its type as a union with <code>undefined</code>—a potential ghost you must always account for.
</p>

<div class="comparison-grid">
    <div class="feature-name">Optional Parameter Properties</div>
    <div class="grid-header">Advantages</div>
    <div class="grid-header">Disadvantages & Risks</div>
    <div class="grid-cell">
        <ul>
            <li>Creates a clean, flexible API.</li>
            <li>Callers can omit arguments that are not essential, reducing verbosity.</li>
        </ul>
    </div>
    <div class="grid-cell">
        <ul>
            <li><strong>Clarifying Risks </strong>: This creates a <strong>responsibility contract</strong>. The function's internal logic *must* handle the <code>undefined</code> case to prevent runtime failure.</li>
            <li>Optional parameters must appear after all required parameters.</li>
        </ul>
    </div>
</div>

<h4>Example: The Contextual Logger</h4>
<p>A logging function where contextual details are helpful for debugging but not strictly required for the function to operate.</p>

```typescript
type LogLevel = 'INFO' | 'WARN' | 'ERROR'; // Using Literal Types from Chunk 7

// The function signature accommodates a 'present absence'.
function logEvent(message: string, level: LogLevel, details?: object): void {
  const timestamp = new Date().toISOString();
  console.log(`[${timestamp}] [${level}] ${message}`);
  // Explicitly checking for the ghost of the parameter.
  if (details) {
    console.log('  Details:', JSON.stringify(details, null, 2));
  }
}

logEvent('User session started', 'INFO'); // 'details' is absent.
logEvent('Data validation failed', 'ERROR', { input: 'user@domain.com' }); // 'details' is present.
```
<p><small><strong>Source Reference</strong>: Explained under <a href="https://www.typescriptlang.org/docs/handbook/2/functions.html#optional-parameters">Optional Parameters</a> in the handbook (Page 47).</small></p>


<h3 id="section2-2">2.2 Default Parameters: The Safety Net</h3>
<p>
    Using the <code>=</code> syntax provides a parameter with a <strong>safety net</strong> value. If the caller provides nothing for that parameter, the default is automatically used, ensuring the function always has a concrete, predictable value to work with.
</p>
<div class="oracle-specific">
    <strong>Paradoxical Example </strong>: This is a <strong>choice invisible</strong>. If you don't make a choice, a sensible one is made for you, simplifying the call while ensuring robust behavior.
</div>
<p class="rhyme">
    When a value’s not set, there’s no need to fret,<br>
    A default parameter’s your safety net.
</p>

<h4>Example: The Configuration Factory</h4>
<p>This function configures a network request, defaulting to the most common settings (<code>GET</code> method, 5-second timeout).</p>

```typescript
interface APIRequest {
  endpoint: string;
  method: 'GET' | 'POST';
  timeout: number;
}

// Function with 'safety net' values.
function createAPIRequest(endpoint: string, method: 'GET' | 'POST' = 'GET', timeout: number = 5000): APIRequest {
  return { endpoint, method, timeout };
}

const getRequest = createAPIRequest('/users');
// Result: { endpoint: '/users', method: 'GET', timeout: 5000 }
```
<p><small><strong>Source Reference</strong>: Covered in <a href="https://www.typescriptlang.org/docs/handbook/2/functions.html#default-parameters">Default Parameters</a> in the handbook (Page 48).</small></p>


<h3 id="section2-3">2.3 Rest Parameters: The Gathering Net</h3>
<p>
    The <code>...</code> syntax on the final parameter of a function transforms it into a <strong>gathering net</strong>. It catches all remaining arguments passed by the caller and bundles them neatly into an array.
</p>
<div class="postgresql-bridge">
    <strong>Paradoxical Example </strong>: It represents a <strong>finite infinity</strong> of arguments—a single parameter that can hold a boundless number of values, giving your function immense flexibility.
</div>

<h4>Example: The Universal Aggregator</h4>
<p>A function to sum a variable number of values, showcasing the power of the gathering net.</p>

```typescript
// The 'gathering net' in action.
function sum(...values: number[]): number {
  return values.reduce((total, current) => total + current, 0);
}

const total = sum(10, 20, 30, 40, 50); // total is 150
```
<p><small><strong>Source Reference</strong>: Detailed under <a href="https://www.typescriptlang.org/docs/handbook/2/functions.html#rest-parameters-and-arguments">Rest Parameters</a> (Page 49).</small></p>


<h2 id="part3">Part 3: Advanced Function Patterns—The Tools of Abstraction</h2>

<h3 id="section3-1">3.1 Arrow Functions: The Lexical Anchor</h3>
<p>
    Arrow functions offer a concise syntax for creating functions, but their most powerful feature is acting as a <strong>lexical anchor</strong> for the <code>this</code> keyword.
</p>
<div class="oracle-specific">
    <strong>Paradoxical Example </strong>: The <strong>binding arrow</strong> that never misses its contextual target. It solves one of JavaScript’s oldest problems by refusing to have its own <code>this</code> context, instead inheriting it from its parent scope. This makes it invaluable for callbacks in object-oriented code.
</div>

<h4>Example: Preserving Context in Asynchronous Code</h4>

```typescript
class DataFetcher {
  private dataId: string = 'data-123';

  fetch() {
    console.log(`Initiating fetch for ${this.dataId}`);
    
    // Without an arrow function, 'this' inside setTimeout would be lost.
    // The arrow function anchors 'this' to the DataFetcher instance.
    setTimeout(() => {
      console.log(`Completed fetch for ${this.dataId}`);
    }, 1000);
  }
}

const fetcher = new DataFetcher();
fetcher.fetch();
```
<p><small><strong>Source Reference</strong>: The critical role of arrow functions with <code>this</code> is explained on pages 51-52 of the handbook PDF.</small></p>


<h3 id="section3-2">3.2 Higher-Order Functions: The Thought Architects</h3>
<p>
    Higher-order functions are the <strong>thought architects</strong> of an application. By accepting functions as arguments or returning them as results, they allow you to operate not just on data, but on logic itself. This is the heart of functional programming.
</p>
<div class="postgresql-bridge">
    <strong>Paradoxical Example (Multi-Word)</strong>: This is a function that holds <strong>a conversation with other functions</strong>, orchestrating them to build complex, reusable patterns.
</div>
<p class="rhyme">
    A function that takes or returns a routine,<br>
    Builds a cleaner, more powerful coding machine.
</p>

<h4>Example: The Logic Wrapper</h4>
<p>A generic <code>withLogging</code> function that wraps another function to add logging before and after its execution, without modifying the original function.</p>

```typescript
// Type alias for any generic function signature
type AnyFunction&lt;T extends any[], R&gt; = (...args: T) => R;

// The higher-order function: our 'thought architect'
function withLogging&lt;T extends any[], R&gt;(fn: AnyFunction&lt;T, R&gt;): AnyFunction&lt;T, R&gt; {
  return (...args: T): R => {
    console.log(`Calling function '${fn.name}' with arguments:`, args);
    const result = fn(...args);
    console.log(`Function '${fn.name}' returned:`, result);
    return result;
  };
}

function add(a: number, b: number): number {
  return a + b;
}

// The original 'add' function is now enhanced with logging.
const loggedAdd = withLogging(add);
loggedAdd(5, 10);
```
<p><small><strong>Source Reference</strong>: Based on concepts from <a href="https://www.typescriptlang.org/docs/handbook/2/functions.html#function-type-expressions">Function Type Expressions</a> (Page 45).</small></p>


<h2 id="part4">Part 4: Function Overloading—The Shape-Shifter</h2>
<p>
    Function overloading allows a single function name to become a <strong>shape-shifter</strong>, presenting multiple, distinct, and type-safe interfaces based on the arguments it receives.
</p>
<div class="caution">
    <strong>Comedy (Punctuation Joke)</strong>: Why did the TypeScript function go to the costume party? Because with overloading, it could be a <code>string-reverser</code>, a <code>number-doubler</code>, or an <code>array-flattener</code>—it had a different signature for every occasion!
</div>
<div class="oracle-specific">
    <strong>Paradoxical Example </strong>: It is a <strong>singular plurality</strong>—one function with many faces. The compiler knows which face to expect based on your call, providing unparalleled type safety for flexible APIs.
</div>

<h4>Example: The Multi-Purpose Identifier Factory</h4>
<p>A function <code>createIdentifier</code> that generates a simple string ID from a number, or a more complex composite ID from two strings.</p>

```typescript
// Overload Signatures: The 'multiple faces' of the function
function createIdentifier(seed: number): string;
function createIdentifier(prefix: string, suffix: string): string;

// Implementation Signature: The single, hidden 'heart'
function createIdentifier(arg1: number | string, arg2?: string): string {
  if (typeof arg1 === 'number') {
    // Logic for the first overload
    return `ID-${arg1.toString().padStart(8, '0')}`;
  } else {
    // Logic for the second overload
    return `${arg1.toUpperCase()}-${arg2?.toUpperCase()}`;
  }
}

// The compiler provides precise type checking for each call.
const numericId = createIdentifier(12345); // Returns: "ID-00012345"
const compositeId = createIdentifier("user", "profile"); // Returns: "USER-PROFILE"

// const invalidCall = createIdentifier("user"); // Compile-time error: No overload matches.
```
<p><small><strong>Source Reference</strong>: This pattern is explicitly detailed in the <a href="https://www.typescriptlang.org/docs/handbook/2/functions.html#function-overloads">Function Overloads</a> section of the handbook (Pages 56-57).</small></p>

</div>
</body>
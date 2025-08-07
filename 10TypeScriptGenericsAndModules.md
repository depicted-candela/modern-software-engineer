<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lecture: TypeScript Generics and Modules</title>
    <link rel="stylesheet" href="styles/lecture.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code&family=Lato:wght@400;700&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>

<body>
<div class="toc-popup-container">
    <input type="checkbox" id="toc-toggle" class="toc-toggle-checkbox">
    <label for="toc-toggle" class="toc-toggle-label">
        <span>Table of Contents</span>
        <span class="toc-icon-open"></span>
    </label>
    <div class="toc-content">
        <h4>Lecture Navigation</h4>
        <ul>
            <li><a href="#part1">Part 1: Foundational Generics</a>
                <ul>
                    <li><a href="#concept1">Concept 1: Generic Functions</a></li>
                </ul>
            </li>
            <li><a href="#part2">Part 2: Generics in Data Structures</a>
                <ul>
                    <li><a href="#concept2">Concept 2: Generic Classes & Interfaces</a></li>
                </ul>
            </li>
            <li><a href="#part3">Part 3: Advanced Generics</a>
                <ul>
                    <li><a href="#concept3">Concept 3: Generic Constraints</a></li>
                </ul>
            </li>
            <li><a href="#part4">Part 4: Code Organization</a>
                <ul>
                    <li><a href="#concept4">Concept 4: ES Modules</a></li>
                </ul>
            </li>
            <li><a href="#part5">Part 5: Layered Combination</a>
                <ul>
                    <li><a href="#pattern5">Pattern: Event Dispatcher</a></li>
                </ul>
            </li>
        </ul>
    </div>
</div>

<div class="container">
<h1 id="part1">Part 1: The Foundation of Generics - Creating Reusable Components</h1>
<h2 id="concept1">Concept 1: Generic Functions</h2>

<div class="caution">
    <h4>Pillar I: Defining Core Concepts</h4>
    <p><strong>Pedagogical Goal:</strong> Grab Attention at the Start</p>
</div>
<p class="rhyme">Why did the generic function break up with the <code>any</code> type? Because it felt <code>any</code> was too non-committal and had no standards!</p>
<p>A generic function is a <strong>flexible formation</strong>, built for a variety of type applications. Instead of being locked to one type, it uses a <strong>Polymorphic Key</strong>—a type parameter, usually <code>&lt;T&gt;</code>—that acts as a placeholder. This key creates a <strong>Type Conduit</strong>, a secure link between what goes in and what comes out.</p>
<h3>Structural Usage and Properties</h3>
<ul>
    <li><strong>Syntax</strong>: <code>function functionName&lt;T&gt;(arg: T): T { ... }</code></li>
    <li><strong>Type Parameter (<code>&lt;T&gt;</code>)</strong>: A placeholder that captures a type at the moment of creation.</li>
    <li><strong>Type Usage (<code>arg: T</code>, <code>: T</code>)</strong>: This forges a <strong>type-safe chain</strong>, ensuring the output type is identical to the input type.</li>
    <li><strong>Advantage</strong>: <strong>Reusability</strong>. You architect a single, robust function that operates on an infinity of types. This is the heart of the <strong>DRY (Don't Repeat Yourself)</strong> principle—a core tenet of efficient engineering.</li>
    <li><strong>Disadvantage</strong>: Can introduce a layer of abstraction that might be overkill for simple, ephemeral functions.</li>
</ul>
<h3>Example 1: The Identity Conduit</h3>
<p>This function is the purest demonstration of a type's journey. It accepts a value and returns it, unchanged. Its true purpose is to make the flow of the type itself visible and tangible.</p>

```typescript
// A generic function acting as a "Type Conduit"
function identity<T>(arg: T): T {
    // The type T flows from argument to return value.
    return arg;
}

// Usage with an explicit type parameter (the key is provided)
let numericOutput: number = identity<number>(42);

// Usage with type inference (the key's shape is deduced from the lock)
let stringOutput: string = identity("hello world");

console.log(numericOutput); // Output: 42
console.log(stringOutput);  // Output: "hello world"
```
<div class="postgresql-bridge">
    <p><strong>Relationship to Prior Concepts</strong>: This elevates the <strong>Functions (Chunk 8)</strong> we've seen from static blueprints into dynamic, adaptable templates, escaping the rigid world of <code>any</code> or the repetitive labor of function overloading for every type.</p>
</div>
<div class="oracle-specific">
    <h4>Theoretical Foundation</h4>
    <ul>
        <li><strong>TypeScript Handbook</strong>: Introduces this exact pattern as the "Hello World of Generics." It explains that <code>T</code> allows the function to "capture the type the user provides... so that we can use that information later." This act of capturing and reusing is the essence of generic programming.<sup class="footnote-ref"><a href="#fn1">[1]</a></sup></li>
        <li><strong>C++ Templates</strong>: The soul of TypeScript generics comes from C++ templates. It's the same powerful idea: writing code that operates on types yet to be specified.<sup class="footnote-ref"><a href="#fn2">[2]</a></sup></li>
    </ul>
</div>

<h1 id="part2">Part 2: Applying Generics to Data Structures</h1>
<h2 id="concept2">Concept 2: Generic Classes and Interfaces</h2>
<div class="caution">
    <h4>Pillar I: Defining Core Concepts</h4>
    <p><strong>Pedagogical Goal:</strong> Reset Focus / "Pattern Interrupt"</p>
</div>
<p>A generic class or interface is a <strong>Type-Gated Silo</strong>: a structure designed to hold a specific kind of data. You can build a silo for grain (<code>Stack&lt;number&gt;</code>) or a silo for water (<code>Stack&lt;string&gt;</code>), but the gatekeeper, <code>&lt;T&gt;</code>, ensures you can't pour water into the grain silo.</p>
<h3>Structural Usage and Properties</h3>
<ul>
    <li><strong>Syntax (Class)</strong>: <code>class Stack&lt;T&gt; { ... }</code></li>
    <li><strong>Syntax (Interface)</strong>: <code>interface IStack&lt;T&gt; { ... }</code></li>
    <li><strong>Type Usage</strong>: The parameter <code>T</code> is woven throughout the class blueprint, typing its internal storage, its method parameters, and its return values.</li>
    <li><strong>Advantage</strong>: <strong>Structural Integrity</strong>. It guarantees that every operation within an instance of the class is type-consistent. A <code>Stack&lt;number&gt;</code> is a world of numbers; strings are not permitted entry. This compile-time guarantee is a cornerstone of <strong>Reliability</strong>.</li>
    <li><strong>Utility Context</strong>: Absolutely essential for creating fundamental, reusable data structures—stacks, queues, trees—the very bones of complex algorithms.</li>
</ul>
<h3>Example 2: A Generic Stack</h3>
<p>A stack is a Last-In, First-Out (LIFO) structure. When it's generic, it becomes a universal tool for managing ordered data of any kind.</p>
<p class="rhyme">Popping from an empty stack is like trying to withdraw from your bank account on a Friday. You get <code>undefined</code> and a vague sense of disappointment.</p>

```typescript
// The generic contract: an abstract idea of a Stack
interface IStack<T> {
    push(item: T): void;
    pop(): T | undefined;
    peek(): T | undefined;
    size(): number;
}

// The generic implementation: a concrete blueprint for any Stack
class Stack<T> implements IStack<T> {
    private storage: T[] = []; // Internal state is typed by T

    push(item: T): void {
        this.storage.push(item);
    }

    pop(): T | undefined {
        return this.storage.pop();
    }

    peek(): T | undefined {
        return this.storage[this.storage.length - 1];
    }

    size(): number {
        return this.storage.length;
    }
}

// Instantiation: creating a specific silo for user objects
const userStack = new Stack<{ id: number; name: string }>();
userStack.push({ id: 1, name: "Alice" });
userStack.push({ id: 2, name: "Bob" });

const poppedUser = userStack.pop();
console.log(poppedUser); // Output: { id: 2, name: 'Bob' }
```
<p class="rhyme">With <code>Stack&lt;number&gt;</code> so keen, no string will ever intervene.</p>
<div class="postgresql-bridge">
    <p><strong>Relationship to Prior Concepts</strong>: This is a direct evolution of <strong>Classes and Interfaces (Chunks 7 & 9)</strong>. We are no longer defining a single, static shape but a template from which infinite, type-safe variations can be created.</p>
</div>
<div class="oracle-specific">
    <h4>Theoretical Foundation</h4>
    <ul>
        <li><strong>TypeScript Handbook</strong>: The guide explains that by placing the type parameter on the class itself, "we make sure all of the properties of the class are working with the same type," thereby ensuring internal consistency.<sup class="footnote-ref"><a href="#fn3">[3]</a></sup></li>
    </ul>
</div>

<h1 id="part3">Part 3: Advanced Generics - Constraining Type Parameters</h1>
<h2 id="concept3">Concept 3: Generic Constraints</h2>
<div class="caution">
    <h4>Pillar III: Clarifying Disadvantages, Risks & Limitations</h4>
    <p><strong>Pedagogical Goal:</strong> Illustrate a Technical Concept</p>
</div>
<p class="rhyme">Using a generic without a constraint is like hiring a contractor without checking their license. They might be able to build a doghouse, but don't be surprised when they try to use a hammer on your database.</p>
<p>Constraints are a <strong>Property Leash</strong>. They allow a generic type <code>T</code> to be flexible, but only within the safe, predictable boundaries of another type. We use the <code>extends</code> keyword to attach this leash, often in combination with the <code>keyof</code> operator, which acts like a blueprint of an object's available properties.</p>
<h3>Structural Usage and Properties</h3>
<ul>
    <li><strong>Syntax</strong>: <code>&lt;T extends SomeType&gt;</code> or <code>&lt;K extends keyof T&gt;</code></li>
    <li><strong><code>extends keyof T</code></strong>: This pattern is a cornerstone of advanced TypeScript. It constrains a type parameter <code>K</code> to be one of the keys of another type parameter <code>T</code>.</li>
    <li><strong>Indexed Access Type (<code>T[K]</code>)</strong>: An <strong>Indexed Reflection</strong>. It allows you to look up the type of a property on an object type. The combination <code>T[K]</code> gives you the exact type of the property <code>K</code> on <code>T</code>.</li>
    <li><strong>Advantage</strong>: <strong>Intelligent Type Safety</strong>. It allows you to write functions that are both generic and aware of the structure of the types they are operating on. This moves beyond simple reusability to creating genuinely smart, self-validating tools, which is critical for <strong>Reliability</strong>.</li>
</ul>
<h3>Example 3: The Type-Safe Property Plucker</h3>
<p>This function can safely access a property from any object because the compiler, thanks to the constraint, guarantees the key exists before the code is ever run.</p>

```typescript
// The 'Property Leash' in action: K must be a key of T.
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

interface Product {
    id: string;
    price: number;
    inStock: boolean;
}

const product: Product = { id: "abc-123", price: 99.9, inStock: true };

// Valid: TypeScript understands that "price" is a key of Product
// and infers the return type as number.
const price: number = getProperty(product, "price");
console.log(price); // Output: 99.9

// Invalid: The compiler stops this at the source.
// This is not a runtime error; it is a compile-time impossibility.
// const invalidProp = getProperty(product, "description");
// Error: Argument of type '"description"' is not assignable to parameter of type '"id" | "price" | "inStock"'.
```
<div class="postgresql-bridge">
    <p><strong>Relationship to Prior Concepts</strong>: This is a powerful fusion of <strong>Generics</strong>, <strong>Interfaces (Chunk 7)</strong>, and TypeScript's structural type operators (<code>keyof</code>). It demonstrates a layered understanding where the shape of one type dynamically constrains another.</p>
</div>
<div class="oracle-specific">
    <h4>Theoretical Foundation</h4>
    <ul>
        <li><strong>TypeScript Handbook</strong>: The "Generic Constraints" and "Using Type Parameters in Generic Constraints" sections explicitly detail this pattern. It's presented as the solution for when "you want to write a generic function that works on a set of types where you have some knowledge about what capabilities that set of types will have."<sup class="footnote-ref"><a href="#fn4">[4]</a></sup></li>
    </ul>
</div>

<h1 id="part4">Part 4: Code Organization with Modules</h1>
<h2 id="concept4">Concept 4: ES Modules (<code>import</code>/<code>export</code>)</h2>
<div class="caution">
    <h4>Pillar I: Defining Core Concepts</h4>
    <p><strong>Pedagogical Goal:</strong> Reinforce a concept with metaphor</p>
</div>
<p>Modules are <strong>Code Archipelagos</strong>. Each file is an island, with its own private ecosystem of variables, functions, and classes. Nothing can leave an island unless it is explicitly sent across a bridge built by the <code>export</code> keyword. To use resources from another island, you must build a port with the <code>import</code> keyword.</p>
<h3>Structural Usage and Properties</h3>
<ul>
    <li><strong><code>export</code></strong>: Builds the bridges.
        <ul>
            <li><strong>Named Export</strong>: <code>export const ...</code> - Builds multiple, named bridges.</li>
            <li><strong>Default Export</strong>: <code>export default ...</code> - Builds one main, unnamed highway off the island. Best for when a module has a single primary purpose.</li>
        </ul>
    </li>
    <li><strong><code>import</code></strong>: Builds the ports to receive goods.
        <ul>
            <li><strong>Named Import</strong>: <code>import { thing } from './island';</code> - Docks at a specific, named bridge.</li>
            <li><strong>Default Import</strong>: <code>import MainThing from './island';</code> - Connects to the main highway.</li>
        </ul>
    </li>
    <li><strong>Barrel Exports (<code>index.ts</code>)</strong>: A <strong>Central Trade Hub</strong>. A special island that does nothing but build bridges to all the other islands in its archipelago, making it a single point of contact for external trade.</li>
</ul>
<h3>Example 4: A Utility Archipelago</h3>

```typescript
// src/utils/string-utils.ts (Island of String Manipulation)
export function toUpperCase(str: string): string {
    return str.toUpperCase();
}
export function toLowerCase(str: string): string {
    return str.toLowerCase();
}

// src/utils/math-utils.ts (Island of Mathematics)
export const PI = 3.14159;
export default function add(a: number, b: number): number { // The main highway
    return a + b;
}

// src/utils/index.ts (The Central Trade Hub)
export * from './string-utils'; // Re-exporting all named bridges
export { default as add } from './math-utils'; // Re-exporting the highway with a name
export { PI } from './math-utils';

// src/main.ts (The Mainland Consumer)
import { toUpperCase, add, PI } from './utils'; // Importing from the hub

console.log(toUpperCase("hello")); // Output: HELLO
console.log(add(PI, 1));          // Output: 4.14159
```
<p class="rhyme">With an <code>export</code>, your code goes out the door;<br>with an <code>import</code>, you can use it and more.</p>
<div class="postgresql-bridge">
    <p><strong>Relationship to Prior Concepts</strong>: Modules provide the architectural foundation for everything. They are the containers for our <strong>Interfaces</strong>, <strong>Classes</strong>, <strong>Functions</strong>, and <strong>Generics</strong>, enforcing boundaries and creating a structure that is essential for <strong>Scalability</strong> and <strong>Modifiability</strong>.</p>
</div>
<div class="oracle-specific">
    <h4>Theoretical Foundation</h4>
    <ul>
        <li><strong>TypeScript Handbook</strong>: The "Modules" chapter is the definitive guide, explaining how TypeScript implements the ES Module standard for organizing code and managing dependencies.<sup class="footnote-ref"><a href="#fn5">[5]</a></sup></li>
    </ul>
</div>

<h1 id="part5">Part 5: Layered Combination - The Type-Safe Event Dispatcher</h1>
<h2 id="pattern5">Pattern: The Hardcore Combination</h2>
<div class="caution">
    <h4>Immersion Joke: A Fictional Case Study</h4>
    <p><strong>Pedagogical Goal:</strong> Create a Memorable Capstone Example</p>
</div>
<p>Today, we are lead architects for <strong>"ChronoGuard Inc.,"</strong> a startup providing temporal insurance. Our task is to build the central messaging system for their temporal agents. This system must be a <strong>reactively autonomous system</strong>, a <strong>Central Nervous System</strong> for the entire operation. It must handle critical events like <code>'timeline:branched'</code>, <code>'paradox:detected'</code>, and <code>'causality:violated'</code>.</p>
<p>The payloads for these events must be <em>perfectly</em> typed. A mistake is not just a bug; dispatching a <code>paradox</code> payload to a <code>timeline</code> listener could accidentally un-invent toast. This is where we combine all our TypeScript knowledge to create a system where such mistakes are a <strong>compile-time impossibility</strong>.</p>
<h3>The Pattern: A Type-Safe, Modular Event Dispatcher</h3>
<ul>
    <li><strong>Utility Context</strong>: Used in complex applications to allow different parts of the system (modules) to communicate without being directly coupled (<strong>Decoupling</strong>).</li>
    <li><strong>Structural Usage</strong>:
        <ol>
            <li>An <strong>interface</strong> (<code>EventMap</code>) defines the "contract" for all possible events and their payload shapes. This acts as a <strong>Single Source of Truth</strong>.</li>
            <li>A <strong>generic class</strong> (<code>EventDispatcher&lt;T&gt;</code>) provides the core publish/subscribe logic.</li>
            <li><strong>Generic constraints</strong> (<code>K extends keyof T</code>) and <strong>indexed access types</strong> (<code>T[K]</code>) are used in the <code>on</code> and <code>dispatch</code> methods to create a <strong>symbiotic dance</strong> between event names and their payloads, ensuring <strong>compile-time type safety</strong>.</li>
            <li><strong>Modules</strong> are used to separate the dispatcher logic, type definitions, and the services that use them, creating a <strong>scalable</strong> and <strong>maintainable</strong> architecture.</li>
        </ol>
    </li>
</ul>
<h3>Example 5: The ChronoGuard Event Dispatcher</h3>

```typescript
// 1. src/lib/chrono-event-types.ts (The Book of Truth)
// Technical Superstrate: A perfectly valid interface.
// Humorous Substrate: The content is absurd.
export interface ChronoEventMap {
  'timeline:branched': { newTimelineId: string; divergencePoint: Date };
  'paradox:detected': { realityInstabilityIndex: number; originatingTimeline: string };
  'causality:violated': { subject: string; action: string; correctionStrategy: 'prune' | 'merge' };
}

// 2. src/lib/dispatcher.ts (The Central Nervous System)
type Callback<T> = (payload: T) => void;

export class EventDispatcher<T extends object> {
    private listeners: { [K in keyof T]?: Callback<T[K]>[] } = {};

    on<K extends keyof T>(eventName: K, callback: Callback<T[K]>): void {
        (this.listeners[eventName] = this.listeners[eventName] || []).push(callback);
    }

    dispatch<K extends keyof T>(eventName: K, payload: T[K]): void {
        this.listeners[eventName]?.forEach(cb => cb(payload));
        // Semantic Catalyst: A subtle hint at the absurdity in comments.
        // IMPORTANT: Failure to provide a 'correctionStrategy' for causality violations
        // defaults to timeline pruning. Handle with care.
    }
}

// 3. src/services/temporal-agent.ts
import { EventDispatcher } from '../lib/dispatcher';
import { ChronoEventMap } from '../lib/chrono-event-types';

export function reportBranch(dispatcher: EventDispatcher<ChronoEventMap>) {
    const newId = `timeline-${Math.random().toString(36).substr(2, 9)}`;
    console.log(`Agent 7: Reporting new timeline branch: ${newId}`);
    // Type-safe dispatch: The payload MUST match ChronoEventMap['timeline:branched']
    dispatcher.dispatch('timeline:branched', { newTimelineId: newId, divergencePoint: new Date() });
}

// 4. src/index.ts (Mission Control)
import { EventDispatcher } from './lib/dispatcher';
import { ChronoEventMap } from './lib/chrono-event-types';
import { reportBranch } from './services/temporal-agent';

const dispatcher = new EventDispatcher<ChronoEventMap>();

// Type-safe subscription from the Paradox Resolution Department
dispatcher.on('paradox:detected', (payload) => {
    console.log(`[ALERT] Paradox detected! Instability Index: ${payload.realityInstabilityIndex}`);
});

dispatcher.on('timeline:branched', (payload) => {
    console.log(`[LOG] Timeline branch detected. ID: ${payload.newTimelineId} at ${payload.divergencePoint}`);
});

reportBranch(dispatcher);

// --- COMPILE-TIME ERROR EXAMPLES ---
// 1. Wrong payload shape
// dispatcher.dispatch('user:created', { id: 123, name: "Eve" }); // Error: 'id' does not exist, 'userId' is missing.

// 2. Wrong callback parameter type
// dispatcher.on('user:created', (payload: { id: number }) => {}); // Error: Type '{ id: number; }' is not assignable to type '{ userId: number; name: string; }'.
```
<p>This final example demonstrates the pinnacle of TypeScript's type system: leveraging layered concepts to build systems that are not just functional, but are also inherently robust, reliable, and easy to reason about—a <strong>creativity engine</strong> for high-stakes software development.</p>

<div class="footnotes">
<ol>
<li id="fn1"><p><strong>TypeScript Handbook</strong>, Pages 109-110, "Hello World of Generics". <a href="#part1">↩</a></p></li>
<li id="fn2"><p><strong>The C++ Programming Language</strong>, 4th Ed., Bjarne Stroustrup, Page 684, Section 23.5 "Function Templates". <a href="#part1">↩</a></p></li>
<li id="fn3"><p><strong>TypeScript Handbook</strong>, Page 115, "Generic Classes" and Page 114, "Generic Types". <a href="#part2">↩</a></p></li>
<li id="fn4"><p><strong>TypeScript Handbook</strong>, Page 117, "Generic Constraints" and Page 119, "Using Type Parameters in Generic Constraints". <a href="#part3">↩</a></p></li>
<li id="fn5"><p><strong>TypeScript Handbook Reference</strong>, Pages 110-123, "Modules". <a href="#part4">↩</a></p></li>
</ol>
</div>
</div>
</body>
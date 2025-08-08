<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lecture: TypeScript Classes - A Comprehensive Guide</title>
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
        <ul>
            <li>
                <a href="#part1">Part 1: The Anatomy of a Class</a>
                <ul>
                    <li><a href="#part1-1">1.1: Core Components</a></li>
                </ul>
            </li>
            <li>
                <a href="#part2">Part 2: Encapsulation</a>
            </li>
            <li>
                <a href="#part3">Part 3: Inheritance</a>
            </li>
            <li>
                <a href="#part4">Part 4: Abstract Classes</a>
            </li>
        </ul>
    </div>
</div>

<div class="container">

<h1>TypeScript Classes: From Blueprint to Living Object</h1>

<h2 id="part1">Part 1: The Anatomy of a Class — The Structural Blueprint</h2>

<p>
A class is a blueprint, a <strong>thought architecture</strong>, that combines data (properties) and behavior (methods). This builds upon <strong>Chunk 8 (Functions)</strong>, as constructors and methods are specialized functions scoped to the class. The fundamental pattern is object instantiation: define a blueprint once (<code>class</code>) and create multiple, independent objects (<code>instances</code>) from it using the <code>new</code> keyword.
</p>

<h3 id="part1-1">1.1: Core Components</h3>
<p class="rhyme">
A quick question to start: What do you call an object-oriented programmer who just inherited a fortune? A subclass. Okay, now let's talk about the blueprints for that inheritance.
</p>
<ul>
    <li><strong>Properties</strong>: Variables that hold the state of an instance.</li>
    <li><strong>Constructor</strong>: A special method for creating and initializing an instance. It's the <strong>entry point</strong> for an object's life.</li>
    <li><strong>Methods</strong>: Functions that define the behavior.</li>
</ul>

<h4>Structural Usage & Example</h4>
<p>Let's model a <code>SystemUser</code>. The state is the user's identity; the behavior is how that identity acts within the system.</p>

```typescript
// --- Artificial Data ---
const adminUserData = { id: 101, role: "ADMIN" };
const guestUserData = { id: 205, role: "GUEST" };

// --- Class Definition: The Structural Blueprint ---
class SystemUser {
  // Properties: The object's internal state
  id: number;
  role: string;

  // Constructor: Initializes the state
  constructor(id: number, role: string) {
    this.id = id;
    this.role = role;
  }

  // Method: Defines the object's public behavior
  isAdmin(): boolean {
    return this.role === "ADMIN";
  }
}

// --- Instantiation: Creating concrete objects from the blueprint ---
const adminUser = new SystemUser(adminUserData.id, adminUserData.role);
const guestUser = new SystemUser(guestUserData.id, guestUserData.role);

// The state is now a tangible object we can interact with
console.log(`User ${adminUser.id} is admin: ${adminUser.isAdmin()}`); 
console.log(`User ${guestUser.id} is admin: ${guestUser.isAdmin()}`);
```
<div class="postgresql-bridge">
    <p>
        <strong>Utility Context</strong>: A class is the perfect tool for creating a <strong>digital twin</strong> of a real-world concept, making complex systems manageable.
    </p>
    <p>
        <strong>Software Engineering Principle (Modifiability)</strong>: By bundling data and logic, a class becomes a self-contained unit. This makes changes predictable and contained, preventing the <strong>cascading update</strong> problem where one small change breaks everything.
    </p>
    <p><small><strong>Source Reference</strong>: <code>typescript-handbook-v4.1.pdf</code> (Pages 76-77) details this fundamental structure. The concept of a class as a <code>structural blueprint</code> is a <strong>Grounded Combination</strong> from <code>The Metaphorical Scaffolding Framework.pdf</code> (Pillar I).</small></p>
</div>


<h2 id="part2">Part 2: Encapsulation — The Public Promise and the Private Secret</h2>
<p>
The pattern of information hiding creates a stable public API—a <strong>well-defined contract</strong>—while the internal workings are a private implementation detail.
</p>
<ul>
    <li><strong><code>public</code></strong>: (Default) The member is accessible from anywhere. This is the class's public promise.</li>
    <li><strong><code>private</code></strong>: The member is only accessible from within the defining class. This is the object's <strong>secret diary</strong>; no one else gets to read or write in it.
        <ul>
            <li><strong>Advantage</strong>: Creates <code>bug-free?</code> code by preventing outside interference. It guarantees the object’s state is always valid.</li>
            <li><strong>Disadvantage</strong>: Creates a rigid boundary. It offers a form of <strong>golden handcuffs</strong>—security at the cost of flexibility, as subclasses cannot access these members.</li>
        </ul>
    </li>
    <li><strong><code>protected</code></strong>: The member is accessible within the class and its subclasses. This is a <strong>family recipe</strong>—passed down through generations (inheritance) but not shared with the outside world.</li>
</ul>

<h4>Structural Usage & Example</h4>
<p>A <code>DatabaseConnection</code> class. The connection string is a dangerous secret (<code>private</code>). The connection status is a detail subclasses (<code>protected</code>) might need. The methods to connect are the public API.</p>

```typescript
// --- Artificial Data ---
const sensitiveConfig = { connectionString: "user:pass@db.server:5432/prod_db" };

// --- Class Definition with Encapsulation ---
class DatabaseConnection {
  private connectionString: string;       // The secret diary
  protected status: string;               // The family recipe
  public readonly creationTime: Date;     // The public record

  constructor(connStr: string) {
    this.connectionString = connStr;
    this.status = "disconnected";
    this.creationTime = new Date();
  }

  public connect(): void { // The public promise
    this.status = "connecting";
    // Internal logic uses the private member safely
    console.log("Connection established.");
    this.status = "connected";
  }
}

const db = new DatabaseConnection(sensitiveConfig.connectionString);
db.connect();
// console.log(db.connectionString); // Error: A secret.
// console.log(db.status);           // Error: A family matter.
```
<div class="caution">
    <p>
        <strong>Software Engineering Principle (Reliability)</strong>: Encapsulation makes an object a <strong>fortress of logic</strong>. Its internal state is protected from the chaotic world outside, ensuring it can only change in predictable, controlled ways.
    </p>
    <p><small><strong>Source Reference</strong>: <code>typescript-handbook-v4.1.pdf</code> (Pages 80, 82-85) details these modifiers. The metaphors <code>secret diary</code>, <code>family recipe</code>, and <code>golden handcuffs</code> are applications of the principles in <code>The Metaphorical Scaffolding Framework.pdf</code> (Pillar I & III).</small></p>
</div>

<h2 id="part3">Part 3: Inheritance — A Timeline Convergence</h2>
<p>
An "is-a" relationship. A <code>Car</code> <em>is-a</em> <code>Vehicle</code>. This creates a hierarchy where specialized <strong>structural descendants</strong> inherit from a general ancestor. The <code>super()</code> call in a subclass constructor is mandatory if the superclass has a constructor, and must be the first statement.
</p>
<div class="rhyme">
Forgetting <code>super()</code> is a classic bug. The most dangerous phrase in programming is "this will be easy." It's like a C programmer saying, "I'm sure I freed all the memory." The humor comes from the almost certain catastrophic reality, which is exactly the kind of bug we need to watch for.
</div>

<h4>Structural Usage & Example</h4>
<p>Model different log types. A <code>BaseLog</code> provides common features. <code>SystemLog</code> and <code>UserActivityLog</code> are specialized versions.</p>

```typescript
// --- Artificial Data ---
const systemEvent = { timestamp: new Date(), message: "DB timeout", severity: "HIGH" };
const userEvent = { timestamp: new Date(), message: "User login", userId: 123 };

// --- Class Hierarchy ---
class BaseLog {
  constructor(public timestamp: Date, public message: string) {}

  public format(): string {
    return `[${this.timestamp.toISOString()}] - ${this.message}`;
  }
}

class SystemLog extends BaseLog {
  constructor(timestamp: Date, message: string, public severity: "HIGH") {
    super(timestamp, message); // The mandatory call to the ancestor
  }

  // Method Overriding: Giving the descendant its own voice
  public format(): string {
    const baseFormatted = super.format(); // We can still access the original voice
    return `[${this.severity}] ${baseFormatted}`;
  }
}
const sysLog = new SystemLog(systemEvent.timestamp, systemEvent.message, systemEvent.severity);
console.log(sysLog.format());
```
<div class="postgresql-bridge">
    <p><strong>Software Engineering Principle (Scalability)</strong>: Inheritance enables the Open/Closed Principle: the system is <em>open</em> for extension (add new log types) but <em>closed</em> for modification (no need to change <code>BaseLog</code>).</p>
    <p><small><strong>Source Reference</strong>: <code>typescript-handbook-v4.1.pdf</code> (Pages 78-79) covers <code>extends</code> and <code>super()</code>. The joke is an application of the "Illustrate a Technical Concept" pattern from <code>A Unified Hierarchical Model for Comedic Integration.pdf</code> (Table 1).</small></p>
</div>

<h2 id="part4">Part 4: Abstract Classes — The Tangible Ghost</h2>
<p>
An abstract class is a template for other classes. It is a <strong>tangible ghost</strong>—it has a defined shape and even some implemented logic, but it cannot be instantiated directly. It's a blueprint for a blueprint. Its abstract methods are a contract, a <strong>promise hollow</strong> until a concrete subclass provides an implementation.
</p>
<h4>Structural Usage & Example</h4>
<p>Define a <code>DataProcessor</code> that has a standard <code>process</code> method but requires subclasses to implement specific <code>read</code> and <code>write</code> methods.</p>

```typescript
// --- Artificial Data ---
const jsonData = `{"data": "sample"}`;

// --- Abstract Class: A partially implemented blueprint ---
abstract class DataProcessor {
  // A concrete method providing the "template" algorithm
  public process(data: string): void {
    const parsedData = this.read(data);
    this.write(parsedData);
  }

  // Abstract methods: The contract that subclasses must fulfill
  protected abstract read(data: string): any;
  protected abstract write(data: any): void;
}

// --- Concrete Implementation ---
class JsonProcessor extends DataProcessor {
  protected read(data: string): any {
    console.log("Reading JSON...");
    return JSON.parse(data);
  }
  protected write(data: any): void {
    console.log("Writing parsed JSON to storage...");
  }
}

const jsonProcessor = new JsonProcessor();
jsonProcessor.process(jsonData);
// const genericProcessor = new DataProcessor(); // Error: Cannot summon a ghost.
```
<div class="oracle-specific">
    <p>
        <strong>Software Engineering Principle (Modifiability)</strong>: The Template Method Pattern, implemented with an abstract class, allows you to define the skeleton of an algorithm in a base class and let subclasses override specific steps. This makes the overall algorithm's structure reusable and its <strong>workflow absolute</strong>.
    </p>
    <p><small><strong>Source Reference</strong>: <code>typescript-handbook-v4.1.pdf</code> (Pages 90-91) explains abstract classes. The metaphors <code>tangible ghost</code> and <code>promise hollow</code> are from <code>The Metaphorical Scaffolding Framework.pdf</code> (Pillar I & III).</small></p>
</div>
</div>
</body>
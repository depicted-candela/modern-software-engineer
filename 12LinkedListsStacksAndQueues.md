<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lecture: Linked Lists, Stacks, and Queues</title>
    <link rel="stylesheet" href="styles/lecture.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code&family=Lato:wght@400;700&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>

<div class="toc-popup-container">
    <input type="checkbox" id="toc-toggle" class="toc-toggle-checkbox">
    <label for="toc-toggle" class="toc-toggle-label">
        <span>Lecture Outline</span>
        <span class="toc-icon-open"></span>
    </label>
    <div class="toc-content">
        <h4>Table of Contents</h4>
        <ul>
            <li><a href="#section-1">1. ADTs vs. Data Structures</a></li>
            <li><a href="#section-2">2. Stacks: The LIFO Contract</a>
                <ul><li><a href="#section-2-1">Implementation: Array-Based</a></li></ul>
            </li>
            <li><a href="#section-3">3. Queues: The FIFO Contract</a>
                <ul><li><a href="#section-3-1">Implementation: Circular Array</a></li></ul>
            </li>
            <li><a href="#section-4">4. Linked Lists</a>
                <ul>
                    <li><a href="#section-4-1">Doubly Linked List</a></li>
                    <li><a href="#section-4-2">Pattern: Sentinel Node</a></li>
                </ul>
            </li>
            <li><a href="#section-5">5. Immersion Example: The Journal</a></li>
        </ul>
    </div>
</div>

<div class="container">

<h1>Lecture: Linked Lists, Stacks, and Queues</h1>

<h2 id="section-1">1. Fundamental Concepts: ADTs vs. Data Structures</h2>

<p>
It is critical to distinguish between an <strong>Abstract Data Type (ADT)</strong> and a <strong>Data Structure</strong>.
</p>
<ul>
    <li>An <strong>ADT</strong> is a contract. It's the <em>what</em>. It defines a set of operations but says nothing about how they are implemented. Think of it as an <code>API Key</code>.</li>
    <li>A <strong>Data Structure</strong> is the implementation. It's the <em>how</em>. It's the concrete arrangement of data that fulfills the contract. Think of it as the <code>running code</code> behind the API.</li>
</ul>

<div class="postgresql-bridge">
<p><strong>Software Engineering Principle (Abstraction):</strong> Programming to an interface (the ADT) instead of an implementation is a foundational principle. It creates a <strong>veil of simplicity</strong> that hides the machinery, allowing you to swap out one data structure for another without breaking the rest of your application.</p>
</div>

<h2 id="section-2">2. Stacks: The LIFO Contract</h2>

<p>
A <strong>Stack</strong> is an ADT enforcing a <strong>Last-In, First-Out (LIFO)</strong> policy. It's a <strong>temporary tower</strong> of data where the last item placed on top is the first one you can access.
</p>
<p class="rhyme">
"Last one on the pile, first to leave in style."
</p>
<h4>Core Properties</h4>
<ul>
    <li><strong>Ordering:</strong> LIFO.</li>
    <li><strong>Operations:</strong> <code>push(item)</code>, <code>pop()</code>, <code>peek()</code>.</li>
    <li><strong>Time Complexity:</strong> All core operations are <strong>instantaneous memory</strong> access, a strict O(1) contract.</li>
    <li><strong>Utility Context:</strong> Function call stacks (the machine's short-term memory), undo/redo features (a history of actions), backtracking algorithms (exploring a maze and retreating).</li>
</ul>

<h3 id="section-2-1">Implementation 1: The Array-Based Stack</h3>
<p>
This is the stack as a <strong>contiguous column</strong>. It uses a pre-allocated array and a single integer (<code>top</code>) to track the summit of our data tower.
</p>
<div class="oracle-specific">
<p><strong>Source:</strong> CLRS (<code>cormen-elementary-data-structures.pdf</code>), Section 10.1, "Stacks", pages 4-5. This code is a direct translation of the CLRS pseudocode, including the critical <code>overflow</code> and <code>underflow</code> checks.</p>
</div>
<ul>
    <li><strong>Advantages:</strong> It's the CPU's best friend. Contiguous memory means fast, cache-friendly access. It's a <strong>thought architecture</strong> of pure efficiency.</li>
    <li><strong>Disadvantages:</strong> It's a <strong>brittle solution</strong>. The fixed capacity creates <strong>golden handcuffs</strong>—you're trapped by the size you initially chose. Exceeding it is catastrophic.</li>
    <li><strong>Software Engineering Principle (Performance vs. Flexibility):</strong> Choose an array-based implementation when performance is critical and the maximum size is predictable.</li>
</ul>
<div class="caution">
<p><strong>Punctuation Joke (Pattern Interrupt):</strong> Trying to <code>push</code> onto a full stack is a classic developer experience. In fact, a kernel developer and a normal person get into a bar fight. The normal person says, "I'll punch you so hard you'll be in a coma!" The kernel dev replies, "Oh yeah? I'll punch you so hard your <em>children</em> will be in a coma!" ...Anyway, that's what a stack overflow feels like.</p>
</div>

<h4>Real-World Example: An Undo/Redo System</h4>
<p>An Undo/Redo system in a text editor is a perfect use case for a stack, where each saved state is pushed onto the history.</p>

```python
# FixedStack class definition from the lecture
class FixedStack:
    def __init__(self, capacity):
        if capacity <= 0: raise ValueError("Capacity must be positive")
        self._data = [None] * capacity
        self._capacity = capacity
        self._top = -1
    def push(self, item):
        if self.is_full(): raise OverflowError("Stack is full")
        self._top += 1
        self._data[self._top] = item
    def pop(self):
        if self.is_empty(): raise IndexError("Pop from an empty stack")
        item = self._data[self._top]
        self._data[self._top] = None
        self._top -= 1
        return item
    def peek(self):
        if self.is_empty(): raise IndexError("Peek from an empty stack")
        return self._data[self._top]
    def is_empty(self): return self._top == -1
    def is_full(self): return self._top == self._capacity - 1
    def __len__(self): return self._top + 1

class EditorState:
    def __init__(self, content): self.content = content

class UndoManager:
    def __init__(self, capacity=10):
        self._history = FixedStack(capacity)
    def save_state(self, content):
        try:
            self._history.push(EditorState(content))
            print(f"Saved: '{content}'")
        except OverflowError:
            print("Undo history is full.")
    def undo(self):
        if self._history.is_empty():
            print("Nothing to undo."); return None
        state = self._history.pop()
        print(f"Undoing to: '{state.content}'")
        return state

# Artificial Data: A series of edits
manager = UndoManager(capacity=3)
editor_content = ""
manager.save_state(editor_content)
editor_content = "Hello"
manager.save_state(editor_content)
editor_content += " World!"
manager.save_state(editor_content)
manager.save_state("This will not be saved") # Expected: Undo history is full.
manager.undo()
manager.undo()
```

<h2 id="section-3">3. Queues: The FIFO Contract</h2>
<p>
A <strong>Queue</strong> is an ADT enforcing a <strong>First-In, First-Out (FIFO)</strong> policy. It is a <strong>patient serpent</strong> of data, consuming from its head what it was fed at its tail.
</p>
<p class="rhyme">
"First to the gate, first to meet its fate."
</p>
<h4>Core Properties</h4>
<ul>
    <li><strong>Ordering:</strong> FIFO.</li>
    <li><strong>Operations:</strong> <code>enqueue(item)</code>, <code>dequeue()</code>.</li>
    <li><strong>Time Complexity:</strong> All core operations must be O(1).</li>
    <li><strong>Utility Context:</strong> Message queues (the <strong>nerve system</strong> of distributed architectures), print schedulers, Breadth-First Search (BFS).</li>
</ul>

<h3 id="section-3-1">Implementation 1: The Circular Array</h3>
<p>
To achieve O(1) <code>dequeue</code> without a costly O(n) shift, we turn our array into a <strong>finite infinity</strong>—a ring buffer. The <code>head</code> and <code>tail</code> indices chase each other around this data racetrack.
</p>
<div class="oracle-specific">
<p><strong>Source:</strong> CLRS (<code>cormen-elementary-data-structures.pdf</code>), Section 10.1, "Queues", pages 6-7. The modulo arithmetic (<code>%</code>) is the key mechanism for implementing the "wrap-around" logic described here.</p>
</div>
<ul>
    <li><strong>Advantages:</strong> O(1) operations within a fixed-size, cache-friendly memory block.</li>
    <li><strong>Disadvantages:</strong> Fixed capacity and slightly more complex logic than a simple stack.</li>
    <li><strong>Software Engineering Principle (Algorithmic Efficiency):</strong> This pattern is a crucial optimization to avoid performance degradation in a bounded queue.</li>
</ul>

<h4>Real-World Example: Server Request Handler</h4>
<p>A web server handles incoming requests in the order they are received, a classic FIFO pattern ideal for a queue.</p>

```python
# CircularQueue class definition from the lecture
class CircularQueue:
    def __init__(self, capacity):
        self._capacity = capacity + 1
        self._data = [None] * self._capacity
        self._head = 0
        self._tail = 0
    def enqueue(self, item):
        if self.is_full(): raise OverflowError("Queue is full")
        self._data[self._tail] = item
        self._tail = (self._tail + 1) % self._capacity
    def dequeue(self):
        if self.is_empty(): raise IndexError("Dequeue from an empty queue")
        item = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._capacity
        return item
    def is_empty(self): return self._head == self._tail
    def is_full(self): return (self._tail + 1) % self._capacity == self._head
    def __len__(self):
        return (self._tail - self._head + self._capacity) % self._capacity

class Server:
    def __init__(self, max_pending=5):
        self._request_queue = CircularQueue(max_pending)
    def receive_request(self, client_ip, resource):
        req = f"GET {resource} FROM {client_ip}"
        try:
            self._request_queue.enqueue(req)
            print(f"Queued: {req}")
        except OverflowError:
            print(f"Server busy. Dropping request: {req}")
    def process_next_request(self):
        if self._request_queue.is_empty():
            print("No requests to process.")
            return
        req = self._request_queue.dequeue()
        print(f"Processing: {req}...")

# Artificial Data: A stream of incoming web requests
server = Server(max_pending=3)
server.receive_request("192.168.1.10", "/index.html")
server.receive_request("10.0.0.5", "/api/data")
server.process_next_request() # Processes the first request
server.receive_request("192.168.1.12", "/images/logo.png")
server.receive_request("10.0.0.8", "/about.html") # Queue is now full
server.receive_request("198.51.100.2", "/login") # This one gets dropped
```

<h2 id="section-4">4. Linked Lists: The Dynamic Data Chain</h2>
<p>
A <strong>Linked List</strong> is a data structure of nodes scattered across memory, a <strong>connected void</strong>. Each node holds data and a pointer—a thread of Ariadne—leading to the next node.
</p>

<h3 id="section-4-1">The Doubly Linked List</h3>
<p>
Adding a <code>prev</code> pointer makes the list a <strong>two-way street</strong>, allowing bidirectional traversal. This enables O(1) insertion and deletion <em>before or after</em> any known node.
</p>
<div class="oracle-specific">
<p><strong>Source:</strong> CLRS (<code>cormen-elementary-data-structures.pdf</code>), Section 10.2, "Linked lists", pages 9-12. This describes the structure and the fundamental <code>LIST-INSERT</code> and <code>LIST-DELETE</code> operations.</p>
</div>
<ul>
    <li><strong>Advantages:</strong> Dynamically sized. Insertion/deletion are O(1) if the location is known, a massive advantage over arrays where these are O(n).</li>
    <li><strong>Disadvantages:</strong> Accessing the <em>k</em>-th element is O(k) — a <strong>one-step-at-a-time pilgrimage</strong>. Higher memory overhead per element and poor cache locality.</li>
</ul>

<h3 id="section-4-2">Pattern: The Sentinel Node</h3>
<p>
To simplify implementation, we use a single dummy node called a <strong>sentinel</strong>. This <strong>empty guardian</strong> sits between the logical head and tail, making the list circular and eliminating all special case logic (e.g., <code>if self.head is None</code>).
</p>
<div class="postgresql-bridge">
<p><strong>Source:</strong> CLRS (<code>cormen-elementary-data-structures.pdf</code>), Section 10.2, "Sentinels", pages 13-14. This source demonstrates how this pattern transforms messy boundary-checking code into clean, unified logic.</p>
<p><strong>Software Engineering Principle (Reducing Complexity):</strong> The sentinel pattern is a classic example of trading a small, constant amount of memory for significantly simpler, more robust, and more maintainable code.</p>
</div>

<h4>Real-World Example: LRU Cache</h4>
<p>A Least Recently Used (LRU) cache evicts the item that hasn't been accessed for the longest time. A doubly linked list is perfect for this: when an item is accessed, its node is moved to the front in O(1). When eviction is needed, the node at the tail is removed in O(1).</p>

```python
# Deque class (Doubly Linked List with Sentinel) definition from the lecture
class Deque:
    class _Node:
        def __init__(self, data, prev_node, next_node):
            self.data, self.prev, self.next = data, prev_node, next_node
    def __init__(self):
        self._sentinel = self._Node(None, None, None)
        self._sentinel.prev = self._sentinel.next = self._sentinel
        self._size = 0
    def is_empty(self): return self._size == 0
    def __len__(self): return self._size
    def _insert_between(self, item, pred, succ):
        new_node = self._Node(item, pred, succ)
        pred.next = new_node
        succ.prev = new_node
        self._size += 1
        return new_node
    def _delete_node(self, node):
        pred, succ = node.prev, node.next
        pred.next, succ.prev = succ, pred
        self._size -= 1
        return node.data
    def add_first(self, item): self._insert_between(item, self._sentinel, self._sentinel.next)
    def add_last(self, item): self._insert_between(item, self._sentinel.prev, self._sentinel)
    def remove_first(self):
        if self.is_empty(): raise IndexError("Deque is empty")
        return self._delete_node(self._sentinel.next)
    def remove_last(self):
        if self.is_empty(): raise IndexError("Deque is empty")
        return self._delete_node(self._sentinel.prev)
    def __iter__(self): # For easy printing
        curr = self._sentinel.next
        while curr is not self._sentinel:
            yield curr.data
            curr = curr.next

# Artificial Data: A command-line history that can be navigated
history = Deque()
history.add_last("ls -l")
history.add_last("cd /tmp")
history.add_last("vim config")

# Simulate moving a command to the front (e.g., re-running an old command)
# This would require a more advanced Deque, but we simulate it here:
print("History:", list(history))
```

<h2 id="section-5">5. Immersion Example: The Chronos Project Event Journal</h2>
<p>
Let's design a core component for a high-stakes system: the event journal for the Chronos Project Time Machine. The machine's operations must be logged. If we create a paradox, we must be able to roll back the changes instantly. This is a <strong>Fictional Case Study</strong> where the <strong>Technical Superstrate</strong> is a robust journaling system, but the <strong>Humorous Substrate</strong> is its absurd application.
</p>
<div class="oracle-specific">
<p><strong>Context:</strong> High-performance databases often use an append-only log. This makes writes a <strong>frictionless absolute</strong>, deferring the complex work of organizing data to a background "compaction" process. A failed transaction is a <strong>time-delay poison</strong>; we need to undo it before it contaminates the timeline.</p>
<p><strong>Source:</strong> Designing Data-Intensive Applications (<code>kleppmann-designing-data-intensive-applications.pdf</code>), Chapter 3.</p>
</div>

<p>Our system requires a harmonious combination of our data structures:</p>
<ul>
    <li><strong>Queue Behavior:</strong> The log is a <strong>river of data</strong>; new events flow to the end. We use the <code>add_last</code> of our <code>Deque</code>.</li>
    <li><strong>Stack Behavior:</strong> Transactions are nested realities. <code>begin_transaction</code> pushes a boundary onto a <code>Stack</code>. <code>rollback_transaction</code> pops the last reality off.</li>
    <li><strong>Linked List Structure:</strong> A rollback means removing nodes. The <code>Deque</code> makes this a series of O(1) excisions, not a slow O(n) array shuffle. It's the difference between surgical removal and amputating the end of the log.</li>
</ul>

```python
# The Journal class uses the Deque and FixedStack classes defined previously.
class Journal:
    def __init__(self, transaction_capacity=10):
        self._log = Deque() # Doubly Linked List for the log
        self._transaction_stack = FixedStack(transaction_capacity) # Stack for transactions
    def log_operation(self, op_type, target_id, data=None):
        op = {'type': op_type, 'id': target_id, 'data': data}
        self._log.add_last(op) # QUEUE: Enqueue to the end
        print(f"Logged: {op_type} on {target_id}")
    def begin_transaction(self):
        self._transaction_stack.push(len(self._log)) # STACK: Push marker
        print("--- Tx Start ---")
    def rollback_transaction(self):
        if self._transaction_stack.is_empty(): return
        start_marker = self._transaction_stack.pop() # STACK: Pop last transaction
        num_to_rollback = len(self._log) - start_marker
        for _ in range(num_to_rollback):
            op = self._log.remove_last() # LINKED LIST: Efficient O(1) removal
            print(f"  ...rolling back {op['type']} on {op['id']}")
        print("--- Tx Rolled Back ---")
    def commit_transaction(self):
        if self._transaction_stack.is_empty(): return
        self._transaction_stack.pop() # STACK: Confirm transaction
        print("--- Tx Commit ---")

# Artificial Data: Simulating temporal operations
print("\n--- Chronos Project Journal ---")
journal = Journal()
journal.log_operation('OBSERVE', 'Cretaceous Period')
journal.log_operation('TWEAK', 'Butterfly_7B4')
journal.begin_transaction()
journal.log_operation('CREATE_PARADOX', 'Grandfather') # Semantic Catalyst: "Whoops, paradox alarms!"
journal.rollback_transaction()
journal.begin_transaction()
journal.log_operation('DELIVER_HINT', 'My Past Self')
journal.commit_transaction()
```
</div>
</body>
# Exercise 1: Fixed-Capacity Stack Implementation

**Objective**: Implement a `Stack` class using a Python list as the underlying storage, simulating a fixed-capacity array. This exercise focuses on the LIFO principle, encapsulation, and handling boundary conditions.

**Specifications**:
1.  Create a class `FixedStack` that is initialized with a `capacity`.
2.  The internal storage should be a pre-allocated Python list of size `capacity`.
3.  Implement the following methods:
    *   `push(item)`: Adds an item to the top of the stack. Must raise an `OverflowError` if the stack is full. This operation must be O(1).
    *   `pop()`: Removes and returns the item from the top of the stack. Must raise an `IndexError` (or a custom `UnderflowError`) if the stack is empty. This operation must be O(1).
    *   `peek()`: Returns the top item without removing it. Must raise an `IndexError` if the stack is empty. This operation must be O(1).
    *   `is_empty()`: Returns `True` if the stack is empty, `False` otherwise.
    *   `is_full()`: Returns `True` if the stack is full, `False` otherwise.
4.  Your implementation should use an integer index (like `S.top`) to manage the stack, not rely solely on Python's list `append` and `pop` methods to emphasize the underlying array-based mechanism.

**Artificial Data & Test Case**:
```python
# Initialize a stack with a capacity of 3
stack = FixedStack(3)

# Test 1: Basic push and peek
print(f"Is empty? {stack.is_empty()}") # Expected: True
stack.push(10)
stack.push(20)
print(f"Peek: {stack.peek()}") # Expected: 20

# Test 2: Fill to capacity and check is_full
stack.push(30)
print(f"Is full? {stack.is_full()}") # Expected: True

# Test 3: Overflow
try:
    stack.push(40)
except OverflowError as e:
    print(e) # Expected: Stack overflow error message

# Test 4: Pop and underflow
print(f"Popped: {stack.pop()}") # Expected: 30
print(f"Popped: {stack.pop()}") # Expected: 20
print(f"Popped: {stack.pop()}") # Expected: 10
print(f"Is empty? {stack.is_empty()}") # Expected: True
try:
    stack.pop()
except IndexError as e:
    print(e) # Expected: Stack underflow error message
```

**Source & Theory**:
*   **CLRS (cormen-elementary-data-structures.pdf), Section 10.1, "Stacks and queues", Pages 4-5**: This section details the array-based implementation of a stack with a `top` attribute and discusses the `STACK-EMPTY`, `PUSH`, and `POP` operations, including overflow and underflow conditions. The O(1) time complexity for each operation is a key property.
*   **Python Tutorial (python-tutorial.pdf), Section 5.1.1, "Using Lists as Stacks"**: While this source shows the simple way using `append` and `pop`, this exercise requires you to implement the more fundamental mechanism described in CLRS to understand how it works under the hood, a key principle in Software Engineering for not relying on "magic" abstractions without understanding their mechanics.

---

# Exercise 2: Circular Queue Implementation

**Objective**: Implement a `CircularQueue` class using a Python list as a fixed-size circular buffer. This exercise trains the FIFO principle, managing pointers/indices in a fixed-size array, and the wrap-around logic.

**Specifications**:
1.  Create a class `CircularQueue` that is initialized with a `capacity`. Note: to store `k` items, the underlying list will need size `k+1` to distinguish between a full and empty queue.
2.  Implement the following methods:
    *   `enqueue(item)`: Adds an item to the tail of the queue. Must raise an `OverflowError` if the queue is full. This operation must be O(1).
    *   `dequeue()`: Removes and returns the item from the head of the queue. Must raise an `IndexError` if the queue is empty. This operation must be O(1).
    *   `is_empty()`: Returns `True` if the queue is empty.
    *   `is_full()`: Returns `True` if the queue is full.
3.  You must use `head` and `tail` integer indices to manage the queue and implement the circular wrap-around logic yourself.

**Artificial Data & Test Case**:
```python
# Queue can hold 3 items, so internal list size is 4
q = CircularQueue(3)

# Test 1: Enqueue and Dequeue
print(f"Is empty? {q.is_empty()}") # Expected: True
q.enqueue('A')
q.enqueue('B')
print(f"Dequeued: {q.dequeue()}") # Expected: A

# Test 2: Wrap-around
q.enqueue('C')
q.enqueue('D') # Fills the queue
print(f"Is full? {q.is_full()}") # Expected: True
print(f"Dequeued: {q.dequeue()}") # Expected: B. Head moves.
q.enqueue('E') # Tail wraps around to the start of the list.
print(f"Is full? {q.is_full()}") # Expected: True

# Test 3: Overflow
try:
    q.enqueue('F')
except OverflowError as e:
    print(e) # Expected: Queue overflow

# Test 4: Emptying and Underflow
print(f"Dequeued: {q.dequeue()}") # Expected: C
print(f"Dequeued: {q.dequeue()}") # Expected: D
print(f"Dequeued: {q.dequeue()}") # Expected: E
print(f"Is empty? {q.is_empty()}") # Expected: True
try:
    q.dequeue()
except IndexError as e:
    print(e) # Expected: Queue underflow
```

**Source & Theory**:
*   **CLRS (cormen-elementary-data-structures.pdf), Section 10.1, "Queues", Pages 6-7**: Describes the circular array implementation with `head` and `tail` attributes. It explains the "wrap around" logic and the condition for a full queue (`Q.head == Q.tail + 1` or the specific wrap-around case), which is fundamental to this exercise. The O(1) time complexity is highlighted.

---

# Exercise 3: Implementing a Deque (Double-Ended Queue)

**Objective**: Implement a `Deque` using a doubly linked list. This exercise combines linked list mechanics with the functional requirements of a deque, demonstrating the advantage of linked lists for O(1) insertions/deletions at both ends.

**Specifications**:
1.  Create a private `_Node` class to represent list elements, with `data`, `next`, and `prev` attributes.
2.  Create a `Deque` class. For simplicity and robustness, use a **sentinel node** to represent the head/tail of the list, simplifying boundary checks.
3.  The `Deque` class should have an internal `_sentinel` node and a `_size` counter.
4.  Implement the following O(1) methods:
    *   `add_first(item)`: Adds an item to the front of the deque.
    *   `add_last(item)`: Adds an item to the back of the deque.
    *   `remove_first()`: Removes and returns the item from the front. Raises `IndexError` if empty.
    *   `remove_last()`: Removes and returns the item from the back. Raises `IndexError` if empty.
    *   `is_empty()`: Returns `True` if empty.
    *   `__len__()`: Returns the number of items.

**Artificial Data & Test Case**:
```python
d = Deque()
print(f"Is empty? {d.is_empty()}") # Expected: True

# Test 1: Add last, remove first (FIFO behavior)
d.add_last(10)
d.add_last(20)
print(f"Length: {len(d)}") # Expected: 2
print(f"Removed first: {d.remove_first()}") # Expected: 10

# Test 2: Add first, remove last (FIFO behavior, reversed)
d.add_first(5)
print(f"Removed last: {d.remove_last()}") # Expected: 20
print(f"Removed last: {d.remove_last()}") # Expected: 5
print(f"Is empty? {d.is_empty()}") # Expected: True

# Test 3: Add first, remove first (LIFO behavior)
d.add_first(30)
d.add_first(40)
print(f"Removed first: {d.remove_first()}") # Expected: 40
print(f"Removed first: {d.remove_first()}") # Expected: 30

# Test 4: Underflow
try:
    d.remove_last()
except IndexError as e:
    print(e) # Expected: Deque is empty
```

**Source & Theory**:
*   **CLRS (cormen-elementary-data-structures.pdf), Section 10.2, "Linked lists" & "Sentinels", Pages 9-14**: Provides the complete theory for doubly linked lists, including the `LIST-INSERT` and `LIST-DELETE` primitives. The "Sentinels" subsection is key, as it explains how a dummy object simplifies the code for insertion and deletion by removing the need for `if/else` checks for the head or tail of the list. This directly relates to the Software Engineering principle of reducing code complexity and potential bugs.
*   **CLRS (cormen-elementary-data-structures.pdf), Exercise 10.1-6**: This exercise explicitly asks for the implementation of a deque, and this problem provides the full implementation context.

---

# Hardcore Combined Problem: Log-Structured File System Journal

**Objective**: Simulate the journaling component of a log-structured file system. This system must efficiently process a stream of file system operations (write, delete), store them chronologically, and support state restoration and "compaction" (removing obsolete records). This problem combines the FIFO nature of a queue, the LIFO nature of a stack for transaction management, and the efficient insertion of a linked list.

**Problem Statement**:
You are to build a `Journal` class that models an in-memory transaction log.
1.  **Core Data Structure**: The journal itself will be a **Doubly Linked List** of `Operation` objects. Each `Operation` has a `type` ('write', 'delete'), a `file_id`, and `data` (for writes). A linked list is chosen because we may need to remove operations from the middle during compaction without shifting large amounts of data.
2.  **Incoming Operations**: New operations arrive and are added to the end of the journal, behaving like a **Queue**.
3.  **Transactions**: Operations can be grouped into transactions. A transaction is a sequence of operations that must be committed or rolled back as a single unit. You will use a **Stack** to manage transaction boundaries.

**Specifications**:
1.  **`Journal` Class**:
    *   `log_operation(op_type, file_id, data=None)`: Appends a new operation to the tail of the linked list journal. O(1).
    *   `begin_transaction()`: Pushes a special marker onto a transaction stack. This marker will later store a pointer to the first operation node of this transaction. O(1).
    *   `commit_transaction()`: Finalizes the transaction. Pops the marker from the stack. O(1). If the stack is empty, it means there's no open transaction to commit.
    *   `rollback_transaction()`: Undoes all operations in the current transaction. It should pop the transaction marker, then remove all operation nodes from the journal's linked list back to the marker's position. This demonstrates the advantage of a linked list for efficient node removal. The complexity should be proportional to the number of operations in the transaction, not the size of the whole journal.
    *   `compact()`: This is the most complex part. It simulates cleaning up the journal. It should iterate through the journal from the beginning. For a given `file_id`, only the *last* 'write' operation is valid. Any 'write' followed by a later 'delete' for the same `file_id` is obsolete. All obsolete operations should be removed. This task requires an auxiliary data structure (like a dictionary, a concept from a previous chunk) to track the latest state of each file.

**Artificial Data & Test Case**:
```python
journal = Journal()

# Log some operations
journal.log_operation('write', file_id='file_a', data='content1')
journal.log_operation('write', file_id='file_b', data='content_b')

# Start a transaction that will be rolled back
journal.begin_transaction()
journal.log_operation('write', file_id='file_a', data='bad_content') # This will overwrite file_a
journal.log_operation('delete', file_id='file_b')
journal.rollback_transaction()

# After rollback, the state should be as if the transaction never happened
# print(journal) -> Expected: Op(write, file_a, content1), Op(write, file_b, content_b)

# Start a transaction that will be committed
journal.begin_transaction()
journal.log_operation('write', file_id='file_c', data='new_file')
journal.log_operation('write', file_id='file_a', data='content2') # Overwrites file_a again
journal.commit_transaction()

# print(journal) -> Expected: Original ops + the new committed ones

# Perform compaction
# The first write to file_a is now obsolete.
final_state = journal.compact()
# print(journal) -> Expected: Op(write, file_b, content_b), Op(write, file_c, new_file), Op(write, file_a, content2)
# The order might change depending on compaction implementation, but only the latest versions should exist.
```

**Source & Theory**:
*   **Combination of Concepts**: This problem forces the integration of multiple data structures, leveraging their specific properties:
    *   **Queue (FIFO)**: The natural, chronological ordering of the log is a queue-like behavior (`log_operation` is like `enqueue`). Implemented with the tail of the linked list for O(1) appends. Source: **CLRS Chapter 10.1**.
    *   **Stack (LIFO)**: Perfectly models the nested, last-in-first-out nature of transactions (`begin`, `commit`, `rollback`). Source: **CLRS Chapter 10.1**.
    *   **Doubly Linked List**: The core of the solution. Its O(1) node removal is critical for efficient `rollback_transaction` and `compact` methods, which would be prohibitively slow (O(N*M)) with an array-based list. Source: **CLRS Chapter 10.2**.
*   **Design Data-Intensive Applications (kleppmann-designing-data-intensive-applications.pdf), Chapter 3**: This chapter discusses log-structured storage engines. The core idea of an append-only log followed by compaction is the direct inspiration for this problem, providing a real-world context where these fundamental data structures are essential. This exercise simulates in-memory the principles of LSM-Trees and log-structured file systems.
*   **Software Engineering Principles**: This problem requires significant attention to **Encapsulation** (the `Journal` class hides the complex interactions), **Modularity** (each method has a clear responsibility), and **Algorithmic Efficiency** (choosing the right data structure for each sub-problem is key to performance).
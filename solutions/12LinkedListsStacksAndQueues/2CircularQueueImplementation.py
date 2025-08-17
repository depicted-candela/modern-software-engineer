#   Exercise 2: Circular Queue Implementation
# Objective: Implement a CircularQueue class using a Python list as a fixed-size 
# circular buffer. This exercise trains the FIFO principle, managing 
# pointers/indices in a fixed-size array, and the wrap-around logic.

#   Specifications:

# Create a class CircularQueue that is initialized with a capacity. Note: to store 
# k items, the underlying list will need size k+1 to distinguish between a full and 
# empty queue.
# Implement the following methods:
# enqueue(item): Adds an item to the tail of the queue. Must raise an 
# OverflowError if the queue is full. This operation must be O(1).
# dequeue(): Removes and returns the item from the head of the queue. Must raise 
# an IndexError if the queue is empty. This operation must be O(1).
# is_empty(): Returns True if the queue is empty.
# is_full(): Returns True if the queue is full.
# You must use head and tail integer indices to manage the queue and implement the 
# circular wrap-around logic yourself.

class CircularQueue:
    def __init__(self, capacity):
        self._capacity = capacity + 1
        self._buffer = [None] * self._capacity
        self._head = 0
        self._tail = 0
    def enqueue(self, item):
        if self.is_full():
            message = f"The queue of size {self._capacity} is full"
            message += f"with {self._buffer[self._head]} as its last item"
            raise OverflowError(message)
        self._buffer[self._tail] = item
        self._tail = (self._tail + 1) % self._capacity
    def dequeue(self):
        if self.is_empty():
            message = f"The queue is empty at {self._head}, no items are for process"
            raise IndexError(message)
        item = self._buffer[self._head]
        self._buffer[self._head] = None
        self._head = (self._head + 1) % self._capacity
        return item
    def is_empty(self): return self._head == self._tail
    def is_full(self): return (self._tail + 1) % self._capacity == self._head
    def __str__(self): return f"{self._buffer}"

# Queue can hold 3 items, so internal list size is 4
q = CircularQueue(3)

# Test 1: Enqueue and Dequeue
print(f"Is empty? {q.is_empty()}") # Expected: True
q.enqueue('A')
print(q)
q.enqueue('B')
print(q)
print(f"Dequeued: {q.dequeue()}") # Expected: A

# Test 2: Wrap-around
q.enqueue('C')
print(q)
q.enqueue('D') # Fills the queue
print(q)
print(f"Is full? {q.is_full()}") # Expected: True
print(f"Dequeued: {q.dequeue()}") # Expected: B. Head moves.
q.enqueue('E') # Tail wraps around to the start of the list.
print(f"Is full? {q.is_full()}") # Expected: True
print(q)

# Test 3: Overflow
try:
    q.enqueue('F')
    print(q)
except OverflowError as e:
    print(e) # Expected: Queue overflow

# Test 4: Emptying and Underflow
print(f"Dequeued: {q.dequeue()}") # Expected: C
print(q)
print(f"Dequeued: {q.dequeue()}") # Expected: D
print(q)
print(f"Dequeued: {q.dequeue()}") # Expected: E
print(q)
print(f"Is empty? {q.is_empty()}") # Expected: True
try:
    q.dequeue()
except IndexError as e:
    print(e) # Expected: Queue underflow
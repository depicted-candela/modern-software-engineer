class FixedStack:
    def __init__(self, capacity: int):
        self._top = -1
        self._capacity = capacity
        self._storage = [None] * capacity
    def push(self, item):
        if self.is_full():
            message = f"The fixed stack is in its maximum capacity {self._capacity}"
            raise OverflowError(message)
        self._top += 1
        self._storage[self._top] = item
    def pop(self):
        if self.is_empty(): raise IndexError("The stack is empty")
        last_item = self._storage[self._top]
        self._storage[self._top] = None
        self._top -= 1
        return last_item
    def peek(self):
        if self.is_empty(): raise IndexError("The stack is empty")
        return self._storage[self._top]
    def is_empty(self):
        return self._top == -1
    def is_full(self):
        return self._top == self._capacity - 1
    
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
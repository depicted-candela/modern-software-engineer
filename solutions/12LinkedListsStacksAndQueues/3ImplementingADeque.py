class Deque:
    class _Node:
        def __init__(self, data, prev, next):
            self.data, self.prev, self.next = data, prev, next
    def __init__(self):
        self._sentinel = self._Node(None, None, None)
        self._sentinel.next = self._sentinel
        self._sentinel.prev = self._sentinel
        self._size = 0
    def add_first(self, item):
        newNode = self._Node(item, self._sentinel, self._sentinel.next)
        self._sentinel.next.prev = newNode
        self._sentinel.next = newNode
        self._size += 1
    def add_last(self, item):
        newNode = self._Node(item, self._sentinel.prev, self._sentinel)
        self._sentinel.prev.next = newNode
        self._sentinel.prev = newNode
        self._size += 1
    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        return node.data
    def remove_first(self):
        return self.delete_node(self._sentinel.next)
    def remove_last(self):
        return self.delete_node(self._sentinel.prev)
    def is_empty(self):
        return self._size == 0
    def __len__(self):
        return self._size

d = Deque()
print(f"Is empty? {d.is_empty()}") # Expected: True
assert d.is_empty() == True

# Test 1: Add last, remove first (FIFO behavior)
d.add_last(10)
d.add_last(20)
assert len(d) == 2
print(f"Length: {len(d)}") # Expected: 2
test_first_deletion = d.remove_first()
print(test_first_deletion)
assert test_first_deletion == 10
print(f"Removed first: {test_first_deletion}") # Expected: 10

# Test 2: Add first, remove last (FIFO behavior, reversed)
d.add_first(5)
test_second_deletion = d.remove_last()
assert test_second_deletion == 20
print(f"Removed last: {test_second_deletion}") # Expected: 20
test_third_deletion = d.remove_last()
assert test_third_deletion == 5
print(f"Removed last: {test_third_deletion}") # Expected: 5
assert d.is_empty() == True
print(f"Is empty? {d.is_empty()}") # Expected: True

# Test 3: Add first, remove first (LIFO behavior)
d.add_first(30)
d.add_first(40)
test_fourth_deletion = d.remove_first()
assert test_fourth_deletion == 40
print(f"Removed first: {test_fourth_deletion}") # Expected: 40
test_fifth_deletion = d.remove_first()
assert test_fifth_deletion == 30
print(f"Removed first: {test_fifth_deletion}") # Expected: 30

# Test 4: Underflow
try:
    d.remove_last()
except IndexError as e:
    print(e) # Expected: Deque is empty
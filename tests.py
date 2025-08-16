# Deque class (Doubly Linked List with Sentinel) definition from the lecture
class Deque:
    """
    A double-ended queue (deque) implementation using a doubly linked list
    with a sentinel node.
    """
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        def __init__(self, data, prev_node, next_node):
            self.data = data
            self.prev = prev_node
            self.next = next_node

    def __init__(self):
        """
        Initializes an empty Deque.
        The sentinel node's prev and next pointers point to itself,
        creating an empty circular list.
        """
        self._sentinel = self._Node(None, None, None) # Sentinel node
        self._sentinel.prev = self._sentinel.next = self._sentinel
        self._size = 0 # Number of actual elements in the deque

    def is_empty(self):
        """
        Returns True if the deque is empty, False otherwise.
        """
        return self._size == 0

    def __len__(self):
        """
        Returns the number of elements in the deque.
        Allows use of len(deque_instance).
        """
        return self._size

    def _insert_between(self, item, pred, succ):
        """
        Adds a new node containing 'item' between 'pred' (predecessor)
        and 'succ' (successor) nodes.
        This is an internal helper method.
        """
        new_node = self._Node(item, pred, succ)
        pred.next = new_node
        succ.prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node):
        """
        Deletes a given 'node' from the deque and returns its data.
        This is an internal helper method.
        """
        pred, succ = node.prev, node.next
        pred.next, succ.prev = succ, pred
        self._size -= 1
        return node.data

    def add_first(self, item):
        """
        Adds an 'item' to the front (leftmost) of the deque.
        """
        self._insert_between(item, self._sentinel, self._sentinel.next)

    def add_last(self, item):
        """
        Adds an 'item' to the back (rightmost) of the deque.
        """
        self._insert_between(item, self._sentinel.prev, self._sentinel)

    def remove_first(self):
        """
        Removes and returns the item from the front (leftmost) of the deque.
        Raises an IndexError if the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._delete_node(self._sentinel.next)

    def remove_last(self):
        """
        Removes and returns the item from the back (rightmost) of the deque.
        Raises an IndexError if the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._delete_node(self._sentinel.prev)

    def __iter__(self):
        """
        Allows iteration over the deque elements from front to back.
        Enables use in for loops or conversion to list, e.g., list(deque).
        """
        curr = self._sentinel.next
        while curr is not self._sentinel:
            yield curr.data
            curr = curr.next

    def __str__(self):
        """
        Returns a string representation of the deque, useful for debugging.
        """
        return str(list(self))

# --- Examples and Demonstrations ---

def print_deque_status(deque_instance, message="Current Deque Status"):
    """Helper function to print the deque's current state clearly."""
    print(f"\n--- {message} ---")
    print(f"Is empty: {deque_instance.is_empty()}")
    print(f"Length: {len(deque_instance)}")
    print(f"Contents: {deque_instance}") # Uses __str__ which uses __iter__
    print("-" * (len(message) + 10))

print("--- Deque Operation Demonstration ---")

# 1. __init__(): Creating a new Deque instance
print("\n1. Demonstrating __init__ (Deque Initialization)")
my_deque = Deque()
print_deque_status(my_deque, "After Deque() initialization")
# Expected: Is empty: True, Length: 0, Contents: []

# 2. is_empty() and __len__(): On an empty deque
print("\n2. Demonstrating is_empty() and __len__() on an empty deque:")
print(f"Is deque empty? {my_deque.is_empty()} (Expected: True)")
print(f"Length of deque? {len(my_deque)} (Expected: 0)")

# 3. add_first(item): Adding elements to the front
print("\n3. Demonstrating add_first(item):")
my_deque.add_first("Apple")
print_deque_status(my_deque, "After add_first('Apple')")
# Expected: Contents: ['Apple'], Length: 1

my_deque.add_first("Banana")
print_deque_status(my_deque, "After add_first('Banana')")
# Expected: Contents: ['Banana', 'Apple'], Length: 2

my_deque.add_first(100)
print_deque_status(my_deque, "After add_first(100)")
# Expected: Contents: [100, 'Banana', 'Apple'], Length: 3

# 4. add_last(item): Adding elements to the back
print("\n4. Demonstrating add_last(item):")
my_deque.add_last("Cherry")
print_deque_status(my_deque, "After add_last('Cherry')")
# Expected: Contents: [100, 'Banana', 'Apple', 'Cherry'], Length: 4

my_deque.add_last(True)
print_deque_status(my_deque, "After add_last(True)")
# Expected: Contents: [100, 'Banana', 'Apple', 'Cherry', True], Length: 5

# 5. _insert_between(): (Internal helper, demonstrated by add_first/add_last)
print("\n5. Demonstrating _insert_between() implicitly via add_first() and add_last():")
print("The _insert_between method is an internal helper.")
print("When 'Apple' was added via add_first, it called _insert_between(Apple, sentinel, sentinel.next).")
print("When True was added via add_last, it called _insert_between(True, sentinel.prev, sentinel).")
print("Current contents: ", my_deque)

# 6. remove_first(): Removing elements from the front
print("\n6. Demonstrating remove_first():")
removed_item = my_deque.remove_first()
print(f"Removed item from front: {removed_item}")
print_deque_status(my_deque, "After remove_first()")
# Expected: Removed: 100, Contents: ['Banana', 'Apple', 'Cherry', True], Length: 4

removed_item = my_deque.remove_first()
print(f"Removed item from front: {removed_item}")
print_deque_status(my_deque, "After second remove_first()")
# Expected: Removed: 'Banana', Contents: ['Apple', 'Cherry', True], Length: 3

# 7. remove_last(): Removing elements from the back
print("\n7. Demonstrating remove_last():")
removed_item = my_deque.remove_last()
print(f"Removed item from back: {removed_item}")
print_deque_status(my_deque, "After remove_last()")
# Expected: Removed: True, Contents: ['Apple', 'Cherry'], Length: 2

removed_item = my_deque.remove_last()
print(f"Removed item from back: {removed_item}")
print_deque_status(my_deque, "After second remove_last()")
# Expected: Removed: 'Cherry', Contents: ['Apple'], Length: 1

# 8. _delete_node(): (Internal helper, demonstrated by remove_first/remove_last)
print("\n8. Demonstrating _delete_node() implicitly via remove_first() and remove_last():")
print("The _delete_node method is an internal helper.")
print("When 100 was removed via remove_first, _delete_node was called on its node.")
print("When True was removed via remove_last, _delete_node was called on its node.")
print("Current contents: ", my_deque)

# Clear the deque for error testing
print("\n--- Clearing the deque to test empty scenarios ---")
while not my_deque.is_empty():
    removed_item = my_deque.remove_first()
    print(f"Removed {removed_item}. Deque: {my_deque}")
print_deque_status(my_deque, "After emptying the deque")

# 9. Error Handling: remove_first() and remove_last() on an empty deque
print("\n9. Demonstrating error handling for remove_first() and remove_last() on an empty deque:")
try:
    my_deque.remove_first()
except IndexError as e:
    print(f"Caught expected error for remove_first() on empty deque: '{e}'")

try:
    my_deque.remove_last()
except IndexError as e:
    print(f"Caught expected error for remove_last() on empty deque: '{e}'")

# 10. __iter__(): Explicit demonstration (already heavily used by print_deque_status and str(deque))
print("\n10. Demonstrating __iter__ (explicitly):")
print("Re-populating the deque for iteration example.")
my_deque.add_last("First")
my_deque.add_last("Second")
my_deque.add_last("Third")
print("Deque elements using a for loop (relies on __iter__):")
for item in my_deque:
    print(f"  --> {item}")
print("Deque elements converted to a list (relies on __iter__):", list(my_deque))

# --- Original Artificial Data Example: Command Line History ---
print("\n--- Original Artificial Data Example: Command Line History ---")
history = Deque()
print_deque_status(history, "Initial empty history")

# Add commands
print("Adding initial commands to history:")
history.add_last("ls -l")
print_deque_status(history, "After add_last('ls -l')")

history.add_last("cd /tmp")
print_deque_status(history, "After add_last('cd /tmp')")

history.add_last("vim config")
print_deque_status(history, "After add_last('vim config')")

# Simulate a frequently used command or new command added to the front
print("\nSimulating adding a new/frequently used command to the front (most recent):")
history.add_first("clear_screen")
print_deque_status(history, "After add_first('clear_screen')")
# Note: 'clear_screen' is now the first item, representing the 'most recent' command.

# Simulating navigating history: Removing the most recent command
print("\nSimulating 'undoing' or removing the last-entered command (remove_first):")
if not history.is_empty():
    last_entered_command = history.remove_first()
    print(f"Removed the most recently added command (from front): '{last_entered_command}'")
    print_deque_status(history, "History after remove_first()")
else:
    print("History is empty, cannot remove first.")

# Simulating a command being removed from the 'oldest' end
print("\nSimulating purging the oldest command (remove_last):")
if not history.is_empty():
    oldest_command = history.remove_last()
    print(f"Removed the oldest command (from back): '{oldest_command}'")
    print_deque_status(history, "History after remove_last()")
else:
    print("History is empty, cannot remove last.")

print("\nFinal state of the command history:", history)
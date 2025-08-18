from dataclasses import dataclass

@dataclass
class Operation:
    type: str
    file_id: int
    data: str
    def __repr__(self):
        return f"Op({self.type}, {self.file_id}, {self.data})"

class TransactionalStack:
    def __init__(self, capacity):
        self._capacity = capacity
        self._buffer = [None] * capacity
        self._top = -1
    def push(self, operation: Operation):
        if self.is_full(): raise OverflowError("Stack is full")
        self._top += 1
        self._buffer[self._top] = operation
    def pop(self):
        if self.is_empty(): raise IndexError("The transactional stack is already empty")
        operation = self._buffer[self._top]
        self._buffer[self._top] = None
        self._top -= 1
        return operation
    def peek(self):
        if self.is_empty(): raise IndexError("Peek from an empty stack")
        return self._buffer[self._top]
    def is_empty(self): 
        return self._top == -1
    def is_full(self):
        return self._top == self._capacity - 1

class Logs:
    class _Node:
        def __init__(self, entry, prev, next):
            self.entry = entry
            self.prev = prev
            self.next = next
    def __init__(self):
        self._kernel = self._Node(None, None, None)
        self._kernel.prev = self._kernel
        self._kernel.next = self._kernel
        self._tail, self._head = 0, 0
        self._size = 0
    def delete_log(self, log):
        log.prev.next = log.next
        log.next.prev = log.prev
        self._size -= 1
        return log
    def insert_between(self, log, prev, next):
        new_log = self._Node(log, prev, next)
        prev.next = new_log
        next.prev = new_log
        self._size += 1
    def add_first(self, log):
        self.insert_between(log, self._kernel, self._kernel.next)
    def remove_last(self):
        return self.delete_log(self._kernel.prev)
    def __iter__(self):
        curr = self._kernel.next
        while curr is not self._kernel:
            yield curr.entry.data
            curr = curr.next
    def __len__(self):
        return self._size

class Journal:
    def __init__(self, transactional_capacity):
        self._logs = Logs()
        self._operations = TransactionalStack(transactional_capacity)
    def log_operation(self, op_type: str, file_id: int, data: str=None):
        operation = Operation(op_type, file_id, data)
        self._logs.add_first(operation)
    def begin_transaction(self):
        self._operations.push(len(self._logs))
    def commit_transaction(self):
        try:
            self._operations.pop()
        except IndexError as e:
            raise ValueError("An empty transaction cannot be committed") from e
    def rollback_transaction(self):
        if self._operations.is_empty():
            raise IndexError("There aren't operations to roll back")
        marker = self._operations.pop()
        true_marker = len(self._logs) - marker
        for _ in range(true_marker): 
            rolled_operation = self._logs.remove_last()
            print(f"{rolled_operation.entry} rolled back")
    def compact(self):
        latest_operations = {}
        current = self._logs._kernel.next
        while current is not self._logs._kernel:
            operation = current.entry
            latest_operations[operation.file_id] = {'log': current, 'op': operation}
            current = current.next
        current = self._logs._kernel.next
        while current is not self._logs._kernel:
            next_log = current.next
            op = current
            latest = latest_operations.get(op.entry.file_id)
            cond1 = latest['log'] is not current ## Pointer usage
            cond2 = (op.entry.type == 'write' and op.entry.file_id in latest_operations and latest_operations[op.entry.file_id]['op'].type == 'delete')
            if cond1 or cond2:
                self._logs.delete_log(current)
            current = next_log
    def __repr__(self):
        """String representation of the journal."""
        return f"Journal({list(self._logs)})"

journal = Journal(10)

# Log some operations
journal.log_operation('write', file_id='file_a', data='content1')
journal.log_operation('write', file_id='file_b', data='content_b')

# Start a transaction that will be rolled back
journal.begin_transaction()
journal.log_operation('write', file_id='file_a', data='bad_content')
journal.log_operation('delete', file_id='file_b')
journal.rollback_transaction()

# Print journal state
print(journal)

# Start a transaction that will be committed
journal.begin_transaction()
journal.log_operation('write', file_id='file_c', data='new_file')
journal.log_operation('write', file_id='file_a', data='content2')
journal.commit_transaction()

# Print journal state
print(journal)

# Perform compaction
final_state = journal.compact()
print(f"Final state: {final_state}")
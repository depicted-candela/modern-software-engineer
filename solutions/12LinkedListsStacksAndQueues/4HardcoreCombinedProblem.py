from dataclasses import dataclass

@dataclass
class Operation:
    type: str
    file_id: int
    data: str

class Journal:
    def log_operation(op_type: Operation, file_id, data=None):
        pass
    def begin_transaction():
        pass
    def commit_transaction():
        pass
    def rollback_transaction():
        pass
    def compact():
        pass
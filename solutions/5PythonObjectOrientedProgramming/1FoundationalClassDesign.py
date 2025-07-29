record1_data = {
    'id': 'REC-001', 
    'source': 'Telespazio', 
    'value': 45.23, 
    'validated': False}
record2_data = {
    'id': 'REC-002', 
    'source': 'IGAC', 
    'value': 78.1, 
    'validated': True}

class DataRecord:
    def __init__(self, record: dict):
        self.id = record['id']
        self.source = record['source']
        self.value = record['value']
        self.validated = record['validated']
    def __str__(self):
        return f"[{self.id} from {self.source}] Value: {self.value} (Validated: {self.validated})"
    def validate_record(self):
        self.validated = True
    
record = DataRecord(record1_data)
record.validate_record()
print(record)


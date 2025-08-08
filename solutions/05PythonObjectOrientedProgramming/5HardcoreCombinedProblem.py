from abc import ABC, abstractmethod

dataset = [
    {'id': 1, 'type': 'geospatial', 'coords': (4.6, -74.0), 'value': 100}, # Valid
    {'id': 2, 'type': 'telemetry', 'coords': None, 'value': -50},        # Invalid value
    {'id': 3, 'type': 'geospatial', 'coords': (91.0, -74.0), 'value': 200}, # Invalid coords
    {'id': 4, 'type': 'generic', 'coords': None, 'value': 300}            # Missing type-specific check
]

class ValidationRule(ABC):
    def __init__(self, message: str):
        super().__init__()
        self.error = message
    @abstractmethod
    def is_valid(self, record) -> bool: pass

class ValuePositiveRule(ValidationRule):
    def is_valid(self, record: dict) -> bool:
        key = 'value'
        return key in record and record[key] > 0

class TypeKnownRule(ValidationRule):
    def is_valid(self, record: dict):
        key = 'type'
        return key in record and record[key] in ['geospatial', 'telemetry']

class GeospatialCoordsRule(ValidationRule):
    def is_valid(self, record: dict) -> bool:
        value = 'coords'
        type = 'geospatial'
        if type in record and value in record:
            lat, lon = record[value]
            return -91 < lat < 91 and -181 < lon < 181
        return False

class DataValidator:
    def __init__(self):
        self.__rules: list[ValidationRule] = []
    def add_rule(self, rule: ValidationRule):
        self.__rules.append(rule)
    def validate_dataset(self, dataset):
        errors: dict[int, list[str]] = {}
        for record in dataset:
            record_id = record.get('id')
            for rule in self.__rules:
                if not rule.is_valid(record):
                    errors.setdefault(record_id, []).append(rule.error)
        return errors

if __name__ == '__main__':
    validator = DataValidator()
    validator.add_rule(ValuePositiveRule('Telemetries are always positive'))
    validator.add_rule(TypeKnownRule('Records must be telemetry or geospatial'))
    validator.add_rule(GeospatialCoordsRule('Geospatial must be coherent with angular geodesic systems'))
    print(validator.validate_dataset(dataset))

# value_positive = ValuePositiveRule('Telemetries are always positive')
# known_type = TypeKnownRule('Records must be telemetry or geospatial')
# appropriate_coords = GeospatialCoordsRule('Geospatial must be coherent with angular geodesic systems')
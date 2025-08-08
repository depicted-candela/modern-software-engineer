import json
from json import JSONDecodeError

api_endpoints = [
    "api/source1",
    "api/unreachable",
    "api/source2",
    "api/source3"
]

mock_api_responses = {
    "api/source1": '{"id": 1, "geometry": {"type": "Point", "coordinates": [-74.0060, 40.7128]}}',
    "api/source2": '{"id": 2, "geometry": "invalid_structure"}', # Will cause DataParsingError on access
    "api/source3": '{"id": 3, "geometry": {"type": "LineString", "coordinates": [[-74, 40], [-73, 41]]}}' # Will cause ValidationRuleError
}

class APIConnection(Exception):
    """For network-related issues"""
    pass

class DataParsingError(ValueError):
    """For malformed JSON or data structure issues"""
    pass

class ValidationRuleError(ValueError):
    """For records that fail domain-specific validation"""
    pass

def fetch_data(endpoint: str):
    mock_api_response = mock_api_responses[endpoint]
    return json.dumps(mock_api_response) if not "unreachable" in endpoint else APIConnection(f"Unreachable in {endpoint}")

class DatabaseConnection:
    def __init__(self):
        self.records = []
    def __enter__(self):
        print("DB connection opened.")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("DB connection closed.")
    def write(self, record):
        self.records.append(record)

def run_pipeline(endpoints: list[str]):
    with DatabaseConnection() as dc:
        failures = []
        for endpoint in endpoints:
            try:
                fetched_data = fetch_data(endpoint)
                try:
                    parsed_data = json.loads(fetched_data)
                    if type(parsed_data) != dict: 
                        raise ValidationRuleError("The parsed data is not a dict")
                    keys = parsed_data.keys()
                    if type(keys) != dict: 
                        raise ValidationRuleError("Keys of parsed data is not a dict")
                    if "geometry" not in keys: 
                        raise ValidationRuleError("Keys of parsed data does not have geometry")
                    geotype = keys["geometry"]
                    if set(["type", "coordinates"]).issubset(geotype.keys()):
                        raise ValidationRuleError("Keys of parsed geometry does not have sufficient features")
                    type_value, geometry = geotype["type"], geotype["geometry"]
                    is_not_point = type_value != "Point"
                    dim_geo = len(geometry)
                    failed_dim_geo = dim_geo != 2
                    if is_not_point or failed_dim_geo: 
                        message == f"type value {type_value} must be Point" if is_not_point else f"Geometrical dimensions {dim_geo} must be 2"
                        raise ValidationRuleError(f"Geometry type invalid ")
                except JSONDecodeError as e: raise DataParsingError from e
                except ValidationRuleError as e: 
                    e.add_note("Nested ValidationRuleError")
                    raise e
            except APIConnection as e:
                message = f"Failing endpoint {endpoint} as API Connection for network-related issues"
                e.add_note(message)
                failures.append(e)
                continue
            except DataParsingError as e:
                message = f"Failing endpoint {endpoint} as DataParsing error for malformed JSON or data structure issues"
                e.add_note(message)
                failures.append(e)
                continue
            except ValidationRuleError as e:
                message = f"Failing endpoint {endpoint} as ValidationRuleError for records that fail domain-specific validation"
                e.add_note(message)
                failures.append(e)
                continue
            except Exception as e:
                message = f"Unexpected exeption {e}"
                failures.append(e)
                continue
            dc.write(endpoint)
        if len(failures) != 0: 
            raise ExceptionGroup("Pipeline encountered one or more errors", failures)

if __name__ == "__main__":
    run_pipeline(api_endpoints)
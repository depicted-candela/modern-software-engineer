# Core Training: Python Functions


#   Exercise 1: Foundational Data Processor
# Objective: Master the core concepts of function definition (def, return), and the use of positional, 
# keyword, and default value parameters. This exercise connects to Chunk 1 (Data Types) and Chunk 2 
# (Control Structures).

# A list of data records representing gravity measurements.
# Format 1: A tuple (record_id, latitude, longitude, gravity_value)
# Format 2: A tuple with an optional quality score (record_id, latitude, longitude, gravity_value, quality)
record_1 = (1001, 4.60, -74.08, 9.780)
record_2 = (1002, 4.61, -74.07, 9.781, 0.95)

def normalize_record(record, default_quality=0.85):
    elements = len(record)
    record_id, lat, long, gravity = record[:4]
    quality = default_quality if elements == 4 else record[-1]
    return {'record_id': record_id, 'lat': lat, 'long': long, 'gravity': gravity, 'quality': quality}


#   Exercise 2: Dynamic Data Aggregator and Scope Management
# Objective: Understand and implement functions that can handle a variable number of arguments 
# (*args, **kwargs). This exercise also focuses on managing variable scope (local vs. global).

import logging, sys

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout
)

# Global variable to track error count
ERROR_COUNT = 0

# Sample calls to the logger
log_entry_1 = ("Pipeline Stage 1 Complete", 1678886400)
metadata_1 = {"author": "Castelblanco", "status": "success"}
log_entry_2 = ("ERROR: Geoidal model failed to converge", 1678887000, "High-Severity")
metadata_2 = {"author": "Castelblanco", "status": "failure", "retry_attempt": 3}

def log_event(message, *context, **metadata):
    logging.info(f" Core message: {message}")
    for entry in context: print(f"Context -> {entry}")
    for key, value in metadata.items(): print(f"Metadata -> key: {key}, value: {value}")
    global ERROR_COUNT
    if "status" in metadata and metadata['status'] == 'failure': ERROR_COUNT += 1


#   Exercise 3: Higher-Order Functions for Data Transformation
# Objective: To practice using higher-order functions (functions that take other functions as arguments) 
# and lambda expressions for concise, powerful data manipulation.
cadastral_data = [
    {"id": "A-01", "x_coords": [0, 10], "y_coords": [0, 5], "is_valid": True},
    {"id": "A-02", "x_coords": [5, 15], "y_coords": [10, 20], "is_valid": False},
    {"id": "B-01", "x_coords": [10, 20], "y_coords": [5, 10], "is_valid": True},
    {"id": "C-01", "x_coords": [0, 5], "y_coords": [0, 2], "is_valid": True},
]

filter_valid_records = lambda input_data: list(filter(lambda rec: rec["is_valid"], input_data))
calculate_area = lambda input_data: list(
        map(lambda rec: (rec["x_coords"][1] - rec["x_coords"][0])* (rec["y_coords"][1] - rec["y_coords"][0]), 
            input_data
        )
    )

def process_data(data, transformer):
    return transformer(data)


#   Exercise 4: Recursive Processing of Hierarchical Systems
# Objective: To solve a problem using recursion, a pattern where a function calls itself to break a 
# problem down into smaller, similar sub-problems.
system_architecture = {
    "DataIngest": {
        "SourceConnectors": {
            "PostgreSQL": None,
            "S3Bucket": None,
        },
        "Validator": None
    },
    "ProcessingEngine": {
        "TransformationCore": {
            "Geometric": None,
            "Temporal": None
        },
        "Cache": None
    },
    "API": None
}

def ping_system(system_node, path=""):
    print(path)
    keys = len(system_node.keys())
    for step, (key, value) in enumerate(system_node.items()):
        if not value:
            print(f"{path}.{key}")
            if step == keys - 1: return
        else: ping_system(value, path+f".{key}")


#   Hardcore Combined Problem: Generic, Multi-Stage Data Pipeline Executor
# Objective: To integrate all concepts from this chunk (def, return, all parameter types, scope, 
# lambda, higher-order functions, and recursion) to build a meaningful and complex algorithm. This 
# problem requires you to leverage each concept for a specific simplification it enables.

# Raw data from a simulated planetary observation satellite
observations = [
    {"id": 1, "type": "SPECTRAL", "data": {"band1": 0.5, "band2": 0.7}, "valid": True},
    {"id": 2, "type": "THERMAL", "data": 95.4, "valid": False},
    {"id": 3, "type": "SPATIAL", "data": {"points": [(1,1), (2,2)]}, "valid": True},
    {"id": 4, "type": "SPECTRAL", "data": {"band1": 0.4, "nested_data": {"sub_band": 0.9}}, "valid": True}
]
# State object to be managed during the pipeline execution
pipeline_state = {"errors": 0, "processed_count": 0}
# --- Pipeline Helper Functions (to be used in stages) ---
def flatten_nested_data(record):
    """Recursively flattens a dictionary."""
    flat_record = {}
    def _flatten(obj, name=''):
        if type(obj) is dict:
            for key, value in obj.items():
                _flatten(value, name + key + '_')
        else:
            flat_record[name[:-1]] = obj
    _flatten(record)
    return flat_record
def add_metadata(record, **kwargs):
    """Adds metadata to a record."""
    record.update(kwargs)
    return record
pipeline_stages = [
    {
        "name": "Flatten Spectral Data",
        "function": flatten_nested_data,
        "apply_if": lambda rec: rec.get("type") == "SPECTRAL" and isinstance(rec.get("data"), dict)
    },
    {
        "name": "Add Observer Metadata",
        "function": add_metadata,
        "kwargs": {"observer": "N.A.C.B.", "system": "AlephOne"}
    }
]
def run_pipeline(data_records, stages, global_state):
    for record in data_records:
        if not record["valid"]: 
            global_state["errors"] += 1
            return
        for stage in stages:
            function_to_run = stage["function"]
            if "apply_if" in stage:
                anonymous = stage["apply_if"]
                if not anonymous(record): continue
                kwargs = stage.get("kwargs", {})
                record = function_to_run(record, **kwargs) if kwargs else function_to_run(record)
        global_state["processed_count"] += 1
    return data_records


if __name__ == "__main__":
    # Exercise 1
    # normalize_record(record_1)
    # normalize_record(record_2)
    # Exercise 2
    # log_event("Message 1", *log_entry_1, **metadata_1)
    # log_event("Message 2", *log_entry_2, **metadata_2)
    # logging.info(f"Final ERROR COUNT: {ERROR_COUNT}")
    # Exercise 3
    # valid_records = process_data(cadastral_data, filter_valid_records)
    # logging.info(f"Cadastral valid records: {valid_records}")
    # valid_areas = process_data(valid_records, calculate_area)
    # logging.info(f"Cadastral valid areas: {valid_areas}")
    # Exercise 4
    # ping_system(system_architecture)
    run_pipeline(observations, pipeline_stages, pipeline_state)
    print(f"The observations are {observations}")
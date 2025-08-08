## Chunk 6: Python Error Handling

### Exercise 1: Basic Exception Handling

**Task:** Write a Python function `safe_to_float_converter` that takes a list of strings. The function should iterate through the list, attempt to convert each string to a float, and append the result to a new list. If a `ValueError` occurs during conversion, the function should append the float `0.0` to the results list instead of crashing.

**Artificial Data:**
```python
str_data = ["10.5", "20.2", "not_a_number", "7", "-5.88", "3.14e-2"]
```

**Software Engineering Principle:** Robustness. A function should gracefully handle predictable invalid inputs without terminating the entire program.

**Source:** [Python Tutorial: 8.3. Handling Exceptions](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)

---

### Exercise 2: Handling Multiple Specific Exceptions and the `else` Clause

**Task:** Write a function `calculate_ratios` that takes a list of tuples. Each tuple contains a numerator and a denominator. The function should iterate through the list and attempt to perform the division.
- If the division is successful, an `else` block should print the result in the format `Success: {result}`.
- It must handle `TypeError` if a denominator is not a number, printing `Error: Non-numeric denominator '{value}' found.`.
- It must handle `ZeroDivisionError` if a denominator is zero, printing `Error: Division by zero attempted.`.
- The function should continue processing the entire list despite any errors.

**Artificial Data:**
```python
division_tasks = [(10, 2), (5, 0), (8, "four"), (15, 3), (20, 5.0)]
```

**Software Engineering Principle:** Specificity and Clear Feedback. Handling distinct error types separately allows for more precise error reporting and recovery logic. The `else` clause ensures that success-dependent code does not run in an exception path.

**Source:** [Python Tutorial: 8.3. Handling Exceptions](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)

---

### Exercise 3: User-Defined Exceptions and `raise`

**Task:** Create a custom exception class named `DataOutOfRangeError` that inherits from `ValueError`. Then, write a function `validate_atmospheric_pressure` that accepts a pressure value in kilopascals (kPa). The valid range for Earth's sea-level pressure is between 87 kPa and 109 kPa. If the value is outside this range, the function must `raise` a `DataOutOfRangeError` with a descriptive message. The calling code should use a `try...except` block to catch this specific error and print the error message.

**Artificial Data:**
```python
pressure_readings = [101.3, 99.8, 112.5, 85.0, 105.7]
```

**Software Engineering Principle:** Abstraction and Domain Modeling. Custom exceptions make the program's error conditions explicit and self-documenting, aligning the code with the problem domain's specific rules.

**Source:** [Python Tutorial: 8.4. Raising Exceptions](https://docs.python.org/3/tutorial/errors.html#raising-exceptions), [8.6. User-defined Exceptions](https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions)

---

### Exercise 4: The `finally` Clause and Resource Management

**Task:** Simulate processing a temporary data buffer. Create a mock class `DataBuffer` with `open()`, `process()`, and `close()` methods, along with an `is_closed` boolean attribute. The `process` method should raise a `RuntimeError` if the data inside is marked as "corrupt". Write a function `process_data_buffer` that creates an instance of `DataBuffer`, opens it, and processes it within a `try` block. A `finally` block must ensure the buffer's `close()` method is always called, whether processing succeeds or fails. Verify this behavior with both clean and corrupt data.

**Artificial Data (Mock Class):**
```python
class DataBuffer:
    def __init__(self, data):
        self._data = data
        self.is_closed = True
        print("Buffer created.")

    def open(self):
        self.is_closed = False
        print("Buffer opened.")

    def process(self):
        print("Processing data...")
        if "corrupt" in self._data:
            raise RuntimeError("Data corruption detected!")
        print("Data processed successfully.")

    def close(self):
        self.is_closed = True
        print("Buffer closed.")

clean_buffer_data = "clean_data_stream"
corrupt_buffer_data = "corrupt_data_stream"
```

**Software Engineering Principle:** Resource Safety. The `finally` clause guarantees that critical cleanup logic, like closing files, network connections, or releasing locks, is executed, preventing resource leaks.

**Source:** [Python Tutorial: 8.7. Defining Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions)

---

### Exercise 5: Exception Chaining and Adding Contextual Notes

**Task:** You are writing a configuration loader. Create a custom `ConfigError` exception. Write a function `get_db_port` that takes a config dictionary. The function attempts to access the 'database' section and then its 'port' key.
- If a `KeyError` occurs, catch it and `raise` a new `ConfigError('Configuration key missing') from e`.
- If the port value cannot be converted to an integer, catch the `ValueError`, add a note to the exception using `e.add_note(f"Invalid port value found: '{port_val}'")`, and re-raise the original `ValueError`.

**Artificial Data:**
```python
configs = [
    {'database': {'host': 'localhost', 'port': 5432}},
    {'database': {'host': 'localhost'}}, # Missing port key
    {'database': {'host': 'localhost', 'port': 'bad_port'}} # Invalid port value
]
```

**Software Engineering Principle:** Debuggability and Maintainability. Exception chaining (`raise from`) preserves the root cause of an error, while adding notes (`add_note`) enriches the exception with runtime context, making debugging complex systems significantly easier.

**Source:** [Python Tutorial: 8.5. Exception Chaining](https://docs.python.org/3/tutorial/errors.html#exception-chaining), [8.10. Enriching Exceptions with Notes](https://docs.python.org/3/tutorial/errors.html#enriching-exceptions-with-notes)

---

### Hardcore Combined Problem: Resilient Geospatial Data Aggregation Pipeline

**Context:** Your task is to build a fault-tolerant pipeline that processes geospatial records from multiple, potentially unreliable API endpoints. The pipeline must attempt to process every record from every source, aggregate all failures, and ensure all resources are cleaned up correctly.

**Task:**
1.  **Define Custom Exceptions:**
    -   `APIConnectionError(Exception)`: For network-related issues.
    -   `DataParsingError(ValueError)`: For malformed JSON or data structure issues.
    -   `ValidationRuleError(ValueError)`: For records that fail domain-specific validation.

2.  **Mock Components:**
    -   A function `fetch_data(endpoint)`: Takes a URL string. It should return a JSON string for valid endpoints and raise an `APIConnectionError` for "api/unreachable".
    -   A mock `DatabaseConnection` class: Must have `__enter__` and `__exit__` methods (to be used with a `with` statement) that print "DB connection opened." and "DB connection closed." respectively. It should also have a `write(record)` method.

3.  **Algorithm (`run_pipeline` function):**
    -   The function takes a list of API endpoints.
    -   It must use a `with` statement to manage the `DatabaseConnection`.
    -   It initializes an empty list, `failures`, to collect all exceptions.
    -   It iterates through each endpoint. For each one:
        a.  It uses an inner `try...except` block to handle the entire fetch-parse-validate-write sequence for that endpoint.
        b.  **Fetch:** Call `fetch_data`. If it fails, add a note to the exception indicating the failed endpoint, and append it to `failures`.
        c.  **Parse:** Try to parse the fetched JSON. If a `json.JSONDecodeError` occurs, `raise` a `DataParsingError` `from` the original exception, add a note with the endpoint, and append it to `failures`.
        d.  **Validate:** The parsed record must be a dictionary containing a `'geometry'` key with a `'type'` of "Point" and a `'coordinates'` list of exactly two numbers. If not, raise a `ValidationRuleError` with a descriptive message, add a note, and append it.
        e.  **Write:** If all previous steps succeed, write the record to the database.
    -   After the loop, if the `failures` list is not empty, `raise` an `ExceptionGroup("Pipeline encountered one or more errors", failures)`.

4.  **Caller:** The top-level calling code should catch the `ExceptionGroup` and print out the details of each collected exception to demonstrate a full error report.

**Artificial Data:**
```python
api_endpoints = [
    "api/source1",
    "api/unreachable",
    "api/source2",
    "api/source3"
]

# Mock responses for fetch_data(endpoint)
mock_api_responses = {
    "api/source1": '{"id": 1, "geometry": {"type": "Point", "coordinates": [-74.0060, 40.7128]}}',
    "api/source2": '{"id": 2, "geometry": "invalid_structure"}', # Will cause DataParsingError on access
    "api/source3": '{"id": 3, "geometry": {"type": "LineString", "coordinates": [[-74, 40], [-73, 41]]}}' # Will cause ValidationRuleError
}
```

**Software Engineering Principles:** Resilience, Fault Tolerance, and Observability. This algorithm exemplifies a robust system that does not fail at the first sign of trouble. By collecting and grouping exceptions, it provides a complete diagnostic report, which is invaluable for monitoring and debugging distributed or complex data processing workflows. The use of `with` for resource management and `raise from` for causality tracing represents state-of-the-art error handling practice.

**Source:** All sections from [Python Tutorial: Chapter 8. Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html), with a special focus on [8.9. Raising and Handling Multiple Unrelated Exceptions](https://docs.python.org/3/tutorial/errors.html#raising-and-handling-multiple-unrelated-exceptions).
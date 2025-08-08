# **Python Modules and Packages**

These exercises will simulate building the components of a miniature data utility toolkit, a task that directly benefits from modular, scalable design.

---

## **Exercise 1: The Atomic Unit - A Single Utility Module**

This exercise focuses on the most fundamental concept: encapsulating reusable logic into a single file (a module) and using it in another script. This directly addresses the concept of **module creation** and the **namespacing pattern**.

**Objective:** Create a module with utility functions for basic data validation. This mirrors your work in creating an "automated quality control system."

*   **Key Skills:** Structuring code into modules, using standard library tools.
*   **Concepts:** Module creation (`.py` files), importing with `import`.
*   **Pattern:** Namespacing (avoiding naming conflicts).
*   **Relationship:** You will be encapsulating functions (Chunk 3) that operate on primitive and collection types (Chunk 1) using control structures (Chunk 2).

**Problem:**

1.  Create a file named `validators.py`. Inside this file, define two functions:
    *   `is_valid_id(item: str) -> bool`: Returns `True` if the input string `item` contains only numeric characters.
    *   `has_required_keys(data: dict, keys: list) -> bool`: Returns `True` if the dictionary `data` contains all keys specified in the `keys` list.
2.  Create a second file named `main_app.py`.
3.  In `main_app.py`, import the `validators` module.
4.  Using the provided artificial data, use the functions from the `validators` module to check the data and print the results.

**Artificial Data (for `main_app.py`):**

```python
 main_app.py (partial)
RECORDS = [
    {'id': '1024', 'user': 'nicolas', 'access_level': 'admin'},
    {'id': '10a25', 'user': 'castelblanco', 'access_level': 'user'},
    {'id': '2048', 'user': 'architect'},  Missing 'access_level'
]
REQUIRED_KEYS = ['id', 'user', 'access_level']
```

**Implementation Guidance:**

**`validators.py`:**
```python
 validators.py
 A module for data validation functions.

def is_valid_id(item: str) -> bool:
    """Checks if a string represents a valid numeric ID."""
    return item.isnumeric()

def has_required_keys(data: dict, keys: list) -> bool:
    """Checks if a dictionary contains all required keys."""
    return all(key in data for key in keys)
```

**`main_app.py`:**
```python
 main_app.py
 Main script to process records using the validators module.

import validators  The core of this exercise

RECORDS = [
    {'id': '1024', 'user': 'nicolas', 'access_level': 'admin'},
    {'id': '10a25', 'user': 'castelblanco', 'access_level': 'user'},
    {'id': '2048', 'user': 'architect'},
]
REQUIRED_KEYS = ['id', 'user', 'access_level']

print("--- Running Data Validation ---")
for i, record in enumerate(RECORDS):
    print(f"\nRecord {i+1}: {record}")
    
     Using the namespaced functions
    id_check = validators.is_valid_id(record.get('id', ''))
    keys_check = validators.has_required_keys(record, REQUIRED_KEYS)
    
    print(f"  - Is ID valid? {id_check}")
    print(f"  - Has all required keys? {keys_check}")
```

**Software Engineering Principles:**

*   **Modifiability & Reusability:** The `validators` module can be reused across any number of projects. If you need to change the logic for ID validation, you only need to modify `validators.py`, and all applications that import it will get the update. This is a core tenet of scalable systems.
*   **Testability:** The functions in `validators.py` are "pure"—they take input and produce output without side effects, making them trivial to unit test in isolation.

**Source Connection:**

*   **Python Official Documentation: [6. Modules](https://docs.python.org/3/tutorial/modules.html)**: The first page of this chapter directly explains how a file becomes a module and how to import it, which is the exact theory needed to solve this problem.

---

## **Exercise 2: Building a Hierarchical Package**

This exercise moves from a single module to a package, introducing hierarchy and structure. It addresses **package creation** and the use of `__init__.py`.

**Objective:** Organize the validation logic and a new set of "processing" utilities into a structured package. This simulates the initial architecture of a larger system

*   **Key Skills:** Structuring code into modules, building a small package.
*   **Concepts:** Packages (directories with `__init__.py`), hierarchical organization.
*   **Pattern:** Relative imports (will be explored in the hardcore problem).
*   **Relationship:** This is a direct extension of Exercise 1, organizing modules (which contain functions) into a scalable directory structure.

**Problem:**

1.  Create the following directory structure:
    ```
    geotool/
    ├── __init__.py
    ├── validators/
    │   ├── __init__.py
    │   └── schema.py
    └── processors/
        ├── __init__.py
        └── converter.py
    ```
2.  Move the validation logic from Exercise 1 into `geotool/validators/schema.py`. Rename the functions to be more domain-specific: `is_valid_polygon_id` and `has_required_fields`.
3.  In `geotool/processors/converter.py`, create a function `wkt_to_coords(wkt: str) -> dict` that takes a mock "Well-Known Text" string (e.g., `'POLYGON((x1 y1, x2 y2))'`) and returns a dictionary (e.g., `{'type': 'Polygon', 'coordinates': [[x1, y1], [x2, y2]]}`). This is a simplified transformation.
4.  Leave all `__init__.py` files empty. Their presence is what defines the packages.
5.  Create a `main_app_2.py` outside the `geotool` directory that imports and uses functions from both `geotool.validators.schema` and `geotool.processors.converter`.

**Artificial Data (for `main_app_2.py`):**

```python
 main_app_2.py (partial)
POLYGON_RECORD = {
    'id': '500123',
    'fields': ['id', 'owner', 'geometry'],
    'geometry': 'POLYGON((30 10, 40 40, 20 40, 10 20, 30 10))'
}
REQUIRED_FIELDS = ['id', 'geometry']
```

**Implementation Guidance:**

*   **File Structure:** Use your terminal or editor to create the directories and empty `__init__.py` files.
*   **`geotool/validators/schema.py`**: Contains your validation functions.
*   **`geotool/processors/converter.py`**: Contains the `wkt_to_coords` function.
*   **`main_app_2.py`**:

```python
 main_app_2.py
from geotool.validators import schema
from geotool.processors import converter

POLYGON_RECORD = {
    'id': '500123',
    'fields': ['id', 'owner', 'geometry'],
    'geometry': 'POLYGON((30 10, 40 40, 20 40, 10 20, 30 10))'
}
REQUIRED_FIELDS = ['id', 'geometry']

print("--- Processing Geospatial Record ---")
print(f"Record: {POLYGON_RECORD['id']}")

 Use the structured package
is_valid = schema.has_required_fields(POLYGON_RECORD, REQUIRED_FIELDS)
print(f"  - Record has required fields? {is_valid}")

if is_valid:
    coords = converter.wkt_to_coords(POLYGON_RECORD['geometry'])
    print(f"  - Converted Coords: {coords}")
```

**Software Engineering Principles:**

*   **Scalability:** This structure is highly scalable. You can add new validators (e.g., `crs.py` for coordinate reference systems) or new processors (e.g., `reproject.py`) without affecting existing code. This separation of concerns is critical for large systems.
*   **Modifiability:** If the WKT parsing logic needs to be improved, you only touch `converter.py`. The rest of the system is decoupled from that specific implementation.

**Source Connection:**

*   **Python Official Documentation: [6.4. Packages](https://docs.python.org/3/tutorial/modules.html#packages)**: This section explicitly details how directories with `__init__.py` are treated as packages and how to import submodules using the `package.submodule` syntax.
*   **Real Python: [Python Modules and Packages: An Introduction](https://realpython.com/python-modules-packages/)**: Provides a more narrative explanation of the *why* behind packages, which complements the official documentation.

---

## **Hardcore Combined Problem: A Foundational Data Pipeline Orchestrator**

This problem combines all concepts from Chunk 4 with previous chunks to build a meaningful algorithm that reflects your experience. It forces the use of multiple modules, standard library utilities, and package structuring to solve a complex, multi-step problem.

**Objective:** Create a command-line tool that scans a directory for mock geospatial data files (`.csv`), validates each file's structure and content using your `geotool` package, and generates a summary report.

**The Orchestrator will:**
1.  Take a directory path as a command-line argument (`sys.argv`).
2.  Scan the directory for files ending in `.csv` (`os` module).
3.  For each CSV, read its rows (standard `csv` module).
4.  Use the `geotool` package to perform validation on each row:
    *   A row must be a dictionary with the required headers (`geotool.validators.schema`).
    *   A row's `wkt` field must contain a parseable geometry (`geotool.processors.converter`).
5.  Use **module-level constants** to define configuration (e.g., required headers).
6.  Use **relative imports** within the package to make modules aware of each other.
7.  Generate a `report.txt` summarizing how many files were processed, how many rows were valid, and how many were invalid, with reasons.

**Expanded `geotool` Package Structure:**

```
geotool/
├── __init__.py
├── config.py              NEW: Module for constants
├── validators/
│   ├── __init__.py
│   └── schema.py
└── processors/
    ├── __init__.py
    └── converter.py
    └── pipeline.py          NEW: The main orchestrator logic
```

**Artificial Data (create a `data/` directory):**

`data/region_A.csv`:
```csv
id,owner,wkt
101,city,"POLYGON((0 0, 10 0, 10 10, 0 10, 0 0))"
102,private,"POLYGON((20 20, 30 20, 30 30, 20 30, 20 20))"
```

`data/region_B.csv`:
```csv
id,owner,wkt
201,state,"POLYGON((5 5, 6 5, 6 6, 5 6, 5 5))"
202,federal,"INVALID_GEOMETRY"
203,city,"POLYGON((2 2, 3 2, 3 3, 2 3, 2 2))"
```

`data/metadata.txt` (This file should be ignored by the tool).

**Implementation Guidance:**

**1. `geotool/config.py` (Module-level Constants)**
```python
 geotool/config.py
REQUIRED_HEADERS = ['id', 'owner', 'wkt']
```

**2. `geotool/validators/schema.py` (Now uses the config)**
```python
 geotool/validators/schema.py
from .. import config   <-- RELATIVE IMPORT

def has_required_fields(row: dict) -> bool:
    """Checks if a data row has all required headers."""
    return all(header in row for header in config.REQUIRED_HEADERS)
```

**3. `geotool/processors/pipeline.py` (The Core Logic)**
```python
 geotool/processors/pipeline.py
import os
import csv
from ..validators import schema  <-- Relative imports
from . import converter         <--
from .. import config

def process_directory(path: str):
    report = {
        'files_processed': 0,
        'total_rows': 0,
        'valid_rows': 0,
        'invalid_rows': 0,
        'errors': []
    }

    for filename in os.listdir(path):
        if not filename.endswith('.csv'):
            continue
        
        report['files_processed'] += 1
        filepath = os.path.join(path, filename)

        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                report['total_rows'] += 1
                is_valid_schema = schema.has_required_fields(row)
                try:
                    converter.wkt_to_coords(row.get('wkt', ''))
                    is_valid_geom = True
                except (ValueError, IndexError):
                    is_valid_geom = False

                if is_valid_schema and is_valid_geom:
                    report['valid_rows'] += 1
                else:
                    report['invalid_rows'] += 1
                    error_msg = f"File: {filename}, Row: {i+2}, Reason: "
                    if not is_valid_schema:
                        error_msg += f"Missing headers. Expected {config.REQUIRED_HEADERS}."
                    elif not is_valid_geom:
                        error_msg += f"Invalid WKT geometry '{row.get('wkt', '')}'."
                    report['errors'].append(error_msg)

    generate_report(report)

def generate_report(report_data: dict):
    with open('report.txt', 'w') as f:
        f.write("--- Geospatial Data Quality Report ---\n")
        f.write(f"Files Processed: {report_data['files_processed']}\n")
        f.write(f"Total Rows Scanned: {report_data['total_rows']}\n")
        f.write(f"Valid Rows: {report_data['valid_rows']}\n")
        f.write(f"Invalid Rows: {report_data['invalid_rows']}\n")
        if report_data['errors']:
            f.write("\n--- Error Details ---\n")
            for error in report_data['errors']:
                f.write(f"- {error}\n")
    print("Report generated successfully at 'report.txt'.")

```

**4. `run_pipeline.py` (The entry point)**
```python
 run_pipeline.py
import sys
from geotool.processors import pipeline

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_pipeline.py <directory_path>")
        sys.exit(1)
        
    data_directory = sys.argv[1]
    pipeline.process_directory(data_directory)
```

**To Run:**
`python run_pipeline.py data`

**Solution Rationale & Connections:**

This solution is a microcosm of a real data engineering task and maximizes the utility of Chunk 4's concepts:

*   **Structure for Scalability:** The `geotool` package is now a true tool. Adding a new processing step (e.g., re-projection) is as simple as adding a `reproject.py` module in `processors`. This is the essence of a **scalable** and **modifiable** architecture.
*   **Centralized Configuration (`config.py`):** The `config.py` module demonstrates the **module-level constants pattern**. If the required headers change, you modify one file, not the functions that depend on it. This greatly improves maintainability.
*   **Intra-Package Communication (Relative Imports):** The use of `from .. import config` and `from . import converter` showcases the **relative import pattern**. This makes the package self-contained. It doesn't rely on the system's `PYTHONPATH` to find its own components, making it robust and portable. This is crucial for creating installable libraries.
*   **Leveraging the Standard Library (`os`, `sys`, `csv`):** This demonstrates the relationship between your own packages and Python's powerful standard library. You are not reinventing the wheel for file system access or CSV parsing; you are building your specialized logic on top of these reliable foundations. This addresses the **Reliability** principle.
*   **Integration of All Chunks:**
    *   **Chunk 4:** `os`, `sys`, package structure, relative imports, module constants.
    *   **Chunk 3 (Functions):** The entire system is orchestrated by calling functions like `process_directory`, which in turn call validation and conversion functions.
    *   **Chunk 2 (Control Structures):** `for` loops iterate over files and rows; `if/else` logic directs the validation flow.
    *   **Chunk 1 (Data Types):** Dictionaries (`row`, `report`), lists (`errors`), strings (`filepath`, `error_msg`), and booleans (`is_valid_geom`) are the fundamental currency of the entire process.

**Source Connection:**

*   **Python Official Documentation: [6.4.2. Intra-package References](https://docs.python.org/3/tutorial/modules.html#intra-package-references)**: This section is the direct theoretical basis for using leading dots (`.` and `..`) to create self-contained packages that can resolve their own internal dependencies.
*   **Python Crash Course by Eric Matthes, Chapter 8**: This chapter provides practical, project-based examples of building and using modules, which aligns well with the hands-on nature of this hardcore problem.
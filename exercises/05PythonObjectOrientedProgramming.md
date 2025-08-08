### **Exercises: Chunk 5 - Python Object-Oriented Programming**

---

#### **Exercise 1: Foundational Class Design**

*   **Objective**: Create a basic class to represent a single data record, incorporating attributes and special methods `__init__` and `__str__`. This exercise establishes the fundamental structure of a class.
*   **Concepts**: Class definition, attributes, methods, `__init__`, `__str__`.
*   **Key Skills**: Designing a single class, using special methods.
*   **Artificial Data**:
    ```python
    record1_data = {'id': 'REC-001', 'source': 'Telespazio', 'value': 45.23, 'validated': False}
    record2_data = {'id': 'REC-002', 'source': 'IGAC', 'value': 78.1, 'validated': True}
    ```
*   **Task**:
    1.  Define a class named `DataRecord`.
    2.  In the `__init__` method, accept a dictionary as an argument. Initialize instance attributes `id`, `source`, `value`, and `validated` from this dictionary.
    3.  Implement the `__str__` method to return a human-readable string summarizing the record, for example: `"[REC-001 from Telespazio] Value: 45.23 (Validated: False)"`.
    4.  Create a method called `validate_record()` that sets the `validated` attribute to `True`.
    5.  Instantiate two `DataRecord` objects using the provided data. Print the objects before and after calling `validate_record()` on the first one to see the change.
*   **Software Engineering Principles**:
    *   **Modifiability**: The class is self-contained. If the structure of a record changes, you only need to update this class.
    *   **Testability**: The state of an instance (`validated` status) can be easily checked and modified through methods, making unit testing straightforward.
*   **Source Reference**:
    *   **Python Official Documentation (9.3. A First Look at Classes)**: Review this section for the fundamental syntax of class definitions, `__init__()`, and instance objects.
    *   **Real Python (How Do You Define a Class in Python?)**: Use this to understand the role of `__init__` as an initializer and `self` to refer to the instance.

---

#### **Exercise 2: Inheritance and Behavioral Specialization**

*   **Objective**: Model different types of data records using inheritance. Override a base class method to provide specialized behavior in a subclass and use `__eq__` to define object equality.
*   **Concepts**: Inheritance, method overriding, special method `__eq__`.
*   **Key Skills**: Designing class hierarchies, implementing inheritance.
*   **Artificial Data**:
    ```python
    geodata_raw = {'id': 'GEO-55A', 'source': 'Telespazio', 'value': (6.2, -75.5), 'validated': False, 'epsg_code': 4326}
    elevation_raw = {'id': 'ELEV-B2', 'source': 'IGAC', 'value': 1500.7, 'validated': True, 'vertical_datum': 'WGS84'}
    elevation_duplicate = {'id': 'ELEV-B2', 'source': 'IGAC', 'value': 1500.7, 'validated': True, 'vertical_datum': 'WGS84'}
    ```
*   **Task**:
    1.  Create a base class `BaseRecord` with an `__init__` that accepts `id`, `source`, and `value`.
    2.  In `BaseRecord`, define a method `get_record_type()` that returns `"Base Record"`.
    3.  Define an `__eq__` method in `BaseRecord` that considers two records equal if their `id` and `source` are identical.
    4.  Create two child classes, `GeospatialRecord` and `ElevationRecord`, that inherit from `BaseRecord`.
    5.  Extend the `__init__` method in both child classes using `super()` to also accept their specific attributes (`epsg_code` for `GeospatialRecord`, `vertical_datum` for `ElevationRecord`).
    6.  **Override** the `get_record_type()` method in each child class to return `"Geospatial Record"` and `"Elevation Record"` respectively.
    7.  Instantiate records from the raw data. Verify that `elevation_raw` and `elevation_duplicate` are considered equal using the `==` operator. Print the record type for each instance to show polymorphism in action.
*   **Software Engineering Principles**:
    *   **Scalability/Reusability**: You can easily introduce new record types (e.g., `CadastralRecord`) by inheriting from `BaseRecord`, reusing the common logic for ID, source, and equality.
*   **Source Reference**:
    *   **Python Official Documentation (9.5. Inheritance)**: This section covers the syntax for creating derived classes and overriding methods.
    *   **Real Python (How Do You Inherit From Another Class in Python?)**: Provides practical examples of parent/child classes and using `super()` to extend functionality.

---

#### **Exercise 3: Encapsulation and Controlled Access**

*   **Objective**: Protect the internal state of an object using encapsulation. Implement property decorators to create a controlled public interface for accessing and modifying "private" attributes.
*   **Concepts**: Encapsulation (`_attr`, `__attr`), `property` decorators.
*   **Key Skills**: Implementing encapsulation, using special methods for attribute access.
*   **Artificial Data**:
    ```python
    # A dictionary representing a system component with sensitive quality metrics
    component_data = {'name': 'PostgreSQL_DB', 'initial_q_score': 95.5}
    ```
*   **Task**:
    1.  Define a class `SystemComponent`. In its `__init__`, store the name publicly but the quality score as a "private" attribute (e.g., `__quality_score`).
    2.  Use the `@property` decorator to create a public getter for the quality score.
    3.  Use the `@quality_score.setter` decorator to create a public setter for the quality score. The setter logic must enforce a rule: the quality score cannot be set to a value less than 0 or greater than 100. If an invalid value is provided, it should raise a `ValueError`.
    4.  Instantiate a `SystemComponent` with the provided data.
    5.  Attempt to get the quality score and print it.
    6.  Attempt to set the quality score to a valid value (e.g., `98.0`) and an invalid value (e.g., `101.0`), catching the `ValueError` with a `try...except` block to prove the validation works.
*   **Software Engineering Principles**:
    *   **Reliability**: Encapsulation prevents direct, uncontrolled modification of the object's state, ensuring data integrity. The object maintains a valid state at all times.
*   **Source Reference**:
    *   **Python Official Documentation (9.6. Private Variables)**: Explains the concept of name mangling (`__spam`) as a limited mechanism for private members.
    *   **Real Python (Object-Oriented Programming (OOP) in Python)**: The broader article discusses encapsulation as a key pillar of OOP. While not showing property decorators in the free preview, the concept is central. For implementation, official Python docs on `@property` are the best reference.

---

#### **Exercise 4: Building Complex Objects with Composition**

*   **Objective**: Use composition to build a complex object from smaller, independent objects. This models "has-a" relationships, which are fundamental to system design.
*   **Concepts**: Composition.
*   **Key Skills**: Designing classes that contain instances of other classes.
*   **Artificial Data**:
    ```python
    # Use the SystemComponent class from the previous exercise
    db_component = SystemComponent({'name': 'PostgreSQL_DB', 'initial_q_score': 92.0})
    api_component = SystemComponent({'name': 'FastAPI_Service', 'initial_q_score': 98.5})
    qc_module = SystemComponent({'name': 'QC_Module', 'initial_q_score': 88.0})
    ```
*   **Task**:
    1.  Define a new class called `SystemBlueprint`.
    2.  The `__init__` method should accept a `name` for the blueprint and initialize an empty list to hold components (e.g., `self.components`).
    3.  Create a method `add_component(component)` that takes an instance of `SystemComponent` and adds it to the list.
    4.  Create a method `calculate_average_quality()` that iterates through the composed `SystemComponent` objects and returns their average quality score.
    5.  Implement the `__str__` method to print the blueprint's name and list the names of all its components.
    6.  Instantiate a `SystemBlueprint`. Add the three component instances (`db_component`, `api_component`, `qc_module`) to it.
    7.  Print the `SystemBlueprint` object and its average quality score.
*   **Software Engineering Principles**:
    *   **Modifiability/Scalability**: The `SystemBlueprint` is not tightly coupled to the components. You can change `SystemComponent` or add new component types without altering `SystemBlueprint`, as long as they adhere to the expected interface (having a `quality_score` property).
*   **Source Reference**:
    *   This pattern is a general OOP principle. In *Python Crash Course*, Chapter 9 covers "Instances as Attributes," which is the practical implementation of composition.

---

#### **Hardcore Combined Problem: Architecting a Polymorphic Data Processing Pipeline**

*   **Objective**: Integrate all concepts from this chunk (Classes, Inheritance, Encapsulation, Special Methods) and patterns (Polymorphism, Composition, ABCs) to build a flexible data processing pipeline. The solution should be an algorithm that leverages these OOP features to handle a complex task in a simple, scalable way.
*   **Scenario**: Your resume highlights revolutionizing data processing and creating quality control systems. This problem asks you to architect a system that validates a dataset using a series of configurable, polymorphic validation rules.
*   **Concepts & Patterns**: All from Chunk 5.
*   **Key Skills**: Designing class hierarchies, implementing encapsulation, using special methods, applying polymorphism and composition, and using ABCs for interfaces.
*   **Artificial Data**:
    ```python
    # A list of dictionaries, where each is a data record. Some are valid, some are not.
    dataset = [
        {'id': 1, 'type': 'geospatial', 'coords': (4.6, -74.0), 'value': 100}, # Valid
        {'id': 2, 'type': 'telemetry', 'coords': None, 'value': -50},        # Invalid value
        {'id': 3, 'type': 'geospatial', 'coords': (91.0, -74.0), 'value': 200}, # Invalid coords
        {'id': 4, 'type': 'generic', 'coords': None, 'value': 300}            # Missing type-specific check
    ]
    ```
*   **Task**:
    1.  **Define an Abstract Base Class**:
        *   Create an ABC named `ValidationRule` using the `abc` module.
        *   It should have an `__init__` that takes an error message string.
        *   Define an abstract method `@abstractmethod` called `is_valid(record)` that must be implemented by subclasses.

    2.  **Implement Concrete Rules (Inheritance & Polymorphism)**:
        *   Create three classes that inherit from `ValidationRule`:
            *   `ValuePositiveRule`: Checks if `record['value']` is greater than 0.
            *   `TypeKnownRule`: Checks if `record['type']` is one of `['geospatial', 'telemetry']`.
            *   `GeospatialCoordsRule`: Checks if `record['coords']` are valid latitude/longitude tuples (lat: -90 to 90, lon: -180 to 180). This rule should *only* apply if the record's type is `'geospatial'`.

    3.  **Create a Composed Validator (Composition & Encapsulation)**:
        *   Create a class named `DataValidator`.
        *   Its `__init__` should initialize a "private" list of rules (`self.__rules`).
        *   Create a public method `add_rule(rule)` to add an instance of a `ValidationRule` subclass to its list.
        *   Create a `validate_dataset(dataset)` method. This is the core algorithm. It should:
            *   Take a list of records (the dataset).
            *   Return a dictionary of `errors`, where keys are record IDs and values are a list of error messages from the rules that failed for that record.

    4.  **Execute the Pipeline**:
        *   Instantiate `DataValidator`.
        *   Instantiate and add all three validation rules to the validator.
        *   Call `validate_dataset` with the sample `dataset`.
        *   Print the resulting errors dictionary in a clean format. The output should correctly identify which rules failed for which records.

*   **Software Engineering Principles**:
    *   **All Principles**: This exercise touches on all of them. The ABC provides a **testable** and **modifiable** interface. Polymorphism allows the `DataValidator` to treat all rules the same, making it **scalable**. Composition allows the `DataValidator` to be configured with different rules, and Encapsulation protects its internal list of rules, ensuring **reliability**.
*   **Source Reference**:
    *   This problem requires a synthesis of knowledge from all provided resources. Key sections are the Python Docs on **Classes (9)**, **Inheritance (9.5)**, **Private Variables (9.6)**, and the concepts of **Polymorphism and Abstraction** from the Real Python article. You will also need to reference the `abc` module from Python's standard library.
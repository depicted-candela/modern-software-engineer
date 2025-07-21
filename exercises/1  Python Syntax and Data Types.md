# **Part 1: Exercises for Chunk 1: Python Syntax and Data Types**

These exercises will guide you from basic data manipulation to complex, single-line transformations using comprehensions, ensuring you master the core building blocks of Python.

---

## **Exercise 1: Primitive Types, Operators, and Type Conversion**

*   **Objective:** This exercise focuses on manipulating primitive data types (`int`, `float`, `str`) using arithmetic operators. It will test your ability to perform type conversions, a fundamental skill for handling raw data.
*   **Problem Description:** You have a list of daily sales figures that have been recorded as strings. Your task is to calculate the total sales and the average daily sales.
*   **Artificial Data:**
    ```python
    daily_sales_str = ["150.50", "200", "99.99", "75", "300.10"]
    ```
*   **Task:**
    1.  Create a new list called `daily_sales_float` by converting each string in `daily_sales_str` to a `float`.
    2.  Calculate the sum of all sales and store it in a variable called `total_sales`.
    3.  Calculate the average sales and store it in a variable called `average_sales`.
    4.  Print the results in a formatted string: `Total sales: $XXXX.XX, Average sales: $XXX.XX`.
*   **Entities Covered:**
    *   **Concepts**: `int`, `float`, `str`, `list`, arithmetic operators (`+`, `/`), type conversions (`float()`, `str()`).
    *   **Patterns**: F-string formatting.
    *   **Relationships**: This exercise demonstrates that raw data, often represented as strings, must be converted to the appropriate numeric type before mathematical operations can be performed.
*   **Software Engineering Principle:** **Reliability**. The code must reliably handle numbers represented as both integers (`"200"`) and floats (`"150.50"`) within strings, which is a common real-world scenario.
*   **Source & Theory:** This task is based on the concepts described in Real Python's "Basic Data Types" guide and the official Python documentation. Real Python clarifies that Python's data types are classes, and using `float()` is a way to construct a float object from another type, like a string. The official documentation further details the use of arithmetic operators like `+` and `/`.

---

## **Exercise 2: Collection Types and Basic Operations**

*   **Objective:** To practice structuring raw data into a more efficient collection type (`dictionary`) for rapid, key-based lookups. This addresses the specified `Exercise Context` of creating dictionaries from data.
*   **Artificial Data:**
    ```python
    user_data = [(101, "aqua_dev"), (102, "beta_user"), (103, "gamma_guru")]
    ```
*   **Task:**
    1.  Convert the `user_data` list of tuples into a dictionary named `user_mapping`, where the user ID (the first element of the tuple) is the key and the username (the second element) is the value.
    2.  Directly access and print the username for the user with ID `102`.
    3.  Add a new user, ID `104` with username `"delta_debug"`, to the dictionary.
*   **Entities Covered:**
    *   **Concepts**: `lists`, `tuples`, `dictionaries`, variable assignment.
    *   **Patterns**: Collection operations (dictionary creation, key-based lookup, and updating).
    *   **Relationships**: This problem shows the practical advantage of using a dictionary for direct data retrieval (`user_mapping[102]`) over iterating through a list to find a specific user.
*   **Software Engineering Principle:** **Scalability**. While iterating a 3-item list is fast, this pattern of using dictionaries for lookups is far more scalable. Dictionaries offer O(1) average time complexity for lookups, which is critical when dealing with thousands or millions of users.
*   **Source & Theory:** The Python Official Documentation introduces lists as a versatile, mutable sequence. This exercise takes that a step further by converting a list into a dictionary, a key-value mapping that is highly optimized for data retrieval by a unique identifier. The methods for list manipulation are detailed at W3Schools.

---

## **Exercise 3: Advanced String and List Manipulation**

*   **Objective:** To clean and reformat inconsistently formatted string data and present it in a standardized way, using string methods and f-strings.
*   **Artificial Data:**
    ```python
    participants = ["  alex thorn  ", "  JANE DOE", " betty Crocker  "]
    ```
*   **Task:**
    1.  Create a new list called `cleaned_participants`.
    2.  For each name in the `participants` list, apply string methods to remove all leading/trailing whitespace and convert the name to title case (e.g., "Alex Thorn").
    3.  Add the cleaned name to the `cleaned_participants` list.
    4.  Finally, loop through the `cleaned_participants` list and print the result using an f-string: `Participant: [Cleaned Name]`.
*   **Entities Covered:**
    *   **Concepts**: `str`, `list`, string methods.
    *   **Patterns**: String manipulation (`strip()`, `title()`), list appending, f-strings for formatting.
    *   **Relationships**: This task highlights a common data processing pipeline: raw data often requires cleaning (string manipulation) as a preliminary step before it can be effectively used or displayed (iteration and printing).
*   **Software Engineering Principle:** **Modifiability**. Using f-strings (e.g., `f"Participant: {name}"`) makes the output string easier to read and modify in the future compared to older methods like manual string concatenation.
*   **Source & Theory:** This exercise directly applies the methods found in the W3Schools "Python String Methods" resource. Specifically, `strip()` is used for removing extraneous whitespace and `title()` is used to enforce consistent capitalization. Chaining these methods (`name.strip().title()`) is a powerful and common pattern for writing concise data cleaning code.

---

## **Exercise 4 (Layered Combination): Comprehensions and Mixed-Type Data**

*   **Objective:** To use Python's powerful comprehension syntax to filter and transform a complex, mixed-type data structure in a single, expressive line of code.
*   **Artificial Data:**
    ```python
    inventory = [
        {'name': 'Laptop', 'price': '1200.00', 'in_stock': True},
        {'name': 'Mouse', 'price': 80.50, 'in_stock': False},
        {'name': 'Keyboard', 'price': '150', 'in_stock': True},
        {'name': 'Webcam', 'price': 105.99, 'in_stock': True}
    ]
    ```*   **Task:**
    Using a **set comprehension**, create a `set` named `premium_products_in_stock` that contains the names of all products that are currently `in_stock` AND have a price greater than $100.00.
*   **Entities Covered:**
    *   **Concepts**: `list`, `dict`, `set`, `float`, `str`, `bool`, comparison operators (`>`), logical operators (`and`).
    *   **Patterns**: Set comprehension, type conversion within a comprehension.
    *   **Relationships**: This problem synthesizes all the core concepts of Chunk 1. It requires you to unpack data from a nested structure, apply conditional logic based on multiple keys, perform on-the-fly type conversion (`float()`), and store the final, unique results in a `set`.
*   **Software Engineering Principle:** **Efficiency**. Comprehensions are a hallmark of Pythonic code. They are often more efficient and always more concise than writing an explicit `for` loop to build a new collection, demonstrating your fluency in the language.
*   **Source & Theory:** This exercise challenges you to apply the comprehension syntax mentioned in the Python Official Documentation and Real Python's guide. To solve it, you must combine this pattern with dictionary data access (e.g., `item['key']`), conditional logic (`if item['in_stock']`), and robust type conversion (`float(item['price'])`), proving a layered mastery of the chunk's topics.

***

# **Part 2: Hardcore Combined Problem for Chunk 2: Python Control Structures**

*   **Objective:** To integrate all concepts from Chunk 2 (`if/elif/else`, `for`, `while`, `break`, `continue`, `enumerate`, `zip`, and nested structures) to solve a single, complex data validation and processing problem.
*   **Problem Description:** You are in charge of an automated system that processes a queue of incoming server requests. Each request must be validated against several criteria: it must be from a recognized IP, it must not be on a denylist, and you can only process a certain number of `high_priority` requests per batch.
*   **Artificial Data:**
    ```python
    request_queue = [
        ('192.168.1.5', 'read', 'high_priority'),
        ('10.0.0.3', 'write', 'low_priority'),
        ('192.168.1.5', 'delete', 'high_priority'),  Duplicate IP, should be skipped
        ('203.0.113.1', 'read', 'low_priority'),   Unrecognized IP
        ('10.0.0.2', 'connect', 'high_priority'),
        ('10.0.0.4', 'read', 'low_priority'),
    ]
    recognized_ips = {'192.168.1.5', '10.0.0.1', '10.0.0.2', '10.0.0.3'}
    denylist_ips = {'10.0.0.4'}
    priority_quota = 2
    ```
*   **Task:**
    Write a script that processes the `request_queue`.
    1.  Initialize `processed_ips = set()` to track duplicates, `priority_requests_processed = 0`, and `report = []`.
    2.  Use a `for` loop with `enumerate` to iterate through the `request_queue` to get both a `step` number and the `(ip, action, priority)` tuple.
    3.  **Nested Control Flow:**
        *   **`continue`**: If the `ip` is in the `denylist_ips` OR if the `ip` has already been processed (is in `processed_ips`), print a "REJECTED" message and use `continue` to immediately move to the next request.
        *   **`if/else`**: If the `ip` is not in `recognized_ips`, print a "WARNING" message and skip to the next request with `continue`.
    4.  **`while` Loop and `break`**: If a request is `high_priority`:
        *   Use a `while priority_requests_processed < priority_quota:` loop. If the condition is met, increment `priority_requests_processed`, print a "PROCESSING PRIORITY" message, and `break` the `while` loop to proceed.
        *   If the quota is already met, print a "DEFERRED" message and `continue` to the next request in the outer `for` loop.
    5.  **Successful Processing & `zip`**: If a request passes all checks:
        *   Add the `ip` to the `processed_ips` set.
        *   Use `zip` to pair the `(ip, action, priority)` tuple with a list of `actions_to_log = ["log_event", "validate_permissions", "execute_action"]`. Loop through the pairs and print each loggable action.
        *   Append a success string to your `report`.
    6.  **`else` on `for` loop**: After the `for` loop finishes naturally (without a `break`), print a final message: "Batch processing complete."
    7.  Print the final `report`.
*   **Entities Covered:**
    *   **Concepts**: `if/elif/else`, `for`, `while`, `break`, `continue`.
    *   **Patterns**: `Nested structures`, `iteration with enumerate()`, `combining zip() with for loops`.
    *   **Relationships**: This problem shows how control structures are the engine for implementing complex business logic, orchestrating the flow of operations based on multiple, interdependent conditions and data states.
*   **Software Engineering Principle:** **Reliability**. The script must robustly handle various failure modes (denylisted, duplicate, unrecognized IPs) without crashing, and it must strictly adhere to the processing quota for priority requests.
*   **Source & Theory:** This problem is a synthesis of the control flow tools detailed in the Python Official Documentation and Real Python. The core logic uses `if/elif/else` blocks for decision-making. Advanced patterns, including nested loops, the use of `continue` to manage flow, and the `else` clause on the `for` loop, are all concepts explained in the official documentation. The use of `enumerate()` and `zip()` to write cleaner, more Pythonic loops is also a key pattern from the official docs that this problem requires you to implement.
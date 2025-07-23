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
    ```
    *   **Task:**
    Using a **set comprehension**, create a `set` named `premium_products_in_stock` that contains the names of all products that are currently `in_stock` AND have a price greater than $100.00.
*   **Entities Covered:**
    *   **Concepts**: `list`, `dict`, `set`, `float`, `str`, `bool`, comparison operators (`>`), logical operators (`and`).
    *   **Patterns**: Set comprehension, type conversion within a comprehension.
    *   **Relationships**: This problem synthesizes all the core concepts of Chunk 1. It requires you to unpack data from a nested structure, apply conditional logic based on multiple keys, perform on-the-fly type conversion (`float()`), and store the final, unique results in a `set`.
*   **Software Engineering Principle:** **Efficiency**. Comprehensions are a hallmark of Pythonic code. They are often more efficient and always more concise than writing an explicit `for` loop to build a new collection, demonstrating your fluency in the language.
*   **Source & Theory:** This exercise challenges you to apply the comprehension syntax mentioned in the Python Official Documentation and Real Python's guide. To solve it, you must combine this pattern with dictionary data access (e.g., `item['key']`), conditional logic (`if item['in_stock']`), and robust type conversion (`float(item['price'])`), proving a layered mastery of the chunk's topics.

***

# **Part 2: Hardcore Combined Problem for Chunk 2: Control Structures**

*   **Objective:** To design and implement a "Log File Anomaly Detector" algorithm. This problem requires you to integrate and strategically apply **all** concepts, patterns, and relationships from Chunk 2 to solve a complex data processing and validation task. You must leverage each tool for its specific strengths to create a solution that is both robust and elegantly simple despite the complexity of the requirements.
*   **Concepts & Patterns to Combine**: `if/elif/else`, `for`, `while`, loop control statements (`break`, `continue`, `pass`), nested structures, iteration with `enumerate()`, combining `zip()`, and `ternary expressions`.

*   **Problem Description:**
    You are building an anomaly detection system that parses a stream of server log entries and correlates them with a parallel stream of system performance metrics. The system must identify potential security events, such as brute-force login attempts or resource exhaustion attacks. The log stream is noisy, and your algorithm's primary challenge is to intelligently filter, correlate, and detect complex patterns that span multiple log entries.

*   **Artificial Data:**
    ```python
    # A stream of log entries: (timestamp, level, message)
    log_stream = [
        (1668837600, 'INFO', 'User admin logged in successfully'),
        (1668837601, 'DEBUG', 'Database connection established'), # Should be ignored
        (1668837602, 'ERROR', 'Failed login attempt for user guest from IP 192.168.1.100'),
        (1668837603, 'ERROR', 'Failed login attempt for user guest from IP 192.168.1.100'),
        (1668837604, 'INFO', 'User alex logged in successfully'), # Breaks the consecutive error pattern
        (1668837605, 'ERROR', 'Failed login attempt for user guest from IP 192.168.1.100'),
        (1668837606, 'WARN', 'High CPU load detected'),
        (1668837607, 'ERROR', 'Service unavailable: connection timeout to payment_gateway'),
    ]

    # A parallel stream of system metrics: (timestamp, cpu_usage_percent, memory_usage_mb)
    system_metrics = [
        (1668837600, 10, 256),
        (1668837601, 12, 258),
        (1668837602, 15, 260),
        (1668837603, 18, 262),
        (1668837604, 13, 270),
        (1668837605, 25, 280),
        (1668837606, 95, 300), # Correlates with the 'High CPU load' warning
        (1668837607, 88, 290),
    ]
    
    # Configuration
    BRUTE_FORCE_THRESHOLD = 3 # Number of consecutive failed logins from one IP to trigger an alert
    CPU_WARNING_THRESHOLD = 90
    ```

*   **Task: The Anomaly Detection Algorithm**
    Write a script that processes the `log_stream` and `system_metrics`.

    1.  Initialize necessary data structures: `incident_report = []` and `ip_fail_count = {}`.
    2.  Use a `for` loop that combines `zip` and `enumerate` to iterate over the `log_stream` and `system_metrics` simultaneously. This provides the index, the log entry, and the corresponding metric for each step, which is a massive simplification over manual indexing.
    3.  **Guard Clauses for Simplification**:
        *   At the top of your loop, check if the log level is 'DEBUG'. If it is, use the `pass` keyword to signify that we are intentionally taking no action. Then, use `continue` to immediately skip to the next log entry. This prevents cluttering your main logic with checks for irrelevant data.
    4.  **Leverage Ternary Expressions**:
        *   For each log, assign a `status` string. Use a **ternary expression** for conciseness: `status = 'CRITICAL' if log[1] == 'ERROR' else 'NORMAL'`.
    5.  **Complex Nested Logic with `while` for Pattern Detection**:
        *   If a log entry is an 'ERROR' indicating a `'Failed login'`, extract the IP address.
        *   Increment the failure count for that IP in your `ip_fail_count` dictionary.
        *   **Here is the core pattern detection**: If the failure count for an IP reaches `BRUTE_FORCE_THRESHOLD`, initiate a **`while` loop** to look *ahead* in the log stream to confirm if this is part of a sustained attack.
            *   The `while` loop should continue as long as the next few logs are *also* failed logins from the same IP. This is a condition-based check that a `for` loop cannot easily handle.
            *   Use `break` to exit the `while` loop immediately if you encounter a log that is *not* a failed login from that IP, as this breaks the attack pattern.
            *   If the `while` loop completes its checks and confirms a sustained attack, add a detailed "BRUTE-FORCE ALERT" to your `incident_report`.
    6.  **Correlating Data with `zip`**:
        *   If a log entry is a 'WARN', check the corresponding `cpu_usage_percent` from the `system_metrics` tuple that `zip` provided for that iteration. If the CPU usage is above `CPU_WARNING_THRESHOLD`, add a "RESOURCE EXHAUSTION ALERT" to the report.
    7.  **`for-else` Clause**:
        *   Attach an `else` block to your main `for` loop. This block will only execute if the `for` loop completes without being interrupted by a `break`. Print a message like "System Scan Complete. All logs processed." This confirms the integrity of the completed scan.

*   **Why This Design Maximizes Simplification:**
    *   **The Problem is Complex**: Correlating parallel data streams and detecting stateful, multi-entry patterns is a genuinely complex task.
    *   **`for/zip/enumerate` as a Simplifier**: This combination turns three separate, error-prone loops or manual index tracking into a single, elegant iteration statement. It provides all necessary data (`index`, `log`, `metric`) contextually.
    *   **`continue` as a Simplifier**: The guard clause `if level == 'DEBUG': continue` radically cleans up the code. Without it, all subsequent logic would need to be nested inside an `if level != 'DEBUG':` block.
    -   **`while` for the Right Reason**: The nested `while` loop is not just for show; it solves a problem that is difficult for the main `for` loop: looking ahead based on a *dynamic condition* (are the *next N* logs also errors?) rather than just iterating a fixed sequence.
    -   **`break` for Efficiency**: Breaking out of the `while` loop is the most efficient way to stop checking for a pattern once it's been invalidated.
    - **Ternary for Conciseness**: Using a ternary expression to set the `status` is cleaner and more readable than a full `if/else` block for a simple assignment.
    -   **`pass` for Clarity**: Using `pass` makes it explicit to other developers that the 'DEBUG' case was considered and intentionally ignored, not forgotten.

This enhanced problem forces a deep understanding of *when* and *why* to use each control structure, pushing you to write code that is not just correct, but is a model of algorithmic elegance and clarity.
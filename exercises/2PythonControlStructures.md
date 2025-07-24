The following exercises for **Chunk 2: Python Control Structures** are designed to reinforce the concepts, patterns, and their relationships with the foundational data types from Chunk 1. They emphasize not just *how* to use these structures, but *why* and *when* to use them for efficient, reliable, and modifiable code.

### **Exercises for Chunk 2: Python Control Structures**

These exercises are structured to build from simple logical branching to complex, nested iteration, culminating in a problem that synthesizes all concepts in a meaningful data processing algorithm.

---

### **Exercise 1: Conditional Data Validation and Categorization**

*   **Objective**: Use conditional statements (`if`, `elif`, `else`) to validate and categorize raw data, a common task in data cleaning and preparation. This directly tests your ability to write conditional logic.
*   **Entities Covered**:
    *   **Concepts**: `if`, `elif`, `else`.
    *   **Relationships**: Applies logical operators (`and`, `or`, `not`) to primitive types (`str`, `int`, `bool`) and collection types (`dict`) from **Chunk 1**.
    *   **Advantages**: Demonstrates how conditionals create clear, readable business logic.
    *   **Disadvantages**: Shows how deeply nested `if` statements can become hard to maintain (a motivation for future patterns like polymorphism).
*   **Problem Description**: You have a list of dictionaries representing incoming API requests. Each request needs to be validated and categorized. A request is valid if it contains 'user_id' and 'payload' keys. Valid requests should be categorized as 'High Priority' if the payload size is over 1000 bytes and the user is a 'premium_user'; otherwise, they are 'Standard Priority'. Invalid requests should be categorized as 'Invalid'.

*   **Artificial Data**:
    ```python
    api_requests = [
        {'user_id': 101, 'payload_size': 1200, 'is_premium_user': True, 'payload': '...'},
        {'user_id': 102, 'payload_size': 800, 'is_premium_user': True, 'payload': '...'},
        {'user_id': 103, 'payload_size': 1500, 'is_premium_user': False, 'payload': '...'},
        {'user_id': 104, 'payload_size': 500, 'is_premium_user': False, 'payload': '...'},
        {'request_id': 901, 'payload_size': 2000, 'payload': '...'}, # Missing 'user_id'
        {'user_id': 105, 'is_premium_user': True, 'payload': '...'}, # Missing 'payload_size'
    ]
    ```
    *   **Software Engineering Principle**: *Modifiability*. This structure is easy to modify. If a new 'Medium Priority' category were introduced, you would simply add an `elif` condition.
*   **Resource Citation**:
    *   **Real Python: Python Conditional Statements** ([https://realpython.com/python-conditional-statements/](https://realpython.com/python-conditional-statements/)): This article provides a comprehensive overview of `if/elif/else` structures, including the use of logical operators (`and`, `or`, `not`) to combine conditions, which is central to solving this problem.

---

### **Exercise 2: Processing Parallel Data Streams with Iteration Patterns**

*   **Objective**: Use advanced iteration patterns (`zip`, `enumerate`) to efficiently process multiple related sequences of data simultaneously.
*   **Entities Covered**:
    *   **Concepts**: `for` loops.
    *   **Patterns**: `zip()`, `enumerate()`, ternary expressions.
    *   **Relationships**: Operates on lists and strings (Chunk 1) to produce formatted output.
    *   **Advantages**: Shows how `zip` and `enumerate` avoid manual index management, leading to cleaner, more Pythonic, and less error-prone code.
*   **Problem Description**: You are given three lists: `timestamps`, `sensor_ids`, and `readings`. They are all correlated by index. Process these lists to produce a report. For each record, if the reading is within the normal range (0 to 100), format a success message. Otherwise, format an error message. The report should include the 1-based index of the reading.

*   **Artificial Data**:
    ```python
    timestamps = [1678886400, 1678886401, 1678886402, 1678886403, 1678886404]
    sensor_ids = ['A-101', 'B-202', 'A-101', 'C-303', 'B-202']
    readings = [25.5, 99.9, 101.2, -5.0, 75.0]
    ```

*   **Solution**:
    ```python
    report_lines = []
    # Pattern: Use zip to combine three lists into one iterable of tuples.
    # Pattern: Use enumerate to get a clean, 1-based index for the report.
    for index, (ts, sensor, reading) in enumerate(zip(timestamps, sensor_ids, readings), start=1):
        # Relationship to Chunk 1: Applying comparison operators to floats/integers.
        is_valid = 0 <= reading <= 100
        
        # Pattern: Ternary expression for concise conditional assignment.
        status = "SUCCESS" if is_valid else "ERROR"
        
        # Relationship to Chunk 1: Using f-strings for easy string formatting.
        report_line = f"Record {index}: [{status}] - Timestamp: {ts}, Sensor: {sensor}, Reading: {reading}"
        report_lines.append(report_line)

    # Print the result for verification.
    for line in report_lines:
        print(line)
    ```
*   **Explanation**:
    *   `zip(timestamps, sensor_ids, readings)` elegantly combines the three lists. Without it, you would need to manage an index manually (e.g., `for i in range(len(timestamps))`), which is verbose and assumes all lists have the same length. `zip` stops when the shortest iterable is exhausted, which is often a desirable behavior.
    *   `enumerate(..., start=1)` provides a clean, sequential index, avoiding `index = i + 1` inside the loop.
    *   The **ternary expression** (`... if ... else ...`) makes the assignment of the `status` variable extremely concise and readable for a simple binary choice.
    *   **Software Engineering Principle**: *Efficiency*. These patterns are not only more readable but are also implemented in C under the hood, making them generally more performant than manual Python-level loops for the same logic.
*   **Resource Citation**:
    *   **Python Official Documentation: More Control Flow Tools** ([https://docs.python.org/3/tutorial/controlflow.html](https://docs.python.org/3/tutorial/controlflow.html)): The documentation explains the `for` statement and briefly introduces looping techniques. While it doesn't go deep into `zip`, it establishes the foundation of iteration that `zip` and `enumerate` build upon.

---

### **Hardcore Combined Problem: Intelligent Log Processor**

*   **Objective**: Synthesize all concepts and patterns from Chunk 2 (`if/elif/else`, `for`, `while`, `break`, `continue`, `pass`, `nested structures`, `enumerate`, `zip`, `ternary`) to solve a meaningful, complex problem that mirrors real-world scenarios.
*   **Entities Covered**:
    *   **Concepts**: All from Chunk 2.
    *   **Patterns**: All from Chunk 2.
    *   **Relationships**: Deeply intertwined with Chunk 1 concepts (lists, dictionaries, strings, booleans, integers) for state management and data manipulation.
*   **Problem Description**:
    You are building a security log processor. You receive a list of data batches, where each batch is a list of user action tuples `(timestamp, user_id, action)`. Your goal is to find the **first user** who successfully performs a "critical sequence": `login` followed by `purchase` within a `60-second` window.
    However, there are constraints:
    1.  The processor must stop checking as soon as the first valid user sequence is found.
    2.  Some log entries are corrupted and are represented by `None`. These should be skipped.
    3.  A `logout` action invalidates any active `login` for that user, resetting their critical sequence.
    4.  An action named `heartbeat` should be ignored entirely, acting as a placeholder.
    5.  The entire process should not scan more than `100` total log entries across all batches to prevent run-away processing.

*   **Artificial Data**:
Use this script to create sufficient data to make this exercise significant and complete the main 
```python
import random
import time
import pprint

# --- Configuration ---

# Total number of log entries to generate
TOTAL_LOGS_TO_GENERATE = 100000

# Number of unique user IDs to simulate
NUM_USERS = 20

# The types of events a user can perform
# We can make 'login' and 'logout' special
EVENT_TYPES = ['heartbeat', 'purchase', 'view_page', 'add_to_cart']

# Starting point for timestamps (uses current time as a base)
# Using a fixed value makes the output reproducible if you also fix the random seed
# random.seed(42) # Uncomment for reproducible results
START_TIMESTAMP = int(time.time())

# The maximum time gap between consecutive events
MAX_TIME_JUMP_SECONDS = 15

# --- Session Simulation Probabilities ---
# Chance that the next log event is a new user logging in
NEW_LOGIN_PROBABILITY = 0.30 # 30%

# Chance that an active user will log out after an action
LOGOUT_PROBABILITY = 0.15 # 15%

# --- Batching Configuration ---
# The minimum and maximum number of logs in a single batch
MIN_BATCH_SIZE = 2
MAX_BATCH_SIZE = 5

# The probability of injecting a None into a batch
NONE_INJECTION_PROBABILITY = 0.10 # 10%


def generate_significant_log_data():
    """
    Generates realistic, structured log data by simulating user sessions.
    """
    all_logs = []
    active_users = {}
    current_timestamp = START_TIMESTAMP
    user_ids = list(range(1, NUM_USERS + 1))
    print(f"Generating {TOTAL_LOGS_TO_GENERATE} logs for {NUM_USERS} potential users...")
    while len(all_logs) < TOTAL_LOGS_TO_GENERATE:
        should_create_new_login = random.random() < NEW_LOGIN_PROBABILITY
        if not active_users:
            should_create_new_login = True
        log_entry = None
        if should_create_new_login:
            inactive_users = [uid for uid in user_ids if uid not in active_users]
            if not inactive_users:
                continue 
            
            user_id = random.choice(inactive_users)
            event_type = 'login'
            
            active_users[user_id] = current_timestamp
            log_entry = (current_timestamp, user_id, event_type)
            
        else:
            user_id = random.choice(list(active_users.keys()))
            event_type = random.choice(EVENT_TYPES)
            
            log_entry = (current_timestamp, user_id, event_type)
            
            if random.random() < LOGOUT_PROBABILITY:
                current_timestamp += random.randint(1, MAX_TIME_JUMP_SECONDS)
                logout_entry = (current_timestamp, user_id, 'logout')
                all_logs.append(logout_entry)
                
                del active_users[user_id]

        if log_entry:
            all_logs.append(log_entry)
        
        current_timestamp += random.randint(1, MAX_TIME_JUMP_SECONDS)

    log_batches = []
    current_batch = []
    
    random.shuffle(all_logs) 

    all_logs.sort(key=lambda x: x[0]) 

    remaining_logs = len(all_logs)
    batch_sizes = []
    while remaining_logs > 0:
        size = random.randint(MIN_BATCH_SIZE, MAX_BATCH_SIZE)
        batch_sizes.append(min(size, remaining_logs))
        remaining_logs -= size

    log_iterator = iter(all_logs)
    for size in batch_sizes:
        batch = []
        for _ in range(size):
            try:
                if random.random() < NONE_INJECTION_PROBABILITY:
                    batch.append(None)
                
                batch.append(next(log_iterator))

            except StopIteration:
                break
        if batch:
            log_batches.append(batch)
            
    print("Log generation complete.")
    return log_batches

def critical_sequence(generate_log_batches):
    pass

# --- Main execution ---
if __name__ == "__main__":
    TIME_WINDOW = 60
    MAX_LOGS_TO_PROCESS = 100

    generated_log_batches = generate_significant_log_data()

    critical_sequence()
```

*   **Solution**:

```python
    def find_first_critical_sequence_user(batches, window, max_logs):
        active_logins = {}  # Relationship: Using a dict from Chunk 1 for state management.
        found_user_id = None
        logs_processed = 0

        # Outer loop to iterate through batches
        for batch in batches:
            # Nested loop to iterate through logs in a batch
            for log_entry in batch:
                if logs_processed >= max_logs:
                    print("Processing limit reached. Stopping.")
                    break  # break from the inner loop

                logs_processed += 1

                if log_entry is None:
                    print(f"Log {logs_processed}: Corrupted entry. Skipping.")
                    continue # Skip this iteration for corrupted data

                timestamp, user_id, action = log_entry

                # Use if/elif/else to handle different actions
                if action == 'login':
                    print(f"Log {logs_processed}: User {user_id} logged in at {timestamp}.")
                    active_logins[user_id] = timestamp
                elif action == 'purchase':
                    # Check if the user has an active login session
                    if user_id in active_logins:
                        login_time = active_logins[user_id]
                        time_diff = timestamp - login_time
                        
                        # Ternary for a concise status message
                        status = "within" if time_diff <= window else "outside"
                        print(f"Log {logs_processed}: User {user_id} purchase detected. Time diff: {time_diff}s ({status} window).")
                        
                        if time_diff <= window:
                            print(f"CRITICAL SEQUENCE DETECTED for user {user_id}!")
                            found_user_id = user_id
                            break # Found our user, exit inner loop
                    else:
                        print(f"Log {logs_processed}: User {user_id} made a purchase without a recent login.")
                elif action == 'logout':
                    print(f"Log {logs_processed}: User {user_id} logged out. Invalidating session.")
                    if user_id in active_logins:
                        del active_logins[user_id]
                elif action == 'heartbeat':
                    # Use 'pass' as a placeholder for an ignored action
                    pass
            
            if found_user_id is not None or logs_processed >= max_logs:
                break # break from the outer loop if user found or limit reached

        return found_user_id

    # --- Execution ---
    result = find_first_critical_sequence_user(log_batches, TIME_WINDOW, MAX_LOGS_TO_PROCESS)
    print("\n--- RESULT ---")
    if result:
        print(f"The first user to complete the critical sequence was: {result}")
    else:
        print("No user completed the critical sequence within the given constraints.")

    ```
*   **Explanation**:
    *   **Nested `for` Loops**: The code iterates through `batches` and then `log_entry` within each batch, a classic nested structure for processing batched data.
    *   **`break`**: This is used in three key places for **Efficiency**. First, it stops the entire process when the `max_logs` limit is hit. Second, and more importantly, it exits both the inner and outer loops once `found_user_id` is set, ensuring no unnecessary work is done after the goal is achieved.
    *   **`continue`**: This is used for **Reliability**. When a `None` entry is found, `continue` immediately skips to the next log entry, preventing the program from crashing and making the processor resilient to data corruption.
    *   **`if/elif/else`**: This structure forms the core logic, correctly routing the program's flow based on the `action` string.
    *   **`pass`**: The `pass` statement under `heartbeat` is a perfect example of its intended use: a syntactical placeholder for code that might be added later, without breaking the `if/elif` structure.
    *   **State Management**: The `active_logins` dictionary is a crucial element from Chunk 1. Control structures are meaningless without state to act upon. This dictionary holds the state of the system, which the control structures query and modify.
    *   **Software Engineering Principles**: This solution balances several principles. *Efficiency* (early exit with `break`), *Reliability* (handling corruption with `continue`), and *Modifiability* (new actions can be added as new `elif` blocks).
*   **Resource Citation**:
    *   **GeeksforGeeks: Python Loops** ([https://www.geeksforgeeks.org/loops-in-python/](https://www.geeksforgeeks.org/loops-in-python/)): This resource provides clear examples of `break`, `continue`, and `pass`, which are essential for managing the complex flow of the hardcore problem. The logic for skipping items, exiting early, and handling placeholders is directly influenced by the patterns described here.
    *   **Python Official Documentation: More Control Flow Tools**: The fundamental principles of `for`, `if`, and `break`/`continue` as described in the official docs provide the formal basis for this entire algorithm. The combination of these tools is what allows for this complex, stateful, and efficient processing.
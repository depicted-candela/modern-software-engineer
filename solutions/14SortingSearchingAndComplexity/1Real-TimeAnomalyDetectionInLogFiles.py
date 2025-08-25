    # Exercise 1: Real-Time Anomaly Detection in Log Files

# Description: You are tasked with building a monitoring tool for a 
# server that generates log entries. The tool must process a small, 
# sliding window of the most recent log entries (e.g., the last 100 
# entries) and sort them by severity level (an integer). For entries 
# with the same severity, their original chronological order must be 
# preserved to analyze event sequences. The sorting must happen 
# in-place to minimize memory usage on the server. The data in the 
# window is "nearly sorted" because log severities often come in 
# bursts (e.g., a series of low-severity logs followed by a burst of 
# high-severity ones).

# Artificial Data: A generator function will create a list of log 
# entry tuples (timestamp, severity_level), simulating a nearly 
# sorted stream.


# Specifications & Theory:

# The sorting algorithm must be stable to preserve the chronological 
# order of logs with the same severity.
# The sorting algorithm must be in-place (using O(1) auxiliary space) 
# to minimize memory overhead.
# Given the small and "nearly sorted" nature of the data window, an 
# algorithm with a good best-case performance (O(n)) is highly 
# desirable, even if its worst-case is O(n^2).

import random

def generate_log_data(size=100):
    """Generates a list of log entries, nearly sorted by severity."""
    data = []
    # Create bursts of severities
    for severity in sorted(random.sample(range(1, 11), 5)):
        burst_size = size // 5
        for _ in range(burst_size):
            # Add some noise to make it "nearly sorted"
            sev = max(1, severity + random.randint(-1, 1))
            timestamp = len(data) + 1
            data.append((timestamp, sev))
    # Shuffle slightly to ensure it's not perfectly sorted
    random.shuffle(data)
    return data[:size]

log_entries = generate_log_data()
original_entries = log_entries.copy()

def bubble_sort(
        arr: list[tuple[int, int]], 
        position: int
        ) -> tuple[int, int]:
    """
    Sorts a list of dictionaries in-place using bubble sort based on 
    a specified key.
    Returns (comparisons, swaps).
    SE Principle (Modifiability, Testability): Key allows flexible 
    sorting, counters enable precise analysis.
    """
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j][position] > arr[j+1][position]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True
        # Optimization: if no two elements were swapped by inner loop, 
        # then array is sorted
        if not swapped:
            break
    return comparisons, swaps

comparisons, swaps = bubble_sort(log_entries, 0)

def validate_log_sort(sort_func):
    # Test Case 1: General Correctness and Stability
    test_data = [(1, 5), (2, 2), (3, 5), (4, 1), (5, 2)]
    original_data_copy = list(test_data)
    
    # In-place check: The function should modify the list directly
    sort_func(test_data, 1)
    
    # Correctness check
    assert test_data == [(4, 1), (2, 2), (5, 2), (1, 5), (3, 5)], "Sorting failed."
    
    # Stability check: Check original order for items with severity 2 and 5
    pos_2_orig = [item[0] for item in original_data_copy if item[1] == 2]
    pos_2_sorted = [item[0] for item in test_data if item[1] == 2]
    assert pos_2_orig == pos_2_sorted, "Stability failed for severity 2."
    
    pos_5_orig = [item[0] for item in original_data_copy if item[1] == 5]
    pos_5_sorted = [item[0] for item in test_data if item[1] == 5]
    assert pos_5_orig == pos_5_sorted, "Stability failed for severity 5."
    
    print("Log Sort Validation Passed: Correct, Stable, and In-Place.")


if __name__ == "__main__":
    validate_log_sort(bubble_sort)
# Example of how to use the validator:
# your_sort_function(data, key_index)
# validate_log_sort(your_sort_function)
#   Exercise 3: Memory-Constrained Sorting for an Embedded System

# Description: You are developing firmware for an embedded device that 
# processes telemetry data. The device has very limited RAM. It needs to 
# sort an array of sensor readings in-place to find median and quartile 
# values for calibration. The sorting must have a guaranteed worst-case 
# time complexity of O(n log n) to ensure predictable processing times, and 
# it must use O(1) auxiliary space (excluding the input array itself).

#   Specifications & Theory:

# The sorting algorithm must be in-place, meaning it uses O(1) additional 
# memory. This is a hard constraint that eliminates algorithms like Merge 
# Sort.
# The algorithm must have a guaranteed worst-case time complexity of 
# O(n log n). This eliminates algorithms like Quicksort, whose worst-case is 
# O(n^2).


#   Artificial Data: A generator function for a large array of 
# floating-point sensor readings.

import random, heapq

def generate_telemetry_data(size=5000):
    return [random.uniform(0.0, 1000.0) for _ in range(size)]

telemetry_data = generate_telemetry_data()

def _heapify(arr: list[int], n: int, i: int) -> None:
    """
    Maintains the max-heap property for a subtree rooted at index i.
    n is the size of the heap.
    SE Principle (Modifiability): A helper function for heap operations.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2
    # See if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    # See if right child of root exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        _heapify(arr, n, largest)  # Heapify the root.
def heap_sort(arr: list[int]) -> None:
    """
    Sorts an array in-place using Heap Sort.
    SE Principle (Efficiency, Space Efficiency): Achieves O(N log N) time with O(1) auxiliary space.
    """
    n = len(arr)
    # Build a max-heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move current root to end
        _heapify(arr, i, 0)

def your_in_place_sort(telemetry_data):
    heap_sort(telemetry_data)

def validate_in_place_sort(sort_func):
    # Test Case: Large random data
    test_data = generate_telemetry_data(2000)
    original_id = id(test_data)
    expected_sorted = sorted(test_data) # Use Python's Timsort as the ground truth
    
    # Check memory usage (conceptual - hard to enforce in Python, but we check object ID)
    sort_func(test_data)
    assert id(test_data) == original_id, "Sort was not in-place (list object was replaced)."
    
    # Correctness check
    assert test_data == expected_sorted, "Sorting failed."
    
    # Performance check for worst-case (conceptual)
    # The choice of algorithm (Heap Sort) guarantees O(n log n) worst-case.
    # A true test would involve timing on a reverse-sorted list and comparing against Quicksort.
    
    print("In-Place Sort Validation Passed.")

# Example of how to use the validator:
# your_in_place_sort(telemetry_data)
validate_in_place_sort(your_in_place_sort)
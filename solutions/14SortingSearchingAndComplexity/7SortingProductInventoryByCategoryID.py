#       Exercise 7: Sorting Product Inventory by Category ID

#   Description: An e-commerce company needs to sort its entire product 
# inventory for a bulk export. Each product has a category_id which is an 
# integer between 1 and 1000. The primary requirement is to sort millions of 
# products by this category_id in linear time (O(n)). Stability is also 
# required to maintain the original product order within each category.

#   Specifications & Theory:

# The sorting must achieve linear time complexity. This rules out any 
# comparison-based sort, which has a lower bound of Ω(n log n).
# The keys (category_id) are integers within a known, relatively small range.
# The sort must be stable.

#   Key Skills:

# Recognizing that the problem constraints (integer keys in a small range, 
# linear time requirement) point to a non-comparison sort.
# Implementing an appropriate linear-time sorting algorithm.

#   Software Engineering Principles:

# Efficiency: Choosing an algorithm that meets a strict linear time 
# requirement by leveraging data properties.
# Scalability: The solution should handle millions of items efficiently.


#   Artificial Data: A generator for a large list of product tuples 
# (product_sku, category_id).

import random

def generate_product_data(size=1_000_000, max_category=1000):
    return [(f"SKU_{i}", random.randint(1, max_category)) for i in range(size)]

product_inventory = generate_product_data()
MAX_CATEGORY_ID = 1000

def _counting_sort_for_radix(arr: list[tuple[str, int]], exp: int, key_index=0) -> None:
    """
    A stable counting sort to sort elements based on digit represented by exp.
    exp is 10^i, where i is the current digit position.
    SE Principle (Reliability, Testability): Correctly sorts based on specific digit while preserving stability.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # For base 10 digits (0-9)
    # Store count of occurrences in count[]
    for i in range(n):
        index = (arr[i][key_index] // exp) % 10
        count[index] += 1
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i-1]
    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i][1] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    # Copying the output array to arr, so that arr now contains sorted numbers
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr: list[tuple[str, int]], key_index=0, k=1) -> None:
    """
    Sorts a list of integers using Radix Sort.
    Assumes integers are non-negative.
    SE Principle (Efficiency): Linear time for certain input distributions.
    """

    # Find the maximum number to know number of digits
    max1 = max(arr, key=lambda x: x[key_index])[key_index]
    # Do counting sort for every digit. Note that instead of passing digit number,
    # exp is passed. exp is 10^i where i is current digit number
    exp = k
    while max1 // exp > 0:
        _counting_sort_for_radix(arr, exp, key_index)
        exp *= 10

# radix_sort(product_inventory)

import time

def validate_linear_time_sort(sort_func):
    # Test Case 1: Correctness and Stability
    test_data = [("A", 3), ("B", 1), ("C", 2), ("D", 3), ("E", 1)]
    original_copy = list(test_data)
    
    sort_func(test_data, key_index=1, k=1)
    
    # Correctness
    assert test_data == [("B", 1), ("E", 1), ("C", 2), ("A", 3), ("D", 3)], "Sorting failed."
    
    # Stability
    cat1_orig = [item[0] for item in original_copy if item[1] == 1]
    cat1_sorted = [item[0] for item in test_data if item[1] == 1]
    assert cat1_orig == cat1_sorted, "Stability failed for category 1."
    
    # Test Case 2: Performance
    large_data = generate_product_data(500_000)
    
    start_time = time.perf_counter()
    sort_func(large_data, key_index=1, k=1000)
    end_time = time.perf_counter()
    
    # A simple performance check. Should be very fast.
    assert end_time - start_time < 1.0, "Sorting is too slow for a linear-time algorithm on this data size."
    
    print("Linear-Time Sort Validation Passed.")

# Example:
validate_linear_time_sort(radix_sort) # You'd need to adapt the counting sort
#   Exercise 5: Fast Lookup in a Static Product Database

# Description: You are working on an e-commerce platform with a massive, 
# static product database where products are identified by a unique, 
# integer product_id. The database is stored in memory as a list, sorted 
# by product_id. Your task is to create a function that performs lookups 
# for specific product IDs as fast as possible. The number of products 
# can be in the millions, so a linear scan is unacceptable.


#   Specifications & Theory:

# The input data is a large, sorted array.
# The lookup function must be significantly more efficient than linear 
# time. This points to a logarithmic time complexity.


#   Key Skills:

# Recognizing that a sorted array allows for logarithmic time search.
# Implementing an efficient search algorithm for sorted data.


#   Software Engineering Principles:

# Efficiency: Selecting the appropriate algorithm to leverage the 
# pre-sorted nature of the data for fast lookups.

# Artificial Data: A large, sorted list of product IDs.

product_ids = list(range(1_000_000, 2_000_000))
target_id = 1_500_000

def binary_search(arr: list[int], target: int) -> int | None:
    """
    Performs a binary search for a target element in a sorted list.
    SE Principle (Reliability, Testability): Handles empty/single-element lists and out-of-bounds targets.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

import time

def validate_fast_lookup(lookup_func):
    # Test Case 1: Correctness (found)
    data = [10, 20, 30, 40, 50]
    assert lookup_func(data, 30) == 2, "Lookup failed for existing element."
    
    # Test Case 2: Correctness (not found)
    assert lookup_func(data, 35) is None, "Lookup failed for non-existing element."
    
    # Test Case 3: Performance on large data
    large_data = list(range(2_000_000))
    target = 1_500_000
    
    start_time = time.perf_counter()
    result = lookup_func(large_data, target)
    end_time = time.perf_counter()
    
    assert result == target, "Lookup failed on large dataset."
    assert end_time - start_time < 0.01, "Lookup is too slow for large dataset."
    
    print("Fast Lookup Validation Passed.")

validate_fast_lookup(binary_search)
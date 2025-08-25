#   Exercise 4: High-Throughput Request Processing

# Description: You are building a load balancer for a web service that 
# receives millions of requests per second. For analytics, you need to sort 
# requests by their processing time. The primary requirement is the fastest 
# possible average-case performance. While occasional latency spikes 
# (worst-case performance) are acceptable, the average throughput is 
# critical. The sorting must be done in-place to minimize memory overhead 
# per request batch.

#   Specifications & Theory:

# The algorithm must prioritize average-case time complexity over 
# worst-case guarantees.
# It should be in-place (O(log n) stack space is acceptable).
# The solution should include a mechanism to mitigate the risk of 
# worst-case performance on structured data (like sorted or reverse-sorted 
# lists).

#   Key Skills:

# Identifying the algorithm with the best average-case performance for 
# general-purpose sorting.
# Understanding the trade-off between average-case and worst-case 
# performance.
# Implementing a randomized strategy to improve reliability.

# Artificial Data: A generator for large, random, sorted, and 
# reverse-sorted lists to test all scenarios.

import random

def generate_request_times(size=10000, case='random'):
    if case == 'random':
        return [random.randint(1, 1000) for _ in range(size)]
    elif case == 'sorted':
        return list(range(size))
    elif case == 'reversed':
        return list(range(size - 1, -1, -1))

random_requests = generate_request_times()
sorted_requests = generate_request_times(case='sorted')
reversed_requests = generate_request_times(case='reversed')

def partition(arr: list[int], low: int, high: int) -> int:
    """
    Partitions the array around a pivot (arr[high]).
    Returns the pivot's final index.
    SE Principle (Modifiability): Core partitioning logic, separable.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def randomized_partition(arr: list[int], low: int, high: int) -> int:
    """
    Selects a random pivot and partitions the array.
    SE Principle (Reliability): Random pivot reduces worst-case probability.
    """
    rand_idx = random.randint(low, high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx] # Swap random element with high for _partition
    return partition(arr, low, high)

def randomized_quicksort(arr: list[int], low: int, high: int) -> None:
    """
    Implements deterministic Quicksort in-place.
    SE Principle (Efficiency): Recursive, but pivot choice can lead to worst-case.
    """
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)


import time

def validate_high_throughput_sort(sort_func):
    # Test Case 1: Correctness on random data
    test_data_random = generate_request_times(1000, 'random')
    expected_sorted = sorted(test_data_random)
    sort_func(test_data_random, 0, len(test_data_random) - 1)
    assert test_data_random == expected_sorted, "Sorting failed on random data."
    
    # Test Case 2: Performance on worst-case input for deterministic pivot
    # A randomized algorithm should handle this gracefully
    test_data_reversed = generate_request_times(5000, 'reversed')
    start_time = time.perf_counter()
    sort_func(test_data_reversed, 0, len(test_data_reversed) - 1)
    end_time = time.perf_counter()
    
    # A simple performance check: should not be excessively slow
    # This won't fail for O(n^2) on small N, but is a proxy.
    # In a real test, you'd assert time < some_threshold
    assert end_time - start_time < 1.0, "Performance on reversed data is too slow, suggesting worst-case behavior."
    
    print("High-Throughput Sort Validation Passed.")

validate_high_throughput_sort(randomized_quicksort)
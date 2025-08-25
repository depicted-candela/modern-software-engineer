#   Exercise 6: Log Timestamp Search Optimization

# Description: You are analyzing high-frequency trading logs. The log 
# entries are indexed by an integer timestamp and are sorted. The 
# timestamps are known to be uniformly distributed over time (e.g., one 
# entry every microsecond). You need to build a search function to find 
# the log entry for a specific timestamp. The search must be as fast as 
# possible, leveraging the uniform distribution of the timestamps.


#   Specifications & Theory:

# The input data is a large, sorted, and uniformly distributed array.
# The search algorithm should have an average-case time complexity better 
# than O(log n).
# The solution should also be tested against non-uniformly distributed 
# data to observe its performance degradation.


#   Key Skills:

# Identifying that uniform distribution allows for an optimization over 
# binary search.
# Implementing a search algorithm that leverages this property.
# Understanding the performance trade-offs related to data distribution.

#   Artificial Data: A large, sorted list of product IDs.

product_ids = list(range(1_000_000, 2_000_000))
target_id = 1_500_000

def interpolation_search(arr: list[int], target: int) -> int | None:
    """
    Performs an interpolation search for a target element in a sorted, uniformly distributed list.
    SE Principle (Reliability): Checks for out-of-bounds target to prevent errors and improve robustness.
    """
    low = 0
    high = len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        # Handle cases where low == high to prevent division by zero
        if low == high:
            if arr[low] == target:
                return low
            return None
        # Estimate position
        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])
        # Clamp pos to prevent out-of-bounds access if formula yields an invalid index
        pos = max(low, min(high, pos))
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return None

import time

def validate_optimized_search_corrected(search_func):
    # --- Test Case 1: Validate O(log log n) or ~O(1) on uniform data ---
    print("--- VALIDATING UNIFORM DATA SCALING (EXPECTED: ~O(1)) ---")
    n = 1_000_000
    uniform_data_n = list(range(n))
    target_n = n // 2

    start_time_n = time.perf_counter()
    search_func(uniform_data_n, target_n)
    end_time_n = time.perf_counter()
    time_n = end_time_n - start_time_n
    print(f"Time for n={n}: {time_n:.8f}s")

    # Now test with a much larger dataset
    n_large = n * 10
    uniform_data_large = list(range(n_large))
    target_large = n_large // 2

    start_time_large = time.perf_counter()
    search_func(uniform_data_large, target_large)
    end_time_large = time.perf_counter()
    time_large = end_time_large - start_time_large
    print(f"Time for n={n_large}: {time_large:.8f}s")

    # For O(1) or O(log log n), time should not increase significantly.
    # A generous factor of 2-4x allows for caching effects, noise, etc.
    assert time_large < time_n * 4, f"Uniform search scaled poorly. Time increased from {time_n}s to {time_large}s."
    print("✅ Uniform scaling validation passed.\n")


    # --- Test Case 2: Validate O(n) degradation on non-uniform data ---
    print("--- VALIDATING NON-UNIFORM DATA SCALING (EXPECTED: O(n)) ---")
    n_nu = 100_000 # Start smaller, as this is slow
    non_uniform_data_nu = [100] * (n_nu - 1) + [1_000_000]
    target_nu = 101 # Worst-case target

    start_time_nu_n = time.perf_counter()
    search_func(non_uniform_data_nu, target_nu)
    end_time_nu_n = time.perf_counter()
    time_nu_n = end_time_nu_n - start_time_nu_n
    print(f"Time for n={n_nu}: {time_nu_n:.8f}s")

    # Now test with a larger dataset
    n_nu_large = n_nu * 5 # Use a smaller multiplier as O(n) is slow
    non_uniform_data_nu_large = [100] * (n_nu_large - 1) + [1_000_000]

    start_time_nu_large = time.perf_counter()
    search_func(non_uniform_data_nu_large, target_nu)
    end_time_nu_large = time.perf_counter()
    time_nu_large = end_time_nu_large - start_time_nu_large
    print(f"Time for n={n_nu_large}: {time_nu_large:.8f}s")

    # For O(n), time should increase roughly linearly with n.
    # Expected ratio is ~5x. We allow a generous range (e.g., 3x to 7x) to account for noise.
    ratio = time_nu_large / time_nu_n
    print(f"Observed scaling ratio: {ratio:.2f}x (Expected ~5x)")
    assert 3 < ratio < 7, "Non-uniform search did not scale linearly as expected."
    print("✅ Non-uniform scaling validation passed.")

# Run the corrected validation
validate_optimized_search_corrected(interpolation_search)
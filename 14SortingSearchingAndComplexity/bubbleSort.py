def bubble_sort(arr):
    """
    Concept: Bubble Sort - repeatedly compares and swaps adjacent elements.
    Pattern: Adjacent comparison and swap.
    Property: In-place sorting.
    """
    n = len(arr)
    swaps = 0
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them.
        swapped = False # Optimization: if no swaps in a pass, list is sorted (Best case: O(n))
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                swaps += 1
        if not swapped: # Best-case optimization: The "early exit" shortcut.
            break
    return arr, swaps
# Artificial Data: See how different starting points affect the "nudges"
data_worst_case = [5, 4, 3, 2, 1] # A completely backwards line
data_best_case = [1, 2, 3, 4, 5]  # An already perfect line
data_average_case = [64, 34, 25, 12, 22, 11, 90] # A typically jumbled queue
arr1, swaps1 = bubble_sort(list(data_worst_case))
arr2, swaps2 = bubble_sort(list(data_best_case))
arr3, swaps3 = bubble_sort(list(data_average_case))
print(f"Bubble Sort Worst Case: {arr1, swaps1}")
print(f"Bubble Sort Best Case: {arr2, swaps2}")
print(f"Bubble Sort Average Case: {arr3, swaps3}")
# Time Complexity:
# Worst-case (reverse sorted): O(n^2) - a "quadratic ascent" of comparisons and swaps.
# Best-case (already sorted): O(n) - a "linear stroll" to confirm order.
# Average-case: O(n^2) - still a "quadratic ascent."
# Space Complexity: O(1) (in-place) - a "space-divine" sort.
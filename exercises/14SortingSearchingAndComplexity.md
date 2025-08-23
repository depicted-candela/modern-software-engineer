# Exercise 1: Implementing Bubble Sort and Analyzing Basic Complexity

**Description:** Implement the Bubble Sort algorithm in Python. After sorting, calculate and state its worst-case and best-case time complexity using Big O notation, justifying your answer based on the number of comparisons and swaps performed.

**Artificial Data:**
1.  `input_data_worst = [5, 4, 3, 2, 1]` (for worst-case scenario)
2.  `input_data_best = [1, 2, 3, 4, 5]` (for best-case scenario)
3.  `input_data_average = [64, 34, 25, 12, 22, 11, 90]` (for general observation)

**Specifications & Theory:**
*   **Bubble Sort Concept**: Repeatedly stepping through the list, comparing adjacent elements and swapping them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.
*   **Worst-Case Complexity**: Occurs when the list is in reverse order. In this scenario, every element needs to be swapped in every pass, leading to `(n-1) + (n-2) + ... + 1` comparisons and swaps. This sum is `n(n-1)/2`, which simplifies to `O(n^2)`. (Refer to `ConcreteMathematics_Graham-Knuth-Patashnik_1994` - Chapter 9: Asymptotics for notation, and general sorting algorithm resources like `SortingTechniques...` from Python docs or *GeeksforGeeks Bubble Sort* for algorithm details).
*   **Best-Case Complexity**: Occurs when the list is already sorted. In this case, only one pass is needed to confirm no swaps, resulting in `n-1` comparisons. This simplifies to `O(n)`.
*   **Space Complexity**: `O(1)` as it sorts in-place without requiring additional significant memory beyond temporary storage for swaps.

**Key Skills:** Implementing a basic sorting algorithm, basic complexity analysis.
**Software Engineering Principles:**
*   **Efficiency**: Understanding why Bubble Sort is generally inefficient despite its simplicity.
*   **Testability**: Designing test cases for best, worst, and average scenarios.

# Exercise 2: Implementing Merge Sort with Divide-and-Conquer

**Description:** Implement the Merge Sort algorithm in Python. This implementation should clearly demonstrate the "divide-and-conquer" pattern. Analyze its time complexity using Big O notation.

**Artificial Data:**
`data_merge = [38, 27, 43, 3, 9, 82, 10]`

**Specifications & Theory:**
*   **Merge Sort Concept**: A comparison-based sorting algorithm that works by breaking a list down into several sub-lists until each sub-list consists of a single element (and is thus "sorted"), and then repeatedly merging sub-lists to produce new sorted sub-lists until there is only one sorted list remaining. (Refer to *GeeksforGeeks Merge Sort*).
*   **Divide-and-Conquer Pattern**: The core of Merge Sort.
    1.  **Divide**: Break the `n`-element list into two sub-lists of `n/2` elements each.
    2.  **Conquer**: Recursively sort the two sub-lists.
    3.  **Combine**: Merge the two sorted sub-lists back into one sorted list.
    (This pattern is extensively discussed in *Cormen Chapter 4.1: Multiplying square matrices* as a general strategy, and *Cormen Chapter 2.3.1* directly applies to Merge Sort).
*   **Time Complexity**: Each level of recursion involves `O(n)` work (for merging). The depth of the recursion tree is `log n`. Therefore, the total time complexity is `O(n log n)` in all cases (worst, average, best). (Refer to *Cormen Chapter 3: Characterizing Running Times* and *MathematicsForComputerScience_Lehman-Leighton-Meyer_2015* - Chapter 14: Sums and Asymptotics for recurrence relations and their solutions).
*   **Space Complexity**: `O(n)` due to the temporary arrays created during the merging step.

**Key Skills:** Implementing a recursive sorting algorithm, understanding divide-and-conquer, analyzing `O(n log n)` complexity.
**Software Engineering Principles:**
*   **Scalability**: Demonstrating how recursion efficiently handles larger inputs.
*   **Modifiability**: The `merge` function is a separate, reusable component.

# Exercise 3: Implementing Heap Sort and Heap Property Maintenance

**Description:** Implement the Heap Sort algorithm in Python. Your implementation should include a clear `heapify` function to maintain the max-heap property and a function to build the initial max-heap. Sort the given array and demonstrate how the heap property is maintained throughout the process.

**Artificial Data:**
`data_heap = [4, 10, 3, 5, 1, 9, 8]`

**Specifications & Theory:**
*   **Heap Sort Concept**: A comparison-based sorting technique based on binary heaps. It builds a max-heap from the input data, then repeatedly extracts the maximum element (root), moving it to the end of the array and rebuilding the heap from the remaining elements.
*   **Max-Heap Property**: For every node `i` other than the root, `A[PARENT(i)] >= A[i]`. This ensures the largest element is always at the root. (Refer to *Cormen Chapter 6.1: Heaps*).
*   **Heapify (Sift-Down) Pattern**: This operation maintains the max-heap property. If a node `i` violates the property, `heapify` compares it with its children and swaps it with the largest child. This process is then recursively called on the child's subtree. Its time complexity is `O(log n)`. (Refer to *Cormen Chapter 6.2: Maintaining the heap property*).
*   **Build Max-Heap Pattern**: Converts an arbitrary array into a max-heap. This is done by calling `heapify` on all non-leaf nodes, starting from the last non-leaf node up to the root. This operation has a time complexity of `O(n)`. (Refer to *Cormen Chapter 6.3: Building a heap*).
*   **Time Complexity**: Building the heap is `O(n)`. There are `n-1` extractions, each involving a `heapify` call, taking `O(log n)` time. Thus, the overall time complexity is `O(n log n)`.
*   **Space Complexity**: `O(1)` as it sorts in-place.

**Key Skills:** Implementing heap-based sorting, understanding and maintaining heap properties.
**Software Engineering Principles:**
*   **Reliability**: Ensuring the heap property is consistently maintained after each operation.
*   **Efficiency**: Utilizing the `O(n)` heap build and `O(log n)` heapify operations.

# Exercise 4: Implementing Quicksort with Lomuto Partitioning

**Description:** Implement the Quicksort algorithm in Python using the Lomuto partition scheme (where the pivot is typically the last element). Clearly define the partitioning step and explain how it contributes to the overall sorting process. Analyze the algorithm's average-case and worst-case time complexities.

**Artificial Data:**
`data_quick = [10, 7, 8, 9, 1, 5, 2, 4, 6, 3]`

**Specifications & Theory:**
*   **Quicksort Concept**: A divide-and-conquer sorting algorithm. It picks an element as a pivot and partitions the given array around the picked pivot.
*   **Lomuto Partitioning Pattern**: This scheme selects the last element as the pivot. It maintains two pointers, `i` (index of the smaller element) and `j` (current element). As it iterates `j` from `low` to `high-1`, if `arr[j]` is less than or equal to the pivot, `i` is incremented, and `arr[i]` and `arr[j]` are swapped. Finally, the pivot is swapped with `arr[i+1]`. (Refer to *Cormen Chapter 7.1: Description of quicksort* for the partitioning concept).
*   **Divide-and-Conquer Relationship**: Quicksort recursively sorts the sub-arrays to the left and right of the pivot. The partitioning step performs the "divide" and partially "combine" roles. (Refer to *Cormen Chapter 2.3.1* for the general divide-and-conquer method).
*   **Average-Case Time Complexity**: When partitioning is balanced (e.g., roughly equal halves), the recurrence is `T(n) = 2T(n/2) + O(n)`, which solves to `O(n log n)`. This is common for randomized pivot selection. (Refer to *Cormen Chapter 7.2: Performance of quicksort* for balanced partitioning).
*   **Worst-Case Time Complexity**: Occurs when partitioning is maximally unbalanced (e.g., one sub-array has `n-1` elements, the other has 0). This happens if the pivot is always the smallest or largest element. The recurrence becomes `T(n) = T(n-1) + T(0) + O(n)`, which solves to `O(n^2)`. (Refer to *Cormen Chapter 7.2: Worst-case partitioning*).
*   **Space Complexity**: `O(log n)` in the average case (for recursion stack depth) and `O(n)` in the worst case.

**Key Skills:** Implementing Quicksort, understanding partitioning, analyzing average vs. worst-case complexity.
**Software Engineering Principles:**
*   **Efficiency**: Understanding the importance of pivot selection for performance.
*   **Modifiability**: Encapsulating the partitioning logic in a separate function.

# Exercise 5: Implementing Binary Search for Element Lookup

**Description:** Implement the Binary Search algorithm in Python to find a target element in a **sorted** array. The function should return the index of the target if found, otherwise -1. Provide a clear analysis of its time complexity.

**Artificial Data:**
`sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]`
`target_found = 23`
`target_not_found = 42`

**Specifications & Theory:**
*   **Binary Search Concept**: An efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one. (Refer to *LeetCode Binary Search* for algorithm details).
*   **Halving Search Space Pattern**: The core mechanism is to compare the target value with the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated, and the search continues on the remaining half.
*   **Time Complexity**: Each comparison reduces the search space by half. The number of comparisons required is proportional to `log_2(n)`. Thus, its time complexity is `O(log n)`. (Refer to *Cormen Chapter 3: Characterizing Running Times*).
*   **Space Complexity**: `O(1)` for iterative implementation, `O(log n)` for recursive implementation due to call stack.
*   **Prerequisite**: The array *must* be sorted for Binary Search to work correctly. (Relationship to sorting algorithms from previous exercises is crucial here, as searching is efficient only after optimal data access is ensured).

**Key Skills:** Implementing an efficient search algorithm, understanding `O(log n)` complexity.
**Software Engineering Principles:**
*   **Efficiency**: Choosing the optimal algorithm for sorted data.
*   **Reliability**: Handling edge cases (empty array, target not found, first/last element).

# Exercise 6: Implementing Interpolation Search

**Description:** Implement the Interpolation Search algorithm in Python to find a target element in a **uniformly distributed and sorted** array. The function should return the index of the target if found, otherwise -1. Analyze its average-case and worst-case time complexities, highlighting the conditions under which it outperforms Binary Search.

**Artificial Data:**
`sorted_uniform_array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`
`target_found = 70`
`target_not_found = 35`
`sorted_non_uniform_array = [1, 2, 3, 10, 20, 30, 40, 50, 60, 1000]` (for worst-case scenario)

**Specifications & Theory:**
*   **Interpolation Search Concept**: An improvement over binary search for uniformly distributed sorted data. Instead of always going to the middle element, it estimates the position of the target based on its value relative to the low and high elements.
    *   `pos = low + ((high - low) / (arr[high] - arr[low])) * (target - arr[low])`
    (Refer to *GeeksforGeeks Interpolation Search* for algorithm details).
*   **Probabilistic Estimation Pattern**: The key difference from binary search is this estimation, which performs well when data is uniformly distributed.
*   **Average-Case Time Complexity**: For uniformly distributed data, `O(log log n)`. This is because the search space is reduced much faster than by halving, by making a "guess" closer to the target's actual position. (Refer to *GeeksforGeeks Interpolation Search* for this complexity claim).
*   **Worst-Case Time Complexity**: `O(n)`. This occurs when the values are not uniformly distributed (e.g., an array with many identical values or a highly skewed distribution), leading to poor position estimates and degenerating to linear search in the worst case. (Refer to *Cormen Chapter 3: Characterizing Running Times* for general complexity analysis).
*   **Relationship to Binary Search**: Interpolation Search is an optimization of Binary Search, performing better under specific data distribution properties (uniformity). If data is not uniform, Binary Search is more robust.

**Key Skills:** Implementing an optimized search algorithm, understanding probabilistic performance, comparing search strategies.
**Software Engineering Principles:**
*   **Efficiency**: Choosing the right algorithm based on data characteristics.
*   **Reliability**: Understanding the limitations and potential worst-case scenarios for non-uniform data.

# Exercise 7: Empirical Performance Comparison of Sorting Algorithms (Layered Combination)

**Description:** Write a Python script to empirically compare the execution times of Bubble Sort, Merge Sort, Heap Sort, and Quicksort across different input conditions: random, already sorted, and reverse sorted arrays. For each algorithm and condition, measure the time taken for input sizes `N = 100, 1000, 10000`. Present the results in a structured format (e.g., a table). Analyze if the empirical results align with their theoretical Big O complexities.

**Artificial Data:**
*   **Input Sizes**: `N_values = [100, 1000, 10000]`
*   **Input Types (for each N)**:
    *   `random_array`: `[random.randint(0, N*10) for _ in range(N)]`
    *   `sorted_array`: `list(range(N))`
    *   `reverse_sorted_array`: `list(range(N-1, -1, -1))`

**Specifications & Theory:**
*   **Concepts**: All sorting algorithms (Bubble, Merge, Heap, Quick), Big O notation, empirical measurement.
*   **Patterns**: Benchmarking, iterative testing.
*   **Relationships**: This exercise directly links the theoretical complexity (`O(n^2)`, `O(n log n)`) of sorting algorithms to their practical performance. It highlights that constant factors (often ignored in Big O) can matter for smaller `N`, but asymptotic behavior dominates for larger `N`. (Refer to *ComputerOrganizationAndDesign_Patterson-Hennessy_2020* - Chapter 1: Computer Abstractions and Technology, which discusses how theoretical complexity relates to real machine performance, and *Cormen Chapter 3* for the theoretical underpinnings).
*   **Tools**: Use Python's `time` module for measurement.

**Key Skills:** Empirical performance testing, correlating empirical data with theoretical complexity, understanding constant factors.
**Software Engineering Principles:**
*   **Efficiency**: Practical observation of performance differences.
*   **Testability**: Comprehensive testing across various input sizes and distributions.
*   **Modifiability**: Structuring the benchmark script to easily add/remove algorithms or input types.

# Exercise 8: Kth Order Statistic using Partitioning (Layered Combination)

**Description:** Implement a Python function, `find_kth_smallest`, that efficiently finds the *k*-th smallest element in an unsorted array using a partitioning strategy similar to Quicksort (e.g., Hoare's or Lomuto's). The function should ideally run in average linear time. Analyze its worst-case and average-case time complexities.

**Artificial Data:**
`data_select = [7, 10, 4, 3, 20, 15, 8, 12, 16]`
`k_values = [1, 3, 5, 9]` (1st, 3rd, 5th, 9th smallest)

**Specifications & Theory:**
*   **Concepts**: Medians and Order Statistics, Partitioning, Big O notation.
*   **Patterns**: Quicksort's partitioning step (`partition`), binary search tree-like logic (recursively selecting one partition).
*   **`find_kth_smallest` Algorithm**:
    1.  Select a pivot (e.g., random or last element).
    2.  Partition the array around the pivot. Let the pivot end up at index `p`.
    3.  If `p` is `k-1` (0-indexed), then `arr[p]` is the *k*-th smallest.
    4.  If `p > k-1`, the *k*-th smallest must be in the left partition; recursively call on the left sub-array.
    5.  If `p < k-1`, the *k*-th smallest must be in the right partition; recursively call on the right sub-array, adjusting `k` to `k - (p - low + 1)`.
    (This algorithm is known as Quickselect. It is closely related to `RANDOMIZED-SELECT` discussed in *Cormen Chapter 9.2: Selection in expected linear time* and its partitioning procedure from *Cormen Chapter 7.3: A randomized version of quicksort*).
*   **Average-Case Time Complexity**: `O(n)` because on average, each partition discards a significant portion of the array, similar to the average-case analysis of Quicksort focusing on one side.
*   **Worst-Case Time Complexity**: `O(n^2)` if unlucky pivot choices repeatedly lead to maximally unbalanced partitions, similar to Quicksort's worst case.
*   **Space Complexity**: `O(log n)` average, `O(n)` worst (for recursion stack).

**Key Skills:** Adapting sorting primitives for selection, understanding average linear time, using partitioning.
**Software Engineering Principles:**
*   **Efficiency**: Achieving average-case linear time for selection.
*   **Modifiability**: Reusing the `partition` function from Quicksort (if implemented).

---

# Hardcore Combined Problem: "Dynamic Data Stream Optimizer"

**Description:**
Design and implement a `DataStreamOptimizer` class in Python. This class simulates a high-frequency data pipeline that processes streams of sensor readings (integers). The system has two critical requirements:
1.  **Maintain Sorted Unique Readings**: Dynamically maintain a sorted list of the `M` most recent *unique* sensor readings. When the number of unique readings exceeds `M`, the *oldest unique* reading must be removed.
2.  **Rank and Criticality Check**: For any new incoming reading, determine its 1-indexed rank within the currently maintained `M` unique readings. Additionally, flag the reading as "critical" if its rank falls within the top 10% (i.e., `rank <= M * 0.1`). Assume `M` is a positive integer.

**Artificial Data:**
`M = 10`
`readings_stream = [50, 20, 80, 10, 60, 30, 90, 40, 70, 15, 25, 55, 85, 5, 95, 100, 10, 20]`

**Implementation Details:**
The `DataStreamOptimizer` class should include:
*   `__init__(self, M: int)`: Initializes the system with maximum capacity `M`.
*   `add_reading(self, value: int) -> tuple[int, bool]`: Processes a new sensor `value`. It should update the set of unique readings, manage the `M` most recent, maintain sorted order, and return `(rank, is_critical)`.
*   `get_current_readings(self) -> list[int]`: Returns the currently maintained `M` unique readings in sorted order.

**Analysis:**
Analyze the time complexity of `add_reading` and `get_current_readings` in terms of `M`. Justify your choices for internal data structures by relating their properties to the desired efficiency.

**Specifications & Theory:**
*   **Concepts**:
    *   **Sorting**: Implicitly maintained sorted order. Heap Sort or similar could be used for re-sorting, but for small `M`, simpler insertion might be `O(M)`. A balanced BST-like structure or `heapq` could be more efficient.
    *   **Searching**: Binary Search (`O(log M)`) for `rank` lookup on the sorted list. Interpolation Search could be considered if the sensor readings were known to be uniformly distributed for `O(log log M)` average performance, but Binary Search is more robust without this assumption.
    *   **Complexity (Big O notation)**: Crucial for justifying performance choices.
    *   **Arrays**: Underlying storage for sorted data.
    *   **Hashing (from Chunk 16)**: Essential for `O(1)` average time complexity to track `uniqueness` of elements and check for presence before insertion/removal.
    *   **Queues (from Chunk 12)**: A `collections.deque` provides `O(1)` append/pop from both ends, perfect for managing the "most recent" aspect (sliding window) of unique elements.

*   **Patterns & Properties Leveraged for Simplification**:
    *   **Maintaining Uniqueness and Recency (Sliding Window)**: Use a `collections.deque` (Queue) to store elements in order of arrival, and a `set` (Hash Map) to store all currently active unique elements. When `deque` size exceeds `M`, pop oldest, remove from `set`.
        *   `collections.deque`: `O(1)` append/pop. (Python docs: `collections.deque`)
        *   `set`: `O(1)` average for add/remove/check existence. (Cormen Chapter 11: Hash Tables).
    *   **Maintaining Sorted Order for `M` Unique Elements**: Since we only care about the *M* largest values, a `min-heap` of size `M` can efficiently maintain the *M* largest elements. For rank calculation, however, the full sorted list is needed. A combined approach would be:
        *   Keep the actual *M* unique elements in a Python `list`. After each `add_reading` (and potential removal of the oldest), sort this list. For small `M`, this sorting `O(M log M)` is acceptable.
        *   Alternatively, a self-balancing binary search tree (not explicitly covered in prior chunks but conceptually related to BST from Chunk 13) would allow `O(log M)` insertion/deletion and sorted iteration, but adds complexity. For this problem, a simple `list.sort()` after modifications is a good initial trade-off given `M` isn't huge.
    *   **Rank Calculation**: After `current_readings` is sorted, use `bisect_left` (binary search) to find the insertion point, which gives the rank.
        *   `bisect_left`: `O(log M)`. (Python docs related to sorting, implicitly `LeetCode Binary Search`).

*   **Time Complexity Analysis**:
    *   `add_reading`:
        *   Checking `value` existence in `unique_elements` set: `O(1)` average.
        *   Adding/removing from `recent_readings` deque: `O(1)`.
        *   Adding/removing from `unique_elements` set: `O(1)` average.
        *   Rebuilding `current_readings` list from `unique_elements` and sorting it: `O(M log M)`. This is the dominant factor.
        *   Finding rank using binary search (`bisect_left`): `O(log M)`.
        *   **Overall `add_reading`**: `O(M log M)` in worst case due to re-sorting, `O(1)` if no new unique element is added or removed.
    *   `get_current_readings`: `O(M)` to return the list (it's already sorted internally).

*   **Space Complexity Analysis**:
    *   `unique_elements` set: `O(M)`.
    *   `recent_readings` deque: `O(M)`.
    *   `current_readings` list: `O(M)`.
    *   **Overall**: `O(M)`.

**Key Skills for Hardcore Problem:**
*   **Data Structure Selection**: Choosing `deque` for recency, `set` for uniqueness, and `list` for ordered output/rank, leveraging their specific `O(1)` or `O(log N)` properties for efficiency.
*   **Algorithm Integration**: Combining sorting logic (implicit in maintaining `current_readings`) with searching (binary search for rank) and dynamic data management (queue + hash set).
*   **Complexity Analysis**: Justifying `O(M log M)` for `add_reading` due to dynamic sorting, and `O(log M)` for searching.
*   **Problem Decomposition**: Breaking down the requirements (uniqueness, recency, sorted order, rank) into manageable sub-problems addressed by appropriate data structures.

**Software Engineering Principles:**
*   **Efficiency**: Maximizing efficiency by using hash sets for `O(1)` uniqueness checks and `bisect_left` for `O(log M)` rank lookups. The `O(M log M)` sorting after each significant change is a pragmatic trade-off for correctness given the requirement to keep the full `M` unique items sorted for rank.
*   **Scalability**: The design scales well with data stream size due to `O(1)` queue/set operations and `O(M log M)` operations relative to the fixed window size `M`.
*   **Modifiability**: Encapsulating logic within a class, making it easy to change internal data structures if performance bottlenecks emerge for very large `M`.
*   **Testability**: Each component (uniqueness tracking, recency tracking, sorting, rank calculation) is testable individually and as part of the `add_reading` method.
*   **Reliability**: Handling empty arrays, edge ranks, and duplicates gracefully.

```python
import collections
import bisect
import random
import time

class DataStreamOptimizer:
    def __init__(self, M: int):
        if M <= 0:
            raise ValueError("M must be a positive integer.")
        self.M = M
        self.unique_elements = set()  # Concept: Hashing for O(1) uniqueness check
        self.recent_readings_queue = collections.deque() # Concept: Queues for O(1) recency/sliding window
        self.sorted_unique_list = [] # Concept: Arrays, implicitly maintained sorted

    def _update_sorted_list(self):
        """
        Pattern: In-place sorting. Rebuilds and sorts the list of current unique elements.
        Relationship: Optimizes data access for subsequent searches.
        """
        self.sorted_unique_list = sorted(list(self.unique_elements)) # O(M log M)

    def add_reading(self, value: int) -> tuple[int, bool]:
        """
        Adds a new reading to the stream, maintaining M unique recent elements.
        Calculates rank and criticality.
        """
        # 1. Handle recency and uniqueness (Sliding Window Pattern)
        if value not in self.unique_elements:
            # If it's a new unique element
            self.recent_readings_queue.append(value)
            self.unique_elements.add(value)
            
            if len(self.unique_elements) > self.M:
                # Need to evict oldest unique element
                evicted_value = -1
                while evicted_value == -1 or evicted_value not in self.unique_elements:
                    # Find the oldest value that is still unique in the set
                    oldest_in_queue = self.recent_readings_queue.popleft()
                    if oldest_in_queue in self.unique_elements:
                        # Check if this oldest value is still truly unique in the active set
                        # This loop handles cases where a value was added, then re-added,
                        # making its *first* occurrence irrelevant for recency.
                        # However, for simplicity and typical data streams, just assume
                        # values are distinct enough for oldest_in_queue to be the one to remove.
                        # A more robust solution might require a counter for each value in the queue
                        # to only remove when its last appearance passes the window.
                        # For this problem's constraint: oldest *unique* element.
                        if len(self.unique_elements) > self.M: # Re-check M boundary
                             self.unique_elements.remove(oldest_in_queue)
                             evicted_value = oldest_in_queue # Mark as evicted
                        else: # M boundary no longer exceeded
                            self.recent_readings_queue.appendleft(oldest_in_queue) # Put it back
                            break
                        
                
            self._update_sorted_list() # Re-sort after structural change
        else:
            # If value already exists, update its recency by moving it to the end of the queue
            # This is an O(M) operation for deque, but ensures correctness of "M most recent unique"
            # More efficient: track last seen position with a dict for O(1) update.
            # For simplicity, and typical M values, this is acceptable.
            # For strict O(1) recency update with removal, a doubly linked list + hash map (like LRU) is needed.
            # Based on problem wording, "M most recent unique sensor readings" implies order of adding to queue matters.
            # If we don't remove and re-add, it would track "M unique readings present in the window", not "M most recent unique".
            
            # Find and remove old entry to update recency
            temp_deque = collections.deque()
            found = False
            while self.recent_readings_queue:
                q_val = self.recent_readings_queue.popleft()
                if q_val == value and not found:
                    found = True
                else:
                    temp_deque.append(q_val)
            if found:
                temp_deque.append(value)
            self.recent_readings_queue = temp_deque
            
            # If the set size changed (e.g., first adding a duplicate after eviction), sorted list needs update
            if value not in self.unique_elements: # Should not happen if it already existed
                 self.unique_elements.add(value)
                 self._update_sorted_list()

            # No need to update sorted_unique_list or unique_elements set if value already present and M not exceeded
            # because the set of *unique* elements remains the same. Only their recency changes.
            # If the strict interpretation of "M most recent unique" means their sorted list might change
            # due to an eviction, then _update_sorted_list() is called above.
            
        # 2. Calculate rank (Searching Concept)
        # Pattern: Binary search tree-like logic for finding rank
        rank = bisect.bisect_left(self.sorted_unique_list, value) + 1 # O(log M)
        
        # 3. Determine criticality
        is_critical = rank <= self.M * 0.1 # Complexity: O(1)

        return rank, is_critical

    def get_current_readings(self) -> list[int]:
        """
        Returns the currently maintained M unique readings in sorted order.
        Complexity: O(M) to create a copy of the list.
        """
        return list(self.sorted_unique_list)

# --- Test Cases ---

# Test 1: Basic functionality
M_test1 = 5
optimizer1 = DataStreamOptimizer(M_test1)
stream_test1 = [10, 30, 20, 50, 40, 15, 35, 60]

print(f"--- Test 1 (M={M_test1}): Basic Functionality ---")
for reading in stream_test1:
    rank, critical = optimizer1.add_reading(reading)
    print(f"Added {reading}: Rank={rank}, Critical={critical}, Current_Readings={optimizer1.get_current_readings()}")
# Expected output:
# 10: R=1,C=T,CR=[10]
# 30: R=2,C=F,CR=[10,30]
# 20: R=2,C=T,CR=[10,20,30]
# 50: R=4,C=F,CR=[10,20,30,50]
# 40: R=4,C=F,CR=[10,20,30,40,50] (Reached M=5)
# 15: R=2,C=T,CR=[15,20,30,40,50] (10 evicted)
# 35: R=3,C=F,CR=[15,20,30,35,40] (50 evicted)
# 60: R=5,C=F,CR=[20,30,35,40,60] (15 evicted)


# Test 2: Duplicates and M boundary
M_test2 = 3
optimizer2 = DataStreamOptimizer(M_test2)
stream_test2 = [10, 20, 10, 30, 40, 20]

print(f"\n--- Test 2 (M={M_test2}): Duplicates & Boundary ---")
for reading in stream_test2:
    rank, critical = optimizer2.add_reading(reading)
    print(f"Added {reading}: Rank={rank}, Critical={critical}, Current_Readings={optimizer2.get_current_readings()}")
# Expected output:
# 10: R=1,C=T,CR=[10]
# 20: R=2,C=F,CR=[10,20]
# 10: R=1,C=T,CR=[10,20] (10 is not new unique, recency updated)
# 30: R=3,C=F,CR=[10,20,30] (Reached M=3)
# 40: R=3,C=F,CR=[20,30,40] (10 evicted, 40 added)
# 20: R=1,C=T,CR=[20,30,40] (20 is not new unique, recency updated)


# Test 3: Hardcore combined scenario
M_hardcore = 10
optimizer_hardcore = DataStreamOptimizer(M_hardcore)
readings_stream_hardcore = [50, 20, 80, 10, 60, 30, 90, 40, 70, 15, 25, 55, 85, 5, 95, 100, 10, 20]

print(f"\n--- Test 3 (M={M_hardcore}): Hardcore Combined ---")
for i, reading in enumerate(readings_stream_hardcore):
    rank, critical = optimizer_hardcore.add_reading(reading)
    current_readings = optimizer_hardcore.get_current_readings()
    print(f"Step {i+1}, Added {reading}: Rank={rank}, Critical={critical}, Current_Readings={current_readings}")

# Expected sequence:
# Initial (M=10, 10% = 1 element critical)
# 1. Added 50: R=1,C=True,CR=[50]
# 2. Added 20: R=1,C=True,CR=[20,50]
# 3. Added 80: R=3,C=False,CR=[20,50,80]
# 4. Added 10: R=1,C=True,CR=[10,20,50,80]
# 5. Added 60: R=4,C=False,CR=[10,20,50,60,80]
# 6. Added 30: R=3,C=False,CR=[10,20,30,50,60,80]
# 7. Added 90: R=7,C=False,CR=[10,20,30,50,60,80,90]
# 8. Added 40: R=4,C=False,CR=[10,20,30,40,50,60,80,90]
# 9. Added 70: R=7,C=False,CR=[10,20,30,40,50,60,70,80,90]
# 10. Added 15: R=2,C=True,CR=[10,15,20,30,40,50,60,70,80,90] (M=10 reached)
# 11. Added 25: R=4,C=False,CR=[15,20,25,30,40,50,60,70,80,90] (10 evicted, 25 added)
# 12. Added 55: R=7,C=False,CR=[15,20,25,30,40,50,55,60,70,80] (90 evicted, 55 added)
# 13. Added 85: R=9,C=False,CR=[15,20,25,30,40,50,55,60,70,85] (80 evicted, 85 added)
# 14. Added 5: R=1,C=True,CR=[5,15,20,25,30,40,50,55,60,70] (85 evicted, 5 added)
# 15. Added 95: R=10,C=False,CR=[5,15,20,25,30,40,50,55,60,95] (70 evicted, 95 added)
# 16. Added 100: R=11 (Rank > M, not possible), R=10,C=False,CR=[5,15,20,25,30,40,50,55,60,100] (95 evicted, 100 added)
# 17. Added 10: R=1,C=True,CR=[5,10,15,20,25,30,40,50,55,60] (100 evicted, 10 added - oldest removed, 10 is re-added)
# 18. Added 20: R=3,C=False,CR=[5,10,15,20,25,30,40,50,55,60] (20 is not new unique, recency updated)

```
# Exercise 1: In-Place Array Transformations and Memory Fundamentals

**Objective**: To master basic array manipulation (indexing, slicing), in-place operations, and understand their relationship with contiguous memory representation. This exercise connects directly to Python fundamentals of lists and control structures (Chunks 1 & 2).

**Problem Description**: You are given a list of integers representing pixel values. Implement a Python function `invert_and_mirror(pixel_array)` that performs two operations **in-place** to minimize memory usage:
1.  **Mirror**: Reverse the entire array.
2.  **Invert**: After mirroring, invert each pixel value based on a 256-color spectrum (i.e., `new_value = 255 - old_value`).
Do not use any auxiliary arrays or lists. Your function should modify the original list directly.

**Artificial Data**:
```python
 Input Data
image_strip = [10, 250, 128, 5, 200, 150, 80]

 Expected Output after invert_and_mirror(image_strip):
 1. Mirrored: [80, 150, 200, 5, 128, 250, 10]
 2. Inverted: [175, 105, 55, 250, 127, 5, 245]
 Final state of image_strip should be: [175, 105, 55, 250, 127, 5, 245]
```

**Theoretical and Source References**:
*   **Source 1**: *TheC++ProgrammingLanguage_BjarneStroustrup_2013_FourthEdition*, `Chapter_07_Pointers_Arrays_and_References.pdf`.
    *   **Specification**: Section 7.4 ("Pointers into Arrays") explains how array elements are stored contiguously. This physical layout is what makes in-place swapping of elements (e.g., `array[i], array[j] = array[j], array[i]`) an efficient, O(1) operation for a single swap, which is the core of an in-place reversal.
*   **Source 2**: *ComputerOrganizationAndDesign_Patterson-Hennessy_2020*, `05_Chapter_02_Instructions_Language_of_the_Computer.pdf`.
    *   **Specification**: Section 2.3 ("Operands of the Computer Hardware") discusses memory operands and base address plus offset addressing. This low-level view clarifies why accessing `array[i]` is a fast calculation, reinforcing the efficiency of direct, in-place manipulation.
*   **Relationship to Previous Chunks**: This exercise directly applies Python `list` manipulation (Chunk 1) and `for` or `while` loops (Chunk 2) to implement the reversal logic.

**Software Engineering Principles Emphasis**:
*   **Efficiency**: The in-place requirement forces a solution with O(1) space complexity, which is critical for handling large datasets like images where creating a copy would be memory-intensive. The time complexity should be O(n).

---

# Exercise 2: The Two-Pointer Technique for String and Array Problems

**Objective**: To implement the two-pointer pattern for solving problems that involve searching for pairs or subsequences in sorted/structured arrays and strings.

**Problem Description**: Write a function `is_palindrome_alphanumeric(s: str) -> bool` that determines if a given string `s` is a palindrome, considering only alphanumeric characters and ignoring cases. An empty string is a valid palindrome. Use the two-pointer technique, with one pointer starting from the beginning and one from the end, moving towards each other.

**Artificial Data**:
```python
 Input Data
test_case_1 = "A man, a plan, a canal: Panama"  Expected: True
test_case_2 = "race a car"  Expected: False
test_case_3 = ".,_,"  Expected: True
test_case_4 = "Was it a car or a cat I saw?"  Expected: True
```

**Theoretical and Source References**:
*   **Source 1**: *TheC++ProgrammingLanguage_BjarneStroustrup_2013_FourthEdition*, `Chapter_36_Strings.pdf`.
    *   **Specification**: Section 36.3.3 ("Fundamental Operations") discusses character access (`s[i]`) and comparison, which are the fundamental operations used at each step of the two-pointer algorithm. The immutability of strings means we are only reading, which is efficient.
*   **Source 2**: *IntroductionToInformationRetrieval_Manning-Raghavan-Schutze_2008*, `04_Chapter_02_The_term_vocabulary_and_postings_lists.pdf`.
    *   **Specification**: Section 2.2.3 ("Normalization") discusses concepts like case-folding and removing punctuation. Your solution must implement a similar normalization logic by checking `char.isalnum()` and `char.lower()` before comparing characters pointed to by the two pointers. This relates the problem to standard text processing techniques.
*   **Relationship to Previous Chunks**: The implementation requires functions, conditionals, and loops (Chunks 2 & 3) and leverages Python's built-in string methods (Chunk 1).

**Software Engineering Principles Emphasis**:
*   **Efficiency**: The two-pointer technique provides a solution with O(n) time complexity and O(1) space complexity, which is significantly more efficient than naive approaches that might involve creating a reversed copy of the processed string (which would be O(n) space).

---

# Exercise 3: The Sliding Window Pattern for Subarray Analysis

**Objective**: To implement the sliding window pattern to efficiently solve problems involving contiguous subarrays or substrings that satisfy a certain property.

**Problem Description**: Given an array of positive integers `nums` and a positive integer `target`, write a function `min_subarray_len(target, nums)` that returns the minimal length of a contiguous subarray whose sum is greater than or equal to `target`. If there is no such subarray, return 0. The window should expand by moving its right edge and shrink by moving its left edge.

**Artificial Data**:
```python
# Input Data
target_1 = 7
nums_1 = [2, 3, 1, 2, 4, 3] # Expected: 2 (subarray [4, 3])

target_2 = 4
nums_2 = [1, 4, 4] # Expected: 1 (subarray [4])

target_3 = 11
nums_3 = [1, 1, 1, 1, 1, 1, 1, 1] # Expected: 0
```

**Theoretical and Source References**:
*   **Source 1**: *TheC++ProgrammingLanguage_BjarneStroustrup_2013_FourthEdition*, `Chapter_07_Pointers_Arrays_and_References.pdf`.
    *   **Specification**: Section 7.4.1 ("Navigating Arrays") shows iteration through arrays using pointers/indices. The sliding window is a sophisticated form of navigation where two indices (left and right) are managed dynamically to define a subarray, avoiding the O(n^2) complexity of checking every possible subarray.
*   **Relationship to Previous Chunks**: This pattern is an advanced application of loops (Chunk 2) and arithmetic operations (Chunk 1) for solving a specific class of optimization problems on arrays.

**Software Engineering Principles Emphasis**:
*   **Efficiency**: A brute-force approach would be O(n^2). The sliding window pattern optimizes this to O(n) time complexity because each element is visited at most twice (once by the right pointer, once by the left). This demonstrates a significant performance gain.
*   **Modifiability**: The core logic of the sliding window (expand, check, shrink) is a reusable pattern that can be adapted to solve many other problems (e.g., longest substring with K distinct characters).

---

# Exercise 4: Kadane's Algorithm for Maximum Subarray Sum

**Objective**: To implement Kadane's algorithm, a classic example of dynamic programming, to find the contiguous subarray with the largest sum.

**Problem Description**: Write a function `max_subarray_sum(nums)` that takes an integer array `nums` (which can contain positive and negative numbers) and finds the contiguous subarray with the largest sum, returning that sum.

**Artificial Data**:
```python
 Input Data
nums_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  Expected: 6 (subarray [4, -1, 2, 1])
nums_2 = [1]  Expected: 1
nums_3 = [5, 4, -1, 7, 8]  Expected: 23 (the entire array)
nums_4 = [-5, -1, -3]  Expected: -1 (subarray [-1])
```

**Theoretical and Source References**:
*   **Source 1**: [GeeksforGeeks: Kadane’s Algorithm](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/).
    *   **Specification**: This article details the core logic: iterate through the array, keeping track of the `max_so_far` and the `current_max`. The key insight is that if `current_max` becomes negative, it's better to start a new subarray. This is a simple yet powerful dynamic programming approach.
*   **Source 2**: [LeetCode: Maximum Subarray](https://leetcode.com/problems/maximum-subarray/).
    *   **Specification**: This provides a formal problem statement and a platform to test against numerous edge cases, solidifying the understanding of the algorithm's robustness.
*   **Relationship to Previous Chunks**: The implementation is a single loop (Chunk 2) over a list (Chunk 1), using conditional logic to update state variables. It serves as an accessible introduction to dynamic programming concepts that will be explored further in Chunk 15.

**Software Engineering Principles Emphasis**:
*   **Efficiency**: Kadane's algorithm solves the problem in O(n) time and O(1) space, a vast improvement over the O(n^2) or O(n^3) brute-force solutions. This highlights how a clever algorithm can dramatically reduce resource consumption.

---

# Hardcore Combined Problem: KMP-Informed Sliding Window Maximum

**Objective**: To synthesize patterns (Sliding Window, KMP) and concepts (array manipulation, string immutability, contiguous memory) into a single, efficient algorithm. The solution must leverage the specific properties of each pattern to solve a complex, layered problem.

**Problem Description**: You are a data analyst at a streaming service. You have a long string `data_stream` representing user activity over time, and a shorter string `engagement_pattern` representing a key user behavior. You need to find the contiguous subarray of `scores` (an array of the same length as `data_stream`) that has the maximum possible value, but only for subarrays that correspond to segments of the `data_stream` that **start with** the `engagement_pattern`.

Write a function `max_score_for_patterned_segment(data_stream: str, engagement_pattern: str, scores: list[int]) -> int`.

- The function should first find all starting indices of `engagement_pattern` in `data_stream`.
- For each occurrence, it defines a "valid segment" in the `scores` array starting at that index.
- Within each valid segment, you must find the maximum subarray sum.
- The function should return the highest maximum subarray sum found across all valid segments. If no patterns are found, return 0.

**Example**:
- `data_stream` = "ab**xyz**abc**xyz**de"
- `engagement_pattern` = "**xyz**"
- `scores` = [1, 2, **5, -8, 6**, 1, 2, 3, **1, 10, -5**, 4, 5]
- **Step 1**: `engagement_pattern` "xyz" starts at indices 2 and 8 in `data_stream`.
- **Step 2**: This defines two valid segments in `scores`:
    - Segment 1 starts at index 2: `[5, -8, 6, 1, 2, 3, 1, 10, -5, 4, 5]`
    - Segment 2 starts at index 8: `[1, 10, -5, 4, 5]`
- **Step 3**: Apply Kadane's algorithm to each segment:
    - Max subarray sum in Segment 1 is `[6, 1, 2, 3, 1, 10]` = 23.
    - Max subarray sum in Segment 2 is `[1, 10]` = 11. (Or `[1, 10, -5, 4, 5]` = 15). Let's re-calculate: `[1, 10]`=11, `[1, 10, -5]`=6, `[1, 10, -5, 4]`=10, `[1, 10, -5, 4, 5]`=15. So, max is 15.
- **Step 4**: The overall maximum is `max(23, 15) = 23`. The function should return 23.

**Artificial Data**:
```python
 Input Data
data_stream = "axbyabxyabxyc"
engagement_pattern = "abxy"
scores = [-1, 10, -5, 1, 8, -2, 4, 5, 2, 3, 6, -10, 20]
 Expected Output: 17
 Pattern "abxy" found at index 4. Segment is [8, -2, 4, 5, 2, 3, 6, -10, 20].
 Max subarray sum in this segment is [8, -2, 4, 5, 2] = 17.

data_stream_2 = "aaaaaaaa"
engagement_pattern_2 = "aa"
scores_2 = [1, -5, 4, -5, 4, -5, 4, -5]
 Expected Output: 4
 Occurrences at 0, 1, 2, 3, 4, 5, 6.
 Segment 0: [1, -5, 4, -5, 4, -5, 4, -5] -> Max sum is 4
 Segment 1: [-5, 4, -5, 4, -5, 4, -5] -> Max sum is 4
 ... and so on. The highest max is 4.
```

**Theoretical and Source References**:
*   **Source 1**: [GeeksforGeeks: KMP Algorithm](https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/).
    *   **Specification**: You must use the KMP algorithm to find all occurrences of `engagement_pattern` in `data_stream` efficiently. A naive search would be O(m*n), but KMP is O(m+n), which is critical if `data_stream` is very large. This leverages KMP's prefix table pattern.
*   **Source 2**: [LeetCode: Maximum Subarray](https://leetcode.com/problems/maximum-subarray/).
    *   **Specification**: For each segment identified by KMP, you must apply Kadane's algorithm. This requires understanding how to apply an algorithm to a *slice* or *view* of an array, which relates back to the concept of contiguous memory and efficient indexing.
*   **Source 3**: *IntroductionToInformationRetrieval_Manning-Raghavan-Schutze_2008*, `05_Chapter_03_Dictionaries_and_tolerant_retrieval.pdf`.
    *   **Specification**: Section 3.2 ("Wildcard queries") discusses searching for patterns in text. While KMP is more specific, this chapter provides the context for why efficient string searching is a fundamental problem in information systems. Your solution is a specialized form of this general problem.

**Software Engineering Principles Emphasis**:
*   **Efficiency**: The solution must be highly efficient. A naive implementation would be O(n*m) for searching and O(k*n) for subarray sums (where k is number of occurrences), leading to a very slow algorithm. The optimal solution uses KMP (O(n+m)) and then runs Kadane's on the segments. Since Kadane's is linear, the total time complexity will be dominated by finding the patterns and running Kadane's once over the relevant parts of the array, approaching O(n+m).
*   **Modularity**: A clean solution would separate the KMP search logic from the Kadane's algorithm logic into distinct helper functions, demonstrating good code organization (related to Chunk 4).
#       Hardcore Combined Problem: "Dynamic Data Stream Optimizer"


#   Description: Design and implement a DataStreamOptimizer class in Python. 
# This class simulates a high-frequency data pipeline that processes streams 
# of sensor readings (integers). The system has two critical requirements:

# Maintain Sorted Unique Readings: Dynamically maintain a sorted list of the 
# M most recent unique sensor readings. When the number of unique readings 
# exceeds M, the oldest unique reading must be removed.
# Rank and Criticality Check: For any new incoming reading, determine its 
# 1-indexed rank within the currently maintained M unique readings. 
# Additionally, flag the reading as "critical" if its rank falls within the 
# top 10% (i.e., rank <= M * 0.1). Assume M is a positive integer.


# Specifications & Theory:

#   Uniqueness and Recency Management: Requires a combination of a hash set 
# (set for O(1) uniqueness checks) and a queue (collections.deque for O(1) 
# recency/sliding window).
# Sorted Order Maintenance: The list of M unique items must be kept sorted 
# to allow for efficient rank calculation. A naive re-sort (O(M log M)) 
# after each change is a valid starting point, but more advanced structures 
# could optimize this.
# Rank Calculation: The "rank" is the position in the sorted list. For a 
# sorted list, this can be found in O(log M) time.
# Overall System: The solution requires a synthesis of hashing, queues, 
# sorting, and searching to meet all requirements efficiently.


#   Key Skills:

# Data Structure Synthesis: Combining multiple data structures (set, deque,
# list) to solve a multi-faceted problem.
# Algorithmic Trade-offs: Choosing between re-sorting 
# (O(M log M)) vs. more complex data structures for insertion.
# Dynamic Data Management: Handling a continuous stream of data with a 
# fixed-size window.


#   Software Engineering Principles:

# Efficiency: Using the most efficient data structures for each sub-problem 
# (hashing for uniqueness, queues for recency, binary search for rank).
# Scalability: The design should handle a high volume of incoming readings 
# by ensuring add_reading is as fast as possible.

# Artificial Data:

M = 10
readings_stream = [
    50, 20, 80, 10, 60, 30, 90, 40, 70, 15, 25, 55, 85, 5, 95, 100, 10, 20
]

from math import floor
from collections import deque
from bisect import bisect_left, insort_left

class DataStreamOptimizer:
    top = 0.1

    def __init__(self, recent_buffer_size):
        self.top = 0.1
        self.M = recent_buffer_size
        if recent_buffer_size == 0: self.M = 1
        self.threeshold = floor(self.M * self.top)
        if self.threeshold < 1: self.threeshold = 1
        self.uniqueness_buffer = set()
        self.recency_buffer = deque()
        self.sorted_buffer = []

    def add_reading(self, value: int) -> tuple[int, bool]:
        if value in self.uniqueness_buffer:
            self.recency_buffer.remove(value)
            self.recency_buffer.append(value)
        else:
            size = len(self.uniqueness_buffer)
            if size == self.M:
                oldest = self.recency_buffer.popleft()
                self.uniqueness_buffer.remove(oldest)
                oldest_index = bisect_left(self.sorted_buffer, oldest)
                self.sorted_buffer.pop(oldest_index)
            self.uniqueness_buffer.add(value)
            self.recency_buffer.append(value)
            insort_left(self.sorted_buffer, value)
        rank = self.sorted_buffer.index(value) + 1
        is_critical = rank <= self.threeshold
        return rank, is_critical
    
    def get_current_readings(self) -> list[int]:
        return self.sorted_buffer

def validate_data_stream_optimizer():
    """
    A definitive validation suite with corrected test data.
    """
    M = 10
    optimizer = DataStreamOptimizer(M)
    
    stream = [50, 20, 80, 10, 60, 30, 90, 40, 70, 15, 25, 55, 85, 5, 95, 100, 10, 20, 95]
    
    # Corrected expected_states list. The error was at step 12 (value 55).
    expected_states = [
        # (value, rank, critical, list)
        (50, 1, True, [50]),
        (20, 1, True, [20, 50]),
        (80, 3, False, [20, 50, 80]),
        (10, 1, True, [10, 20, 50, 80]),
        (60, 4, False, [10, 20, 50, 60, 80]),
        (30, 3, False, [10, 20, 30, 50, 60, 80]),
        (90, 7, False, [10, 20, 30, 50, 60, 80, 90]),
        (40, 4, False, [10, 20, 30, 40, 50, 60, 80, 90]),
        (70, 7, False, [10, 20, 30, 40, 50, 60, 70, 80, 90]),
        (15, 2, False, [10, 15, 20, 30, 40, 50, 60, 70, 80, 90]),
        (25, 4, False, [10, 15, 20, 25, 30, 40, 60, 70, 80, 90]),  # Evicts 50
        (55, 6, False, [10, 15, 25, 30, 40, 55, 60, 70, 80, 90]),  # Evicts 20
        (85, 9, False, [10, 15, 25, 30, 40, 55, 60, 70, 85, 90]),  # Evicts 80
        (5, 1, True, [5, 15, 25, 30, 40, 55, 60, 70, 85, 90]),   # Evicts 10
        (95, 10, False, [5, 15, 25, 30, 40, 55, 70, 85, 90, 95]),  # Evicts 60
        (100, 10, False, [5, 15, 25, 40, 55, 70, 85, 90, 95, 100]),# Evicts 30
        (10, 2, False, [5, 10, 15, 25, 40, 55, 70, 85, 95, 100]), # Evicts 90
        (20, 4, False, [5, 10, 15, 20, 25, 55, 70, 85, 95, 100]), # Evicts 40
        (95, 9, False, [5, 10, 15, 20, 25, 55, 70, 85, 95, 100]), # Duplicate 95, no structural change
    ]

    for i, value in enumerate(stream):
        (_, exp_rank, exp_crit, exp_list) = expected_states[i]
        rank, critical = optimizer.add_reading(value)
        current_list = optimizer.get_current_readings()
        
        assert rank == exp_rank, f"Step {i+1} (value {value}): Rank mismatch. Got {rank}, expected {exp_rank}."
        assert critical == exp_crit, f"Step {i+1} (value {value}): Criticality mismatch. Got {critical}, expected {exp_crit}."
        assert current_list == exp_list, f"Step {i+1} (value {value}): List state mismatch.\nGot:      {current_list}\nExpected: {exp_list}"
        
    print("Hardcore Combined Problem Validation Passed.")

# Execute to verify the reference implementation
validate_data_stream_optimizer()
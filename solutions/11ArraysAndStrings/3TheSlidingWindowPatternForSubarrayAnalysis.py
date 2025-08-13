target_1 = 7
nums_1 = [2, 3, 1, 2, 4, 3]
target_2 = 4
nums_2 = [1, 4, 4]
target_3 = 11
nums_3 = [1, 1, 1, 1, 1, 1, 1, 1]

def min_subarray_len(target, nums):
    cum_sum = 0
    window_min = 0
    min_seq = float('inf')
    for window_max in range(len(nums)):
        cum_sum += nums[window_max]
        while cum_sum >= target:
            min_seq = min(min_seq, window_max - window_min + 1)
            cum_sum -= nums[window_max]
            window_min += 1
    return 0 if min_seq == float('inf') else min_seq

print(min_subarray_len(target_1, nums_1))
print(min_subarray_len(target_2, nums_2))
print(min_subarray_len(target_3, nums_3))
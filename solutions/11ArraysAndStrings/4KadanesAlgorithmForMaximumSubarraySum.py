# Input Data
nums_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums_2 = [1]
nums_3 = [5, 4, -1, 7, 8]
nums_4 = [-5, -1, -3]
nums_l = [nums_1, nums_2, nums_3, nums_4]

def max_subarray_sum(nums):
    local_max = nums[0]
    global_max = nums[0]
    for i in range(1, len(nums)):
        current_signal = nums[i]
        local_max = max(current_signal, local_max + current_signal)
        global_max = max(local_max, global_max)
    return global_max

for nums in nums_l:
    print(max_subarray_sum(nums))
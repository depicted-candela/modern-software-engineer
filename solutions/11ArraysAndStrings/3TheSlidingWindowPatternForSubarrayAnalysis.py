target_1 = 7
nums_1 = [2, 3, 1, 2, 4, 3]
target_2 = 4
nums_2 = [1, 4, 4]

target_3 = 11
nums_3 = [1, 1, 1, 1, 1, 1, 1, 1]

def min_subarray_len(target, nums):
    seq_num = 0
    iteration = 0
    subarray = []
    finalsubarray = []
    while iteration < len(nums) - 1:
        seq_num += nums[iteration]
        if (seq_num >= target):
            finalsubarray = subarray
            if (iteration < len(nums) - 1):
                subarray.pop(0)
                iteration += 1
                continue
            else: return len(finalsubarray)
        else:
            subarray.append(nums[iteration])
            iteration += 1
    return 0

print(min_subarray_len(target_1, nums_1))
print(min_subarray_len(target_2, nums_2))
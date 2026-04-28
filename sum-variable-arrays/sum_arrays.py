from typing import List


def subarraySum(nums):
    # nums[start,......, i]
    sums = 0
    for i, n in enumerate(nums):
        start = max(0, i - n) # start = max(0, i - nums[i])
        sub_array = nums[start:i+1]
        sums += sum(sub_array)
    return sums
    
        

print(subarraySum([3,1,1,2]))
from typing import List


def subarraySum(nums):
    # nums[start,......, i]
    sums = 0
    for i, n in enumerate(nums):
        start = max(0, i - n) # start = max(0, i - nums[i])
        sub_array = nums[start:i+1]
        sums += sum(sub_array)
    return sums
# better solution using prefix sum to get O(1) range sum instead of O(k) for each subarray sum
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        
        # build prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        total = 0
        for i, num in enumerate(nums):
            start = max(0, i - num)
            total += prefix[i+1] - prefix[start]  # O(1) range sum
        
        return total
        

print(subarraySum([3,1,1,2]))
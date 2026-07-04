from typing import List

# Problem: Count the number of contiguous subarrays whose elements sum to k.
#
# Approach: Prefix Sum + Hash Map
#
# Idea
#   Let currentSum be the prefix sum up to the current index.
#   A subarray ending here sums to k iff there exists an earlier prefix sum
#   `diff` such that:
#       currentSum - diff = k   ->   diff = currentSum - k
#   Every earlier prefix sum equal to `diff` marks the start of a subarray
#   summing to k, so we add how many times we've seen `diff` so far.
#
# Hash map
#   prefixSums maps a prefix sum value -> how many times it has occurred.
#   Seed it with { 0 : 1 } so subarrays starting at index 0 are counted
#   (a prefix sum of exactly k has diff = 0, which must exist once).
#
# Time:  O(n) — single pass, O(1) hash lookups
# Space: O(n) — up to n distinct prefix sums stored


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSums = { 0 : 1 }
        currentSum = 0

        for num in nums:
            currentSum += num
            diff = currentSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[currentSum] = 1 + prefixSums.get(currentSum, 0)
        return res

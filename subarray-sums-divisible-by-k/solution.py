from typing import List

# Problem: Count the number of contiguous subarrays whose sum is divisible by k.
#
# Approach: Prefix Sum + Hash Map (grouping by remainder)
#
# Idea
#   Let currentSum be the prefix sum up to the current index.
#   A subarray sums to a multiple of k iff two prefix sums share the same
#   remainder mod k:
#       (currentSum - earlierSum) % k == 0   <->   currentSum % k == earlierSum % k
#   So for each new prefix sum we look at its remainder `rem` and add how many
#   earlier prefix sums had that same remainder — each pairs with the current
#   index to form a subarray divisible by k.
#
# Remainder note
#   In Python, `%` always returns a non-negative result for a positive k
#   (e.g. -3 % 5 == 2), so negative numbers are handled correctly without
#   any extra normalization.
#
# Hash map
#   seen maps a remainder value -> how many times it has occurred.
#   Seed it with { 0 : 1 } so subarrays whose own sum is divisible by k
#   (remainder 0 with no earlier prefix) are counted.
#
# Time:  O(n) — single pass, O(1) hash lookups
# Space: O(k) — at most k distinct remainders stored


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        seen = { 0 : 1 }
        currentSum = 0

        for num in nums:
            currentSum += num
            rem = currentSum % k

            res += seen.get(rem, 0)
            seen[rem] = 1 + seen.get(rem, 0)
        return res

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = {}
        count = 0
        
        for num in nums:
            if seen.get(k - num, 0) > 0:
                count += 1
                seen[k - num] -= 1
            else:
                seen[num] = seen.get(num, 0) + 1
        return count
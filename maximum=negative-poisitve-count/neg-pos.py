class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 1. Find the count of negative numbers
        # This finds the first index where nums[i] is NOT negative
        def get_neg_count(nums):
            l, r = 0, n
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < 0:
                    l = mid + 1
                else:
                    r = mid
            return l

        # 2. Find the start of positive numbers
        # This finds the first index where nums[i] > 0
        def get_pos_count(nums):
            l, r = 0, n
            while l < r:
                mid = (l + r) // 2
                if nums[mid] <= 0: # Skips negatives and zeros
                    l = mid + 1
                else:
                    r = mid
            return n - l # Total length minus the index where positives start

        neg = get_neg_count(nums)
        pos = get_pos_count(nums)
        
        return max(neg, pos)
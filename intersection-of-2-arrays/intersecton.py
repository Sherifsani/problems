from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Optimization: Ensure nums1 is the smaller array
        # This makes the sorting phase faster!
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        # We sort the smaller array
        nums1.sort()
        res = set()

        # We iterate through the larger array
        for i in nums2:
            l, h = 0, len(nums1) - 1
            while l <= h:
                mid = (l + h) // 2
                if nums1[mid] == i:
                    res.add(i)
                    break
                elif nums1[mid] > i:
                    h = mid - 1
                else:
                    l = mid + 1
        return list(res)
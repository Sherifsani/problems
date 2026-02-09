from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Helper function must be defined BEFORE the main logic calls it
        def binary_search(find_left: bool) -> int:
            l, r = 0, len(nums) - 1
            bound = -1
            
            while l <= r:
                mid = (l + r) // 2
                
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    # We found the target!
                    bound = mid
                    if find_left:
                        # Keep looking to the left to find the starting point
                        r = mid - 1
                    else:
                        # Keep looking to the right to find the ending point
                        l = mid + 1
            return bound

        # Execute the search twice
        start = binary_search(find_left=True)
        end = binary_search(find_left=False)
        
        return [start, end]
from typing import List

class Solution:
    # solution 1 (mapping)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_dict = {}
        res = []
        for i in range(1, len(nums) + 1):
            num_dict[i] = 0
        for i in nums:
            num_dict[i] = i
        return [i for i in num_dict.keys() if num_dict[i] == 0]
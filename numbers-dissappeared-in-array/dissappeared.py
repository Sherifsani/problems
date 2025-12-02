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
    
    # solution 2 (index marking)
    def findDisappearedNumbersII(self, nums: List[int]) -> List[int] :
        # Step 1: Mark the indices of numbers we see
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        # Step 2: Collect numbers whose positions were never marked
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result

# for i in range(len(nums)):
    
#     # if nums[abs(nums[i]) - 1] < 0:
#     #     continue
#     # nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
#     print(nums)
# res = []
# for i in range(len(nums)):
#     if nums[i] > 0:
#         res.append(i + 1)

# print(res)
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = count = 0
        for num in nums:
            if num != 1:
                count = 0
                continue
            count += 1
            longest = max(longest, count)
        return longest

'''

my approach
***********
1. initialize longest and count with 0
2. iterate through nums and if a 1 is reached;
3. increment count and assign longest the greater value of max and longest
4. else, reset count to 0 and skip the iteration entirely
'''
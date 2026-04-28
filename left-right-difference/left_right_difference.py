from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)

        answer = [0] * n
        left_sum = [0] * (n + 1)
        right_sum = [0] * (n + 1)

        for i in range(n):
            left_sum[i+1] = left_sum[i] + nums[i]

        for i in range(n-1,-1,-1):
            right_sum[i] = right_sum[i+1] + nums[i]

        for i in range(n):
            answer[i] = abs(left_sum[i] - right_sum[i + 1])
        return answer

from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        if target not in set(nums):
            return 0

        n = len(nums)
        t = [1 if x == target else -1 for x in nums]

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + t[i]

        def merge_count(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2
            left, left_count = merge_count(arr[:mid])
            right, right_count = merge_count(arr[mid:])

            count = left_count + right_count
            sorted_arr = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    # left[i] < right[j..] since right is sorted ascending
                    count += len(right) - j
                    sorted_arr.append(left[i])
                    i += 1
                else:
                    sorted_arr.append(right[j])
                    j += 1

            sorted_arr.extend(left[i:])
            sorted_arr.extend(right[j:])
            return sorted_arr, count

        _, answer = merge_count(prefix)
        return answer

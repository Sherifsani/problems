from typing import List

# Problem: Count subarrays where `target` appears more than half the time (majority element).
#
# Approach: Prefix Sum + Merge Sort (Count Pairs)
#
# Step 1 — Transform
#   Replace each element with +1 if it equals target, -1 otherwise.
#   Build prefix sums of this transformed array.
#
#   A subarray nums[i..j] has target as majority iff:
#       sum(t[i..j]) > 0
#   Which equals:
#       prefix[j+1] - prefix[i] > 0  →  prefix[i] < prefix[j+1]
#
# Step 2 — Reduce
#   Counting majority subarrays becomes counting pairs (i, k) where:
#       i < k  and  prefix[i] < prefix[k]
#   This is the classic "count non-inversions across halves" problem.
#
# Step 3 — Merge Sort
#   Use divide-and-conquer on the prefix array:
#   - Recursively count valid pairs within each half.
#   - In the merge step, count cross pairs where left[i] < right[j].
#     Since both halves are sorted ascending:
#       if left[i] < right[j], then left[i] < right[j], right[j+1], ..., right[-1]
#       → count += len(right) - j
#   - Merge the two sorted halves as usual.
#
# Time:  O(n log n)  — merge sort on n+1 prefix values
# Space: O(n)        — prefix array + merge sort call stack


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        if target not in set(nums):
            return 0

        n = len(nums)

        # Transform: +1 for target, -1 for everything else
        t = [1 if x == target else -1 for x in nums]

        # Build prefix sums; prefix[0] = 0, prefix[i] = t[0] + ... + t[i-1]
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
                    # All of right[j:] are > left[i] (right is sorted),
                    # so left[i] forms a valid pair with each of them.
                    count += len(right) - j
                    sorted_arr.append(left[i])
                    i += 1
                else:
                    # right[j] <= left[i], so right[j] has no valid left partner yet;
                    # place it and advance j.
                    sorted_arr.append(right[j])
                    j += 1

            sorted_arr.extend(left[i:])
            sorted_arr.extend(right[j:])
            return sorted_arr, count

        _, answer = merge_count(prefix)
        return answer

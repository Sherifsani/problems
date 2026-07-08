from typing import List

# Problem: Return all possible subsets (the power set) of a list of distinct
#          integers. The result must not contain duplicate subsets.
#
# Approach: DFS + Backtracking (include / exclude each element)
#
# Idea
#   Walk the elements by index. At each index i we make a binary choice:
#       1. include nums[i] in the current subset, then recurse on i + 1
#       2. exclude nums[i], then recurse on i + 1
#   Once i reaches the end of the list, `cur` is one complete subset, so we
#   store a copy of it. The two branches together enumerate all 2^n subsets.
#
#   `cur` is a single shared list mutated in place: we append before the
#   include branch and pop after it (backtracking) so it's restored to the
#   right state before taking the exclude branch. cur.copy() is stored so
#   later mutations don't corrupt the saved subset.
#
# Time:  O(n * 2^n) — 2^n subsets, each up to length n to copy
# Space: O(n) — recursion depth and current subset, excluding the output


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, cur):
            # base case: past the last index -> record this subset
            if i >= len(nums):
                res.append(cur.copy())
                return

            # include nums[i]
            cur.append(nums[i])
            dfs(i + 1, cur)

            # exclude nums[i]
            cur.pop()
            dfs(i + 1, cur)

        dfs(0, [])
        return res

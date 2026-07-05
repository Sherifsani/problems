from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Problem: Count the number of downward paths in a binary tree whose node
#          values sum to targetSum. Paths must go from a node to one of its
#          descendants (top -> bottom) but need not start at the root or end
#          at a leaf.
#
# Approach: Prefix Sum + Hash Map, carried along each root-to-node path (DFS)
#
# Idea
#   This is the tree version of "subarray sum equals k". Along any single
#   root-to-node path, currentSum is the running sum from the root.
#   A path ending at the current node sums to targetSum iff some ancestor
#   prefix sum `diff` exists such that:
#       currentSum - diff = targetSum   ->   diff = currentSum - targetSum
#   Each ancestor prefix equal to `diff` marks the start of a valid path, so
#   we add how many times we've seen `diff` on the current path.
#
# Hash map
#   sums maps a prefix sum value -> how many times it occurs on the path from
#   the root to the current node. Seed with { 0 : 1 } so paths starting at the
#   root are counted (diff of 0 must exist once).
#
# Backtracking
#   The map must reflect only the ancestors of the current node. After
#   recursing into both children we decrement sums[currentSum] to remove this
#   node before returning to the parent, so sibling subtrees don't see it.
#
# Time:  O(n) — each node visited once, O(1) hash work per node
# Space: O(h) — recursion depth plus prefix sums along one path (h = tree height)


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sums = { 0 : 1 }
        currentSum = 0

        def dfs(node, sums, currentSum):
            if not node:
                return 0
            count = 0
            currentSum += node.val
            diff = currentSum - targetSum
            if diff in sums:
                count += sums[diff]
            sums[currentSum] = sums.get(currentSum, 0) + 1
            count += dfs(node.left, sums, currentSum)
            count += dfs(node.right, sums, currentSum)
            sums[currentSum] -= 1
            return count

        return dfs(root, sums, currentSum)

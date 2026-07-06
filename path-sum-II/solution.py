from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Problem: Return every root-to-leaf path whose node values sum to targetSum.
#          A leaf is a node with no children; each returned path must start at
#          the root and end at a leaf.
#
# Approach: DFS + Backtracking
#
# Idea
#   Walk down the tree tracking `remaining`, the amount still needed to reach
#   targetSum. Subtract each node's value as we descend. When we hit a leaf
#   with remaining == 0, the current path is a valid answer.
#
#   `path` holds the nodes on the current root-to-current-node route. We append
#   on entry and pop on exit (backtracking) so the same list is reused across
#   the whole traversal. A copy (path[:]) is stored in res when a match is found
#   so later mutations don't corrupt the saved answer.
#
# Time:  O(n^2) worst case — visiting n nodes, and copying a path can cost O(n)
# Space: O(h) — recursion depth and current path (h = tree height),
#               excluding the output list


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, remaining, path):
            if not node:
                return

            remaining = remaining - node.val
            path.append(node.val)

            if not node.left and not node.right:
                if remaining == 0:  # leaf reached with full sum -> valid path
                    res.append(path[:])

            dfs(node.left, remaining, path)
            dfs(node.right, remaining, path)

            path.pop()

        dfs(root, targetSum, [])
        return res

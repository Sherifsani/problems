from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def maxZigZag(node, direction, path):
            if not node:
                return 0
            res[0] = max(path, res[0])
            maxZigZag(node.left, "left", 1 if direction == "left" else path + 1)
            maxZigZag(node.right, "right", 1 if direction == "right" else path + 1)

        maxZigZag(root.left, "left", 1)
        maxZigZag(root.right, "right", 1)
        return res[0]

'''
Logic:
- Use DFS to traverse every node.
- At each node, track the direction we came from and the current zigzag path length.
- If we came from the same direction (e.g., left->left), reset path to 1.
- If we changed direction (e.g., left->right), increment path by 1.
- Keep a global max (`res[0]`) updated at each node.
- Start by pretending we came from root going left and right with path length 1.
'''

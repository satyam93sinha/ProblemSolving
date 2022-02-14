"""
Maximum Depth of Binary Tree == Height of Binary Tree
Number of nodes along the longest path from root to the farthest leaf

Edge Cases:
1. Root is None; return 0
2. Tree is completely left/right heavy
3. Single node, i.e., root; return 1
4. Tree is balanced; calculate height
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base condition
        if not root:
            return 0
        # hypothesis
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        
        # induction
        height = 1 + max(left_height, right_height)
        return height
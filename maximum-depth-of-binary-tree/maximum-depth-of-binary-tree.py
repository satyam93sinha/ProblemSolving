"""
Maximum Depth of Binary Tree == Height of Binary Tree
Here, it is number of nodes along the longest path from root to the farthest leaf

Edge Cases:
1. Root is None; return 0
2. Tree is single-sided left/right heavy
3. Single node, i.e., root; return 1
4. Tree is balanced/unbalanced; calculate height

Test Cases:
[3,9,20,null,null,15,7]
[]
[1]
[3, 9, null, 8, null, 7]
[3, null, 9, null, 8, null, 7]
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
        
        # hypothesis => find solution for smaller chunks/take decision which reduces the input
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        
        # induction => build up the answer
        height = 1 + max(left_height, right_height)
        return height
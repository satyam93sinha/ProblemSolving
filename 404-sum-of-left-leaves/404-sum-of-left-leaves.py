# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def helper(root, path):
            nonlocal sum_left_leaves
            if not root:
                return 0
            left = helper(root.left, 'left')
            right = helper(root.right, 'right')
            if path == 'left' and not root.left and not root.right:
                sum_left_leaves += root.val
        
        sum_left_leaves = 0
        helper(root, 'root')
        return sum_left_leaves
        
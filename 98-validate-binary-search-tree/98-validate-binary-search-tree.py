# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode, min_ = float('-inf'), max_ = float('inf')) -> bool:
        if not root:
            return True
        return (min_<root.val<max_
               and self.isValidBST(root.left, min_, root.val)
               and self.isValidBST(root.right, root.val, max_))
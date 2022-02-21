# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror(root, root)
    
    def is_mirror(self, root_left, root_right) -> bool:
        if not root_left and not root_right:
            return True
        if not root_left or not root_right:
            return False
        return(root_left.val == root_right.val
               and self.is_mirror(root_left.left, root_right.right)
               and self.is_mirror(root_left.right, root_right.left))

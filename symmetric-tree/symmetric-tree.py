# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.symmetric(root, root)
    
    def symmetric(self, left_root, right_root) -> bool:
        if not left_root and not right_root:
            return True
        elif left_root and right_root:
            if left_root.val != right_root.val:
                return False
            else:
                return self.symmetric(left_root.left, right_root.right) and self.symmetric(left_root.right, right_root.left)
        
        else:
            return False
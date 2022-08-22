# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror(root, root)
    
    def is_mirror(self, root1, root2) -> bool:
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        else:
            return ((root1.val == root2.val)
                    and (self.is_mirror(root1.left, root2.right))
                        and (self.is_mirror(root1.right, root2.left)))
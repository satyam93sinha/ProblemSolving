# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # root's value is less than low, everything in left will be lesser than root's value so need to discard all of the left part
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        # root's value is greater than high, everything in right will be greater than root's value so need to discard all of the right part
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        # root value lies in the range of (low, high)
        # thus, root will be included
        # decision to include root is made so shortening the tree
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
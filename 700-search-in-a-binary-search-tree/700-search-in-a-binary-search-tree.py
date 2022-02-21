# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.parent_search_BST(root, val)
    
    def parent_search_BST(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        # hypothesis
        if val < root.val:
            left = self.parent_search_BST(root.left, val)
            return left
        else:
            right = self.parent_search_BST(root.right, val)
            return right
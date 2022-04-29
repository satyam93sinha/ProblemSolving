# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def preorder_traversal(root):
            nonlocal traverse
            if not root:
                return
            traverse.append(root.val)
            preorder_traversal(root.left)
            preorder_traversal(root.right)
        
        traverse = []
        preorder_traversal(root)
        return traverse
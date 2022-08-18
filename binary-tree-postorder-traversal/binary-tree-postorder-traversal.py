# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []
        
        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            postorder.append(root.val)
        
        helper(root)
        return postorder
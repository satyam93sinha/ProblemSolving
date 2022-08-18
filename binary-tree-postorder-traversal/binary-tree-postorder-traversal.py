# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []
        stack = []
        
        while stack or root:
            if root:
                stack.append(root)
                postorder.append(root.val)
                root = root.right
            else:
                root = stack.pop()
                root = root.left
        
        postorder.reverse()
        return postorder
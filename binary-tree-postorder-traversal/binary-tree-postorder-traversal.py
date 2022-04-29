# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        current = root
        tree_postorder_traversal = []
        while stack or current:
            if current:
                stack.append(current)
                tree_postorder_traversal.append(current.val)
                current = current.right
            else:
                current = stack.pop()
                current = current.left
        
        return tree_postorder_traversal[::-1]
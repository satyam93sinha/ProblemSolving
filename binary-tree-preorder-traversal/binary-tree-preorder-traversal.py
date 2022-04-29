# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        current = root
        tree_preorder_traversal = []
        while stack or current:
            if current:
                tree_preorder_traversal.append(current.val)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        return tree_preorder_traversal
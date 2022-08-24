# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # preorder iterative
        # node, left, right order
        stack = []
        preorder = []
        current = root
        while current or stack:
            if current:
                stack.append(current)
                preorder.append(current.val)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
                preorder.append("None")
        
        stack = []
        preorder_right_left = []
        while root or stack:
            if root:
                stack.append(root)
                preorder_right_left.append(root.val)
                root = root.right
            else:
                root = stack.pop()
                root = root.left
                preorder_right_left.append("None")
        
        # print("preorder:", preorder)
        # print("preorder_right_left:", preorder_right_left)
        return preorder == preorder_right_left
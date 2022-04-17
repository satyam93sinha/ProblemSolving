# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            # change nodes, build answer
            node.left = None
            self.current.right = node
            self.current = node
            
            inorder(node.right)
        
        answer = self.current = TreeNode(-1)
        inorder(root)
        return answer.right
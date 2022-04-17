# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.inorder_BST_array = []
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        self.inorder_BST(root) # array containing sorted elements is built
        dummy = current = TreeNode()
        
        for value in self.inorder_BST_array:
            current.right = TreeNode(value)
            current = current.right
        
        return dummy.right
    
    def inorder_BST(self, root: TreeNode):
        if not root:
            return None
        self.inorder_BST(root.left)
        self.inorder_BST_array.append(root.val)
        self.inorder_BST(root.right)
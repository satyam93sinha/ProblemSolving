'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        # Code here
        ancestor = float('inf')
        inorderSuccessorVal = -1
        while root:
            if root.data > x.data and ancestor > root.data:
                ancestor = root.data
            if x.data < root.data:
                root = root.left
            elif x.data > root.data:
                root = root.right
            else:
                if root.right:
                    root = root.right
                    while root.left:
                        root = root.left
                    return root.data
                else:
                    return ancestor if ancestor != float('inf') else -1
        
        return inorderSuccessorVal
                
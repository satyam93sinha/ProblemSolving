"""
Edge Cases:
1. root is None; return None; not possible, a constraint
2. p is not present in the BST; search for the inorder successor value
3. p has right subtree => find min in right subtree of p and return its value
4. p does not have right subtree => parent is the inorder successor

Test Cases:
[]
3
[4]
5
[4]
3
[5,3,6,2,4,null,null,1]
6
[8,4,6, null, 7, null, null, 5]
4
[8,4,6, null, 7, null, null, 5]
3
[2, 1, 3]
1

Approaches:
1. Brute Force
Intuition:
Find the inorder traversal of the BST and store it in an array. Then, iterate over the array and return the value that is either first greater than given p. We can also use binary search to find this number/index and return the answer making this search in O(logn) though the inorder traversal takes O(n).
Time: O(n)
Space: O(n) for skewed trees or O(height of the BST)

2. Use inorder property to find inorder successor
Intuition:
Break the problem -> 
 i) Find p node in the BST.
 ii) Find min in p's right subtree if right subtree is present.
 iii) If right subtree is not present, look for ancestors greater than p.val value
Time: O(height of the BST)
Space: O(1) if we use while loop for all the operation else recursion will have recursive stack leading to O(height of the BST) space complexity.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        p = self.find(root, p)
        successor = None
        if not p:
            return None
        if p.right:
            successor = self.find_min(p.right)
        else:
            successor = self.find_ancestor(root, p)
        return successor
    
    def find(self, root: TreeNode, p: TreeNode) -> TreeNode:
        while root.val != p.val:
            if p.val < root.val:
                root = root.left
            else:
                root = root.right
        return root
    
    def find_min(self, root) -> TreeNode:
        while root.left:
            root = root.left
        return root
    
    def find_ancestor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        successor = None
        while root.val != p.val:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right
        
        return successor
            
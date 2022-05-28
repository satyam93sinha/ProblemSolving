"""
Edge Cases:
1. root is null; not possible, a constraint; return True
2. only root is present; return True
3. single sided left-heavy tree; check if BST
4. single sided right-heavy tree; check if BST
5. unbalanced/balanced binary tree; check if BST

Test Cases:
[]
[2]
[1, 2, null, 3]
[3, 2, null, 1]
[1, null, 2, null, 3]
[3, null, 2, null, 1]
[2, 1, 3]
[5, 1, 4, null, null, 3, 6]

Approaches:
1. Brute Force :: Credit mycodeschool youtube channel
Intuition:
Check for four things -
i) IsSubtreeLesser(root, value) -> checks if given root.val is lesser than the provided value(provided value is the root node's value)
ii) IsSubtreeGreater(root, value)
iii) IsBinarySearchTree(root.left) -> checks if given root is also a BST
iv) IsBinarySearchTree(root.right)
Time: O(n^2) => because it looks into all the n node's value n times
Space: O(height of the tree) => recursive stack space

2. Optimised :: Credit mycodeschool youtube channel
Intuition:
Maintain a min and max value, root.val should be in range(min, max) and we have to check for BST for every node.
Time: O(n)
Space: O(height of the BST) => recursive stack space
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, min_val, max_val):
            if not root:
                return True
            return (min_val < root.val < max_val 
                    and helper(root.left, min_val, root.val)
                    and helper(root.right, root.val, max_val))
        
        return helper(root, float('-inf'), float('inf'))
        
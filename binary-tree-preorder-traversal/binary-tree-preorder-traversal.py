"""
Edge Cases:
1. root is None
2. left-sided binary tree
3. right-sided binary tree
4. left-heavy or right-heavy binary tree
5. balanced binary tree

Test cases:
[]
[1, null, 2, 3]
[1, 2, null, 3]
[1, null, 2, null, 3]
[1, 2, null, 3, 4]
[1, null, 2, 3, 4]

Approaches:
1. Use Recursion
Time: O(n) 
Space: O(n) recursive stack
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        def helper(root):
            if not root:
                return
            preorder.append(root.val)
            helper(root.left)
            helper(root.right)
        
        helper(root)
        return preorder
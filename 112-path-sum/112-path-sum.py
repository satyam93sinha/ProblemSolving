"""
Edge Cases:
1. Tree is empty; no root node; false because no root-to-leaf paths
2. Tree has single node, root == leaf node, return True iff root.val == targetSum
3. Tree has multiple nodes, 
    3.1 tree has root-to-leaf path equalling targetSum, return True
    3.2 tree does not have targetSum in root-to-leaf path, return False
    
Approaches:
1. Brute Force - recursion
Intuition:
We have to find a root-to-leaf path that equals given targetSum. Thus, we subtract the root.val at every recursive call from targetSum dealing only with root, its children and targetSum.
Time: O(N) visiting every node exactly once
Space: O(N) recursive call stack would be O(N) iff its left/right heavy tree, in case of balanced binary tree O(logN)

2. Iteration
Intuition:
curr_sum = targetSum
curr_sum -= node.val
append node and curr_sum to a stack and pop it with every iteration to see if we have a leaf node and curr_sum equal to 0.
Time: O(N) visiting every node exactly once
Space: O(N) to store nodes in stack
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # iteration
        stack = [[root, targetSum - root.val]] if root else []
        
        while stack:
            node, curr_sum = stack.pop()
            if (not node.left 
                and not node.right 
                and curr_sum == 0):
                return True
            
            if node.left:
                stack.append([node.left, 
                                curr_sum - node.left.val])
            if node.right:
                stack.append([node.right, 
                              curr_sum - node.right.val])
        
        return False
        
        
        
        """
        # recursion
        # edge case-1 and when we go beyond leaves with no root
        if not root:
            return False
        
        # if leaf node is found and targetSum == root.val,
        # we found our root to leaf path
        if not root.left and not root.right:
            return targetSum == root.val
        
        # go left and right of node to find targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        """
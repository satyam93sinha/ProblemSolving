"""
Edge Cases:
1. root is None; return empty list?
2. tree has only one node, i.e., root; return [[root.val]]
3. balanced or unbalanced tree, i.e., do level-order traversal
4. left heavy tree with no right child;
5. right heavy tree with no left child;

Test Cases:
1. root = []
2. root = [1]
3. root = [3, 9, 20, null, null, 15, 7]
4. root = [3, 8, null, 7, null, 5, null]
5. root = [3, null, 8, null, 9, null, 10]

Approaches:
1. Brute Force
Intuition:
Level Order => Breadth First Search algorithm will be used => Queue DS

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = collections.deque()
        level_order_traversal = []
        if root:
            queue.append(root)
        while queue:
            length = len(queue)
            current_level = []
            for _ in range(length):
                popped_node = queue.popleft()
                current_level.append(popped_node.val)
                
                if popped_node.left:
                    queue.append(popped_node.left)
                    
                if popped_node.right:
                    queue.append(popped_node.right)
                
            level_order_traversal.append(current_level)
        
        return level_order_traversal
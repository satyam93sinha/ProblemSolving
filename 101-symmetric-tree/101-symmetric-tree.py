# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque()
        queue.append(root)
        queue.append(root)
        
        while queue:
            node1, node2 = queue.popleft(), queue.popleft()
            if not node1 and not node2:
                continue
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val:
                return False
            else:
                # symmetric, node1's left and node2's right match
                queue.append(node1.left)
                queue.append(node2.right)
                queue.append(node1.right)
                queue.append(node2.left)
        
        return True
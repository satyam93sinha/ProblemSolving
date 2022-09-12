# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # iterative
        queue = collections.deque()
        if root:
            queue.append(root)
            queue.append(root)
            
        while queue:
            length = len(queue)
            for _ in range(length//2):
                node1 = queue.popleft()
                node2 = queue.popleft()
                # unequal nodes, not mirrors
                if not node1 and not node2:
                    continue
                if not node1 or not node2:
                    return False
                if node1.val != node2.val:
                    return False
                
                # mirrors
                queue.append(node1.left)
                queue.append(node2.right)
                
                queue.append(node1.right)
                queue.append(node2.left)
                
        return True
        
        
        """
        # recursive, top-down approach
        def is_mirror(root1, root2) -> bool:
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            return (root1.val == root2.val) and is_mirror(root1.left, root2.right) and is_mirror(root1.right, root2.left)
        
        return is_mirror(root, root)
        """
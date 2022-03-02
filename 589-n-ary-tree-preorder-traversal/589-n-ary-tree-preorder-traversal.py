"""
Edge Cases:
1. root is None; return []
2. root is present; has single child then branching into n-ary tree;
    1
     \
      2
     / | \ \
    3  6 4 5
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        def preorder_traversal(node):
            if not node:
                return
            output.append(node.val)
            for child in node.children:
                preorder_traversal(child)
        
        output = []
        preorder_traversal(root)
        return output
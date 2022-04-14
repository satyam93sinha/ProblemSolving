# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base condition when root is absent or,
        # root becomes None, value is not found
        if not root:
            return None
        else:
            # value would be either less or greater than root.val
            if val < root.val:
                return self.searchBST(root.left, val)
            elif val > root.val:
                return self.searchBST(root.right, val)
            else:
                # value is found
                return root
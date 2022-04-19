class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def find_two_swapped(root: TreeNode):
            nonlocal x, y, pred
            if root is None:
                return
            
            find_two_swapped(root.left)
            if pred and root.val < pred.val:
                y = root
                # first swap occurence
                if x is None:
                    x = pred 
                # second swap occurence
                else:
                    return
            pred = root
            find_two_swapped(root.right)
        
        x = y = pred = None
        find_two_swapped(root)
        x.val, y.val = y.val, x.val
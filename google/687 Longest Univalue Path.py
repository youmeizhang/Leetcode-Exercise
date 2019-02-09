class Solution:
    def longestUnivaluePath(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        
        self.res = 0
        
        def tranverse(root):
            if not root:
                return 0
            left = tranverse(root.left)
            right = tranverse(root.right)
            
            pr, pl = 0, 0
            if root.left and root.left.val == root.val:
                pl = 1 + left
            if root.right and root.right.val == root.val:
                pr = 1 + right
            self.res = max(self.res, pr + pl)
            return max(pr, pl)
            

        tranverse(root)
        return self.res
            

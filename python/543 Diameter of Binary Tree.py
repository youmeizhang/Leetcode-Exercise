class Solution:
    def diameterOfBinaryTree(self, root):
        self.res = 0
        
        def tranverse(root):
            if not root:
                return 0
            left = tranverse(root.left)
            right = tranverse(root.right)
            self.res = max(self.res, left + right)
            
            return max(left, right) + 1
        
        tranverse(root)
        return self.res

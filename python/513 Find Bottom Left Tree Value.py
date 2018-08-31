class Solution:
    def findBottomLeftValue(self, root):
        num = 1
        self.max = 1
        self.res = TreeNode(root.val)
        
        def tranverse(root, num):
            if root.left: tranverse(root.left, num+1)
            if root.right: tranverse(root.right, num+1)
                
            if num > self.max:
                self.max = num
                self.res = root
        
        tranverse(root, num)
        
        return self.res.val

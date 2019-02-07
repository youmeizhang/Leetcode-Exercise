class Solution:
    def findSecondMinimumValue(self, root: 'TreeNode') -> 'int':
        self.res = []
        
        def tranverse(root):
            if not root:
                return 
            self.res.append(root.val)
            tranverse(root.left)
            tranverse(root.right)
            
        tranverse(root)
        if len(list(set(self.res))) <= 1:
            return -1
        
        return list(sorted(set(self.res)))[1]

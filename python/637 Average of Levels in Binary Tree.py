class Solution:
    def averageOfLevels(self, root):
        self.tmp = []
        self.res = []
        def tranverse(root, level):
            if root is None:
                return
            if level == 1:
                self.tmp.append(root.val)
                
            elif level > 1:
                tranverse(root.left, level - 1)
                tranverse(root.right, level - 1)
                
        
        def height(root):
            if root is None:
                return 0
            lheight = height(root.left)
            rheight = height(root.right)
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1
                
        def printvalue(root):
            h = height(root)
            for i in range(1, h+1):
                tranverse(root, i)
                self.res.append(sum(self.tmp) / len(self.tmp))
                self.tmp = []
                
        printvalue(root)
        return self.res

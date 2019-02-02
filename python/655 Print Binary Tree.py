class Solution:
    def printTree(self, root):
        
        def height(root):
            if not root:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            return max(lh + 1, rh + 1)
        
        h = height(root)
        self.matrix = [[""] * (2**h - 1) for _ in range(h)]
        
        def tranverse(root, level, pos):
            if not root:
                return
            
            pad = 2**(h-level-1) - 1
            space = 2**(h-level) - 1
            
            index = pad + (space + 1) * pos
            self.matrix[level][index] = str(root.val)
            tranverse(root.left, level + 1, pos << 1)
            tranverse(root.right, level + 1, (pos << 1) + 1)
            
        tranverse(root, 0, 0)
        return self.matrix
            

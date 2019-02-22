class Solution(object):
    def closestValue(self, root, target):
        self.min_diff = float('inf')
        self.ans = root.val
        
        def tranverse(root):
            if not root:
                return
            diff = abs(root.val - target)
            if diff < self.min_diff:
                self.min_diff = diff
                self.ans = root.val
                
            tranverse(root.left)
            tranverse(root.right)
            
        tranverse(root)
        return self.ans
            

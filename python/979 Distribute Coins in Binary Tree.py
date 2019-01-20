class Solution(object):    
    def distributeCoins(self, root):
        self.ans = 0
        
        def tranverse(root):
            res = 0
            if not root:
                return 0
            left = tranverse(root.left)
            right = tranverse(root.right)
            self.ans += abs(left) + abs(right)
            res = root.val + left + right - 1
            return res
            
        tranverse(root)
        return self.ans

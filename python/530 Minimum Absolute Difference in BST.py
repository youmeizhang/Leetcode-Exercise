class Solution:
    def getMinimumDifference(self, root):
        val = []
        
        def tranverse(root):
            if not root:
                return
            val.append(root.val)
            tranverse(root.left)
            tranverse(root.right)
    
        tranverse(root)
        
        val = sorted(val)
        ans = val[1] - val[0]
        
        n = len(val)
        for i in range(2, n):
            ans = min(val[i] - val[i - 1], ans)
        return ans

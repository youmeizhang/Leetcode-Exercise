# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.res = []
        self.ans = float('inf')
        def helper(root):
            if not root:
                return
            
            if root.left:
                helper(root.left)
                
            self.res.append(root.val)
            
            if root.right:
                helper(root.right)
        helper(root)
        
        n = len(self.res)
        
        for i in range(1, n):
            self.ans = min(self.ans, abs(self.res[i] - self.res[i-1]))
        return self.ans

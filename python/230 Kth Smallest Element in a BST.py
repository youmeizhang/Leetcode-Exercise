# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = 0
        self.count = 0
        
        def dfs(root, k):
            if not root:
                return
            dfs(root.left, k)
            self.count += 1
            if self.count == k:
                self.res = root.val
            dfs(root.right, k)
            
        dfs(root, k)
        return self.res
            
        

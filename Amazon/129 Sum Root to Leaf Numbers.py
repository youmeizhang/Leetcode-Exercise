#credit to: https://blog.csdn.net/aliceyangxi1987/article/details/50549460

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        if not root:
            return 0
        return self.dfs(root, 0)
        
    def dfs(self, root, val):        
        val = val * 10 + root.val
        
        if (root.right or root.left) is None:
            return val
        
        total = 0
        if root.left:
            total += self.dfs(root.left, val)
        if root.right:
            total += self.dfs(root.right, val)
            
        return total
            
        """
        :type root: TreeNode
        :rtype: int
        """
        

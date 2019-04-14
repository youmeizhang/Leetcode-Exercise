# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        res = [0]
        
        def dfs(root):
            if not root:
                return True
            
            if root.left is None and root.right is None:
                res[0] += 1
                return True
                
            left = dfs(root.left)
            right = dfs(root.right)
            if left and right and (root.left is None or root.left.val == root.val) and (root.right is None or root.right.val == root.val):
                res[0] += 1
                return True
            else:
                return False
            
        dfs(root) 
        return res[0]
        """
        :type root: TreeNode
        :rtype: int
        """
        

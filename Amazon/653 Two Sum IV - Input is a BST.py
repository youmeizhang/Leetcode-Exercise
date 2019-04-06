# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        self.dic = {}
        self.res = []
        def dfs(root):
            if not root:
                return 
            if (k - root.val) in self.dic:
                self.res.append([root.val, k-root.val])
            else:
                self.dic[root.val] = 0
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        if len(self.res) > 0:
            return True
        else:
            return False
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, sum_):
        
        res = []
        path = []
        
        self.dfs(root, sum_, path, res)
        return res
    
    def dfs(self, root, sum_, path, res):
        if not root:
            return
        temp = sum_
        path.append(root.val)
        
        for i in range(len(path) - 1, -1, -1):
            temp -= path[i]
            if temp == 0:
                res.append(path[i:])
        
        self.dfs(root.left, sum_, path, res)
        self.dfs(root.right, sum_, path, res)
        path.pop()
        
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
# unknown error why it does not pass one test case

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, sum_):
        self.res = []
        
        def helper(root, target, ls):
            if not root:
                return
            test(root, target, ls)
            helper(root.left, target, ls)
            helper(root.right, target, ls)
        
        def test(root, target, ls):
            if not root:
                return
            if root.val == target:
                ls.append(root.val)
                self.res.append(ls)
            
            test(root.right, target - root.val, ls + [root.val])
            
            test(root.left, target - root.val, ls + [root.val])
        
        helper(root, sum_, [])
        
        return self.res
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        
                

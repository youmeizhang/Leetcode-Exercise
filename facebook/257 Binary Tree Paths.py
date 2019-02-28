# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        
        def dfs(root, path_list, res):
            if not root:
                return
            path_list.append(str(root.val))
            if not root.left and not root.right:
                res.append("->".join(path_list))
            
            if root.left:
                dfs(root.left, path_list, res)
            if root.right:
                dfs(root.right, path_list, res)
            path_list.pop()
        
        path_list = []
        res = []
        dfs(root, path_list, res)
        return res
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        

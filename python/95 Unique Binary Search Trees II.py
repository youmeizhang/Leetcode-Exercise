# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        
        def helper(start, end):
            if start > end:
                return [None, ]
            res = []
            for i in range(start, end+1):
                left_tree = helper(start, i-1)
                right_tree = helper(i+1, end)
                
                for l in left_tree:
                    for r in right_tree:
                        curr_tree = TreeNode(i)
                        curr_tree.left = l
                        curr_tree.right = r
                        res.append(curr_tree)
            return res
        
        return helper(1, n) if n else []
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        

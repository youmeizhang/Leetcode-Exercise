# credit to: https://leetcode.com/superluminal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        res = [0]
        
        def helper(node, a, b):
            if node is None:
                return
            res[0] = max(res[0], abs(node.val - a), abs(node.val - b))
            a = min(a, node.val)
            b = max(b, node.val)
            helper(node.left, a, b)
            helper(node.right, a, b)
            
        helper(root, root.val, root.val)
            
        return res[0]
    
        """
        :type root: TreeNode
        :rtype: int
        """
        

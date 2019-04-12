# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        point = root
        while point:
            if p.val > point.val and q.val > point.val:
                point = point.right
            elif p.val < point.val and q.val < point.val:
                point = point.left
            else:
                return point
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        

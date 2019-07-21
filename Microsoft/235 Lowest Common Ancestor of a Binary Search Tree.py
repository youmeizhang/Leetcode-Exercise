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
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p, q):
            
            if not root or root.val == p or root.val == q:
                
                return root
            if root.val < p and root.val < q:
                return helper(root.right, p, q)
            elif root.val > q and root.val > p:
                return helper(root.left, p, q)
            else:
                
                return root
            
        return helper(root, p.val, q.val)

        
            

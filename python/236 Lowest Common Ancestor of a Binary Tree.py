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

            right = helper(root.right, p, q)
            left = helper(root.left, p, q)
                
            if right and left:
                return root
            return left if left else right
        
        return helper(root, p.val, q.val)

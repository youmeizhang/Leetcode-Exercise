# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        def tranverse(root):
            if not root:
                return 0, None
            d1, node1 = tranverse(root.left)
            d2, node2 = tranverse(root.right)
            if d1 > d2:
                return d1 + 1, node1
            elif d1 < d2:
                return d2 + 1, node2
            else:
                return d1 + 1, root
            
        
        return tranverse(root)[1]
            
        

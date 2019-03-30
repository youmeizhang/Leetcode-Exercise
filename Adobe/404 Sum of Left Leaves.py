# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        self.res = 0
        def tranverse(root):
            if not root:
                return
            if root.left:
                if not root.left.left and not root.left.right:
                    self.res += root.left.val
                tranverse(root.left)
            if root.right:
                tranverse(root.right)
        tranverse(root)
        return self.res
        """
        :type root: TreeNode
        :rtype: int
        """
        

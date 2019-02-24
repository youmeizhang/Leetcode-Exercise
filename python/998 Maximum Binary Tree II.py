# credit to: https://blog.csdn.net/fuxuemingzhu/article/details/87904081

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        if not root:
            return TreeNode(val)
        if val > root.val:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
        return root
        
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        

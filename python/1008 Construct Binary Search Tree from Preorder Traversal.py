# credit to: https://blog.csdn.net/fuxuemingzhu/article/details/88379241

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None
        n = len(preorder)
        root = TreeNode(preorder[0])
        i = 1
        while i < n:
            if preorder[i] > preorder[0]:
                break
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        
        

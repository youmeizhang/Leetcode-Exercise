# credit to: https://blog.csdn.net/fuxuemingzhu/article/details/88379241

# O(N^2)
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
        
# credit to: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/discuss/252232/JavaC%2B%2BPython-O(N)-Solution   

# O(N) since construct is called exactly N times
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.i = 0
        def construct(preorder, bound):
            if self.i == len(preorder) or preorder[self.i] > bound:
                return None
            root = TreeNode(preorder[self.i])
            self.i += 1
            root.left = construct(preorder, root.val)
            root.right = construct(preorder, bound)
            return root
        
        return construct(preorder, float('inf'))
        
        

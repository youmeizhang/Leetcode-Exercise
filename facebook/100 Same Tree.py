# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        self.pl = ""
        self.ql = ""
        
        def tranverse(root):
            if not root:
                self.pl += "#"
                return 
            self.pl += str(root.val)
            
            tranverse(root.left)
            tranverse(root.right)
            
        def tranverse2(root):
            if not root:
                self.ql += "#"
                return 
            self.ql += str(root.val)
            
            tranverse2(root.left)
            tranverse2(root.right)
            
        tranverse(p)
        tranverse2(q)
        
        return self.pl == self.ql
    
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        

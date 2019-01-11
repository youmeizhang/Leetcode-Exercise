# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        res = []
        def tranverse(root):
            res.append('(')
            if root is not None and (root.left is not None or root.right is not None):
                res.append(str(root.val))
                tranverse(root.left)
                tranverse(root.right)
                if res[-1] == ")" and res[-2] == "(":
                    res.pop()
                    res.pop()
                res.append(')')
            elif root is not None and root.left is None and root.right is None:
                res.append(str(root.val))
                res.append(')')
            elif root is None:
                res.append(')')
                
        tranverse(t)
        
        return "".join(res[1:-1])

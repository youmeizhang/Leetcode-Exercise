# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        
        def inorderTraversal(root):
            res = []
            if root:
                res = inorderTraversal(root.left) 
                res.append(root.val)
                res = res + inorderTraversal(root.right)
            return res

        res = inorderTraversal(root)
        #print(res)
        res = sorted(res)
        idx_l = res.index(L)
        idx_r = res.index(R)
        
        return sum(res[idx_l:idx_r+1])

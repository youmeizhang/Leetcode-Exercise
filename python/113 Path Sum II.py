# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        
    
        def dfs(root, sum_, ls, res):
            if not root.left and not root.right and sum_ == root.val:
                ls.append(root.val)
                res.append(ls)
            if root.left:
                dfs(root.left, sum_ - root.val, ls + [root.val], res)
            if root.right:
                dfs(root.right, sum_ - root.val, ls + [root.val], res)
        
        res = []  
        if not root:
            return res
        dfs(root, sum_, [], res)
        return res
        

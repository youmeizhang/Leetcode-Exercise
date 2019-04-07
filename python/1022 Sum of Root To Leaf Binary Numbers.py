# credit to: https://leetcode.com/badgergo/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        self.res = 0
        def dfs(root, acc):
            if not root:
                return 
            
            acc = acc * 2 + root.val
            
            if root.left is None and root.right is None:
                self.res += acc
            dfs(root.left, acc)
            dfs(root.right, acc)
        dfs(root, 0)
        return self.res

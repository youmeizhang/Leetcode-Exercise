# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        
        def traverse(root, val):
            if not root: return 0
            res = (val == root.val)
            res += traverse(root.left, val - root.val)
            res += traverse(root.right, val - root.val)
            return res
        if not root: return 0
        ans = traverse(root, sum)
        ans += self.pathSum(root.right, sum)
        ans += self.pathSum(root.left, sum)
        return ans
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum_):
        self.num = 0
        
        def helper(root, target):
            if not root:
                return
            test(root, target)
            helper(root.left, target)
            helper(root.right, target)
        
        def test(root, target):
            if not root:
                return
            if root.val == target:
                self.num += 1
            
            test(root.right, target - root.val)
            test(root.left, target - root.val)
        
        helper(root, sum_)
        
        return self.num
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> int:
        self.res = 0
        path = []
        self.dfs(root, sum_, path)
        return self.res
    
    def dfs(self, root, sum_, path):
        if not root:
            return
        temp = sum_
        path.append(root.val)
        for i in range(len(path)-1, -1, -1):
            temp -= path[i]
            if temp == 0:
                self.res += 1
                
        self.dfs(root.left, sum_, path)
        self.dfs(root.right, sum_, path)
        path.pop()
    
               

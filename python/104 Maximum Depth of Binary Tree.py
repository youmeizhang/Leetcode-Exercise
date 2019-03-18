# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iteration
class Solution(object):
    def maxDepth(self, root):
        stack = []
        
        if root is not None:
            stack.append([1, root])
            
        max_depth = 0
        while stack:
            curr_depth, node = stack.pop()
            
            if node is not None:
                max_depth = max(curr_depth, max_depth)
                stack.append([curr_depth + 1, node.left])
                stack.append([curr_depth + 1, node.right])
        return max_depth
            
        """
        :type root: TreeNode
        :rtype: int
        """
# recursion
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
            
        """
        :type root: TreeNode
        :rtype: int
        """
        

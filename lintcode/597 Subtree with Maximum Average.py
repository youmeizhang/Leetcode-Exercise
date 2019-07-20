"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        self.avg = 0
        self.node = None
        
        def helper(root):
            if not root:
                return 0, 0
            
            left, cnt1 = helper(root.left)
            right, cnt2 = helper(root.right)
            sumRoot = left + right + root.val
            cnt = cnt1 + cnt2 + 1
            avg = sumRoot * 1.0 / cnt
            if self.node is None or avg > self.avg:
                self.avg = avg
                self.node = root
            return sumRoot, cnt
            
        helper(root)
        return self.node

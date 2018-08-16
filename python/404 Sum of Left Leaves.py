class Solution(object):
    def isLeaf(self, root):
        if root.left == None and root.right == None:
            return True
        
    def sumOfLeftLeaves(self, root):
        if root == None:
            return 0
        res = 0
            
        if root.left and self.isLeaf(root.left):
            res += root.left.val
        return res + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

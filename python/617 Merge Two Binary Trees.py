class Solution(object):
    def mergeTrees(self, t1, t2):
        if not t1 and not t2:
            return
        elif not t1:
            return t2
        elif not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
            
        return t1

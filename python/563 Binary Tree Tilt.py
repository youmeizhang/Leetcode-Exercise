class Solution:
    def findTilt(self, root):
        self.res = 0
        def tranverse(root):
            if not root:
                return 0
            l = tranverse(root.left)
            r = tranverse(root.right)
            self.res += abs(l - r)
            return root.val + l + r
        tranverse(root)
        return self.res

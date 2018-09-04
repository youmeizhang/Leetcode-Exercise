class Solution:
    def convertBST(self, root):
        self.sum = 0
        
        def tranverse(root):
            if not root:
                return
            tranverse(root.right)
            root.val += self.sum
            self.sum = root.val
            tranverse(root.left)

        tranverse(root)
        return root

class Solution(object):
    def preorder(self, root):
        res = []
        def preorder(root):
            if root == None:
                return None
            res.append(root.val)
            for child in root.children:
                preorder(child)
        preorder(root)
        return res

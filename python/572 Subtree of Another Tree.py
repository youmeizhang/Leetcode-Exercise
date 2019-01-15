class Solution(object):
    def isSubtree(self, s, t):
        def preorder(root):
            if not root:
                return "$"
            return "#" + str(root.val) + "@" + preorder(root.left) + preorder(root.right)
        
        return preorder(t) in preorder(s)

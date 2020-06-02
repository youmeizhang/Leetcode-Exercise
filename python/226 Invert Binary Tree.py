class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        right = self.invertTree(root.left)
        left = self.invertTree(root.right)
        root.left = left
        root.right = right
        return root

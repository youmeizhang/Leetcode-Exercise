class Solution:
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        
        if not root:
            return '~'
        c = chr(root.val + ord('a'))
        if not root.left and not root.right:
            return c
        
        return min(self.smallestFromLeaf(root.left), self.smallestFromLeaf(root.right)) + c

class Solution:
    def findMode(self, root):
        if not root: return []
        count = collections.defaultdict(int)
        def preorder(root):
            if root:
                count[root.val] += 1
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        max_occ = max(count.values())
        return [e for e in count if count[e] == max_occ]

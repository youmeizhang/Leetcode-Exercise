class Solution:
    def findFrequentTreeSum(self, root):
        if not root: return []
        counter = collections.Counter()
        
        def subTreeSum(root):
            if not root: return 0
            return root.val + subTreeSum(root.left) + subTreeSum(root.right)
        
        def tranverse(root):
            if not root:
                return
            counter[subTreeSum(root)] += 1
            tranverse(root.left)
            tranverse(root.right)
        tranverse(root)
        max_occ = max(counter.values())
        return [e for e in counter if counter[e] == max_occ]

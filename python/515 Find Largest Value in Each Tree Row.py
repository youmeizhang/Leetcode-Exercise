class Solution:
    def largestValues(self, root):
        if not root: return []
        qa, res = [root], []
        while qa:
            maxn = -2147483647 - 1
            qb = []
            for n in qa:
                maxn = max(n.val, maxn)
                if n.left: qb.append(n.left)
                if n.right: qb.append(n.right)
            res.append(maxn)
            qa = qb
        return res

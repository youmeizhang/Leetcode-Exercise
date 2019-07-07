# credit to: https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/discuss/328841/JavaC%2B%2BPython-Several-Ideas

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        depth = cur = 0
        for c in seq:
            if c == "(":
                cur += 1
                depth = max(cur, depth)
        half = depth / 2
        
        n = len(seq)
        res = [0] * n
        cur = 0
        
        for i, c in enumerate(seq):
            if c == '(':
                cur += 1
                if cur > half:
                    res[i] = 1
            else:
                if cur > half:
                    res[i] = 1
                cur -= 1
        return res

class Solution:
    def findContentChildren(self, g, s):
        m = len(g)
        n = len(s)

        g = sorted(g)
        s = sorted(s)

        ans = 0    
        i = m - 1
        j = n - 1
        while(min(i, j) >= 0):
            if g[i] <= s[j]:
                ans += 1
                i -= 1
                j -= 1
            else:
                i -= 1
        return ans

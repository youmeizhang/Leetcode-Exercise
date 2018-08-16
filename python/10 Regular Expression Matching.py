def isMatch(self, s, p):
    if not p:
        return not s
    if p[-1] == "*":
        if s and (s[-1] == p[-2] or p[-2] == "."):
            return self.isMatch(s, p[:-2]) or self.isMatch(s[:-1], p)
        else:
            return self.isMatch(s, p[:-2])
    else:
        if s and (s[-1] == p[-1] or p[-1] == "."):
            return self.isMatch(s[:-1], p[:-1])
        else:
            return False

# DP Solution:
'''
if s[i-1] == p[j-1] or p[j-1] == ".":
    T[i][j] = T[i-1][j-1]
elif p[j-1] == "*":
    T[i][j] = T[i][j-2]
    if s[i-1] == p[j-1] or p[j-1] == ".":
        T[i][j] = T[i][j] or T[i-1][j]
        
else:
    T[i][j] = False
'''

class Solution(object):
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)

        dp = [[False] * (n+1) for x in range(m+1)]
        dp[0][0] = True

        for j in range(2, n+1):
            dp[0][j] = dp[0][j-2] and p[j-1] == "*"

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == "*":
                    dp[i][j] = dp[i][j-2] or dp[i][j-1] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == "."))
                else:
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j - 1] or p[j-1] == ".")
        return dp[-1][-1]

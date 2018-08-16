class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[0] * (n + 1) for x in range(m + 1)]
        for s in strs:
            dic = collections.Counter(s)
            zero = dic['0']
            one = dic['1']
            for x in range(m, zero - 1, -1):
                for y in range(n, one - 1, -1):
                    dp[x][y] = max(dp[x - zero][y - one] + 1, dp[x][y])
        return dp[m][n]

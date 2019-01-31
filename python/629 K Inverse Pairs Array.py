class Solution(object):
    def kInversePairs(self, n, k):
        dp = [[0] * (k+1) for _ in range(n+1)]
        dp[0][0] = 1
        M = 1000000007

        for i in range(n+1):
            for j in range(i):
                for m in range(k+1):
                    if m - j >= 0 and m - j <= k:
                        dp[i][m] = (dp[i][m] + dp[i-1][m-j]) % M

        return dp[n][k]

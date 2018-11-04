class Solution(object):
    def minFallingPathSum(self, A):
        w = len(A[0])
        h = len(A)
        dp = [[0] * (w + 2) for i in range(h)]
        for i in range(h):
            dp[i][0] = dp[i][-1] = float('inf')
            for j in range(1, w+1):
                dp[i][j] = A[i][j-1]
            
        for i in range(1, h):
            for j in range(1, w+1):
                dp[i][j] = A[i][j-1] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
        return min(dp[-1])

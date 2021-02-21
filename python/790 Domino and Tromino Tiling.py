class Solution:
    def numTilings(self, N: int) -> int:
        if N < 2:
            return 1
        dp = [[0] * 2 for _ in range(N+1)]
        
        dp[0][0] = 1
        dp[0][1] = 0
        
        dp[1][0] = 1
        dp[1][1] = 0
        
        mod = 10**9 + 7
        
        for i in range(2, N+1):
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + 2*dp[i-1][1]) % mod
            dp[i][1] = (dp[i-1][1] + dp[i-2][0]) % mod
        
        return dp[-1][0]

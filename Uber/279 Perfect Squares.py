class Solution(object):
    def numSquares(self, n):
        if n <= 0:
            return 0
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            j = 1
            while i - j * j >= 0:
                dp[i] = min(dp[i-j*j]+1, dp[i])
                j += 1
        return dp[-1]
        """
        :type n: int
        :rtype: int
        """
        

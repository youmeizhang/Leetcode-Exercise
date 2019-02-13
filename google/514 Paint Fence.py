class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        # dp[i] = (k - 1) * (dp[i-1] + dp[i-2])
        if k == 1:
            if n > 2:
                return 0
            else:
                return k
            
        dp = [0, k, k*k, 0]
        if n <= 2:
            return dp[n]
        for i in range(2, n):
            dp[3] = (k-1) * (dp[1] + dp[2])
            dp[1] = dp[2]
            dp[2] = dp[3]
        return dp[3]

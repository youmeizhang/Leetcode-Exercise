# memoization method
class Solution(object):
    def climbStairs(self, n):
        memo = [0] * (n+1)
        
        def helper(i, n, memo):
            if i > n:
                return 0
            elif i == n:
                return 1
            elif memo[i] > 0:
                return memo[i]
            
            res = helper(i+1, n, memo) + helper(i+2, n, memo)
            memo[i] = res
            return res
        
        return helper(0, n, memo)
        
        """
        :type n: int
        :rtype: int
        """
        
        
# dynamic programming
class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[-1]
        
        
        """
        :type n: int
        :rtype: int
        """
        

# minimize the maximum cost

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
        return self.cost(1, n, dp)

    def cost(self, left, right, dp):
            if right <= left:
                return 0
            if dp[left][right] != float('inf'):
                return dp[left][right]
            for k in range(left, right+1):
                dp[left][right] = min(dp[left][right], max(self.cost(left, k-1, dp), self.cost(k+1, right, dp))+k)
            return dp[left][right]
                
            

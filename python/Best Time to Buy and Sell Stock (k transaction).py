class Solution(object):
    def maxProfit(self, prices):
        if prices == []:
            return 0
        k = 1
        dp = [[0] * len(prices) for i in range(k+1)]
        for i in range(1,k+1):
            maxdiff = float('-inf') #minimum
            for j in range(len(prices)):
                maxdiff = max(maxdiff, dp[i-1][j] - prices[j])
                dp[i][j] = max(dp[i][j-1], prices[j] + maxdiff)
        return dp[k][len(prices)-1]
    
#Time Limit
class Solution(object):
    def maxProfit(self, k, prices):
        if len(prices) < 2 or k == 0:
            return 0
        dp = [[0] * len(prices) for i in range((k+1))]
        for i in range(1, k+1):
            for j in range(len(prices)):
                for m in range(0, j):
                    dp[i][j] = max(dp[i][j], dp[i][j-1], dp[i-1][m] + prices[j] - prices[m])

        return dp[k][len(prices) - 1]

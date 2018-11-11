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

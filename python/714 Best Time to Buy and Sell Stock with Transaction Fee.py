class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n, lastBuy, lastSold = len(prices), -prices[0], 0
        for i in range(1, n):
            currBuy = max(lastBuy, lastSold - prices[i])
            currSold = max(lastSold, lastBuy + prices[i] - fee)
            lastBuy = currBuy
            lastSold = currSold

        return lastSold
        

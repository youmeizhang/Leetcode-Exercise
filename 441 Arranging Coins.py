class Solution:
    def arrangeCoins(self, n):
        res = math.sqrt(2*n + 1/4) - 1/2
        return int(res)

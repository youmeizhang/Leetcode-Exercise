class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
        n = len(arr)
        dp = [0] * (n+1)
        for i in range(n):
            for j in range(k):
                if i - j >= 0:
                    dp[i+1] = max(dp[i+1], dp[i-j] + (j+1) * max(arr[i-j:i+1]))

        return dp[-1]
        

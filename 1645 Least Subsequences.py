class Solution:
    """
    @param arrayIn: The original array.
    @return: Count the minimum number of subarrays.
    """
    def LeastSubsequences(self, arrayIn):
        # Write your code here.
        dp = [1] * len(arrayIn)
        res = 1
        for i in range(1, len(arrayIn)):
            for j in range(i):
                if arrayIn[i] >= arrayIn[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            
            res = max(res, dp[i])
        return res

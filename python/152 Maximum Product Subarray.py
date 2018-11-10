class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)
        min_dp = [0] * n
        max_dp = [0] * n
        for i in range(n):
            min_dp[i] = nums[i]
            max_dp[i] = nums[i]

        for i in range(1, n):
            max_dp[i] = max(max_dp[i], max_dp[i-1] * nums[i], min_dp[i-1] * nums[i])
            min_dp[i] = min(min_dp[i], min_dp[i-1] * nums[i], max_dp[i-1] * nums[i])

        print(max_dp, min_dp)
        return max(max_dp)

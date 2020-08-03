# credit to: https://leetcode.com/problems/greatest-sum-divisible-by-three/discuss/559999/Come-here-if-you-can't-seem-to-get-it-(Full-Explanation-%2B-uncondensed-code)

class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[0] * 3 for _ in range(n+1)]
        dp[0][1] = float('-inf')
        dp[0][2] = float('-inf')
        for i in range(1, n+1):
            if nums[i-1] % 3 == 0:
                dp[i][0] = max(dp[i-1][0], dp[i-1][0] + nums[i-1])
                dp[i][1] = max(dp[i-1][1], dp[i-1][1] + nums[i-1])
                dp[i][2] = max(dp[i-1][2], dp[i-1][2] + nums[i-1])
            elif nums[i-1] % 3 == 1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][2] + nums[i-1])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] + nums[i-1])
                dp[i][2] = max(dp[i-1][2], dp[i-1][1] + nums[i-1])
            elif nums[i-1] % 3 == 2:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + nums[i-1])
                dp[i][1] = max(dp[i-1][1], dp[i-1][2] + nums[i-1])
                dp[i][2] = max(dp[i-1][2], dp[i-1][0] + nums[i-1])
        return dp[-1][0]
                

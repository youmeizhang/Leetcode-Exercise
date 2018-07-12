class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        n = len(nums)
        if (total % 2) != 0:
            return False

        target = sum(nums) // 2

        dp = [False for i in range(total + 1)]
        dp[0] = True

        for num in nums:
            for i in reversed(range(total)):
                if dp[i]:
                    dp[i + num] = True
            if dp[target]:
                return True
        return False

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        n = len(nums)
        dp[0] = 1
        for i in range(1, target+1):
            total = 0
            for j in range(n):
                if nums[j] <= i:
                    total += dp[i - nums[j]]
            dp[i] = total
        return dp[target]

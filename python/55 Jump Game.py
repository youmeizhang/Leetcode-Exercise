class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n
        for i in range(1, n):
            dp[i] = max(dp[i-1], nums[i-1]) - 1
            if dp[i] < 0:
                return False
        return True
            

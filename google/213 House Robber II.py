class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
            
        def helper(nums):
            n = len(nums)
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
            if n == 2:
                return max(nums)

            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            dp[-1] = 0
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return max(dp)


        return max(helper(nums[1:]), helper(nums[:n-1]))
    
        """
        :type nums: List[int]
        :rtype: int
        """
        

# credit to: https://leetcode.com/problems/target-sum/discuss/97334/Java-(15-ms)-C%2B%2B-(3-ms)-O(ns)-iterative-DP-solution-using-subset-sum-with-explanation

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        
        def helper(nums, s):
            dp = [0] * (s + 1)
            dp[0] = 1
            for n in nums:
                for i in range(s, n-1, -1):
                    dp[i] += dp[i-n]
            return dp[s]
                    
        total = 0
        for i in range(n):
            total += nums[i]
            
        if total < S or (total + S) % 2 > 0:
            return 0
        else:
            return helper(nums, (total + S) / 2)
                    
                
        

# credit to: https://leetcode.com/problems/predict-the-winner/discuss/96829/DP-O(n2)-%2B-MIT-OCW-solution-explanation

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def helper(dp, i, j):
            if i > j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            a = min(helper(dp, i+2, j), helper(dp, i+1, j-1)) + nums[i]
            b = min(helper(dp, i+1, j-1), helper(dp, i, j-2)) + nums[j]
            dp[i][j] = max(a, b)
            return dp[i][j]
        
        n = len(nums)
        if n % 2 == 0:
            return True
    
        dp = [[-1] * n for _ in range(n)]
        res = helper(dp, 0, n-1)
        return 2 * res >= sum(nums)
        
        
            
        

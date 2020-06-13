from copy import copy
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n < 1:
            return []
        res = []
        nums.sort()
        dp = [0] * n
        dp[0] = [nums[0]]
        for i in range(1, n):
            maxSet = []
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    tmp = copy(dp[j])
                    if len(tmp) > len(maxSet):
                        maxSet = tmp
            maxSet.append(nums[i])
            dp[i] = maxSet
        res = []

        for i in range(n):
            if len(dp[i]) > len(res):
                res = dp[i]
        return res
    
        
